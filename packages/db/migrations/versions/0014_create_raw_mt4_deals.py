"""Create raw_mt4_deals table

Revision ID: 0014
Revises: 0013
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table
- TradeRecord entries where close_time > 0 (closed positions + balance/credit ops)
- MT4 has no separate "deal" entity — a closed TradeRecord IS the deal
- close_price = actual exit price; profit = realized P&L; reason = close reason
- Balance ops: cmd=6, symbol="", profit = deposit/withdrawal amount
- Source: mtmanapi.dll TradesUserHistory() — same TradeRecord struct as orders (28 fields),
  captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0014"
down_revision = "0013"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_deals",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT4 TradeRecord fields (closed deals: close_time > 0)
        sa.Column("order_id", sa.Integer(), nullable=False),            # order (ticket)
        sa.Column("login", sa.Integer(), nullable=False),                # login
        sa.Column("symbol", sa.String(), nullable=True),                 # symbol (empty for balance ops)
        sa.Column("cmd", sa.Integer(), nullable=True),                   # 0=BUY,1=SELL,6=BALANCE,7=CREDIT
        sa.Column("volume", sa.Integer(), nullable=True),                # lots×100
        sa.Column("open_time", sa.BigInteger(), nullable=True),          # position open unix timestamp
        sa.Column("close_time", sa.BigInteger(), nullable=False),        # close unix timestamp (always > 0)
        sa.Column("state", sa.Integer(), nullable=True),                 # 3=closed_normal, 4=closed_part etc.
        sa.Column("open_price", sa.Float(), nullable=True),              # entry price (0 for balance ops)
        sa.Column("close_price", sa.Float(), nullable=True),             # exit price
        sa.Column("profit", sa.Float(), nullable=True),                  # realized P&L
        sa.Column("commission", sa.Float(), nullable=True),
        sa.Column("storage", sa.Float(), nullable=True),                 # total swap over holding period
        sa.Column("magic", sa.Integer(), nullable=True),
        sa.Column("reason", sa.Integer(), nullable=True),                # close reason (0=client, 3=stopout)
        sa.Column("timestamp", sa.BigInteger(), nullable=True),          # last modification unix time
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),  # derived from close_time

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
        CREATE UNIQUE INDEX uq_raw_mt4_deals_active
        ON raw_mt4_deals (broker_id, server_id, order_id)
        WHERE status = 'active'
        """
    )
    op.create_index(
        "ix_raw_mt4_deals_broker_collected",
        "raw_mt4_deals", ["broker_id", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt4_deals_broker_login_collected",
        "raw_mt4_deals", ["broker_id", "login", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt4_deals_broker_symbol_collected",
        "raw_mt4_deals", ["broker_id", "symbol", sa.text("collected_at DESC")],
    )


def downgrade() -> None:
    op.drop_index("ix_raw_mt4_deals_broker_symbol_collected", table_name="raw_mt4_deals")
    op.drop_index("ix_raw_mt4_deals_broker_login_collected", table_name="raw_mt4_deals")
    op.drop_index("ix_raw_mt4_deals_broker_collected", table_name="raw_mt4_deals")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt4_deals_active")
    op.drop_table("raw_mt4_deals")
