# Testing Indicators

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/tester_indicator

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
            -   [Where to Get Trade Robots and Indicators](/en/docs/mt4/terminal/autotrading/charts_analysis_get_indicators)
            -   [MQL4](/en/docs/mt4/terminal/autotrading/mql4)
            -   [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor)
            -   [Expert Advisors](/en/docs/mt4/terminal/autotrading/experts)
            -   [Strategy Testing](/en/docs/mt4/terminal/autotrading/tester)
            -   [Indicator Testing](/en/docs/mt4/terminal/autotrading/tester_indicator)
            -   [Expert Optimization](/en/docs/mt4/terminal/autotrading/tester_optimization)
            -   [Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)
            -   [Scripts](/en/docs/mt4/terminal/autotrading/scripts)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)Indicator Testing

# Testing Indicators

The Strategy Tester in the trading platform allows you to test not only Expert Advisors, but also indicators. This can be done in the visual testing mode. The behavior of the indicator is shown on a chart, which is plotted based on a sequences of ticks simulated in the tester.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Various indicators are available in the MetaTrader <a href="/en/docs/mt4/terminal/market" class="topiclink">Market</a>. Before purchasing you can download a demo version of an indicator and test it in the strategy tester.&lt;/s2&gt;</span></p></td></tr></tbody></table>

This section describes how to configure and [testing](/en/docs/mt4/terminal/autotrading/tester_indicator#testing) indicators.

## Setup

-   [How to Select an Indicator and Configure It](/en/docs/mt4/terminal/autotrading/tester_indicator#indicator)
-   [Symbol and Its Period](/en/docs/mt4/terminal/autotrading/tester_indicator#symbol)
-   [Modeling Techniques](/en/docs/mt4/terminal/autotrading/tester_indicator#mode)
-   [Time Range](/en/docs/mt4/terminal/autotrading/tester_indicator#range)

### How to Select an Indicator and Configure It [#](tester_indicator#indicator)

If you need to test an indicator, select the appropriate program type "Indicators" in the strategy tester. After that, select an indicator from the list. The list features all indicators, which are located in the terminal folder MQL4\\Indicators (including subfolders).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you select testing of indicators, the visual mode is automatically activated.</span></p></td></tr></tbody></table>

![Indicator Testing Settings](/en/docs/mt4/terminal/img/test_indicator.png "Indicator Testing Settings")

You can test any indicator from the [Market](/en/docs/mt4/terminal/market) for free before buying. Download the demo version of the indicator, double-click on it in the [Navigator](/en/docs/mt4/terminal/overview/navigator) and click on "Test":

![Testing of demo versions of products from the Market](/en/docs/mt4/terminal/img/test_indicator_market.png "Testing of demo versions of products from the Market")

Then the indicator will be selected in the strategy tester, you will only have to configure parameters and start the testing process.

If an indicator has any input parameters, you can configure them before the start of testing. Click "Indicator Properties".

![Indicator Properties](/en/docs/mt4/terminal/img/test_indicator_inputs.png "Indicator Properties")

### Symbol and Its Period [#](tester_indicator#symbol)

To start testing, it is not enough just to select an indicator and set it up. One has to select a symbol and a period (timeframe) for testing. These are data that will be used for testing. At testing, one can select an available in terminal symbol or use an external data file. History data files of \*.FXT format stored in the /TESTER directory are used in testing. These file are created automatically at testing if an available in the terminal symbol was selected.

The symbol is defined in the field of the same name, and timeframe is in the "Period" field. If no data file for this symbol, period and modeling method does not exist yet, it will be created automatically. If there are no history data for the symbol or period, the tester will download the last 512 history bars automatically.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If there are some data outside the latest 512 bars for the symbol, the history data will be downloaded automatically, up to the last available one. This can cause sharp increase of the incoming traffic.</span></p></td></tr></tbody></table>

### Modeling Techniques [#](tester_indicator#mode)

Historical data are saved in the terminal only as bars and represent records appearing as [TOHLCV (HST format)](/en/docs/mt4/terminal/service/history_center). These data can be used for modeling of price changes at testing indicators. In some cases, such information is not enough for testing. For example, for the daily timeframe, price changes within a bar can result in generating a trade signal. At the same time, no generation may occur at testing. In other words, testing an indicator based on only bars can be inaccurate and give a false idea about the efficiency.

The trading terminal allows to test indicators by various methods of historical data modeling. Using historical data from smaller periods, it is possible to see price fluctuations within bars, i.e., price changes will be emulated more precisely. For example, when an indicator is tested on one-hour data, price changes for a bar can be modeled on one-minute data. Thus, modeling brings historical data near the real price fluctuations and makes expert testing more authentic.

One of three methods of historical data modeling can be chosen for testing:

-   Open prices only (fastest method to analyze the bar just completed)
-   Control points (the nearest less timeframe is used)
-   Every tick (based on all available least timeframes)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Find out more about modeling techniques in section <a href="/en/docs/mt4/terminal/autotrading/tester/tester_parameters#model" class="topiclink">"Testing Strategies"</a>.</span></p></td></tr></tbody></table>

The price history stored in the client terminal includes only Bid prices. On default, to model Ask prices, the strategy tester uses the current spread of a symbol at the beginning of testing. However a user can set a custom spread for testing in the "Spread" field.

### Time Range [#](tester_indicator#range)

The range of dates allows to test experts not on all available data, but within a certain time space only. This can be useful if there is a need to test a certain part of history data. Date range can be used not only for expert testing, but also for modeling of the testing succession of bars (file of data modeled to be used for testing).

It is often no need to model data of the entire history, especially for every-tick modeling where the amount of unused data can be very large. That is why, if data range was allowed to be set at the initial modeling of testing succession, bars that are beyond this range will not be modeled, but just transcribed into the output succession. The data will not be excluded from the succession in order the correct calculation of indicators on the entire received history to be possible.

It must be noted that the first 100 bars will not be modeled either. This limitation does not depend on the date range defined.

To enable date range limitation, one has to flag "Use date" and specify the necessary values in the fields of "From" and "To". After all settings have been made, one can press the "Start" button and start testing. After testing has started, the approximate time of completing of this process can be viewed in the lower part of the window.

## Indicator Testing Process [#](tester_indicator#testing)

The behavior of the indicator is shown on a chart, which is plotted based on a sequences of ticks simulated in the tester. This chart is generated automatically after the testing process is started. It's name contains the financial symbol, the timeframe used and the property "visual".

![Indicator Testing](/en/docs/mt4/terminal/img/test_indicator_result.png "Indicator Testing")

Logs on the indicator testing process appear n the "Journal" tab. This journal is similar to that in the ["Terminal — Experts" window](/en/docs/mt4/terminal/overview/terminal/terminal_experts). The only difference is that in the tester window, logs are related to the indicator testing instead of operation on a real chart. After the testing process is over, these data are displayed in a separate directory /TESTER/LOGS. The log files are stored in folder /EXPERTS/LOGS, file names correspond to journal creation date — YYYYMMDD.LOG.

[History Files in FXT Format](/en/docs/mt4/terminal/autotrading/tester/tester_fxt)

[Expert Optimization](/en/docs/mt4/terminal/autotrading/tester_optimization)