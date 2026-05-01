"""Rule engine runner.

Orchestrates evaluation of all active rules for a given broker.
Called by ARQ job scheduler or directly for testing.

Usage:
    from engine import run_broker_rules
    run_broker_rules(broker_id="...", source_systems=["mt5"])
"""

from __future__ import annotations

import os
import time
from datetime import datetime, timezone

import structlog
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from rules.sfa import SFARule
from rules.pge import PGERule
from rules.larb import LARBRule

log = structlog.get_logger()

# Rule registry — handler code → class
_RULE_REGISTRY = {
    "SFA":  SFARule,
    "PGE":  PGERule,
    "LARB": LARBRule,
}


def _get_engine():
    url = os.environ.get("FXDEALER_DB_URL")
    if not url:
        raise RuntimeError("FXDEALER_DB_URL not set")
    return create_engine(url, pool_pre_ping=True)


def run_broker_rules(
    broker_id: str,
    *,
    handlers: list[str] | None = None,   # None = run all active
    dry_run: bool = False,               # if True, compute but don't persist
) -> dict:
    """
    Run all active rule engines for a broker.

    Returns summary dict with counts per rule.
    """
    start = time.time()
    engine = _get_engine()
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    results_summary = {}

    try:
        conn = session.connection()

        # ── Load active rule engine configs for this broker ──────────────
        rule_rows = conn.execute(
            text(
                "SELECT re.id, re.handler, re.version, rc.is_active, rc.min_score_alert, "
                "rc.evaluation_window_hours, rc.config_json "
                "FROM re_rule_engines re "
                "LEFT JOIN re_rule_configs rc ON rc.rule_engine_id = re.id "
                "  AND rc.broker_id = :broker_id "
                "WHERE re.is_active = 1 "
                "ORDER BY re.handler"
            ),
            {"broker_id": broker_id},
        ).mappings().fetchall()

        if not rule_rows:
            log.warning("engine.no_rules", broker_id=broker_id)
            return {}

        # ── Load accounts to evaluate ─────────────────────────────────────
        account_rows = conn.execute(
            text(
                "SELECT source_account_id, login FROM norm_accounts "
                "WHERE broker_id = :broker_id AND status = 'active'"
            ),
            {"broker_id": broker_id},
        ).mappings().fetchall()

        if not account_rows:
            log.info("engine.no_accounts", broker_id=broker_id)
            return {}

        accounts = [dict(r) for r in account_rows]
        log.info("engine.run.start", broker_id=broker_id, accounts=len(accounts))

        for rule_row in rule_rows:
            handler = rule_row["handler"]

            if handlers and handler not in handlers:
                continue

            rule_cls = _RULE_REGISTRY.get(handler)
            if not rule_cls:
                log.warning("engine.unknown_handler", handler=handler)
                continue

            # Skip if broker explicitly disabled this rule
            if rule_row["is_active"] is not None and rule_row["is_active"] == 0:
                log.info("engine.rule.disabled", handler=handler, broker_id=broker_id)
                continue

            rule = rule_cls(rule_engine_id=str(rule_row["id"]))
            config = rule_row["config_json"] or {}
            if rule_row["evaluation_window_hours"]:
                config["evaluation_window_hours"] = rule_row["evaluation_window_hours"]
            min_score = rule_row["min_score_alert"] or 50

            evaluated = 0
            skipped = 0
            flagged = 0
            cases_opened = 0

            log.info("engine.rule.start", handler=handler, broker_id=broker_id)

            for acct in accounts:
                account_id = acct["source_account_id"]
                try:
                    result = rule.evaluate_account(
                        source_account_id=account_id,
                        broker_id=broker_id,
                        conn=conn,
                        config=config,
                    )

                    if result is None:
                        skipped += 1
                        continue

                    evaluated += 1

                    if result.total_score > 0:
                        log.debug(
                            "engine.eval",
                            handler=handler,
                            account=account_id,
                            score=result.total_score,
                            severity=result.severity,
                        )

                    if dry_run:
                        if result.severity != "normal":
                            flagged += 1
                        continue

                    snapshot_id = rule.save_result(result, conn)

                    if result.severity != "normal":
                        flagged += 1

                    if snapshot_id and result.severity in ("suspicious", "abuse_candidate"):
                        case_id = rule.maybe_open_case(result, snapshot_id, min_score, conn)
                        if case_id:
                            cases_opened += 1

                except Exception as exc:
                    log.error(
                        "engine.eval.error",
                        handler=handler,
                        account=account_id,
                        error=str(exc),
                    )
                    skipped += 1

            results_summary[handler] = {
                "evaluated": evaluated,
                "skipped": skipped,
                "flagged": flagged,
                "cases_opened": cases_opened,
            }
            log.info(
                "engine.rule.done",
                handler=handler,
                **results_summary[handler],
            )

    except Exception as exc:
        log.error("engine.run.error", broker_id=broker_id, error=str(exc))
        raise
    finally:
        session.close()
        engine.dispose()

    duration_ms = int((time.time() - start) * 1000)
    log.info(
        "engine.run.done",
        broker_id=broker_id,
        duration_ms=duration_ms,
        rules_run=list(results_summary.keys()),
    )
    return results_summary
