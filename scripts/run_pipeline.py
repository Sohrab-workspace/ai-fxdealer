"""End-to-end pipeline runner.

Runs all collectors (incremental), normalizers, and rule engines in sequence.
Designed to be run on a schedule (ARQ) or manually for testing.

Usage:
    FXDEALER_DB_URL=postgresql://fxdealer:fxdealer@localhost:5432/fxdealer \
        PYTHONIOENCODING=utf-8 python -X utf8 scripts/run_pipeline.py

    # Skip collectors (normalize + rules only, using existing raw data):
    ... python scripts/run_pipeline.py --skip-collect

    # Run rules only (no collect, no normalize):
    ... python scripts/run_pipeline.py --rules-only

    # Dry run rule engines (compute but don't write to DB):
    ... python scripts/run_pipeline.py --dry-run
"""

from __future__ import annotations

import os
import re
import sys
import time
import argparse
import uuid
from datetime import datetime, timezone
from pathlib import Path

# ── Path setup ────────────────────────────────────────────────────────────────

repo_root = str(Path(__file__).parent.parent)
for p in [
    repo_root,
    str(Path(repo_root) / "packages"),           # parent: enables `from shared.x import`, `from db.x import`
    str(Path(repo_root) / "packages" / "shared"), # direct: enables `from base_collector import`
    str(Path(repo_root) / "packages" / "db"),
    str(Path(repo_root) / "packages" / "queue"),
    str(Path(repo_root) / "services" / "rule-engine"),
]:
    if p not in sys.path:
        sys.path.insert(0, p)

import structlog
structlog.configure(
    processors=[
        structlog.dev.ConsoleRenderer(colors=False),
    ]
)
log = structlog.get_logger()

# ── Configuration ──────────────────────────────────────────────────────────────

DB_URL = os.environ.get("FXDEALER_DB_URL", "postgresql://fxdealer:fxdealer@localhost:5432/fxdealer")

# Test IDs matching what the collectors used
TEST_BROKER_ID  = "00000000-0000-0000-0000-000000000001"
MT5_SERVER_ID   = "00000000-0000-0000-0000-000000000002"
MT4_SERVER_ID   = "00000000-0000-0000-0000-000000000002"   # same server in test
CT_SERVER_ID    = "00000000-0000-0000-0000-000000000004"
TEST_CONNECTION = uuid.UUID("00000000-0000-0000-0000-000000000003")

# ── Credentials from .env.local ────────────────────────────────────────────────

def _parse_sectioned(path: str) -> dict[str, dict[str, str]]:
    sections: dict[str, dict[str, str]] = {}
    current = "global"
    sections[current] = {}
    try:
        text = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return sections
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.lower().endswith("credentials:") or s.lower().endswith("credentials"):
            current = s.rstrip(":").strip().lower()
            sections[current] = {}
            continue
        m = re.match(r'^([A-Za-z][A-Za-z0-9 _\-]*)[\s]*:[\s]*(.*)', s)
        if m:
            key = m.group(1).strip().lower().replace(" ", "_")
            sections[current][key] = m.group(2).strip()
    return sections

_env_local = Path(repo_root) / ".env.local"
_secs = _parse_sectioned(str(_env_local))

def _sec(name: str) -> dict:
    for k, v in _secs.items():
        if name.lower() in k.lower():
            return v
    return {}

_mt5 = _sec("mt5")
_mt4 = _sec("mt4")
_ct  = _sec("ctrader")

MT5_CONFIG = {
    "server":   f"{_mt5.get('server','')}:{_mt5.get('port','443')}",
    "login":    int(_mt5.get("login", "0") or "0"),
    "password": _mt5.get("pass", "") or _mt5.get("password", ""),
}
MT4_CONFIG = {
    "dll_path": _mt4.get("dll_address", ""),
    "server":   f"{_mt4.get('server','')}:{_mt4.get('port','443')}",
    "login":    int(_mt4.get("login", "0") or "0"),
    "password": _mt4.get("pass", "") or _mt4.get("password", ""),
}
CT_CONFIG = {
    "host":     _ct.get("server", "live-managerapi.p.ctrader.com"),
    "port":     int(_ct.get("port", "5011") or "5011"),
    "login":    int(_ct.get("login", "0") or "0"),
    "password": _ct.get("pass", "") or _ct.get("password", ""),
    "plant_id": _ct.get("plant_id", "") or _ct.get("plant", ""),
    "env_name": _ct.get("env_name", "live"),
}

