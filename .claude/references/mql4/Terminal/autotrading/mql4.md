# MQL4

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/mql4

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)MQL4

# MQL4

MetaQuotes Language 4 (MQL4) is the language for programming of trade strategies built in the client terminal. It allows to write custom expert advisors that automate trade processes and ideally suit for implementation of traders' own strategies. Moreover, traders' own custom indicators, scripts and DLL's can be created in MQL4.

Syntax of MQL4 is quite similar to that of C language. A large amount of functions necessary to analyze quotes, manage positions, call technical indicators, and others, are included in MQL4. The [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor), an editor for expert advisors, is used for writing the source code of programs. The MetaQuotes Language Dictionary that contains descriptions of all language constructions and functions is built in the editor.

Programs written in MQL4 are different in tasks and properties:

-   [Expert Advisor](/en/docs/mt4/terminal/autotrading/experts) is a mechanical trading system (MTS) to be run when a new tick incomes. It can work not only in the mode alerts, but also perform trade operations independently. Terminal allows to [test trading strategies](/en/docs/mt4/terminal/autotrading/tester) on history data in order to detect the expert features under different market conditions;
-   [Custom Indicator](/en/docs/mt4/terminal/autotrading/custom_indicators) is a technical indicator written individually. Custom indicators are used only for analyzing of price changes;
-   [Script](/en/docs/mt4/terminal/autotrading/scripts) is a program that is intended for a single execution of some actions. Unlike experts, scripts are launched not tick by tick, but on a command.

[Where to Get Trade Robots and Indicators](/en/docs/mt4/terminal/autotrading/charts_analysis_get_indicators)

[MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor)