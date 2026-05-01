"""Overview / dashboard summary endpoint."""

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/overview", tags=["overview"])


class OverviewResponse(BaseModel):
    total_accounts: int
    total_deals: int
    open_positions: int
    flagged_accounts: int
    abuse_candidates: int
    live_ticks_mt5: int
    live_ticks_mt4: int
    collectors_healthy: int
    collectors_total: int


@router.get("/", response_model=OverviewResponse)
def get_overview(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    bid = broker_ctx.broker_id

    def count(table: str, extra: str = "") -> int:
        q = f"SELECT COUNT(*) FROM {table} WHERE broker_id = :bid"
        if extra:
            q += f" AND {extra}"
        return db.execute(text(q), {"bid": bid}).scalar() or 0

    flagged_row = db.execute(
        text(
            """
            SELECT COUNT(*) FROM (
                SELECT DISTINCT ON (source_account_id) source_account_id, severity
                FROM re_account_scores WHERE broker_id = :bid
                ORDER BY source_account_id, evaluated_at DESC
            ) s WHERE severity IN ('monitor', 'suspicious', 'abuse_candidate')
            """
        ),
        {"bid": bid},
    ).scalar() or 0

    abuse_row = db.execute(
        text(
            """
            SELECT COUNT(*) FROM (
                SELECT DISTINCT ON (source_account_id) source_account_id, severity
                FROM re_account_scores WHERE broker_id = :bid
                ORDER BY source_account_id, evaluated_at DESC
            ) s WHERE severity = 'abuse_candidate'
            """
        ),
        {"bid": bid},
    ).scalar() or 0

    healthy_collectors = db.execute(
        text(
            """
            SELECT COUNT(*) FROM (
                SELECT DISTINCT ON (source_system, entity) source_system, entity, status
                FROM raw_collector_runs WHERE broker_id = :bid
                ORDER BY source_system, entity, collected_at DESC
            ) sub WHERE status = 'success'
            """
        ),
        {"bid": bid},
    ).scalar() or 0

    total_collectors = db.execute(
        text(
            """
            SELECT COUNT(*) FROM (
                SELECT DISTINCT source_system, entity
                FROM raw_collector_runs WHERE broker_id = :bid
            ) sub
            """
        ),
        {"bid": bid},
    ).scalar() or 0

    return OverviewResponse(
        total_accounts=count("norm_accounts", "status = 'active'"),
        total_deals=count("norm_deals"),
        open_positions=count("norm_positions", "status = 'active'"),
        flagged_accounts=int(flagged_row),
        abuse_candidates=int(abuse_row),
        live_ticks_mt5=count("raw_mt5_ticks"),
        live_ticks_mt4=count("raw_mt4_ticks"),
        collectors_healthy=int(healthy_collectors),
        collectors_total=int(total_collectors),
    )
