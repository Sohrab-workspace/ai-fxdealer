"""Create account_login_history table.

Normalized IP/CID login history per account across MT4 and MT5.
Populated by log_parser.py which parses raw server log entries.
TimescaleDB hypertable partitioned by login_time.

Primary uses:
- Cross-account IP linking: SELECT login FROM account_login_history
    WHERE broker_id=X AND ip_address='1.2.3.4' — finds all accounts
    that ever logged in from the same IP (linked account detection)
- CID/machine linking: same pattern on computer_id
- Investigation panel: full IP/location timeline per account
- IP/CID rule engines (future): flag accounts sharing IPs with known
    abusers, or accounts using the same machine as flagged accounts

Retention: 2 years.

Revision ID: 0040
Revises: 0039
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0040"
down_revision = "0039"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "account_login_history",

        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("source_system", sa.String(), nullable=False),        # mt4 | mt5
        sa.Column("source_account_id", sa.String(), nullable=False),
        sa.Column("login", sa.BigInteger(), nullable=False),

        sa.Column("ip_address", sa.String(), nullable=True),
        sa.Column("computer_id", sa.String(), nullable=True),           # CID / hardware fingerprint
        sa.Column("terminal_build", sa.Integer(), nullable=True),
        sa.Column("session_type", sa.Integer(), nullable=True),

        sa.Column("login_time", sa.DateTime(timezone=True), nullable=False),  # partition key
        sa.Column("raw_log_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("parsed_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False,
                  server_default=sa.text("NOW()")),
    )

    op.execute("SELECT create_hypertable('account_login_history', 'login_time')")

    # Find all accounts from a given IP address (linked account detection)
    op.create_index(
        "ix_account_login_history_broker_ip",
        "account_login_history",
        ["broker_id", "ip_address", sa.text("login_time DESC")],
    )
    # Find all accounts from a given machine (CID-based linking)
    op.create_index(
        "ix_account_login_history_broker_cid",
        "account_login_history",
        ["broker_id", "computer_id", sa.text("login_time DESC")],
    )
    # Per-account login timeline
    op.create_index(
        "ix_account_login_history_broker_account",
        "account_login_history",
        ["broker_id", "source_account_id", sa.text("login_time DESC")],
    )

    op.execute("SELECT add_retention_policy('account_login_history', INTERVAL '2 years')")


def downgrade() -> None:
    op.execute("SELECT remove_retention_policy('account_login_history', if_exists => true)")
    op.drop_index("ix_account_login_history_broker_account", table_name="account_login_history")
    op.drop_index("ix_account_login_history_broker_cid",     table_name="account_login_history")
    op.drop_index("ix_account_login_history_broker_ip",      table_name="account_login_history")
    op.drop_table("account_login_history")
