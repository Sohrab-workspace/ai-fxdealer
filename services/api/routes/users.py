"""Trader/user profiles endpoint — norm_accounts joined with risk scores."""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/users", tags=["users"])


class UserRow(BaseModel):
    id: str
    login: Optional[int]
    account_name: Optional[str]
    source_system: str
    country: Optional[str]
    account_status: Optional[str]
    is_demo: Optional[int]
    currency: Optional[str]
    last_access_ts: Optional[int]
    risk_level: str


class UsersResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[UserRow]


class UserStatsResponse(BaseModel):
    total: int
    live: int
    demo: int
    high_risk: int


class ChartPoint(BaseModel):
    label: str
    count: int


class UserChartsResponse(BaseModel):
    status_dist: list[ChartPoint]
    risk_dist: list[ChartPoint]


@router.get("/stats", response_model=UserStatsResponse)
def user_stats(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    bid = broker_ctx.broker_id

    total = db.execute(
        text("SELECT COUNT(*) FROM norm_accounts WHERE broker_id = :bid AND status = 'active'"),
        {"bid": bid},
    ).scalar() or 0

    live = db.execute(
        text("SELECT COUNT(*) FROM norm_accounts WHERE broker_id = :bid AND status = 'active' AND (is_demo = 0 OR is_demo IS NULL)"),
        {"bid": bid},
    ).scalar() or 0

    demo = db.execute(
        text("SELECT COUNT(*) FROM norm_accounts WHERE broker_id = :bid AND status = 'active' AND is_demo = 1"),
        {"bid": bid},
    ).scalar() or 0

    high_risk = db.execute(
        text("""
            SELECT COUNT(DISTINCT source_account_id)
            FROM (
                SELECT DISTINCT ON (source_account_id)
                    source_account_id, severity
                FROM re_account_scores
                WHERE broker_id = :bid
                ORDER BY source_account_id, evaluated_at DESC
            ) s
            WHERE severity IN ('abuse_candidate', 'suspicious')
        """),
        {"bid": bid},
    ).scalar() or 0

    return UserStatsResponse(total=total, live=live, demo=demo, high_risk=high_risk)


@router.get("/charts", response_model=UserChartsResponse)
def user_charts(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    bid = broker_ctx.broker_id

    status_rows = db.execute(
        text("""
            SELECT COALESCE(source_system, 'unknown') AS label, COUNT(*) AS count
            FROM norm_accounts
            WHERE broker_id = :bid AND status = 'active'
            GROUP BY source_system
            ORDER BY count DESC
        """),
        {"bid": bid},
    ).fetchall()

    risk_rows = db.execute(
        text("""
            SELECT severity AS label, COUNT(*) AS count
            FROM (
                SELECT DISTINCT ON (source_account_id)
                    source_account_id, severity
                FROM re_account_scores
                WHERE broker_id = :bid
                ORDER BY source_account_id, evaluated_at DESC
            ) s
            GROUP BY severity
            ORDER BY count DESC
        """),
        {"bid": bid},
    ).fetchall()

    return UserChartsResponse(
        status_dist=[ChartPoint(label=r[0], count=r[1]) for r in status_rows],
        risk_dist=[ChartPoint(label=r[0], count=r[1]) for r in risk_rows],
    )


@router.get("/", response_model=UsersResponse)
def list_users(
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    search: Optional[str] = Query(None, max_length=100),
    source_system: Optional[str] = Query(None),
    risk_level: Optional[str] = Query(None),
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    bid = broker_ctx.broker_id
    offset = (page - 1) * page_size
    where_parts = ["na.broker_id = :bid", "na.status = 'active'"]
    params: dict = {"bid": bid, "limit": page_size, "offset": offset}

    if search:
        where_parts.append("(na.login::text ILIKE :search OR na.account_name ILIKE :search)")
        params["search"] = f"%{search}%"
    if source_system:
        where_parts.append("na.source_system = :source_system")
        params["source_system"] = source_system
    if risk_level:
        where_parts.append("COALESCE(latest_s.severity, 'unscored') = :risk_level")
        params["risk_level"] = risk_level

    where_sql = " AND ".join(where_parts)

    base_query = f"""
        FROM norm_accounts na
        LEFT JOIN LATERAL (
            SELECT severity
            FROM re_account_scores ras
            WHERE ras.source_account_id = na.source_account_id
              AND ras.broker_id = :bid
            ORDER BY ras.evaluated_at DESC
            LIMIT 1
        ) latest_s ON true
        WHERE {where_sql}
    """

    total = db.execute(text(f"SELECT COUNT(*) {base_query}"), params).scalar() or 0

    rows = db.execute(
        text(f"""
            SELECT
                na.id::text,
                na.login,
                na.account_name,
                na.source_system,
                na.country,
                na.account_status,
                na.is_demo,
                na.currency,
                na.last_access_ts,
                COALESCE(latest_s.severity, 'unscored') AS risk_level
            {base_query}
            ORDER BY na.login ASC NULLS LAST
            LIMIT :limit OFFSET :offset
        """),
        params,
    ).fetchall()

    return UsersResponse(
        total=total,
        page=page,
        page_size=page_size,
        items=[UserRow(**dict(r._mapping)) for r in rows],
    )
