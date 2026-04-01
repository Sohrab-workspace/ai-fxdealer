"""Create raw_ctrader_groups table

Revision ID: 0027
Revises: 0026
Create Date: 2026-04-01

Notes:
- Plain PostgreSQL — low volume config/reference data
- Source: Spotware Manager API → LightGroupListReq (payloadType 473)
- ProtoGroup: field 1 = groupId (int64), field 2.8 = partial group name string
- Full payload_json preserves all fields
- group_name extracted by collector from nested field 2.8 at ingest time
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0027"
down_revision = "0026"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_ctrader_groups",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # ProtoGroup key fields
        sa.Column("group_id", sa.BigInteger(), nullable=False),              # field 1
        sa.Column("group_name", sa.String(), nullable=True),                 # field 2.8 — partial, extracted by collector

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
        CREATE UNIQUE INDEX uq_raw_ctrader_groups_active
        ON raw_ctrader_groups (broker_id, server_id, group_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_ctrader_groups_broker_collected", "raw_ctrader_groups", ["broker_id", "collected_at"])


def downgrade() -> None:
    op.drop_index("ix_raw_ctrader_groups_broker_collected", table_name="raw_ctrader_groups")
    op.execute("DROP INDEX IF EXISTS uq_raw_ctrader_groups_active")
    op.drop_table("raw_ctrader_groups")
