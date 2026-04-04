"""Quick MT4 history test — verifies ReportsRequest (vtable 110) batch approach.

Tests the batch history API (ReportsRequest) which fetches all logins in one
server call instead of per-login loops (TradesUserHistory x 12K accounts).

Usage:
    cd ai-fxdealer
    python scripts/test_mt4_history.py
"""
import re
import sys
import time
from ctypes import sizeof
from pathlib import Path

# ── path setup ────────────────────────────────────────────────────────────────
repo = Path(__file__).parent.parent
for p in ["packages/shared", "packages/db", "services/collector-mt4"]:
    s = str(repo / p)
    if s not in sys.path:
        sys.path.insert(0, s)

# ── load .env.local ───────────────────────────────────────────────────────────
def _load_env(path):
    sections, cur = {}, "global"
    sections[cur] = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s: continue
        if s.lower().endswith("credentials:") or s.lower().endswith("credentials"):
            cur = s.rstrip(":").strip().lower()
            sections[cur] = {}
            continue
        m = re.match(r'^([A-Za-z][A-Za-z0-9 _\-]*)[\s]*:[\s]*(.*)', s)
        if m:
            sections[cur][m.group(1).strip().lower().replace(" ", "_")] = m.group(2).strip()
    return sections

_sections = _load_env(str(repo / ".env.local"))
_mt4 = next((v for k, v in _sections.items() if "mt4" in k), {})

SERVER   = _mt4.get("server", "")
PORT     = _mt4.get("port", "443")
LOGIN    = int(_mt4.get("login", "0") or "0")
PASSWORD = _mt4.get("pass", "") or _mt4.get("password", "")
DLL      = _mt4.get("dll_address", "")

print(f"Server: {SERVER}:{PORT}  Login: {LOGIN}  DLL: {DLL}")

# ── import wrapper ────────────────────────────────────────────────────────────
from ctypes_wrapper import (MT4Manager, UserRecord, TradeRecord, OnlineRecord,
                             ReportGroupRequest, _VT_REPORTS_REQUEST,
                             _VT_TRADES_USER_HISTORY, _call_vtfn)
from ctypes import c_int, POINTER, byref, cast

print(f"Struct sizes: UserRecord={sizeof(UserRecord)}, TradeRecord={sizeof(TradeRecord)}, "
      f"OnlineRecord={sizeof(OnlineRecord)}, ReportGroupRequest={sizeof(ReportGroupRequest)}")
print(f"ReportsRequest vtable index: {_VT_REPORTS_REQUEST}")
print(f"TradesUserHistory vtable index: {_VT_TRADES_USER_HISTORY}")

# ── connect ───────────────────────────────────────────────────────────────────
mgr = MT4Manager.create(dll_path=DLL, server=f"{SERVER}:{PORT}",
                        login=LOGIN, password=PASSWORD)
mgr.connect()
print("Connected!")

# ── fetch accounts ────────────────────────────────────────────────────────────
t0 = time.monotonic()
accounts = mgr.get_users_by_group("*")
print(f"Accounts: {len(accounts)}  ({int((time.monotonic()-t0)*1000)}ms)")

now     = int(time.time())
from_ts = now - 30 * 86400
to_ts   = now

# ── test ReportsRequest batch (all logins in one call) ────────────────────────
print(f"\nTesting ReportsRequest batch for all {len(accounts)} logins "
      f"(from={from_ts} to={to_ts}) ...")

logins = [a["login"] for a in accounts]
req = ReportGroupRequest()
req.name    = b""
req.from_ts = c_int(from_ts).value
req.to_ts   = c_int(to_ts).value
req.total   = len(logins)
login_arr = (c_int * len(logins))(*logins)

t1 = time.monotonic()
total = c_int(0)
ptr = _call_vtfn(
    mgr._mgr, _VT_REPORTS_REQUEST,
    POINTER(TradeRecord),
    [POINTER(ReportGroupRequest), POINTER(c_int), POINTER(c_int)],
    byref(req),
    cast(login_arr, POINTER(c_int)),
    byref(total),
)
elapsed_batch = int((time.monotonic() - t1) * 1000)
count_batch = total.value
if ptr and count_batch > 0:
    mgr._memfree(ptr)
print(f"  ReportsRequest returned {count_batch} records in {elapsed_batch}ms")

# ── compare: get_history_by_group (uses batch internally) ─────────────────────
print(f"\nRunning get_history_by_group (batch) ...")
t2 = time.monotonic()
deals = mgr.get_history_by_group("*", from_ts, to_ts)
elapsed_full = int((time.monotonic() - t2) * 1000)
print(f"Deals (30d): {len(deals)}  ({elapsed_full}ms = {elapsed_full//1000}s)")

# ── online ────────────────────────────────────────────────────────────────────
online = mgr.get_online()
print(f"Online: {len(online)}")

mgr.disconnect()
total_time = int((time.monotonic() - t0) * 1000)
print(f"\nTotal time: {total_time}ms = {total_time//1000}s")
print(f"SUCCESS — {len(accounts)} accounts, {len(deals)} deals, {len(online)} online")
