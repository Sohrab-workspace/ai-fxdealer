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

DLL factory pattern (corrected — CManagerFactory is NOT a DLL export):
    DLL exports exactly two C functions:
      MtManVersion() → int
      MtManCreate(int version, CManagerInterface**) → int

    MT4Manager wraps these two C functions directly:
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
    c_short, c_ushort,
    c_long, c_ulong, c_longlong, c_ulonglong, c_bool, c_void_p,
    byref, cast, CFUNCTYPE,
)
from datetime import datetime, timezone
from typing import Any

import structlog

log = structlog.get_logger()

# ── DLL version constant ───────────────────────────────────────────────────────
# MAKELONG(ManAPIProgramBuild=1440, ManAPIProgramVersion=400)
# = (ManAPIProgramVersion << 16) | ManAPIProgramBuild
# = (400 << 16) | 1440 = 26215840
_MAN_API_VERSION = (400 << 16) | 1440  # 26215840

# MT4 return code for success
_RET_OK = 0

# ── ctypes structures matching MT4ManagerAPI.h ─────────────────────────────────

MT4_MAX_STRING = 64


class UserRecord(Structure):
    """
    MT4 UserRecord — account record (MT4ManagerAPI.h).
    Default packing (no #pragma pack around this struct).
    Size = 1120 bytes (includes 4-byte alignment pad before balance).

    Field sizes verified against MT4ManagerAPI.h lines 924-976.
    """
    _fields_ = [
        ("login",                  c_int),          # account login
        ("group",                  c_char * 16),    # group name
        ("password",               c_char * 16),    # password hash
        ("enable",                 c_int),          # 0=disabled, 1=enabled
        ("enable_change_password", c_int),
        ("enable_read_only",       c_int),          # TRUE = may not trade
        ("enable_otp",             c_int),
        ("enable_reserved",        c_int * 2),      # for future use
        ("password_investor",      c_char * 16),    # read-only password
        ("password_phone",         c_char * 32),    # phone password
        ("name",                   c_char * 128),   # client name
        ("country",                c_char * 32),
        ("city",                   c_char * 32),
        ("state",                  c_char * 32),
        ("zipcode",                c_char * 16),
        ("address",                c_char * 96),
        ("lead_source",            c_char * 32),
        ("phone",                  c_char * 32),
        ("email",                  c_char * 48),
        ("comment",                c_char * 64),
        ("id",                     c_char * 32),    # SSN / national ID
        ("status",                 c_char * 16),
        ("regdate",                c_int),          # registration unix timestamp
        ("lastdate",               c_int),          # last connection unix timestamp
        ("leverage",               c_int),          # leverage (e.g. 100 = 1:100)
        ("agent_account",          c_int),          # agent / IB login
        ("timestamp",              c_int),          # last update unix timestamp
        ("last_ip",                c_int),          # last connection IP (packed int)
        # NOTE: ctypes auto-inserts 4-byte pad here for double alignment (default packing)
        ("balance",                c_double),
        ("prevmonthbalance",       c_double),
        ("prevbalance",            c_double),
        ("credit",                 c_double),
        ("interestrate",           c_double),
        ("taxes",                  c_double),
        ("prevmonthequity",        c_double),
        ("prevequity",             c_double),
        ("reserved2",              c_double * 2),
        ("otp_secret",             c_char * 32),
        ("secure_reserved",        c_char * 240),
        ("send_reports",           c_int),
        ("mqid",                   c_uint),         # MQ client ID
        ("user_color",             c_uint),         # COLORREF display color
        ("unused",                 c_char * 40),
        ("api_data",               c_char * 16),
    ]


