"""Collector status endpoints."""

from typing import Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/collectors", tags=["collectors"])


class CollectorRunRow(BaseModel):
    id: str
    source_system: str
    entity: Optional[str]
    sync_mode: str
    status: str
    records_fetched: Optional[int]
    records_saved: Optional[int]
    duration_ms: Optional[int]
    error_message: Optional[str]
    collected_at: str


class CollectorStatusResponse(BaseModel):
    items: list[CollectorRunRow]


@router.get("/status", response_model=CollectorStatusResponse)
def collector_status(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    """Latest run per (source_system, entity) pair."""
    rows = db.execute(
        text(
            """
            SELECT DISTINCT ON (source_system, entity)
                id::text, source_system, entity, sync_mode, status,
                records_fetched, records_saved, duration_ms, error_message,
                collected_at::text AS collected_at
            FROM raw_collector_runs
            WHERE broker_id = :bid
            ORDER BY source_system, entity, collected_at DESC
            """
        ),
        {"bid": broker_ctx.broker_id},
    ).fetchall()

    return CollectorStatusResponse(items=[CollectorRunRow(**dict(r._mapping)) for r in rows])


class DBCountsResponse(BaseModel):
    raw_mt5_accounts: int
    raw_mt5_deals: int
    raw_mt4_accounts: int
    raw_mt4_deals: int
    raw_ctrader_accounts: int
    raw_ctrader_deals: int
    norm_accounts: int
    norm_deals: int
    norm_positions: int
    raw_mt5_ticks: int
    raw_mt4_ticks: int


@router.get("/db-counts", response_model=DBCountsResponse)
def db_counts(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    """Quick DB row counts for monitoring."""
    bid = broker_ctx.broker_id

    def count(table: str) -> int:
        return db.execute(text(f"SELECT COUNT(*) FROM {table} WHERE broker_id = :bid"), {"bid": bid}).scalar() or 0

    return DBCountsResponse(
        raw_mt5_accounts=count("raw_mt5_accounts"),
        raw_mt5_deals=count("raw_mt5_deals"),
        raw_mt4_accounts=count("raw_mt4_accounts"),
        raw_mt4_deals=count("raw_mt4_deals"),
        raw_ctrader_accounts=count("raw_ctrader_accounts"),
        raw_ctrader_deals=count("raw_ctrader_deals"),
        norm_accounts=count("norm_accounts"),
        norm_deals=count("norm_deals"),
        norm_positions=count("norm_positions"),
        raw_mt5_ticks=count("raw_mt5_ticks"),
        raw_mt4_ticks=count("raw_mt4_ticks"),
    )
