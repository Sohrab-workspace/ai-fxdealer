"""Create raw_mt5_exposure table

Revision ID: 0008
Revises: 0007
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table (low-volume aggregate snapshot)
- Stores currency-level net exposure across all client accounts
- Note: Symbol = currency name (e.g. "EUR"), NOT a trading symbol like "EURUSD"
- Source: MT5Manager.ExposureGetAll() — 6 fields, real payload captured 2026-03-23
- All 6 fields extracted (record is small enough for full hybrid)
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0008"
down_revision = "0007"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_exposure",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # All 6 MT5 fields extracted
        sa.Column("symbol", sa.String(), nullable=False),           # Symbol — currency name e.g. "EUR"
        sa.Column("digits", sa.Integer(), nullable=True),           # Digits
        sa.Column("price_rate", sa.Float(), nullable=True),         # PriceRate — FX rate to base currency
        sa.Column("volume_clients", sa.Float(), nullable=True),     # VolumeClients — net client exposure
        sa.Column("volume_coverage", sa.Float(), nullable=True),    # VolumeCoverage — hedged portion
        sa.Column("volume_net", sa.Float(), nullable=True),         # VolumeNet — net after coverage

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

    # One active exposure record per currency per (broker, server)
    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt5_exposure_active
        ON raw_mt5_exposure (broker_id, server_id, symbol)
        WHERE status = 'active'
        """
    )

    op.create_index(
        "ix_raw_mt5_exposure_broker_collected",
        "raw_mt5_exposure",
        ["broker_id", sa.text("collected_at DESC")],
    )


def downgrade() -> None:
    op.drop_index("ix_raw_mt5_exposure_broker_collected", table_name="raw_mt5_exposure")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_exposure_active")
    op.drop_table("raw_mt5_exposure")
