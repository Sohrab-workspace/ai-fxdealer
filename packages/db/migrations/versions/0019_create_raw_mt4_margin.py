"""Create raw_mt4_margin table

Revision ID: 0019
Revises: 0018
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table
- Real-time account financial state: balance, equity, margin usage, free margin, floating P&L
- All 13 fields extracted (small record, full hybrid)
- Source: mtmanapi.dll MarginLevelGet() — MarginLevel struct (13 fields), captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0019"
down_revision = "0018"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_margin",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # All 13 MT4 MarginLevel fields extracted
        sa.Column("login", sa.Integer(), nullable=False),
        sa.Column("group_name", sa.String(), nullable=True),            # group
        sa.Column("balance", sa.Float(), nullable=True),
        sa.Column("equity", sa.Float(), nullable=True),                 # balance + floating + credit
        sa.Column("margin", sa.Float(), nullable=True),                 # margin used
        sa.Column("margin_free", sa.Float(), nullable=True),            # free margin
        sa.Column("margin_level", sa.Float(), nullable=True),           # equity/margin × 100 %
        sa.Column("margin_initial", sa.Float(), nullable=True),
        sa.Column("margin_maintenance", sa.Float(), nullable=True),
        sa.Column("profit_loss", sa.Float(), nullable=True),            # realized + unrealized P&L
        sa.Column("assets", sa.Float(), nullable=True),
        sa.Column("liabilities", sa.Float(), nullable=True),
        sa.Column("floating", sa.Float(), nullable=True),               # unrealized P&L only

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
        CREATE UNIQUE INDEX uq_raw_mt4_margin_active
        ON raw_mt4_margin (broker_id, server_id, login)
        WHERE status = 'active'
        """
    )
    op.create_index(
        "ix_raw_mt4_margin_broker_collected",
        "raw_mt4_margin", ["broker_id", sa.text("collected_at DESC")],
    )
    op.create_index("ix_raw_mt4_margin_broker_login", "raw_mt4_margin", ["broker_id", "login"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt4_margin_broker_login", table_name="raw_mt4_margin")
    op.drop_index("ix_raw_mt4_margin_broker_collected", table_name="raw_mt4_margin")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt4_margin_active")
    op.drop_table("raw_mt4_margin")
