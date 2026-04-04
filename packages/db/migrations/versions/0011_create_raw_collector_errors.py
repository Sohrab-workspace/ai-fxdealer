"""Create raw_collector_errors table

Revision ID: 0011
Revises: 0010
Create Date: 2026-03-27

Notes:
- TimescaleDB hypertable — partitioned by collected_at
- Retention policy: 180 days (CLAUDE.md: connectivity and collector logs)
- Internal platform log — no payload_json, status, or archived_at
- Written by collector inside handle_error() for: connection failures,
  fetch failures, save failures, and circuit breaker events
- Schema defined from CLAUDE.md error handling spec and BaseCollector contract
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0011"
down_revision = "0010"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_collector_errors",

        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("source_system", sa.String(), nullable=False),   # mt4|mt5|ctrader|fxbo|bridge|lp|news|calendar
        sa.Column("connection_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("entity", sa.String(), nullable=True),           # which entity was being fetched
        sa.Column("sync_mode", sa.String(), nullable=True),        # bootstrap|incremental
        sa.Column("error_type", sa.String(), nullable=True),       # connection|fetch|save|circuit_breaker
        sa.Column("error_code", sa.String(), nullable=True),       # MT5 retcode, exception class, HTTP status
        sa.Column("error_message", sa.String(), nullable=False),   # full error text
        sa.Column("context_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),  # cursor, retry count, payload snippet
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),   # hypertable partition key
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )

    # Convert to TimescaleDB hypertable — partition by collected_at
    op.execute("SELECT create_hypertable('raw_collector_errors', 'collected_at')")

    # Per CLAUDE.md indexing standard for collector tables
    op.create_index(
        "ix_raw_collector_errors_broker_system_collected",
        "raw_collector_errors",
        ["broker_id", "source_system", sa.text("collected_at DESC")],
    )

    # TimescaleDB retention policy — 180 days
    op.execute("SELECT add_retention_policy('raw_collector_errors', INTERVAL '180 days')")


def downgrade() -> None:
    op.execute("SELECT remove_retention_policy('raw_collector_errors', if_exists => true)")
    op.drop_index("ix_raw_collector_errors_broker_system_collected", table_name="raw_collector_errors")
    op.drop_table("raw_collector_errors")
