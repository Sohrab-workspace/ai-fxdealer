"""Shared raw record ingestion helpers.

Used by all collector services to:
- Upsert raw records with superseding deduplication pattern
- Write collector run logs (raw_collector_runs)
- Write collector error logs (raw_collector_errors)

All operations use synchronous SQLAlchemy (collectors run in sync threads
dispatched by ARQ). Database URL comes from FXDEALER_DB_URL env var.
"""

import os
import uuid
from datetime import datetime, timezone
from typing import Any

import structlog
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

log = structlog.get_logger()

_engine = None
_Session = None


def _get_session() -> Session:
    global _engine, _Session
    if _engine is None:
        url = os.environ.get("FXDEALER_DB_URL")
        if not url:
            raise RuntimeError("FXDEALER_DB_URL environment variable is not set.")
        _engine = create_engine(url, pool_pre_ping=True, pool_size=5, max_overflow=10)
        _Session = sessionmaker(bind=_engine)
    return _Session()


def save_raw_records(
    table_name: str,
    rows: list[dict],
    dedup_columns: list[str] | None = None,
) -> int:
    """
    Insert raw records with superseding deduplication.

    For each incoming row:
    1. If a matching active record exists (same dedup_columns + status='active'):
       - Mark existing as 'superseded', set archived_at = NOW()
    2. Insert the new record as status='active'

    Returns count of rows inserted.
    """
    if not rows:
        return 0

    session = _get_session()
    inserted = 0

    try:
        with session.begin():
            for row in rows:
                # Supersede any existing active record
                if dedup_columns:
                    where_clauses = " AND ".join(
                        f"{col} = :{col}" for col in dedup_columns if col in row
                    )
                    if where_clauses:
                        params = {col: row[col] for col in dedup_columns if col in row}
                        params["now"] = datetime.now(timezone.utc)
                        session.execute(
                            text(
                                f"""
                                UPDATE {table_name}
                                SET status = 'superseded', archived_at = :now, updated_at = :now
                                WHERE {where_clauses}
                                  AND status = 'active'
                                """
                            ),
                            params,
                        )

                # Build INSERT with only columns present in the row
                cols = list(row.keys())
                col_names = ", ".join(cols)
                placeholders = ", ".join(f":{col}" for col in cols)
                insert_params = {}
                for col in cols:
                    val = row[col]
                    if isinstance(val, uuid.UUID):
                        insert_params[col] = str(val)
                    elif isinstance(val, dict | list):
                        import json
                        insert_params[col] = json.dumps(val, default=str)
                    else:
                        insert_params[col] = val

                session.execute(
                    text(f"INSERT INTO {table_name} ({col_names}) VALUES ({placeholders})"),
                    insert_params,
                )
                inserted += 1

        return inserted

    except Exception as exc:
        log.error("ingestion.save_raw.error", table=table_name, error=str(exc))
        raise
    finally:
        session.close()


def log_collector_run(run: dict) -> None:
    """Write a collector run result to raw_collector_runs."""
    session = _get_session()
    try:
        row = {
            "id":              str(uuid.uuid4()),
            "broker_id":       str(run["broker_id"]),
            "source_system":   run["source_system"],
            "connection_id":   str(run.get("connection_id", "")),
            "server_id":       str(run["server_id"]) if run.get("server_id") else None,
            "sync_mode":       run.get("sync_mode", "incremental"),
            "status":          run.get("status", "success"),
            "records_fetched": run.get("records_fetched", 0),
            "records_saved":   run.get("records_saved", 0),
            "duration_ms":     run.get("duration_ms"),
            "cursor_from":     run.get("cursor_from"),
            "cursor_to":       run.get("cursor_to"),
            "error_message":   run.get("error_message"),
            "collected_at":    run.get("collected_at", datetime.now(timezone.utc)),
            "created_at":      datetime.now(timezone.utc),
        }
        cols = [k for k, v in row.items() if v is not None]
        col_names = ", ".join(cols)
        placeholders = ", ".join(f":{col}" for col in cols)
        params = {col: row[col] for col in cols}

        with session.begin():
            session.execute(
                text(f"INSERT INTO raw_collector_runs ({col_names}) VALUES ({placeholders})"),
                params,
            )
    except Exception as exc:
        log.error("ingestion.log_run.error", error=str(exc))
    finally:
        session.close()


def log_collector_error(err: dict) -> None:
    """Write a collector error to raw_collector_errors."""
    import json
    session = _get_session()
    try:
        context_json = err.get("context_json", {})
        row = {
            "id":            str(uuid.uuid4()),
            "broker_id":     str(err["broker_id"]),
            "source_system": err["source_system"],
            "connection_id": str(err.get("connection_id", "")),
            "server_id":     str(err["server_id"]) if err.get("server_id") else None,
            "error_type":    err.get("error_type", "Unknown"),
            "error_message": err.get("error_message", ""),
            "context_json":  json.dumps(context_json, default=str) if context_json else None,
            "collected_at":  err.get("collected_at", datetime.now(timezone.utc)),
            "created_at":    datetime.now(timezone.utc),
        }
        cols = [k for k, v in row.items() if v is not None]
        col_names = ", ".join(cols)
        placeholders = ", ".join(f":{col}" for col in cols)
        params = {col: row[col] for col in cols}

        with session.begin():
            session.execute(
                text(f"INSERT INTO raw_collector_errors ({col_names}) VALUES ({placeholders})"),
                params,
            )
    except Exception as exc:
        log.error("ingestion.log_error.error", error=str(exc))
    finally:
        session.close()
