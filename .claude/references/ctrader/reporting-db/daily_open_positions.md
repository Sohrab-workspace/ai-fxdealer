# `daily_open_positions`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `trader_id` | bigint | NO |  |  |
| `position_id` | bigint | NO |  |  |
| `open_timestamp` | timestamp without time zone | NO |  |  |
| `report_timestamp` | timestamp without time zone | NO |  |  |
| `symbol_id` | bigint | NO |  |  |
| `stake` | bigint | YES |  |  |
| `volume` | bigint | YES |  |  |
| `lot_size` | bigint | NO |  |  |
| `trade_side` | integer | NO |  | BUY(1), SELL(2) |
| `vwap_price` | bigint | NO |  |  |
| `margin` | bigint | NO |  |  |
| `net_unrealized_pnl` | bigint | NO |  |  |
| `gross_unrealized_pnl` | bigint | NO |  |  |
| `quote_to_deposit_rate` | double precision | NO |  |  |
| `last_spot` | bigint | NO |  |  |
| `unrealized_swap` | bigint | NO | 0 |  |
| `is_precise_money` | boolean | NO | false | FALSE is for 2 digits, TRUE is for 8 digits |

## Sample Data

| `trader_id` | `position_id` | `open_timestamp` | `report_timestamp` | `symbol_id` | `stake` | `volume` | `lot_size` | `trade_side` | `vwap_price` | `margin` | `net_unrealized_pnl` | `gross_unrealized_pnl` | `quote_to_deposit_rate` | `last_spot` | `unrealized_swap` | `is_precise_money` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1022 | 19 | 2023-08-18 12:02:34.767000 | 2023-08-18 20:55:00.010000 | 5 | NULL | 100000 | 10000000 | 1 | 63901 | 128 | 137 | 137 | 1.0 | [REDACTED] | 0 | False |
| 1022 | 19 | 2023-08-18 12:02:34.767000 | 2023-08-19 20:55:00.001000 | 5 | NULL | 100000 | 10000000 | 1 | 63901 | 128 | 126 | 121 | 1.0 | [REDACTED] | 5 | False |
| 1022 | 19 | 2023-08-18 12:02:34.767000 | 2023-08-20 20:55:00.002000 | 5 | NULL | 100000 | 10000000 | 1 | 63901 | 128 | 100 | 95 | 1.0 | [REDACTED] | 5 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
