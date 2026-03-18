# Scripts

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/scripts

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
                -   [Creation](/en/docs/mt4/terminal/autotrading/scripts/scripts_create)
                -   [Setup](/en/docs/mt4/terminal/autotrading/scripts/scripts_setup)
                -   [Launch](/en/docs/mt4/terminal/autotrading/scripts/scripts_launch)
                -   [Shutdown](/en/docs/mt4/terminal/autotrading/scripts/scripts_remove)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)Scripts

# Scripts

Script is a program written in [MetaQuotes Language 4 (MQL4)](/en/docs/mt4/terminal/autotrading/mql4) and intended for a single performing of any actions. A script can fulfil both analytical and trading functions. Unlike experts, scripts are executed on request, not by ticks. In other words, where an expert works almost continuously, a script, having completed the function once, stops functioning by itself.

Working with scripts means:

-   [Creation of a Script](/en/docs/mt4/terminal/autotrading/scripts/scripts_create)  
    The built-in ["MetaEditor"](/en/docs/mt4/terminal/autotrading/metaeditor) is used to create and compile a script. It is a constituent of the client terminal and represents a convenient development environment of MQL4 programs.
-   [Script Setup](/en/docs/mt4/terminal/autotrading/scripts/scripts_create)  
    One has to set up scripts first before using them. Working parameters common for all scripts are defined in the [client terminal setup window](/en/docs/mt4/terminal/setup/setup_experts). Every script has its own settings, as well.
-   [Launching of a Script](/en/docs/mt4/terminal/autotrading/scripts/scripts_create)  
    To launch a script, one has to attach it to the chart. The script algorithm will be launched immediately after that.
-   [Deletion of a Script](/en/docs/mt4/terminal/autotrading/scripts/scripts_create)  
    The script completes its working after it has been deleted from the chart.

[Remove](/en/docs/mt4/terminal/autotrading/custom_indicators/custom_indicators_remove)

[Creation](/en/docs/mt4/terminal/autotrading/scripts/scripts_create)