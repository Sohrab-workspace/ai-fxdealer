# Auto Trading

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)Auto Trading

# Auto Trading

To work at financial markets more effectively, one can develop one's own successful system of trading. It is very difficult to act within a chosen system of trading in the manual mode due to significant influence of normal human emotions. Mechanical trading systems do not suffer from this disadvantage.

Client Terminal gives a large range of means for development and use of mechanical trading systems (MTS, experts, advisors). The development environment allows to create, debug, and test expert advisors. Experts are able not only alert about recommendation trading signals, but undertake the complete control over trading activities online.

[MetaQuotes Language 4](/en/docs/mt4/terminal/autotrading/mql4), [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor) and [strategy testing tools](/en/docs/mt4/terminal/overview/strategy_tester) are built in the terminal. One can create the following using these means:

-   [Expert Advisors](/en/docs/mt4/terminal/autotrading/experts) — mechanical trading systems that allow complete automation of analytical and trading activities;
-   [Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators) — independently written [technical indicators](/en/docs/mt4/terminal/analytics/tech_indicators) intended for analyzing of price changes;
-   [Scripts](/en/docs/mt4/terminal/autotrading/scripts) — programs to be executed only once, on request.

### New algorithmic trading features

The new platform allows [accelerating trading](https://www.mql5.com/en/articles/2635) dozens of times: MQL5 compiler aggressively optimizes the obtained EX5 executable code, the OrderSendAsync asynchronous function is executed in fractions of a millisecond, orders are processed on a trade server in no time, while price and Depth of Market updates are delivered to the terminal without delay. All components of the fifth generation platform (terminal and trading server) are developed with the maximum time efficiency in mind and are subjected to internal stress tests for performance under high-load conditions.

The new MQL5 language speed is comparable to that of С++, while MQL5 programs work up to 20 times faster than MQL4 ones since all functions of the new language are developed taking into account the capabilities of modern processors and code profiling results. If necessary and properly qualified, you can further accelerate the calculations using OpenCL functions. The MetaEditor development environment supports the OpenCL interface for using the power of modern video cards.

The new platform allows you to trade both on Forex and a stock exchange enabling you to develop a single [trading strategy for multiple instruments](https://www.mql5.com/en/articles/2739). The new tester is a multi-asset tool, which means that you are able to test strategies working on multiple financial instruments simultaneously. Thus, you develop the same code both for testing and for real trading. There are no restrictions on the part of the tester, and you do not have to test each instrument within a complex strategy separately. The entire trading environment is reproduced as accurately as possible and ticks are synchronized across all used instruments up to milliseconds.

All timeframes in the new terminal are built automatically based on the minute history at the first call from a chart, an EA or an indicator. In this case, all timeframes are rebuilt and synchronized with each other automatically without manual intervention maintaining the integrity and relevance of all data on each symbol. When running [multi-currency testing](https://www.mql5.com/en/docs/runtime/testing#multicurrency), all necessary history for all used symbols is automatically downloaded from the trade server, while the timer events and the Sleep() function calls are handled correctly.

Time & Sales with real volumes and order levels, as well as manual trading inside the Depth of Market and developing scalper strategies based on the order book and liquidity are available for you in order to trade on an exchange. The expanded Depth of Market featuring volumes and the appropriate MQL5 functions allow you to develop custom symbols for intraday trading. While developing such robots, you can use real ticks to test strategies trading on multiple symbols.

Custom symbols are another key advantage of the new platform. To create them, simply enter the calculation formula or download files with minute bars or tick history. You can test your strategies both on custom symbols, and the ones provided by the trade server. Thus, the new terminal allows you to test your trading ideas on an unlimited set of symbols and any markets  simply create a necessary symbol and test your EA on it.

Explore [MQL5 language features](https://www.mql5.com/en/articles/447) and take your EA programming skills to the next level.

[Trading on Chart](/en/docs/mt4/terminal/positions/trading_chart)

[Where to Get Trade Robots and Indicators](/en/docs/mt4/terminal/autotrading/charts_analysis_get_indicators)