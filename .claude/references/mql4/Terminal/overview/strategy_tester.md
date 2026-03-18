# Tester

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/strategy_tester

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)Tester

# Tester

"Tester" is a multifunctional window that allows to [test strategies](/en/docs/mt4/terminal/autotrading/tester) and [optimize parameters of expert advisors](/en/docs/mt4/terminal/autotrading/tester_optimization). When being tested, the expert is passed on the modeled data one time what allows to estimate its profitability and effectiveness. For optimization purposes, the mechanical trading system is passed many times in order to find out such parameters of the expert at which its profitability is the highest.

The window can be called by the ["View — Strategy Tester" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_view) command, by pressing of accelerating keys of Ctrl+R, or the !["Strategy Tester" Window](/en/docs/mt4/terminal/img/tb_standard_strategy_tester.png ""Strategy Tester" Window") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).

![strategy_tester](/en/docs/mt4/terminal/img/strategy_tester.png)

There are several tabs in this window:

-   [Settings](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup) — settings of testing and optimization. The parameters of expert advisors, period to be tested, the method of bars modeling, and many other things, can be set up in this tab;
-   [Results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_results) — the results of trade operations performed by the expert, as well as the direction of balance changes;
-   [Graph](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_charts) — displaying of testing results in a graph;
-   [Report](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_report) — the detailed testing report. Many indications of testing and effectiveness of experts can be found here: the amount of bars modeled, the total profit, the most profitable and unprofitable positions, the amount of profit and loss trades, etc.;
-   [Journal](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_journal) — a log where all actions and internal messages of the expert are recorded;
-   [Optimization Results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_results) — information about every pass, including inputs, profitability, drawdowns, and other data;
-   [Optimization Graph](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_charts) — the results of expert optimization as a graph. Besides each pass profitability, the amount of profit and loss trades is displayed in the graph.

As in the ["Terminal" window](/en/docs/mt4/terminal/overview/terminal), some tabs of the "Tester" window are hidden if they are empty. So, initially, only the tabs of ["Settings"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup) and ["Journal"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_journal) can be seen in this window. The tabs of ["Results"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_results), ["Graph"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_charts), and ["Report"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_report), will only appear after an expert has been tested. After it has also been optimized, the tabs of ["Optimization Results"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_results) and ["Optimization Graph"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_charts) will appear. More detailed information about testing experts can be found in the [section of the same name](/en/docs/mt4/terminal/autotrading/tester).

[Journal](/en/docs/mt4/terminal/overview/terminal/terminal_journal)

[Setup](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup)