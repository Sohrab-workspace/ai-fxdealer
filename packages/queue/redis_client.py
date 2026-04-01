"""Redis client factory for ARQ job scheduler and Redis Streams.

All connection details come from FXDEALER_REDIS_URL environment variable.
Never hardcode credentials here.
"""

import os
from redis.asyncio import Redis, ConnectionPool

_pool: ConnectionPool | None = None


def get_redis_url() -> str:
    url = os.environ.get("FXDEALER_REDIS_URL")
    if not url:
        raise RuntimeError(
            "FXDEALER_REDIS_URL environment variable is not set. "
            "Example: redis://:password@localhost:6379/0"
        )
    return url


async def get_redis_pool() -> ConnectionPool:
    """Return a shared async connection pool. Creates it on first call."""
    global _pool
    if _pool is None:
        _pool = ConnectionPool.from_url(
            get_redis_url(),
            max_connections=20,
            decode_responses=False,
        )
    return _pool


async def get_redis() -> Redis:
    """Return an async Redis client using the shared pool."""
    pool = await get_redis_pool()
    return Redis(connection_pool=pool)
