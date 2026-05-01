"""Create re_rule_engines and re_rule_configs tables + seed rule engines

Revision ID: 0031
Revises: 0030
Create Date: 2026-04-21

Notes:
- re_rule_engines: catalog of available detection rules (seeded here)
- re_rule_configs: per-broker per-rule threshold overrides
- Seeds LARB (Latency Arbitrage), PGE (Price Gap Exploitation), SFA (Swap-Free Abuse)
- Brokers start with NULL configs (use defaults from code) until explicitly configured
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import uuid

revision = "0031"
down_revision = "0030"
branch_labels = None
depends_on = None

# Seed UUIDs — fixed so references are stable across environments
_LARB_ID = "a1b2c3d4-0001-0001-0001-000000000001"
_PGE_ID  = "a1b2c3d4-0002-0002-0002-000000000002"
_SFA_ID  = "a1b2c3d4-0003-0003-0003-000000000003"


def upgrade() -> None:
    # ── re_rule_engines ──────────────────────────────────────────────────────
    op.create_table(
        "re_rule_engines",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("handler", sa.String(), nullable=False),              # LARB | PGE | SFA
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("version", sa.String(), nullable=True, server_default="1.0.0"),
        sa.Column("is_active", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),

        sa.UniqueConstraint("handler", name="uq_re_rule_engines_handler"),
    )

    # Seed the three initial rule engines
    op.execute(
        f"""
        INSERT INTO re_rule_engines (id, handler, name, description, version, is_active)
        VALUES
          ('{_LARB_ID}', 'LARB', 'Latency Arbitrage',
           'Detects traders exploiting price feed latency between broker and LP/market reference price.',
           '1.0.0', 1),
          ('{_PGE_ID}',  'PGE',  'Price Gap Exploitation',
           'Detects traders opening positions to profit from price gaps at market open or news events.',
           '1.0.0', 1),
          ('{_SFA_ID}',  'SFA',  'Swap-Free Hedging Abuse',
           'Detects traders exploiting swap-free grace periods via hedged positions to accumulate positive swap.',
           '1.0.0', 1)
        """
    )

    # ── re_rule_configs ──────────────────────────────────────────────────────
    op.create_table(
        "re_rule_configs",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("rule_engine_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("is_active", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("evaluation_window_hours", sa.Integer(), nullable=True, server_default="168"),
        sa.Column("min_score_alert", sa.Integer(), nullable=True, server_default="50"),
        sa.Column("config_json", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),

        sa.ForeignKeyConstraint(["rule_engine_id"], ["re_rule_engines.id"], name="fk_re_rule_configs_rule_engine"),
        sa.UniqueConstraint("broker_id", "rule_engine_id", name="uq_re_rule_configs_broker_rule"),
    )
    op.create_index("ix_re_rule_configs_broker_id", "re_rule_configs", ["broker_id"])


def downgrade() -> None:
    op.drop_index("ix_re_rule_configs_broker_id", table_name="re_rule_configs")
    op.drop_table("re_rule_configs")
    op.drop_table("re_rule_engines")
