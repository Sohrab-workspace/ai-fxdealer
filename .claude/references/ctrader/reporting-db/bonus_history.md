# `bonus_history`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `bonus_history_id` | bigint | NO |  |  |
| `trader_id` | bigint | NO |  |  |
| `manager_delta` | bigint | NO |  |  |
| `manager_bonus` | bigint | NO |  |  |
| `ib_delta` | bigint | NO |  |  |
| `ib_bonus` | bigint | NO |  |  |
| `operation_type` | integer | NO |  | BONUS_DEPOSIT(0), BONUS_WITHDRAW(1) |
| `description` | character varying | YES |  |  |
| `external_note` | character varying | YES |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `introducing_broker_id` | bigint | YES |  |  |
| `is_precise_money` | boolean | NO | false | FALSE is for 2 digits, TRUE is for 8 digits |
| `asset_to_usd_rate` | double precision | YES |  |  |

## Sample Data

| `bonus_history_id` | `trader_id` | `manager_delta` | `manager_bonus` | `ib_delta` | `ib_bonus` | `operation_type` | `description` | `external_note` | `create_timestamp` | `introducing_broker_id` | `is_precise_money` | `asset_to_usd_rate` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2178 | 24040 | 24040 | 0 | 0 | 0 | 1556369 |  | 2024-06-18 08:54:03.732000 | NULL | False | 1.0 |
| 2 | 2178 | -24040 | 0 | 0 | 0 | 1 | Bonus conversion | Bonus conversion | 2024-06-19 00:00:03.219000 | NULL | False | 1.0 |
| 3 | 3089 | 17416 | 17416 | 0 | 0 | 0 | 2108879 |  | 2025-04-25 11:07:05.505000 | NULL | False | 1.0 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
