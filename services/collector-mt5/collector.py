"""MT5 Collector — Full implementation of BaseCollector for MetaTrader 5.

Uses the official MT5Manager pip package (MetaQuotes Python SDK).
Connects as a Manager (not a trading account) via MT5Manager.ManagerAPI().

Credentials are loaded from config dict (sourced from AWS Secrets Manager at runtime).
Never hardcode server/login/password here.

MT5Manager returns typed objects (MTUser, MTDeal, etc.) — this module serializes
them to plain dicts before passing to save_raw / payload_json storage.

Connection model: one MT5Collector instance per broker per server.
"""

import hashlib
import json
import time
import uuid
from datetime import datetime, timezone
from typing import Any
from uuid import UUID

import structlog

import MT5Manager

from shared.base_collector import BaseCollector
from db.ingestion import save_raw_records, save_tick_records, log_collector_run, log_collector_error

log = structlog.get_logger()


# ── Unicode surrogate sanitizer ───────────────────────────────────────────────

import re as _re
_SURROGATE_RE = _re.compile(r'[\ud800-\udfff]')

def _sanitize(obj):
    """Recursively replace lone Unicode surrogates with U+FFFD.

    MT5 servers can return strings (names, addresses) containing lone UTF-16
    surrogate code points (e.g. \\ud8da). PostgreSQL rejects these as invalid
    JSON. Replace them with the Unicode replacement character so the payload
    stores cleanly without data loss elsewhere in the record.
    """
    if isinstance(obj, str):
        return _SURROGATE_RE.sub('\ufffd', obj)
    elif isinstance(obj, dict):
        return {k: _sanitize(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [_sanitize(v) for v in obj]
    return obj


# ── MT5 object → dict serializer ─────────────────────────────────────────────

def _mt5_to_dict(obj) -> dict:
    """Convert any MT5Manager typed object to a plain serializable dict."""
    if obj is None:
        return {}
    result = {}
    for attr in dir(obj):
        if attr.startswith("_"):
            continue
        val = getattr(obj, attr)
        if callable(val):
            continue
        # Recurse for nested MT5 objects
        if hasattr(val, "__class__") and val.__class__.__module__ == "MT5Manager":
            result[attr] = _mt5_to_dict(val)
        elif isinstance(val, (list, tuple)):
            result[attr] = [
                _mt5_to_dict(item) if hasattr(item, "__class__") and item.__class__.__module__ == "MT5Manager"
                else item
                for item in val
            ]
        else:
            result[attr] = val
    return result


def _ingestion_hash(record: dict) -> str:
    """Stable SHA-256 hash of the record payload for deduplication."""
    canonical = json.dumps(record, sort_keys=True, default=str)
    return hashlib.sha256(canonical.encode()).hexdigest()[:32]


# ── MT5Collector ─────────────────────────────────────────────────────────────

class MT5Collector(BaseCollector):
    """
    Full MT5 collector implementing BaseCollector.

    Entities collected:
        accounts   → UserRequestByGroup("*")
        deals      → DealRequestByGroup("*", from_ts, to_ts)
        orders     → HistoryRequestByGroup("*", from_ts, to_ts)  [historical]
        positions  → PositionGetByGroup("*")
        symbols    → SymbolGetArray()
        groups     → GroupRequestArray()
        online     → OnlineGetArray()
        summary    → SummaryGetAll()
        exposure   → ExposureGetAll()
    """

    # ── Required collector metadata ───────────────────────────────────────────
    source_system = "mt5"

    def __init__(
        self,
        broker_id: UUID,
        server_id: UUID | None,
        connection_id: UUID,
        config: dict,
    ):
        self.broker_id = broker_id
        self.server_id = server_id
        self.connection_id = connection_id
        self.config = config           # {server, login, password, ...}
        self.sync_mode = "incremental"
        self.cursor: str | None = None
        self.last_success_at: datetime | None = None
        self.status = "disconnected"
        self._manager: MT5Manager.ManagerAPI | None = None
        self._log = log.bind(
            broker_id=str(broker_id),
            source_system=self.source_system,
            server_id=str(server_id) if server_id else None,
            connection_id=str(connection_id),
        )

    # ── BaseCollector: connect / health ──────────────────────────────────────

    def connect(self) -> None:
        server = self.config["server"]
        login = int(self.config["login"])
        password = self.config["password"]

        self._manager = MT5Manager.ManagerAPI()
        result = self._manager.Connect(server, login, password)

        if not result:
            self.status = "error"
            raise ConnectionError(
                f"MT5Manager.Connect failed for server={server} login={login}"
            )

        self.status = "connected"
        self._log.info("collector.mt5.connected", server=server, login=login)

    def health_check(self) -> dict:
        if self._manager is None:
            return {"status": "disconnected"}
        try:
            time_obj = self._manager.TimeGet()
            return {
                "status": "connected",
                "server": self.config.get("server"),
                "server_time": getattr(time_obj, "Time", None),
            }
        except Exception as exc:
            self.status = "error"
            return {"status": "error", "error": str(exc)}

    # ── BaseCollector: sync modes ─────────────────────────────────────────────

    def bootstrap_sync(self, start_time=None, end_time=None) -> dict:
        self.sync_mode = "bootstrap"
        now = int(time.time())
        from_ts = int(start_time) if start_time else now - 365 * 86400 * 2  # 2yr default
        to_ts = int(end_time) if end_time else now

        totals: dict[str, int] = {}
        start = time.monotonic()

        # Static entities first (no time window)
        for entity in ("accounts", "symbols", "groups", "positions", "online", "summary", "exposure", "ticks"):
            try:
                records = self.fetch_entity(entity)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
                self._log.info("collector.mt5.entity_done", entity=entity, saved=saved)
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "bootstrap"})

        # Time-windowed entities
        for entity in ("deals", "orders", "server_logs"):
            try:
                records = self.fetch_entity(entity, from_ts=from_ts, to_ts=to_ts)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
                self._log.info("collector.mt5.entity_done", entity=entity, saved=saved)
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "bootstrap"})

        duration_ms = int((time.monotonic() - start) * 1000)
        result = {
            "sync_mode": "bootstrap",
            "records_fetched": sum(totals.values()),
            "records_saved": sum(totals.values()),
            "duration_ms": duration_ms,
            "cursor_to": str(to_ts),
            "entities": totals,
        }
        self.log_run(result)
        self.last_success_at = datetime.now(timezone.utc)
        self.cursor = str(to_ts)
        return result

    def incremental_sync(self, cursor=None) -> dict:
        self.sync_mode = "incremental"
        now = int(time.time())
        from_ts = int(cursor) if cursor else now - 3600  # default: last 1hr
        to_ts = now

        totals: dict[str, int] = {}
        start = time.monotonic()

        # Snapshot entities (always re-fetch full set)
        for entity in ("accounts", "positions", "online", "summary", "exposure", "ticks"):
            try:
                records = self.fetch_entity(entity)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "incremental"})

        # Incremental entities (time-windowed from cursor)
        for entity in ("deals", "orders", "server_logs"):
            try:
                records = self.fetch_entity(entity, from_ts=from_ts, to_ts=to_ts)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "incremental", "cursor": cursor})

        duration_ms = int((time.monotonic() - start) * 1000)
        result = {
            "sync_mode": "incremental",
            "records_fetched": sum(totals.values()),
            "records_saved": sum(totals.values()),
            "duration_ms": duration_ms,
            "cursor_from": str(from_ts),
            "cursor_to": str(to_ts),
        }
        self.log_run(result)
        self.last_success_at = datetime.now(timezone.utc)
        self.cursor = str(to_ts)
        return result

    # ── BaseCollector: fetch_entity ───────────────────────────────────────────

    def fetch_entity(self, entity_name: str, **kwargs) -> list[dict]:
        m = self._manager
        if m is None:
            raise RuntimeError("Not connected. Call connect() first.")

        from_ts = kwargs.get("from_ts", int(time.time()) - 86400)
        to_ts   = kwargs.get("to_ts",   int(time.time()))

        if entity_name == "accounts":
            objs = m.UserRequestByGroup("*") or []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "deals":
            objs = m.DealRequestByGroup("*", from_ts, to_ts) or []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "orders":
            # HistoryRequest covers completed orders; OrderGetByGroup covers pending
            history = m.HistoryRequestByGroup("*", from_ts, to_ts) or []
            pending = m.OrderGetByGroup("*") or []
            return [_mt5_to_dict(o) for o in history + pending]

        elif entity_name == "positions":
            objs = m.PositionGetByGroup("*") or []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "symbols":
            objs = m.SymbolGetArray() or []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "groups":
            objs = m.GroupRequestArray() or []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "online":
            objs = m.OnlineGetArray() or []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "summary":
            objs = m.SummaryGetAll() or []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "exposure":
            objs = m.ExposureGetAll() or []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "server_logs":
            # ManagerAPI.LoggerServerRequest(mode, type, from, to, filter) → [MTLogRecordPy]
            # mode=0 (MTLogModeStd), type=0 (MTLogTypeAll = all events), filter="" (no filter)
            # MTLogRecord fields: flags, code, type, datetime (unix s), source, message, datetime_msc
            objs = m.LoggerServerRequest(0, 0, from_ts, to_ts, "") or []
            if not isinstance(objs, (list, tuple)):
                objs = []
            return [_mt5_to_dict(o) for o in objs]

        elif entity_name == "ticks":
            # Get current last tick for every symbol via TickLast(symbol).
            # MTTick payload fields (lowercase): ask, bid, datetime, datetime_msc,
            # flags, last, volume, volume_ext.  Symbol is NOT in MTTick — inject as _symbol.
            sym_objs = m.SymbolGetArray() or []
            ticks = []
            for sym_obj in sym_objs:
                sym_dict = _mt5_to_dict(sym_obj)
                symbol = sym_dict.get("Symbol", "")
                if not symbol:
                    continue
                try:
                    tick_obj = m.TickLast(symbol)
                    if tick_obj:
                        tick_dict = _mt5_to_dict(tick_obj)
                        tick_dict["_symbol"] = symbol
                        ticks.append(tick_dict)
                except Exception:
                    pass
            return ticks

        else:
            raise ValueError(f"Unknown entity: {entity_name!r}")

    # ── BaseCollector: save_raw ───────────────────────────────────────────────

    def save_raw(self, entity_name: str, records: list[dict]) -> int:
        if not records:
            return 0

        entity_to_table = {
            "accounts":    "raw_mt5_accounts",
            "deals":       "raw_mt5_deals",
            "orders":      "raw_mt5_orders",
            "positions":   "raw_mt5_positions",
            "symbols":     "raw_mt5_symbols",
            "groups":      "raw_mt5_groups",
            "online":      "raw_mt5_online",
            "summary":     "raw_mt5_summary",
            "exposure":    "raw_mt5_exposure",
            "server_logs": "raw_mt5_server_logs",
            "ticks":       "raw_mt5_ticks",
        }
        table = entity_to_table.get(entity_name)
        if not table:
            raise ValueError(f"No table mapped for entity: {entity_name!r}")

        now = datetime.now(timezone.utc)

        # Ticks are append-only: no status, ingestion_hash, or superseding
        if entity_name == "ticks":
            rows = []
            for rec in records:
                rec = _sanitize(rec)
                row = {
                    "id":           uuid.uuid4(),
                    "broker_id":    self.broker_id,
                    "server_id":    self.server_id,
                    "payload_json": rec,
                    "collected_at": now,
                }
                row.update(_extract_mt5_fields("ticks", rec))
                rows.append(row)
            return save_tick_records(table, rows)

        rows = []
        for rec in records:
            rec = _sanitize(rec)
            row = {
                "id":              uuid.uuid4(),
                "broker_id":       self.broker_id,
                "server_id":       self.server_id,
                "payload_json":    rec,
                "collected_at":    now,
                "ingestion_hash":  _ingestion_hash(rec),
                "status":          "active",
                "created_at":      now,
            }
            row.update(_extract_mt5_fields(entity_name, rec))
            rows.append(row)

        return save_raw_records(table, rows, dedup_columns=_dedup_columns(entity_name))

    # ── BaseCollector: log_run / handle_error ─────────────────────────────────

    def log_run(self, result: dict) -> None:
        log_collector_run({
            "broker_id":       self.broker_id,
            "source_system":   self.source_system,
            "connection_id":   self.connection_id,
            "server_id":       self.server_id,
            "sync_mode":       result.get("sync_mode", self.sync_mode),
            "status":          "success",
            "records_fetched": result.get("records_fetched", 0),
            "records_saved":   result.get("records_saved", 0),
            "duration_ms":     result.get("duration_ms"),
            "cursor_from":     result.get("cursor_from"),
            "cursor_to":       result.get("cursor_to"),
            "collected_at":    datetime.now(timezone.utc),
        })

    def handle_error(self, error: Exception, context: dict) -> None:
        self._log.error(
            "collector.mt5.error",
            error=str(error),
            error_type=type(error).__name__,
            **{k: str(v) for k, v in context.items()},
        )
        log_collector_error({
            "broker_id":     self.broker_id,
            "source_system": self.source_system,
            "connection_id": self.connection_id,
            "server_id":     self.server_id,
            "error_type":    type(error).__name__,
            "error_message": str(error),
            "context_json":  context,
            "collected_at":  datetime.now(timezone.utc),
        })


