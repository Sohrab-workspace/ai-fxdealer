# `trade_order`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `trade_order_id` | bigint | NO |  |  |
| `position_id` | bigint | NO |  |  |
| `order_type` | integer | NO |  | MARKET(1), LIMIT(2), STOP(3), STOP_LOSS_TAKE_PROFIT(4), MARKET_RANGE(5), STOP_LIMIT(6) |
| `volume` | bigint | NO |  |  |
| `limit_price` | bigint | YES |  |  |
| `expiration_timestamp` | timestamp without time zone | YES |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `trade_side` | integer | NO |  | BUY(1), SELL(2) |
| `order_status` | integer | NO |  | ACCEPTED(1), FILLED(2), REJECTED(3), EXPIRED(4), CANCELLED(5), ERROR(6) |
| `close_timestamp` | timestamp without time zone | YES |  |  |
| `entry_price` | bigint | YES |  |  |
| `closing_order` | boolean | NO |  |  |
| `stop_price` | bigint | YES |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |
| `base_slippage_price` | bigint | YES |  |  |
| `slippage_in_points` | integer | YES |  |  |
| `order_label` | character varying | YES |  |  |
| `order_channel` | character varying | YES |  |  |
| `order_comment` | character varying | YES |  |  |
| `stop_loss` | bigint | YES |  |  |
| `take_profit` | bigint | YES |  |  |
| `relative_stop_loss` | bigint | YES |  |  |
| `relative_take_profit` | bigint | YES |  |  |
| `client_order_id` | character varying | YES |  |  |
| `time_in_force` | integer | NO |  | GOOD_TILL_DATE(1), GOOD_TILL_CANCEL(2), IMMEDIATE_OR_CANCEL(3), MARKET_ON_OPEN(5) |
| `symbol_id` | bigint | NO |  |  |
| `trader_id` | bigint | NO |  |  |
| `book_type` | integer | NO |  | BOOK_A(1), BOOK_B(2) |
| `mirroring_commission_rate` | numeric | NO | 0 |  |
| `measurement_units` | character varying | YES |  |  |
| `lot_size` | bigint | NO |  |  |
| `inner_mirroring_fee` | boolean | NO | true |  |
| `stake` | bigint | YES |  |  |
| `desired_vwap` | bigint | YES |  |  |
| `guaranteed_stop_loss` | boolean | NO | false |  |
| `check_tolerance` | boolean | NO | false |  |
| `is_stopout` | boolean | NO | false |  |
| `trailing_stop_loss` | boolean | YES |  |  |
| `tsl_distance` | bigint | YES |  |  |
| `close_with_pid` | bigint | YES |  |  |
| `stop_trigger_method` | integer | YES |  | TRADE(1), OPPOSITE(2), DOUBLE_TRADE(3), DOUBLE_OPPOSITE(4) |
| `stop_loss_trigger_method` | integer | YES |  | TRADE(1), OPPOSITE(2), DOUBLE_TRADE(3), DOUBLE_OPPOSITE(4) |
| `desired_open_timestamp` | timestamp without time zone | YES |  | Desired time to execute MOO order |
| `oco_order_id` | bigint | YES |  |  |
| `has_filled_volume` | boolean | YES |  |  |
| `additional_channel` | ARRAY | YES |  | CROSS_BROKER(1), SHARED_ACCOUNT_OWNER(2), IDEA_TRADE(3), SHARED_ACCOUNT_MANAGER(4),
        AC_RESERVED_2(5), AC_RESERVED_3(6), AC_RESERVED_4(7), AC_RESERVED_5(8), AC_RESERVED_6(9), AC_RESERVED_7(10), AC_RESERVED_8(11),
        AC_RESERVED_9(12), AC_RESERVED_10(13) |
| `session_id` | bigint | YES |  |  |
| `break_even_trigger_price_pips` | bigint | YES |  |  |
| `break_even_additional_distance_pips` | bigint | YES |  |  |

## Sample Data

| `trade_order_id` | `position_id` | `order_type` | `volume` | `limit_price` | `expiration_timestamp` | `create_timestamp` | `trade_side` | `order_status` | `close_timestamp` | `entry_price` | `closing_order` | `stop_price` | `utc_last_update_timestamp` | `base_slippage_price` | `slippage_in_points` | `order_label` | `order_channel` | `order_comment` | `stop_loss` | `take_profit` | `relative_stop_loss` | `relative_take_profit` | `client_order_id` | `time_in_force` | `symbol_id` | `trader_id` | `book_type` | `mirroring_commission_rate` | `measurement_units` | `lot_size` | `inner_mirroring_fee` | `stake` | `desired_vwap` | `guaranteed_stop_loss` | `check_tolerance` | `is_stopout` | `trailing_stop_loss` | `tsl_distance` | `close_with_pid` | `stop_trigger_method` | `stop_loss_trigger_method` | `desired_open_timestamp` | `oco_order_id` | `has_filled_volume` | `additional_channel` | `session_id` | `break_even_trigger_price_pips` | `break_even_additional_distance_pips` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 100000 | NULL | NULL | 2023-08-16 09:30:19.478000 | 2 | 2 | 2023-08-16 09:30:19.745000 | NULL | False | NULL | [REDACTED] | NULL | NULL | NULL | cTrader | NULL | NULL | NULL | NULL | NULL | ctd-28ddfea9603548b08a812fd539f0a380 | 3 | 1 | 1021 | 2 | 0 | EUR | 10000000 | True | NULL | 109280 | False | False | False | NULL | NULL | NULL | NULL | NULL | NULL | NULL | True | NULL | NULL | NULL | NULL |
| 24920 | 11323 | 1 | 200 | NULL | NULL | 2024-03-06 08:39:53.194000 | 1 | 2 | 2024-03-06 08:39:53.484000 | NULL | True | NULL | [REDACTED] | NULL | NULL | NULL | cTrader Copy | Strategy Provider: Wriggle | NULL | NULL | NULL | NULL | CH:04c6cbc2-2fc1-4738-9a97-15417a0b8da9 | 3 | 41 | 1648 | 2 | 0 | Oz | 10000 | False | NULL | NULL | False | False | False | NULL | NULL | NULL | NULL | NULL | NULL | NULL | True | NULL | 88634 | NULL | NULL |
| 2 | 1 | 4 | 100000 | 109130 | NULL | 2023-08-16 09:30:54.112000 | 1 | 2 | 2023-08-16 11:41:06.592000 | NULL | True | 109289 | [REDACTED] | NULL | NULL | NULL | cTrader | NULL | NULL | NULL | NULL | NULL | ctd-8f3bc43c0b6e4ba092d8c70c266831ad | 2 | 1 | 1021 | 2 | 0 | EUR | 10000000 | True | NULL | NULL | False | False | False | True | 153 | NULL | 1 | NULL | NULL | NULL | True | NULL | NULL | NULL | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