# ── DB helpers ─────────────────────────────────────────────────────────────────

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

_engine = None
def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(DB_URL, pool_pre_ping=True, pool_size=5, max_overflow=10)
    return _engine

def db_count(table: str, status: str = "active") -> int:
    with get_engine().connect() as c:
        return c.execute(text(f"SELECT count(*) FROM {table} WHERE status=:s AND broker_id=:b"),
                         {"s": status, "b": TEST_BROKER_ID}).scalar() or 0


# ── Phase 1: Collectors ────────────────────────────────────────────────────────

def run_mt5_collector(incremental: bool = True) -> dict:
    print("\n[MT5] Starting collector...")
    svc = str(Path(repo_root) / "services" / "collector-mt5")
    if svc not in sys.path:
        sys.path.insert(0, svc)
    # Clear cached modules
    for m in ("collector",):
        sys.modules.pop(m, None)

    try:
        from collector import MT5Collector
    except ImportError as e:
        print(f"  [MT5] Import failed: {e}")
        return {"error": str(e)}

    c = MT5Collector(
        broker_id=uuid.UUID(TEST_BROKER_ID),
        server_id=uuid.UUID(MT5_SERVER_ID),
        connection_id=TEST_CONNECTION,
        config=MT5_CONFIG,
    )
    try:
        c.connect()
        print(f"  [MT5] Connected to {MT5_CONFIG['server']}")
    except Exception as e:
        print(f"  [MT5] Connect failed: {e}")
        return {"error": str(e)}

    now = int(time.time())
    if incremental:
        print("  [MT5] Running incremental_sync...")
        result = c.incremental_sync()
    else:
        print("  [MT5] Running bootstrap_sync (30 days)...")
        result = c.bootstrap_sync(start_time=now - 30 * 86400, end_time=now)

    saved = result.get("records_saved", 0)
    duration = result.get("duration_ms", 0)
    print(f"  [MT5] Done: {saved} records saved in {duration}ms")
    return result


def run_mt4_collector(incremental: bool = True) -> dict:
    print("\n[MT4] Starting collector...")
    if not MT4_CONFIG["dll_path"] or not os.path.exists(MT4_CONFIG["dll_path"]):
        print(f"  [MT4] DLL not found: {MT4_CONFIG['dll_path']}")
        return {"error": "DLL not found", "skipped": True}

    # Swap to MT4 collector path
    mt5_svc = str(Path(repo_root) / "services" / "collector-mt5")
    if mt5_svc in sys.path:
        sys.path.remove(mt5_svc)
    svc = str(Path(repo_root) / "services" / "collector-mt4")
    if svc not in sys.path:
        sys.path.insert(0, svc)
    for m in ("collector", "ctypes_wrapper"):
        sys.modules.pop(m, None)

    try:
        from collector import MT4Collector
    except ImportError as e:
        print(f"  [MT4] Import failed: {e}")
        return {"error": str(e)}

    c = MT4Collector(
        broker_id=uuid.UUID(TEST_BROKER_ID),
        server_id=uuid.UUID(MT4_SERVER_ID),
        connection_id=TEST_CONNECTION,
        config=MT4_CONFIG,
    )
    try:
        c.connect()
        print(f"  [MT4] Connected to {MT4_CONFIG['server']}")
    except Exception as e:
        print(f"  [MT4] Connect failed: {e}")
        return {"error": str(e)}

    now = int(time.time())
    if incremental:
        print("  [MT4] Running incremental_sync...")
        result = c.incremental_sync()
    else:
        print("  [MT4] Running bootstrap_sync (30 days)...")
        result = c.bootstrap_sync(start_time=now - 30 * 86400, end_time=now)

    saved = result.get("records_saved", 0)
    duration = result.get("duration_ms", 0)
    print(f"  [MT4] Done: {saved} records saved in {duration}ms")
    return result


