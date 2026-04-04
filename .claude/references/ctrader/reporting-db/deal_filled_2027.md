# `deal_filled_2027`

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

_No rows returned or table is empty._

## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
