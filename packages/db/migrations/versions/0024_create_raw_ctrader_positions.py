"""Create raw_ctrader_positions table

Revision ID: 0024
Revises: 0023
Create Date: 2026-04-01

Notes:
- Plain PostgreSQL — re-synced frequently for open positions
- Single table for both open (payloadType 407) and closed (720) positions
- position_status field distinguishes: OPEN=1 / CLOSED=2
- ProtoPosition embeds ProtoTradeData (symbol, volume, side, trader, timestamps)
- Monetary values in cents; volumes in cents of lot size
- Source: Spotware Manager API → ProtoPosition + ProtoTradeData (entities.md)
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0024"
down_revision = "0023"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_ctrader_positions",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted ProtoPosition fields (field numbers from entities.md)
        sa.Column("position_id", sa.BigInteger(), nullable=False),           # field 1
        sa.Column("position_status", sa.Integer(), nullable=True),           # field 4 — OPEN=1/CLOSED=2
        sa.Column("swap_cents", sa.BigInteger(), nullable=True),             # field 5 — accumulated swap
        sa.Column("price", sa.Float(), nullable=True),                       # field 6 — VWAP open price
        sa.Column("stop_loss", sa.Float(), nullable=True),                   # field 7
        sa.Column("take_profit", sa.Float(), nullable=True),                 # field 8
        sa.Column("commission_cents", sa.BigInteger(), nullable=True),       # field 13
        sa.Column("book_type", sa.Integer(), nullable=True),                 # field 11 — A=1/B=2
        sa.Column("money_digits", sa.Integer(), nullable=True),              # field 30
        sa.Column("used_margin_cents", sa.BigInteger(), nullable=True),      # field 23

        # Extracted from embedded ProtoTradeData (position field 3)
        sa.Column("symbol_id", sa.BigInteger(), nullable=True),              # tradeData.1
        sa.Column("volume", sa.BigInteger(), nullable=True),                 # tradeData.2 — cents of lot
        sa.Column("trade_side", sa.Integer(), nullable=True),                # tradeData.3 — BUY=1/SELL=2
        sa.Column("trader_id", sa.BigInteger(), nullable=False),             # tradeData.4
        sa.Column("open_ts", sa.BigInteger(), nullable=True),                # tradeData.7 — Unix ms
        sa.Column("close_ts", sa.BigInteger(), nullable=True),               # tradeData.8 — Unix ms (closed only)
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
        CREATE UNIQUE INDEX uq_raw_ctrader_positions_active
        ON raw_ctrader_positions (broker_id, server_id, position_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_ctrader_positions_broker_collected", "raw_ctrader_positions", ["broker_id", "collected_at"])
    op.create_index("ix_raw_ctrader_positions_broker_trader", "raw_ctrader_positions", ["broker_id", "trader_id"])
    op.create_index("ix_raw_ctrader_positions_broker_symbol", "raw_ctrader_positions", ["broker_id", "symbol_id"])


def downgrade() -> None:
    op.drop_index("ix_raw_ctrader_positions_broker_symbol", table_name="raw_ctrader_positions")
    op.drop_index("ix_raw_ctrader_positions_broker_trader", table_name="raw_ctrader_positions")
    op.drop_index("ix_raw_ctrader_positions_broker_collected", table_name="raw_ctrader_positions")
    op.execute("DROP INDEX IF EXISTS uq_raw_ctrader_positions_active")
    op.drop_table("raw_ctrader_positions")
