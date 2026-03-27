"""Create raw_mt4_groups table

Revision ID: 0016
Revises: 0015
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table (low-volume config/reference per CLAUDE.md)
- ConGroup struct key fields extracted; securities (ConGroupMargin[128]) stored only in payload_json
- Source: mtmanapi.dll GroupsRequest() — ConGroup struct from MT4ManagerAPI.h, captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0016"
down_revision = "0015"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_groups",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted ConGroup key fields
        sa.Column("group_name", sa.String(), nullable=False),             # group — e.g. "real\managers"
        sa.Column("currency", sa.String(), nullable=True),                # account currency e.g. "USD"
        sa.Column("default_leverage", sa.Integer(), nullable=True),
        sa.Column("default_deposit", sa.Float(), nullable=True),          # new account starting balance
        sa.Column("stopping_level", sa.Integer(), nullable=True),         # stop-out level %
        sa.Column("margin_call", sa.Integer(), nullable=True),            # margin call level %
        sa.Column("trading", sa.Integer(), nullable=True),                # 1=enabled, 0=disabled
        sa.Column("commission_base", sa.Float(), nullable=True),
        sa.Column("commission_type", sa.Integer(), nullable=True),        # 0=disabled, 1=per lot, 2=%
        sa.Column("commission_lots", sa.Float(), nullable=True),
        sa.Column("balance_min", sa.Float(), nullable=True),
        sa.Column("interest_rate", sa.Float(), nullable=True),
        sa.Column("tax", sa.Float(), nullable=True),
        sa.Column("hedge_prohibited", sa.Integer(), nullable=True),       # 1=no hedging
        sa.Column("close_fifo", sa.Integer(), nullable=True),             # 1=FIFO closing required

        # securities (ConGroupMargin[128]) stored only in payload_json — complex nested array
        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),

        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ingestion_hash", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )

    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt4_groups_active
        ON raw_mt4_groups (broker_id, server_id, group_name)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_mt4_groups_broker_id", "raw_mt4_groups", ["broker_id"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt4_groups_broker_id", table_name="raw_mt4_groups")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt4_groups_active")
    op.drop_table("raw_mt4_groups")
