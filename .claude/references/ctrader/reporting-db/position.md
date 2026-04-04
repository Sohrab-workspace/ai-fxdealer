# `position`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `position_id` | bigint | NO |  |  |
| `symbol_id` | bigint | NO |  |  |
| `close_timestamp` | timestamp without time zone | YES |  |  |
| `trader_id` | bigint | NO |  |  |
| `position_status` | integer | NO |  | CREATED(0), OPEN(1), CLOSED(2), ERROR(3) |
| `stop_loss` | bigint | YES |  |  |
| `take_profit` | bigint | YES |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |
| `book_type` | integer | NO |  | BOOK_A(1), BOOK_B(2) |
| `open_timestamp` | timestamp without time zone | YES |  |  |
| `spread_betting` | boolean | NO | false |  |
| `guaranteed_stop_loss` | boolean | NO | false |  |
| `trailing_stop_loss` | boolean | YES |  |  |
| `buy_margin` | bigint | YES | 0 |  |
| `sell_margin` | bigint | YES | 0 |  |
| `rollover_commission_paid_timestamp` | timestamp without time zone | YES |  | Timestamp when last comission payed |
| `is_precise_money` | boolean | NO | false | FALSE is for 2 digits, TRUE is for 8 digits |
| `create_trade_order_id` | bigint | YES |  |  |
| `break_even_trigger_price_pips` | bigint | YES |  |  |
| `break_even_additional_distance_pips` | bigint | YES |  |  |

## Sample Data

| `position_id` | `symbol_id` | `close_timestamp` | `trader_id` | `position_status` | `stop_loss` | `take_profit` | `utc_last_update_timestamp` | `book_type` | `open_timestamp` | `spread_betting` | `guaranteed_stop_loss` | `trailing_stop_loss` | `buy_margin` | `sell_margin` | `rollover_commission_paid_timestamp` | `is_precise_money` | `create_trade_order_id` | `break_even_trigger_price_pips` | `break_even_additional_distance_pips` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 2023-08-16 11:41:06.592000 | 1021 | 2 | NULL | NULL | [REDACTED] | 2 | 2023-08-16 09:30:19.745000 | False | False | True | 0 | 0 | NULL | False | 1 | NULL | NULL |
| 2 | 1 | 2023-08-18 11:36:40.607000 | 1022 | 2 | NULL | NULL | [REDACTED] | 2 | NULL | False | False | NULL | 0 | 0 | NULL | False | 3 | NULL | NULL |
| 3 | 1 | 2023-08-18 11:37:38.955000 | 1022 | 2 | NULL | NULL | [REDACTED] | 2 | 2023-08-18 11:37:10.813000 | False | False | NULL | 0 | 0 | NULL | False | 4 | NULL | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
