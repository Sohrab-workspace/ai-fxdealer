# `balance_history_trading`

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
| 2 | 1021 | 152 | 100152 | 2 | positionEntity id 1 | 2023-08-16 11:41:06.668000 | [REDACTED] | NULL | 3 | 100152 | 99972 | 100152 | 0 | NULL | NULL | False | 1.0 |
| 4 | 1022 | -5 | 999995 | 2 | positionEntity id 3 | 2023-08-18 11:37:38.980000 | [REDACTED] | NULL | 3 | 999995 | 999989 | 1000000 | 0 | NULL | NULL | False | 1.0 |
| 5 | 1022 | -7 | 999988 | 2 | positionEntity id 4 | 2023-08-18 11:38:34.037000 | [REDACTED] | NULL | 4 | 999988 | 999986 | 999995 | 0 | NULL | NULL | False | 1.0 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
