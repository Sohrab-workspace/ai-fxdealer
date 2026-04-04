# `price_stream`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `price_stream_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `description` | character varying | YES |  |  |
| `deleted` | boolean | NO |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |

## Sample Data

| `price_stream_id` | `name` | `description` | `deleted` | `utc_last_update_timestamp` |
| --- | --- | --- | --- | --- |
| 3 | [REDACTED] | (#) hashtag | False | [REDACTED] |
| 2 | [REDACTED] | (!) exclamation | False | [REDACTED] |
| 4 | [REDACTED] | (.) dot | False | [REDACTED] |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
