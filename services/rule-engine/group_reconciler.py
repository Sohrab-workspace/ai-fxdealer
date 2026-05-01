"""Group swap-free reconciler.

After each group sync, compares the current group list on a broker/server
against broker_group_swap_settings. Any group not yet classified gets:
  1. Inserted into broker_group_swap_settings with swap_free=False (safe default)
  2. Inserted into broker_group_pending_review (status='pending')

The pending review table drives the admin notification prompt on dashboard
login. Admin then classifies each new group as swap-free or normal.

Called from the normalization phase in run_pipeline.py after groups are
collected but before norm_accounts is populated, so that the normalizer
can immediately use the swap_free settings.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone

import structlog
from sqlalchemy import text

log = structlog.get_logger()

_GROUP_TABLE = {
    "mt5": ("raw_mt5_groups", "group_name"),
    "mt4": ("raw_mt4_groups", "group_name"),
}


def reconcile_group_swap_settings(
    broker_id: str,
    server_id: str,
    source_system: str,
    conn,
) -> dict:
    """
    Detect groups with no swap classification and queue them for admin review.
    Returns {"new_groups": int, "total_groups": int}.
    """
    if source_system not in _GROUP_TABLE:
        return {"new_groups": 0, "total_groups": 0}

    table, name_col = _GROUP_TABLE[source_system]

    rows = conn.execute(
        text(
            f"SELECT DISTINCT {name_col} AS group_name FROM {table} "
            "WHERE broker_id = :broker_id AND server_id = :server_id AND status = 'active'"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()

    if not rows:
        return {"new_groups": 0, "total_groups": 0}

    group_names = [r["group_name"] for r in rows if r["group_name"]]
    now = datetime.now(timezone.utc)
    new_count = 0

    for group_name in group_names:
        existing = conn.execute(
            text(
                "SELECT 1 FROM broker_group_swap_settings "
                "WHERE broker_id = :b AND server_id = :s "
                "AND source_system = :sys AND group_name = :g"
            ),
            {"b": broker_id, "s": server_id, "sys": source_system, "g": group_name},
        ).fetchone()

        if existing:
            continue

        # New group — register with safe default
        conn.execute(
            text(
                "INSERT INTO broker_group_swap_settings "
                "(id, broker_id, server_id, source_system, group_name, swap_free, created_at) "
                "VALUES (:id, :b, :s, :sys, :g, false, NOW()) "
                "ON CONFLICT (broker_id, server_id, source_system, group_name) DO NOTHING"
            ),
            {
                "id": str(uuid.uuid4()),
                "b": broker_id,
                "s": server_id,
                "sys": source_system,
                "g": group_name,
            },
        )

        # Queue for admin notification
        conn.execute(
            text(
                "INSERT INTO broker_group_pending_review "
                "(id, broker_id, server_id, source_system, group_name, "
                " status, detected_at, created_at) "
                "VALUES (:id, :b, :s, :sys, :g, 'pending', :detected_at, NOW()) "
                "ON CONFLICT (broker_id, server_id, source_system, group_name) "
                "WHERE status = 'pending' DO NOTHING"
            ),
            {
                "id": str(uuid.uuid4()),
                "b": broker_id,
                "s": server_id,
                "sys": source_system,
                "g": group_name,
                "detected_at": now,
            },
        )

        new_count += 1

    if new_count > 0:
        conn.commit()
        log.info(
            "group_reconciler.new_groups",
            broker_id=broker_id,
            server_id=server_id,
            source_system=source_system,
            new_groups=new_count,
            total_groups=len(group_names),
        )

    return {"new_groups": new_count, "total_groups": len(group_names)}


def get_swap_free_groups(
    broker_id: str,
    server_id: str,
    source_system: str,
    conn,
) -> set[str]:
    """Return the set of group names classified as swap_free=True."""
    rows = conn.execute(
        text(
            "SELECT group_name FROM broker_group_swap_settings "
            "WHERE broker_id = :b AND server_id = :s "
            "AND source_system = :sys AND swap_free = true"
        ),
        {"b": broker_id, "s": server_id, "sys": source_system},
    ).mappings().fetchall()
    return {r["group_name"] for r in rows}


def get_pending_review_count(broker_id: str, conn) -> int:
    """Return count of groups awaiting admin swap-free classification."""
    return conn.execute(
        text(
            "SELECT count(*) FROM broker_group_pending_review "
            "WHERE broker_id = :b AND status = 'pending'"
        ),
        {"b": broker_id},
    ).scalar() or 0
