# `trader_group_symbol`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `trader_group_id` | bigint | NO |  |  |
| `symbol_id` | bigint | NO |  |  |
| `enabled` | boolean | NO |  |  |
| `commission_profile_id` | bigint | YES |  |  |
| `volume_profile_id` | bigint | YES |  |  |
| `execution_profile_id` | bigint | YES |  |  |
| `protection_profile_id` | bigint | YES |  |  |
| `swap_free_profile_id` | bigint | YES |  |  |
| `gsl_schedule_id` | bigint | YES |  |  |
| `leverage_id` | bigint | YES |  |  |
| `trade_notification_profile_id` | bigint | YES |  |  |

## Sample Data

| `trader_group_id` | `symbol_id` | `enabled` | `commission_profile_id` | `volume_profile_id` | `execution_profile_id` | `protection_profile_id` | `swap_free_profile_id` | `gsl_schedule_id` | `leverage_id` | `trade_notification_profile_id` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1023 | 1 | True | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL |
| 1023 | 2 | True | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL |
| 1023 | 3 | True | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
