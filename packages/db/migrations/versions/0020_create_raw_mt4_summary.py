"""Create raw_mt4_summary table

Revision ID: 0020
Revises: 0019
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table
- Server-level aggregate open interest per symbol: count, net volume, buy/sell split,
  floating P&L, hedged volume
- All 9 fields extracted (small record, full hybrid)
- Source: mtmanapi.dll SummaryGet() — SymbolSummary struct (9 fields), captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0020"
down_revision = "0019"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_summary",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # All 9 MT4 SymbolSummary fields extracted
        sa.Column("symbol", sa.String(), nullable=False),
        sa.Column("count", sa.Integer(), nullable=True),               # open position count
        sa.Column("volume", sa.Integer(), nullable=True),              # total volume (lots×100)
        sa.Column("volume_buy", sa.Integer(), nullable=True),          # buy side (lots×100)
        sa.Column("volume_sell", sa.Integer(), nullable=True),         # sell side (lots×100)
        sa.Column("profit", sa.Float(), nullable=True),                # total floating P&L
        sa.Column("hedged", sa.Integer(), nullable=True),              # hedged volume (lots×100)
        sa.Column("hedged_buy", sa.Float(), nullable=True),
        sa.Column("hedged_sell", sa.Float(), nullable=True),

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
        CREATE UNIQUE INDEX uq_raw_mt4_summary_active
        ON raw_mt4_summary (broker_id, server_id, symbol)
        WHERE status = 'active'
        """
    )
    op.create_index(
        "ix_raw_mt4_summary_broker_collected",
        "raw_mt4_summary", ["broker_id", sa.text("collected_at DESC")],
    )
    op.create_index("ix_raw_mt4_summary_broker_symbol", "raw_mt4_summary", ["broker_id", "symbol"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt4_summary_broker_symbol", table_name="raw_mt4_summary")
    op.drop_index("ix_raw_mt4_summary_broker_collected", table_name="raw_mt4_summary")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt4_summary_active")
    op.drop_table("raw_mt4_summary")
