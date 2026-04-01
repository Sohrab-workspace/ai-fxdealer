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
from db.ingestion import save_raw_records, log_collector_run, log_collector_error

log = structlog.get_logger()


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
        for entity in ("accounts", "symbols", "groups", "positions", "online", "summary", "exposure"):
            try:
                records = self.fetch_entity(entity)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
                self._log.info("collector.mt5.entity_done", entity=entity, saved=saved)
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "bootstrap"})

        # Time-windowed entities
        for entity in ("deals", "orders"):
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
        for entity in ("accounts", "positions", "online", "summary", "exposure"):
            try:
                records = self.fetch_entity(entity)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "incremental"})

        # Incremental entities (time-windowed from cursor)
        for entity in ("deals", "orders"):
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

        else:
            raise ValueError(f"Unknown entity: {entity_name!r}")

    # ── BaseCollector: save_raw ───────────────────────────────────────────────

    def save_raw(self, entity_name: str, records: list[dict]) -> int:
        if not records:
            return 0

        entity_to_table = {
            "accounts":  "raw_mt5_accounts",
            "deals":     "raw_mt5_deals",
            "orders":    "raw_mt5_orders",
            "positions": "raw_mt5_positions",
            "symbols":   "raw_mt5_symbols",
            "groups":    "raw_mt5_groups",
            "online":    "raw_mt5_online",
            "summary":   "raw_mt5_summary",
            "exposure":  "raw_mt5_exposure",
        }
        table = entity_to_table.get(entity_name)
        if not table:
            raise ValueError(f"No table mapped for entity: {entity_name!r}")

        now = datetime.now(timezone.utc)
        rows = []
        for rec in records:
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
        "accounts":  ["broker_id", "server_id", "login"],
        "deals":     ["broker_id", "server_id", "deal_id"],
        "orders":    ["broker_id", "server_id", "order_id"],
        "positions": ["broker_id", "server_id", "position_id"],
        "symbols":   ["broker_id", "server_id", "symbol"],
        "groups":    ["broker_id", "server_id", "group"],
        "online":    ["broker_id", "server_id", "session_id"],
        "summary":   ["broker_id", "server_id", "symbol"],
        "exposure":  ["broker_id", "server_id", "symbol"],
    }.get(entity_name, [])


def _extract_mt5_fields(entity_name: str, rec: dict) -> dict:
    """Extract typed columns from raw MT5 dict for indexing."""
    _ts = _unix_ms_to_dt

    if entity_name == "accounts":
        return {
            "login":               rec.get("Login"),
            "group":               rec.get("Group"),
            "name":                rec.get("Name"),
            "email":               rec.get("EMail"),
            "balance":             rec.get("Balance"),
            "credit":              rec.get("Credit"),
            "leverage":            rec.get("Leverage"),
            "registration":        _unix_s_to_dt(rec.get("Registration")),
            "last_access":         _unix_s_to_dt(rec.get("LastAccess")),
            "last_ip":             rec.get("LastIP"),
            "country":             rec.get("Country"),
            "status":              rec.get("Status"),
            "rights":              rec.get("Rights"),
            "agent":               rec.get("Agent"),
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
            "price_sl":         rec.get("PriceSL"),
            "price_tp":         rec.get("PriceTP"),
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
            "price_sl":         rec.get("PriceSL"),
            "price_tp":         rec.get("PriceTP"),
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
            "volume_min":       rec.get("VolumeMin"),
            "volume_max":       rec.get("VolumeMax"),
            "volume_step":      rec.get("VolumeStep"),
            "tick_size":        rec.get("TickSize"),
            "tick_value":       rec.get("TickValue"),
            "currency_base":    rec.get("CurrencyBase"),
            "currency_profit":  rec.get("CurrencyProfit"),
            "currency_margin":  rec.get("CurrencyMargin"),
        }

    elif entity_name == "groups":
        return {
            "group":            rec.get("Group"),
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
            "symbol":   rec.get("Symbol"),
            "buy":      rec.get("Buy"),
            "sell":     rec.get("Sell"),
            "buy_volume":  rec.get("BuyVolume"),
            "sell_volume": rec.get("SellVolume"),
            "buy_profit":  rec.get("BuyProfit"),
            "sell_profit": rec.get("SellProfit"),
        }

    elif entity_name == "exposure":
        return {
            "symbol":      rec.get("Symbol"),
            "buy_volume":  rec.get("BuyVolume"),
            "sell_volume": rec.get("SellVolume"),
            "buy_profit":  rec.get("BuyProfit"),
            "sell_profit": rec.get("SellProfit"),
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
