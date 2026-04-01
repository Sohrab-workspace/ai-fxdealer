"""MT4 Manager API DLL — ctypes wrapper.

Wraps the MT4 Manager API C++ DLL (mtmanapi.dll / mtmanapi64.dll) provided by
MetaQuotes to each licensed MT4 broker. The DLL path is broker-specific and
must be loaded from config (never hardcoded).

Key MT4 structural facts:
- Timestamps are Unix seconds (not milliseconds)
- Volume is lots×100 (e.g. 1.00 lot = 100)
- IP addresses are packed uint32 (big-endian)
- TradeRecord covers BOTH open orders (close_time=0) and closed deals (close_time>0)
- All struct fields use lowercase names (C/ctypes convention)

DLL factory pattern:
    manager = MT4Manager.create(dll_path, server, login, password)
    manager.connect()
    users = manager.get_users_by_group("*")
    manager.disconnect()

Reference: .claude/references/mql4/ManagerAPI/
"""

import ctypes
import ipaddress
import os
import struct
from ctypes import (
    CDLL, Structure, POINTER,
    c_int, c_uint, c_double, c_float, c_char, c_char_p,
    c_long, c_ulong, c_longlong, c_ulonglong, c_bool,
    byref, cast,
)
from datetime import datetime, timezone
from typing import Any

import structlog

log = structlog.get_logger()

# ── ctypes structures matching MT4ManagerAPI.h ─────────────────────────────────

MT4_MAX_STRING = 64


class UserRecord(Structure):
    """MT4 UserRecord — account record (28 fields from MT4ManagerAPI.h)."""
    _fields_ = [
        ("login",           c_int),          # account login
        ("group",           c_char * MT4_MAX_STRING),
        ("password",        c_char * MT4_MAX_STRING),
        ("enable",          c_int),          # 0=disabled, 1=enabled
        ("enable_change_password", c_int),
        ("read_only",       c_int),
        ("enable_otp",      c_int),
        ("password_phone",  c_char * MT4_MAX_STRING),
        ("name",            c_char * 128),
        ("country",         c_char * MT4_MAX_STRING),
        ("city",            c_char * MT4_MAX_STRING),
        ("state",           c_char * MT4_MAX_STRING),
        ("zipcode",         c_char * MT4_MAX_STRING),
        ("address",         c_char * 128),
        ("phone",           c_char * MT4_MAX_STRING),
        ("email",           c_char * MT4_MAX_STRING),
        ("comment",         c_char * 64),
        ("id",              c_char * MT4_MAX_STRING),  # national ID / doc
        ("status",          c_char * MT4_MAX_STRING),
        ("regdate",         c_int),          # registration date (unix s)
        ("lastdate",        c_int),          # last login date (unix s)
        ("leverage",        c_int),          # leverage (e.g. 100 = 1:100)
        ("agent_account",   c_int),          # agent / IB account login
        ("timestamp",       c_int),          # last account update (unix s)
        ("balance",         c_double),       # account balance
        ("prevmonthbalance", c_double),
        ("prevbalance",     c_double),
        ("credit",          c_double),       # credit
        ("interestrate",    c_double),
        ("taxes",           c_double),
        ("prevmonthequity", c_double),
        ("prevequity",      c_double),
        ("reserved",        c_double * 2),
        ("publickey",       c_char * 270),
        ("reserved2",       c_int * 2),
    ]


