# `price_stream_symbol`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `price_stream_id` | bigint | NO |  |  |
| `symbol_id` | bigint | NO |  |  |
| `bid_markup` | integer | NO | 0 |  |
| `ask_markup` | integer | NO | 0 |  |
| `markup_is_relative` | boolean | NO | false |  |

## Sample Data

| `price_stream_id` | `symbol_id` | `bid_markup` | `ask_markup` | `markup_is_relative` |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | False |
| 1 | 2 | 1 | 1 | False |
| 1 | 3 | 100 | 100 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
