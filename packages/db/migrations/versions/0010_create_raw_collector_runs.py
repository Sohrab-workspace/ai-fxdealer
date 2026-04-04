"""Create raw_collector_runs table

Revision ID: 0010
Revises: 0009
Create Date: 2026-03-27

Notes:
- TimescaleDB hypertable — partitioned by collected_at
- Retention policy: 180 days (CLAUDE.md: connectivity and collector logs)
- Internal platform log — no payload_json, status, or archived_at
- Written by every collector at end of bootstrap_sync() and incremental_sync()
- Schema defined from CLAUDE.md BaseCollector contract and observability spec
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0010"
down_revision = "0009"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_collector_runs",

        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("source_system", sa.String(), nullable=False),   # mt4|mt5|ctrader|fxbo|bridge|lp|news|calendar
        sa.Column("connection_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("entity", sa.String(), nullable=True),           # deals|orders|positions|accounts|ticks|etc.
        sa.Column("sync_mode", sa.String(), nullable=False),       # bootstrap|incremental
        sa.Column("status", sa.String(), nullable=False),          # success|error|partial
        sa.Column("records_fetched", sa.Integer(), nullable=True),
        sa.Column("records_saved", sa.Integer(), nullable=True),
        sa.Column("duration_ms", sa.Integer(), nullable=True),
        sa.Column("cursor_from", sa.String(), nullable=True),      # cursor at run start
        sa.Column("cursor_to", sa.String(), nullable=True),        # cursor at run end (new position)
        sa.Column("error_message", sa.String(), nullable=True),    # null on success
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),   # hypertable partition key
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )

    # Convert to TimescaleDB hypertable — partition by collected_at
    op.execute("SELECT create_hypertable('raw_collector_runs', 'collected_at')")

    # Per CLAUDE.md indexing standard for collector tables
    op.create_index(
        "ix_raw_collector_runs_broker_system_collected",
        "raw_collector_runs",
        ["broker_id", "source_system", sa.text("collected_at DESC")],
    )

    # TimescaleDB retention policy — 180 days
    op.execute("SELECT add_retention_policy('raw_collector_runs', INTERVAL '180 days')")


def downgrade() -> None:
    op.execute("SELECT remove_retention_policy('raw_collector_runs', if_exists => true)")
    op.drop_index("ix_raw_collector_runs_broker_system_collected", table_name="raw_collector_runs")
    op.drop_table("raw_collector_runs")