class TradeRecord(Structure):
    """
    MT4 TradeRecord — used for BOTH open orders and closed deals.
    #pragma pack(push,1) — NO alignment padding.
    Size = 224 bytes.

    Field layout verified against MT4ManagerAPI.h lines 1015-1051.

    Discriminator:
        close_time == 0   → open order (raw_mt4_orders)
        close_time >  0   → closed deal (raw_mt4_deals)
    """
    _pack_ = 1   # matches #pragma pack(push,1) in MT4ManagerAPI.h

    _fields_ = [
        ("order",             c_int),     # order/deal ticket
        ("login",             c_int),     # account login
        ("symbol",            c_char * 12),
        ("digits",            c_int),     # price decimal digits
        ("cmd",               c_int),     # OP_BUY=0, OP_SELL=1, ..., OP_BALANCE=6
        ("volume",            c_int),     # volume in lots×100
        ("open_time",         c_int),     # open time unix s (__time32_t)
        ("state",             c_int),     # TS_OPEN_NORMAL etc.
        ("open_price",        c_double),  # no alignment pad (pack=1)
        ("sl",                c_double),  # stop loss
        ("tp",                c_double),  # take profit
        ("close_time",        c_int),     # 0=open, >0=closed (unix s)
        ("gw_volume",         c_int),     # gateway order volume
        ("expiration",        c_int),     # pending expiry unix s (0=GTC)
        ("reason",            c_char),    # TR_REASON_CLIENT=0, TR_REASON_DEALER=2, ...
        ("conv_reserv",       c_char * 3),
        ("conv_rates",        c_double * 2),  # profit→deposit rate at open/close
        ("commission",        c_double),
        ("commission_agent",  c_double),
        ("storage",           c_double),  # accrued swap
        ("close_price",       c_double),
        ("profit",            c_double),  # floating or realised P&L
        ("taxes",             c_double),
        ("magic",             c_int),     # EA magic number
        ("comment",           c_char * 32),
        ("gw_order",          c_int),     # gateway order ticket
        ("activation",        c_int),
        ("gw_open_price",     c_short),   # gateway price deviation pips (short!)
        ("gw_close_price",    c_short),   # gateway price deviation pips (short!)
        ("margin_rate",       c_double),  # margin currency → deposit currency rate
        ("timestamp",         c_int),     # last modification unix s
        ("api_data",          c_int * 4), # for API usage
        ("next",              c_uint),    # __ptr32 internal linked list (32-bit ptr)
    ]


class OnlineRecord(Structure):
    """
    MT4 OnlineRecord — active connected session.
    Default packing (no #pragma pack around this struct).
    Size = 32 bytes.

    Field layout verified against MT4ManagerAPI.h lines 1001-1008.
    """
    _fields_ = [
        ("counter",   c_int),    # connections counter
        ("reserved",  c_int),    # reserved
        ("login",     c_int),    # user login
        ("ip",        c_uint),   # connection IP address (packed uint32)
        ("group",     c_char * 16),  # user group
    ]


class ReportGroupRequest(Structure):
    """
    MT4 ReportGroupRequest — used with ReportsRequest batch history fetch.
    #pragma pack(push,1) — NO alignment padding.
    Size = 44 bytes.

    Field layout verified against MT4ManagerAPI.h lines 1243-1250.
    """
    _pack_ = 1
    _fields_ = [
        ("name",    c_char * 32),  # request group name (can be empty)
        ("from_ts", c_int),        # from __time32_t
        ("to_ts",   c_int),        # to   __time32_t
        ("total",   c_int),        # count of logins in the logins array
    ]


class MarginLevel(Structure):
    """MT4 MarginLevel — account margin snapshot."""
    _fields_ = [
        ("login",        c_int),
        ("group",        c_char * MT4_MAX_STRING),
        ("balance",      c_double),
        ("equity",       c_double),
        ("margin",       c_double),
        ("margin_free",  c_double),
        ("margin_level", c_double),
        ("profit",       c_double),
        ("floating",     c_double),
        ("credit",       c_double),
        ("orders",       c_int),
    ]


