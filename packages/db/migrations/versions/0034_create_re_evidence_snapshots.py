"""Create re_evidence_snapshots table

Revision ID: 0034
Revises: 0033
Create Date: 2026-04-21

Notes:
- Immutable evidence packages captured at evaluation time
- Contains full picture: metric details, raw data references, score breakdown
- Links to re_account_scores via evaluation_id
- Links to re_cases via case_id (nullable — snapshots exist before case is opened)
- Never modified after creation — soft-delete not applicable
- Plain PostgreSQL
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0034"
down_revision = "0033"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "re_evidence_snapshots",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("rule_engine_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_account_id", sa.String(), nullable=True),
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("evaluation_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("snapshot_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        # Full evidence: {
        #   score: int,
        #   severity: str,
        #   metrics: [{group, name, value, score, weight, detail}],
        #   account_summary: {login, group, balance, swap_free, ...},
        #   deal_sample: [...],   -- representative deals
        #   position_sample: [...],
        #   raw_refs: [uuid, ...]  -- raw_id references
        # }
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )
    op.create_index("ix_re_evidence_broker_account", "re_evidence_snapshots", ["broker_id", "source_account_id"])
    op.create_index("ix_re_evidence_evaluation_id", "re_evidence_snapshots", ["evaluation_id"])


def downgrade() -> None:
    op.drop_index("ix_re_evidence_evaluation_id", table_name="re_evidence_snapshots")
    op.drop_index("ix_re_evidence_broker_account", table_name="re_evidence_snapshots")
    op.drop_table("re_evidence_snapshots")
