# `liquidity_feed_symbol`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `liquidity_feed_id` | bigint | NO |  |  |
| `symbol_id` | bigint | NO |  |  |
| `send_lots` | boolean | NO | false | IF TRUE THEN volume is converted to lots using lp_lot_size. Valid only for PrimeXM (spec. logic), GFT (spec. logic) SmartTrade, FXEdge, ACM, ICM, OneZero (default logic) |
| `product` | integer | YES |  | CURRENCY(4), INDEX(7), OTHER(12) use only for Bitmex volume/price |
| `deal_expiration_timeout` | bigint | NO | 15000 | timeout after which a deal without response is considered as missed deal |
| `no_quote_timeout` | bigint | NO | 120000 | timeout after which. Used for monitoring |
| `data` | text | YES |  |  symbol alias for price data requests |
| `trade_data` | text | YES |  | symbol alias for trading requests |
| `lp_lot_size` | bigint | YES |  | In cents by default, but can be dependent on specific adapter logic. Formula might differ depending on adapter. value_units = volume_cents/lp_lot_size_cents |
| `liquidity_feed_symbol_id` | bigint | NO |  |  |

## Sample Data

| `liquidity_feed_id` | `symbol_id` | `send_lots` | `product` | `deal_expiration_timeout` | `no_quote_timeout` | `data` | `trade_data` | `lp_lot_size` | `liquidity_feed_symbol_id` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 66 | 1 | False | NULL | 15000 | 120000 | EURUSD | EURUSD | NULL | 104 |
| 66 | 43 | False | NULL | 15000 | 120000 | USDTRY | USDTRY | NULL | 105 |
| 66 | 44 | False | NULL | 15000 | 120000 | EURTRY | EURTRY | NULL | 106 |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
