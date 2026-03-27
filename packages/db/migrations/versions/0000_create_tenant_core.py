"""Create tenant core tables

Revision ID: 0000
Revises:
Create Date: 2026-03-27

Notes:
- Plain PostgreSQL tables (low-volume config/reference per CLAUDE.md)
- Tables: brokers, broker_servers, broker_users, broker_crm_connections,
          broker_integrations, roles, user_broker_roles, audit_logs
- Credentials are never stored here — only AWS Secrets Manager key references
- audit_logs: broker_id and actor_id are bare UUIDs (no FK) so the log
  survives tenant or user deletion; no soft delete on audit logs
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0000"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ------------------------------------------------------------------
    # brokers
    # ------------------------------------------------------------------
    op.create_table(
        "brokers",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("slug", sa.String(), nullable=False),          # subdomain: broker-name.fxdealer.com
        sa.Column("status", sa.String(), nullable=False, server_default="active"),  # active | archived
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("uq_brokers_slug", "brokers", ["slug"], unique=True)

    # ------------------------------------------------------------------
    # broker_servers
    # ------------------------------------------------------------------
    op.create_table(
        "broker_servers",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("brokers.id"), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("source_system", sa.String(), nullable=False),  # mt4 | mt5 | ctrader
        sa.Column("host", sa.String(), nullable=True),
        sa.Column("port", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_broker_servers_broker_id", "broker_servers", ["broker_id"])

    # ------------------------------------------------------------------
    # broker_users
    # ------------------------------------------------------------------
    op.create_table(
        "broker_users",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("brokers.id"), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.Column("full_name", sa.String(), nullable=True),
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.execute(
        """
        CREATE UNIQUE INDEX uq_broker_users_broker_email
        ON broker_users (broker_id, email)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_broker_users_broker_id", "broker_users", ["broker_id"])

    # ------------------------------------------------------------------
    # broker_crm_connections
    # ------------------------------------------------------------------
    op.create_table(
        "broker_crm_connections",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("brokers.id"), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("crm_type", sa.String(), nullable=False),       # fxbo | other
        sa.Column("host", sa.String(), nullable=True),            # CRM API base URL or host
        sa.Column("secret_key_ref", sa.String(), nullable=True),  # AWS Secrets Manager key name only
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_broker_crm_connections_broker_id", "broker_crm_connections", ["broker_id"])

    # ------------------------------------------------------------------
    # broker_integrations
    # ------------------------------------------------------------------
    op.create_table(
        "broker_integrations",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("brokers.id"), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("integration_type", sa.String(), nullable=False),  # bridge | lp | notification | market_data | other
        sa.Column("config_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),  # non-secret config
        sa.Column("secret_key_ref", sa.String(), nullable=True),     # AWS Secrets Manager key name only
        sa.Column("status", sa.String(), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_broker_integrations_broker_id", "broker_integrations", ["broker_id"])

    # ------------------------------------------------------------------
    # roles
    # ------------------------------------------------------------------
    op.create_table(
        "roles",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("name", sa.String(), nullable=False),            # admin | dealer | readonly
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )
    op.create_index("uq_roles_name", "roles", ["name"], unique=True)

    # ------------------------------------------------------------------
    # user_broker_roles
    # ------------------------------------------------------------------
    op.create_table(
        "user_broker_roles",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("broker_users.id"), nullable=False),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("brokers.id"), nullable=False),
        sa.Column("role_id", postgresql.UUID(as_uuid=True), sa.ForeignKey("roles.id"), nullable=False),
        sa.Column("assigned_by", postgresql.UUID(as_uuid=True), sa.ForeignKey("broker_users.id"), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )
    op.execute(
        """
        CREATE UNIQUE INDEX uq_user_broker_roles
        ON user_broker_roles (user_id, broker_id, role_id)
        """
    )
    op.create_index("ix_user_broker_roles_broker_id", "user_broker_roles", ["broker_id"])
    op.create_index("ix_user_broker_roles_user_id", "user_broker_roles", ["user_id"])

    # ------------------------------------------------------------------
    # audit_logs
    # ------------------------------------------------------------------
    op.create_table(
        "audit_logs",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        # Bare UUIDs — no FK constraints so log survives tenant or user deletion
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("actor_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("action", sa.String(), nullable=False),          # e.g. "account.restrict", "rule.update"
        sa.Column("resource_type", sa.String(), nullable=False),   # e.g. "account", "rule", "user"
        sa.Column("resource_id", sa.String(), nullable=True),      # external or internal ID of affected resource
        sa.Column("detail_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("ip_address", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )
    op.create_index("ix_audit_logs_broker_id", "audit_logs", ["broker_id"])
    op.create_index("ix_audit_logs_actor_id", "audit_logs", ["actor_id"])
    op.create_index(
        "ix_audit_logs_broker_resource",
        "audit_logs", ["broker_id", "resource_type", "resource_id"],
    )

    # Seed the three platform roles
    op.execute(
        """
        INSERT INTO roles (id, name, description, created_at)
        VALUES
            (gen_random_uuid(), 'admin',    'Full access. Manages users, config, rules, executes all actions.', NOW()),
            (gen_random_uuid(), 'dealer',   'Investigates accounts, views all data, executes dealer actions. Cannot manage users.', NOW()),
            (gen_random_uuid(), 'readonly', 'Views data and dashboards only. Cannot execute actions or change config.', NOW())
        """
    )


def downgrade() -> None:
    op.drop_index("ix_audit_logs_broker_resource", table_name="audit_logs")
    op.drop_index("ix_audit_logs_actor_id", table_name="audit_logs")
    op.drop_index("ix_audit_logs_broker_id", table_name="audit_logs")
    op.drop_table("audit_logs")

    op.drop_index("ix_user_broker_roles_user_id", table_name="user_broker_roles")
    op.drop_index("ix_user_broker_roles_broker_id", table_name="user_broker_roles")
    op.execute("DROP INDEX IF EXISTS uq_user_broker_roles")
    op.drop_table("user_broker_roles")

    op.execute("DROP INDEX IF EXISTS uq_roles_name")
    op.drop_table("roles")

    op.drop_index("ix_broker_integrations_broker_id", table_name="broker_integrations")
    op.drop_table("broker_integrations")

    op.drop_index("ix_broker_crm_connections_broker_id", table_name="broker_crm_connections")
    op.drop_table("broker_crm_connections")

    op.drop_index("ix_broker_users_broker_id", table_name="broker_users")
    op.execute("DROP INDEX IF EXISTS uq_broker_users_broker_email")
    op.drop_table("broker_users")

    op.drop_index("ix_broker_servers_broker_id", table_name="broker_servers")
    op.drop_table("broker_servers")

    op.execute("DROP INDEX IF EXISTS uq_brokers_slug")
    op.drop_table("brokers")
