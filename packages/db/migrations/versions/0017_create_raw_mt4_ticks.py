"""Create raw_mt4_ticks table

Revision ID: 0017
Revises: 0016
Create Date: 2026-03-27

Notes:
- TimescaleDB hypertable — partitioned by collected_at
- Retention policy: 90 days (CLAUDE.md: raw tick data)
- MT4 ticks have only 3 fields: ctm (unix seconds), bid, ask — no last/volume unlike MT5
- Symbol is not in the TickAPI payload; collector must inject it before storing
- Ticks are append-only — no status, ingestion_hash, updated_at, archived_at
- Source: mtmanapi.dll TicksRequest() — TickAPI struct (3 fields), captured 2026-03-26
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0017"
down_revision = "0016"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_mt4_ticks",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Extracted fields
        sa.Column("symbol", sa.String(), nullable=False),               # added by collector (not in TickAPI)
        sa.Column("ctm", sa.BigInteger(), nullable=False),              # unix second timestamp
        sa.Column("bid", sa.Float(), nullable=True),
        sa.Column("ask", sa.Float(), nullable=True),
        sa.Column("source_timestamp", sa.DateTime(timezone=True), nullable=True),  # derived from ctm

        sa.Column("payload_json", postgresql.JSONB(astext_type=sa.Text()), nullable=False),

        # Append-only — no status, ingestion_hash, updated_at, archived_at
        sa.Column("collected_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("NOW()")),
    )

    op.execute("SELECT create_hypertable('raw_mt4_ticks', 'collected_at')")

    op.create_index(
        "ix_raw_mt4_ticks_broker_symbol_collected",
        "raw_mt4_ticks", ["broker_id", "symbol", sa.text("collected_at DESC")],
    )
    op.create_index(
        "ix_raw_mt4_ticks_broker_collected",
        "raw_mt4_ticks", ["broker_id", sa.text("collected_at DESC")],
    )

    op.execute("SELECT add_retention_policy('raw_mt4_ticks', INTERVAL '90 days')")


def downgrade() -> None:
    op.execute("SELECT remove_retention_policy('raw_mt4_ticks', if_exists => true)")
    op.drop_index("ix_raw_mt4_ticks_broker_collected", table_name="raw_mt4_ticks")
    op.drop_index("ix_raw_mt4_ticks_broker_symbol_collected", table_name="raw_mt4_ticks")
    op.drop_table("raw_mt4_ticks")
