"""Base rule engine framework.

Every rule engine (LARB, PGE, SFA, ...) extends BaseRule and implements:
  - HANDLER: str — short code matching re_rule_engines.handler
  - METRIC_WEIGHTS: dict[str, int] — metric_name → weight (must sum to 100)
  - evaluate_account(account_id, broker_id, conn, config) → RuleEvalResult

The WeightedScorer converts raw metric values to 0-100 scores using
per-metric scoring functions, then computes the weighted total.

Severity bands (from skill files):
  0  –  24  →  normal
  25 –  49  →  monitor
  50 –  69  →  suspicious
  70 – 100  →  abuse_candidate
"""

from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

import structlog

log = structlog.get_logger()

# ---------------------------------------------------------------------------
# Severity model
# ---------------------------------------------------------------------------

SEVERITY_BANDS = [
    (70, "abuse_candidate"),
    (50, "suspicious"),
    (25, "monitor"),
    (0,  "normal"),
]


def score_to_severity(score: int) -> str:
    for threshold, label in SEVERITY_BANDS:
        if score >= threshold:
            return label
    return "normal"


# ---------------------------------------------------------------------------
# Data objects
# ---------------------------------------------------------------------------

@dataclass
class MetricResult:
    """Result of computing one metric for an account."""
    metric_group: str          # e.g. "A", "B", "C"
    metric_name: str           # e.g. "hedge_ratio", "swap_pnl_ratio"
    metric_value: float        # raw computed value
    metric_score: int          # normalized 0–100 score
    weight: int                # configured weight
    detail: dict = field(default_factory=dict)  # supporting evidence data

    @property
    def weighted_score(self) -> float:
        return self.metric_score * self.weight / 100


@dataclass
class RuleEvalResult:
    """Complete result of evaluating one account against one rule."""
    handler: str
    broker_id: str
    source_account_id: str
    login: int | None
    evaluation_id: str
    metrics: list[MetricResult]
    evaluated_at: datetime

    @property
    def total_score(self) -> int:
        return min(100, int(sum(m.weighted_score for m in self.metrics)))

    @property
    def severity(self) -> str:
        return score_to_severity(self.total_score)

    @property
    def score_breakdown(self) -> dict[str, float]:
        """Group-level score contribution."""
        groups: dict[str, float] = {}
        for m in self.metrics:
            groups[m.metric_group] = groups.get(m.metric_group, 0.0) + m.weighted_score
        return groups


# ---------------------------------------------------------------------------
# BaseRule
# ---------------------------------------------------------------------------

