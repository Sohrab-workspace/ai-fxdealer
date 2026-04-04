# `dynamic_commission`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `trader_group_id` | bigint | NO |  |  |
| `monthly_volume` | numeric | NO |  |  |
| `discount` | numeric | NO |  |  |

## Sample Data

| `trader_group_id` | `monthly_volume` | `discount` |
| --- | --- | --- |
| 1055 | 0.00 | 0.0000 |
| 1080 | 0.00 | 0.0000 |
| 1083 | 0.00 | 0.0000 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
