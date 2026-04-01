"""Create raw_mt5_online table

Revision ID: 0021
Revises: 0020
Create Date: 2026-04-01

Notes:
- Plain PostgreSQL (low-volume, polled every ~30 seconds)
- Session-level snapshot: one record per active MT5 manager/trader session
- Partial unique index on session_id — each TCP session deduped while active
- Superseding pattern: re-syncs create new records, prior ones become superseded
- Source: MT5Manager.OnlineGetArray() — MTOnline object, 8 fields
- Fields captured live 2026-04-01:
    Address (IP string), Build (int), ComputerID (MD5 string),
    Group (string), Login (int64), SessionID (int64), Time (unix s), Type (int)
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0021"
down_revision = "0020"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_online",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # All 8 MTOnline fields
        sa.Column("login", sa.BigInteger(), nullable=False),
        sa.Column("session_id", sa.BigInteger(), nullable=False),
        sa.Column("address", sa.String(), nullable=True),          # client IP
        sa.Column("build", sa.Integer(), nullable=True),           # terminal build number
        sa.Column("computer_id", sa.String(), nullable=True),      # MD5 of machine IDs
        sa.Column("group", sa.String(), nullable=True),            # account group
        sa.Column("time", sa.BigInteger(), nullable=True),         # session start unix seconds
        sa.Column("type", sa.Integer(), nullable=True),            # session type bitmask

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
        CREATE UNIQUE INDEX uq_raw_mt5_online_active
        ON raw_mt5_online (broker_id, server_id, session_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_mt5_online_broker_collected", "raw_mt5_online", ["broker_id", "collected_at"])
    op.create_index("ix_raw_mt5_online_broker_login", "raw_mt5_online", ["broker_id", "login"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt5_online_broker_login", table_name="raw_mt5_online")
    op.drop_index("ix_raw_mt5_online_broker_collected", table_name="raw_mt5_online")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_online_active")
    op.drop_table("raw_mt5_online")
