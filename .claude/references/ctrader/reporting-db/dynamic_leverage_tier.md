# `dynamic_leverage_tier`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `leverage_id` | bigint | NO |  |  |
| `volume` | bigint | NO |  |  |
| `leverage` | integer | NO |  |  |

## Sample Data

| `leverage_id` | `volume` | `leverage` |
| --- | --- | --- |
| 1001 | 1000000 | 50000 |
| 1002 | 10000000 | 5000 |
| 1003 | 10000000 | 50000 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