def run_ctrader_collector(incremental: bool = True) -> dict:
    print("\n[cTrader] Starting collector...")
    svc = str(Path(repo_root) / "services" / "collector-ctrader")
    if svc not in sys.path:
        sys.path.insert(0, svc)
    for m in ("collector",):
        sys.modules.pop(m, None)

    try:
        from collector import CTraderCollector
    except ImportError as e:
        print(f"  [cTrader] Import failed: {e}")
        return {"error": str(e)}

    c = CTraderCollector(
        broker_id=uuid.UUID(TEST_BROKER_ID),
        server_id=uuid.UUID(CT_SERVER_ID),
        connection_id=TEST_CONNECTION,
        config=CT_CONFIG,
    )
    try:
        c.connect()
        print(f"  [cTrader] Connected")
    except Exception as e:
        print(f"  [cTrader] Connect failed: {e}")
        return {"error": str(e)}

    now = int(time.time())
    if incremental:
        print("  [cTrader] Running incremental_sync...")
        result = c.incremental_sync()
    else:
        print("  [cTrader] Running bootstrap_sync (30 days)...")
        result = c.bootstrap_sync(start_time=(now - 30 * 86400) * 1000, end_time=now * 1000)

    saved = result.get("records_saved", 0)
    duration = result.get("duration_ms", 0)
    print(f"  [cTrader] Done: {saved} records saved in {duration}ms")
    return result


# ── Phase 2: Normalization ─────────────────────────────────────────────────────

def run_normalization() -> dict:
    print("\n[NORM] Starting normalization pipeline...")
    from normalizers.mt5 import run_mt5_normalization
    from normalizers.mt4 import run_mt4_normalization
    from normalizers.ctrader import run_ctrader_normalization

    engine = get_engine()
    session = sessionmaker(bind=engine)()
    conn = session.connection()
    totals = {}

    try:
        # MT5
        print("  [NORM] MT5...")
        r = run_mt5_normalization(TEST_BROKER_ID, MT5_SERVER_ID, conn)
        totals["mt5"] = r
        print(f"    accounts={r['accounts']} deals={r['deals']} positions={r['positions']} symbols={r['symbols']}")

        # MT4
        print("  [NORM] MT4...")
        r = run_mt4_normalization(TEST_BROKER_ID, MT4_SERVER_ID, conn)
        totals["mt4"] = r
        print(f"    accounts={r['accounts']} deals={r['deals']}")

        # cTrader
        print("  [NORM] cTrader...")
        r = run_ctrader_normalization(TEST_BROKER_ID, CT_SERVER_ID, conn)
        totals["ctrader"] = r
        print(f"    accounts={r['accounts']} deals={r['deals']}")

    finally:
        session.close()

    # Verify norm table counts
    with engine.connect() as c:
        na = c.execute(text("SELECT count(*) FROM norm_accounts WHERE broker_id=:b AND status='active'"), {"b": TEST_BROKER_ID}).scalar()
        nd = c.execute(text("SELECT count(*) FROM norm_deals WHERE broker_id=:b"), {"b": TEST_BROKER_ID}).scalar()
        np = c.execute(text("SELECT count(*) FROM norm_positions WHERE broker_id=:b AND status='active'"), {"b": TEST_BROKER_ID}).scalar()
    print(f"\n  [NORM] DB: norm_accounts={na} norm_deals={nd} norm_positions={np}")
    return totals


# ── Phase 2.5: Group Reconciler ───────────────────────────────────────────────

