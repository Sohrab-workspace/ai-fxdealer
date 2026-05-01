"""Create re_metrics and re_account_scores tables (TimescaleDB hypertables)

Revision ID: 0032
Revises: 0031
Create Date: 2026-04-21

Notes:
- re_metrics: individual metric results per account per evaluation run
  e.g. for SFA: hedge_ratio=0.95, leg_cycling_count=8, swap_pnl_ratio=0.82
  One row per metric per evaluation_id
- re_account_scores: final weighted score per account per evaluation
  Aggregated from re_metrics under same evaluation_id
  severity bands: normal(0-24) | monitor(25-49) | suspicious(50-69) | abuse_candidate(70+)
- Both are TimescaleDB hypertables partitioned by evaluated_at
- No primary key constraints (TimescaleDB requirement)
- evaluation_id uniqueness enforced at application layer
- Retention: 2 years
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0032"
down_revision = "0031"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ── re_metrics ───────────────────────────────────────────────────────────
    op.create_table(
        "re_metrics",

        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("rule_engine_id", postgresql.UUID(as_uuid=True), nullable=False),  # bare UUID for perf
        sa.Column("evaluation_id", postgresql.UUID(as_uuid=True), nullable=False),   # groups metrics from same run
        sa.Column("source_account_id", sa.String(), nullable=False),
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("metric_group", sa.String(), nullable=True),     # A | B | C ... (rule group label)
        sa.Column("metric_name", sa.String(), nullable=False),
        sa.Column("metric_value", sa.Float(), nullable=True),      # raw computed value
        sa.Column("metric_score", sa.Integer(), nullable=True),    # normalized 0-100
        sa.Column("weight", sa.Integer(), nullable=True),
        sa.Column("weighted_score", sa.Float(), nullable=True),    # metric_score * weight / 100
        sa.Column("detail_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("evaluated_at", sa.DateTime(timezone=True), nullable=False),  # hypertable key
    )
    op.create_index("ix_re_metrics_broker_eval", "re_metrics", ["broker_id", "evaluation_id"])
    op.create_index("ix_re_metrics_broker_account_time", "re_metrics", ["broker_id", "source_account_id", "evaluated_at"])
    op.create_index("ix_re_metrics_broker_rule_time", "re_metrics", ["broker_id", "rule_engine_id", "evaluated_at"])

    op.execute("SELECT create_hypertable('re_metrics', 'evaluated_at', if_not_exists => TRUE)")
    op.execute("SELECT add_retention_policy('re_metrics', INTERVAL '2 years', if_not_exists => TRUE)")

    # ── re_account_scores ────────────────────────────────────────────────────
    op.create_table(
        "re_account_scores",

        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("rule_engine_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("evaluation_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("source_account_id", sa.String(), nullable=False),
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("total_score", sa.Integer(), nullable=False),     # 0-100 final weighted score
        sa.Column("severity", sa.String(), nullable=False),
        # normal | monitor | suspicious | abuse_candidate
        sa.Column("score_breakdown_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("evaluated_at", sa.DateTime(timezone=True), nullable=False),  # hypertable key
    )
    # evaluation_id lookup (non-unique in DDL — uniqueness enforced at app layer)
    op.create_index("ix_re_account_scores_eval_id", "re_account_scores", ["evaluation_id"])
    op.create_index("ix_re_account_scores_broker_account_time", "re_account_scores", ["broker_id", "source_account_id", "evaluated_at"])
    op.create_index("ix_re_account_scores_broker_rule_time", "re_account_scores", ["broker_id", "rule_engine_id", "evaluated_at"])
    op.create_index("ix_re_account_scores_severity", "re_account_scores", ["broker_id", "severity", "evaluated_at"])

    op.execute("SELECT create_hypertable('re_account_scores', 'evaluated_at', if_not_exists => TRUE)")
    op.execute("SELECT add_retention_policy('re_account_scores', INTERVAL '2 years', if_not_exists => TRUE)")


def downgrade() -> None:
    op.drop_index("ix_re_account_scores_severity", table_name="re_account_scores")
    op.drop_index("ix_re_account_scores_broker_rule_time", table_name="re_account_scores")
    op.drop_index("ix_re_account_scores_broker_account_time", table_name="re_account_scores")
    op.drop_index("ix_re_account_scores_eval_id", table_name="re_account_scores")
    op.drop_table("re_account_scores")

    op.drop_index("ix_re_metrics_broker_rule_time", table_name="re_metrics")
    op.drop_index("ix_re_metrics_broker_account_time", table_name="re_metrics")
    op.drop_index("ix_re_metrics_broker_eval", table_name="re_metrics")
    op.drop_table("re_metrics")
