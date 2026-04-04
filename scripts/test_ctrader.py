"""cTrader end-to-end test script.

Tests both the Manager API collector and the Reporting DB connection.

Usage:
    # Manager API + Reporting DB (no platform DB needed):
    uv run python scripts/test_ctrader.py

    # With platform DB verification (Docker must be running + migrations applied):
    FXDEALER_DB_URL=postgresql://fxdealer:fxdealer@localhost:5432/fxdealer \
        uv run python scripts/test_ctrader.py

Requires:
    - stunnel running for Reporting DB tests
      (C:\\Program Files (x86)\\stunnel\\bin\\stunnel.exe)
"""

import os
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

# ── Path setup ────────────────────────────────────────────────────────────────
repo_root    = str(Path(__file__).parent.parent)
packages_dir = str(Path(repo_root) / "packages")
svc_path     = str(Path(repo_root) / "services" / "collector-ctrader")

if packages_dir not in sys.path:
    sys.path.append(packages_dir)   # append — avoids shadowing stdlib 'queue'
if svc_path not in sys.path:
    sys.path.insert(0, svc_path)

# Clear any cached collector modules from prior tests
for _mod in ("collector",):
    sys.modules.pop(_mod, None)

# ── Credentials from .env.local ───────────────────────────────────────────────

def _parse_sections(path: str) -> dict[str, dict[str, str]]:
    """Parse .env.local into {section: {key: value}} dict."""
    sections: dict[str, dict[str, str]] = {}
    current = "global"
    sections[current] = {}
    try:
        text = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return sections
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.lower().endswith("credentials:") or stripped.lower().endswith("credentials"):
            current = stripped.rstrip(":").strip().lower()
            sections[current] = {}
            continue
        m = re.match(r'^([A-Za-z][A-Za-z0-9 _\-/]*)[\s]*:[\s]*(.*)', stripped)
        if m:
            key = m.group(1).strip().lower().replace(" ", "_").replace("/", "_")
            val = m.group(2).strip()
            sections[current][key] = val
    return sections


_env_path = Path(repo_root) / ".env.local"
_sections = _parse_sections(str(_env_path))


def _section(name: str) -> dict[str, str]:
    for k, v in _sections.items():
        if name.lower() in k.lower():
            return v
    return {}


_ct = _section("ctrader")
CT_HOST      = _ct.get("server_address_domain", "live-managerapi.p.ctrader.com")
CT_PORT      = int(_ct.get("port_5011", _ct.get("port", "5011")) or "5011")
CT_LOGIN     = int(_ct.get("login", "10023") or "10023")
CT_PASSWORD  = _ct.get("pass", "Vista1234")
CT_PLANT_ID  = _ct.get("plantid", "opofinance")
CT_ENV_NAME  = _ct.get("environmentname", "live")

# Reporting DB credentials (from capture_schema.py)
REPDB_DEMO = dict(
    host="127.0.0.1", port=5432,
    user="opofinance_demo_repo", password="k0OKby8J",
    dbname="ctrader_spotware", connect_timeout=10,
    sslmode="disable",
)
REPDB_LIVE = dict(
    host="127.0.0.1", port=5433,
    user="opofinance_live_repo", password="90mVYphS",
    dbname="ctrader_spotware", connect_timeout=10,
    sslmode="disable",
)

# ── Test IDs ──────────────────────────────────────────────────────────────────

TEST_BROKER_ID  = uuid.UUID("00000000-0000-0000-0000-000000000001")
TEST_SERVER_ID  = uuid.UUID("00000000-0000-0000-0000-000000000004")
TEST_CONNECTION = uuid.UUID("00000000-0000-0000-0000-000000000005")

# ── Platform DB check ─────────────────────────────────────────────────────────

DB_URL = os.environ.get("FXDEALER_DB_URL", "")
USE_DB = bool(DB_URL)


def _check_db_count(table: str, broker_id: uuid.UUID, status: str = "active") -> int:
    if not USE_DB:
        return -1
    try:
        from sqlalchemy import create_engine, text
        engine = create_engine(DB_URL, pool_pre_ping=True)
        with engine.connect() as conn:
            r = conn.execute(
                text(f'SELECT COUNT(*) FROM {table} WHERE broker_id = :bid AND status = :status'),
                {"bid": str(broker_id), "status": status},
            )
            return r.scalar() or 0
    except Exception:
        return -1


# ── Reporting helpers ─────────────────────────────────────────────────────────

_results: list[dict] = []


def _report(system: str, ok: bool, msg: str, details: dict | None = None) -> None:
    icon = "✅" if ok else "❌"
    _results.append({"system": system, "ok": ok, "msg": msg, "details": details or {}})
    det = ""
    if details:
        det = "  " + "  ".join(f"{k}={v}" for k, v in details.items())
    print(f"  {icon} {msg}{det}")


# ── Manager API test ──────────────────────────────────────────────────────────