class ServerLog(Structure):
    """
    MT4 ServerLog — one server log entry.
    Default packing (no #pragma pack).
    Size = 796 bytes (4 + 24 + 256 + 512).

    Field layout from MT4ManagerAPI.h:
        int  code;       // EnErrLogTypes (0=standard, 1=logins, 2=trades, 3=errors, 4=full)
        char time[24];   // formatted time string "YYYY.MM.DD HH:MM:SS"
        char ip[256];    // IP address string
        char message[512]; // log message text
    """
    _fields_ = [
        ("code",    c_int),        # EnErrLogTypes
        ("time",    c_char * 24),  # formatted time string "YYYY.MM.DD HH:MM:SS"
        ("ip",      c_char * 256), # IP address string
        ("message", c_char * 512), # log message text
    ]


class TickRequest(Structure):
    """
    MT4 TickRequest — parameter struct for TicksRequest().
    #pragma pack(push,1) — NO alignment padding.
    Size = 21 bytes.

    Field layout from MT4ManagerAPI.h:
        char       symbol[12];  // symbol name
        __time32_t from;        // start of period (unix seconds)
        __time32_t to;          // end of period (unix seconds)
        char       flags;       // TICK_FLAG_RAW=1, TICK_FLAG_NORMAL=2, TICK_FLAG_ALL=3
    """
    _pack_ = 1
    _fields_ = [
        ("symbol", c_char * 12),
        ("from_ts", c_int),
        ("to_ts",   c_int),
        ("flags",   c_char),
    ]


class TickRecord(Structure):
    """
    MT4 TickRecord — one tick returned by TicksRequest().
    #pragma pack(push,1) — NO alignment padding.
    Size = 25 bytes.

    Field layout from MT4ManagerAPI.h:
        __time32_t ctm;      // tick time (unix seconds)
        double     bid, ask; // bid and ask prices
        int        datafeed; // datafeed index
        char       flags;    // TICK_FLAG_* flags
    """
    _pack_ = 1
    _fields_ = [
        ("ctm",      c_int),
        ("bid",      c_double),
        ("ask",      c_double),
        ("datafeed", c_int),
        ("flags",    c_char),
    ]


