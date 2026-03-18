# Working with Charts

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/chart_management

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
            -   [Chart Opening](/en/docs/mt4/terminal/chart_management/charts_open)
            -   [Setup](/en/docs/mt4/terminal/chart_management/charts_setup)
            -   [Chart Management](/en/docs/mt4/terminal/chart_management/charts_control)
            -   [Publishing Charts Online](/en/docs/mt4/terminal/chart_management/mql5_charts)
            -   [Quick Trading](/en/docs/mt4/terminal/chart_management/chart_trading)
            -   [Charts Print](/en/docs/mt4/terminal/chart_management/charts_print)
            -   [Deleted Charts](/en/docs/mt4/terminal/chart_management/charts_deleted)
            -   [Templates and Profiles](/en/docs/mt4/terminal/chart_management/templates)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)Working with Charts

# Working with Charts

A chart shows the price changes for a security with the time. Charts are necessary for performing [technical analysis](/en/docs/mt4/terminal/analytics), [working of expert advisors](/en/docs/mt4/terminal/autotrading/experts) and [testing](/en/docs/mt4/terminal/autotrading/tester) thereof. Up to ninety-nine charts can be opened in the terminal at the same time.

The client terminal allows to:

-   [open](/en/docs/mt4/terminal/chart_management/charts_open) up to 99 chart simultaneously;
-   [set up](/en/docs/mt4/terminal/chart_management/charts_setup) their representation form and information shown;
-   [print](/en/docs/mt4/terminal/chart_management/charts_print) charts;
-   [impose and delete](/en/docs/mt4/terminal/chart_management/charts_control) various objects and indicators;
-   recover [deleted charts](/en/docs/mt4/terminal/chart_management/charts_deleted);
-   use chart [templates](/en/docs/mt4/terminal/chart_management/templates).

### New trading features

The new generation platform has two times [more timeframes](https://www.mql5.com/en/docs/constants/chartconstants/enum_timeframes) (21 vs 9), as well as the precise time scale. Now graphical objects are not necessarily linked to bars. Object anchors can be placed in any position between the chart bars. Moreover, when switching between timeframes, the accurate positioning of the control points of the object is preserved. New built-in indicators and analytical tools have also been added.

In the new terminal, all timeframes are built based on minute bars, while the history is downloaded and synchronized automatically without the need for manual download. Additionally, the trade server stores the tick history of each symbol, so that you can use it for [testing on real ticks](https://www.mql5.com/en/articles/2612). This ensures the maximum accuracy of testing trading robots on history and allows you to avoid mistakes when using rough tick generation methods.

The new platform also features custom symbols, or synthetic indices you can create yourself. To do that, simply enter the calculation formula or download files with minute bars or tick history. You can test your strategies both on custom symbols, and the ones provided by the trade server. Thus, the new terminal allows you to test your trading ideas on an unlimited set of symbols and markets.

![custom_symbol_create](/en/docs/mt4/terminal/img/custom_symbol_create.png)

[Fast Navigation](/en/docs/mt4/terminal/overview/fast_nav)

[Chart Opening](/en/docs/mt4/terminal/chart_management/charts_open)