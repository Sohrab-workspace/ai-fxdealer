"""Create raw_ctrader_orders table

Revision ID: 0025
Revises: 0024
Create Date: 2026-04-01

Notes:
- Plain PostgreSQL — re-synced frequently for pending orders
- Source: Spotware Manager API → ProtoPendingOrderListReq (payloadType 409)
- Entity: ProtoOrder + embedded ProtoTradeData (entities.md)
- Monetary values in cents; volumes in cents of lot size
- order_type: MARKET=1, LIMIT=2, STOP=3, STOP_LIMIT=4, MARKET_RANGE=5
- order_status: ACCEPTED=1, FILLED=2, REJECTED=3, EXPIRED=4, CANCELLED=5
- time_in_force: GTC=1, GTD=2, GFD=3, FOK=4, IOC=5
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0025"
down_revision = "0024"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_ctrader_orders",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted ProtoOrder fields (field numbers from entities.md)
        sa.Column("order_id", sa.BigInteger(), nullable=False),              # field 1
        sa.Column("order_type", sa.Integer(), nullable=True),                # field 3 — ProtoOrderType
        sa.Column("order_status", sa.Integer(), nullable=True),              # field 4 — ProtoOrderStatus
        sa.Column("expiration_ts", sa.BigInteger(), nullable=True),          # field 6 — Unix ms
        sa.Column("execution_price", sa.Float(), nullable=True),             # field 9
        sa.Column("executed_volume", sa.BigInteger(), nullable=True),        # field 10 — cents
        sa.Column("stop_loss", sa.Float(), nullable=True),                   # field 11
        sa.Column("take_profit", sa.Float(), nullable=True),                 # field 12
        sa.Column("limit_price", sa.Float(), nullable=True),                 # field 21
        sa.Column("stop_price", sa.Float(), nullable=True),                  # field 22
        sa.Column("commission_cents", sa.BigInteger(), nullable=True),       # field 24
        sa.Column("time_in_force", sa.Integer(), nullable=True),             # field 26 — ProtoTimeInForce
        sa.Column("position_id", sa.BigInteger(), nullable=True),            # field 30
        sa.Column("book_type", sa.Integer(), nullable=True),                 # field 14 — A=1/B=2
        sa.Column("money_digits", sa.Integer(), nullable=True),              # field 54

        # Extracted from embedded ProtoTradeData (order field 2)
        sa.Column("symbol_id", sa.BigInteger(), nullable=True),              # tradeData.1
        sa.Column("volume", sa.BigInteger(), nullable=True),                 # tradeData.2 — cents of lot
        sa.Column("trade_side", sa.Integer(), nullable=True),                # tradeData.3 — BUY=1/SELL=2
        sa.Column("trader_id", sa.BigInteger(), nullable=False),             # tradeData.4
        sa.Column("open_ts", sa.BigInteger(), nullable=True),                # tradeData.7 — Unix ms
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),

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
        CREATE UNIQUE INDEX uq_raw_ctrader_orders_active
        ON raw_ctrader_orders (broker_id, server_id, order_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_ctrader_orders_broker_collected", "raw_ctrader_orders", ["broker_id", "collected_at"])
    op.create_index("ix_raw_ctrader_orders_broker_trader", "raw_ctrader_orders", ["broker_id", "trader_id"])
    op.create_index("ix_raw_ctrader_orders_broker_symbol", "raw_ctrader_orders", ["broker_id", "symbol_id"])


def downgrade() -> None:
    op.drop_index("ix_raw_ctrader_orders_broker_symbol", table_name="raw_ctrader_orders")
    op.drop_index("ix_raw_ctrader_orders_broker_trader", table_name="raw_ctrader_orders")
    op.drop_index("ix_raw_ctrader_orders_broker_collected", table_name="raw_ctrader_orders")
    op.execute("DROP INDEX IF EXISTS uq_raw_ctrader_orders_active")
    op.drop_table("raw_ctrader_orders")
