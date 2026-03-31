"""
cTrader Reporting DB — Schema & Sample Data Capture Script

Usage:
    python capture_schema.py

Requires:
    - stunnel running (C:\Program Files (x86)\stunnel\bin\stunnel.exe)
    - psycopg2-binary (pip install psycopg2-binary)
    - IP whitelisted at support@spotware.com

Output:
    .claude/references/ctrader/reporting-db/{table_name}.md
"""

import os
import re
import psycopg2
import psycopg2.extras

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "reporting-db")

DEMO_CONN = dict(
    host="127.0.0.1",
    port=5432,
    user="opofinance_demo_repo",
    password="k0OKby8J",
    dbname="ctrader_spotware",
    connect_timeout=20,
)

LIVE_CONN = dict(
    host="127.0.0.1",
    port=5433,
    user="opofinance_live_repo",
    password="90mVYphS",
    dbname="ctrader_spotware",
    connect_timeout=20,
)

# PII field patterns — values will be replaced with [REDACTED]
PII_PATTERNS = re.compile(
    r"(email|name|phone|mobile|address|first|last|login|username|password|national_id|passport|ssn)",
    re.IGNORECASE,
)


def redact_row(columns, row):
    result = []
    for col, val in zip(columns, row):
        if val is not None and PII_PATTERNS.search(col):
            result.append("[REDACTED]")
        else:
            result.append(val)
    return result


def get_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
              AND table_type = 'BASE TABLE'
            ORDER BY table_name
        """)
        return [row[0] for row in cur.fetchall()]


def get_columns(conn, table):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT
                c.column_name,
                c.data_type,
                c.is_nullable,
                c.column_default,
                pg_catalog.col_description(
                    (quote_ident(c.table_schema) || '.' || quote_ident(c.table_name))::regclass::oid,
                    c.ordinal_position
                ) AS description
            FROM information_schema.columns c
            WHERE c.table_schema = 'public'
              AND c.table_name = %s
            ORDER BY c.ordinal_position
        """, (table,))
        return cur.fetchall()


def get_samples(conn, table, columns, limit=3):
    with conn.cursor() as cur:
        try:
            cur.execute(f'SELECT * FROM "{table}" LIMIT {limit}')
            rows = cur.fetchall()
            col_names = [desc[0] for desc in cur.description]
            redacted = [redact_row(col_names, row) for row in rows]
            return col_names, redacted
        except Exception as e:
            return [c[0] for c in columns], []


def write_table_md(table, columns, sample_cols, sample_rows):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, f"{table}.md")

    col_table = "| Column | Type | Nullable | Default | Description |\n"
    col_table += "|--------|------|----------|---------|-------------|\n"
    for col in columns:
        name, dtype, nullable, default, desc = col
        col_table += f"| `{name}` | {dtype} | {nullable} | {default or ''} | {desc or ''} |\n"

    sample_md = ""
    if sample_rows:
        header = " | ".join(f"`{c}`" for c in sample_cols)
        separator = " | ".join("---" for _ in sample_cols)
        sample_md = f"| {header} |\n| {separator} |\n"
        for row in sample_rows:
            cells = " | ".join(str(v) if v is not None else "NULL" for v in row)
            sample_md += f"| {cells} |\n"
    else:
        sample_md = "_No rows returned or table is empty._"

    content = f"""# `{table}`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

{col_table}
## Sample Data

{sample_md}

## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Written: {path}")


def main():
    print("Connecting to Demo DB...")
    try:
        conn = psycopg2.connect(**DEMO_CONN)
        print("Connected.")
    except Exception as e:
        print(f"Connection failed: {e}")
        print("\nCheck that:")
        print("  1. stunnel is running")
        print("  2. Your IP (check with: curl https://api.ipify.org) is whitelisted at support@spotware.com")
        return

    tables = get_tables(conn)
    print(f"Found {len(tables)} tables: {', '.join(tables)}\n")

    for table in tables:
        print(f"Processing: {table}")
        columns = get_columns(conn, table)
        sample_cols, sample_rows = get_samples(conn, table, columns)
        write_table_md(table, columns, sample_cols, sample_rows)

    conn.close()
    print("\nDone. Files written to:", OUTPUT_DIR)
    print("Update .claude/references/ctrader/README.md table list if new tables were found.")


if __name__ == "__main__":
    main()
