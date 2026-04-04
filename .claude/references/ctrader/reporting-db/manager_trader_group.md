# `manager_trader_group`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `manager_id` | bigint | NO |  |  |
| `trader_group_id` | bigint | NO |  |  |

## Sample Data

| `manager_id` | `trader_group_id` |
| --- | --- |
| 1009 | 1000 |
| 1017 | 1089 |
| 1017 | 1090 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
