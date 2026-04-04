# `action`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `action_id` | bigint | NO |  |  |
| `action_type` | integer | NO |  | CREATE_STOP_LOSS_TAKE_PROFIT(1), AMEND_STOP_LOSS_TAKE_PROFIT(2), CANCEL_STOP_LOSS_TAKE_PROFIT(3), CREATE_CLOSING_ORDER(4), CREATE_ORDER(5), CANCEL_PENDING_ORDER(6), AMEND_OPEN_PENDING_ORDER(7), CREATE_OCO_LINK(8), CANCEL_OCO_LINK(9) |
| `action_status` | integer | NO |  | PENDING(1), STARTED(2), PASSED(3), FAILED(4), ERROR(5) |
| `trade_order_id` | bigint | YES |  |  |
| `stop_loss` | bigint | YES |  |  |
| `take_profit` | bigint | YES |  |  |
| `expiration_timestamp` | timestamp without time zone | YES |  |  |
| `volume` | bigint | YES |  |  |
| `price` | bigint | YES |  |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO | timezone('UTC'::text, now()) |  |
| `client_request_id` | character varying | YES |  |  |
| `session_id` | character varying | YES |  |  |
| `slippage_in_points` | integer | YES |  |  |
| `relative_stop_loss` | bigint | YES |  |  |
| `relative_take_profit` | bigint | YES |  |  |
| `order_label` | character varying | YES |  |  |
| `order_channel` | character varying | YES |  |  |
| `order_comment` | character varying | YES |  |  |
| `execute_timestamp` | timestamp without time zone | YES |  |  |
| `position_id` | bigint | NO |  |  |
| `order_method` | character varying | YES |  |  |
| `stake` | bigint | YES |  |  |
| `guaranteed_stop_loss` | boolean | NO | false |  |
| `check_tolerance` | boolean | NO | false |  |
| `sent_by_dealer` | boolean | YES | false |  |
| `trailing_stop_loss` | boolean | YES |  |  |
| `tsl_distance` | bigint | YES |  |  |
| `stop_trigger_method` | integer | YES |  | stop_trigger_method IS 'TRADE(1), OPPOSITE(2), DOUBLE_TRADE(3), DOUBLE_OPPOSITE(4)' |
| `stop_loss_trigger_method` | integer | YES |  | stop_loss_trigger_method IS 'TRADE(1), OPPOSITE(2), DOUBLE_TRADE(3), DOUBLE_OPPOSITE(4)' |
| `desired_open_timestamp` | timestamp without time zone | YES |  | Desired time to execute MOO order |
| `oco_order_id` | bigint | YES |  |  |
| `authentication_id` | bigint | YES |  |  |
| `break_even_trigger_price_pips` | bigint | YES |  |  |
| `break_even_additional_distance_pips` | bigint | YES |  |  |

## Sample Data

| `action_id` | `action_type` | `action_status` | `trade_order_id` | `stop_loss` | `take_profit` | `expiration_timestamp` | `volume` | `price` | `utc_last_update_timestamp` | `client_request_id` | `session_id` | `slippage_in_points` | `relative_stop_loss` | `relative_take_profit` | `order_label` | `order_channel` | `order_comment` | `execute_timestamp` | `position_id` | `order_method` | `stake` | `guaranteed_stop_loss` | `check_tolerance` | `sent_by_dealer` | `trailing_stop_loss` | `tsl_distance` | `stop_trigger_method` | `stop_loss_trigger_method` | `desired_open_timestamp` | `oco_order_id` | `authentication_id` | `break_even_trigger_price_pips` | `break_even_additional_distance_pips` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 50247 | 2 | 3 | 22783 | NULL | 204200000 | NULL | NULL | NULL | [REDACTED] | ctm-4a98d276e2a540dbabbf2dc516378763 | NULL | NULL | NULL | NULL | NULL | cTrader 2 Android | NULL | 2024-02-29 15:18:12.474000 | 10388 | NULL | NULL | False | False | False | NULL | NULL | NULL | NULL | NULL | NULL | 89112 | NULL | NULL |
| 1 | 5 | 3 | 1 | NULL | NULL | NULL | 100000 | NULL | [REDACTED] | ctd-28ddfea9603548b08a812fd539f0a380 | NULL | NULL | NULL | NULL | NULL | cTrader | NULL | 2023-08-16 09:30:19.478000 | 1 | orderWindow#dark | NULL | False | False | False | NULL | NULL | NULL | NULL | NULL | NULL | 56130 | NULL | NULL |
| 2 | 1 | 3 | 2 | 109430 | 109130 | NULL | NULL | NULL | [REDACTED] | ctd-8f3bc43c0b6e4ba092d8c70c266831ad | NULL | NULL | NULL | NULL | NULL | cTrader | NULL | 2023-08-16 09:30:54.112000 | 1 | NULL | NULL | False | False | False | True | NULL | NULL | 1 | NULL | NULL | 56130 | NULL | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
