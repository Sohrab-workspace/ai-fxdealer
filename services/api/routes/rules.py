"""Rule engine endpoints — account scores and findings."""

from typing import Optional
from fastapi import APIRouter, Depends, Query
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from database import get_db
from middleware.auth import BrokerContext, get_broker_context

router = APIRouter(prefix="/api/v1/rules", tags=["rules"])


class ScoreRow(BaseModel):
    id: str
    source_account_id: str
    login: Optional[int]
    total_score: int
    severity: str
    evaluated_at: str
    rule_engine_id: str


class ScoresResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[ScoreRow]


@router.get("/scores", response_model=ScoresResponse)
def list_scores(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=500),
    severity: Optional[str] = None,
    min_score: Optional[int] = None,
    login: Optional[int] = None,
):
    """Latest rule engine scores per account (most recent evaluation per account)."""
    filters = ["s.broker_id = :bid"]
    params: dict = {"bid": broker_ctx.broker_id}

    if severity:
        filters.append("s.severity = :sev")
        params["sev"] = severity
    if min_score is not None:
        filters.append("s.total_score >= :ms")
        params["ms"] = min_score
    if login is not None:
        filters.append("s.login = :login")
        params["login"] = login

    where = " AND ".join(filters)
    offset = (page - 1) * page_size
    params["limit"] = page_size
    params["offset"] = offset

    # Get latest score per account via window function
    count_sql = f"""
        SELECT COUNT(*) FROM (
            SELECT DISTINCT ON (s.source_account_id)
                s.id, s.source_account_id, s.login, s.total_score, s.severity,
                s.evaluated_at::text, s.rule_engine_id::text
            FROM re_account_scores s
            WHERE {where}
            ORDER BY s.source_account_id, s.evaluated_at DESC
        ) sub
    """
    count_row = db.execute(text(count_sql), params).scalar()

    rows_sql = f"""
        SELECT id, source_account_id, login, total_score, severity,
               evaluated_at::text AS evaluated_at, rule_engine_id::text AS rule_engine_id
        FROM (
            SELECT DISTINCT ON (s.source_account_id)
                s.id::text, s.source_account_id, s.login, s.total_score, s.severity,
                s.evaluated_at, s.rule_engine_id
            FROM re_account_scores s
            WHERE {where}
            ORDER BY s.source_account_id, s.evaluated_at DESC
        ) sub
        ORDER BY total_score DESC
        LIMIT :limit OFFSET :offset
    """
    rows = db.execute(text(rows_sql), params).fetchall()

    return ScoresResponse(
        total=count_row or 0,
        page=page,
        page_size=page_size,
        items=[ScoreRow(**dict(r._mapping)) for r in rows],
    )


class SeveritySummary(BaseModel):
    normal: int
    monitor: int
    suspicious: int
    abuse_candidate: int
    total_scored: int


@router.get("/scores/summary", response_model=SeveritySummary)
def scores_summary(
    broker_ctx: BrokerContext = Depends(get_broker_context),
    db: Session = Depends(get_db),
):
    """Count of accounts by severity from the latest evaluation run per account."""
    rows = db.execute(
        text(
            """
            SELECT severity, COUNT(*) AS cnt FROM (
                SELECT DISTINCT ON (source_account_id)
                    source_account_id, severity
                FROM re_account_scores
                WHERE broker_id = :bid
                ORDER BY source_account_id, evaluated_at DESC
            ) sub
            GROUP BY severity
            """
        ),
        {"bid": broker_ctx.broker_id},
    ).fetchall()

    counts = {r.severity: r.cnt for r in rows}
    total = sum(counts.values())
    return SeveritySummary(
        normal=counts.get("normal", 0),
        monitor=counts.get("monitor", 0),
        suspicious=counts.get("suspicious", 0),
        abuse_candidate=counts.get("abuse_candidate", 0),
        total_scored=total,
    )
