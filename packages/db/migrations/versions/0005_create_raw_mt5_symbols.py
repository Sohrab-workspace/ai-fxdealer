"""Create raw_mt5_symbols table

Revision ID: 0005
Revises: 0004
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table (low-volume config/reference per CLAUDE.md)
- Re-synced periodically to capture spread, swap, and contract specification changes
- Source: MT5Manager.SymbolGetArray() — 89 fields, real payload captured 2026-03-23
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0005"
down_revision = "0004"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_symbols",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT5 fields — hybrid raw storage
        sa.Column("symbol", sa.String(), nullable=False),               # Symbol — e.g. "EURUSD"
        sa.Column("description", sa.String(), nullable=True),           # Description — "Euro vs US Dollar"
        sa.Column("path", sa.String(), nullable=True),                  # Path — "FX\Forex\EURUSD"
        sa.Column("currency_base", sa.String(), nullable=True),         # CurrencyBase — "EUR"
        sa.Column("currency_profit", sa.String(), nullable=True),       # CurrencyProfit — "USD"
        sa.Column("currency_margin", sa.String(), nullable=True),       # CurrencyMargin — "EUR"
        sa.Column("digits", sa.Integer(), nullable=True),               # Digits — price decimal places
        sa.Column("contract_size", sa.Float(), nullable=True),          # ContractSize — 100000.0 for forex
        sa.Column("spread", sa.Integer(), nullable=True),               # Spread — points (0=floating)
        sa.Column("trade_mode", sa.Integer(), nullable=True),           # TradeMode — 0=disabled…4=full
        sa.Column("calc_mode", sa.Integer(), nullable=True),            # CalcMode — margin calculation mode
        sa.Column("swap_long", sa.Float(), nullable=True),              # SwapLong — overnight buy swap
        sa.Column("swap_short", sa.Float(), nullable=True),             # SwapShort — overnight sell swap

        # Full raw payload
        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),

        # Housekeeping
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ingestion_hash", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )

    # Deduplication — one active spec snapshot per (broker, server, symbol)
    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt5_symbols_active
        ON raw_mt5_symbols (broker_id, server_id, symbol)
        WHERE status = 'active'
        """
    )

    # Symbol lookup (rule engine, spread monitoring, swap abuse detection)
    op.create_index("ix_raw_mt5_symbols_broker_symbol", "raw_mt5_symbols", ["broker_id", "symbol"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt5_symbols_broker_symbol", table_name="raw_mt5_symbols")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_symbols_active")
    op.drop_table("raw_mt5_symbols")
