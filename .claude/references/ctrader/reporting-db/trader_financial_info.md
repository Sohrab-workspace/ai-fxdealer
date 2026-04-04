# `trader_financial_info`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `trader_id` | bigint | NO |  |  |
| `balance` | bigint | NO | 0 |  |
| `balance_version` | bigint | NO |  |  |
| `nonwithdrawable_bonus` | bigint | NO | 0 |  |
| `total_volume_in_usd` | bigint | NO | 0 |  |
| `equity_based_roi` | double precision | NO | 0 |  |
| `cash_equity` | bigint | NO | 0 |  |
| `unrealized_profit` | bigint | NO | 0 |  |
| `time_weighted_roi` | double precision | NO | 0 |  |
| `last_ea` | bigint | NO | 0 |  |
| `last_deal_execution_timestamp` | timestamp without time zone | YES |  | Execution timestamp of last deal |
| `management_fee` | bigint | YES |  |  |
| `first_deposit` | bigint | YES |  |  |
| `first_deposit_timestamp` | timestamp without time zone | YES |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |

## Sample Data

| `trader_id` | `balance` | `balance_version` | `nonwithdrawable_bonus` | `total_volume_in_usd` | `equity_based_roi` | `cash_equity` | `unrealized_profit` | `time_weighted_roi` | `last_ea` | `last_deal_execution_timestamp` | `management_fee` | `first_deposit` | `first_deposit_timestamp` | `utc_last_update_timestamp` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1022 | 10303096 | 96 | 0 | 402996854 | -0.0667459400694016 | 10303096 | 0 | 0.0 | [REDACTED] | [REDACTED] | NULL | [REDACTED] | [REDACTED] | [REDACTED] |
| 666 | 0 | 1 | 0 | 0 | 0.0 | 0 | 0 | 0.0 | [REDACTED] | NULL | NULL | NULL | NULL | [REDACTED] |
| 1000 | 0 | 1 | 0 | 0 | 0.0 | 0 | 0 | 0.0 | [REDACTED] | NULL | NULL | NULL | NULL | [REDACTED] |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
