"""Create raw_mt5_accounts table

Revision ID: 0002
Revises: 0001
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table (low-volume config/reference per CLAUDE.md)
- Periodic snapshots — each sync supersedes the prior active record
- Source: MT5Manager.UserGet() — 46 fields, real payload captured 2026-03-23
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0002"
down_revision = "0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_accounts",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT5 fields — hybrid raw storage
        sa.Column("login", sa.BigInteger(), nullable=False),          # Login
        sa.Column("group_name", sa.String(), nullable=True),          # Group
        sa.Column("name", sa.String(), nullable=True),                # Name
        sa.Column("balance", sa.Float(), nullable=True),              # Balance
        sa.Column("credit", sa.Float(), nullable=True),               # Credit
        sa.Column("leverage", sa.Integer(), nullable=True),           # Leverage
        sa.Column("rights", sa.Integer(), nullable=True),             # Rights (bitmask)
        sa.Column("country", sa.String(), nullable=True),             # Country
        sa.Column("last_ip", sa.String(), nullable=True),             # LastIP
        sa.Column("registration", sa.BigInteger(), nullable=True),    # Registration (unix seconds)
        sa.Column("last_access", sa.BigInteger(), nullable=True),     # LastAccess (unix seconds)
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),  # derived from Registration

        # Full raw payload
        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),

        # Housekeeping
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ingestion_hash", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )

    # Deduplication — one active snapshot per (broker, server, login)
    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt5_accounts_active
        ON raw_mt5_accounts (broker_id, server_id, login)
        WHERE status = 'active'
        """
    )

    # Account lookup (investigation panel, rule engine)
    op.create_index("ix_raw_mt5_accounts_broker_login", "raw_mt5_accounts", ["broker_id", "login"])
    # Group-level queries (group assignment checks, rule scoping)
    op.create_index("ix_raw_mt5_accounts_broker_group", "raw_mt5_accounts", ["broker_id", "group_name"])
    # Geo / IP fraud queries
    op.create_index("ix_raw_mt5_accounts_broker_country", "raw_mt5_accounts", ["broker_id", "country"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt5_accounts_broker_country", table_name="raw_mt5_accounts")
    op.drop_index("ix_raw_mt5_accounts_broker_group", table_name="raw_mt5_accounts")
    op.drop_index("ix_raw_mt5_accounts_broker_login", table_name="raw_mt5_accounts")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_accounts_active")
    op.drop_table("raw_mt5_accounts")
