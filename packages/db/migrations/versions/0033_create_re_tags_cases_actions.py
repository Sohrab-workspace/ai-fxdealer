"""Create re_account_tags, re_cases, re_case_actions tables

Revision ID: 0033
Revises: 0032
Create Date: 2026-04-21

Notes:
- re_account_tags: risk labels applied to accounts by rule engine or dealers
  Multiple active tags per account supported
  status: active | removed
- re_cases: investigation case lifecycle
  status: pending → under_review → resolved | terminated
  created_by: rule_engine | manual
- re_case_actions: append-only action log per case
  action_type: monitor | restrict | adjust_balance | convert_account | terminate | note | status_change
- All plain PostgreSQL
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0033"
down_revision = "0032"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ── re_account_tags ──────────────────────────────────────────────────────
    op.create_table(
        "re_account_tags",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("source_account_id", sa.String(), nullable=False),
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("tag", sa.String(), nullable=False),               # LARB | PGE | SFA | HIGH_RISK | MANUAL | etc
        sa.Column("severity", sa.String(), nullable=True),
        sa.Column("tagged_by", sa.String(), nullable=False),         # rule_engine | manual
        sa.Column("rule_engine_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("evidence_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("tagged_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("removed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("removed_by", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),  # active | removed
    )
    op.create_index("ix_re_account_tags_broker_account", "re_account_tags", ["broker_id", "source_account_id"])
    op.create_index("ix_re_account_tags_broker_tag", "re_account_tags", ["broker_id", "tag", "status"])

    # ── re_cases ─────────────────────────────────────────────────────────────
    op.create_table(
        "re_cases",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("source_account_id", sa.String(), nullable=False),
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("rule_engine_id", postgresql.UUID(as_uuid=True), nullable=True),  # NULL for manual cases
        sa.Column("status", sa.String(), nullable=False, server_default="pending"),
        # pending | under_review | resolved | terminated
        sa.Column("severity", sa.String(), nullable=True),
        sa.Column("score", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("summary", sa.String(), nullable=True),
        sa.Column("evidence_snapshot_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("assigned_to", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("created_by", sa.String(), nullable=False),        # rule_engine | manual
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("resolved_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_re_cases_broker_account", "re_cases", ["broker_id", "source_account_id"])
    op.create_index("ix_re_cases_broker_status", "re_cases", ["broker_id", "status", "created_at"])
    op.create_index("ix_re_cases_broker_rule", "re_cases", ["broker_id", "rule_engine_id", "created_at"])

    # ── re_case_actions ──────────────────────────────────────────────────────
    op.create_table(
        "re_case_actions",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("case_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("action_type", sa.String(), nullable=False),
        # monitor | restrict | adjust_balance | convert_account | terminate | note | status_change
        sa.Column("performed_by", postgresql.UUID(as_uuid=True), nullable=True),  # NULL = automated
        sa.Column("detail_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),

        sa.ForeignKeyConstraint(["case_id"], ["re_cases.id"], name="fk_re_case_actions_case"),
    )
    op.create_index("ix_re_case_actions_case_id", "re_case_actions", ["case_id"])
    op.create_index("ix_re_case_actions_broker_time", "re_case_actions", ["broker_id", "created_at"])


def downgrade() -> None:
    op.drop_index("ix_re_case_actions_broker_time", table_name="re_case_actions")
    op.drop_index("ix_re_case_actions_case_id", table_name="re_case_actions")
    op.drop_table("re_case_actions")

    op.drop_index("ix_re_cases_broker_rule", table_name="re_cases")
    op.drop_index("ix_re_cases_broker_status", table_name="re_cases")
    op.drop_index("ix_re_cases_broker_account", table_name="re_cases")
    op.drop_table("re_cases")

    op.drop_index("ix_re_account_tags_broker_tag", table_name="re_account_tags")
    op.drop_index("ix_re_account_tags_broker_account", table_name="re_account_tags")
    op.drop_table("re_account_tags")
