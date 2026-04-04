# `manager_permission`

## Description

> _Auto-captured from ctrader_spotware reporting DB (Demo environment)._

## Fields

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| `manager_id` | bigint | NO |  |  |
| `permission` | character varying | NO |  |  |

## Sample Data

| `manager_id` | `permission` |
| --- | --- |
| 1000 | ROLE_ASSET_CLASS_EDIT |
| 1000 | ROLE_DEALING |
| 1000 | ROLE_PROFILES_EDIT |


## Notes

- Source: cTrader Reporting DB (`ctrader_spotware`)
- Access: read-only replica via stunnel → dbapi.ctrader.com:15220
- PII fields redacted with `[REDACTED]`
