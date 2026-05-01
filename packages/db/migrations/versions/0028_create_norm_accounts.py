"""Create norm_accounts table

Revision ID: 0028
Revises: 0027
Create Date: 2026-04-21

Notes:
- Normalized account view unified across MT4, MT5, cTrader
- One active record per (broker_id, server_id, source_account_id)
- Plain PostgreSQL — supersede pattern on re-sync
- source_account_id = login as string (cross-source stable key)
- swap_free flag critical for SFA rule engine targeting
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0028"
down_revision = "0027"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "norm_accounts",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_system", sa.String(), nullable=False),          # mt4 | mt5 | ctrader
        sa.Column("source_account_id", sa.String(), nullable=False),      # login as string
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("group_name", sa.String(), nullable=True),
        sa.Column("account_name", sa.String(), nullable=True),
        sa.Column("balance", sa.Float(), nullable=True),
        sa.Column("equity", sa.Float(), nullable=True),
        sa.Column("credit", sa.Float(), nullable=True),
        sa.Column("leverage", sa.Integer(), nullable=True),
        sa.Column("currency", sa.String(), nullable=True),
        sa.Column("country", sa.String(), nullable=True),
        sa.Column("swap_free", sa.Integer(), nullable=True, server_default="0"),
        sa.Column("is_demo", sa.Integer(), nullable=True, server_default="0"),
        sa.Column("registration_ts", sa.BigInteger(), nullable=True),
        sa.Column("last_access_ts", sa.BigInteger(), nullable=True),
        sa.Column("account_status", sa.String(), nullable=True),
        sa.Column("raw_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("normalized_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )

    op.execute(
        """
        CREATE UNIQUE INDEX uq_norm_accounts_active
        ON norm_accounts (broker_id, server_id, source_account_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_norm_accounts_broker_login", "norm_accounts", ["broker_id", "login"])
    op.create_index("ix_norm_accounts_broker_group", "norm_accounts", ["broker_id", "group_name"])
    op.create_index("ix_norm_accounts_broker_country", "norm_accounts", ["broker_id", "country"])
    op.create_index("ix_norm_accounts_swap_free", "norm_accounts", ["broker_id", "swap_free"])


def downgrade() -> None:
    op.drop_index("ix_norm_accounts_swap_free", table_name="norm_accounts")
    op.drop_index("ix_norm_accounts_broker_country", table_name="norm_accounts")
    op.drop_index("ix_norm_accounts_broker_group", table_name="norm_accounts")
    op.drop_index("ix_norm_accounts_broker_login", table_name="norm_accounts")
    op.execute("DROP INDEX IF EXISTS uq_norm_accounts_active")
    op.drop_table("norm_accounts")