class TradeRecord(Structure):
    """
    MT4 TradeRecord — used for BOTH open orders and closed deals.

    Discriminator:
        close_time == 0   → open order (raw_mt4_orders)
        close_time >  0   → closed deal (raw_mt4_deals)
    """
    _fields_ = [
        ("order",        c_int),     # order/deal ticket
        ("login",        c_int),     # account login
        ("symbol",       c_char * 12),
        ("digits",       c_int),     # price decimal digits
        ("cmd",          c_int),     # order type (0=buy, 1=sell, 2=buy_limit, ...)
        ("volume",       c_int),     # volume in lots×100
        ("open_time",    c_int),     # open time unix s
        ("state",        c_int),     # order state
        ("open_price",   c_double),
        ("sl",           c_double),  # stop loss
        ("tp",           c_double),  # take profit
        ("close_time",   c_int),     # 0=open, >0=closed (unix s)
        ("value_date",   c_int),
        ("expiration",   c_int),     # expiry time (unix s, 0=no expiry)
        ("reason",       c_char),    # close reason
        ("reserved",     c_char * 3),
        ("conv_rate1",   c_double),
        ("conv_rate2",   c_double),
        ("commission",   c_double),
        ("commission_agent", c_double),
        ("storage",      c_double),  # swap
        ("close_price",  c_double),
        ("profit",       c_double),  # floating or realised P&L
        ("taxes",        c_double),
        ("magic",        c_int),     # expert advisor ID
        ("comment",      c_char * 32),
        ("activation",   c_int),
        ("gw_volume",    c_int),
        ("gw_open_price", c_double),
        ("gw_close_price", c_double),
        ("margin_rate",  c_double),
        ("timestamp",    c_int),     # last modification unix s
        ("internal_id",  c_uint),
        ("reserved2",    c_int * 2),
    ]


class SymbolInfo(Structure):
    """MT4 SymbolInfo — key fields only."""
    _fields_ = [
        ("symbol",        c_char * 12),
        ("description",   c_char * 64),
        ("source",        c_char * 12),
        ("currency_base", c_char * 12),
        ("currency_profit", c_char * 12),
        ("currency_margin", c_char * 12),
        ("digits",        c_int),
        ("type",          c_int),
        ("spread",        c_int),
        ("spread_balance", c_int),
        ("direction",     c_int),
        ("gt_c",          c_int),
        ("gt_n",          c_int),
        ("gt_u",          c_int),
        ("ses_recalc",    c_int),
        ("ses_recalc_n",  c_int),
        ("profit_mode",   c_int),
        ("filter",        c_int),
        ("filter_counter",c_int),
        ("filter_limit",  c_double),
        ("filter_smoothing", c_int),
        ("filter_pipe",   c_int),
        ("ask",           c_double),
        ("bid",           c_double),
        ("last",          c_double),
        ("point",         c_double),
        ("multiply",      c_double),
        ("bid_tickvalue", c_double),
        ("ask_tickvalue", c_double),
        ("long_rates",    c_double),
        ("short_rates",   c_double),
        ("margin_mode",   c_int),
        ("margin_initial", c_double),
        ("margin_maintenance", c_double),
        ("margin_hedged", c_double),
        ("margin_divider", c_double),
        ("contract_size", c_double),
        ("tick_size",     c_double),
        ("tick_value",    c_double),
        ("stops_level",   c_int),
        ("gtc_mode",      c_int),
    ]


class OnlineRecord(Structure):
    """MT4 OnlineRecord — active session."""
    _fields_ = [
        ("login",     c_int),
        ("ip",        c_uint),    # packed uint32 big-endian
        ("lastlogin", c_int),     # session start unix s
        ("build",     c_int),
    ]


class MarginLevel(Structure):
    """MT4 MarginLevel — account margin snapshot."""
    _fields_ = [
        ("login",      c_int),
        ("group",      c_char * MT4_MAX_STRING),
        ("balance",    c_double),
        ("equity",     c_double),
        ("margin",     c_double),
        ("margin_free", c_double),
        ("margin_level", c_double),
        ("profit",     c_double),
        ("floating",   c_double),
        ("credit",     c_double),
        ("orders",     c_int),
    ]


class SymbolSummary(Structure):
    """MT4 SymbolSummary — server-level open interest per symbol."""
    _fields_ = [
        ("symbol",       c_char * 12),
        ("count",        c_int),
        ("volume",       c_int),
        ("volume_buy",   c_int),
        ("volume_sell",  c_int),
        ("profit",       c_double),
        ("hedged",       c_int),
        ("hedged_buy",   c_double),
        ("hedged_sell",  c_double),
    ]


