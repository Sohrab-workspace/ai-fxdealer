# Debugging

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/settings/settings_debug

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

# Debugging

Common parameters of program [debugging](/en/docs/mt5/metaeditor/development/debug) and [profiling](/en/docs/mt5/metaeditor/development/profiling) are set up in this tab.

![Debugging](/en/docs/mt5/metaeditor/img/settings_debug.png "Debugging")

The following parameters are represented here:

-   Use specified settings — turn on/off use of specified settings for program debugging and profiling. In this case a program will be run on a chart with the specified symbol and period. During debugging on history, these parameters are used for visual testing. If this option is disabled, editing of the below fields will be unavailable.

-   Symbol — the symbol the chart by which will be used for debugging/profiling programs.
-   Period — the chart period that will be used for debugging/profiling programs.

-   Date — the time period to run a program [while debugging on history](/en/docs/mt5/metaeditor/development/debug#history). Visual testing in the strategy tester will run on this period data.
-   Execution — the strategy tester allows you to emulate network delays during an Expert Advisor operation in order to bring testing closer to real conditions. A certain time delay is inserted between placing a trade request and its execution in the strategy tester. From the moment of sending a request till its execution, the price can change. This allows you to evaluate how trade processing speed affects the trading results. Select a delay to be used when debugging on history: no delay, a fixed value (one of the predefined values or a custom one) or a random value. For more details please read the client terminal user guide.
-   Tick generation mode — used for debugging on history. For more details please read the client terminal user guide.

-   Every tick — this is the most accurate, but the slowest mode. All ticks are emulated.
-   OHLC on М1 — in this mode, only 4 prices of every 1-minute bar are generated — Open, High, Low and Close prices.
-   Only Open prices — OHLC prices are generated, but only the Open price is used for testing/optimization.

-   Deposit and leverage — initial deposit amount and leverage used during debugging on history.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">If no symbol or chart period is specified in this tab, then the first symbol in the Market Watch window and period H1 will be used for debugging/profiling on default.</span></p></td></tr></tbody></table>