"""Create raw_ctrader_symbols table

Revision ID: 0026
Revises: 0025
Create Date: 2026-04-01

Notes:
- Plain PostgreSQL — low volume config/reference data
- Source: Spotware Manager API → ProtoManagerSymbolListReq (payloadType 467)
- ProtoManagerSymbol fields are Protobuf-number-keyed (no stable string names in API)
- Only fields 1 (symbolId), 5 (digits), 17 (lotSize), 18 (minVolume) extracted
- Symbol name is nested inside a length-delimited protobuf field — not directly parseable
  without the full .proto schema; stored in payload_json only
- Full payload_json preserves all fields for future parsing improvements
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0026"
down_revision = "0025"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "raw_ctrader_symbols",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("broker_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("server_id", postgresql.UUID(as_uuid=True), nullable=True),

        # Key ProtoManagerSymbol fields (field numbers from live capture)
        sa.Column("symbol_id", sa.BigInteger(), nullable=False),             # field 1 — internal ID
        sa.Column("digits", sa.Integer(), nullable=True),                    # field 5 — price decimals
        sa.Column("lot_size", sa.BigInteger(), nullable=True),               # field 17 — e.g. 100000
        sa.Column("min_volume", sa.BigInteger(), nullable=True),             # field 18 — cents of lot
        # symbol_name nested in protobuf sub-message — not extractable without .proto schema
        # Collector should attempt extraction and store here if available

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
        CREATE UNIQUE INDEX uq_raw_ctrader_symbols_active
        ON raw_ctrader_symbols (broker_id, server_id, symbol_id)
        WHERE status = 'active'
        """
    )
    op.create_index("ix_raw_ctrader_symbols_broker_collected", "raw_ctrader_symbols", ["broker_id", "collected_at"])


def downgrade() -> None:
    op.drop_index("ix_raw_ctrader_symbols_broker_collected", table_name="raw_ctrader_symbols")
    op.execute("DROP INDEX IF EXISTS uq_raw_ctrader_symbols_active")
    op.drop_table("raw_ctrader_symbols")
