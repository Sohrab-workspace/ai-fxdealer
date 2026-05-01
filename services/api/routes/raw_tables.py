"""Generic raw table browser endpoint — dev tooling."""

from typing import Optional, Any
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/raw", tags=["raw_tables"])

RAW_TABLES = frozenset({
    "raw_mt5_accounts", "raw_mt5_deals", "raw_mt5_positions",
    "raw_mt5_orders", "raw_mt5_ticks", "raw_mt5_server_logs",
    "raw_mt5_symbols", "raw_mt5_groups",
    "raw_mt4_accounts", "raw_mt4_deals", "raw_mt4_positions",
    "raw_mt4_orders", "raw_mt4_ticks", "raw_mt4_server_logs",
    "raw_mt4_symbols", "raw_mt4_groups",
    "raw_ctrader_accounts", "raw_ctrader_deals", "raw_ctrader_positions",
    "raw_ctrader_orders", "raw_ctrader_symbols", "raw_ctrader_ticks",
    "raw_ctrader_groups", "raw_ctrader_execution_reports",
})

EXCLUDE_COLS = frozenset({"payload_json", "ingestion_hash"})

UUID_TYPES = frozenset({"uuid"})
TS_TYPES = frozenset({
    "timestamp with time zone", "timestamp without time zone", "date"
})
TEXT_TYPES = frozenset({"character varying", "text", "character", "varchar"})


class RawTableResponse(BaseModel):
    table: str
    total: int
    page: int
    page_size: int
    columns: list[str]
    items: list[dict[str, Any]]


@router.get("/{table_name}", response_model=RawTableResponse)
def browse_raw_table(
    table_name: str,
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    search: Optional[str] = Query(None, max_length=100),
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    if table_name not in RAW_TABLES:
        raise HTTPException(status_code=404, detail="Table not in allowlist")

    col_rows = db.execute(
        text("""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = :tbl AND table_schema = 'public'
            ORDER BY ordinal_position
        """),
        {"tbl": table_name},
    ).fetchall()

    if not col_rows:
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found in DB")

    columns = [r[0] for r in col_rows if r[0] not in EXCLUDE_COLS]
    col_type_map: dict[str, str] = {r[0]: r[1] for r in col_rows if r[0] not in EXCLUDE_COLS}
    text_cols = [c for c in columns if col_type_map.get(c, "") in TEXT_TYPES]

    bid = broker_ctx.broker_id
    offset = (page - 1) * page_size
    params: dict[str, Any] = {"bid": bid, "limit": page_size, "offset": offset}
    where_parts = ["broker_id = :bid"]

    if search and text_cols:
        search_conds = " OR ".join(f'"{c}" ILIKE :search' for c in text_cols[:8])
        where_parts.append(f"({search_conds})")
        params["search"] = f"%{search}%"

    where_sql = " AND ".join(where_parts)

    # Cast UUIDs and timestamps to text for clean serialization
    select_parts = []
    for c in columns:
        dt = col_type_map.get(c, "")
        if dt in UUID_TYPES or dt in TS_TYPES:
            select_parts.append(f'"{c}"::text AS "{c}"')
        else:
            select_parts.append(f'"{c}"')
    col_list = ", ".join(select_parts)

    total = db.execute(
        text(f"SELECT COUNT(*) FROM {table_name} WHERE {where_sql}"), params
    ).scalar() or 0

    sort_col = (
        "collected_at" if "collected_at" in columns
        else "created_at" if "created_at" in columns
        else columns[0]
    )

    rows = db.execute(
        text(
            f'SELECT {col_list} FROM {table_name} WHERE {where_sql} '
            f'ORDER BY "{sort_col}" DESC LIMIT :limit OFFSET :offset'
        ),
        params,
    ).fetchall()

    items: list[dict[str, Any]] = []
    for row in rows:
        d: dict[str, Any] = {}
        for col, val in zip(columns, row):
            if val is None:
                d[col] = None
            elif isinstance(val, (int, float, bool)):
                d[col] = val
            else:
                d[col] = str(val)
        items.append(d)

    return RawTableResponse(
        table=table_name,
        total=total,
        page=page,
        page_size=page_size,
        columns=columns,
        items=items,
    )
