"""Create norm_deals table (TimescaleDB hypertable)

Revision ID: 0029
Revises: 0028
Create Date: 2026-04-21

Notes:
- Normalized deal/execution record unified across MT4, MT5, cTrader
- MT4: one closed TradeRecord = one NormDeal (open+close in one record)
- MT5: one DealRequestByGroup entry record (action=0=in)
- cTrader: one ProtoDeal fill execution
- volume_lots: always normalized to standard lots
  MT5: Volume / 10000; MT4: volume / 100; cTrader: volume / (lot_size * 100)
- duration_ms: close_time_msc - open_time_msc (position holding period)
- TimescaleDB hypertable partitioned by deal_time, retention 2 years
- No primary key constraint (TimescaleDB requirement) — id is unique but not declared PK
- Dedup enforced by normalizer before insert (check existing by source_deal_id)
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0029"
down_revision = "0028"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "norm_deals",

        # id not declared primary_key — TimescaleDB hypertables require partition key in all unique indexes
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_system", sa.String(), nullable=False),
        sa.Column("source_deal_id", sa.String(), nullable=False),
        sa.Column("source_account_id", sa.String(), nullable=False),
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("symbol", sa.String(), nullable=True),
        sa.Column("direction", sa.Integer(), nullable=True),             # 0=buy, 1=sell
        sa.Column("volume_lots", sa.Float(), nullable=True),
        sa.Column("price", sa.Float(), nullable=True),
        sa.Column("profit", sa.Float(), nullable=True),
        sa.Column("commission", sa.Float(), nullable=True),
        sa.Column("swap", sa.Float(), nullable=True),
        sa.Column("open_time_msc", sa.BigInteger(), nullable=True),
        sa.Column("close_time_msc", sa.BigInteger(), nullable=True),
        sa.Column("deal_time_msc", sa.BigInteger(), nullable=False),
        sa.Column("duration_ms", sa.BigInteger(), nullable=True),
        sa.Column("deal_type", sa.String(), nullable=True),
        # trade | balance | credit | deposit | withdrawal
        sa.Column("raw_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("deal_time", sa.DateTime(timezone=True), nullable=False),   # hypertable partition key
        sa.Column("normalized_at", sa.DateTime(timezone=True), nullable=False),
    )

    # Source deal lookup (non-unique — dedup enforced by normalizer)
    op.create_index("ix_norm_deals_source_id", "norm_deals", ["broker_id", "server_id", "source_system", "source_deal_id"])
    op.create_index("ix_norm_deals_broker_login_time", "norm_deals", ["broker_id", "login", "deal_time"])
    op.create_index("ix_norm_deals_broker_symbol_time", "norm_deals", ["broker_id", "symbol", "deal_time"])

    # Convert to TimescaleDB hypertable partitioned by deal_time
    op.execute(
        "SELECT create_hypertable('norm_deals', 'deal_time', if_not_exists => TRUE)"
    )

    # Retention policy: 2 years
    op.execute(
        "SELECT add_retention_policy('norm_deals', INTERVAL '2 years', if_not_exists => TRUE)"
    )


def downgrade() -> None:
    op.drop_index("ix_norm_deals_broker_symbol_time", table_name="norm_deals")
    op.drop_index("ix_norm_deals_broker_login_time", table_name="norm_deals")
    op.drop_index("ix_norm_deals_source_id", table_name="norm_deals")
    op.drop_table("norm_deals")
