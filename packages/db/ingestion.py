"""Shared raw record ingestion helpers.

Used by all collector services to:
- Upsert raw records with superseding deduplication pattern
- Write collector run logs (raw_collector_runs)
- Write collector error logs (raw_collector_errors)

All operations use synchronous SQLAlchemy (collectors run in sync threads
dispatched by ARQ). Database URL comes from FXDEALER_DB_URL env var.
"""

import json
import os
import uuid
from datetime import datetime, timezone

import structlog
from psycopg2.extras import execute_values
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session

log = structlog.get_logger()

_engine = None
_Session = None

_CHUNK_SIZE = 2000  # rows per bulk operation


def _get_session() -> Session:
    global _engine, _Session
    if _engine is None:
        url = os.environ.get("FXDEALER_DB_URL")
        if not url:
            raise RuntimeError("FXDEALER_DB_URL environment variable is not set.")
        _engine = create_engine(url, pool_pre_ping=True, pool_size=5, max_overflow=10)
        _Session = sessionmaker(bind=_engine)
    return _Session()


def _serialize_row(row: dict) -> dict:
    """Prepare a row dict for psycopg2 — convert UUIDs and dicts to DB-safe types."""
    out = {}
    for col, val in row.items():
        if isinstance(val, uuid.UUID):
            out[col] = str(val)
        elif isinstance(val, (dict, list)):
            out[col] = json.dumps(val, default=str)
        else:
            out[col] = val
    return out


def save_raw_records(
    table_name: str,
    rows: list[dict],
    dedup_columns: list[str] | None = None,
) -> int:
    """
    Insert raw records with superseding deduplication, using bulk operations.

    For each chunk of rows:
    1. Bulk UPDATE: mark any existing active records with matching dedup keys
       as 'superseded' using a single IN-clause query per chunk.
    2. Bulk INSERT: insert all new rows in one execute_values call.

    This replaces the previous row-by-row approach which was too slow for
    large entity batches (e.g. 800k+ deals).

    Returns total count of rows inserted.
    """
    if not rows:
        return 0

    inserted = 0
    now = datetime.now(timezone.utc)

    # Quote column names once — handles SQL reserved words (group, time, type …)
    if rows:
        cols = list(rows[0].keys())
        quoted_cols = ", ".join(f'"{c}"' for c in cols)

    for chunk_start in range(0, len(rows), _CHUNK_SIZE):
        chunk = rows[chunk_start: chunk_start + _CHUNK_SIZE]
        serialized = [_serialize_row(r) for r in chunk]

        session = _get_session()
        try:
            raw_conn = session.connection().connection
            cur = raw_conn.cursor()

            # ── Step 1: bulk supersede existing active records ────────────────
            if dedup_columns:
                valid_dedup = [c for c in dedup_columns if c in (chunk[0] if chunk else {})]
                if valid_dedup:
                    # Build tuple list of dedup key values for the IN clause
                    key_tuples = tuple(
                        tuple(str(r[c]) if isinstance(r[c], uuid.UUID) else r[c] for c in valid_dedup)
                        for r in chunk
                    )
                    quoted_dedup = ", ".join(f'"{c}"' for c in valid_dedup)
                    placeholders = ", ".join(["%s"] * len(valid_dedup))

                    update_sql = f"""
                        UPDATE {table_name}
                        SET status = 'superseded',
                            archived_at = %s,
                            updated_at = %s
                        WHERE ({quoted_dedup}) IN %s
                          AND status = 'active'
                    """
                    cur.execute(update_sql, (now, now, key_tuples))

            # ── Step 2: bulk insert all rows in one shot ──────────────────────
            values = [tuple(r[c] for c in cols) for r in serialized]
            insert_sql = f"INSERT INTO {table_name} ({quoted_cols}) VALUES %s"
            execute_values(cur, insert_sql, values, page_size=500)

            raw_conn.commit()
            inserted += len(chunk)

        except Exception as exc:
            try:
                raw_conn.rollback()
            except Exception:
                pass
            log.error("ingestion.save_raw.error", table=table_name, error=str(exc))
            raise
        finally:
            session.close()

    return inserted


def save_tick_records(table_name: str, rows: list[dict]) -> int:
    """
    Append-only bulk insert for tick tables.

    Tick tables (raw_mt5_ticks, raw_mt4_ticks) have no status / ingestion_hash /
    archived_at columns — they are append-only TimescaleDB hypertables.
    This bypasses the supersede step used by save_raw_records.
    """
    if not rows:
        return 0

    inserted = 0
    cols = list(rows[0].keys())
    quoted_cols = ", ".join(f'"{c}"' for c in cols)

    for chunk_start in range(0, len(rows), _CHUNK_SIZE):
        chunk = rows[chunk_start: chunk_start + _CHUNK_SIZE]
        serialized = [_serialize_row(r) for r in chunk]

        session = _get_session()
        try:
            raw_conn = session.connection().connection
            cur = raw_conn.cursor()
            values = [tuple(r[c] for c in cols) for r in serialized]
            execute_values(cur, f"INSERT INTO {table_name} ({quoted_cols}) VALUES %s", values, page_size=500)
            raw_conn.commit()
            inserted += len(chunk)
        except Exception as exc:
            try:
                raw_conn.rollback()
            except Exception:
                pass
            log.error("ingestion.save_ticks.error", table=table_name, error=str(exc))
            raise
        finally:
            session.close()

    return inserted


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
