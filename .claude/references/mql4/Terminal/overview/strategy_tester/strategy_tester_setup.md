# Setup

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup

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
            -   [Main Menu](/en/docs/mt4/terminal/overview/main_menu)
            -   [Toolbars](/en/docs/mt4/terminal/overview/toolbars)
            -   [Market Watch](/en/docs/mt4/terminal/overview/market_watch)
            -   [Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)
            -   [Data Window](/en/docs/mt4/terminal/overview/data_window)
            -   [Navigator](/en/docs/mt4/terminal/overview/navigator)
            -   [Chart Switching Bar](/en/docs/mt4/terminal/overview/charts_bar)
            -   [Client terminal](/en/docs/mt4/terminal/overview/terminal)
            -   [Tester](/en/docs/mt4/terminal/overview/strategy_tester)
                -   [Setup](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup)
                -   [Properties](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_properties)
                -   [Results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_results)
                -   [Graph](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_charts)
                -   [Report](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_report)
                -   [Journal](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_journal)
                -   [Optimization Results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_results)
                -   [Optimization Graph](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_charts)
            -   [Search](/en/docs/mt4/terminal/overview/search)
            -   [Fast Navigation](/en/docs/mt4/terminal/overview/fast_nav)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Tester](/en/docs/mt4/terminal/overview/strategy_tester)Setup

# Setup

![strategy_tester](/en/docs/mt4/terminal/img/strategy_tester.png)

[Testing parameters](/en/docs/mt4/terminal/autotrading/tester/tester_parameters) and [experts optimization parameters](/en/docs/mt4/terminal/autotrading/tester_optimization/tester_optimization_parameters) can be set up in this tab. At testing, the expert is passed on the modeled data one time what allows to determine the profitability and efficiency thereof. At optimization, the mechanical trading system is passed several times with the purpose of determining of such expert parameters at which its profitability is the highest.

The following commands and options are available in this tab:

-   Expert Advisor — select the expert to be tested in the list. The expert must be compiled and placed in the /EXPERTS directory. All newly created experts will be automatically placed into this directory;
-   Symbol — select one of the securities available;
-   Period — select the symbol timeframe;
-   Model — select the method of bars modeling:

-   -   Every tick (based on all available least timeframes with fractal interpolation of every tick);
    -   Control points (based on the nearest less timeframe with fractal interpolation of 12 control points);
    -   Open prices only (fastest method to analyze the bar just completed);

-   Spread — the price history stored in the client terminal includes only Bid prices. On default, to model Ask prices, the strategy tester uses the current spread of a symbol at the beginning of testing. However a user can set a custom spread for testing in the "Spread" field.
-   Use date — use range of dates when testing. If this option is enabled, the data from the given range will be used during testing. Otherwise, all available data for the given symbol and period are used;
-   Visual mode — enable the mode of the visual displaying the test process on a graph. You can adjust the speed of the testing visualization using the lever located to the right. You can also specify a date in the "Skip to" field to skip visualizing the test till that date.
-   Optimization — enable the expert parameters optimization mode. More details about expert parameters optimization can be found in the [section of the same name](/en/docs/mt4/terminal/autotrading/tester_optimization);
-   Expert properties — open the ["Expert Properties"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_properties) window that allows to manage the expert parameters when testing and optimizing;
-   Symbol properties — view the symbol parameters. These data are given in the [\*.FXT file](/en/docs/mt4/terminal/autotrading/tester/tester_fxt) heading and used to emulate the server operation;
-   Open chart — create a new chart window for the symbol selected for testing. When being tested, the expert works with a virtual chart. Signs of opening and closing of positions, objects and indicators used by the expert, are imposed in this chart. This chart can be opened only after the expert has been tested. For opening of a virtual chart, the TESTER.TPL template is used, and, if it is not available, the default settings are used. You can also give a template the same name as that of an Expert Advisor. In this case, that exact template will be used when opening the chart of the Expert Advisor;
-   Modify expert — open the ["MetaEditor"](/en/docs/mt4/terminal/autotrading/metaeditor) and start to edit the selected expert. This is useful if there is a need to introduce small changes and recompile the expert fast;
-   Start — start testing or optimization. After this button has been pressed, one can estimate the speed of testing or optimization in progress bar in the lower part of the window. After the testing has been started, the "Start" button will be replaced with the "Stop" button. Having pressed this button during testing/optimization, one can stop the process.

More details about testing experts can be found in the [section of the same name](/en/docs/mt4/terminal/autotrading/tester).

[Tester](/en/docs/mt4/terminal/overview/strategy_tester)

[Properties](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_properties)