# `execution_profile`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `execution_profile_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `min_book_b_delay` | integer | NO | 200 |  |
| `max_book_b_delay` | integer | NO | 300 |  |
| `execution_policy` | integer | NO |  | BOOK_A(1), BOOK_B(2), BOOK_A_WITH_CONDITION(3) |
| `gsl_execution_policy` | integer | NO |  | DISABLED(0), ENABLED_DECLINE_IF_A_BOOK(1), ENABLED_FORCE_B_BOOK(2), ENABLED_EXECUTE_INTO_SYMBOL_BOOK(3) |
| `utc_last_update_timestamp` | timestamp without time zone | YES |  |  |
| `condition_volume_usd` | bigint | YES |  |  |
| `deleted` | boolean | NO | false |  |
| `scalping_delay_seconds` | integer | NO | 0 |  |

## Sample Data

| `execution_profile_id` | `name` | `description` | `min_book_b_delay` | `max_book_b_delay` | `execution_policy` | `gsl_execution_policy` | `utc_last_update_timestamp` | `condition_volume_usd` | `deleted` | `scalping_delay_seconds` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | [REDACTED] |  | 200 | 300 | 2 | 0 | [REDACTED] | NULL | False | 0 |
| 2 | [REDACTED] | NULL | 200 | 300 | 1 | 0 | [REDACTED] | NULL | False | 0 |
| 3 | [REDACTED] | NULL | 200 | 300 | 3 | 0 | [REDACTED] | 5000 | False | 0 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