class BaseRule(ABC):
    """
    Abstract base for all rule engines.

    Subclasses implement evaluate_account() using norm_* tables.
    The framework handles persistence (re_metrics, re_account_scores,
    re_evidence_snapshots) and case creation.
    """

    HANDLER: str = ""           # e.g. "SFA" — must match re_rule_engines.handler
    METRIC_WEIGHTS: dict[str, int] = {}  # metric_name → weight (sum should = 100)

    def __init__(self, rule_engine_id: str):
        self.rule_engine_id = rule_engine_id
        self.log = structlog.get_logger().bind(rule=self.HANDLER)

    @abstractmethod
    def evaluate_account(
        self,
        source_account_id: str,
        broker_id: str,
        conn,                   # SQLAlchemy connection
        config: dict,           # re_rule_configs.config_json (merged with defaults)
    ) -> RuleEvalResult | None:
        """
        Evaluate one account against this rule.

        Returns RuleEvalResult or None if account has insufficient data.
        Should never raise — catch and log internally.
        """
        ...

    def get_default_config(self) -> dict:
        """Default thresholds. Subclass overrides to provide rule-specific defaults."""
        return {
            "evaluation_window_hours": 168,   # 7 days
            "min_score_alert": 50,
        }

    def merge_config(self, db_config: dict | None) -> dict:
        """Merge DB config overrides on top of defaults."""
        cfg = self.get_default_config()
        if db_config:
            cfg.update(db_config)
        return cfg

    def make_evaluation_id(self) -> str:
        return str(uuid.uuid4())

    def save_result(self, result: RuleEvalResult, conn) -> str | None:
        """
        Persist evaluation to re_metrics, re_account_scores, re_evidence_snapshots.
        Returns evidence_snapshot_id or None on failure.
        """
        from sqlalchemy import text

        try:
            now = result.evaluated_at
            snapshot_id = str(uuid.uuid4())

            # ── 1. Insert metric rows ──────────────────────────────────────
            import json
            metric_rows = []
            for m in result.metrics:
                metric_rows.append({
                    "id": str(uuid.uuid4()),
                    "broker_id": result.broker_id,
                    "rule_engine_id": self.rule_engine_id,
                    "evaluation_id": result.evaluation_id,
                    "source_account_id": result.source_account_id,
                    "login": result.login,
                    "metric_group": m.metric_group,
                    "metric_name": m.metric_name,
                    "metric_value": m.metric_value,
                    "metric_score": m.metric_score,
                    "weight": m.weight,
                    "weighted_score": m.weighted_score,
                    "detail_json": json.dumps(m.detail),
                    "evaluated_at": now,
                })

            if metric_rows:
                conn.execute(
                    text(
                        "INSERT INTO re_metrics "
                        "(id, broker_id, rule_engine_id, evaluation_id, source_account_id, login, "
                        "metric_group, metric_name, metric_value, metric_score, weight, weighted_score, "
                        "detail_json, evaluated_at) VALUES "
                        "(:id, :broker_id, :rule_engine_id, :evaluation_id, :source_account_id, :login, "
                        ":metric_group, :metric_name, :metric_value, :metric_score, :weight, :weighted_score, "
                        ":detail_json, :evaluated_at)"
                    ),
                    metric_rows,
                )

            # ── 2. Insert account score ────────────────────────────────────
            conn.execute(
                text(
                    "INSERT INTO re_account_scores "
                    "(id, broker_id, rule_engine_id, evaluation_id, source_account_id, login, "
                    "total_score, severity, score_breakdown_json, evaluated_at) VALUES "
                    "(:id, :broker_id, :rule_engine_id, :evaluation_id, :source_account_id, :login, "
                    ":total_score, :severity, :score_breakdown_json, :evaluated_at)"
                ),
                {
                    "id": str(uuid.uuid4()),
                    "broker_id": result.broker_id,
                    "rule_engine_id": self.rule_engine_id,
                    "evaluation_id": result.evaluation_id,
                    "source_account_id": result.source_account_id,
                    "login": result.login,
                    "total_score": result.total_score,
                    "severity": result.severity,
                    "score_breakdown_json": json.dumps(result.score_breakdown),
                    "evaluated_at": now,
                },
            )

            # ── 3. Build + insert evidence snapshot ───────────────────────
            snapshot = {
                "handler": result.handler,
                "score": result.total_score,
                "severity": result.severity,
                "score_breakdown": result.score_breakdown,
                "metrics": [
                    {
                        "group": m.metric_group,
                        "name": m.metric_name,
                        "value": m.metric_value,
                        "score": m.metric_score,
                        "weight": m.weight,
                        "weighted_score": m.weighted_score,
                        "detail": m.detail,
                    }
                    for m in result.metrics
                ],
                "evaluated_at": now.isoformat(),
            }
            conn.execute(
                text(
                    "INSERT INTO re_evidence_snapshots "
                    "(id, broker_id, rule_engine_id, source_account_id, login, evaluation_id, snapshot_json, created_at) "
                    "VALUES (:id, :broker_id, :rule_engine_id, :source_account_id, :login, :evaluation_id, :snapshot_json, :created_at)"
                ),
                {
                    "id": snapshot_id,
                    "broker_id": result.broker_id,
                    "rule_engine_id": self.rule_engine_id,
                    "source_account_id": result.source_account_id,
                    "login": result.login,
                    "evaluation_id": result.evaluation_id,
                    "snapshot_json": json.dumps(snapshot),
                    "created_at": now,
                },
            )

            conn.commit()

            self.log.info(
                "rule.eval.saved",
                account=result.source_account_id,
                score=result.total_score,
                severity=result.severity,
            )
            return snapshot_id

        except Exception as exc:
            try:
                conn.rollback()
            except Exception:
                pass
            self.log.error("rule.eval.save_error", error=str(exc))
            return None

    def maybe_open_case(
        self,
        result: RuleEvalResult,
        evidence_snapshot_id: str,
        min_score: int,
        conn,
    ) -> str | None:
        """
        Open a new case if score >= min_score and no open case exists for this account+rule.
        Returns case_id or None.
        """
        from sqlalchemy import text

        if result.total_score < min_score:
            return None

        # Check for existing open case
        existing = conn.execute(
            text(
                "SELECT id FROM re_cases WHERE broker_id = :broker_id "
                "AND source_account_id = :account_id AND rule_engine_id = :rule_id "
                "AND status IN ('pending', 'under_review') LIMIT 1"
            ),
            {
                "broker_id": result.broker_id,
                "account_id": result.source_account_id,
                "rule_id": self.rule_engine_id,
            },
        ).mappings().fetchone()

        if existing:
            return str(existing[0])

        import json
        case_id = str(uuid.uuid4())
        conn.execute(
            text(
                "INSERT INTO re_cases "
                "(id, broker_id, source_account_id, login, rule_engine_id, status, severity, score, "
                "title, evidence_snapshot_id, created_by, created_at) "
                "VALUES (:id, :broker_id, :source_account_id, :login, :rule_engine_id, 'pending', "
                ":severity, :score, :title, :evidence_snapshot_id, 'rule_engine', NOW())"
            ),
            {
                "id": case_id,
                "broker_id": result.broker_id,
                "source_account_id": result.source_account_id,
                "login": result.login,
                "rule_engine_id": self.rule_engine_id,
                "severity": result.severity,
                "score": result.total_score,
                "title": f"{self.HANDLER} — {result.severity.replace('_', ' ').title()} (score {result.total_score})",
                "evidence_snapshot_id": evidence_snapshot_id,
            },
        )
        conn.commit()

        self.log.info(
            "rule.case.opened",
            case_id=case_id,
            account=result.source_account_id,
            score=result.total_score,
            severity=result.severity,
        )
        return case_id
