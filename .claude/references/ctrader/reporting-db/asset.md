# `asset`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `asset_id` | bigint | NO |  |  |
| `name` | character varying | NO |  |  |
| `is_deposit_asset` | boolean | NO |  |  |
| `is_depositable` | boolean | NO |  |  |
| `digits` | integer | NO | 2 | Allowed (0, 1, 2, 3, 4, 5, 6, 7, 8) digits |
| `description` | character varying | NO |  |  |
| `type` | integer | NO |  | FOREX(1), METALS(2), INDICES(3), COMMODITY(4), STOCK(5), CRYPTO(6), OTHER(7) |
| `display_name` | character varying | NO |  |  |
| `major` | boolean | NO | false |  |
| `calendar_alias` | character varying | YES |  |  |
| `allowed_initial_balances` | ARRAY | YES |  |  |
| `cn_app_allowed` | boolean | NO | true |  |
| `utc_last_update_timestamp` | timestamp without time zone | NO | timezone('UTC'::text, now()) |  |

## Sample Data

| `asset_id` | `name` | `is_deposit_asset` | `is_depositable` | `digits` | `description` | `type` | `display_name` | `major` | `calendar_alias` | `allowed_initial_balances` | `cn_app_allowed` | `utc_last_update_timestamp` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | [REDACTED] | False | True | 2 | NOK | 1 | [REDACTED] | False | NULL | NULL | True | [REDACTED] |
| 11 | [REDACTED] | False | True | 2 | NZD | 1 | [REDACTED] | False | NULL | NULL | True | [REDACTED] |
| 12 | [REDACTED] | False | True | 2 | PLN | 1 | [REDACTED] | False | NULL | NULL | True | [REDACTED] |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
