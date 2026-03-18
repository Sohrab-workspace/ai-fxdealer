---
name: mt5-integration
description: MT5 Manager API integration for AI FXDealer collector service.
  Use when building or modifying the MT5 collector, connecting to MT5 server,
  fetching MT5 entities (deals, orders, positions, accounts, users, symbols,
  groups, ticks, server logs, balance operations, margin events, online sessions),
  implementing MT5Manager Python methods, handling MT5 connection or return codes,
  designing raw_mt5_* database schemas, or writing any code that interacts with
  a MetaTrader 5 server via the Manager API.
allowed-tools: [Read, Write, Edit, Bash, Grep]
---

# MT5 Integration Skill

## Critical context — read this first

AI FXDealer uses the **MT5Manager pip package** (official MetaQuotes Python SDK)
to connect to MT5 servers as a manager — NOT as a trading account.

Install: `pip install MT5Manager`
PyPI: https://pypi.org/project/mt5manager/
Official Python docs: .claude/references/mql5/API/managerapi_python.md

This is a collector service. Its only job:
1. Connect to MT5 server with manager credentials
2. Fetch raw entity data exactly as returned
3. Store in raw_mt5_* tables with payload_json preserved
4. Never transform, normalize, or interpret data in the collector

Runs on a **Windows EC2 instance** — MT5Manager is Windows-only (win_amd64 wheel).
One collector instance per broker per MT5 server.

---

## ⚠️ Sections to IGNORE in the docs

These folders are for end-users and MQL5 scripting — NOT for your collector:
```
.claude/references/mql5/client/        ← trading terminal user guide
.claude/references/mql5/android/       ← mobile app
.claude/references/mql5/iphone/        ← mobile app
.claude/references/mql5/metaeditor/    ← IDE for MQL5 scripting
.claude/references/mql5/platform/      ← server admin/installation
.claude/references/mql5/manager/       ← manager desktop application UI
.claude/references/mql5/Administrator/ ← administrator desktop UI
.claude/references/mql5/Gateway/       ← gateway component
.claude/references/mql5/WebAPI/        ← web API (not what we use)
```

**Only read from `.claude/references/mql5/API/`**

---

## Documentation map — what to read for each task

### Connection

| Task | File |
|---|---|
| How to connect (Python) | .claude/references/mql5/API/managerapi_python.md |
| Manager API overview | .claude/references/mql5/API/ManagerAPI.md |
| Manager API purpose | .claude/references/mql5/API/managerapi_purpose.md |
| Getting started | .claude/references/mql5/API/getting_started.md |
| Best practices | .claude/references/mql5/API/managerapi_best_practice.md |
| Factory / create manager | .claude/references/mql5/API/managerapi_exported.md |
| mtManagerCreate / mtManagerVersion | .claude/references/mql5/API/managerapi_exported/mtmanagercreate.md |
| IMTManagerAPI connect method | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_connect.md |
| Pump modes (subscribe to events) | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_enpumpmodes.md |

### Users / Accounts

| Task | File |
|---|---|
| IMTManagerAPI user methods overview | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_user.md |
| UserGet (fetch single user) | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userget.md |
| UserRequest (bulk/history) | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userrequest.md |
| UserSubscribe (real-time) | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usersubscribe.md |
| IMTUser object fields | .claude/references/mql5/API/reference_user/imtuser.md |
| IMTUser field details | .claude/references/mql5/API/reference_user/imtuser/ ← all files |
| Account balance/margin fields | .claude/references/mql5/API/reference_trading/user_account/imtaccount.md |

### Deals

| Task | File |
|---|---|
| IMTManagerAPI deal methods | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal.md |
| IMTDeal object fields | .claude/references/mql5/API/reference_trading/trading_deal/imtdeal.md |
| IMTDeal enums | .claude/references/mql5/API/reference_trading/trading_deal/imtdeal/imtdeal_enum.md |
| IMTDeal comment | .claude/references/mql5/API/reference_trading/trading_deal/imtdeal/imtdeal_comment.md |
| Deal sink (real-time events) | .claude/references/mql5/API/reference_trading/trading_deal/imtdealsink.md |
| Deal array operations | .claude/references/mql5/API/reference_trading/trading_deal/imtdealarray.md |

### Orders

| Task | File |
|---|---|
| IMTManagerAPI order methods | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_order.md |
| IMTOrder object fields | .claude/references/mql5/API/reference_trading/trading_order/imtorder.md |
| IMTOrder enums | .claude/references/mql5/API/reference_trading/trading_order/imtorder/imtorder_enum.md |
| IMTOrder key fields | .claude/references/mql5/API/reference_trading/trading_order/imtorder/ ← all files |
| Order sink (real-time) | .claude/references/mql5/API/reference_trading/trading_order/imtordersink.md |
| History sink (closed orders) | .claude/references/mql5/API/reference_trading/trading_order/imthistorysink.md |

### Positions

