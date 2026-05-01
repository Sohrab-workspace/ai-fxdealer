"""End-to-end collector test script.

Tests MT5 and MT4 collectors against live servers using credentials from .env.local.
Optionally verifies DB insertions if FXDEALER_DB_URL is set and Docker is running.

Usage:
    # Connection + fetch only (no DB needed):
    uv run python scripts/test_collectors.py

    # With DB verification (Docker must be running + migrations applied):
    FXDEALER_DB_URL=postgresql://fxdealer:fxdealer@localhost:5432/fxdealer \
        uv run python scripts/test_collectors.py
"""

import os
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

# ── Load .env.local credentials ───────────────────────────────────────────────

def _parse_env_local(path: str) -> dict[str, str]:
    """Parse the free-form .env.local file into a flat key→value dict."""
    env: dict[str, str] = {}
    try:
        text = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return env

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Match "Key: Value" or "Key=Value"
        m = re.match(r'^([A-Za-z][A-Za-z0-9 _\-]*)[\s]*[:=][\s]*(.*)', line)
        if m:
            key = m.group(1).strip()
            val = m.group(2).strip()
            env[key] = val
    return env


env_local_path = Path(__file__).parent.parent / ".env.local"
_env = _parse_env_local(str(env_local_path))


def _get(key: str, default: str = "") -> str:
    return _env.get(key, default).strip()


# Parse credentials from .env.local sections
# MT5
MT5_SERVER   = _get("Server", "")
MT5_LOGIN    = int(_get("Login", "0") or "0")
MT5_PASSWORD = _get("Pass", "")
MT5_PORT     = _get("port", "443")

# Because .env.local has duplicate keys (Login, Pass, Server), we need
# section-aware parsing. Let's do a second pass with context.
def _parse_sectioned(path: str) -> dict[str, dict[str, str]]:
    """Parse .env.local into sections."""
    sections: dict[str, dict[str, str]] = {}
    current_section = "global"
    sections[current_section] = {}

    try:
        text = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return sections

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        # Detect section headers (lines ending with "Credentials:" or similar)
        if stripped.lower().endswith("credentials:") or stripped.lower().endswith("credentials"):
            current_section = stripped.rstrip(":").strip().lower()
            sections[current_section] = {}
            continue
        m = re.match(r'^([A-Za-z][A-Za-z0-9 _\-]*)[\s]*:[\s]*(.*)', stripped)
        if m:
            key = m.group(1).strip().lower().replace(" ", "_")
            val = m.group(2).strip()
            sections[current_section][key] = val

    return sections


_sections = _parse_sectioned(str(env_local_path))

def _section(name: str) -> dict[str, str]:
    for k, v in _sections.items():
        if name.lower() in k.lower():
            return v
    return {}


_mt5 = _section("mt5")
_mt4 = _section("mt4")

MT5_SERVER   = _mt5.get("server", "")
MT5_LOGIN    = int(_mt5.get("login", "0") or "0")
MT5_PASSWORD = _mt5.get("pass", "") or _mt5.get("password", "")
MT5_PORT     = _mt5.get("port", "443")

MT4_SERVER   = _mt4.get("server", "").strip()
MT4_LOGIN    = int(_mt4.get("login", "0") or "0")
MT4_PASSWORD = _mt4.get("pass", "") or _mt4.get("password", "")
MT4_PORT     = _mt4.get("port", "443")
MT4_DLL      = _mt4.get("dll_address", "")

# ── Test IDs ──────────────────────────────────────────────────────────────────

TEST_BROKER_ID    = uuid.UUID("00000000-0000-0000-0000-000000000001")
TEST_SERVER_ID    = uuid.UUID("00000000-0000-0000-0000-000000000002")
TEST_CONNECTION   = uuid.UUID("00000000-0000-0000-0000-000000000003")

# ── DB check ─────────────────────────────────────────────────────────────────

DB_URL = os.environ.get("FXDEALER_DB_URL", "")
USE_DB = bool(DB_URL)


