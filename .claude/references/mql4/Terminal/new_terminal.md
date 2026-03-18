# New trading features

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/new_terminal

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
            -   [Trading](/en/docs/mt4/terminal/new_terminal/new_trading)
            -   [Charts](/en/docs/mt4/terminal/new_terminal/new_charts)
            -   [MQL5](/en/docs/mt4/terminal/new_terminal/new_mql5)
            -   [Tools](/en/docs/mt4/terminal/new_terminal/new_tools)
            -   [Strategy Tester](/en/docs/mt4/terminal/new_terminal/new_tester)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)New trading features

# New trading features

The current version of the trading platform is most popular all over the world thanks to its user-friendly interface, a variety of technical analysis tools and the integrated MQL4 language for developing indicators and trading robots. Let us congratulate you on your excellent choice and offer you a brief tour on the fifth generation terminal features.

### Exchange trading

The new platform allows you to trade not only Forex symbols but also exchange instruments — Time & Sales with real volumes and order levels, as well as manual [trading inside the Depth of Market](https://www.metatrader5.com/en/terminal/help/trading/depth_of_market#quick_trading) and developing scalper strategies based on the order book and liquidity are available for you. For fundamental traders, the platform features the Economic Calendar with a detailed description of each indicator, while the event schedule is displayed directly on a chart. The Calendar functions allow you to track and analyze changes of the necessary macroeconomic indicator directly from MQL5 programs.

![terminal5](/en/docs/mt4/terminal/img/terminal5.png)

### Programs run up to 20 times faster

The MQL5 execution speed is comparable to that of С++ applications, while MQL5 programs work up to 20 times faster than MQL4 ones. This is proved by the execution time of standard tests on MQL4, MQL5 and C++. The lower the bar, the less time spent on execution and the better the result. The tests have been conducted on Windows 10 (build 17763) x64, Xeon  E5-2630 v4 @ 2.20GHz, Memory: 65457 Mb.

![mql4_vs_mql5_vs_cpp](/en/docs/mt4/terminal/img/mql4_vs_mql5_vs_cpp.png)

If we also keep in mind asynchronous operations having an execution time less than a millisecond, we can safely state that MQL5 provides algorithmic trading features that were previously available only to a handful of professional traders. With the fifth generation platform, you do not need third-party connections to exchange protocols. Besides, you do not need to place your terminals as close to a broker as possible. Just get a VPS next to the trading server and send your fast MQL5 robot to trade there directly from the terminal. Low network costs, high Depth of Market refresh rates and asynchronous order sending [accelerate trading operations dozens of times](https://www.mql5.com/en/articles/2635), which is a key factor in the algorithmic trading.

### Multi-threaded strategy tester and MQL5 Cloud Network

The new platform offers maximum opportunities for testing and optimizing trading strategies for the algorithmic trading. Below are just a few of the main advantages of the new tester:

-   Testing multi-asset strategies that trade on multiple symbols simultaneously, while all the necessary history is downloaded from the trade server automatically. Accurate emulation of the trading environment allows you to correctly test arbitrage strategies, pair trading and other similar systems that require synchronization of ticks, Depths of Market, OHLC prices and indicator values for all necessary symbols.
-   Testing on [real ticks](https://www.mql5.com/en/articles/2612) allows you to develop strategies based on instant price changes. Ticks for all symbols are reproduced with millisecond precision, while the test can be performed in debug and program profiling mode enabling the development of efficient trading robots in terms of speed.
-   Multi-threaded optimization using all cores of the local PC the terminal is installed on. For even higher speed, connect [MQL5 Cloud Network](https://www.mql5.com/en/articles/341) agents to receive the results of thousands of hours of calculations in 30 minutes.
-   Advanced reports and visualization of optimization results simplify the analysis of obtained data and the search for patterns. The 3D optimization graph is provided as well. You can zoom it in and out, rotate to a convenient angle, etc. Charts and trading parameters provide you with a detailed picture of the obtained testing and optimization results.

![3d_visualization](/en/docs/mt4/terminal/img/3d_visualization.png)

Explore the new features and trade in the fifth generation platform!

[Client terminal](/en/docs/mt4/terminal)

[Trading](/en/docs/mt4/terminal/new_terminal/new_trading)