| Task | File |
|---|---|
| IMTManagerAPI position methods | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position.md |
| IMTPosition object fields | .claude/references/mql5/API/reference_trading/trading_position/imtposition.md |
| IMTPosition key fields | .claude/references/mql5/API/reference_trading/trading_position/imtposition/ ← all files |
| Position sink (real-time) | .claude/references/mql5/API/reference_trading/trading_position/imtpositionsink.md |

### Ticks

| Task | File |
|---|---|
| IMTManagerAPI tick methods | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_tick.md |
| TickHistoryRequest | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickhistoryrequest.md |
| TickLast (latest tick) | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_ticklast.md |
| TickStat | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_tick/imtmanagerapi_tickstat.md |
| MTTick object | .claude/references/mql5/API/mttick.md |
| MTTickShort object | .claude/references/mql5/API/mttickshort.md |
| MTTickStat object | .claude/references/mql5/API/mttickstat.md |
| Tick sink (real-time subscribe) | .claude/references/mql5/API/reference_ticks/imtticksink.md |

### Symbols

| Task | File |
|---|---|
| IMTConSymbol fields | .claude/references/mql5/API/config_symbol/imtconsymbol.md |
| Symbol enums | .claude/references/mql5/API/config_symbol/imtconsymbol/imtconsymbol_enum.md |
| Symbol field details | .claude/references/mql5/API/config_symbol/imtconsymbol/ ← all files |
| Symbol sink (config changes) | .claude/references/mql5/API/config_symbol/imtconsymbolsink.md |
| IMTManagerAPI config symbols | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_config/imtmanagerapi_config_symbol/ |

### Groups

| Task | File |
|---|---|
| IMTConGroup fields | .claude/references/mql5/API/config_group/imtcongroup.md |
| Group enums | .claude/references/mql5/API/config_group/imtcongroup/imtcongroup_enum.md |
| Group field details | .claude/references/mql5/API/config_group/imtcongroup/ ← all files |
| Group sink | .claude/references/mql5/API/config_group/imtcongroupsink.md |
| IMTManagerAPI config groups | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_config/imtmanagerapi_config_group/ |

### Online sessions (login activity)

| Task | File |
|---|---|
| IMTManagerAPI online methods | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_online.md |
| IMTOnline object | .claude/references/mql5/API/reference_online/imtonline.md |
| Online array | .claude/references/mql5/API/reference_online/imtonlinearray.md |

### Exposure / margin

| Task | File |
|---|---|
| IMTManagerAPI exposure | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_exposure.md |
| IMTExposure object | .claude/references/mql5/API/reference_trading/trading_exposure/imtexposure.md |
| Exposure sink | .claude/references/mql5/API/reference_trading/trading_exposure/imtexposuresink.md |

### Summary / daily stats

| Task | File |
|---|---|
| IMTManagerAPI summary | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_summary.md |
| IMTManagerAPI daily | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_daily.md |
| IMTSummary object | .claude/references/mql5/API/reference_trading/trading_summary/imtsummary.md |
| IMTDaily object | .claude/references/mql5/API/reference_trading/trading_daily/imtdaily.md |

### Return codes / error handling

| Task | File |
|---|---|
| Common return codes | .claude/references/mql5/API/retcodes_common.md |
| Successful codes | .claude/references/mql5/API/retcodes_successful.md |
| Trade return codes | .claude/references/mql5/API/retcodes_trades.md |
| Trade request codes | .claude/references/mql5/API/retcodes_trade_request.md |
| Authentication codes | .claude/references/mql5/API/retcodes_authentication.md |
| Config codes | .claude/references/mql5/API/retcodes_configs.md |
| All return code categories | .claude/references/mql5/API/reference_retcodes.md |

### Sink / event subscription (real-time data)

| Task | File |
|---|---|
| Manager sink overview | .claude/references/mql5/API/imtmanagersink.md |
| onConnect / onDisconnect | .claude/references/mql5/API/imtmanagersink/imtmanagersink_onconnect.md |
| Deal sink | .claude/references/mql5/API/reference_trading/trading_deal/imtdealsink.md |
| Order sink | .claude/references/mql5/API/reference_trading/trading_order/imtordersink.md |
| Position sink | .claude/references/mql5/API/reference_trading/trading_position/imtpositionsink.md |
| Tick sink | .claude/references/mql5/API/reference_ticks/imtticksink.md |
| User sink | .claude/references/mql5/API/reference_user/imtusersink.md |

### IP / Geo data (for IP matching rules)

| Task | File |
|---|---|
| Geo resolution (batch) | .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_geo.md |
| IMTGeo object fields | .claude/references/mql5/API/reference_geo/imtgeo.md |
| IMTGeo field details | .claude/references/mql5/API/reference_geo/imtgeo/ ← all files |

### Examples

| Task | File |
|---|---|
| Python implementation examples | .claude/references/mql5/API/managerapi_examples.md |
| Python setup | .claude/references/mql5/API/managerapi_python.md |
| Best practice guide | .claude/references/mql5/API/managerapi_best_practice.md |

---

