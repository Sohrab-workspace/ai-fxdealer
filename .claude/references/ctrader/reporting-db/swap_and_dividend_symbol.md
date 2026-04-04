# `swap_and_dividend_symbol`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `swap_and_dividend_profile_id` | bigint | NO |  |  |
| `symbol_id` | integer | NO |  |  |
| `swap_rollover_3days` | smallint | YES |  | NONE(0), MONDAY(1), TUESDAY(2), WEDNESDAY(3), THURSDAY(4), FRIDAY(5), SATURDAY(6), SUNDAY(7) |
| `swap_long` | numeric | YES |  |  |
| `swap_short` | numeric | YES |  |  |
| `swap_calculation_type` | integer | YES |  | PIPS(0), PERCENTAGE(1), POINTS(2) |
| `dividends_long` | bigint | NO | 0 |  |
| `dividends_short` | bigint | NO | 0 |  |
| `dividend_time` | timestamp without time zone | YES |  |  |
| `swap_time` | integer | YES |  |  |
| `swap_period` | integer | YES |  |  |
| `skip_swap_periods` | integer | YES |  |  |
| `charge_swap_at_weekends` | boolean | YES |  |  |

## Sample Data

| `swap_and_dividend_profile_id` | `symbol_id` | `swap_rollover_3days` | `swap_long` | `swap_short` | `swap_calculation_type` | `dividends_long` | `dividends_short` | `dividend_time` | `swap_time` | `swap_period` | `skip_swap_periods` | `charge_swap_at_weekends` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 22 | 3 | -0.22 | -0.2 | 0 | 0 | 0 | NULL | 1319 | 24 | 0 | False |
| 2 | 24 | 3 | -3.37 | 0.68 | 0 | 0 | 0 | NULL | 1319 | 24 | 0 | False |
| 2 | 29 | 3 | 3.18 | -9.19 | 0 | 0 | 0 | NULL | 1319 | 24 | 0 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
