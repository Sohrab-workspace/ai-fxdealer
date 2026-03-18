# Results

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/tester_optimization/tester_optimization_results

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
                -   [Setup](/en/docs/mt4/terminal/autotrading/tester_optimization/tester_optimization_parameters)
                -   [Results](/en/docs/mt4/terminal/autotrading/tester_optimization/tester_optimization_results)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Expert Optimization](/en/docs/mt4/terminal/autotrading/tester_optimization)Results

# Results

After optimization has been completed, its results can be viewed in the tabs of "Optimization Results" and "Optimization Graph".

## Optimization Results

![strategy_tester_optimization_result](/en/docs/mt4/terminal/img/strategy_tester_optimization_result.png)

Unlike testing, optimization is supposed to perform many passes of the mechanical trading system (MTS) with different inputs. This is aimed at determining of such expert parameters at which its efficiency will be the highest. To optimize an expert, one has to flag "Optimization" in the [testing settings tab](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup) and press "Start". After that, two new tabs will appear in the window: "Optimization Results" and "Optimization Graph".

There are not all operations listed in the tab of "Optimization Results", unlike that of [testing results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_report), but only final reports about each pass. The entire information is represented as a table with the following fields:

-   Pass — the pass number;
-   Profit — the pure profit (gross profit minus gross loss);
-   Total trades — the total amount of open trade positions;
-   Profit factor — ratio between gross profit and gross loss in per cents. One means that these values are equal;
-   Expected payoff — mathematical expectation of win. This value to be calculated statistically represents the average profit/loss factor of one trade. It can also be considered to represent the expected profit/loss factor of the next trade;
-   Drawdown $ — the largest drawdown related to the initial deposit, in the deposit currency;
-   Drawdown % — the largest drawdown related to the initial deposit, in per cents;
-   Inputs — changeable values of inputs at each pass.

Having clicked with the left mouse button on any column header, one can sort out all records in the table in increasing or decreasing order. At execution of the "Set Input Parameters" context menu command, the data of the selected pass will be written as the expert basic inputs ([expert properties window, "Inputs"](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_properties) tab). At that, it will be switched to the ["Settings" tab](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup), and the optimization will be disabled. Having pressed the "Start" button, one can start to test the expert with the selected inputs. Double click with the left mouse button on the pass line in the Optimization Results tab allows to do the same. Using the "Copy" context menu command or accelerating keys of Ctrl+C, one can copy the selected results lines to the clipboard for further use in other applications. If no line has been selected, the entire table will be copied to the clipboard. To do the same, one can also execute the "Copy All" command. The report about optimization results can be saved on the hard disk as an HTML file. To do so, one has to execute the "Copy As Report" context menu command. Other context menu commands allow to set up representation of results:

-   Skip Useless Results — show/hide the results of unprofitable passes;
-   Show Input Parameters — show/hide the "Inputs" column;
-   Auto Arrange — arrange the column sizes automatically when the window size has been changed.  
    The same action can be done by pressing of A;
-   Grid — show/hide grid to separate the columns.  
    The same actions can be done by pressing of G.

## Optimization Graph

![strategy_tester_optimization_graph](/en/docs/mt4/terminal/img/strategy_tester_optimization_graph.png)

The graph of profit of all passes is drawn automatically in the "Optimization Graph" tab. The graph allows to estimate the profitability of the use of different inputs combinations visually. The graph representing the amount of profitable (green color) and unprofitable (red color) trades at each pass is given in the bottom of the window, as well.

Double click with the left mouse button on any point of the graph switches to the ["Optimization Results" tab](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_results) and selects the corresponding pass. Using the "Copy" context menu command or accelerating keys of Ctrl+C, one can copy the graph to the clipboard to be used in other applications. The graph can also be stored on the hard disk as a GIF file. To do so, one has to execute the "Save as Picture" context menu command or press accelerating keys of Ctrl+S.

[Setup](/en/docs/mt4/terminal/autotrading/tester_optimization/tester_optimization_parameters)

[Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)