# `price_stream_history`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `price_stream_id` | bigint | NO |  |  |
| `symbol_id` | bigint | NO |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `bid_markup` | integer | NO |  |  |
| `ask_markup` | integer | NO |  |  |
| `markup_is_relative` | boolean | NO | false |  |

## Sample Data

| `price_stream_id` | `symbol_id` | `create_timestamp` | `bid_markup` | `ask_markup` | `markup_is_relative` |
| --- | --- | --- | --- | --- | --- |
| 2 | 1 | 2023-08-18 08:58:20.191000 | 7 | 7 | False |
| 2 | 2 | 2023-08-18 08:58:20.191000 | 8 | 8 | False |
| 2 | 3 | 2023-08-18 08:58:20.191000 | 1100 | 1100 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
