"""Create raw_mt5_ticks table

Revision ID: 0007
Revises: 0006
Create Date: 2026-03-27

Notes:
- TimescaleDB hypertable — partitioned by collected_at
- Retention policy: 90 days (CLAUDE.md: raw tick data)
- MTTick payload does NOT include symbol — collector adds it before storing
- Source: MT5Manager.TickLast() — 8 fields, real payload captured 2026-03-23
  Payload fields (lowercase): ask, bid, datetime, datetime_msc, flags, last, volume, volume_ext
- No ingestion_hash / status / archived_at — ticks are append-only, no superseding
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0007"
down_revision = "0006"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_ticks",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted fields — hybrid raw storage
        sa.Column("symbol", sa.String(), nullable=False),               # added by collector (not in MTTick)
        sa.Column("ask", sa.Float(), nullable=True),                    # ask
        sa.Column("bid", sa.Float(), nullable=True),                    # bid
        sa.Column("last", sa.Float(), nullable=True),                   # last (0 for OTC FX)
        sa.Column("volume", sa.BigInteger(), nullable=True),            # volume
        sa.Column("datetime_msc", sa.BigInteger(), nullable=False),     # datetime_msc (unix ms epoch)
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),  # derived from datetime_msc

        # Full raw payload
        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),

        # Housekeeping — ticks are append-only (no status/archived_at)
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )

    # Convert to TimescaleDB hypertable — partition by collected_at
    op.execute("SELECT create_hypertable('raw_mt5_ticks', 'collected_at')")

    # Primary tick query: all ticks for a symbol in a time window (price feed, spread monitoring)
    op.create_index(
        "ix_raw_mt5_ticks_broker_symbol_collected",
        "raw_mt5_ticks",
        ["broker_id", "symbol", sa.text("collected_at DESC")],
    )

    # Standard base index — all raw tables
    op.create_index(
        "ix_raw_mt5_ticks_broker_collected",
        "raw_mt5_ticks",
        ["broker_id", sa.text("collected_at DESC")],
    )

    # TimescaleDB retention policy — 90 days
    # Matches CLAUDE.md retention table: "Raw tick data → 90 days"
    op.execute("SELECT add_retention_policy('raw_mt5_ticks', INTERVAL '90 days')")


def downgrade() -> None:
    op.execute("SELECT remove_retention_policy('raw_mt5_ticks', if_exists => true)")
    op.drop_index("ix_raw_mt5_ticks_broker_collected", table_name="raw_mt5_ticks")
    op.drop_index("ix_raw_mt5_ticks_broker_symbol_collected", table_name="raw_mt5_ticks")
    op.drop_table("raw_mt5_ticks")