# ── Field extraction helpers ──────────────────────────────────────────────────

def _dedup_columns(entity_name: str) -> list[str]:
    """Columns used for the partial unique index (WHERE status = 'active')."""
    return {
        "accounts":    ["broker_id", "server_id", "login"],
        "deals":       ["broker_id", "server_id", "deal_id"],
        "orders":      ["broker_id", "server_id", "order_id"],
        "positions":   ["broker_id", "server_id", "position_id"],
        "symbols":     ["broker_id", "server_id", "symbol"],
        "groups":      ["broker_id", "server_id", "group_name"],
        "online":      ["broker_id", "server_id", "session_id"],
        "summary":     ["broker_id", "server_id", "symbol"],
        "exposure":    ["broker_id", "server_id", "symbol"],
        "server_logs": [],  # no unique key — cursor-based collection prevents re-fetch
        "ticks":       [],  # append-only hypertable
    }.get(entity_name, [])


def _extract_mt5_fields(entity_name: str, rec: dict) -> dict:
    """Extract typed columns from raw MT5 dict for indexing."""
    _ts = _unix_ms_to_dt

    if entity_name == "accounts":
        return {
            "login":               rec.get("Login"),
            "group_name":          rec.get("Group"),          # schema col is group_name
            "name":                rec.get("Name"),
            "balance":             rec.get("Balance"),
            "credit":              rec.get("Credit"),
            "leverage":            rec.get("Leverage"),
            "registration":        rec.get("Registration"),   # BigInteger (unix seconds)
            "last_access":         rec.get("LastAccess"),     # BigInteger (unix seconds)
            "last_ip":             rec.get("LastIP"),
            "country":             rec.get("Country"),
            "rights":              rec.get("Rights"),
            "source_timestamp":    _unix_s_to_dt(rec.get("Registration")),
        }

    elif entity_name == "deals":
        return {
            "deal_id":          rec.get("Deal"),
            "login":            rec.get("Login"),
            "symbol":           rec.get("Symbol"),
            "action":           rec.get("Action"),
            "entry":            rec.get("Entry"),
            "order_id":         rec.get("Order"),
            "position_id":      rec.get("PositionID"),
            "volume":           rec.get("Volume"),
            "price":            rec.get("Price"),
            "profit":           rec.get("Profit"),
            "commission":       rec.get("Commission"),
            "storage":          rec.get("Storage"),
            "time_msc":         rec.get("TimeMsc"),
            "source_timestamp": _ts(rec.get("TimeMsc")),
        }

    elif entity_name == "orders":
        return {
            "order_id":         rec.get("Order"),
            "login":            rec.get("Login"),
            "symbol":           rec.get("Symbol"),
            "type":             rec.get("Type"),
            "state":            rec.get("State"),
            "volume_initial":   rec.get("VolumeInitial"),
            "volume_current":   rec.get("VolumeCurrent"),
            "price_order":      rec.get("PriceOrder"),
            "position_id":      rec.get("PositionID"),
            "time_setup_msc":   rec.get("TimeSetupMsc"),
            "source_timestamp": _ts(rec.get("TimeSetupMsc")),
        }

    elif entity_name == "positions":
        return {
            "position_id":      rec.get("Position"),
            "login":            rec.get("Login"),
            "symbol":           rec.get("Symbol"),
            "action":           rec.get("Action"),
            "volume":           rec.get("Volume"),
            "price_open":       rec.get("PriceOpen"),
            "price_current":    rec.get("PriceCurrent"),
            "profit":           rec.get("Profit"),
            "storage":          rec.get("Storage"),
            "time_create_msc":  rec.get("TimeCreateMsc"),
            "source_timestamp": _ts(rec.get("TimeCreateMsc")),
        }

    elif entity_name == "symbols":
        return {
            "symbol":           rec.get("Symbol"),
            "description":      rec.get("Description"),
            "digits":           rec.get("Digits"),
            "contract_size":    rec.get("ContractSize"),
            "currency_base":    rec.get("CurrencyBase"),
            "currency_profit":  rec.get("CurrencyProfit"),
            "currency_margin":  rec.get("CurrencyMargin"),
        }

    elif entity_name == "groups":
        return {
            "group_name":       rec.get("Group"),   # schema col is group_name
            "currency":         rec.get("Currency"),
            "margin_call":      rec.get("MarginCall"),
            "margin_stop_out":  rec.get("MarginStopOut"),
        }

    elif entity_name == "online":
        return {
            "login":      rec.get("Login"),
            "session_id": rec.get("SessionID"),
            "address":    rec.get("Address"),
            "build":      rec.get("Build"),
            "computer_id": rec.get("ComputerID"),
            "group":      rec.get("Group"),
            "time":       rec.get("Time"),
            "type":       rec.get("Type"),
        }

    elif entity_name == "summary":
        return {
            "symbol":                  rec.get("Symbol"),
            "digits":                  rec.get("Digits"),
            "position_clients":        rec.get("PositionClients"),
            "profit_clients":          rec.get("ProfitClients"),
            "profit_full_clients":     rec.get("ProfitFullClients"),
            "profit_uncovered":        rec.get("ProfitUncovered"),
            "profit_uncovered_full":   rec.get("ProfitUncoveredFull"),
            "volume_buy_clients":      rec.get("VolumeBuyClients"),
            "volume_sell_clients":     rec.get("VolumeSellClients"),
            "volume_buy_clients_ext":  rec.get("VolumeBuyClientsExt"),
            "volume_sell_clients_ext": rec.get("VolumeSellClientsExt"),
            "volume_net":              rec.get("VolumeNet"),
        }

    elif entity_name == "exposure":
        return {
            "symbol":          rec.get("Symbol"),
            "digits":          rec.get("Digits"),
            "price_rate":      rec.get("PriceRate"),
            "volume_clients":  rec.get("VolumeClients"),
            "volume_coverage": rec.get("VolumeCoverage"),
            "volume_net":      rec.get("VolumeNet"),
        }

    elif entity_name == "server_logs":
        # MTLogRecord fields (from MT5Manager Python SDK):
        #   flags (UINT), code (UINT/EnMTLogCode), type (INT/EnMTLogType),
        #   datetime (INT64 unix s), source (wchar str), message (wchar str),
        #   datetime_msc (INT64 unix ms)
        # _mt5_to_dict() returns lowercase attribute names from the Python object.
        time_s = rec.get("datetime")
        return {
            "log_time":       _unix_s_to_dt(time_s),
            "category":       rec.get("type"),      # EnMTLogType (event category)
            "code":           rec.get("code"),      # EnMTLogCode (severity: 0=info,2=err,4=login)
            "message":        rec.get("message"),
            # login, ip_address, computer_id populated later by log_parser.py
            "login":          None,
            "ip_address":     None,
            "computer_id":    None,
            "is_login_event": False,
        }

    elif entity_name == "ticks":
        # MTTick payload uses lowercase keys: ask, bid, datetime, datetime_msc,
        # flags, last, volume, volume_ext.  _symbol is injected by fetch_entity.
        return {
            "symbol":           rec.get("_symbol"),
            "ask":              rec.get("ask"),
            "bid":              rec.get("bid"),
            "last":             rec.get("last"),
            "volume":           rec.get("volume"),
            "datetime_msc":     rec.get("datetime_msc"),
            "source_timestamp": _unix_ms_to_dt(rec.get("datetime_msc")),
        }

    return {}


def _unix_ms_to_dt(ts_ms) -> datetime | None:
    if ts_ms is None:
        return None
    try:
        return datetime.fromtimestamp(int(ts_ms) / 1000, tz=timezone.utc)
    except (ValueError, OSError, OverflowError):
        return None


def _unix_s_to_dt(ts_s) -> datetime | None:
    if ts_s is None:
        return None
    try:
        return datetime.fromtimestamp(int(ts_s), tz=timezone.utc)
    except (ValueError, OSError, OverflowError):
        return None
