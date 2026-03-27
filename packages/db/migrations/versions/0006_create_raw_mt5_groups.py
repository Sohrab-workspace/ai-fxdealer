"""Create raw_mt5_groups table

Revision ID: 0006
Revises: 0005
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL table (low-volume config/reference per CLAUDE.md)
- Group configs change infrequently — re-synced on schedule to detect changes
- Source: MT5Manager.GroupRequestArray() — 42 fields, real payload captured 2026-03-23
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0006"
down_revision = "0005"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_groups",

        # Platform / tenant
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted MT5 fields — hybrid raw storage
        sa.Column("group_name", sa.String(), nullable=False),           # Group — "managers\administrators"
        sa.Column("currency", sa.String(), nullable=True),              # Currency — "USD"
        sa.Column("currency_digits", sa.Integer(), nullable=True),      # CurrencyDigits
        sa.Column("margin_call", sa.Float(), nullable=True),            # MarginCall — margin call level %
        sa.Column("margin_stop_out", sa.Float(), nullable=True),        # MarginStopOut — stop out level %
        sa.Column("trade_flags", sa.Integer(), nullable=True),          # TradeFlags — trading permissions bitmask
        sa.Column("permissions_flags", sa.Integer(), nullable=True),    # PermissionsFlags

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

    # Deduplication — one active config snapshot per (broker, server, group name)
    op.execute(
        """
        CREATE UNIQUE INDEX uq_raw_mt5_groups_active
        ON raw_mt5_groups (broker_id, server_id, group_name)
        WHERE status = 'active'
        """
    )

    # Standard broker-scoped lookup
    op.create_index("ix_raw_mt5_groups_broker_id", "raw_mt5_groups", ["broker_id"])


def downgrade() -> None:
    op.drop_index("ix_raw_mt5_groups_broker_id", table_name="raw_mt5_groups")
    op.execute("DROP INDEX IF EXISTS uq_raw_mt5_groups_active")
    op.drop_table("raw_mt5_groups")