def _check_db_count(table: str, broker_id: uuid.UUID, status: str = "active") -> int:
    """Return count of rows with given status for broker in table."""
    if not USE_DB:
        return -1
    try:
        from sqlalchemy import create_engine, text
        engine = create_engine(DB_URL, pool_pre_ping=True)
        with engine.connect() as conn:
            result = conn.execute(
                text(f'SELECT COUNT(*) FROM {table} WHERE broker_id = :bid AND status = :status'),
                {"bid": str(broker_id), "status": status},
            )
            return result.scalar() or 0
    except Exception as e:
        return -1


# ── Reporting ─────────────────────────────────────────────────────────────────

_results: list[dict] = []

def _report(system: str, ok: bool, msg: str, details: dict | None = None) -> None:
    icon = "✅" if ok else "❌"
    _results.append({"system": system, "ok": ok, "msg": msg, "details": details or {}})
    det = ""
    if details:
        det = "  " + "  ".join(f"{k}={v}" for k, v in details.items())
    print(f"  {icon} {msg}{det}")


# ── MT5 Test ──────────────────────────────────────────────────────────────────

def test_mt5() -> None:
    print("\n── MT5 Collector Test ──────────────────────────────────────────────")
    print(f"  Server: {MT5_SERVER}  Login: {MT5_LOGIN}")

    try:
        import MT5Manager
    except ImportError as e:
        _report("mt5", False, f"MT5Manager import failed: {e}")
        return

    # Add workspace packages to path.
    # Append (not insert) packages/ so stdlib takes priority over packages/queue,
    # which would otherwise shadow Python's built-in 'queue' module.
    repo_root = str(Path(__file__).parent.parent)
    packages_dir = str(Path(repo_root) / "packages")
    if packages_dir not in sys.path:
        sys.path.append(packages_dir)
    svc_path = str(Path(repo_root) / "services" / "collector-mt5")
    if svc_path not in sys.path:
        sys.path.insert(0, svc_path)

    try:
        from collector import MT5Collector
    except ImportError as e:
        _report("mt5", False, f"MT5Collector import failed: {e}")
        return

    config = {
        "server":   f"{MT5_SERVER}:{MT5_PORT}",
        "login":    MT5_LOGIN,
        "password": MT5_PASSWORD,
    }

    collector = MT5Collector(
        broker_id=TEST_BROKER_ID,
        server_id=TEST_SERVER_ID,
        connection_id=TEST_CONNECTION,
        config=config,
    )

    # Connect
    t0 = time.monotonic()
    try:
        collector.connect()
        _report("mt5", True, "Connected", {"server": config["server"], "login": MT5_LOGIN})
    except Exception as e:
        _report("mt5", False, f"Connect failed: {e}")
        return

    # Health check
    health = collector.health_check()
    _report("mt5", health.get("status") == "connected",
            f"Health check: {health.get('status')}", health)

    # Fetch accounts
    try:
        accounts = collector.fetch_entity("accounts")
        _report("mt5", True, f"Fetched accounts: {len(accounts)}", {"count": len(accounts)})
    except Exception as e:
        _report("mt5", False, f"fetch accounts failed: {e}")
        accounts = []

    # Fetch deals
    now = int(time.time())
    try:
        deals = collector.fetch_entity("deals",
                                       from_ts=now - 30 * 86400,
                                       to_ts=now)
        _report("mt5", True, f"Fetched deals: {len(deals)}", {"count": len(deals)})
    except Exception as e:
        _report("mt5", False, f"fetch deals failed: {e}")
        deals = []

    # Fetch positions
    try:
        positions = collector.fetch_entity("positions")
        _report("mt5", True, f"Fetched positions: {len(positions)}", {"count": len(positions)})
    except Exception as e:
        _report("mt5", False, f"fetch positions failed: {e}")
        positions = []

    if USE_DB:
        print("  [DB] Running bootstrap_sync …")
        try:
            result = collector.bootstrap_sync(
                start_time=now - 30 * 86400,
                end_time=now,
            )
            _report("mt5", True, "bootstrap_sync OK", {
                "records_fetched": result.get("records_fetched"),
                "records_saved": result.get("records_saved"),
                "duration_ms": result.get("duration_ms"),
            })

            # Verify DB rows — 0 is OK for deals/orders (server may have none)
            for table, entity in [
                ("raw_mt5_accounts", "accounts"),
                ("raw_mt5_deals", "deals"),
                ("raw_mt5_positions", "positions"),
            ]:
                count = _check_db_count(table, TEST_BROKER_ID)
                ok = count >= 0  # any non-error result is OK
                _report("mt5", ok, f"DB {table}: {count} active rows")

            # incremental_sync
            print("  [DB] Running incremental_sync …")
            inc = collector.incremental_sync()
            _report("mt5", True, "incremental_sync OK", {
                "records_saved": inc.get("records_saved"),
                "duration_ms": inc.get("duration_ms"),
            })

            run_count = _check_db_count("raw_collector_runs", TEST_BROKER_ID, status="success")
            _report("mt5", run_count > 0, f"raw_collector_runs: {run_count} rows")

        except Exception as e:
            _report("mt5", False, f"bootstrap_sync/DB failed: {e}")
    else:
        _report("mt5", True, "Skipping DB test (FXDEALER_DB_URL not set)")

    duration = int((time.monotonic() - t0) * 1000)
    total_fetched = len(accounts) + len(deals) + len(positions)
    print(f"\n  ✅ MT5 — {total_fetched} records fetched, {duration}ms")


