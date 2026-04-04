# `balance_history_default`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `balance_history_id` | bigint | NO |  |  |
| `trader_id` | bigint | NO |  |  |
| `delta` | bigint | NO |  |  |
| `balance` | bigint | NO |  |  |
| `operation_type` | integer | NO |  |  |
| `description` | character varying | YES |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `utc_last_update_datetime` | timestamp without time zone | NO | timezone('utc'::text, now()) |  |
| `external_note` | character varying | YES |  |  |
| `balance_version` | bigint | NO |  |  |
| `equity` | bigint | NO | 0 |  |
| `min_equity` | bigint | NO | 0 |  |
| `max_equity` | bigint | NO | 0 |  |
| `nonwithdrawable_bonus` | bigint | NO | 0 |  |
| `source` | character varying | YES |  |  |
| `external_id` | character varying | YES |  |  |
| `is_precise_money` | boolean | NO | false |  |
| `asset_to_usd_rate` | double precision | YES |  |  |

## Sample Data

| `balance_history_id` | `trader_id` | `delta` | `balance` | `operation_type` | `description` | `create_timestamp` | `utc_last_update_datetime` | `external_note` | `balance_version` | `equity` | `min_equity` | `max_equity` | `nonwithdrawable_bonus` | `source` | `external_id` | `is_precise_money` | `asset_to_usd_rate` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1021 | 100000 | 100000 | 0 |  | 2023-08-14 10:27:04.756000 | [REDACTED] |  | 2 | 100000 | 0 | 100000 | 0 | NULL | NULL | False | 1.0 |
| 3 | 1022 | 1000000 | 1000000 | 0 |  | 2023-08-18 11:36:57.061000 | [REDACTED] |  | 2 | 1000000 | 0 | 1000000 | 0 | NULL | NULL | False | 1.0 |
| 11 | 1022 | 10000000 | 10996019 | 0 |  | 2023-08-18 11:49:23.652000 | [REDACTED] |  | 10 | 10996019 | 996019 | 10996019 | 0 | NULL | NULL | False | 1.0 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
