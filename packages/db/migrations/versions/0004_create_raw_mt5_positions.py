"""Create raw_mt5_positions table

Revision ID: 0004
Revises: 0003
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table
- Snapshot of currently open positions — closed positions become superseded on next sync
- Source: MT5Manager.PositionGetByGroup() — 30 fields, real payload captured 2026-03-23
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0004"
down_revision = "0003"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_positions",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT5 fields — hybrid raw storage
        sa.Column("position_id", sa.BigInteger(), nullable=False),        # Position
        sa.Column("login", sa.BigInteger(), nullable=False),               # Login
        sa.Column("symbol", sa.String(), nullable=True),                   # Symbol
        sa.Column("action", sa.Integer(), nullable=True),                  # Action (0=buy, 1=sell)
        sa.Column("volume", sa.BigInteger(), nullable=True),               # Volume (MT5 units, ÷10000=lots)
        sa.Column("price_open", sa.Float(), nullable=True),                # PriceOpen
        sa.Column("price_current", sa.Float(), nullable=True),             # PriceCurrent
        sa.Column("profit", sa.Float(), nullable=True),                    # Profit (floating P&L)
        sa.Column("storage", sa.Float(), nullable=True),                   # Storage (accrued swap)
        sa.Column("time_create_msc", sa.BigInteger(), nullable=True),      # TimeCreateMsc (open ms epoch)
        sa.Column("time_update_msc", sa.BigInteger(), nullable=True),      # TimeUpdateMsc (last update ms epoch)
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),  # derived from TimeCreateMsc
        sa.Column("external_id", sa.String(), nullable=True),              # ExternalID

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

    # Deduplication — one active snapshot per (broker, server, position ticket)
    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt5_positions_active
        ON raw_mt5_positions (broker_id, server_id, position_id)
        WHERE status = 'active'
        """
    )

    op.create_index(
        "ix_raw_mt5_positions_broker_collected",
        "raw_mt5_positions",
        ["broker_id", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt5_positions_broker_login_collected",
        "raw_mt5_positions",
        ["broker_id", "login", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt5_positions_broker_symbol_collected",
        "raw_mt5_positions",
        ["broker_id", "symbol", sa.text("collected_at DESC")],
    )


def downgrade() -> None:
    op.drop_index("ix_raw_mt5_positions_broker_symbol_collected", table_name="raw_mt5_positions")
    op.drop_index("ix_raw_mt5_positions_broker_login_collected", table_name="raw_mt5_positions")
    op.drop_index("ix_raw_mt5_positions_broker_collected", table_name="raw_mt5_positions")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_positions_active")
    op.drop_table("raw_mt5_positions")
