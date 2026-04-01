"""Create raw_ctrader_accounts table

Revision ID: 0022
Revises: 0021
Create Date: 2026-04-01

Notes:
- Plain PostgreSQL — low volume, re-synced on schedule
- Source: Spotware Manager API → ProtoTraderListReq (payloadType 403)
- Entity: ProtoTrader — complete field mapping in entities.md
- Monetary values in cents (divide by 10^money_digits for display)
- Partial unique index on trader_id per broker/server
- Superseding pattern: re-syncs create new records, old become superseded
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0022"
down_revision = "0021"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_ctrader_accounts",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted ProtoTrader fields (field numbers from entities.md)
        sa.Column("trader_id", sa.BigInteger(), nullable=False),          # field 1
        sa.Column("login", sa.BigInteger(), nullable=False),               # field 2
        sa.Column("group_id", sa.BigInteger(), nullable=True),             # field 3
        sa.Column("balance_cents", sa.BigInteger(), nullable=True),        # field 8
        sa.Column("account_type", sa.Integer(), nullable=True),            # field 9 — HEDGED=1/NETTED=2
        sa.Column("registration_ts", sa.BigInteger(), nullable=True),      # field 25 — Unix ms
        sa.Column("last_connect_ts", sa.BigInteger(), nullable=True),      # field 26 — Unix ms
        sa.Column("online", sa.Integer(), nullable=True),                  # field 27 — 1=online
        sa.Column("deleted", sa.Integer(), nullable=True),                 # field 29 — 1=soft-deleted
        sa.Column("access_rights", sa.Integer(), nullable=True),           # field 59
        sa.Column("leverage_in_cents", sa.BigInteger(), nullable=True),    # field 66
        sa.Column("deposit_asset_id", sa.BigInteger(), nullable=True),     # field 61
        sa.Column("money_digits", sa.Integer(), nullable=True),            # field 80
        sa.Column("swap_free", sa.Integer(), nullable=True),               # field 64
        sa.Column("is_limited_risk", sa.Integer(), nullable=True),         # field 78
        sa.Column("version", sa.BigInteger(), nullable=True),              # field 74
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
        CREATE UNIQUE INDEX uq_raw_ctrader_accounts_active
        ON raw_ctrader_accounts (broker_id, server_id, trader_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_ctrader_accounts_broker_collected", "raw_ctrader_accounts", ["broker_id", "collected_at"])
    op.create_index("ix_raw_ctrader_accounts_broker_login", "raw_ctrader_accounts", ["broker_id", "login"])
    op.create_index("ix_raw_ctrader_accounts_broker_group", "raw_ctrader_accounts", ["broker_id", "group_id"])


def downgrade() -> None:
    op.drop_index("ix_raw_ctrader_accounts_broker_group", table_name="raw_ctrader_accounts")
    op.drop_index("ix_raw_ctrader_accounts_broker_login", table_name="raw_ctrader_accounts")
    op.drop_index("ix_raw_ctrader_accounts_broker_collected", table_name="raw_ctrader_accounts")
    op.execute("DROP INDEX IF EXISTS uq_raw_ctrader_accounts_active")
    op.drop_table("raw_ctrader_accounts")
