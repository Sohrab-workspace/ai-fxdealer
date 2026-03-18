# Connect to an Account

> Source: https://support.metaquotes.net/en/docs/mt5/client/authorization

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
            -   [User Interface](/en/docs/mt5/client/interface)
            -   [Open an Account](/en/docs/mt5/client/acc_open)
            -   [Connect to an Account](/en/docs/mt5/client/authorization)
            -   [Deposits and withdrawals](/en/docs/mt5/client/payments)
            -   [Platform Settings](/en/docs/mt5/client/settings)
            -   [For Advanced Users](/en/docs/mt5/client/start_advanced)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)Connect to an Account

# Connect to an Account

To start working with a trading account, you need to connect to it using a login (account number) and password. Two types of account access are available in the trading platform: master and investor. Logging in using the master password gives full rights for working with the account. Investor authorization allows you to see the account status, analyze prices, and work with your own Expert Advisors, but not trade. The Investor access is a convenient tool for demonstrating the trading process on the account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The trading platform provides the option of <a href="/en/docs/mt5/client/start_advanced/extended_authorization" class="topiclink">extended authentication</a> using SSL certificates.</span></p></td></tr></tbody></table>

Click "![Login](/en/docs/mt5/client/img/login_icon.png "Login") Login to Trade Account" in the [File](/en/docs/mt5/client/interface) menu or in the [Navigator](/en/docs/mt5/client/interface).

![Click Login to Trade Account and specify your login and password](/en/docs/mt5/client/img/authorization.png "Click Login to Trade Account and specify your login and password")

Specify the following data in this window:

-   Login — the number of the account used for connection.
-   Password — the master or investor password for the account.
-   Server — server to connect to. Also you can indicate a server manually. Enter its IP address and port number as \[server number\]:\[port number\], for example, 192.168.0.1:443.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><a name="save" class="hmanchor"></a><span class="f_tableatten">Enable the "Save password" option, and the next time you start the platform, the last used account will be automatically connected to the server. Option "Keep personal settings and data at startup" in the <a href="/en/docs/mt5/client/settings#keep_personal" class="topiclink">platform settings</a> performs the same action.</span></p></td></tr></tbody></table>

After specifying all the details, click "OK" to connect.

## Forced Change of Password [#](authorization#change_password)

Upon authorization, you may be requested to change the master password of the account. Forced password change can be enabled by the trade server administrator. The mechanism of forced change of the master password, when you first connect or on a regular basis, increases safety.

![Forced password change increased safety](/en/docs/mt5/client/img/change_master_password.png "Forced password change increased safety")

Enter the new password, and then enter it again to confirm. The password must meet the following requirements:

-   It cannot be shorter than the length required in the password change dialog.

-   It must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj.

-   It must not be the same as the previous password.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the master password is changed forcedly, the investor password of the account is also reset. A new investor password can be set in the <a href="/en/docs/mt5/client/settings#password" class="topiclink">platform settings</a>.</span></p></td></tr></tbody></table>

[Open an Account](/en/docs/mt5/client/acc_open)

[Deposits and withdrawals](/en/docs/mt5/client/payments)