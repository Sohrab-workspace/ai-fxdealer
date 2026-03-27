"""Create raw_mt5_summary table

Revision ID: 0009
Revises: 0008
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table (low-volume aggregate snapshot)
- Stores symbol-level aggregated open interest across all client accounts
- Used for: daily book overview, exposure monitoring, risk dashboard
- Source: MT5Manager.SummaryGetAll() — 22 fields, real payload captured 2026-03-23
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0009"
down_revision = "0008"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_summary",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT5 fields — hybrid raw storage
        sa.Column("symbol", sa.String(), nullable=False),                       # Symbol e.g. "EURUSD"
        sa.Column("digits", sa.Integer(), nullable=True),                       # Digits
        sa.Column("position_clients", sa.Integer(), nullable=True),             # PositionClients — open count
        sa.Column("profit_clients", sa.Float(), nullable=True),                 # ProfitClients — floating P&L
        sa.Column("profit_full_clients", sa.Float(), nullable=True),            # ProfitFullClients (incl. swap/commission)
        sa.Column("profit_uncovered", sa.Float(), nullable=True),               # ProfitUncovered — unhedged P&L
        sa.Column("profit_uncovered_full", sa.Float(), nullable=True),          # ProfitUncoveredFull
        sa.Column("volume_buy_clients", sa.BigInteger(), nullable=True),        # VolumeBuyClients (MT5 units)
        sa.Column("volume_sell_clients", sa.BigInteger(), nullable=True),       # VolumeSellClients (MT5 units)
        sa.Column("volume_buy_clients_ext", sa.BigInteger(), nullable=True),    # VolumeBuyClientsExt
        sa.Column("volume_sell_clients_ext", sa.BigInteger(), nullable=True),   # VolumeSellClientsExt
        sa.Column("volume_net", sa.Float(), nullable=True),                     # VolumeNet — net buy minus sell

        # Full raw payload (remaining 10 fields: coverage columns, PriceBuy/Sell, PositionCoverage)
        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),

        # Housekeeping
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ingestion_hash", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )

    # One active summary record per symbol per (broker, server)
    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt5_summary_active
        ON raw_mt5_summary (broker_id, server_id, symbol)
        WHERE status = 'active'
        """
    )

    op.create_index(
        "ix_raw_mt5_summary_broker_collected",
        "raw_mt5_summary",
        ["broker_id", sa.text("collected_at DESC")],
    )
    # Symbol lookup for book overview and exposure monitoring dashboards
    op.create_index("ix_raw_mt5_summary_broker_symbol", "raw_mt5_summary", ["broker_id", "symbol"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt5_summary_broker_symbol", table_name="raw_mt5_summary")
    op.drop_index("ix_raw_mt5_summary_broker_collected", table_name="raw_mt5_summary")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_summary_active")
    op.drop_table("raw_mt5_summary")
