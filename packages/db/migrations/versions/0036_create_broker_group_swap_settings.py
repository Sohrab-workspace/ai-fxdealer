"""Create broker_group_swap_settings table.

MT4/MT5 servers have no native swap-free flag on groups — swap-free status
is managed by external server plugins that skip swap charges for specific
groups. Admins must manually classify each group as swap-free or not.

Unclassified groups default to swap_free=False (safe default — never
assume a group is swap-free until an admin explicitly says so).

Revision ID: 0036
Revises: 0035
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0036"
down_revision = "0035"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "broker_group_swap_settings",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True,
                  server_default=sa.text("gen_random_uuid()")),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("source_system", sa.String(), nullable=False),   # mt4 | mt5
        sa.Column("group_name", sa.String(), nullable=False),
        sa.Column("swap_free", sa.Boolean(), nullable=False, server_default="false"),
        sa.Column("set_by", sa.String(), nullable=True),           # admin user who set this
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    )

    # One classification per group per broker/server/platform
    op.execute(
        "CREATE UNIQUE INDEX uq_broker_group_swap_settings "
        "ON broker_group_swap_settings(broker_id, server_id, source_system, group_name)"
    )

    op.create_index(
        "ix_broker_group_swap_broker_sys",
        "broker_group_swap_settings",
        ["broker_id", "source_system"],
    )
    op.create_index(
        "ix_broker_group_swap_free_lookup",
        "broker_group_swap_settings",
        ["broker_id", "server_id", "source_system", "swap_free"],
    )


def downgrade() -> None:
    op.drop_index("ix_broker_group_swap_free_lookup", table_name="broker_group_swap_settings")
    op.drop_index("ix_broker_group_swap_broker_sys", table_name="broker_group_swap_settings")
    op.execute("DROP INDEX IF EXISTS uq_broker_group_swap_settings")
    op.drop_table("broker_group_swap_settings")