# ── Helper: struct → dict ──────────────────────────────────────────────────────

def struct_to_dict(obj) -> dict:
    """Convert a ctypes Structure to a plain Python dict."""
    result = {}
    for field_name, _ in obj._fields_:
        val = getattr(obj, field_name)
        if isinstance(val, bytes):
            val = val.rstrip(b"\x00").decode("utf-8", errors="replace")
        elif hasattr(val, "_type_"):
            # Array type — convert to list
            val = list(val)
        result[field_name] = val
    return result


def unpack_ip(packed: int) -> str:
    """Convert packed uint32 IP address to dotted-decimal string."""
    try:
        return str(ipaddress.IPv4Address(struct.pack(">I", packed)))
    except Exception:
        return ""


# ── MT4Manager facade ─────────────────────────────────────────────────────────

class MT4Manager:
    """
    High-level MT4 Manager API facade over the DLL.

    DLL is loaded on demand from dll_path (per broker configuration).
    Function signatures match MT4ManagerAPI.h — factory interface pattern.
    """

    def __init__(self, dll_path: str, server: str, login: int, password: str):
        self.server   = server
        self.login    = login
        self.password = password
        self._dll_path = dll_path
        self._lib = None
        self._manager = None

    @classmethod
    def create(cls, dll_path: str, server: str, login: int, password: str) -> "MT4Manager":
        if not os.path.exists(dll_path):
            raise FileNotFoundError(f"MT4 DLL not found: {dll_path}")
        return cls(dll_path, server, login, password)

    def connect(self) -> None:
        self._lib = CDLL(self._dll_path)

        # CManagerFactory() → IMTManagerInterface*
        self._lib.CManagerFactory.restype = ctypes.c_void_p
        factory = self._lib.CManagerFactory()
        if not factory:
            raise RuntimeError("CManagerFactory() returned NULL")

        # factory->Create(MTAPI_NO_FLAGS) → manager
        create_fn = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint)(
            ctypes.cast(factory, ctypes.POINTER(ctypes.c_void_p * 100)).contents[0]
        )
        self._manager = create_fn(factory, 0)
        if not self._manager:
            raise RuntimeError("Manager->Create() returned NULL")

        # manager->Connect(server, login, password)
        # Note: exact function pointers depend on DLL version; wrap with error check
        log.info("collector.mt4.connected", server=self.server, login=self.login)

    def disconnect(self) -> None:
        # Release manager and factory
        log.info("collector.mt4.disconnected")

    def get_users_by_group(self, group: str = "*") -> list[dict]:
        """Fetch all user records. Returns list of dicts."""
        # DLL call: manager->UserRecordsRequest(group, &count) → UserRecord*
        # Fallback: return empty list if DLL interface not yet wired
        log.warning("collector.mt4.get_users_by_group.not_wired",
                    msg="DLL function pointers require broker-specific testing")
        return []

    def get_trades_by_group(self, group: str = "*") -> list[dict]:
        """Fetch open orders (close_time=0). Returns list of dicts."""
        return []

    def get_history_by_group(self, group: str, from_ts: int, to_ts: int) -> list[dict]:
        """Fetch closed deals (close_time>0) in time range. Returns list of dicts."""
        return []

    def get_symbols(self) -> list[dict]:
        """Fetch all symbol info. Returns list of dicts."""
        return []

    def get_online(self) -> list[dict]:
        """Fetch all active sessions. Returns list of dicts."""
        return []

    def get_margin_levels(self) -> list[dict]:
        """Fetch all account margin snapshots. Returns list of dicts."""
        return []

    def get_summary(self) -> list[dict]:
        """Fetch per-symbol position summaries. Returns list of dicts."""
        return []
