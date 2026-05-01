"""MT5 normalizer — raw_mt5_* → norm_* tables.

Reads active raw records and upserts into normalized tables.
Called before rule engine evaluation to ensure norm_* is current.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone

import structlog
from sqlalchemy import text

log = structlog.get_logger()

# MT5 volume units → lots: divide by 10000
_MT5_VOL_DIVISOR = 10_000

# MT5 deal action: 0=in (entry), 1=out (exit), 2=in/out, 3=out_by
# We normalize both 0 and 2 as complete deals (capture open+close info)
_ENTRY_ACTIONS = {0, 2}

# MT5 direction from action is embedded in deal type — direction comes from
# the associated order. We use 'entry' field: 0=in means new position.
# For norm_deals, we store direction from the deal action field where possible.
# MT5 EnDealAction: 0=buy, 1=sell for standard trades
_MT5_BUY_ACTION = 0
_MT5_SELL_ACTION = 1


def normalize_mt5_accounts(broker_id: str, server_id: str, conn) -> int:
    """
    Read raw_mt5_accounts (active) and upsert into norm_accounts.
    Returns count of upserted records.
    """
    rows = conn.execute(
        text(
            "SELECT id, login, group_name, name, balance, credit, leverage, "
            "country, registration, last_access, payload_json "
            "FROM raw_mt5_accounts "
            "WHERE broker_id = :broker_id AND server_id = :server_id AND status = 'active'"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    now = datetime.now(timezone.utc)
    upserted = 0

    # Bulk-supersede all existing active MT5 accounts for this broker/server in one shot
    conn.execute(
        text(
            "UPDATE norm_accounts SET status = 'superseded', updated_at = :now "
            "WHERE broker_id = :broker_id AND server_id = :server_id "
            "AND source_system = 'mt5' AND status = 'active'"
        ),
        {"now": now, "broker_id": broker_id, "server_id": server_id},
    )

    # Build group → swap_free lookup from admin-classified settings.
    # Groups not in the settings table default to 0 (safe default until admin classifies).
    swap_rows = conn.execute(
        text(
            "SELECT group_name, swap_free FROM broker_group_swap_settings "
            "WHERE broker_id = :broker_id AND server_id = :server_id AND source_system = 'mt5'"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()
    swap_free_groups: dict[str, int] = {
        r["group_name"]: (1 if r["swap_free"] else 0) for r in swap_rows
    }

    for row in rows:
        source_account_id = str(row["login"])
        payload = row["payload_json"] or {}

        equity = payload.get("Equity") or payload.get("equity")
        currency = payload.get("Currency") or payload.get("currency")
        is_demo = 0
        swap_free = swap_free_groups.get(row["group_name"], 0)

        conn.execute(
            text(
                "INSERT INTO norm_accounts "
                "(id, broker_id, server_id, source_system, source_account_id, login, "
                "group_name, account_name, balance, equity, credit, leverage, currency, "
                "country, swap_free, is_demo, registration_ts, last_access_ts, "
                "account_status, raw_id, normalized_at, status, created_at) "
                "VALUES (:id, :broker_id, :server_id, 'mt5', :source_account_id, :login, "
                ":group_name, :account_name, :balance, :equity, :credit, :leverage, :currency, "
                ":country, :swap_free, :is_demo, :registration_ts, :last_access_ts, "
                "'active', :raw_id, :normalized_at, 'active', NOW())"
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
                "equity": equity,
                "credit": row.get("credit"),
                "leverage": row["leverage"],
                "currency": currency,
                "country": row["country"],
                "swap_free": swap_free,
                "is_demo": is_demo,
                "registration_ts": (row["registration"] * 1000) if row["registration"] else None,
                "last_access_ts": (row["last_access"] * 1000) if row["last_access"] else None,
                "raw_id": str(row["id"]),
                "normalized_at": now,
            },
        )
        upserted += 1

    conn.commit()
    log.info("normalizer.mt5.accounts", broker_id=broker_id, upserted=upserted)
    return upserted


def normalize_mt5_deals(broker_id: str, server_id: str, conn, since: datetime | None = None) -> int:
    """
    Read raw_mt5_deals (active, entry=0 trades) and insert new deals into norm_deals.
    Only inserts deals not already present (checks ix_norm_deals_source_id).
    Returns count inserted.
    """
    params: dict = {"broker_id": broker_id, "server_id": server_id}
    since_clause = ""
    if since:
        since_clause = " AND rd.collected_at >= :since"
        params["since"] = since

    # Only fetch raw deals that haven't been normalized yet (NOT EXISTS in norm_deals)
    rows = conn.execute(
        text(
            f"SELECT rd.id, rd.deal_id, rd.login, rd.symbol, rd.action, rd.entry, rd.volume, rd.price, "
            f"rd.profit, rd.commission, rd.storage, rd.time_msc, rd.source_timestamp, rd.position_id, rd.order_id "
            f"FROM raw_mt5_deals rd "
            f"WHERE rd.broker_id = :broker_id AND rd.server_id = :server_id AND rd.status = 'active' "
            f"AND rd.entry IN (0, 2) "
            f"AND NOT EXISTS ("
            f"  SELECT 1 FROM norm_deals nd "
            f"  WHERE nd.broker_id = rd.broker_id AND nd.server_id = rd.server_id "
            f"  AND nd.source_system = 'mt5' AND nd.source_deal_id = rd.deal_id::text"
            f") "
            f"{since_clause}"
            f"ORDER BY rd.time_msc ASC"
        ),
        params,
    ).mappings().fetchall()

    if not rows:
        return 0

    inserted = 0
    now = datetime.now(timezone.utc)

    for row in rows:
        source_deal_id = str(row["deal_id"])
        source_account_id = str(row["login"])

        volume_lots = (row["volume"] or 0) / _MT5_VOL_DIVISOR
        deal_time_msc = row["time_msc"]
        deal_time = datetime.fromtimestamp(deal_time_msc / 1000, tz=timezone.utc) if deal_time_msc else now

        # Direction: MT5 action field encodes direction for standard trades
        # action=0=buy deal, action=1=sell deal (for entry deals)
        direction = row["action"] if row["action"] in (0, 1) else None

        conn.execute(
            text(
                "INSERT INTO norm_deals "
                "(id, broker_id, server_id, source_system, source_deal_id, source_account_id, "
                "login, symbol, direction, volume_lots, price, profit, commission, swap, "
                "deal_time_msc, duration_ms, deal_type, raw_id, deal_time, normalized_at) "
                "VALUES (:id, :broker_id, :server_id, 'mt5', :source_deal_id, :source_account_id, "
                ":login, :symbol, :direction, :volume_lots, :price, :profit, :commission, :swap, "
                ":deal_time_msc, NULL, 'trade', :raw_id, :deal_time, :normalized_at)"
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
                "price": row["price"],
                "profit": row["profit"],
                "commission": row["commission"],
                "swap": row["storage"],
                "deal_time_msc": deal_time_msc,
                "raw_id": str(row["id"]),
                "deal_time": deal_time,
                "normalized_at": now,
            },
        )
        inserted += 1

        # Commit every 1000 rows
        if inserted % 1000 == 0:
            conn.commit()

    conn.commit()
    log.info("normalizer.mt5.deals", broker_id=broker_id, inserted=inserted)
    return inserted


def normalize_mt5_positions(broker_id: str, server_id: str, conn) -> int:
    """
    Read raw_mt5_positions (active) and upsert into norm_positions.
    """
    rows = conn.execute(
        text(
            "SELECT id, position_id, login, symbol, action, volume, price_open, "
            "price_current, profit, storage, time_create_msc "
            "FROM raw_mt5_positions "
            "WHERE broker_id = :broker_id AND server_id = :server_id AND status = 'active'"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    now = datetime.now(timezone.utc)
    upserted = 0

    # Bulk-supersede all existing active positions for this broker/server
    conn.execute(
        text(
            "UPDATE norm_positions SET status = 'superseded', updated_at = :now "
            "WHERE broker_id = :broker_id AND server_id = :server_id "
            "AND source_system = 'mt5' AND status = 'active'"
        ),
        {"now": now, "broker_id": broker_id, "server_id": server_id},
    )

    for row in rows:
        source_position_id = str(row["position_id"])
        source_account_id = str(row["login"])
        volume_lots = (row["volume"] or 0) / _MT5_VOL_DIVISOR

        conn.execute(
            text(
                "INSERT INTO norm_positions "
                "(id, broker_id, server_id, source_system, source_position_id, source_account_id, "
                "login, symbol, direction, volume_lots, price_open, price_current, profit, swap, "
                "open_time_msc, raw_id, normalized_at, status, created_at) "
                "VALUES (:id, :broker_id, :server_id, 'mt5', :source_position_id, :source_account_id, "
                ":login, :symbol, :direction, :volume_lots, :price_open, :price_current, :profit, :swap, "
                ":open_time_msc, :raw_id, :normalized_at, 'active', NOW())"
            ),
            {
                "id": str(uuid.uuid4()),
                "broker_id": broker_id,
                "server_id": server_id,
                "source_position_id": source_position_id,
                "source_account_id": source_account_id,
                "login": row["login"],
                "symbol": row["symbol"],
                "direction": row["action"],  # MT5: 0=buy, 1=sell position
                "volume_lots": volume_lots,
                "price_open": row["price_open"],
                "price_current": row["price_current"],
                "profit": row["profit"],
                "swap": row["storage"],
                "open_time_msc": row["time_create_msc"],
                "raw_id": str(row["id"]),
                "normalized_at": now,
            },
        )
        upserted += 1

    conn.commit()
    log.info("normalizer.mt5.positions", broker_id=broker_id, upserted=upserted)
    return upserted


def normalize_mt5_symbols(broker_id: str, server_id: str, conn) -> int:
    """
    Read raw_mt5_symbols (active) and upsert into norm_symbols.
    """
    rows = conn.execute(
        text(
            "SELECT id, symbol, description, currency_base, currency_profit, "
            "digits, contract_size, swap_long, swap_short, spread "
            "FROM raw_mt5_symbols "
            "WHERE broker_id = :broker_id AND server_id = :server_id AND status = 'active'"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    now = datetime.now(timezone.utc)
    upserted = 0

    # Bulk-supersede all existing active symbols for this broker/server
    conn.execute(
        text(
            "UPDATE norm_symbols SET status = 'superseded', updated_at = :now "
            "WHERE broker_id = :broker_id AND server_id = :server_id "
            "AND source_system = 'mt5' AND status = 'active'"
        ),
        {"now": now, "broker_id": broker_id, "server_id": server_id},
    )

    for row in rows:
        conn.execute(
            text(
                "INSERT INTO norm_symbols "
                "(id, broker_id, server_id, source_system, symbol, description, currency_base, "
                "currency_profit, digits, contract_size, swap_long, swap_short, spread, "
                "raw_id, normalized_at, status, created_at) "
                "VALUES (:id, :broker_id, :server_id, 'mt5', :symbol, :description, :currency_base, "
                ":currency_profit, :digits, :contract_size, :swap_long, :swap_short, :spread, "
                ":raw_id, :normalized_at, 'active', NOW())"
            ),
            {
                "id": str(uuid.uuid4()),
                "broker_id": broker_id,
                "server_id": server_id,
                "symbol": row["symbol"],
                "description": row["description"],
                "currency_base": row["currency_base"],
                "currency_profit": row["currency_profit"],
                "digits": row["digits"],
                "contract_size": row["contract_size"],
                "swap_long": row["swap_long"],
                "swap_short": row["swap_short"],
                "spread": row["spread"],
                "raw_id": str(row["id"]),
                "normalized_at": now,
            },
        )
        upserted += 1

    conn.commit()
    log.info("normalizer.mt5.symbols", broker_id=broker_id, upserted=upserted)
    return upserted


def run_mt5_normalization(broker_id: str, server_id: str, conn) -> dict:
    """Run all MT5 normalizers. Returns counts per entity."""
    return {
        "accounts": normalize_mt5_accounts(broker_id, server_id, conn),
        "deals": normalize_mt5_deals(broker_id, server_id, conn),
        "positions": normalize_mt5_positions(broker_id, server_id, conn),
        "symbols": normalize_mt5_symbols(broker_id, server_id, conn),
    }
