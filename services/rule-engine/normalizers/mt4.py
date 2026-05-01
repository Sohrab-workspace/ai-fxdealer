"""MT4 normalizer — raw_mt4_* → norm_* tables.

MT4 key differences:
- Volume: lots*100 (divide by 100 for standard lots)
- Timestamps: Unix seconds (multiply by 1000 for ms)
- Deals: TradeRecords with close_time > 0
- No ms precision — duration calculated as (close_time - open_time) * 1000
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone

import structlog
from sqlalchemy import text

log = structlog.get_logger()

_MT4_VOL_DIVISOR = 100  # lots*100 → lots


def normalize_mt4_accounts(broker_id: str, server_id: str, conn) -> int:
    rows = conn.execute(
        text(
            "SELECT id, login, group_name, name, balance, credit, leverage, "
            "country, regdate, lastdate "
            "FROM raw_mt4_accounts "
            "WHERE broker_id = :broker_id AND server_id = :server_id AND status = 'active'"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    now = datetime.now(timezone.utc)
    upserted = 0

    # Bulk-supersede all existing active MT4 accounts for this broker/server
    conn.execute(
        text(
            "UPDATE norm_accounts SET status = 'superseded', updated_at = :now "
            "WHERE broker_id = :broker_id AND server_id = :server_id "
            "AND source_system = 'mt4' AND status = 'active'"
        ),
        {"now": now, "broker_id": broker_id, "server_id": server_id},
    )

    # Build group → swap_free lookup from admin-classified settings.
    swap_rows = conn.execute(
        text(
            "SELECT group_name, swap_free FROM broker_group_swap_settings "
            "WHERE broker_id = :broker_id AND server_id = :server_id AND source_system = 'mt4'"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()
    swap_free_groups: dict[str, int] = {
        r["group_name"]: (1 if r["swap_free"] else 0) for r in swap_rows
    }

    for row in rows:
        source_account_id = str(row["login"])
        swap_free = swap_free_groups.get(row["group_name"], 0)

        conn.execute(
            text(
                "INSERT INTO norm_accounts "
                "(id, broker_id, server_id, source_system, source_account_id, login, "
                "group_name, account_name, balance, credit, leverage, country, swap_free, is_demo, "
                "registration_ts, last_access_ts, account_status, raw_id, normalized_at, status, created_at) "
                "VALUES (:id, :broker_id, :server_id, 'mt4', :source_account_id, :login, "
                ":group_name, :account_name, :balance, :credit, :leverage, :country, :swap_free, 0, "
                ":registration_ts, :last_access_ts, 'active', :raw_id, :normalized_at, 'active', NOW())"
            ),
            {
                "id": str(uuid.uuid4()),
                "broker_id": broker_id,
                "server_id": server_id,
                "source_account_id": source_account_id,
                "login": row["login"],
                "group_name": row["group_name"],
                "account_name": row["name"],
                "balance": row["balance"],
                "credit": row["credit"],
                "leverage": row["leverage"],
                "country": row["country"],
                "swap_free": swap_free,
                "registration_ts": (row["regdate"] * 1000) if row["regdate"] else None,
                "last_access_ts": (row["lastdate"] * 1000) if row["lastdate"] else None,
                "raw_id": str(row["id"]),
                "normalized_at": now,
            },
        )
        upserted += 1

    conn.commit()
    log.info("normalizer.mt4.accounts", broker_id=broker_id, upserted=upserted)
    return upserted


def normalize_mt4_deals(broker_id: str, server_id: str, conn) -> int:
    """
    Raw MT4 deals (closed TradeRecords, close_time > 0) → norm_deals.
    MT4 cmd: 0=BUY, 1=SELL, 6=BALANCE, 7=CREDIT
    """
    # Only fetch raw deals not yet in norm_deals
    rows = conn.execute(
        text(
            "SELECT rd.id, rd.order_id, rd.login, rd.symbol, rd.cmd, rd.volume, rd.open_time, rd.close_time, "
            "rd.open_price, rd.close_price, rd.profit, rd.commission, rd.storage "
            "FROM raw_mt4_deals rd "
            "WHERE rd.broker_id = :broker_id AND rd.server_id = :server_id AND rd.status = 'active' "
            "AND NOT EXISTS ("
            "  SELECT 1 FROM norm_deals nd "
            "  WHERE nd.broker_id = rd.broker_id AND nd.server_id = rd.server_id "
            "  AND nd.source_system = 'mt4' AND nd.source_deal_id = rd.order_id::text"
            ")"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    inserted = 0
    now = datetime.now(timezone.utc)

    for row in rows:
        source_deal_id = str(row["order_id"])
        source_account_id = str(row["login"])

        cmd = row["cmd"] or 0
        # direction: 0=buy, 1=sell — map MT4 cmd
        direction = 0 if cmd == 0 else (1 if cmd == 1 else None)
        deal_type = "trade" if cmd in (0, 1) else ("balance" if cmd == 6 else "credit")

        volume_lots = (row["volume"] or 0) / _MT4_VOL_DIVISOR
        open_time_msc = (row["open_time"] * 1000) if row["open_time"] else None
        close_time_msc = (row["close_time"] * 1000) if row["close_time"] else None
        deal_time_msc = close_time_msc or open_time_msc
        duration_ms = ((row["close_time"] - row["open_time"]) * 1000
                       if row["close_time"] and row["open_time"] else None)

        deal_time = (datetime.fromtimestamp(deal_time_msc / 1000, tz=timezone.utc)
                     if deal_time_msc else now)

        conn.execute(
            text(
                "INSERT INTO norm_deals "
                "(id, broker_id, server_id, source_system, source_deal_id, source_account_id, "
                "login, symbol, direction, volume_lots, price, profit, commission, swap, "
                "open_time_msc, close_time_msc, deal_time_msc, duration_ms, deal_type, "
                "raw_id, deal_time, normalized_at) "
                "VALUES (:id, :broker_id, :server_id, 'mt4', :source_deal_id, :source_account_id, "
                ":login, :symbol, :direction, :volume_lots, :price, :profit, :commission, :swap, "
                ":open_time_msc, :close_time_msc, :deal_time_msc, :duration_ms, :deal_type, "
                ":raw_id, :deal_time, :normalized_at)"
            ),
            {
                "id": str(uuid.uuid4()),
                "broker_id": broker_id,
                "server_id": server_id,
                "source_deal_id": source_deal_id,
                "source_account_id": source_account_id,
                "login": row["login"],
                "symbol": row["symbol"],
                "direction": direction,
                "volume_lots": volume_lots,
                "price": row["close_price"],
                "profit": row["profit"],
                "commission": row["commission"],
                "swap": row["storage"],
                "open_time_msc": open_time_msc,
                "close_time_msc": close_time_msc,
                "deal_time_msc": deal_time_msc,
                "duration_ms": duration_ms,
                "deal_type": deal_type,
                "raw_id": str(row["id"]),
                "deal_time": deal_time,
                "normalized_at": now,
            },
        )
        inserted += 1

        if inserted % 1000 == 0:
            conn.commit()

    conn.commit()
    log.info("normalizer.mt4.deals", broker_id=broker_id, inserted=inserted)
    return inserted


def run_mt4_normalization(broker_id: str, server_id: str, conn) -> dict:
    return {
        "accounts": normalize_mt4_accounts(broker_id, server_id, conn),
        "deals": normalize_mt4_deals(broker_id, server_id, conn),
    }
