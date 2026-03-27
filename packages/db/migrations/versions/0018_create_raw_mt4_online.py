"""Create raw_mt4_online table

Revision ID: 0018
Revises: 0017
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table
- Point-in-time snapshot of all connected MT4 clients
- ip field is a packed uint32 integer (not dotted-decimal string)
- All 7 fields extracted (small record, full hybrid)
- Source: mtmanapi.dll OnlineRequest() — OnlineRecord struct (7 fields), captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0018"
down_revision = "0017"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_online",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # All 7 OnlineRecord fields extracted
        sa.Column("login", sa.Integer(), nullable=False),
        sa.Column("group_name", sa.String(), nullable=True),            # group
        sa.Column("ip", sa.BigInteger(), nullable=True),                # packed uint32 IP address
        sa.Column("login_time", sa.BigInteger(), nullable=True),        # session start unix timestamp
        sa.Column("last_access", sa.BigInteger(), nullable=True),       # last activity unix timestamp
        sa.Column("agent", sa.String(), nullable=True),                 # client string e.g. "MetaTrader 4"
        sa.Column("version", sa.Integer(), nullable=True),              # client build number
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
        CREATE UNIQUE INDEX uq_raw_mt4_online_active
        ON raw_mt4_online (broker_id, server_id, login)
        WHERE status = 'active'
        """
    )
    op.create_index(
        "ix_raw_mt4_online_broker_collected",
        "raw_mt4_online", ["broker_id", sa.text("collected_at DESC")],
    )
    op.create_index("ix_raw_mt4_online_broker_login", "raw_mt4_online", ["broker_id", "login"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt4_online_broker_login", table_name="raw_mt4_online")
    op.drop_index("ix_raw_mt4_online_broker_collected", table_name="raw_mt4_online")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt4_online_active")
    op.drop_table("raw_mt4_online")
