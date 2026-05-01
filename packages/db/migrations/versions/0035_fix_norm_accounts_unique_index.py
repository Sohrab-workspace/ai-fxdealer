"""Fix norm_accounts unique index to include source_system.

The original index (broker_id, server_id, source_account_id) WHERE status='active'
didn't include source_system, causing conflicts when different platforms (MT4/MT5/cTrader)
share the same login numbers.

Revision ID: 0035
"""

from alembic import op

revision = "0035"
down_revision = "0034"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("DROP INDEX IF EXISTS uq_norm_accounts_active")
    op.execute(
        "CREATE UNIQUE INDEX uq_norm_accounts_active "
        "ON norm_accounts(broker_id, server_id, source_system, source_account_id) "
        "WHERE status = 'active'"
    )


def downgrade():
    op.execute("DROP INDEX IF EXISTS uq_norm_accounts_active")
    op.execute(
        "CREATE UNIQUE INDEX uq_norm_accounts_active "
        "ON norm_accounts(broker_id, server_id, source_account_id) "
        "WHERE status = 'active'"
    )
