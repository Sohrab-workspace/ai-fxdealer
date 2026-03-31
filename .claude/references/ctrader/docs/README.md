# Spotware Documentation — Scraped Reference

> Scraped from [docs.spotware.com](https://docs.spotware.com) on 2026-03-31.
> All sections captured in full — tables, code samples, field definitions, error codes.

## Files

| File | Section | Pages | Size |
|------|---------|-------|------|
| [01-manager-api.md](01-manager-api.md) | Manager's API | 5 | 22 KB |
| [02-reporting-api.md](02-reporting-api.md) | Reporting API | 5 | 14 KB |
| [03-webservices-api.md](03-webservices-api.md) | WebServices API | 11 | 171 KB |
| [04-broker-sso-oauth.md](04-broker-sso-oauth.md) | Broker SSO (OAuth) | 13 | 88 KB |
| [05-ctrader-copy.md](05-ctrader-copy.md) | cTrader Copy | 7 | 27 KB |
| [06-repo-db.md](06-repo-db.md) | Repo DB | 3 | 9 KB |
| [07-deeplinks.md](07-deeplinks.md) | Deeplinks | 5 | 12 KB |
| [08-tradingview-integration.md](08-tradingview-integration.md) | TradingView Integration | 3 | 17 KB |
| [09-ctrader-invite.md](09-ctrader-invite.md) | cTrader Invite | 4 | 19 KB |

## Section Summaries

### Manager's API
Protobuf over TCP on port 5011. Covers CRUD operations, trading/pricing actions, list endpoints.
Live-captured responses in [`../manager-api/`](../manager-api/).

### Reporting API
RabbitMQ-based real-time event feed + HTTP snapshot endpoint.
Protobuf-encoded. Covers connection setup, event types, snapshot requests.

### WebServices API
REST API for CRM/trader-room integrations. Account creation, deposits/withdrawals,
cTID operations. Includes full JSON schemas and country list.

### Broker SSO (OAuth)
OAuth 2.0 SSO between broker's client area and cTrader. Covers all flows:
embedded web, user creation, API calls to backend, conformance testing.

### cTrader Copy
Social trading / copy-trading integration. Plant mode, WL isolation, API calls.

### Repo DB
PostgreSQL read-only reporting replica via stunnel. Schema, connection details,
example queries. Live schema capture in [`../reporting-db/`](../reporting-db/).

### Deeplinks
Universal and mobile-only deeplinks for sending users into specific cTrader screens.

### TradingView Integration
Token-based TradingView ↔ cTrader connection. Requirements and auth flow.

### cTrader Invite
Partner/referral programme integration. Invite links, stats API, glossary.