class TickInfo(Structure):
    """
    MT4 TickInfo — last tick per symbol, returned by TickInfoLast().
    Default packing.
    Size = 32 bytes.

    Field layout from MT4ManagerAPI.h:
        char       symbol[12];  // symbol name
        __time32_t ctm;         // tick time (unix seconds)
        double     bid;
        double     ask;
    """
    _fields_ = [
        ("symbol", c_char * 12),
        ("ctm",    c_int),
        ("bid",    c_double),
        ("ask",    c_double),
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
            # Array type — skip reserved fields, convert others
            if "reserved" in field_name:
                continue
            val = list(val)
        result[field_name] = val
    return result


def unpack_ip(packed: int) -> str:
    """Convert packed uint32 IP address to dotted-decimal string."""
    try:
        return str(ipaddress.IPv4Address(struct.pack(">I", packed)))
    except Exception:
        return ""


# ── Vtable call helper ─────────────────────────────────────────────────────────

def _call_vtfn(manager_ptr_val: int, idx: int, restype, argtypes: list, *args):
    """
    Call a virtual method on a C++ object via its vtable.

    manager_ptr_val: raw integer value of the CManagerInterface* pointer
    idx:             vtable index (0-based) from MT4ManagerAPI.h virtual method order
    restype:         ctypes return type
    argtypes:        list of ctypes argument types (excluding `this`)
    *args:           actual arguments (excluding `this`)

    The C++ vtable layout:
        *(void**)manager_ptr_val  → vtable pointer
        vtable[idx]               → function pointer for method #idx
    In 64-bit Windows, `this` is passed as the first argument (rcx register).
    """
    # Get vtable pointer: *((void**)manager_ptr_val)
    vtable_ptr = cast(manager_ptr_val, POINTER(c_void_p)).contents.value
    # Get function pointer from vtable[idx]
    fn_ptr = cast(vtable_ptr, POINTER(c_void_p))[idx]
    # Build function type with `this` as first arg (c_void_p)
    fn_type = CFUNCTYPE(restype, c_void_p, *argtypes)
    fn = fn_type(fn_ptr)
    return fn(manager_ptr_val, *args)


# ── Vtable indices from MT4ManagerAPI.h (0-based, virtual method order) ────────
_VT_MEMFREE                = 3
_VT_CONNECT                = 6
_VT_DISCONNECT             = 7
_VT_LOGIN                  = 9
_VT_ADM_USERS_REQ          = 79   # AdmUsersRequest(group, &total) → UserRecord*
_VT_ADM_TRADES_REQ         = 80   # AdmTradesRequest(group, open_only, &total) → TradeRecord*
_VT_ONLINE_REQ             = 104  # OnlineRequest(&total) → OnlineRecord*
_VT_TRADES_USER_HISTORY    = 108  # TradesUserHistory(login, from, to, &total) → TradeRecord*
_VT_REPORTS_REQUEST        = 110  # ReportsRequest(req*, logins*, &total) → TradeRecord* (batch)
_VT_JOURNAL_REQUEST        = 96   # JournalRequest(mode, from, to, filter, &total) → ServerLog*
_VT_TICK_INFO_LAST         = 145  # TickInfoLast(symbol, &total) → TickInfo*
_VT_TICKS_REQUEST          = 162  # TicksRequest(TickRequest*, &total) → TickRecord*


# ── MT4Manager facade ─────────────────────────────────────────────────────────

class MT4Manager:
    """
    High-level MT4 Manager API facade over the DLL.

    DLL is loaded on demand from dll_path (per broker configuration).
    Uses MtManCreate() (a C export from the DLL) to obtain a
    CManagerInterface* pointer, then calls all virtual methods through
    the C++ vtable.
    """

    def __init__(self, dll_path: str, server: str, login: int, password: str):
        self.server    = server
        self.login     = login
        self.password  = password
        self._dll_path = dll_path
        self._lib: CDLL | None = None
        self._mgr: int = 0   # raw integer value of CManagerInterface*

    @classmethod
    def create(cls, dll_path: str, server: str, login: int, password: str) -> "MT4Manager":
        if not os.path.exists(dll_path):
            raise FileNotFoundError(f"MT4 DLL not found: {dll_path}")
        return cls(dll_path, server, login, password)

    def connect(self) -> None:
        """Load DLL, create manager interface, connect and login."""
        self._lib = CDLL(self._dll_path)

        # Verify DLL version
        self._lib.MtManVersion.restype = c_int
        self._lib.MtManVersion.argtypes = []
        dll_ver = self._lib.MtManVersion()
        log.debug("collector.mt4.dll_version", version=dll_ver, expected=_MAN_API_VERSION)

        # MtManCreate(int version, CManagerInterface** manager) → int
        self._lib.MtManCreate.restype  = c_int
        self._lib.MtManCreate.argtypes = [c_int, POINTER(c_void_p)]

        mgr_ptr = c_void_p()
        ret = self._lib.MtManCreate(_MAN_API_VERSION, byref(mgr_ptr))
        # Success is indicated by a non-null manager pointer.
        # MT4 DLL returns the version code on success (not zero), so
        # do NOT check ret == 0 — only check that the pointer is valid.
        if not mgr_ptr.value:
            raise RuntimeError(
                f"MtManCreate returned NULL manager pointer (code={ret}). "
                f"DLL version={dll_ver}, expected={_MAN_API_VERSION}"
            )
        log.debug("collector.mt4.mtmancreate_ok", ret=ret, ptr=hex(mgr_ptr.value))
        self._mgr = mgr_ptr.value

        # CManagerInterface::Connect(LPCSTR server) → int
        # server format: "host:port"
        server_str = f"{self.server}"
        if ":" not in server_str:
            server_str = server_str  # use as-is; some servers omit port
        ret = _call_vtfn(self._mgr, _VT_CONNECT, c_int, [c_char_p],
                         server_str.encode("ascii"))
        if ret != _RET_OK:
            raise RuntimeError(f"MT4 Connect failed: code={ret}, server={server_str}")

        # CManagerInterface::Login(int login, LPCSTR password) → int
        ret = _call_vtfn(self._mgr, _VT_LOGIN, c_int, [c_int, c_char_p],
                         self.login, self.password.encode("ascii"))
        if ret != _RET_OK:
            raise RuntimeError(f"MT4 Login failed: code={ret}, login={self.login}")

        log.info("collector.mt4.connected", server=self.server, login=self.login)

    def disconnect(self) -> None:
        """Disconnect from server and release manager interface."""
        if self._mgr:
            try:
                _call_vtfn(self._mgr, _VT_DISCONNECT, None, [])
            except Exception as exc:
                log.warning("collector.mt4.disconnect_error", error=str(exc))
            self._mgr = 0
        log.info("collector.mt4.disconnected")

    def _memfree(self, ptr) -> None:
        """Release memory allocated by the DLL (CManagerInterface::MemFree)."""
        if ptr:
            try:
                _call_vtfn(self._mgr, _VT_MEMFREE, None, [c_void_p],
                            cast(ptr, c_void_p))
            except Exception as exc:
                log.warning("collector.mt4.memfree_error", error=str(exc))

    def _assert_connected(self) -> None:
        if not self._mgr:
            raise RuntimeError("MT4Manager not connected. Call connect() first.")

    # ── Data fetch methods ────────────────────────────────────────────────────

    def get_users_by_group(self, group: str = "*") -> list[dict]:
        """
        Fetch all user records for the given group mask.
        Uses AdmUsersRequest (vtable[79]).
        Returns list of dicts.
        """
        self._assert_connected()
        total = c_int(0)
        ptr = _call_vtfn(
            self._mgr, _VT_ADM_USERS_REQ,
            POINTER(UserRecord),
            [c_char_p, POINTER(c_int)],
            group.encode("ascii"),
            byref(total),
        )
        count = total.value
        log.debug("collector.mt4.get_users_by_group", group=group, count=count)

        if not ptr or count <= 0:
            return []

        try:
            result = []
            for i in range(count):
                result.append(struct_to_dict(ptr[i]))
            return result
        finally:
            self._memfree(ptr)

    def get_trades_by_group(self, group: str = "*") -> list[dict]:
        """
        Fetch open orders (close_time==0) for the given group mask.
        Uses AdmTradesRequest(group, open_only=1) (vtable[80]).
        Returns list of dicts.
        """
        self._assert_connected()
        total = c_int(0)
        ptr = _call_vtfn(
            self._mgr, _VT_ADM_TRADES_REQ,
            POINTER(TradeRecord),
            [c_char_p, c_int, POINTER(c_int)],
            group.encode("ascii"),
            1,   # open_only=1 → open orders only
            byref(total),
        )
        count = total.value
        log.debug("collector.mt4.get_trades_by_group", group=group, count=count)

        if not ptr or count <= 0:
            return []

        try:
            result = []
            for i in range(count):
                rec = struct_to_dict(ptr[i])
                if rec.get("close_time", 0) == 0:
                    result.append(rec)
            return result
        finally:
            self._memfree(ptr)

    def get_history_by_group(self, group: str, from_ts: int, to_ts: int) -> list[dict]:
        """
        Fetch closed deals (close_time>0) in [from_ts, to_ts] unix seconds.

        Uses ReportsRequest(req*, logins*, &total) (vtable[110]) — one batched
        server call for all logins, rather than per-login loops.

        AdmTradesRequest(open_only=0) is NOT used — it loads all trades for all
        accounts without a time filter and is prohibitively slow (57+ minutes).
        TradesUserHistory per-login (vtable[108]) is a valid fallback but requires
        one network round-trip per account (~15 min for 12K accounts).
        """
        self._assert_connected()

        # Step 1: get all logins for this group
        total_users = c_int(0)
        user_ptr = _call_vtfn(
            self._mgr, _VT_ADM_USERS_REQ,
            POINTER(UserRecord),
            [c_char_p, POINTER(c_int)],
            group.encode("ascii"),
            byref(total_users),
        )
        user_count = total_users.value
        log.debug("collector.mt4.get_history_by_group",
                  group=group, logins=user_count, from_ts=from_ts, to_ts=to_ts)

        if not user_ptr or user_count <= 0:
            return []

        try:
            logins = [user_ptr[i].login for i in range(user_count)]
        finally:
            self._memfree(user_ptr)

        # Step 2: batch history fetch via ReportsRequest (one call, time-ranged)
        req = ReportGroupRequest()
        req.name    = b""
        req.from_ts = c_int(from_ts).value
        req.to_ts   = c_int(to_ts).value
        req.total   = len(logins)

        login_arr = (c_int * len(logins))(*logins)

        total = c_int(0)
        ptr = _call_vtfn(
            self._mgr, _VT_REPORTS_REQUEST,
            POINTER(TradeRecord),
            [POINTER(ReportGroupRequest), POINTER(c_int), POINTER(c_int)],
            byref(req),
            cast(login_arr, POINTER(c_int)),
            byref(total),
        )
        count = total.value
        log.debug("collector.mt4.get_history_by_group.batch",
                  group=group, count=count, from_ts=from_ts, to_ts=to_ts)

        if not ptr or count <= 0:
            return []

        try:
            result = []
            for i in range(count):
                rec = struct_to_dict(ptr[i])
                if rec.get("close_time", 0) > 0:
                    result.append(rec)
            log.debug("collector.mt4.get_history_by_group.done",
                      group=group, deals=len(result))
            return result
        finally:
            self._memfree(ptr)

    def get_online(self) -> list[dict]:
        """
        Fetch all active sessions.
        Uses OnlineRequest (vtable[104]).
        Returns list of dicts with ip as packed uint32 integer.
        """
        self._assert_connected()
        total = c_int(0)
        ptr = _call_vtfn(
            self._mgr, _VT_ONLINE_REQ,
            POINTER(OnlineRecord),
            [POINTER(c_int)],
            byref(total),
        )
        count = total.value
        log.debug("collector.mt4.get_online", count=count)

        if not ptr or count <= 0:
            return []

        try:
            result = []
            for i in range(count):
                result.append(struct_to_dict(ptr[i]))
            return result
        finally:
            self._memfree(ptr)

    def get_symbols(self) -> list[dict]:
        """
        Fetch symbol info.
        Note: ConSymbol struct is large and complex (1936 bytes).
        Returns empty list — implement SymbolsGetAll (vtable[86]) in a future iteration.
        """
        log.info("collector.mt4.get_symbols.not_implemented",
                 msg="SymbolsGetAll requires ConSymbol struct (1936 bytes) — skipping for now")
        return []

    def get_margin_levels(self) -> list[dict]:
        """
        Fetch account margin snapshots.
        Note: MarginsGet (vtable[128]) requires pumping mode — not yet enabled.
        Returns empty list.
        """
        log.info("collector.mt4.get_margin_levels.not_implemented",
                 msg="MarginsGet requires pumping mode — skipping for now")
        return []

    def get_summary(self) -> list[dict]:
        """
        Fetch per-symbol position summaries.
        Note: SummaryGetAll (vtable[149]) requires pumping mode — not yet enabled.
        Returns empty list.
        """
        log.info("collector.mt4.get_summary.not_implemented",
                 msg="SummaryGetAll requires pumping mode — skipping for now")
        return []

    def get_server_logs(self, from_ts: int, to_ts: int) -> list[dict]:
        """
        Fetch server log entries for the given time range.
        Uses JournalRequest (vtable[96]).

        Signature: JournalRequest(mode, from, to, filter, *total) → ServerLog*
        mode=4 = LOG_TYPE_FULL (all log entries including logins, trades, errors).
        Returns ServerLog* array; caller must release via MemFree.
        """
        self._assert_connected()
        total = c_int(0)

        try:
            ptr = _call_vtfn(
                self._mgr, _VT_JOURNAL_REQUEST,
                POINTER(ServerLog),
                [c_int, c_int, c_int, c_char_p, POINTER(c_int)],
                c_int(4),        # mode = LOG_TYPE_FULL (4) — all log entries
                c_int(from_ts),
                c_int(to_ts),
                b"",             # filter: empty (no keyword filter)
                byref(total),
            )
        except Exception as exc:
            log.warning(
                "collector.mt4.get_server_logs.failed",
                error=str(exc),
                vtable=_VT_JOURNAL_REQUEST,
            )
            return []

        count = total.value
        if not ptr or count <= 0:
            return []

        try:
            result = []
            for i in range(count):
                rec = struct_to_dict(ptr[i])
                result.append(rec)
            log.debug("collector.mt4.get_server_logs", count=len(result),
                      from_ts=from_ts, to_ts=to_ts)
            return result
        finally:
            self._memfree(ptr)

    def get_latest_ticks(self) -> list[dict]:
        """
        Fetch the most recent tick for every available symbol via TickInfoLast (vtable[145]).

        Signature: TickInfoLast(symbol, *total) → TickInfo*
        Pass "*" to request ticks for all symbols (pumping mode; may return empty
        without PumpingSwitch active — falls back gracefully).

        TickInfo struct: symbol (char[12]), ctm (unix s), bid (double), ask (double).
        """
        self._assert_connected()
        total = c_int(0)

        try:
            ptr = _call_vtfn(
                self._mgr, _VT_TICK_INFO_LAST,
                POINTER(TickInfo),
                [c_char_p, POINTER(c_int)],
                b"*",
                byref(total),
            )
        except Exception as exc:
            log.warning(
                "collector.mt4.get_latest_ticks.failed",
                error=str(exc),
                vtable=_VT_TICK_INFO_LAST,
            )
            return []

        count = total.value
        if not ptr or count <= 0:
            return []

        try:
            result = []
            for i in range(count):
                rec = struct_to_dict(ptr[i])
                result.append(rec)
            log.debug("collector.mt4.get_latest_ticks", count=len(result))
            return result
        finally:
            self._memfree(ptr)

    def get_ticks(self, symbol: str, from_ts: int, to_ts: int) -> list[dict]:
        """
        Fetch tick history for a symbol via TicksRequest (vtable[162]).

        Signature: TicksRequest(TickRequest*, *total) → TickRecord*
        TickRequest: symbol (char[12]), from_ts (__time32_t), to_ts (__time32_t), flags (char).
        TickRecord:  ctm (unix s), bid (double), ask (double), datafeed (int), flags (char).
        """
        self._assert_connected()
        total = c_int(0)

        req = TickRequest()
        sym_bytes = symbol.encode("ascii")[:11]
        req.symbol = sym_bytes
        req.from_ts = c_int(from_ts).value
        req.to_ts   = c_int(to_ts).value
        req.flags   = b"\x03"  # TICK_FLAG_ALL = 3

        try:
            ptr = _call_vtfn(
                self._mgr, _VT_TICKS_REQUEST,
                POINTER(TickRecord),
                [POINTER(TickRequest), POINTER(c_int)],
                byref(req),
                byref(total),
            )
        except Exception as exc:
            log.warning(
                "collector.mt4.get_ticks.failed",
                symbol=symbol, error=str(exc),
                vtable=_VT_TICKS_REQUEST,
            )
            return []

        count = total.value
        if not ptr or count <= 0:
            return []

        try:
            result = []
            for i in range(count):
                rec = struct_to_dict(ptr[i])
                rec["_symbol"] = symbol
                result.append(rec)
            log.debug("collector.mt4.get_ticks", symbol=symbol, count=len(result))
            return result
        finally:
            self._memfree(ptr)
