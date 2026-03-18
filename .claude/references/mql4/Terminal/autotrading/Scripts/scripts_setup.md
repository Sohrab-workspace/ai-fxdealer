# Setup

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/scripts/scripts_setup

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Scripts](/en/docs/mt4/terminal/autotrading/scripts)Setup

# Setup

Before starting to use scripts, one has to set them up. Working parameters common for all scripts are stated in the [terminal settings window](/en/docs/mt4/terminal/setup/setup_experts). This window can be opened by the ["Tools — Options" menu](/en/docs/mt4/terminal/overview/main_menu) command or by pressing of accelerating keys of Ctrl+O. To set up script parameters, one has to open the "Expert Advisors" tab.

![options_experts](/en/docs/mt4/terminal/img/options_experts.png)

Only five options influence the operation of scripts:

-   Allow automated trading — this option allows to enable or disable the performing of trade operations by [Expert Advisors](/en/docs/mt4/terminal/autotrading/experts) and [scripts](/en/docs/mt4/terminal/autotrading/scripts). If it is disabled, scripts and Expert Advisors will work, but they won't be able to trade. This limitation can be useful for testing the analytical capacity of an Expert Advisor in the real-time mode (not to be confused with testing of Expert Advisors on history data). Automated trading can also be allowed or disabled using ![AutoTrading](/en/docs/mt4/terminal/img/autotrade_button.png "AutoTrading") button on the toolbar.

-   Allow DLL imports  
    To have their functionalities enlarged, scripts can use DLLs. If this option is enabled, the libraries can be used without any limitations. If this option is disabled, no script will be able to use any external DLLs.

-   Allow WebRequest for listed URL  
    The WebRequest() function in MQL4 is used for receiving and sending information to websites using GET and POST requests. To allow an MQL4 application to send such requests, enable this option and manually explicitly specify the URLs of trusted websites. For security reasons, the option is disabled on default.

[Creation](/en/docs/mt4/terminal/autotrading/scripts/scripts_create)

[Launch](/en/docs/mt4/terminal/autotrading/scripts/scripts_launch)