def run_group_reconciler() -> dict:
    """Reconcile raw group lists against broker_group_swap_settings.

    Inserts newly-seen groups with swap_free=false and queues them in
    broker_group_pending_review so the admin gets notified on next login.
    Must run after normalization so raw_mt5_groups / raw_mt4_groups are current.
    """
    print("\n[GROUPS] Starting group reconciler...")
    from group_reconciler import reconcile_group_swap_settings, get_pending_review_count

    engine = get_engine()
    session = sessionmaker(bind=engine)()
    conn = session.connection()
    totals: dict = {}

    try:
        for source_system, server_id in [("mt5", MT5_SERVER_ID), ("mt4", MT4_SERVER_ID)]:
            r = reconcile_group_swap_settings(TEST_BROKER_ID, server_id, source_system, conn)
            totals[source_system] = r
            print(f"  [{source_system.upper()}] new_groups={r['new_groups']} total_groups={r['total_groups']}")

        pending = get_pending_review_count(TEST_BROKER_ID, conn)
        totals["pending_review"] = pending
        if pending:
            print(f"  [GROUPS] {pending} group(s) pending admin swap-free classification")
    finally:
        session.close()

    return totals


# ── Phase 3: Rule Engines ──────────────────────────────────────────────────────

def run_rules(dry_run: bool = False) -> dict:
    print(f"\n[RULES] Starting rule engine evaluation (dry_run={dry_run})...")
    from engine import run_broker_rules

    results = run_broker_rules(broker_id=TEST_BROKER_ID, dry_run=dry_run)

    if not results:
        print("  [RULES] No results — check that norm_accounts has data")
        return {}

    for handler, stats in results.items():
        ev = stats.get("evaluated", 0)
        sk = stats.get("skipped", 0)
        fl = stats.get("flagged", 0)
        ca = stats.get("cases_opened", 0)
        print(f"  [{handler}] evaluated={ev} skipped={sk} flagged={fl} cases_opened={ca}")

    return results


# ── Phase 4: Log Parser ────────────────────────────────────────────────────────

def run_log_parser() -> dict:
    """Parse raw MT5/MT4 server logs to extract login events.

    Reads raw_mt5_server_logs / raw_mt4_server_logs rows where
    is_login_event=false and message contains 'login from', extracts
    login+IP+CID, writes to account_login_history, and back-fills the
    raw row columns so it isn't re-processed.
    """
    print("\n[LOGS] Starting log parser...")
    from log_parser import run_log_parsing

    engine = get_engine()
    session = sessionmaker(bind=engine)()
    conn = session.connection()

    try:
        r = run_log_parsing(TEST_BROKER_ID, MT5_SERVER_ID, MT4_SERVER_ID, conn)
        mt5_ev = r.get("mt5_login_events", 0)
        mt4_ev = r.get("mt4_login_events", 0)
        print(f"  [LOGS] MT5 login events parsed: {mt5_ev}")
        print(f"  [LOGS] MT4 login events parsed: {mt4_ev}")
    except Exception as e:
        print(f"  [LOGS] Failed: {e}")
        import traceback; traceback.print_exc()
        r = {}
    finally:
        session.close()

    return r