def test_manager_api() -> None:
    print("\n── cTrader Manager API Test ────────────────────────────────────────")
    print(f"  Host: {CT_HOST}:{CT_PORT}  Plant: {CT_PLANT_ID}/{CT_ENV_NAME}  Login: {CT_LOGIN}")

    from collector import CTraderCollector

    config = {
        "host":      CT_HOST,
        "port":      CT_PORT,
        "plant_id":  CT_PLANT_ID,
        "env_name":  CT_ENV_NAME,
        "login":     CT_LOGIN,
        "password":  CT_PASSWORD,
    }

    collector = CTraderCollector(
        broker_id=TEST_BROKER_ID,
        server_id=TEST_SERVER_ID,
        connection_id=TEST_CONNECTION,
        config=config,
    )

    t0 = time.monotonic()

    # Connect
    try:
        collector.connect()
        _report("manager_api", True, "Connected",
                {"host": CT_HOST, "login": CT_LOGIN})
    except Exception as e:
        _report("manager_api", False, f"Connect failed: {e}")
        return

    # Health check
    health = collector.health_check()
    ok = health.get("status") == "connected"
    _report("manager_api", ok, f"Health check: {health.get('status')}", health)
    if not ok:
        return

    now_ms = int(time.time() * 1000)

    # Fetch accounts
    try:
        accounts = collector.fetch_entity("accounts")
        _report("manager_api", True, f"Fetched accounts: {len(accounts)}", {"count": len(accounts)})
        if accounts:
            s = accounts[0]
            print(f"    Sample: trader_id={s.get('1')}  group_id={s.get('3')}  "
                  f"balance_cents={s.get('8')}")
    except Exception as e:
        _report("manager_api", False, f"fetch accounts failed: {e}")
        accounts = []

    # Fetch symbols
    try:
        symbols = collector.fetch_entity("symbols")
        _report("manager_api", True, f"Fetched symbols: {len(symbols)}", {"count": len(symbols)})
    except Exception as e:
        _report("manager_api", False, f"fetch symbols failed: {e}")
        symbols = []

    # Fetch groups
    try:
        groups = collector.fetch_entity("groups")
        _report("manager_api", True, f"Fetched groups: {len(groups)}", {"count": len(groups)})
    except Exception as e:
        _report("manager_api", False, f"fetch groups failed: {e}")
        groups = []

    # Fetch open positions
    try:
        positions = collector.fetch_entity("positions",
                                           from_ms=now_ms - 90 * 86400 * 1000,
                                           to_ms=now_ms)
        _report("manager_api", True, f"Fetched positions: {len(positions)}", {"count": len(positions)})
    except Exception as e:
        _report("manager_api", False, f"fetch positions failed: {e}")
        positions = []

    # Fetch deals (last 30 days)
    try:
        deals = collector.fetch_entity("deals",
                                       from_ms=now_ms - 30 * 86400 * 1000,
                                       to_ms=now_ms)
        _report("manager_api", True, f"Fetched deals: {len(deals)}", {"count": len(deals)})
        if deals:
            s = deals[0]
            print(f"    Sample deal: deal_id={s.get('1')}  trader_id={s.get('4')}  "
                  f"symbol_id={s.get('7')}  volume={s.get('5')}")
    except Exception as e:
        _report("manager_api", False, f"fetch deals failed: {e}")
        deals = []

    # Fetch pending orders
    try:
        orders = collector.fetch_entity("orders",
                                        from_ms=now_ms - 30 * 86400 * 1000,
                                        to_ms=now_ms)
        _report("manager_api", True, f"Fetched orders: {len(orders)}", {"count": len(orders)})
    except Exception as e:
        _report("manager_api", False, f"fetch orders failed: {e}")
        orders = []

    # Platform DB tests
    if USE_DB:
        print("  [DB] Running bootstrap_sync …")
        try:
            result = collector.bootstrap_sync(
                start_time=(now_ms - 30 * 86400 * 1000) / 1000,
                end_time=now_ms / 1000,
            )
            _report("manager_api", True, "bootstrap_sync OK", {
                "records_fetched": result.get("records_fetched"),
                "records_saved":   result.get("records_saved"),
                "duration_ms":     result.get("duration_ms"),
            })

            for table in (
                "raw_ctrader_accounts",
                "raw_ctrader_symbols",
                "raw_ctrader_groups",
                "raw_ctrader_positions",
                "raw_ctrader_deals",
                "raw_ctrader_orders",
            ):
                count = _check_db_count(table, TEST_BROKER_ID)
                _report("manager_api", count >= 0, f"DB {table}: {count} active rows")

            print("  [DB] Running incremental_sync …")
            inc = collector.incremental_sync()
            _report("manager_api", True, "incremental_sync OK", {
                "records_saved": inc.get("records_saved"),
                "duration_ms":   inc.get("duration_ms"),
            })

            run_count = _check_db_count("raw_collector_runs", TEST_BROKER_ID, status="success")
            _report("manager_api", run_count > 0, f"raw_collector_runs: {run_count} rows")

        except Exception as e:
            _report("manager_api", False, f"bootstrap_sync/DB failed: {e}")
            import traceback; traceback.print_exc()
    else:
        _report("manager_api", True, "Skipping DB test (FXDEALER_DB_URL not set)")

    duration = int((time.monotonic() - t0) * 1000)
    total = len(accounts) + len(symbols) + len(groups) + len(positions) + len(deals) + len(orders)
    print(f"\n  ✅ Manager API — {total} records fetched, {duration}ms")


