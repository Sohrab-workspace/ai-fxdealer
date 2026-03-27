"""Create raw_mt5_orders table

Revision ID: 0003
Revises: 0002
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table
- Covers both active (pending) and historical (filled/cancelled) orders —
  same MTOrder structure returned by OrderGetByGroup and HistoryRequestByGroup
- Source: MT5Manager.HistoryRequestByGroup() — 30 fields, real payload captured 2026-03-23
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_orders",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT5 fields — hybrid raw storage
        sa.Column("order_id", sa.BigInteger(), nullable=False),          # Order
        sa.Column("login", sa.BigInteger(), nullable=False),              # Login
        sa.Column("symbol", sa.String(), nullable=True),                  # Symbol
        sa.Column("type", sa.Integer(), nullable=True),                   # Type (EnOrderType)
        sa.Column("state", sa.Integer(), nullable=True),                  # State (4=filled, 3=cancelled)
        sa.Column("position_id", sa.BigInteger(), nullable=True),         # PositionID
        sa.Column("volume_initial", sa.BigInteger(), nullable=True),      # VolumeInitial (MT5 units)
        sa.Column("volume_current", sa.BigInteger(), nullable=True),      # VolumeCurrent (remaining)
        sa.Column("price_order", sa.Float(), nullable=True),              # PriceOrder (requested)
        sa.Column("price_current", sa.Float(), nullable=True),            # PriceCurrent (market at collection)
        sa.Column("time_setup_msc", sa.BigInteger(), nullable=True),      # TimeSetupMsc (placement ms epoch)
        sa.Column("time_done_msc", sa.BigInteger(), nullable=True),       # TimeDoneMsc (fill/cancel ms epoch)
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),  # derived from TimeSetupMsc
        sa.Column("external_id", sa.String(), nullable=True),             # ExternalID (gateway order ID)

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

    # Deduplication — one active record per (broker, server, order ticket)
    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt5_orders_active
        ON raw_mt5_orders (broker_id, server_id, order_id)
        WHERE status = 'active'
        """
    )

    op.create_index(
        "ix_raw_mt5_orders_broker_collected",
        "raw_mt5_orders",
        ["broker_id", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt5_orders_broker_login_collected",
        "raw_mt5_orders",
        ["broker_id", "login", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt5_orders_broker_symbol_collected",
        "raw_mt5_orders",
        ["broker_id", "symbol", sa.text("collected_at DESC")],
    )


def downgrade() -> None:
    op.drop_index("ix_raw_mt5_orders_broker_symbol_collected", table_name="raw_mt5_orders")
    op.drop_index("ix_raw_mt5_orders_broker_login_collected", table_name="raw_mt5_orders")
    op.drop_index("ix_raw_mt5_orders_broker_collected", table_name="raw_mt5_orders")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_orders_active")
    op.drop_table("raw_mt5_orders")
