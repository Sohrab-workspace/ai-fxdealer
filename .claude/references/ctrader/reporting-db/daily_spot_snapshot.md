# `daily_spot_snapshot`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `daily_timestamp` | timestamp without time zone | NO |  |  |
| `price` | bigint | NO |  |  |
| `side` | character | NO |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `symbol_id` | bigint | NO |  |  |

## Sample Data

| `daily_timestamp` | `price` | `side` | `create_timestamp` | `symbol_id` |
| --- | --- | --- | --- | --- |
| 2023-08-02 20:55:00.002000 | 109381 | A | 2023-08-02 20:54:52.451000 | 1 |
| 2023-08-02 20:55:00.002000 | 109378 | B | 2023-08-02 20:54:52.451000 | 1 |
| 2023-08-02 20:55:00.002000 | 127094 | A | 2023-08-02 20:54:59.256000 | 2 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
