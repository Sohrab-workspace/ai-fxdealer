"""Create broker_group_pending_review table.

Tracks groups that appeared for the first time and have not yet been
classified in broker_group_swap_settings. Drives the admin notification
prompt on first login after a new group is detected.

Lifecycle:
  1. Group reconciler detects a new group → inserts row (status='pending')
     and also inserts into broker_group_swap_settings with swap_free=False
  2. Admin sees notification banner on dashboard login
  3. Admin classifies the group → row updated to status='reviewed'
  4. If admin dismisses without classifying → status='dismissed'

Revision ID: 0037
Revises: 0036
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0037"
down_revision = "0036"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "broker_group_pending_review",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text("gen_random_uuid()")),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("source_system", sa.String(), nullable=False),   # mt4 | mt5
        sa.Column("group_name", sa.String(), nullable=False),
        sa.Column("status", sa.String(), nullable=False,
                  server_default="'pending'"),                     # pending | reviewed | dismissed
        sa.Column("detected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("reviewed_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("reviewed_by", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("NOW()")),
    )

    # Prevent duplicate pending notifications for the same group
    op.execute(
        "CREATE UNIQUE INDEX uq_broker_group_pending_active "
        "ON broker_group_pending_review(broker_id, server_id, source_system, group_name) "
        "WHERE status = 'pending'"
    )

    # Used by dashboard to load pending notifications per broker
    op.create_index(
        "ix_broker_group_pending_broker_status",
        "broker_group_pending_review",
        ["broker_id", "status"],
    )


def downgrade() -> None:
    op.drop_index("ix_broker_group_pending_broker_status",
                  table_name="broker_group_pending_review")
    op.execute("DROP INDEX IF EXISTS uq_broker_group_pending_active")
    op.drop_table("broker_group_pending_review")
