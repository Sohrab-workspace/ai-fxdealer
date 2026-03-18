# Expert Advisors

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/experts

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
                -   [Creation](/en/docs/mt4/terminal/autotrading/experts/experts_create)
                -   [Setup](/en/docs/mt4/terminal/autotrading/experts/experts_setup)
                -   [Launch](/en/docs/mt4/terminal/autotrading/experts/experts_launch)
                -   [Shutdown](/en/docs/mt4/terminal/autotrading/experts/experts_remove)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)Expert Advisors

# Expert Advisors

Expert Advisors (experts) are programs in the terminal that have been developed in [MetaQuotes Language 4 (MQL4)](/en/docs/mt4/terminal/autotrading/mql4) and used for automation of analytical and trading processes. They allow to perform prompt technical analysis of price data and manage trading activities on basis of signals received. The entire routine work of technical analysis and trading can be given to experts. An expert can perform analytical and trading operations for any symbols or periods independent on whether the corresponding chart was opened or not.

Working with experts means:

-   [Creation of an Expert](/en/docs/mt4/terminal/autotrading/experts/experts_create)  
    To create and compile an expert, one has to use the built-in ["MetaEditor"](/en/docs/mt4/terminal/autotrading/metaeditor). It is a constituent of the client terminal and represents a convenient development environment of MQL4 programs.
-   [Expert Setup](/en/docs/mt4/terminal/autotrading/experts/experts_create)  
    Before using of experts, one has to set up them first. Working parameters common for all experts are set in the [client terminal settings](/en/docs/mt4/terminal/setup/setup_experts). Besides, each expert can have its own settings.
-   [Launch of an Expert](/en/docs/mt4/terminal/autotrading/experts/experts_create)  
    To launch an expert, one has to impose it into the chart. As soon as a new tick incomes, the expert will start executing.
-   [Expert Shutdown](/en/docs/mt4/terminal/autotrading/experts/experts_create)  
    An expert advisor is shut down after it has been removed from the chart.

### New features of trading robots development

The new MQL5 language syntax is similar to that of MQL4 but MQL5 programs work up to 20 times faster. This is possible because all MQL5 language functions are implemented as efficiently as possible, while the compiler aggressively optimizes the obtained executable EX5 code to achieve the high speed of MQL5 applications.

The second reason is the implementation of asynchronous operations executed in a fraction of a millisecond. These operations open opportunities previously unavailable for many professional traders. With the fifth generation platform, you do not need third-party connections to exchange protocols. Besides, you do not need to place your terminals as close to a broker as possible. Just get a VPS next to the trading server and send your fast MQL5 robot to trade there directly from the terminal. Low network costs, high Depth of Market refresh rates and asynchronous order sending [accelerate trade operations dozens of times](https://www.mql5.com/en/articles/2635) allowing you to develop trading robots for the new class of strategies.

MQL5 implements event handling making it simpler and easier to build complex trading algorithms. At each trading operation, the Trade and TradeTransaction events are sent to the terminal to be processed by the appropriate handlers. Orders, positions and deals are considered separate entities in the new platform, since now you can trade not only usual Forex symbols, but also exchange instruments. The Standard Library offers the ready-made Trading Classes to work with trading functions. The classes simplify the development of trading operations. You only need to declare the CTrade type variable to get the entire functionality necessary to work with all order types.

To quickly check your trading idea, [assemble a robot using MQL5 Wizard](https://www.mql5.com/en/articles/275) modules without writing a single line of code. The ready-made trading signal, open position tracking (trailing stop) and money management (setting volumes in trading operations) modules allow creating an unlimited number of trading strategy versions and combining several types of signals in a single EA. Thus, the new terminal makes it possible to develop complex strategies even with no programming skills.

Another advantage of MQL5 language is the ability to work with the Depth of Market and access the tick history. Analyze Time & Sales and develop strategies based on price change and deal volume directly in an EA. In the new platform, the trade server stores a tick history of each symbol and sends it to the terminal on request when [testing on real ticks](https://www.mql5.com/en/articles/2612). The MetaEditor developer environment allows debugging and profiling EAs directly in the strategy tester enabling a quick check of trading algorithms in different market situations. In the tester, such a test will take a few minutes and hours, while the conventional test of robots online will take days and weeks.

Explore [MQL5 language features](https://www.mql5.com/en/articles/447) and start developing strategies in the new generation platform.

[MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor)

[Creation](/en/docs/mt4/terminal/autotrading/experts/experts_create)