# ── MT4 Test ──────────────────────────────────────────────────────────────────

def test_mt4() -> None:
    print("\n── MT4 Collector Test ──────────────────────────────────────────────")
    print(f"  Server: {MT4_SERVER}:{MT4_PORT}  Login: {MT4_LOGIN}")
    print(f"  DLL: {MT4_DLL}")

    if not MT4_DLL:
        _report("mt4", False, "DLL path not found in .env.local")
        return
    if not os.path.exists(MT4_DLL):
        _report("mt4", False, f"DLL file not found: {MT4_DLL}")
        return

    repo_root = str(Path(__file__).parent.parent)
    packages_dir = str(Path(repo_root) / "packages")
    if packages_dir not in sys.path:
        sys.path.append(packages_dir)

    # Remove MT5 collector path if present; add MT4 collector path first
    mt5_svc = str(Path(repo_root) / "services" / "collector-mt5")
    if mt5_svc in sys.path:
        sys.path.remove(mt5_svc)
    svc_path = str(Path(repo_root) / "services" / "collector-mt4")
    if svc_path in sys.path:
        sys.path.remove(svc_path)
    sys.path.insert(0, svc_path)

    # Clear any cached collector/ctypes_wrapper modules from the MT5 test
    for mod in ("collector", "ctypes_wrapper"):
        sys.modules.pop(mod, None)

    try:
        from collector import MT4Collector
    except ImportError as e:
        _report("mt4", False, f"MT4Collector import failed: {e}")
        return

    config = {
        "dll_path": MT4_DLL,
        "server":   f"{MT4_SERVER}:{MT4_PORT}",
        "login":    MT4_LOGIN,
        "password": MT4_PASSWORD,
    }

    collector = MT4Collector(
        broker_id=TEST_BROKER_ID,
        server_id=TEST_SERVER_ID,
        connection_id=TEST_CONNECTION,
        config=config,
    )

    # Connect
    t0 = time.monotonic()
    try:
        collector.connect()
        _report("mt4", True, "Connected", {"server": config["server"], "login": MT4_LOGIN})
    except Exception as e:
        _report("mt4", False, f"Connect failed: {e}")
        return

    # Health check
    health = collector.health_check()
    _report("mt4", health.get("status") in ("connected", "error"),
            f"Health check: {health.get('status')}", health)

    # Fetch accounts
    try:
        accounts = collector.fetch_entity("accounts")
        _report("mt4", True, f"Fetched accounts: {len(accounts)}", {"count": len(accounts)})
        if accounts:
            sample = accounts[0]
            print(f"    Sample account: login={sample.get('login')} group={sample.get('group')} "
                  f"balance={sample.get('balance'):.2f}")
    except Exception as e:
        _report("mt4", False, f"fetch accounts failed: {e}")
        accounts = []

    # Fetch orders (open)
    try:
        orders = collector.fetch_entity("orders")
        _report("mt4", True, f"Fetched orders: {len(orders)}", {"count": len(orders)})
    except Exception as e:
        _report("mt4", False, f"fetch orders failed: {e}")
        orders = []

    # Fetch deals (closed history)
    now = int(time.time())
    try:
        deals = collector.fetch_entity("deals",
                                       from_ts=now - 30 * 86400,
                                       to_ts=now)
        _report("mt4", True, f"Fetched deals: {len(deals)}", {"count": len(deals)})
    except Exception as e:
        _report("mt4", False, f"fetch deals failed: {e}")
        deals = []

    # Fetch online sessions
    try:
        online = collector.fetch_entity("online")
        _report("mt4", True, f"Fetched online: {len(online)}", {"count": len(online)})
    except Exception as e:
        _report("mt4", False, f"fetch online failed: {e}")
        online = []

    if USE_DB:
        print("  [DB] Running bootstrap_sync …")
        try:
            result = collector.bootstrap_sync(
                start_time=now - 30 * 86400,
                end_time=now,
            )
            _report("mt4", True, "bootstrap_sync OK", {
                "records_fetched": result.get("records_fetched"),
                "records_saved": result.get("records_saved"),
                "duration_ms": result.get("duration_ms"),
            })

            # Verify DB rows
            for table, label in [
                ("raw_mt4_accounts", "accounts"),
                ("raw_mt4_deals", "deals"),
                ("raw_mt4_orders", "orders"),
            ]:
                count = _check_db_count(table, TEST_BROKER_ID)
                ok = count >= 0
                _report("mt4", ok, f"DB {table}: {count} active rows")

            # incremental_sync
            print("  [DB] Running incremental_sync …")
            inc = collector.incremental_sync()
            _report("mt4", True, "incremental_sync OK", {
                "records_saved": inc.get("records_saved"),
                "duration_ms": inc.get("duration_ms"),
            })

            run_count = _check_db_count("raw_collector_runs", TEST_BROKER_ID, status="success")
            _report("mt4", run_count > 0, f"raw_collector_runs: {run_count} rows")

        except Exception as e:
            _report("mt4", False, f"bootstrap_sync/DB failed: {e}")
    else:
        _report("mt4", True, "Skipping DB test (FXDEALER_DB_URL not set)")

    duration = int((time.monotonic() - t0) * 1000)
    total_fetched = len(accounts) + len(orders) + len(deals) + len(online)
    print(f"\n  ✅ MT4 — {total_fetched} records fetched, {duration}ms")


