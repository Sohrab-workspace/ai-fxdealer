"""Create raw_mt5_deals table

Revision ID: 0001
Revises:
Create Date: 2026-03-27

Notes:
- TimescaleDB hypertable partitioned by collected_at
- Retention policy: 2 years (CLAUDE.md: raw deals, orders, positions)
- Hybrid raw storage: key fields extracted for indexing, full payload in payload_json
- Source: MT5Manager.DealRequestByGroup() — 38 fields, real payload captured 2026-03-23
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0001"
down_revision = "0000"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_deals",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT5 fields — hybrid raw storage
        sa.Column("deal_id", sa.BigInteger(), nullable=False),      # Deal
        sa.Column("login", sa.BigInteger(), nullable=False),         # Login
        sa.Column("symbol", sa.String(), nullable=True),             # Symbol
        sa.Column("action", sa.Integer(), nullable=False),           # Action (EnDealAction)
        sa.Column("entry", sa.Integer(), nullable=True),             # Entry (0=in,1=out,2=inout,3=out_by)
        sa.Column("order_id", sa.BigInteger(), nullable=True),       # Order
        sa.Column("position_id", sa.BigInteger(), nullable=True),    # PositionID
        sa.Column("volume", sa.BigInteger(), nullable=True),         # Volume (÷10000 = lots)
        sa.Column("price", sa.Float(), nullable=True),               # Price
        sa.Column("profit", sa.Float(), nullable=True),              # Profit
        sa.Column("commission", sa.Float(), nullable=True),          # Commission
        sa.Column("storage", sa.Float(), nullable=True),             # Storage (swap)
        sa.Column("time_msc", sa.BigInteger(), nullable=False),      # TimeMsc (unix ms epoch)
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),   # derived from TimeMsc
        sa.Column("external_id", sa.String(), nullable=True),        # ExternalID (gateway deal ID)

        # Full raw payload — never modified after insert
        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),

        # Raw table housekeeping
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ingestion_hash", sa.String(), nullable=True),
        sa.Column(
            "status",
            sa.String(),
            nullable=False,
            server_default="active",  # active | archived | superseded
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )

    # Convert to TimescaleDB hypertable — partition by collected_at
    op.execute("SELECT create_hypertable('raw_mt5_deals', 'collected_at')")

    # Standard base index — required on all raw tables (broker_id, collected_at DESC)
    op.create_index(
        "ix_raw_mt5_deals_broker_collected",
        "raw_mt5_deals",
        ["broker_id", sa.text("collected_at DESC")],
    )

    # Account-level queries — investigation panel, rule engine, abuse detection
    op.create_index(
        "ix_raw_mt5_deals_broker_login_collected",
        "raw_mt5_deals",
        ["broker_id", "login", sa.text("collected_at DESC")],
    )

    # Symbol-level queries — exposure monitoring, symbol-based rule engine
    op.create_index(
        "ix_raw_mt5_deals_broker_symbol_collected",
        "raw_mt5_deals",
        ["broker_id", "symbol", sa.text("collected_at DESC")],
    )

    # Partial unique index — one active record per (broker, server, deal ticket)
    # Re-syncs and corrections create superseded records instead of replacing
    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt5_deals_active
        ON raw_mt5_deals (broker_id, server_id, deal_id)
        WHERE status = 'active'
        """
    )

    # TimescaleDB retention policy — 2 years
    # Matches CLAUDE.md retention table: "Raw deals, orders, positions → 2 years"
    op.execute("SELECT add_retention_policy('raw_mt5_deals', INTERVAL '2 years')")


def downgrade() -> None:
    op.execute(
        "SELECT remove_retention_policy('raw_mt5_deals', if_exists => true)"
    )
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_deals_active")
    op.drop_index("ix_raw_mt5_deals_broker_symbol_collected", table_name="raw_mt5_deals")
    op.drop_index("ix_raw_mt5_deals_broker_login_collected", table_name="raw_mt5_deals")
    op.drop_index("ix_raw_mt5_deals_broker_collected", table_name="raw_mt5_deals")
    op.drop_table("raw_mt5_deals")
