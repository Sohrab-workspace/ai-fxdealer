"""cTrader normalizer — raw_ctrader_* → norm_* tables.

cTrader key differences:
- Volumes: cents of lot (divide by lot_size*100 for lots; default lot_size=100000)
- Monetary: cents (divide by 10^money_digits; default money_digits=2)
- Timestamps: Unix milliseconds
- trade_side: BUY=1, SELL=2
- Deals: ProtoDeal — execution records
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone

import structlog
from sqlalchemy import text

log = structlog.get_logger()

_DEFAULT_LOT_SIZE = 100_000   # standard forex lot
_DEFAULT_MONEY_DIGITS = 2     # divide cents by 100 for USD


def _to_lots(volume_cents: int | None, lot_size: int = _DEFAULT_LOT_SIZE) -> float | None:
    if volume_cents is None:
        return None
    return volume_cents / (lot_size * 100)


def _to_currency(cents: int | None, money_digits: int = _DEFAULT_MONEY_DIGITS) -> float | None:
    if cents is None:
        return None
    return cents / (10 ** money_digits)


def normalize_ctrader_accounts(broker_id: str, server_id: str, conn) -> int:
    rows = conn.execute(
        text(
            "SELECT id, trader_id, login, group_id, balance_cents, account_type, "
            "registration_ts, last_connect_ts, online, deleted, swap_free, "
            "leverage_in_cents, money_digits "
            "FROM raw_ctrader_accounts "
            "WHERE broker_id = :broker_id AND server_id = :server_id AND status = 'active' "
            "AND (deleted IS NULL OR deleted = 0)"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    now = datetime.now(timezone.utc)
    upserted = 0

    # Bulk-supersede all existing active cTrader accounts for this broker/server
    conn.execute(
        text(
            "UPDATE norm_accounts SET status = 'superseded', updated_at = :now "
            "WHERE broker_id = :broker_id AND server_id = :server_id "
            "AND source_system = 'ctrader' AND status = 'active'"
        ),
        {"now": now, "broker_id": broker_id, "server_id": server_id},
    )

    for row in rows:
        source_account_id = str(row["trader_id"])
        money_digits = row["money_digits"] or _DEFAULT_MONEY_DIGITS
        leverage = int((row["leverage_in_cents"] or 0) / 100) or None
        balance = _to_currency(row["balance_cents"], money_digits)
        swap_free = 1 if row["swap_free"] else 0

        conn.execute(
            text(
                "INSERT INTO norm_accounts "
                "(id, broker_id, server_id, source_system, source_account_id, login, "
                "balance, leverage, swap_free, registration_ts, last_access_ts, "
                "account_status, raw_id, normalized_at, status, created_at) "
                "VALUES (:id, :broker_id, :server_id, 'ctrader', :source_account_id, :login, "
                ":balance, :leverage, :swap_free, :registration_ts, :last_access_ts, "
                "'active', :raw_id, :normalized_at, 'active', NOW())"
            ),
            {
                "id": str(uuid.uuid4()),
                "broker_id": broker_id,
                "server_id": server_id,
                "source_account_id": source_account_id,
                "login": row["login"],
                "balance": balance,
                "leverage": leverage,
                "swap_free": swap_free,
                "registration_ts": row["registration_ts"],
                "last_access_ts": row["last_connect_ts"],
                "raw_id": str(row["id"]),
                "normalized_at": now,
            },
        )
        upserted += 1

    conn.commit()
    log.info("normalizer.ctrader.accounts", broker_id=broker_id, upserted=upserted)
    return upserted


def normalize_ctrader_deals(broker_id: str, server_id: str, conn) -> int:
    """
    raw_ctrader_deals → norm_deals.
    trade_side: BUY=1→direction=0, SELL=2→direction=1
    """
    # Only fetch raw deals not yet in norm_deals
    rows = conn.execute(
        text(
            "SELECT rd.id, rd.deal_id, rd.trader_id, rd.symbol_id, rd.volume, rd.filled_volume, "
            "rd.execution_price, rd.trade_side, rd.create_ts, rd.execution_ts, rd.commission, "
            "rd.money_digits, rd.deal_status "
            "FROM raw_ctrader_deals rd "
            "WHERE rd.broker_id = :broker_id AND rd.server_id = :server_id AND rd.status = 'active' "
            "AND rd.deal_status = 2 "
            "AND NOT EXISTS ("
            "  SELECT 1 FROM norm_deals nd "
            "  WHERE nd.broker_id = rd.broker_id AND nd.server_id = rd.server_id "
            "  AND nd.source_system = 'ctrader' AND nd.source_deal_id = rd.deal_id::text"
            ")"
        ),
        {"broker_id": broker_id, "server_id": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    inserted = 0
    now = datetime.now(timezone.utc)

    for row in rows:
        source_deal_id = str(row["deal_id"])
        source_account_id = str(row["trader_id"])

        money_digits = row["money_digits"] or _DEFAULT_MONEY_DIGITS
        # cTrader volumes are in cents of lot, use filled_volume
        volume_lots = _to_lots(row["filled_volume"] or row["volume"])
        commission = _to_currency(row["commission"], money_digits)

        # trade_side: 1=BUY→0, 2=SELL→1
        trade_side = row["trade_side"] or 0
        direction = 0 if trade_side == 1 else (1 if trade_side == 2 else None)

        deal_time_msc = row["execution_ts"] or row["create_ts"]
        deal_time = (datetime.fromtimestamp(deal_time_msc / 1000, tz=timezone.utc)
                     if deal_time_msc else now)

        conn.execute(
            text(
                "INSERT INTO norm_deals "
                "(id, broker_id, server_id, source_system, source_deal_id, source_account_id, "
                "login, direction, volume_lots, price, commission, deal_time_msc, "
                "deal_type, raw_id, deal_time, normalized_at) "
                "VALUES (:id, :broker_id, :server_id, 'ctrader', :source_deal_id, :source_account_id, "
                ":login, :direction, :volume_lots, :price, :commission, :deal_time_msc, "
                "'trade', :raw_id, :deal_time, :normalized_at)"
            ),
            {
                "id": str(uuid.uuid4()),
                "broker_id": broker_id,
                "server_id": server_id,
                "source_deal_id": source_deal_id,
                "source_account_id": source_account_id,
                "login": row["trader_id"],  # use trader_id as login for cTrader
                "direction": direction,
                "volume_lots": volume_lots,
                "price": row["execution_price"],
                "commission": commission,
                "deal_time_msc": deal_time_msc,
                "raw_id": str(row["id"]),
                "deal_time": deal_time,
                "normalized_at": now,
            },
        )
        inserted += 1

        if inserted % 1000 == 0:
            conn.commit()

    conn.commit()
    log.info("normalizer.ctrader.deals", broker_id=broker_id, inserted=inserted)
    return inserted


def run_ctrader_normalization(broker_id: str, server_id: str, conn) -> dict:
    return {
        "accounts": normalize_ctrader_accounts(broker_id, server_id, conn),
        "deals": normalize_ctrader_deals(broker_id, server_id, conn),
    }