## Entities to collect and their raw tables

| Entity | Raw table | Sync mode | Key doc |
|---|---|---|---|
| Users / Accounts | raw_mt5_accounts | Bootstrap + incremental | imtmanagerapi_user.md |
| Deals | raw_mt5_deals | Bootstrap + incremental (timestamp cursor) | imtmanagerapi_trading_deal.md |
| Orders (open) | raw_mt5_orders | Bootstrap + incremental | imtmanagerapi_trading_order.md |
| Positions | raw_mt5_positions | Incremental snapshot | imtmanagerapi_trading_position.md |
| Symbols | raw_mt5_symbols | Bootstrap + daily refresh | config_symbol/imtconsymbol.md |
| Groups | raw_mt5_groups | Bootstrap + daily refresh | config_group/imtcongroup.md |
| Ticks | raw_mt5_ticks | Incremental real-time | imtmanagerapi_tick.md |
| Server logs | raw_mt5_server_logs | Incremental | imtmanagerapi_common.md |
| Online sessions | raw_mt5_server_logs | Incremental | imtmanagerapi_online.md |
| Summary / daily | raw_mt5_server_logs | Daily | imtmanagerapi_summary.md |

---

## Raw schema design rule

**Do not design raw_mt5_* schemas without first reading the actual object field docs.**

Process:
```
1. Connect to MT5 test server using MT5Manager
2. Call the relevant fetch method
3. Print ALL fields returned on a real response
4. Save sample payload to tests/fixtures/mt5/{entity}.json
5. Design table columns from REAL returned fields
6. Always keep payload_json with full raw response
```

Read these before designing each table:
- raw_mt5_deals → first read: `.claude/references/mql5/API/reference_trading/trading_deal/imtdeal.md`
- raw_mt5_orders → first read: `.claude/references/mql5/API/reference_trading/trading_order/imtorder.md`
- raw_mt5_positions → first read: `.claude/references/mql5/API/reference_trading/trading_position/imtposition.md`
- raw_mt5_accounts → first read: `.claude/references/mql5/API/reference_user/imtuser.md`
- raw_mt5_symbols → first read: `.claude/references/mql5/API/config_symbol/imtconsymbol.md`
- raw_mt5_groups → first read: `.claude/references/mql5/API/config_group/imtcongroup.md`
- raw_mt5_ticks → first read: `.claude/references/mql5/API/mttick.md`

---

## BaseCollector implementation pattern

```python
import MT5Manager
import structlog
from packages.shared.base_collector import BaseCollector

log = structlog.get_logger()

class MT5Collector(BaseCollector):

    def __init__(self, broker_id, server_id, connection_id,
                 host, login, password):
        self.broker_id = broker_id
        self.server_id = server_id
        self.connection_id = connection_id
        self.host = host
        self.login = login
        self.password = password
        self.manager = None
        self.status = "disconnected"
        self.cursor = None
        self.last_success_at = None

    def connect(self) -> None:
        # Read before implementing:
        # .claude/references/mql5/API/managerapi_python.md
        # .claude/references/mql5/API/managerapi_exported/mtmanagercreate.md
        # .claude/references/mql5/API/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_connect.md
        self.manager = MT5Manager.ManagerAPI()
        result = self.manager.Connect(self.host, self.login, self.password)
        if result != MT5Manager.MTRetCode.MT_RET_OK:
            raise ConnectionError(f"MT5 connect failed: {result}")
        self.status = "connected"
        log.info("mt5.connected",
            broker_id=str(self.broker_id),
            server_id=str(self.server_id),
            host=self.host)
```

---

## Error handling

Retry policy:
```
Attempt 1: immediate
Attempt 2: wait 5 seconds
Attempt 3: wait 30 seconds
After 3 failures: circuit_open, alert Sentry, stop for 10 minutes
```

Return code reference files:
```
.claude/references/mql5/API/retcodes_common.md
.claude/references/mql5/API/retcodes_successful.md
.claude/references/mql5/API/retcodes_trades.md
.claude/references/mql5/API/retcodes_authentication.md
```

Never log or return raw credentials. Never crash on a single entity failure — continue with next entity.

---

## Windows deployment

MT5Manager is Windows-only. collector-mt5 runs on Windows EC2.
Credentials loaded from AWS Secrets Manager at startup — never from .env or hardcoded.

---

## What NOT to do

```
- Never import or call MT5Manager from the frontend or API service
- Never use the MetaTrader5 pip package — that is the terminal client, not manager API
- Never transform or normalize data before saving raw
- Never design raw schemas without reading the real object field docs
- Never advance cursor past failed records
- Never hardcode credentials
- Never read from any folder other than .claude/references/mql5/API/
```

---

## Reference implementations (fill as built)

```
services/collector-mt5/collector.py   ← main collector class
services/collector-mt5/ingestion.py   ← raw save logic
services/collector-mt5/tests/         ← unit tests with mocked MT5Manager
tests/fixtures/mt5/                   ← real captured MT5 payloads per entity
```
