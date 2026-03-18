# Optimization Results

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_results

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Tester](/en/docs/mt4/terminal/overview/strategy_tester)Optimization Results

# Optimization Results

Unlike testing, optimization is supposed to perform many passes for mechanical trading system (MTS) with different inputs.

![strategy_tester_optimization_result](/en/docs/mt4/terminal/img/strategy_tester_optimization_result.png)

This is done to determine the expert parameters with which its profitability is the highest. To optimize, one has to flag the "Optimization" field in the [tab of tester setup](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup) and press the "Start" button. After that, two new tabs will appear in the window: "Optimization Results" and "Optimization Graph".

The "Optimization Results" tab, unlike [Tester Report](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_report), publishes not the entire list of trades, but final reports of each pass. All data are represented in the table with the following fields:

-   Pass — the pass number;
-   Profit — net profit (gross profit minus gross loss);
-   Total trades — the total amount of open trade positions;
-   Profit factor — the ratio between total profit and total loss in per cents. One means that total profit is equal to total loss;
-   Expected Payoff — mathematical expectation of win. This statistically calculable figure shows average profitability/unprofitableness of one trade. It is considered to show the estimate profitability/unprofitableness of the next trade;
-   Drawdown $ — maximum drawdown relating to the initial deposit in the deposit currency;
-   Drawdown % — maximum drawdown relating to the initial deposit in per cents;
-   Inputs — dynamic values of inputs at each pass.

After having clicked with the left mouse button on the heading of any column, one can sort all entries of the table in decreasing or increasing order. Data of the selected pass will be entered as basic inputs of the expert ([expert properties window, the "Inputs" tab](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_properties)) after the "Set Input Parameters" context menu command has been executed. At that, the program switches to the ["Settings" tab](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup), and optimization mode will be stopped. Having pressed the "Start" button, one can test the expert advisor having the pre-defined input parameters and variables. The same action can be done by a double click with the left mouse button on the pass line in the tab of optimization results. Using the "Copy" context menu command or accelerating keys of Ctrl+C, one can copy the selected results to the clipboard for further use in other applications. If no line has been selected, the entire table will be copied to the clipboard. The "Copy All" command can be used to copy the entire table to the clipboard, as well. The report of the optimization results can also be stored in HTML format on the hard disk. To do so, one has to execute the "Save as Report" context menu command. Other context menu commands allow to set up displaying of results:

-   Skip Useless Results — show/hide the results of loss passes;
-   Show Input Parameters — show/hide the "Inputs" column;
-   Auto Arrange — automatic setting of column sizes when the window size changes.  
    The same action can be done by pressing of A;
-   Grid — show/hide grid to separate columns.  
    The same action can be done by pressing of G.

More details are given in the sections of ["testing Expert Advisors"](/en/docs/mt4/terminal/autotrading/tester) and ["Optimization"](/en/docs/mt4/terminal/autotrading/tester_optimization).

[Journal](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_journal)

[Optimization Graph](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_charts)