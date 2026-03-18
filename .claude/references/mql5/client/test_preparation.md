# How the Tester Downloads Historical Data

> Source: https://support.metaquotes.net/en/docs/mt5/client/test_preparation

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
            -   [Expert Advisors and Custom Indicators](/en/docs/mt5/client/trade_robots_indicators)
            -   [Where to Find Trading Robots and Indicators](/en/docs/mt5/client/algotrading_get_ea_indicator)
            -   [How to Create an Expert Advisor or an Indicator](/en/docs/mt5/client/autotrading)
            -   [Strategy Testing](/en/docs/mt5/client/testing)
            -   [How the Tester Downloads Historical Data](/en/docs/mt5/client/test_preparation)
            -   [Strategy Optimization](/en/docs/mt5/client/strategy_optimization)
            -   [Testing Features](/en/docs/mt5/client/testing_features)
            -   [Testing Report](/en/docs/mt5/client/testing_report)
            -   [Testing Visualization](/en/docs/mt5/client/visualization)
            -   [Journal of Testing](/en/docs/mt5/client/tester_journal)
            -   [Optimization Types](/en/docs/mt5/client/optimization_types)
            -   [Real and Generated Ticks](/en/docs/mt5/client/tick_generation)
            -   [MetaTester and Remote Agents](/en/docs/mt5/client/metatester)
            -   [Global Variables](/en/docs/mt5/client/service_global)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)How the Tester Downloads Historical Data

# How the Tester Downloads Historical Data

### Loading Historical Data, Preparing for Testing, and Adjusting the Test Start Date

The [Strategy Tester](/en/docs/mt5/client/testing) creates a highly realistic market simulation. To achieve this, it preloads sufficient historical data for the selected symbol.

Before running any test, the platform synchronizes historical data:

-   From the trading server, M1 bars and tick data for the selected symbol are downloaded to the terminal. On the first launch of the tester, the terminal downloads the entire available history for the symbol.
-   From the terminal, the history is copied in compressed form to the testing agent. The agent then generates ticks locally or uses actual tick data (if available).
-   In multi-currency tests, when the strategy first accesses a new symbol or timeframe, the test is paused while missing data is downloaded. The system also downloads an additional buffer of data so that indicators can calculate values from the very first bar.

### Minimum Historical Data Requirements

To ensure calculation stability, the tester always loads a "pre-start history buffer":

-   D1 and below — from the beginning of the previous calendar year. This provides at least 1 year of history. Example: if the test start date is 01.03.2023, the terminal will download form the terminal data from 01.01.2022. This equals to 14 months before the test start.
-   W1 — at least 100 weekly bars (~2 years).
-   MN1 — at least 100 monthly bars (~8 years).

If the available history is insufficient, the tester automatically shifts the actual start date forward to the nearest point that meets the requirements.

In such cases, testing begins later than the date specified by the user. The tester log will show a relevant message, for example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">start&nbsp;time&nbsp;changed&nbsp;to&nbsp;2024.03.15&nbsp;00:00&nbsp;to&nbsp;provide&nbsp;data&nbsp;at&nbsp;beginning</span></p></td></tr></tbody></table>

This is not an error but a built-in mechanism to ensure correct computations.

For multi-currency tests, whenever the strategy accesses a new symbol or timeframe, the tester pauses to load additional history. This also includes the downloading of an extra buffer for indicator calculations and margin recalculations.

The Strategy Tester stores history for each symbol centrally, available to all local agents. Example (EURUSD):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">\Program&nbsp;Files\MetaTrader&nbsp;5&nbsp;Strategy&nbsp;Tester\Tester\bases\&lt;trading_server_name&gt;\history\EURUSD</span></p></td></tr></tbody></table>

### Tick history is stored similarly:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">\Program&nbsp;Files\MetaTrader&nbsp;5&nbsp;Strategy&nbsp;Tester\Tester\bases\&lt;trading_server_name&gt;\ticks\EURUSD</span></p></td></tr></tbody></table>

### How to Reduce or Avoid Test Start Date Shifts

Use a lower timeframe.

The tester requires at least 100 bars on the selected timeframe before modeling can begin.

This ensures stable indicator calculations and proper initialization.

-   If you run a test on D1, at least 100 daily bars (~5 months) are needed.
-   On H1 or M15, only 100 hourly or 15-minute bars are required. This amount of data is almost always available, even if the history is limited.
-   Therefore, when historical data is insufficient, the start date shift is smaller on lower timeframes than on higher ones.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><img class="help" alt="alert_icon" width="15" height="16" src="/en/docs/mt5/client/img/alert_icon.png"> <span class="f_tableatten">However, the Expert Advisor must operate correctly on the chosen timeframe. If a strategy is originally designed for D1, then when testing on M15 or H1 you must ensure it synchronizes its calculations properly and does not start recalculating signals too frequently.</span></p></td></tr></tbody></table>

### Minimum History by Timeframe and Potential Test Start Shift

<table class="table" cellspacing="0" cellpadding="5" border="1" style="width:1200px;"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Testing Timeframe</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Minimum Data Loaded</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Possible Start Shift</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">M1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">≥100 bars (≈1h 40m) &nbsp; &nbsp; &nbsp; &nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Virtually none</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">M15</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">&gt;100 bars (~25h)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Minimal</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">H1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">≥100 bars (~4 days) &nbsp; &nbsp; &nbsp; &nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Minimal</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">D1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">≥100 bars (~5 months) &nbsp; &nbsp; &nbsp; &nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Up to 5 months</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">W1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">≥100 weeks (~2 years) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Up to 2 years</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">MN1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">≥100 months (~8 years) &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Up to 8 years (if history is limited)</span></p></td></tr></tbody></table>

### How to Read the Table

-   On D1, the tester will always shift the start date forward until at least 100 daily bars are available.
-   On H1 or M15, only a few days of data are needed, which is usually available, so the test starts much closer to the chosen date.
-   On higher timeframes (W1 and MN1), the shift can be very large, since years of history are required.

### Additional Tester Features

-   Tick generation modes:
    -   Every Tick — ticks are generated from M1 bars, providing maximum realism. This is the most resource-intensive and time-consuming testing mode.
    -   1 Minute OHLC — faster but less realistic. Tick sequences are built only from M1 OHLC prices. The number of generated control points is significantly reduced, which shortens test duration. The OnTick() function is triggered at all OHLC points.
    -   Open Prices Only — uses only the opening prices of bars on the selected timeframe. Very fast but less accurate, and requires caution in multi-currency tests. OnTick() is called only at the beginning of each bar at its Open price. Because of this, stop levels and pending orders may not trigger at exact prices (especially on higher timeframes). However, this mode is best for quick preliminary Expert Advisor testing. This is the fastest and least accurate type of testing.
    -   Every Tick based on real ticks — maximum accuracy. Instead of generated tick sequences, the tester uses broker-provided tick data. M1 bars are also used in real-tick mode. The bars are used to verify and correct tick history. This also prevents discrepancies between tester and live terminal charts.

-   Time simulation:
    -   TimeLocal(), TimeTradeServer(), and TimeGMT() return identical values during tests.

-   OnTimer and Sleep:
    -   These functions are supported during tests. Timers slow down the simulation, while Sleep() simulates pauses (but infinite loops cause errors).

### Agent Cache and Reuse

-   Historical data is stored in compressed form and reused if the test interval and settings remain unchanged.
-   Local agent processes remain active for about 5 minutes after a test ends, enabling faster startup of subsequent tests.

[Strategy Testing](/en/docs/mt5/client/testing)

[Strategy Optimization](/en/docs/mt5/client/strategy_optimization)