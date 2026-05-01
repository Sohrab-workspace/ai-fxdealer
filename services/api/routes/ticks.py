"""Ticks endpoints — latest price feed from MT4 and MT5."""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/ticks", tags=["ticks"])


class TickRow(BaseModel):
    symbol: str
    bid: Optional[float]
    ask: Optional[float]
    source_system: str
    collected_at: str


class TicksResponse(BaseModel):
    items: list[TickRow]


@router.get("/latest", response_model=TicksResponse)
def latest_ticks(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
    source_system: Optional[str] = None,
    symbol: Optional[str] = None,
):
    """Returns the most recent tick per symbol across MT4 and MT5."""
    filters_mt5 = ["broker_id = :bid"]
    filters_mt4 = ["broker_id = :bid"]
    params: dict = {"bid": broker_ctx.broker_id}

    if symbol:
        filters_mt5.append("symbol ILIKE :sym")
        filters_mt4.append("symbol ILIKE :sym")
        params["sym"] = f"%{symbol}%"

    where_mt5 = " AND ".join(filters_mt5)
    where_mt4 = " AND ".join(filters_mt4)

    parts = []
    if not source_system or source_system == "mt5":
        parts.append(
            f"SELECT * FROM ("
            f"SELECT DISTINCT ON (symbol) symbol, bid, ask, 'mt5' AS source_system, "
            f"collected_at::text AS collected_at "
            f"FROM raw_mt5_ticks WHERE {where_mt5} ORDER BY symbol, collected_at DESC"
            f") mt5_latest"
        )
    if not source_system or source_system == "mt4":
        parts.append(
            f"SELECT * FROM ("
            f"SELECT DISTINCT ON (symbol) symbol, bid, ask, 'mt4' AS source_system, "
            f"collected_at::text AS collected_at "
            f"FROM raw_mt4_ticks WHERE {where_mt4} ORDER BY symbol, collected_at DESC"
            f") mt4_latest"
        )

    if not parts:
        return TicksResponse(items=[])

    sql = " UNION ALL ".join(parts) + " ORDER BY symbol"
    rows = db.execute(text(sql), params).fetchall()

    return TicksResponse(items=[TickRow(**dict(r._mapping)) for r in rows])
