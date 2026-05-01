"""Create norm_positions, norm_orders, norm_symbols tables

Revision ID: 0030
Revises: 0029
Create Date: 2026-04-21

Notes:
- norm_positions: open position snapshots, supersede pattern
- norm_orders: pending/historical orders, supersede pattern
- norm_symbols: symbol reference data, supersede pattern
- All plain PostgreSQL (moderate volume, not time-series)
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0030"
down_revision = "0029"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ── norm_positions ───────────────────────────────────────────────────────
    op.create_table(
        "norm_positions",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_system", sa.String(), nullable=False),
        sa.Column("source_position_id", sa.String(), nullable=False),
        sa.Column("source_account_id", sa.String(), nullable=False),
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("symbol", sa.String(), nullable=True),
        sa.Column("direction", sa.Integer(), nullable=True),             # 0=buy, 1=sell
        sa.Column("volume_lots", sa.Float(), nullable=True),
        sa.Column("price_open", sa.Float(), nullable=True),
        sa.Column("price_current", sa.Float(), nullable=True),
        sa.Column("profit", sa.Float(), nullable=True),
        sa.Column("swap", sa.Float(), nullable=True),
        sa.Column("open_time_msc", sa.BigInteger(), nullable=True),
        sa.Column("raw_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("normalized_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.execute(
        """
        CREATE UNIQUE INDEX uq_norm_positions_active
        ON norm_positions (broker_id, server_id, source_system, source_position_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_norm_positions_broker_login", "norm_positions", ["broker_id", "login"])
    op.create_index("ix_norm_positions_broker_symbol", "norm_positions", ["broker_id", "symbol"])

    # ── norm_orders ──────────────────────────────────────────────────────────
    op.create_table(
        "norm_orders",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_system", sa.String(), nullable=False),
        sa.Column("source_order_id", sa.String(), nullable=False),
        sa.Column("source_account_id", sa.String(), nullable=False),
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("symbol", sa.String(), nullable=True),
        sa.Column("order_type", sa.String(), nullable=True),             # market | limit | stop | stop_limit
        sa.Column("direction", sa.Integer(), nullable=True),             # 0=buy, 1=sell
        sa.Column("volume_lots", sa.Float(), nullable=True),
        sa.Column("price_order", sa.Float(), nullable=True),
        sa.Column("price_current", sa.Float(), nullable=True),
        sa.Column("time_setup_msc", sa.BigInteger(), nullable=True),
        sa.Column("time_done_msc", sa.BigInteger(), nullable=True),
        sa.Column("order_status", sa.String(), nullable=True),           # pending | filled | cancelled | expired
        sa.Column("raw_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("normalized_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.execute(
        """
        CREATE UNIQUE INDEX uq_norm_orders_active
        ON norm_orders (broker_id, server_id, source_system, source_order_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_norm_orders_broker_login", "norm_orders", ["broker_id", "login"])
    op.create_index("ix_norm_orders_broker_symbol", "norm_orders", ["broker_id", "symbol"])

    # ── norm_symbols ─────────────────────────────────────────────────────────
    op.create_table(
        "norm_symbols",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_system", sa.String(), nullable=False),
        sa.Column("symbol", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("category", sa.String(), nullable=True),               # forex | metals | indices | crypto | energy | other
        sa.Column("currency_base", sa.String(), nullable=True),
        sa.Column("currency_profit", sa.String(), nullable=True),
        sa.Column("digits", sa.Integer(), nullable=True),
        sa.Column("contract_size", sa.Float(), nullable=True),
        sa.Column("swap_long", sa.Float(), nullable=True),
        sa.Column("swap_short", sa.Float(), nullable=True),
        sa.Column("spread", sa.Integer(), nullable=True),
        sa.Column("raw_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("normalized_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.execute(
        """
        CREATE UNIQUE INDEX uq_norm_symbols_active
        ON norm_symbols (broker_id, server_id, source_system, symbol)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_norm_symbols_broker_symbol", "norm_symbols", ["broker_id", "symbol"])


def downgrade() -> None:
    op.drop_index("ix_norm_symbols_broker_symbol", table_name="norm_symbols")
    op.execute("DROP INDEX IF EXISTS uq_norm_symbols_active")
    op.drop_table("norm_symbols")

    op.drop_index("ix_norm_orders_broker_symbol", table_name="norm_orders")
    op.drop_index("ix_norm_orders_broker_login", table_name="norm_orders")
    op.execute("DROP INDEX IF EXISTS uq_norm_orders_active")
    op.drop_table("norm_orders")

    op.drop_index("ix_norm_positions_broker_symbol", table_name="norm_positions")
    op.drop_index("ix_norm_positions_broker_login", table_name="norm_positions")
    op.execute("DROP INDEX IF EXISTS uq_norm_positions_active")
    op.drop_table("norm_positions")
