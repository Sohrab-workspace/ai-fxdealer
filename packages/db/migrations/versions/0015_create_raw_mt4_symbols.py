"""Create raw_mt4_symbols table

Revision ID: 0015
Revises: 0014
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table (low-volume config/reference per CLAUDE.md)
- Market watch snapshot: current bid/ask, spread, daily high/low
- All 10 fields extracted (small record, full hybrid)
- Source: mtmanapi.dll SymbolInfoGet() — 10 fields from MT4ManagerAPI.h, captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0015"
down_revision = "0014"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_symbols",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # All 10 MT4 SymbolInfo fields extracted
        sa.Column("symbol", sa.String(), nullable=False),
        sa.Column("digits", sa.Integer(), nullable=True),
        sa.Column("spread", sa.Integer(), nullable=True),              # in points
        sa.Column("spread_float", sa.Integer(), nullable=True),        # 1=floating
        sa.Column("bid", sa.Float(), nullable=True),
        sa.Column("ask", sa.Float(), nullable=True),
        sa.Column("session_price", sa.Float(), nullable=True),         # session open price
        sa.Column("high", sa.Float(), nullable=True),                  # daily high
        sa.Column("low", sa.Float(), nullable=True),                   # daily low
        sa.Column("time", sa.BigInteger(), nullable=True),             # last quote unix timestamp

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
        CREATE UNIQUE INDEX uq_raw_mt4_symbols_active
        ON raw_mt4_symbols (broker_id, server_id, symbol)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_mt4_symbols_broker_symbol", "raw_mt4_symbols", ["broker_id", "symbol"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt4_symbols_broker_symbol", table_name="raw_mt4_symbols")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt4_symbols_active")
    op.drop_table("raw_mt4_symbols")
