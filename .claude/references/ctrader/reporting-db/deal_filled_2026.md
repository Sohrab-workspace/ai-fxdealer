# `deal_filled_2026`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `deal_id` | bigint | NO |  |  |
| `trade_order_id` | bigint | NO |  |  |
| `volume` | bigint | NO |  |  |
| `limit_price` | bigint | YES |  |  |
| `trade_side` | integer | NO |  |  |
| `symbol_id` | integer | NO |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `margin_rate` | double precision | NO |  |  |
| `book_type` | integer | NO |  |  |
| `position_id` | bigint | NO |  |  |
| `deal_status` | integer | NO |  |  |
| `filled_volume` | bigint | NO |  |  |
| `execution_price` | bigint | YES |  |  |
| `lp_execution_price` | bigint | YES |  |  |
| `execution_timestamp` | timestamp without time zone | NO |  |  |
| `lp_order_id` | character varying | YES |  |  |
| `deal_type` | integer | NO |  |  |
| `offsetted` | boolean | NO | false |  |
| `commission` | bigint | NO | 0 |  |
| `unrealized_swap` | bigint | NO | 0 |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO |  |  |
| `liquidity_feed_id` | bigint | YES |  |  |
| `price_snapshot_id` | bigint | YES |  |  |
| `server_order_id` | character varying | YES |  |  |
| `symbol_markup_execution_price` | bigint | YES |  |  |
| `ib_commission` | bigint | NO | 0 |  |
| `pocket_commission` | bigint | NO | 0 |  |
| `pocket_markup` | bigint | NO | 0 |  |
| `parent_ib_id` | bigint | YES |  |  |
| `mirroring_commission` | bigint | NO | 0 |  |
| `markup` | bigint | NO | 0 |  |
| `lot_size` | bigint | NO |  |  |
| `inner_mirroring_fee` | boolean | NO | true |  |
| `total_volume_in_usd` | bigint | NO | 0 |  |
| `split_revenue` | boolean | NO | false |  |
| `stake` | bigint | YES |  |  |
| `desired_vwap` | bigint | NO | 0 |  |
| `market_vwap` | bigint | NO | 0 |  |
| `tolerance` | integer | NO | 0 |  |
| `reject_reason` | character varying | YES |  |  |
| `manual` | boolean | NO | false |  |
| `spot_price` | bigint | YES |  |  |
| `base_to_usd_conversion_rate` | double precision | NO | (0)::double precision |  |
| `trader_id` | bigint | YES |  |  |
| `filled_eur_volume` | bigint | YES |  |  |
| `filled_gbp_volume` | bigint | YES |  |  |
| `is_precise_money` | boolean | NO | false |  |

## Sample Data

| `deal_id` | `trade_order_id` | `volume` | `limit_price` | `trade_side` | `symbol_id` | `create_timestamp` | `margin_rate` | `book_type` | `position_id` | `deal_status` | `filled_volume` | `execution_price` | `lp_execution_price` | `execution_timestamp` | `lp_order_id` | `deal_type` | `offsetted` | `commission` | `unrealized_swap` | `utc_last_update_timestamp` | `liquidity_feed_id` | `price_snapshot_id` | `server_order_id` | `symbol_markup_execution_price` | `ib_commission` | `pocket_commission` | `pocket_markup` | `parent_ib_id` | `mirroring_commission` | `markup` | `lot_size` | `inner_mirroring_fee` | `total_volume_in_usd` | `split_revenue` | `stake` | `desired_vwap` | `market_vwap` | `tolerance` | `reject_reason` | `manual` | `spot_price` | `base_to_usd_conversion_rate` | `trader_id` | `filled_eur_volume` | `filled_gbp_volume` | `is_precise_money` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 271602 | 338447 | 20 | NULL | 1 | 696 | 2026-01-01 00:06:37.961000 | 516.83 | 2 | 700954 | 2 | 20 | 51683000 | 51683000 | 2026-01-01 00:06:38.185000 | NULL | 1 | True | 31 | 0 | [REDACTED] | 66 | 254070 | NULL | 51683000 | 0 | 0 | 0 | NULL | 0 | 0 | 100 | True | 20543 | False | NULL | 0 | 0 | 0 | NULL | False | NULL | 516.83 | 5877 | 8800 | 7671 | False |
| 271603 | 338360 | 200000 | NULL | 2 | 559 | 2026-01-01 22:04:06.268000 | 1.17416 | 2 | 700918 | 2 | 200000 | 117416 | 117419 | 2026-01-01 22:04:06.512000 | NULL | 1 | True | 6 | 0 | [REDACTED] | 66 | 254071 | NULL | 117416 | 0 | 0 | 0 | NULL | 0 | 6 | 10000000 | False | 398555316 | False | NULL | 117429 | 0 | 0 | NULL | False | NULL | 1.17416 | 4422 | 199650 | 174362 | False |
| 271605 | 338443 | 200 | 433055000 | 2 | 547 | 2026-01-01 23:00:55.025000 | 4332.08 | 2 | 700952 | 2 | 200 | 433198000 | 433202000 | 2026-01-01 23:00:55.227000 | NULL | 2 | True | 6 | 0 | [REDACTED] | 66 | 254073 | NULL | 433198000 | 0 | 0 | 0 | NULL | 0 | 8 | 10000 | False | 2423758715 | False | NULL | 0 | 0 | 0 | NULL | False | NULL | 4332.08 | 5277 | 737272 | 642678 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
