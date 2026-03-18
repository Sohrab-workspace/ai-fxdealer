# Expert Optimization

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/tester_optimization

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)Expert Optimization

# Expert Optimization

Optimization represents successive passes of the same expert advisor with different inputs on the same data. At that, such parameters can be sorted out at which the expert efficiency will be maximal. Terminal possesses some built-in means that allow to automate this process. To optimize an expert, one has to flag the option of the same name in the ["Tester" window](/en/docs/mt4/terminal/autotrading/tester_optimization/tester_optimization_parameters) and press the "Start" button.

### New strategy development features

The fifth generation platform offers the new multi-threaded tester for the algorithmic trading. The tester allows using all CPU cores available on the local PC. Testing and optimization are carried out using special computing agents that are installed as services on the user's computer. Agents work independently and allow parallel processing of optimization passes.

An unlimited number of remote agents can be connected to the Strategy Tester. Besides, you can use [MQL5 Cloud Network](https://www.metatrader5.com/en/terminal/help/mql5cloud/mql5cloud_use) combining thousands of agents around the world. It allows you to check a huge amount of input parameter options in about half an hour, while a conventional tester would require thousands of hours of calculations to fulfill the same task.

![optimization_agents_cloud](/en/docs/mt4/terminal/img/optimization_agents_cloud.png)

In order to find the optimal parameters for your strategy tester, you can select one of the six standard criteria or set a custom one. You can also perform optimization with a forward test. To do this, select the best passes on the backtest period and run them on a forward period the EA has not traded on yet. Together with the random delay mode, the forward optimization allows finding the most stable parameters discarding inefficient ones.

For convenient analysis of obtained optimization results, the new platform offers multiple reports, 3D optimization graph and MQL5 language tools presenting data in any convenient form. Simply try the new tester and [visualize your trading strategy](https://www.mql5.com/en/articles/403).

[Indicator Testing](/en/docs/mt4/terminal/autotrading/tester_indicator)

[Setup](/en/docs/mt4/terminal/autotrading/tester_optimization/tester_optimization_parameters)