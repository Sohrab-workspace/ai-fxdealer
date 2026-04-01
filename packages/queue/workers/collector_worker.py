"""ARQ worker definitions for the collector job scheduler.

Each job runs in broker-scoped context with a dedicated collector instance.
Scheduling is handled by ARQ — never use cron or bare asyncio loops.

Job payload shape (ctx["job_data"]):
    broker_id      str (UUID)
    server_id      str (UUID)
    source_system  str — mt4 | mt5 | ctrader | fxbo
    connection_id  str (UUID)
    sync_mode      str — bootstrap | incremental
    cursor         str | None — last processed timestamp or ID

Circuit-breaker state is tracked in Redis:
    Key: fxdealer:circuit:{broker_id}:{source_system}
    Value: "open" | "closed"
    TTL:  10 minutes when open

Retry policy (from CLAUDE.md error-handling standard):
    3 retries with exponential backoff: 5s, 30s, 120s
"""

import asyncio
import importlib
import os
import uuid
from datetime import datetime, timezone
from typing import Any

import structlog
from arq import cron
from arq.connections import RedisSettings

from queue.redis_client import get_redis_url

log = structlog.get_logger()

# ── Circuit-breaker helpers ───────────────────────────────────────────────────

CIRCUIT_OPEN_TTL_SECONDS = 600   # 10 minutes
CONSECUTIVE_FAILURES_THRESHOLD = 5

_CIRCUIT_KEY = "fxdealer:circuit:{broker_id}:{source_system}"
_FAILURES_KEY = "fxdealer:failures:{broker_id}:{source_system}"


async def _is_circuit_open(redis, broker_id: str, source_system: str) -> bool:
    key = _CIRCUIT_KEY.format(broker_id=broker_id, source_system=source_system)
    return bool(await redis.exists(key))


async def _record_failure(redis, broker_id: str, source_system: str) -> int:
    key = _FAILURES_KEY.format(broker_id=broker_id, source_system=source_system)
    count = await redis.incr(key)
    await redis.expire(key, CIRCUIT_OPEN_TTL_SECONDS)
    return count


async def _open_circuit(redis, broker_id: str, source_system: str) -> None:
    key = _CIRCUIT_KEY.format(broker_id=broker_id, source_system=source_system)
    await redis.set(key, "open", ex=CIRCUIT_OPEN_TTL_SECONDS)
    # Reset failure counter
    fail_key = _FAILURES_KEY.format(broker_id=broker_id, source_system=source_system)
    await redis.delete(fail_key)


async def _close_circuit(redis, broker_id: str, source_system: str) -> None:
    key = _CIRCUIT_KEY.format(broker_id=broker_id, source_system=source_system)
    await redis.delete(key)
    fail_key = _FAILURES_KEY.format(broker_id=broker_id, source_system=source_system)
    await redis.delete(fail_key)


# ── Collector factory ─────────────────────────────────────────────────────────

def _get_collector_class(source_system: str):
    """Dynamically import the collector class for the given source system."""
    module_map = {
        "mt5":     ("collector_mt5.collector", "MT5Collector"),
        "mt4":     ("collector_mt4.collector", "MT4Collector"),
        "ctrader": ("collector_ctrader.collector", "CTraderCollector"),
        "fxbo":    ("collector_fxbo.collector", "FXBOCollector"),
    }
    if source_system not in module_map:
        raise ValueError(f"Unknown source_system: {source_system!r}")
    module_path, class_name = module_map[source_system]
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


# ── ARQ job functions ─────────────────────────────────────────────────────────

