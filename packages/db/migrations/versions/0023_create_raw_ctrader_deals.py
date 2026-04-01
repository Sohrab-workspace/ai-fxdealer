"""Create raw_ctrader_deals table

Revision ID: 0023
Revises: 0022
Create Date: 2026-04-01

Notes:
- TimescaleDB hypertable partitioned by collected_at
- Retention policy: 2 years
- Source: Spotware Manager API → ProtoManagerDealListReq (payloadType 431)
- Entity: ProtoDeal — complete field mapping in entities.md
- Monetary values (commission, equity) in cents
- Volume in cents of lot size
- create_ts (field 8) is used for time-window pagination — always index this
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0023"
down_revision = "0022"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_ctrader_deals",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted ProtoDeal fields (field numbers from entities.md)
        sa.Column("deal_id", sa.BigInteger(), nullable=False),              # field 1
        sa.Column("order_id", sa.BigInteger(), nullable=True),              # field 2
        sa.Column("position_id", sa.BigInteger(), nullable=True),           # field 3
        sa.Column("trader_id", sa.BigInteger(), nullable=False),            # field 4
        sa.Column("volume", sa.BigInteger(), nullable=True),                # field 5 — ordered (cents of lot)
        sa.Column("filled_volume", sa.BigInteger(), nullable=True),         # field 6 — actual filled
        sa.Column("symbol_id", sa.BigInteger(), nullable=True),             # field 7
        sa.Column("create_ts", sa.BigInteger(), nullable=False),            # field 8 — Unix ms (pagination key)
        sa.Column("execution_ts", sa.BigInteger(), nullable=True),          # field 9 — Unix ms
        sa.Column("execution_price", sa.Float(), nullable=True),            # field 11 — with markup
        sa.Column("trade_side", sa.Integer(), nullable=True),               # field 13 — BUY=1 / SELL=2
        sa.Column("deal_status", sa.Integer(), nullable=True),              # field 14 — ProtoDealStatus
        sa.Column("deal_type", sa.Integer(), nullable=True),                # field 15 — ProtoDealType
        sa.Column("commission", sa.BigInteger(), nullable=True),            # field 17 — cents
        sa.Column("book_type", sa.Integer(), nullable=True),                # field 19 — A=1 / B=2
        sa.Column("lp_execution_price", sa.Float(), nullable=True),        # field 20 — without markup
        sa.Column("money_digits", sa.Integer(), nullable=True),             # field 58
        sa.Column("equity_cents", sa.BigInteger(), nullable=True),          # field 57 — account equity at deal
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),

        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ingestion_hash", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )

    # TimescaleDB hypertable + 2yr retention
    op.execute(
        "SELECT create_hypertable('raw_ctrader_deals', 'collected_at', if_not_exists => TRUE)"
    )
    op.execute(
        "SELECT add_retention_policy('raw_ctrader_deals', INTERVAL '2 years')"
    )

    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_ctrader_deals_active
        ON raw_ctrader_deals (broker_id, server_id, deal_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_ctrader_deals_broker_collected", "raw_ctrader_deals", ["broker_id", "collected_at"])
    op.create_index("ix_raw_ctrader_deals_broker_trader", "raw_ctrader_deals", ["broker_id", "trader_id", "collected_at"])
    op.create_index("ix_raw_ctrader_deals_broker_symbol", "raw_ctrader_deals", ["broker_id", "symbol_id", "collected_at"])


def downgrade() -> None:
    op.drop_index("ix_raw_ctrader_deals_broker_symbol", table_name="raw_ctrader_deals")
    op.drop_index("ix_raw_ctrader_deals_broker_trader", table_name="raw_ctrader_deals")
    op.drop_index("ix_raw_ctrader_deals_broker_collected", table_name="raw_ctrader_deals")
    op.execute("DROP INDEX IF EXISTS uq_raw_ctrader_deals_active")
    op.execute("SELECT remove_retention_policy('raw_ctrader_deals', if_not_exists => TRUE)")
    op.drop_table("raw_ctrader_deals")