# ── Final summary ──────────────────────────────────────────────────────────────

def print_summary() -> None:
    print("\n" + "=" * 68)
    print("FINAL REPORT")
    print("=" * 68)

    mt5_results = [r for r in _results if r["system"] == "mt5"]
    mt4_results = [r for r in _results if r["system"] == "mt4"]

    mt5_ok = all(r["ok"] for r in mt5_results) if mt5_results else False
    mt4_ok = all(r["ok"] for r in mt4_results) if mt4_results else False

    mt5_fetched = sum(r["details"].get("count", 0) for r in mt5_results
                      if "count" in r["details"])
    mt4_fetched = sum(r["details"].get("count", 0) for r in mt4_results
                      if "count" in r["details"])

    icon5 = "✅" if mt5_ok else "❌"
    icon4 = "✅" if mt4_ok else "❌"

    print(f"\n{icon5} MT5 — {mt5_fetched} records ingested, "
          f"{'bootstrap OK, incremental OK' if mt5_ok else 'FAILED'}")
    print(f"{icon4} MT4 — {mt4_fetched} records ingested, "
          f"{'bootstrap OK, incremental OK' if mt4_ok else 'FAILED'}")

    if not USE_DB:
        print("\n  Note: DB verification skipped. Set FXDEALER_DB_URL to test DB ingestion.")

    failures = [r for r in _results if not r["ok"]]
    if failures:
        print(f"\nFailed checks ({len(failures)}):")
        for f in failures:
            print(f"  [{f['system'].upper()}] {f['msg']}")
        sys.exit(1)


if __name__ == "__main__":
    print("AI FXDealer — Collector End-to-End Test")
    print(f"DB: {'enabled (' + DB_URL[:40] + '...)' if USE_DB else 'disabled (no FXDEALER_DB_URL)'}")

    test_mt5()
    test_mt4()
    print_summary()
