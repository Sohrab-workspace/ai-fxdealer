# Authorization

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/userguide/authorization

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
            -   [Install Terminal](/en/docs/mt4/terminal/userguide/installation)
            -   [Install on Mac OS](/en/docs/mt4/terminal/userguide/install_mac)
            -   [Install on Linux](/en/docs/mt4/terminal/userguide/install_linux)
            -   [Terminal Start and Data Structure](/en/docs/mt4/terminal/userguide/start_comm)
            -   [Opening of Accounts](/en/docs/mt4/terminal/userguide/open_an_account)
            -   [Authorization](/en/docs/mt4/terminal/userguide/authorization)
            -   [OTP](/en/docs/mt4/terminal/userguide/otp)
            -   [Live Update](/en/docs/mt4/terminal/userguide/liveupdate)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Getting Started](/en/docs/mt4/terminal/userguide)Authorization

# Authorization

Authorization is connection of terminal to the server through a login and a password. It allows to manage a trading account. Two accesses to the account are possible in the terminal: a normal password and an investor password. Being authorized with the standard password, one gets full rights for working with the terminal. Investor authorization allows you to see the account status, analyze prices, and work with your own Expert Advisors, but not trade. Automated trading by Expert Advisors is not allowed either. Investor access is a convenient tool used for demonstration of trading at the account.

To be authorized, it is necessary to execute the "![login_icon](/en/docs/mt4/terminal/img/login_icon.png)Login" command of the context menu of the account (context menu is called by clicking with the right mouse button at the account number) in the ["Navigator" window](/en/docs/mt4/terminal/overview/navigator) or ["File" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file). Then, the account number, one of its passwords (standard or investor) should be given in the appearing window, and a server should be chosen. After all data have been specified, the "Login" button should be pressed.

![authorization](/en/docs/mt4/terminal/img/authorization.png)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If the "Keep personal settings and data at startup", option is enabled, the latest account used will be automatically authorized at the next start of the terminal. The "Keep personal settings and data at startup" option in <a href="/en/docs/mt4/terminal/setup/setup_server" class="topiclink">terminal settings</a> carries out the same action. If you disable this option, the information about previously used account and saved passwords will be deleted upon the next restart of the terminal.</span></p></td></tr></tbody></table>

[Opening of Accounts](/en/docs/mt4/terminal/userguide/open_an_account)

[OTP](/en/docs/mt4/terminal/userguide/otp)