def show_flagged_accounts() -> None:
    print("\n[RESULTS] Flagged accounts (severity != normal):")
    with get_engine().connect() as c:
        # Latest score per account per rule
        rows = c.execute(text("""
            SELECT DISTINCT ON (broker_id, rule_engine_id, source_account_id)
                re.handler, s.source_account_id, s.login, s.total_score, s.severity,
                s.score_breakdown_json, s.evaluated_at
            FROM re_account_scores s
            JOIN re_rule_engines re ON re.id = s.rule_engine_id
            WHERE s.broker_id = :b AND s.severity != 'normal'
            ORDER BY broker_id, rule_engine_id, source_account_id, evaluated_at DESC
        """), {"b": TEST_BROKER_ID}).fetchall()

        if not rows:
            print("  No flagged accounts found.")
            return

        print(f"\n  {'Rule':<8} {'Account':<14} {'Login':<12} {'Score':<7} {'Severity':<20}")
        print("  " + "-" * 70)
        for r in rows:
            print(f"  {r[0]:<8} {r[1]:<14} {str(r[2] or ''):<12} {r[3]:<7} {r[4]}")

        # Show case summary
        cases = c.execute(text("""
            SELECT c.status, re.handler, c.source_account_id, c.login, c.score, c.severity, c.title
            FROM re_cases c
            JOIN re_rule_engines re ON re.id = c.rule_engine_id
            WHERE c.broker_id = :b
            ORDER BY c.created_at DESC LIMIT 20
        """), {"b": TEST_BROKER_ID}).fetchall()

        if cases:
            print(f"\n  [CASES] {len(cases)} cases opened:")
            print(f"  {'Status':<14} {'Rule':<8} {'Account':<14} {'Score':<7} {'Severity'}")
            print("  " + "-" * 70)
            for r in cases:
                print(f"  {r[0]:<14} {r[1]:<8} {r[2]:<14} {r[4]:<7} {r[5]}")


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="AI FXDealer pipeline runner")
    parser.add_argument("--skip-collect", action="store_true",
                        help="Skip collectors, use existing raw data")
    parser.add_argument("--rules-only", action="store_true",
                        help="Skip collectors and normalization")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run rule engines in dry-run mode (no DB writes)")
    parser.add_argument("--bootstrap", action="store_true",
                        help="Run bootstrap (full 30-day) instead of incremental")
    args = parser.parse_args()

    os.environ["FXDEALER_DB_URL"] = DB_URL
    t_start = time.time()

    print("=" * 68)
    print("AI FXDealer — Full Pipeline")
    print(f"  Broker: {TEST_BROKER_ID}")
    print(f"  DB: {DB_URL}")
    print(f"  Mode: {'bootstrap' if args.bootstrap else 'incremental'}")
    print("=" * 68)

    collect_results = {}
    norm_results = {}

    # ── Phase 1: Collect ──────────────────────────────────────────────────
    if not args.skip_collect and not args.rules_only:
        print("\n=== PHASE 1: COLLECTORS ===")
        incremental = not args.bootstrap

        mt5_r = run_mt5_collector(incremental=incremental)
        if not mt5_r.get("error"):
            collect_results["mt5"] = mt5_r

        mt4_r = run_mt4_collector(incremental=incremental)
        if not mt4_r.get("skipped") and not mt4_r.get("error"):
            collect_results["mt4"] = mt4_r
        elif mt4_r.get("skipped"):
            print("  [MT4] Skipped (DLL not available)")

        ct_r = run_ctrader_collector(incremental=incremental)
        if not ct_r.get("error"):
            collect_results["ctrader"] = ct_r

        # Raw DB counts
        print("\n  Raw DB counts after collection:")
        for tbl in ["raw_mt5_accounts", "raw_mt5_deals", "raw_mt4_accounts", "raw_mt4_deals",
                    "raw_ctrader_accounts", "raw_ctrader_deals"]:
            try:
                cnt = db_count(tbl)
                print(f"    {tbl}: {cnt}")
            except Exception:
                pass

    # ── Phase 2: Normalize ────────────────────────────────────────────────
    if not args.rules_only:
        print("\n=== PHASE 2: NORMALIZATION ===")
        try:
            norm_results = run_normalization()
        except Exception as e:
            print(f"  [NORM] Failed: {e}")
            import traceback; traceback.print_exc()

    # ── Phase 2.5: Group Reconciler ───────────────────────────────────────
    if not args.rules_only:
        print("\n=== PHASE 2.5: GROUP RECONCILER ===")
        try:
            run_group_reconciler()
        except Exception as e:
            print(f"  [GROUPS] Failed: {e}")
            import traceback; traceback.print_exc()

    # ── Phase 3: Rule Engines ─────────────────────────────────────────────
    print("\n=== PHASE 3: RULE ENGINES ===")
    try:
        rule_results = run_rules(dry_run=args.dry_run)
    except Exception as e:
        print(f"  [RULES] Failed: {e}")
        import traceback; traceback.print_exc()
        rule_results = {}

    # ── Phase 4: Log Parser ───────────────────────────────────────────────
    if not args.rules_only and not args.dry_run:
        print("\n=== PHASE 4: LOG PARSER ===")
        try:
            run_log_parser()
        except Exception as e:
            print(f"  [LOGS] Failed: {e}")
            import traceback; traceback.print_exc()

    # ── Results ───────────────────────────────────────────────────────────
    if not args.dry_run:
        show_flagged_accounts()

    total_s = time.time() - t_start
    print(f"\n{'='*68}")
    print(f"Pipeline complete in {total_s:.1f}s")
    print(f"{'='*68}")


if __name__ == "__main__":
    main()
