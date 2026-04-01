"""MT4 Collector — Full implementation of BaseCollector for MetaTrader 4.

Uses the MT4 Manager API DLL via the ctypes_wrapper.MT4Manager facade.
DLL path and credentials are broker-specific — loaded from config dict at runtime
(sourced from AWS Secrets Manager). Never hardcode DLL path or credentials.

MT4 structural facts baked into this collector:
- TradeRecord.close_time == 0 → open order → raw_mt4_orders
- TradeRecord.close_time > 0  → closed deal → raw_mt4_deals
- Timestamps are Unix seconds (not milliseconds)
- Volume is lots×100
- IP addresses are packed uint32 — unpacked to dotted-decimal by ctypes_wrapper
"""

import hashlib
import json
import time
import uuid
from datetime import datetime, timezone
from typing import Any
from uuid import UUID

import structlog

from shared.base_collector import BaseCollector
from db.ingestion import save_raw_records, log_collector_run, log_collector_error

from .ctypes_wrapper import MT4Manager, unpack_ip

log = structlog.get_logger()


def _ingestion_hash(record: dict) -> str:
    canonical = json.dumps(record, sort_keys=True, default=str)
    return hashlib.sha256(canonical.encode()).hexdigest()[:32]


class MT4Collector(BaseCollector):
    """
    MT4 collector implementing BaseCollector.

    Entities collected:
        accounts → UserRecordsRequest("*")
        orders   → TradeRecordsRequest("*")          [close_time==0]
        deals    → TradeHistoryRequest("*", from, to) [close_time>0]
        symbols  → SymbolsGetAll()
        groups   → GroupsGet()
        online   → OnlineGet()
        margin   → MarginLevelsRequest()
        summary  → SummaryGet()
    """

    source_system = "mt4"

    def __init__(
        self,
        broker_id: UUID,
        server_id: UUID | None,
        connection_id: UUID,
        config: dict,
    ):
        self.broker_id     = broker_id
        self.server_id     = server_id
        self.connection_id = connection_id
        self.config        = config   # {dll_path, server, login, password}
        self.sync_mode     = "incremental"
        self.cursor: str | None = None
        self.last_success_at: datetime | None = None
        self.status        = "disconnected"
        self._manager: MT4Manager | None = None
        self._log = log.bind(
            broker_id=str(broker_id),
            source_system=self.source_system,
            server_id=str(server_id) if server_id else None,
        )

    # ── connect / health ──────────────────────────────────────────────────────

    def connect(self) -> None:
        dll_path = self.config.get("dll_path")
        if not dll_path:
            raise ValueError("dll_path is required in MT4 collector config")

        self._manager = MT4Manager.create(
            dll_path=dll_path,
            server=self.config["server"],
            login=int(self.config["login"]),
            password=self.config["password"],
        )
        self._manager.connect()
        self.status = "connected"
        self._log.info("collector.mt4.connected")

    def health_check(self) -> dict:
        if self._manager is None:
            return {"status": "disconnected"}
        try:
            online = self._manager.get_online()
            return {"status": "connected", "online_sessions": len(online)}
        except Exception as exc:
            self.status = "error"
            return {"status": "error", "error": str(exc)}

    # ── sync modes ────────────────────────────────────────────────────────────

    def bootstrap_sync(self, start_time=None, end_time=None) -> dict:
        self.sync_mode = "bootstrap"
        now = int(time.time())
        from_ts = int(start_time) if start_time else now - 365 * 86400 * 2
        to_ts   = int(end_time)   if end_time   else now

        totals: dict[str, int] = {}
        start = time.monotonic()

        for entity in ("accounts", "symbols", "online", "margin", "summary"):
            try:
                records = self.fetch_entity(entity)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "bootstrap"})

        for entity in ("orders", "deals"):
            try:
                records = self.fetch_entity(entity, from_ts=from_ts, to_ts=to_ts)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "bootstrap"})

        duration_ms = int((time.monotonic() - start) * 1000)
        result = {
            "sync_mode": "bootstrap",
            "records_fetched": sum(totals.values()),
            "records_saved": sum(totals.values()),
            "duration_ms": duration_ms,
            "cursor_to": str(to_ts),
        }
        self.log_run(result)
        self.last_success_at = datetime.now(timezone.utc)
        self.cursor = str(to_ts)
        return result

    def incremental_sync(self, cursor=None) -> dict:
        self.sync_mode = "incremental"
        now = int(time.time())
        from_ts = int(cursor) if cursor else now - 3600
        to_ts = now

        totals: dict[str, int] = {}
        start = time.monotonic()

        for entity in ("accounts", "orders", "online", "margin", "summary"):
            try:
                records = self.fetch_entity(entity)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "incremental"})

        for entity in ("deals",):
            try:
                records = self.fetch_entity(entity, from_ts=from_ts, to_ts=to_ts)
                saved = self.save_raw(entity, records)
                totals[entity] = saved
            except Exception as exc:
                self.handle_error(exc, {"entity": entity, "sync_mode": "incremental"})

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

    # ── fetch_entity ──────────────────────────────────────────────────────────

    def fetch_entity(self, entity_name: str, **kwargs) -> list[dict]:
        m = self._manager
        if m is None:
            raise RuntimeError("Not connected. Call connect() first.")

        from_ts = kwargs.get("from_ts", int(time.time()) - 86400)
        to_ts   = kwargs.get("to_ts",   int(time.time()))

        if entity_name == "accounts":
            return m.get_users_by_group("*")

        elif entity_name == "orders":
            # Open orders: close_time == 0
            trades = m.get_trades_by_group("*")
            return [t for t in trades if t.get("close_time", 0) == 0]

        elif entity_name == "deals":
            # Closed deals: close_time > 0
            history = m.get_history_by_group("*", from_ts, to_ts)
            return [t for t in history if t.get("close_time", 0) > 0]

        elif entity_name == "symbols":
            return m.get_symbols()

        elif entity_name == "online":
            records = m.get_online()
            # Unpack IP from packed uint32
            for rec in records:
                if "ip" in rec and isinstance(rec["ip"], int):
                    rec["ip_str"] = unpack_ip(rec["ip"])
            return records

        elif entity_name == "margin":
            return m.get_margin_levels()

        elif entity_name == "summary":
            return m.get_summary()

        else:
            raise ValueError(f"Unknown entity: {entity_name!r}")

    # ── save_raw ──────────────────────────────────────────────────────────────

    def save_raw(self, entity_name: str, records: list[dict]) -> int:
        if not records:
            return 0

        entity_to_table = {
            "accounts": "raw_mt4_accounts",
            "orders":   "raw_mt4_orders",
            "deals":    "raw_mt4_deals",
            "symbols":  "raw_mt4_symbols",
            "online":   "raw_mt4_online",
            "margin":   "raw_mt4_margin",
            "summary":  "raw_mt4_summary",
        }
        table = entity_to_table.get(entity_name)
        if not table:
            raise ValueError(f"No table mapped for entity: {entity_name!r}")

        now = datetime.now(timezone.utc)
        rows = []
        for rec in records:
            row = {
                "id":             uuid.uuid4(),
                "broker_id":      self.broker_id,
                "server_id":      self.server_id,
                "payload_json":   rec,
                "collected_at":   now,
                "ingestion_hash": _ingestion_hash(rec),
                "status":         "active",
                "created_at":     now,
            }
            row.update(_extract_mt4_fields(entity_name, rec))
            rows.append(row)

        return save_raw_records(table, rows, dedup_columns=_dedup_columns(entity_name))

    # ── log_run / handle_error ────────────────────────────────────────────────

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
            "collector.mt4.error",
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
    return {
        "accounts": ["broker_id", "server_id", "login"],
        "orders":   ["broker_id", "server_id", "order_id"],
        "deals":    ["broker_id", "server_id", "order_id"],
        "symbols":  ["broker_id", "server_id", "symbol"],
        "online":   ["broker_id", "server_id", "login"],
        "margin":   ["broker_id", "server_id", "login"],
        "summary":  ["broker_id", "server_id", "symbol"],
    }.get(entity_name, [])


