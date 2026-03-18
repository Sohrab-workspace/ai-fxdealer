# Properties

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_properties

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Tester](/en/docs/mt4/terminal/overview/strategy_tester)Properties

# Properties

Parameters of the virtual account and the expert advisor under test can be set up in this window.

![strategy_tester_settings_expert_properties](/en/docs/mt4/terminal/img/strategy_tester_settings_expert_properties.png)

These data will later be used for testing or optimization of the expert parameters. There are three tabs in the window:

-   Testing — Parameters common for both testing and optimizations are placed in this tab. These are volume and currency of initial deposit that are given in the fields of the corresponding names. Types of positions to be opened at testing can be selected, as well: "Only Long" — open only long positions; "Only Short" — only short ones; "Long and Short" — open both types of positions. Whatever expert mechanisms are used, they will open positions only as set here. One can include an optimization genetic algorithm and select a parameter to be optimized (maximization by the balance value, the profit factor, expected payoff, or minimization by the maximal drawdown value or drawdown percent).
-   Inputs — the list of all inputs is given here as a table. Inputs are variables that influence the expert work and can be changed directly from the client terminal. The amount thereof can vary from expert to expert. The current data to be used at [testing an expert](/en/docs/mt4/terminal/autotrading/tester) will be written in the "Value" field. Data to be written in the fields of "Start", "Step" and "Stop" do not influence the expert testing, and are only used for its [optimization](/en/docs/mt4/terminal/autotrading/tester_optimization). Initial value of the variable, step of change, and final value are written in this field. At optimization, expert with parameters within the range between initial and final values will be passed consecutively. Checking from the right of the variable names allows to include the parameter into optimization process. If a variable has not been checked, it will not participate in optimization. Its value will not be changed in the optimization process, and the parameter written in the "Value" field will be used.  
       
    There is an opportunity to download a set of inputs already saved before (including the values of "Start", "Step", and "Stop"). This can be done by pressing of the "Load" button and after the preliminarily saved set of inputs has been selected. The actual set of external variables can be saved by pressing of the button of the same name.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: It is recommended to include only necessary variables into optimization process. If too many variables are included into it, the amount of passes and total optimization time will rapidly increase.</span></p></td></tr></tbody></table>

-   Optimization — this tab allows to manage optimization limits. If the real values meet those required in this tab, the current pass will be stopped and the next pass will start. Parameters limiting testing at optimization of the expert are:

-   -   Balance minimum — minimum balance value in the deposit currency;
    -   Profit maximum — maximal profit in the deposit currency;
    -   Minimal margin level, % — minimal level of margin in per cents;
    -   Maximal drawdown, % — maximal drawdown in per cents;
    -   Consecutive loss — maximal total loss in one series of trades. A loss series is a certain amount of consecutive loss trades;
    -   Consecutive loss trades — maximal amount of loss trades in one series;
    -   Consecutive win — maximal total win in one series of trades. A win series is a certain amount of consecutive win trades;
    -   Consecutive win trades — maximal amount of win trades in one series.

More details are given in the sections of ["testing Expert Advisors"](/en/docs/mt4/terminal/autotrading/tester) and ["Optimization"](/en/docs/mt4/terminal/autotrading/tester_optimization).

[Setup](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup)

[Results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_results)