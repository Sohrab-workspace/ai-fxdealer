# `daily_equity`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `trader_id` | bigint | NO |  |  |
| `date` | date | NO |  |  |
| `equity` | bigint | NO | 0 |  |
| `min_equity` | bigint | NO | 0 |  |
| `max_equity` | bigint | NO | 0 |  |
| `balance` | bigint | NO |  |  |
| `usd_volume` | bigint | NO |  |  |
| `time_weighted_roi` | double precision | NO |  |  |
| `period_equity` | bigint | YES |  |  |
| `is_precise_money` | boolean | NO | false | FALSE is for 2 digits, TRUE is for 8 digits |
| `all_time_abs_roi` | bigint | NO | 0 |  |
| `all_time_abs_equity_trade_dif` | bigint | NO | 0 |  |
| `equity_based_roi_usd` | bigint | NO | 0 |  |
| `all_time_roi` | double precision | NO | 0 |  |
| `vol_per_bal` | integer | NO | 0 |  |

## Sample Data

| `trader_id` | `date` | `equity` | `min_equity` | `max_equity` | `balance` | `usd_volume` | `time_weighted_roi` | `period_equity` | `is_precise_money` | `all_time_abs_roi` | `all_time_abs_equity_trade_dif` | `equity_based_roi_usd` | `all_time_roi` | `vol_per_bal` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1020 | 2023-08-02 | 0 | 0 | 0 | 0 | 0 | 0.0 | NULL | False | 0 | 0 | 0 | 0.0 | 0 |
| 1021 | 2023-08-14 | 100000 | 0 | 100000 | 100000 | 0 | 0.0 | 0 | False | 0 | 0 | 0 | 0.0 | 0 |
| 1021 | 2023-08-15 | 100000 | 100000 | 100000 | 100000 | 0 | 0.0 | NULL | False | 0 | 0 | 0 | 0.0 | 0 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
