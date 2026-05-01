"""Server log parser — extracts login events (IP/CID) from raw server logs.

Reads raw_mt5_server_logs and raw_mt4_server_logs, parses login event
messages, and writes to account_login_history.

MT5 login message format (MTLog.Message):
  "0' 12345678 login from 192.168.1.100 [ComputerID: abc123, Build: 2755, Type: 0x1 (0x1)]"

MT4 login message format (ServerLog.description):
  "12345678: login from 192.168.1.100 build 1234 (terminal_id=abc123)"
  or simply:
  "12345678 login from 192.168.1.100"

Both formats are handled by permissive regex — partial matches are accepted
as long as login number and IP are present.

Processing is idempotent: already-parsed raw_log rows have is_login_event=true
and are skipped on the next run. Batch size is capped at 50k rows per call
to keep memory bounded on large log volumes.
"""

from __future__ import annotations

import re
import uuid
from datetime import datetime, timezone

import structlog
from sqlalchemy import text

log = structlog.get_logger()

# MT5 login event regex — permissive, handles multiple server versions.
# Captures: (1) login, (2) ip_address, (3) computer_id?, (4) build?, (5) session_type_hex?
_MT5_LOGIN_RE = re.compile(
    r"(?:'?\d*'?\s+)?(\d{4,})\s+login\s+from\s+([\d.]+|[0-9a-fA-F:]+)"
    r"(?:[^[]*\[ComputerID:\s*([a-fA-F0-9]{8,}))?"
    r"(?:.*?Build:\s*(\d+))?"
    r"(?:.*?Type:\s*(0x[0-9a-fA-F]+))?",
    re.IGNORECASE | re.DOTALL,
)

# MT4 login event regex
# Captures: (1) login, (2) ip_address, (3) build?, (4) terminal_id?
_MT4_LOGIN_RE = re.compile(
    r"(\d{4,})[\s:]+login\s+from\s+([\d.]+)"
    r"(?:\s+build\s+(\d+))?"
    r"(?:.*?terminal_id=([a-fA-F0-9]+))?",
    re.IGNORECASE | re.DOTALL,
)

_BATCH_SIZE = 50_000


def _parse_mt5_login(message: str) -> dict | None:
    if not message or "login" not in message.lower():
        return None
    m = _MT5_LOGIN_RE.search(message)
    if not m or not m.group(1) or not m.group(2):
        return None
    session_type = None
    if m.group(5):
        try:
            session_type = int(m.group(5), 16)
        except ValueError:
            pass
    return {
        "login":          int(m.group(1)),
        "ip_address":     m.group(2),
        "computer_id":    m.group(3),
        "terminal_build": int(m.group(4)) if m.group(4) else None,
        "session_type":   session_type,
    }


def _parse_mt4_login(message: str) -> dict | None:
    if not message or "login" not in message.lower():
        return None
    m = _MT4_LOGIN_RE.search(message)
    if not m or not m.group(1) or not m.group(2):
        return None
    return {
        "login":          int(m.group(1)),
        "ip_address":     m.group(2),
        "computer_id":    m.group(4),
        "terminal_build": int(m.group(3)) if m.group(3) else None,
        "session_type":   None,
    }


def _insert_login_event(conn, broker_id, server_id, source_system, parsed, log_time, raw_log_id, now):
    conn.execute(
        text(
            "INSERT INTO account_login_history "
            "(id, broker_id, server_id, source_system, source_account_id, login, "
            " ip_address, computer_id, terminal_build, session_type, "
            " login_time, raw_log_id, parsed_at, created_at) "
            "VALUES (:id, :b, :s, :sys, :account_id, :login, "
            " :ip, :cid, :build, :stype, "
            " :login_time, :raw_log_id, :parsed_at, NOW())"
        ),
        {
            "id":         str(uuid.uuid4()),
            "b":          broker_id,
            "s":          server_id,
            "sys":        source_system,
            "account_id": str(parsed["login"]),
            "login":      parsed["login"],
            "ip":         parsed["ip_address"],
            "cid":        parsed["computer_id"],
            "build":      parsed["terminal_build"],
            "stype":      parsed["session_type"],
            "login_time": log_time,
            "raw_log_id": raw_log_id,
            "parsed_at":  now,
        },
    )


def parse_mt5_server_logs(broker_id: str, server_id: str, conn) -> int:
    """Parse unprocessed MT5 server logs for login events → account_login_history."""
    rows = conn.execute(
        text(
            "SELECT id, log_time, message FROM raw_mt5_server_logs "
            "WHERE broker_id = :b AND server_id = :s AND status = 'active' "
            "AND is_login_event = false "
            "AND message IS NOT NULL AND message ILIKE '%login from%' "
            "ORDER BY log_time ASC "
            f"LIMIT {_BATCH_SIZE}"
        ),
        {"b": broker_id, "s": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    now = datetime.now(timezone.utc)
    inserted = 0

    for row in rows:
        parsed = _parse_mt5_login(row["message"])
        if not parsed:
            continue

        _insert_login_event(
            conn, broker_id, server_id, "mt5",
            parsed, row["log_time"], str(row["id"]), now,
        )

        # Mark raw row as parsed and back-fill extracted columns
        conn.execute(
            text(
                "UPDATE raw_mt5_server_logs "
                "SET is_login_event = true, login = :login, "
                "    ip_address = :ip, computer_id = :cid "
                "WHERE id = :id"
            ),
            {
                "login": parsed["login"],
                "ip":    parsed["ip_address"],
                "cid":   parsed["computer_id"],
                "id":    str(row["id"]),
            },
        )

        inserted += 1
        if inserted % 1000 == 0:
            conn.commit()

    conn.commit()
    log.info("log_parser.mt5", broker_id=broker_id, inserted=inserted)
    return inserted


def parse_mt4_server_logs(broker_id: str, server_id: str, conn) -> int:
    """Parse unprocessed MT4 server logs for login events → account_login_history."""
    rows = conn.execute(
        text(
            "SELECT id, log_time, message FROM raw_mt4_server_logs "
            "WHERE broker_id = :b AND server_id = :s AND status = 'active' "
            "AND is_login_event = false "
            "AND message IS NOT NULL AND message ILIKE '%login from%' "
            "ORDER BY log_time ASC "
            f"LIMIT {_BATCH_SIZE}"
        ),
        {"b": broker_id, "s": server_id},
    ).mappings().fetchall()

    if not rows:
        return 0

    now = datetime.now(timezone.utc)
    inserted = 0

    for row in rows:
        parsed = _parse_mt4_login(row["message"])
        if not parsed:
            continue

        _insert_login_event(
            conn, broker_id, server_id, "mt4",
            parsed, row["log_time"], str(row["id"]), now,
        )

        conn.execute(
            text(
                "UPDATE raw_mt4_server_logs "
                "SET is_login_event = true, login = :login, "
                "    ip_address = :ip, computer_id = :cid "
                "WHERE id = :id"
            ),
            {
                "login": parsed["login"],
                "ip":    parsed["ip_address"],
                "cid":   parsed["computer_id"],
                "id":    str(row["id"]),
            },
        )

        inserted += 1
        if inserted % 1000 == 0:
            conn.commit()

    conn.commit()
    log.info("log_parser.mt4", broker_id=broker_id, inserted=inserted)
    return inserted


def run_log_parsing(broker_id: str, mt5_server_id: str, mt4_server_id: str, conn) -> dict:
    return {
        "mt5_login_events": parse_mt5_server_logs(broker_id, mt5_server_id, conn),
        "mt4_login_events": parse_mt4_server_logs(broker_id, mt4_server_id, conn),
    }
