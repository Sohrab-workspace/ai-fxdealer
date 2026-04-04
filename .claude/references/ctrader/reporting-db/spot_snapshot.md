# `spot_snapshot`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `price` | bigint | NO |  |  |
| `side` | character | NO |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `symbol_id` | bigint | NO |  |  |

## Sample Data

| `price` | `side` | `create_timestamp` | `symbol_id` |
| --- | --- | --- | --- |
| 115222 | A | 2026-04-03 20:55:00.035000 | 1 |
| 115139 | B | 2026-04-03 20:55:00.035000 | 1 |
| 132082 | A | 2026-04-03 20:55:00.043000 | 2 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
