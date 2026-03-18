# Expert Advisors

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/setup_experts

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
            -   [Server](/en/docs/mt4/terminal/setup/setup_server)
            -   [Charts](/en/docs/mt4/terminal/setup/setup_charts)
            -   [Objects](/en/docs/mt4/terminal/setup/setup_objects)
            -   [Trade](/en/docs/mt4/terminal/setup/setup_trade)
            -   [Expert Advisors](/en/docs/mt4/terminal/setup/setup_experts)
            -   [Notifications](/en/docs/mt4/terminal/setup/settings_notifications)
            -   [Email](/en/docs/mt4/terminal/setup/setup_email)
            -   [FTP](/en/docs/mt4/terminal/setup/setup_publisher)
            -   [Events](/en/docs/mt4/terminal/setup/setup_events)
            -   [Community](/en/docs/mt4/terminal/setup/settings_mql5community)
            -   [Signals](/en/docs/mt4/terminal/setup/settings_signals)
        -   [User Interface](/en/docs/mt4/terminal/overview)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)Expert Advisors

# Expert Advisors

Settings of working with Expert Advisors are grouped in this tab.

![options_experts](/en/docs/mt4/terminal/img/options_experts.png)

[Expert Advisors](/en/docs/mt4/terminal/autotrading/experts) in the terminal are programs written in [MetaQuotes Language 4](/en/docs/mt4/terminal/autotrading/mql4) and allowing to analyze and trade in the automatic mode (auto trading). The description of how to create and use experts is given in the ["Auto Trading"](/en/docs/mt4/terminal/autotrading) section. The given section describes only settings common for all experts:

-   Allow Auto Trading — this option allows to enable or disable the performing of trade operations by [Expert Advisors](/en/docs/mt4/terminal/autotrading/experts) and [scripts](/en/docs/mt4/terminal/autotrading/scripts). If it is disabled, scripts and Expert Advisors will work, but they won't be able to trade. This limitation can be useful for testing the analytical capacity of an Expert Advisor in the real-time mode (not to be confused with testing of Expert Advisors on history data). Automated trading can also be allowed or disabled using ![AutoTrading](/en/docs/mt4/terminal/img/autotrade_button.png "AutoTrading") button on the toolbar.  
    The option enables/disables autotrading for the entire terminal. If you disable it, no Expert Advisor will be allowed to trade, even if you enable autotrading in the [EA settings](/en/docs/mt4/terminal/autotrading/experts/experts_launch). If you enable it, the Expert Advisors will be allowed to trade, if autotrading is enabled in their settings.

-   Disable Auto Trading when the account has been changed — this option represents a protective mechanism disabling trading by Expert Advisors and scripts when the account is changed. It is useful, for example, when one changes demo account for a real one.
-   Disable Auto Trading when the profile has been changed — a large amount of information about the current settings of all charts in the workspace is stored in [profiles](/en/docs/mt4/terminal/chart_management/templates). Particularly, profiles contain information about Expert Advisors attached. [Expert Advisors](/en/docs/mt4/terminal/autotrading/experts) included into the profile will start working when a new tick incomes. Having enabled this option, one can hinder the trading by the Expert Advisors launching when the profile has been changed.
-   Disable Auto Trading when the charts symbol or period has been changed — if this option is enabled, then when the period or symbol of a chart is changed the expert advisor, which is attached to it, will be automatically prohibited to perform trade operations.

-   Allow DLL imports (potentially dangerous, enable only for trusted applications)  
    To enlarge their functionality, expert advisors can use DLLs (dynamic-links libraries). If it is enabled, such libraries can be used without any limitations. If this option is disabled, no expert can use external DLLs. It is recommended to disable import when working with unknown experts.
-   Allow WebRequest for listed URL  
    The WebRequest() function in MQL4 is used for receiving and sending information to websites using GET and POST requests. To allow an MQL4 application to send such requests, enable this option and manually explicitly specify the URLs of trusted websites. For security reasons, the option is disabled on default.  
    To delete an address from the trusted list, select it and press "Delete" button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Values of options named "Allow Auto trading", "Allow DLL imports (potentially dangerous, enable only for trusted applications)" and "Allow WebRequest for listed URL" specified in this window are default parameters for MQL4 programs newly attached. They do not influence the operation of expert advisors, custom indicators and scripts already running.</span></p></td></tr></tbody></table>

[Trade](/en/docs/mt4/terminal/setup/setup_trade)

[Notifications](/en/docs/mt4/terminal/setup/settings_notifications)