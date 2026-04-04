# `deal_filled_2024`

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
| 2968 | 3841 | 100 | NULL | 1 | 136 | 2024-01-01 13:52:04.458000 | 105.46 | 2 | 1894 | 2 | 100 | 10546000 | 10546000 | 2024-01-01 13:52:04.677000 | NULL | 1 | True | 32 | 0 | [REDACTED] | 66 | 2749 | NULL | 10546000 | 0 | 0 | 0 | NULL | 0 | 0 | 100 | True | 21095 | False | NULL | 10546000 | 0 | 0 | NULL | False | NULL | 105.46 | 1554 | 9555 | 8283 | False |
| 2967 | 3839 | 100 | NULL | 2 | 136 | 2024-01-01 13:51:59.735000 | 105.49 | 2 | 1894 | 2 | 100 | 10549000 | 10549000 | 2024-01-01 13:52:00.001000 | NULL | 1 | True | 32 | 0 | [REDACTED] | 66 | 2748 | NULL | 10549000 | 0 | 0 | 0 | NULL | 0 | 0 | 100 | True | 10549 | False | NULL | 10549000 | 0 | 0 | NULL | False | NULL | 105.49 | 1554 | 9558 | 8285 | False |
| 59177 | 74150 | 30 | NULL | 2 | 109 | 2024-07-02 11:06:58.109000 | 39075.0 | 2 | 31336 | 2 | 30 | 3907449000 | 3907500000 | 2024-07-02 11:06:58.378000 | NULL | 1 | True | 9 | 0 | [REDACTED] | 66 | 53002 | NULL | 3907500000 | 0 | 0 | 0 | NULL | 0 | 15 | 1000 | True | 149251310 | False | NULL | 3907449000 | 0 | 0 | NULL | False | NULL | 39075.0 | 2323 | 1093894 | 926973 | False |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
