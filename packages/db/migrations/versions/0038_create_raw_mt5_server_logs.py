"""Create raw_mt5_server_logs table.

TimescaleDB hypertable partitioned by log_time.
Source: MT5Manager.LogGet(from_ts, to_ts) → list of MTLog objects.
Each MTLog has: Time (unix s), Category (int), Code (int), Message (str).

Contains all server events: login/logout, order rejections, network errors,
balance operations, etc. Full raw message stored for forensic replay.

Login events are identified by is_login_event=true and have login,
ip_address, computer_id pre-extracted by the log parser for fast querying.

Retention: 180 days (per CLAUDE.md connectivity/collector logs policy).

Revision ID: 0038
Revises: 0037
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0038"
down_revision = "0037"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt5_server_logs",

        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # MTLog fields
        sa.Column("log_time", sa.DateTime(timezone=True), nullable=False),  # partition key
        sa.Column("category", sa.Integer(), nullable=True),     # MTLog.Category
        sa.Column("code", sa.Integer(), nullable=True),         # MTLog.Code
        sa.Column("message", sa.Text(), nullable=True),         # MTLog.Message (full text)

        # Extracted by log_parser.py after collection (NULL until parsed)
        sa.Column("login", sa.BigInteger(), nullable=True),
        sa.Column("ip_address", sa.String(), nullable=True),
        sa.Column("computer_id", sa.String(), nullable=True),   # CID (MD5 hardware fingerprint)
        sa.Column("is_login_event", sa.Boolean(), nullable=False, server_default="false"),

        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("ingestion_hash", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("NOW()")),
    )

    op.execute("SELECT create_hypertable('raw_mt5_server_logs', 'log_time')")

    # Base time-range scan
    op.create_index(
        "ix_raw_mt5_server_logs_broker_time",
        "raw_mt5_server_logs",
        ["broker_id", sa.text("log_time DESC")],
    )
    # Fast login event lookup
    op.create_index(
        "ix_raw_mt5_server_logs_login_events",
        "raw_mt5_server_logs",
        ["broker_id", "is_login_event", sa.text("log_time DESC")],
    )
    # Per-account login history
    op.create_index(
        "ix_raw_mt5_server_logs_broker_login",
        "raw_mt5_server_logs",
        ["broker_id", "login"],
    )

    op.execute("SELECT add_retention_policy('raw_mt5_server_logs', INTERVAL '180 days')")


def downgrade() -> None:
    op.execute("SELECT remove_retention_policy('raw_mt5_server_logs', if_exists => true)")
    op.drop_index("ix_raw_mt5_server_logs_broker_login",   table_name="raw_mt5_server_logs")
    op.drop_index("ix_raw_mt5_server_logs_login_events",   table_name="raw_mt5_server_logs")
    op.drop_index("ix_raw_mt5_server_logs_broker_time",    table_name="raw_mt5_server_logs")
    op.drop_table("raw_mt5_server_logs")
