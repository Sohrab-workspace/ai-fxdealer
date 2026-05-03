"""Accounts endpoints — normalized accounts across all source systems."""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/accounts", tags=["accounts"])


class AccountRow(BaseModel):
    id: str
    source_system: str
    source_account_id: str
    login: Optional[int]
    account_name: Optional[str]
    group_name: Optional[str]
    balance: Optional[float]
    equity: Optional[float]
    credit: Optional[float]
    leverage: Optional[int]
    currency: Optional[str]
    country: Optional[str]
    swap_free: Optional[int]
    is_demo: Optional[int]
    account_status: Optional[str]
    registration_ts: Optional[int]
    last_access_ts: Optional[int]


class AccountsResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[AccountRow]


@router.get("/", response_model=AccountsResponse)
def list_accounts(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=500),
    source_system: Optional[str] = None,
    group_name: Optional[str] = None,
    country: Optional[str] = None,
    swap_free: Optional[int] = None,
    search: Optional[str] = None,
):
    filters = ["broker_id = :bid", "status = 'active'"]
    params: dict = {"bid": broker_ctx.broker_id}

    if source_system:
        filters.append("source_system = :ss")
        params["ss"] = source_system
    if group_name:
        filters.append("group_name ILIKE :gn")
        params["gn"] = f"%{group_name}%"
    if country:
        filters.append("country ILIKE :country")
        params["country"] = f"%{country}%"
    if swap_free is not None:
        filters.append("swap_free = :sf")
        params["sf"] = swap_free
    if search:
        filters.append(
            "(account_name ILIKE :search OR source_account_id ILIKE :search "
            "OR CAST(login AS TEXT) ILIKE :search)"
        )
        params["search"] = f"%{search}%"

    where = " AND ".join(filters)
    offset = (page - 1) * page_size
    params["limit"] = page_size
    params["offset"] = offset

    count_row = db.execute(text(f"SELECT COUNT(*) FROM norm_accounts WHERE {where}"), params).scalar()
    rows = db.execute(
        text(
            f"SELECT id::text, source_system, source_account_id, login, account_name, group_name, "
            f"balance, equity, credit, leverage, currency, country, swap_free, is_demo, "
            f"account_status, registration_ts, last_access_ts "
            f"FROM norm_accounts WHERE {where} "
            f"ORDER BY login ASC NULLS LAST "
            f"LIMIT :limit OFFSET :offset"
        ),
        params,
    ).fetchall()

    return AccountsResponse(
        total=count_row or 0,
        page=page,
        page_size=page_size,
        items=[AccountRow(**dict(r._mapping)) for r in rows],
    )


class AccountStatsResponse(BaseModel):
    total: int
    total_balance: float
    avg_balance: float
    negative_count: int


class AccountChartsResponse(BaseModel):
    currency_dist: list[dict]
    balance_ranges: list[dict]


@router.get("/stats", response_model=AccountStatsResponse)
def account_stats(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    bid = broker_ctx.broker_id
    row = db.execute(
        text("""
            SELECT
                COUNT(*)                                   AS total,
                COALESCE(SUM(balance), 0)                  AS total_balance,
                COALESCE(AVG(balance), 0)                  AS avg_balance,
                COUNT(*) FILTER (WHERE balance < 0)        AS negative_count
            FROM norm_accounts
            WHERE broker_id = :bid AND status = 'active'
        """),
        {"bid": bid},
    ).fetchone()
    return AccountStatsResponse(**dict(row._mapping))


@router.get("/charts", response_model=AccountChartsResponse)
def account_charts(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    bid = broker_ctx.broker_id

    currency_rows = db.execute(
        text("""
            SELECT COALESCE(currency, 'Unknown') AS label, COUNT(*) AS count
            FROM norm_accounts
            WHERE broker_id = :bid AND status = 'active'
            GROUP BY currency ORDER BY count DESC LIMIT 8
        """),
        {"bid": bid},
    ).fetchall()

    range_rows = db.execute(
        text("""
            SELECT
                CASE
                    WHEN balance < 0        THEN 'Negative'
                    WHEN balance = 0        THEN 'Zero'
                    WHEN balance < 1000     THEN '$0-1K'
                    WHEN balance < 10000    THEN '$1K-10K'
                    WHEN balance < 100000   THEN '$10K-100K'
                    ELSE                         '$100K+'
                END AS label,
                COUNT(*) AS count
            FROM norm_accounts
            WHERE broker_id = :bid AND status = 'active'
            GROUP BY 1
            ORDER BY count DESC
        """),
        {"bid": bid},
    ).fetchall()

    return AccountChartsResponse(
        currency_dist=[{"label": r[0], "count": r[1]} for r in currency_rows],
        balance_ranges=[{"label": r[0], "count": r[1]} for r in range_rows],
    )


@router.get("/{source_account_id}", response_model=AccountRow)
def get_account(
    source_account_id: str,
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    from fastapi import HTTPException, status as http_status
    row = db.execute(
        text(
            "SELECT id::text, source_system, source_account_id, login, account_name, group_name, "
            "balance, equity, credit, leverage, currency, country, swap_free, is_demo, "
            "account_status, registration_ts, last_access_ts "
            "FROM norm_accounts WHERE broker_id = :bid AND source_account_id = :said AND status = 'active' "
            "LIMIT 1"
        ),
        {"bid": broker_ctx.broker_id, "said": source_account_id},
    ).fetchone()
    if not row:
        raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail="Account not found")
    return AccountRow(**dict(row._mapping))
