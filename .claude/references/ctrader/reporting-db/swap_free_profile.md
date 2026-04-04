# `swap_free_profile`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `swap_free_profile_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `rollover_commission` | bigint | NO | 0 |  |
| `skip_rollover_days` | integer | NO | 3 |  |
| `rollover_charge_period` | integer | NO | 1 |  |
| `rollover_commission_3days` | integer | NO | 0 | NONE(0), MONDAY(1), TUESDAY(2), WEDNESDAY(3), THURSDAY(4), FRIDAY(5), SATURDAY(6), SUNDAY(7) |
| `utc_last_update_timestamp` | timestamp without time zone | YES |  |  |
| `deleted` | boolean | NO | false |  |

## Sample Data

| `swap_free_profile_id` | `name` | `description` | `rollover_commission` | `skip_rollover_days` | `rollover_charge_period` | `rollover_commission_3days` | `utc_last_update_timestamp` | `deleted` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [REDACTED] | NULL | 0 | 3 | 1 | 3 | [REDACTED] | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
