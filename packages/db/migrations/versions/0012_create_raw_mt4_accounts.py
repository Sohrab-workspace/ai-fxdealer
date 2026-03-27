"""Create raw_mt4_accounts table

Revision ID: 0012
Revises: 0011
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table (low-volume config/reference per CLAUDE.md)
- Periodic snapshots — each sync supersedes prior active record per login
- last_ip is stored as packed uint32 integer (not a dotted-decimal string)
- Source: mtmanapi.dll UsersRequest() — 22 fields from MT4ManagerAPI.h, captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0012"
down_revision = "0011"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_accounts",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT4 UserRecord fields
        sa.Column("login", sa.Integer(), nullable=False),
        sa.Column("group_name", sa.String(), nullable=True),          # group
        sa.Column("enable", sa.Integer(), nullable=True),             # 1=active, 0=disabled
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("country", sa.String(), nullable=True),
        sa.Column("city", sa.String(), nullable=True),
        sa.Column("leverage", sa.Integer(), nullable=True),
        sa.Column("balance", sa.Float(), nullable=True),
        sa.Column("credit", sa.Float(), nullable=True),
        sa.Column("margin_level", sa.Float(), nullable=True),
        sa.Column("regdate", sa.BigInteger(), nullable=True),         # registration unix timestamp
        sa.Column("lastdate", sa.BigInteger(), nullable=True),        # last login unix timestamp
        sa.Column("last_ip", sa.BigInteger(), nullable=True),         # packed uint32 IP
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
        CREATE UNIQUE INDEX uq_raw_mt4_accounts_active
        ON raw_mt4_accounts (broker_id, server_id, login)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_mt4_accounts_broker_login", "raw_mt4_accounts", ["broker_id", "login"])
    op.create_index("ix_raw_mt4_accounts_broker_group", "raw_mt4_accounts", ["broker_id", "group_name"])
    op.create_index("ix_raw_mt4_accounts_broker_country", "raw_mt4_accounts", ["broker_id", "country"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt4_accounts_broker_country", table_name="raw_mt4_accounts")
    op.drop_index("ix_raw_mt4_accounts_broker_group", table_name="raw_mt4_accounts")
    op.drop_index("ix_raw_mt4_accounts_broker_login", table_name="raw_mt4_accounts")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt4_accounts_active")
    op.drop_table("raw_mt4_accounts")
