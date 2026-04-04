# `swap_calculation_event`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `event_id` | bigint | NO |  |  |
| `position_id` | bigint | YES |  |  |
| `charged_swap` | bigint | YES |  |  |
| `current_swap` | bigint | YES |  |  |
| `create_timestamp` | timestamp without time zone | YES |  |  |
| `is_precise_money` | boolean | NO | false | FALSE is for 2 digits, TRUE is for 8 digits |

## Sample Data

| `event_id` | `position_id` | `charged_swap` | `current_swap` | `create_timestamp` | `is_precise_money` |
| --- | --- | --- | --- | --- | --- |
| 1 | 19 | 5 | 5 | 2023-08-18 20:59:00.093000 | False |
| 2 | 114 | -10 | -10 | 2023-11-20 20:59:00.120000 | False |
| 3 | 115 | -10 | -10 | 2023-11-20 20:59:00.121000 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
