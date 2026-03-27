"""Alembic migration environment for ai-fxdealer packages/db.

Database URL is read from the FXDEALER_DB_URL environment variable.
Never hardcode credentials here.

Usage:
    # Apply all pending migrations
    cd packages/db
    FXDEALER_DB_URL=postgresql+psycopg2://user:pass@host/dbname alembic upgrade head

    # Generate a new migration (autogenerate from model changes)
    FXDEALER_DB_URL=... alembic revision --autogenerate -m "describe the change"

    # Roll back one step
    FXDEALER_DB_URL=... alembic downgrade -1
"""

import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Import Base so Alembic can autogenerate migrations from model definitions.
# All models must be imported (directly or transitively) before autogenerate runs.
from db.models import Base  # noqa: F401  — registers all table metadata

# ── Alembic Config object (provides access to alembic.ini values) ──────────
config = context.config

# ── Logging ─────────────────────────────────────────────────────────────────
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ── Target metadata for autogenerate ────────────────────────────────────────
target_metadata = Base.metadata


def get_url() -> str:
    url = os.environ.get("FXDEALER_DB_URL")
    if not url:
        raise RuntimeError(
            "FXDEALER_DB_URL environment variable is not set. "
            "Set it before running Alembic commands.\n"
            "Example: export FXDEALER_DB_URL=postgresql+psycopg2://user:pass@localhost:5432/fxdealer"
        )
    return url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode (no live DB connection required).

    Emits SQL to stdout so it can be reviewed or piped to a file.
    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode with a live database connection."""
    configuration = config.get_section(config.config_ini_section, {})
    configuration["sqlalchemy.url"] = get_url()

    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
