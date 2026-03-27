"""Create raw_mt4_orders table

Revision ID: 0013
Revises: 0012
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table
- TradeRecord entries where close_time == 0 (open positions + pending orders)
- Differentiating open vs pending: cmd 0-1 = market positions, cmd 2-5 = pending orders
- Volume is lots×100 (÷100 = standard lots)
- close_price here = current market price (not exit price — position is still open)
- Source: mtmanapi.dll TradesRequest() — TradeRecord struct (28 fields), captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0013"
down_revision = "0012"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_orders",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT4 TradeRecord fields (open orders: close_time=0)
        sa.Column("order_id", sa.Integer(), nullable=False),           # order (ticket)
        sa.Column("login", sa.Integer(), nullable=False),               # login
        sa.Column("symbol", sa.String(), nullable=True),                # symbol
        sa.Column("cmd", sa.Integer(), nullable=True),                  # 0=BUY,1=SELL,2-5=pending,6=BAL,7=CRED
        sa.Column("volume", sa.Integer(), nullable=True),               # lots×100
        sa.Column("open_time", sa.BigInteger(), nullable=True),         # open unix timestamp
        sa.Column("state", sa.Integer(), nullable=True),                # order state
        sa.Column("open_price", sa.Float(), nullable=True),             # entry price
        sa.Column("sl", sa.Float(), nullable=True),                     # stop loss
        sa.Column("tp", sa.Float(), nullable=True),                     # take profit
        sa.Column("close_price", sa.Float(), nullable=True),            # current market price (not exit)
        sa.Column("profit", sa.Float(), nullable=True),                 # floating P&L
        sa.Column("commission", sa.Float(), nullable=True),
        sa.Column("storage", sa.Float(), nullable=True),                # accrued swap
        sa.Column("magic", sa.Integer(), nullable=True),                # EA magic number
        sa.Column("expiration", sa.BigInteger(), nullable=True),        # pending expiry (0=GTC)
        sa.Column("timestamp", sa.BigInteger(), nullable=True),         # last modification unix time
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
        CREATE UNIQUE INDEX uq_raw_mt4_orders_active
        ON raw_mt4_orders (broker_id, server_id, order_id)
        WHERE status = 'active'
        """
    )
    op.create_index(
        "ix_raw_mt4_orders_broker_collected",
        "raw_mt4_orders", ["broker_id", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt4_orders_broker_login_collected",
        "raw_mt4_orders", ["broker_id", "login", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt4_orders_broker_symbol_collected",
        "raw_mt4_orders", ["broker_id", "symbol", sa.text("collected_at DESC")],
    )


def downgrade() -> None:
    op.drop_index("ix_raw_mt4_orders_broker_symbol_collected", table_name="raw_mt4_orders")
    op.drop_index("ix_raw_mt4_orders_broker_login_collected", table_name="raw_mt4_orders")
    op.drop_index("ix_raw_mt4_orders_broker_collected", table_name="raw_mt4_orders")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt4_orders_active")
    op.drop_table("raw_mt4_orders")