def _unix_s_to_dt(ts) -> datetime | None:
    if not ts:
        return None
    try:
        return datetime.fromtimestamp(int(ts), tz=timezone.utc)
    except (ValueError, OSError, OverflowError):
        return None


def _extract_mt4_fields(entity_name: str, rec: dict) -> dict:
    if entity_name == "accounts":
        return {
            "login":            rec.get("login"),
            "group":            rec.get("group"),
            "name":             rec.get("name"),
            "email":            rec.get("email"),
            "balance":          rec.get("balance"),
            "credit":           rec.get("credit"),
            "leverage":         rec.get("leverage"),
            "regdate":          _unix_s_to_dt(rec.get("regdate")),
            "lastdate":         _unix_s_to_dt(rec.get("lastdate")),
            "agent_account":    rec.get("agent_account"),
            "country":          rec.get("country"),
            "enable":           rec.get("enable"),
            "source_timestamp": _unix_s_to_dt(rec.get("regdate")),
        }

    elif entity_name in ("orders", "deals"):
        is_deal = entity_name == "deals"
        result = {
            "order_id":         rec.get("order"),
            "login":            rec.get("login"),
            "symbol":           rec.get("symbol"),
            "cmd":              rec.get("cmd"),
            "volume":           rec.get("volume"),
            "open_time":        _unix_s_to_dt(rec.get("open_time")),
            "open_price":       rec.get("open_price"),
            "sl":               rec.get("sl"),
            "tp":               rec.get("tp"),
            "commission":       rec.get("commission"),
            "storage":          rec.get("storage"),
            "profit":           rec.get("profit"),
            "comment":          rec.get("comment"),
            "magic":            rec.get("magic"),
            "source_timestamp": _unix_s_to_dt(rec.get("open_time")),
        }
        if is_deal:
            result["close_time"] = _unix_s_to_dt(rec.get("close_time"))
            result["close_price"] = rec.get("close_price")
            result["reason"] = rec.get("reason")
            result["source_timestamp"] = _unix_s_to_dt(rec.get("close_time"))
        return result

    elif entity_name == "symbols":
        return {
            "symbol":           rec.get("symbol"),
            "description":      rec.get("description"),
            "digits":           rec.get("digits"),
            "contract_size":    rec.get("contract_size"),
            "bid":              rec.get("bid"),
            "ask":              rec.get("ask"),
            "tick_size":        rec.get("tick_size"),
            "tick_value":       rec.get("tick_value"),
            "currency_base":    rec.get("currency_base"),
            "currency_profit":  rec.get("currency_profit"),
        }

    elif entity_name == "online":
        return {
            "login":    rec.get("login"),
            "ip":       rec.get("ip"),
            "ip_str":   rec.get("ip_str"),
            "lastlogin": _unix_s_to_dt(rec.get("lastlogin")),
            "build":    rec.get("build"),
        }

    elif entity_name == "margin":
        return {
            "login":        rec.get("login"),
            "group":        rec.get("group"),
            "balance":      rec.get("balance"),
            "equity":       rec.get("equity"),
            "margin":       rec.get("margin"),
            "margin_free":  rec.get("margin_free"),
            "margin_level": rec.get("margin_level"),
            "profit":       rec.get("profit"),
            "floating":     rec.get("floating"),
            "credit":       rec.get("credit"),
            "orders":       rec.get("orders"),
        }

    elif entity_name == "summary":
        return {
            "symbol":      rec.get("symbol"),
            "count":       rec.get("count"),
            "volume":      rec.get("volume"),
            "volume_buy":  rec.get("volume_buy"),
            "volume_sell": rec.get("volume_sell"),
            "profit":      rec.get("profit"),
            "hedged":      rec.get("hedged"),
            "hedged_buy":  rec.get("hedged_buy"),
            "hedged_sell": rec.get("hedged_sell"),
        }

    return {}
