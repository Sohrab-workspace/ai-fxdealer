# `authentication`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `id` | bigint | NO |  |  |
| `create_timestamp` | timestamp without time zone | NO |  |  |
| `login` | bigint | NO |  |  |
| `proxy_id` | character varying | NO |  |  |
| `ip_address` | inet | YES |  |  |
| `product_id` | character varying | NO |  |  |
| `application_type` | character varying | YES |  |  |
| `error_code` | integer | YES |  | SUCCESS(NULL), ERROR(2), INVALID_DATA(3), NO_CONNECT(6), NOT_ENOUGH_RIGHTS(7), NO_SUCH_LOGIN(12), ACCOUNT_DISABLED(64), BAD_ACCOUNT_INFO(65), TOKEN_REVOKED(160), TOKEN_EXPIRED(161) |
| `machine_id` | character varying | YES |  |  |
| `mac_address` | macaddr8 | YES |  |  |

## Sample Data

| `id` | `create_timestamp` | `login` | `proxy_id` | `ip_address` | `product_id` | `application_type` | `error_code` | `machine_id` | `mac_address` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 2023-07-20 10:30:40.624000 | [REDACTED] | proxy-a12.ext.p.spotwa.re | [REDACTED] |  | CRAWLER | NULL | NULL | NULL |
| 5 | 2023-07-20 10:30:40.703000 | [REDACTED] | proxy-a12.ext.p.spotwa.re | [REDACTED] |  | CRAWLER | NULL | NULL | NULL |
| 8 | 2023-07-20 10:30:43.630000 | [REDACTED] | proxy-a4.ext.p.spotwa.re | [REDACTED] |  | CRAWLER | NULL | NULL | NULL |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
