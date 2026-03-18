# Results

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_results

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Tester](/en/docs/mt4/terminal/overview/strategy_tester)Results

# Results

The testing results are represented as a table in this tab.

![strategy_tester_results](/en/docs/mt4/terminal/img/strategy_tester_results.png)

Information about all trade operations performed within the testing process can be found here:

-   # — the sequence number of the trade operation;
-   Time — time of the trade operation;
-   Type — the type of operation performed (sell, buy, s/l, t/p, modify, close at stop, etc.);
-   Order — the ticket number of a trading position or a pending order (not to be mixed up with the trade operation number described above);
-   Size — the amount of lots that participated in the operation;
-   Price — the price of the security at the operation performing;
-   S/L — the Stop Loss order value. No entries in this field mean that no order was placed;
-   T/P — the Take Profit order value. No entries in this field mean that no order was placed;
-   Profit — profit/loss. The value of profit/loss will be entered only after positions have been closed;
-   Balance — the value of balance. This value will be entered only after positions have been closed.

Having clicked with the left mouse button on any column heading, one can sort all entries in the table in descending or ascending order. Using the "Copy" context menu command or accelerating keys of Ctrl+C, one can copy the selected lines of results to the clipboard for further use in other applications. If no line has been selected, the entire table will be copied to the clipboard. To copy the entire table to the clipboard, one can execute the "Copy all" command. The report about testing results can be stored in a HTML file on the hard disk. To do so, one has to execute the "Save as Report" context menu command. The "Set Date "From"" and "Set Date "To"" commands allow to specify the time range for testing. At that, the dates of the selected operations will be written in the fields of "Use date from:" and "Use date to:" in [testing settings](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup). This useful if there is a need to test an expert thoroughly or to optimize its parameters within this given range. You can enable or disable the grid and auto arrange the columns using the relevant context menu commands.

More details are given in the sections of ["Tester"](/en/docs/mt4/terminal/autotrading/tester) and ["Optimization"](/en/docs/mt4/terminal/autotrading/tester_optimization).

[Properties](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_properties)

[Graph](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_charts)