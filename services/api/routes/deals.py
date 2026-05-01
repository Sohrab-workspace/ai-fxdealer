"""Deals endpoints — normalized deals (closed trades) across all source systems."""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/deals", tags=["deals"])


class DealRow(BaseModel):
    id: str
    source_system: str
    source_deal_id: str
    source_account_id: str
    login: Optional[int]
    symbol: Optional[str]
    direction: Optional[int]
    volume_lots: Optional[float]
    price: Optional[float]
    profit: Optional[float]
    commission: Optional[float]
    swap: Optional[float]
    open_time_msc: Optional[int]
    close_time_msc: Optional[int]
    deal_time_msc: int
    duration_ms: Optional[int]
    deal_type: Optional[str]
    deal_time: str


class DealsResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[DealRow]


@router.get("/", response_model=DealsResponse)
def list_deals(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=500),
    source_system: Optional[str] = None,
    login: Optional[int] = None,
    symbol: Optional[str] = None,
    deal_type: Optional[str] = None,
    from_ts: Optional[int] = None,
    to_ts: Optional[int] = None,
):
    filters = ["broker_id = :bid"]
    params: dict = {"bid": broker_ctx.broker_id}

    if source_system:
        filters.append("source_system = :ss")
        params["ss"] = source_system
    if login:
        filters.append("login = :login")
        params["login"] = login
    if symbol:
        filters.append("symbol ILIKE :sym")
        params["sym"] = f"%{symbol}%"
    if deal_type:
        filters.append("deal_type = :dt")
        params["dt"] = deal_type
    if from_ts:
        filters.append("deal_time_msc >= :from_ts")
        params["from_ts"] = from_ts
    if to_ts:
        filters.append("deal_time_msc <= :to_ts")
        params["to_ts"] = to_ts

    where = " AND ".join(filters)
    offset = (page - 1) * page_size
    params["limit"] = page_size
    params["offset"] = offset

    count_row = db.execute(text(f"SELECT COUNT(*) FROM norm_deals WHERE {where}"), params).scalar()
    rows = db.execute(
        text(
            f"SELECT id::text, source_system, source_deal_id, source_account_id, login, symbol, "
            f"direction, volume_lots, price, profit, commission, swap, "
            f"open_time_msc, close_time_msc, deal_time_msc, duration_ms, deal_type, "
            f"deal_time::text AS deal_time "
            f"FROM norm_deals WHERE {where} "
            f"ORDER BY deal_time DESC "
            f"LIMIT :limit OFFSET :offset"
        ),
        params,
    ).fetchall()

    return DealsResponse(
        total=count_row or 0,
        page=page,
        page_size=page_size,
        items=[DealRow(**dict(r._mapping)) for r in rows],
    )
