# Strategy Testing

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/tester

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
                -   [Setup](/en/docs/mt4/terminal/autotrading/tester/tester_parameters)
                -   [Results](/en/docs/mt4/terminal/autotrading/tester/tester_results)
                -   [History Files in FXT Format](/en/docs/mt4/terminal/autotrading/tester/tester_fxt)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)Strategy Testing

# Strategy Testing

The terminal allows you not only to write expert advisors, but also [test](/en/docs/mt4/terminal/autotrading/tester/tester_parameters) them before using. This useful function allows to check operativeness and efficiency of the trading system on history data. Testing allows to start automated trading with the full knowledge about expert conduct under different market conditions. The special ["Tester"](/en/docs/mt4/terminal/overview/strategy_tester) window was built into the terminal for this purpose. Using this window, one can [optimize expert inputs](/en/docs/mt4/terminal/autotrading/tester_optimization), as well.

### New features for checking trading systems

The new platform offers traders a multi-asset strategy tester that allows the development and testing of trading systems of any complexity.

The [multi-asset](https://www.mql5.com/en/docs/runtime/testing#multicurrency) nature of the tester means that you are now able to test trading robots working on multiple financial instruments and markets simultaneously, for example, on two Forex pairs and one exchange futures. The entire trading environment is reproduced as accurately as possible and ticks are synchronized across all used instruments up to milliseconds. The margin and the current profit are calculated according to the trading system requirements, be it an ECN platform or an exchange.

An important advantage of the new tester is the availability of the [real tick testing mode](https://www.mql5.com/en/docs/runtime/testing#real_ticks). The trade servers of the new platform store the entire real tick history. The strategy tester automatically downloads all necessary history in the "Every tick based on real ticks" mode. You do not need to worry about getting the correct historical data and providing it to the strategy tester. The tester will handle this on its own.

In addition, the new tester allows you to debug and profile the EA code on historical data without waiting for certain trading events in real time. Debugging on history data runs in the visual testing mode in the Strategy Tester. An EA is executed on a chart based on an emulated or real sequence of ticks.

The tester's important objective is providing EA's test results. Apart from potential profit displayed on history, you also obtain a great amount of statistical data including profit/loss percentage ratio, number of profitable/loss-making deals, recovery factor, expected payoff and much more. The contents and number of parameters in the [new test report](https://www.metatrader5.com/en/terminal/help/algotrading/testing_report) are significantly expanded, while distribution graphs make the trading strategy analysis even more convenient.

![tester_results](/en/docs/mt4/terminal/img/tester_results.png)

[Shutdown](/en/docs/mt4/terminal/autotrading/experts/experts_remove)

[Setup](/en/docs/mt4/terminal/autotrading/tester/tester_parameters)