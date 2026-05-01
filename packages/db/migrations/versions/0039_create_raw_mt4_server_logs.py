"""Create raw_mt4_server_logs table.

TimescaleDB hypertable partitioned by log_time.
Source: MT4 Manager API DLL — LogsRequest(from_ts, to_ts) → ServerLog records.
Each ServerLog has: time (unix s), category (int), ip (string), code (int),
description (text message up to 200 chars).

MT4 server logs use the same collection/parse pattern as MT5:
- Collector stores full raw record in payload_json
- log_parser.py extracts login events → account_login_history

Retention: 180 days.

Revision ID: 0039
Revises: 0038
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0039"
down_revision = "0038"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_server_logs",

        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # ServerLog fields (MT4 Manager API)
        sa.Column("log_time", sa.DateTime(timezone=True), nullable=False),  # partition key
        sa.Column("category", sa.Integer(), nullable=True),
        sa.Column("code", sa.Integer(), nullable=True),
        sa.Column("message", sa.Text(), nullable=True),

        # Extracted by log_parser.py (NULL until parsed)
        sa.Column("login", sa.Integer(), nullable=True),        # MT4 login is int32
        sa.Column("ip_address", sa.String(), nullable=True),
        sa.Column("computer_id", sa.String(), nullable=True),   # terminal ID / CID
        sa.Column("is_login_event", sa.Boolean(), nullable=False, server_default="false"),

        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ingestion_hash", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("NOW()")),
    )

    op.execute("SELECT create_hypertable('raw_mt4_server_logs', 'log_time')")

    op.create_index(
        "ix_raw_mt4_server_logs_broker_time",
        "raw_mt4_server_logs",
        ["broker_id", sa.text("log_time DESC")],
    )
    op.create_index(
        "ix_raw_mt4_server_logs_login_events",
        "raw_mt4_server_logs",
        ["broker_id", "is_login_event", sa.text("log_time DESC")],
    )
    op.create_index(
        "ix_raw_mt4_server_logs_broker_login",
        "raw_mt4_server_logs",
        ["broker_id", "login"],
    )

    op.execute("SELECT add_retention_policy('raw_mt4_server_logs', INTERVAL '180 days')")


def downgrade() -> None:
    op.execute("SELECT remove_retention_policy('raw_mt4_server_logs', if_exists => true)")
    op.drop_index("ix_raw_mt4_server_logs_broker_login",  table_name="raw_mt4_server_logs")
    op.drop_index("ix_raw_mt4_server_logs_login_events",  table_name="raw_mt4_server_logs")
    op.drop_index("ix_raw_mt4_server_logs_broker_time",   table_name="raw_mt4_server_logs")
    op.drop_table("raw_mt4_server_logs")