# ── Reporting DB test ─────────────────────────────────────────────────────────

def test_reporting_db() -> None:
    print("\n── cTrader Reporting DB Test ───────────────────────────────────────")
    print("  (requires stunnel to be running)")

    try:
        import psycopg2
        import psycopg2.extras
    except ImportError:
        _report("reporting_db", False, "psycopg2 not installed (pip install psycopg2-binary)")
        return

    # Schema names differ per environment (Spotware uses broker-specific schemas)
    env_schema = {"Demo": "opofinance_demo", "Live": "opofinance_live"}

    for env_label, conn_params in [("Demo", REPDB_DEMO), ("Live", REPDB_LIVE)]:
        print(f"\n  [{env_label}] localhost:{conn_params['port']} → {conn_params['user']}")
        t0 = time.monotonic()
        schema = env_schema[env_label]
        try:
            conn = psycopg2.connect(**conn_params)
        except Exception as e:
            _report("reporting_db", False, f"{env_label} connect failed: {e}")
            continue

        _report("reporting_db", True, f"{env_label} connected")

        try:
            with conn.cursor() as cur:
                # List tables in broker-specific schema
                cur.execute("""
                    SELECT table_name
                    FROM information_schema.tables
                    WHERE table_schema = %s AND table_type = 'BASE TABLE'
                    ORDER BY table_name
                """, (schema,))
                tables = [r[0] for r in cur.fetchall()]
                _report("reporting_db", True, f"{env_label} tables found: {len(tables)}",
                        {"schema": schema, "tables": ", ".join(tables[:8]) + ("\u2026" if len(tables) > 8 else "")})

                # Row counts for key tables
                key_tables = ["trader", "deal", "position", "trade_order",
                              "trader_group", "symbol", "balance_history"]
                counts = {}
                for t in key_tables:
                    if t in tables:
                        try:
                            cur.execute(f'SELECT COUNT(*) FROM {schema}."{t}"')
                            counts[t] = cur.fetchone()[0]
                        except Exception:
                            counts[t] = "err"

                if counts:
                    count_str = "  ".join(f"{k}={v}" for k, v in counts.items())
                    _report("reporting_db", True, f"{env_label} row counts", counts)
                    print(f"    {count_str}")

                # Sample deal row (deal_id is PK, not id)
                if "deal" in tables:
                    try:
                        cur.execute(f'SELECT * FROM {schema}."deal" ORDER BY deal_id DESC LIMIT 1')
                        cols = [d[0] for d in cur.description]
                        row  = cur.fetchone()
                        if row:
                            sample = dict(zip(cols, row))
                            # Show non-PII fields
                            show = {k: v for k, v in sample.items()
                                    if k in ("deal_id", "position_id", "trade_order_id", "symbol_id",
                                             "create_timestamp", "execution_price", "filled_volume",
                                             "commission", "trader_id", "deal_type")}
                            print(f"    Sample deal: {show}")
                    except Exception as e:
                        print(f"    Sample deal fetch failed: {e}")

        except Exception as e:
            _report("reporting_db", False, f"{env_label} query failed: {e}")
        finally:
            conn.close()

        duration = int((time.monotonic() - t0) * 1000)
        print(f"  [{env_label}] {duration}ms")


# ── Summary ────────────────────────────────────────────────────────────────────

def print_summary() -> None:
    print("\n" + "=" * 68)
    print("FINAL REPORT")
    print("=" * 68)

    for system in ("manager_api", "reporting_db"):
        results = [r for r in _results if r["system"] == system]
        if not results:
            continue
        ok = all(r["ok"] for r in results)
        icon = "✅" if ok else "❌"
        fetched = sum(r["details"].get("count", 0) for r in results if "count" in r["details"])
        label = "Manager API" if system == "manager_api" else "Reporting DB"
        status = "OK" if ok else "FAILED"
        print(f"{icon} cTrader {label} — {fetched} records  [{status}]")

    if not USE_DB:
        print("\n  Note: Platform DB verification skipped. Set FXDEALER_DB_URL to test ingestion.")

    failures = [r for r in _results if not r["ok"]]
    if failures:
        print(f"\nFailed checks ({len(failures)}):")
        for f in failures:
            print(f"  [{f['system'].upper()}] {f['msg']}")
        sys.exit(1)


if __name__ == "__main__":
    print("AI FXDealer — cTrader End-to-End Test")
    print(f"DB: {'enabled (' + DB_URL[:40] + '...)' if USE_DB else 'disabled (no FXDEALER_DB_URL)'}")

    test_manager_api()
    test_reporting_db()
    print_summary()