async def run_bootstrap_sync(ctx: dict, job_data: dict) -> dict:
    """
    Full historical backfill for all entities on a broker+server connection.

    Called once per connection on initial setup or forced re-sync.
    Runs bootstrap_sync() which fetches all available history.
    """
    broker_id = job_data["broker_id"]
    source_system = job_data["source_system"]
    redis = ctx["redis"]

    log.info(
        "collector.bootstrap.start",
        broker_id=broker_id,
        source_system=source_system,
        server_id=job_data.get("server_id"),
    )

    if await _is_circuit_open(redis, broker_id, source_system):
        log.warning(
            "collector.bootstrap.circuit_open",
            broker_id=broker_id,
            source_system=source_system,
        )
        return {"status": "skipped", "reason": "circuit_open"}

    CollectorClass = _get_collector_class(source_system)
    collector = CollectorClass(
        broker_id=uuid.UUID(broker_id),
        server_id=uuid.UUID(job_data["server_id"]) if job_data.get("server_id") else None,
        connection_id=uuid.UUID(job_data.get("connection_id") or str(uuid.uuid4())),
        config=job_data.get("config", {}),
    )

    retries = [5, 30, 120]
    for attempt, backoff in enumerate(retries, 1):
        try:
            collector.connect()
            result = collector.bootstrap_sync(
                start_time=job_data.get("start_time"),
                end_time=job_data.get("end_time"),
            )
            await _close_circuit(redis, broker_id, source_system)
            log.info(
                "collector.bootstrap.completed",
                broker_id=broker_id,
                source_system=source_system,
                **{k: v for k, v in result.items() if isinstance(v, (str, int, float, bool))},
            )
            return result
        except Exception as exc:
            count = await _record_failure(redis, broker_id, source_system)
            log.error(
                "collector.bootstrap.error",
                broker_id=broker_id,
                source_system=source_system,
                attempt=attempt,
                error=str(exc),
            )
            collector.handle_error(exc, {"sync_mode": "bootstrap", "attempt": attempt})

            if count >= CONSECUTIVE_FAILURES_THRESHOLD:
                await _open_circuit(redis, broker_id, source_system)
                log.critical(
                    "collector.circuit.opened",
                    broker_id=broker_id,
                    source_system=source_system,
                    consecutive_failures=count,
                )
                raise

            if attempt < len(retries):
                await asyncio.sleep(backoff)

    raise RuntimeError(f"Bootstrap sync failed after {len(retries)} attempts")


async def run_incremental_sync(ctx: dict, job_data: dict) -> dict:
    """
    Incremental data collection from last known cursor position.

    Scheduled via ARQ cron — runs every N seconds per broker per server.
    Advances cursor on success; holds cursor on save failure.
    """
    broker_id = job_data["broker_id"]
    source_system = job_data["source_system"]
    redis = ctx["redis"]

    if await _is_circuit_open(redis, broker_id, source_system):
        log.warning(
            "collector.incremental.circuit_open",
            broker_id=broker_id,
            source_system=source_system,
        )
        return {"status": "skipped", "reason": "circuit_open"}

    CollectorClass = _get_collector_class(source_system)
    collector = CollectorClass(
        broker_id=uuid.UUID(broker_id),
        server_id=uuid.UUID(job_data["server_id"]) if job_data.get("server_id") else None,
        connection_id=uuid.UUID(job_data.get("connection_id") or str(uuid.uuid4())),
        config=job_data.get("config", {}),
    )

    try:
        collector.connect()
        result = collector.incremental_sync(cursor=job_data.get("cursor"))
        await _close_circuit(redis, broker_id, source_system)
        log.info(
            "collector.incremental.completed",
            broker_id=broker_id,
            source_system=source_system,
            **{k: v for k, v in result.items() if isinstance(v, (str, int, float, bool))},
        )
        return result
    except Exception as exc:
        count = await _record_failure(redis, broker_id, source_system)
        log.error(
            "collector.incremental.error",
            broker_id=broker_id,
            source_system=source_system,
            error=str(exc),
        )
        collector.handle_error(exc, {"sync_mode": "incremental", "cursor": job_data.get("cursor")})

        if count >= CONSECUTIVE_FAILURES_THRESHOLD:
            await _open_circuit(redis, broker_id, source_system)
            log.critical(
                "collector.circuit.opened",
                broker_id=broker_id,
                source_system=source_system,
                consecutive_failures=count,
            )
        raise


# ── ARQ WorkerSettings ────────────────────────────────────────────────────────

def _redis_settings_from_url() -> RedisSettings:
    """Parse FXDEALER_REDIS_URL into ARQ RedisSettings."""
    from urllib.parse import urlparse
    url = get_redis_url()
    parsed = urlparse(url)
    return RedisSettings(
        host=parsed.hostname or "localhost",
        port=parsed.port or 6379,
        password=parsed.password,
        database=int(parsed.path.lstrip("/") or 0),
    )


class WorkerSettings:
    """ARQ worker configuration. Pass to `arq.run_worker(WorkerSettings)`."""

    redis_settings = _redis_settings_from_url()

    functions = [
        run_bootstrap_sync,
        run_incremental_sync,
    ]

    # Retry policy: 3 attempts with exponential backoff
    max_tries = 3
    job_timeout = 3600        # 1 hour max per sync job
    keep_result = 3600        # keep job results for 1 hour

    on_startup = None
    on_shutdown = None
