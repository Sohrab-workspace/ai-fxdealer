"""Positions endpoints — normalized open positions."""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/positions", tags=["positions"])


class PositionRow(BaseModel):
    id: str
    source_system: str
    source_position_id: str
    source_account_id: str
    login: Optional[int]
    symbol: Optional[str]
    direction: Optional[int]
    volume_lots: Optional[float]
    price_open: Optional[float]
    price_current: Optional[float]
    profit: Optional[float]
    swap: Optional[float]
    open_time_msc: Optional[int]


class PositionsResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[PositionRow]


@router.get("/", response_model=PositionsResponse)
def list_positions(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=500),
    source_system: Optional[str] = None,
    login: Optional[int] = None,
    symbol: Optional[str] = None,
):
    filters = ["broker_id = :bid", "status = 'active'"]
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

    where = " AND ".join(filters)
    offset = (page - 1) * page_size
    params["limit"] = page_size
    params["offset"] = offset

    count_row = db.execute(text(f"SELECT COUNT(*) FROM norm_positions WHERE {where}"), params).scalar()
    rows = db.execute(
        text(
            f"SELECT id::text, source_system, source_position_id, source_account_id, login, symbol, "
            f"direction, volume_lots, price_open, price_current, profit, swap, open_time_msc "
            f"FROM norm_positions WHERE {where} "
            f"ORDER BY profit DESC NULLS LAST "
            f"LIMIT :limit OFFSET :offset"
        ),
        params,
    ).fetchall()

    return PositionsResponse(
        total=count_row or 0,
        page=page,
        page_size=page_size,
        items=[PositionRow(**dict(r._mapping)) for r in rows],
    )
