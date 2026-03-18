# Connecting to the Server

> Source: https://support.metaquotes.net/en/docs/mt5/manager/connect

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)Connecting to the Server

# Connecting to the Server

Connect to the server to commence work. To do this, select "![Connect](/en/docs/mt5/manager/img/connect_icon.png "Connect") Connect" in the [File](/en/docs/mt5/manager/main_menu#file) menu or in the [toolbar](/en/docs/mt5/manager/toolbar). After that, the authorization window will appear:

![Authentication](/en/docs/mt5/manager/img/authorization.png "Authentication")

The following data is specified in the login window:

-   Login — manager's account (login) used to connect to the server. If no such account is created on the server, connection is not possible.
-   Password — manager's password.
-   Server — server you are going to connect to. You can select any of the servers previously used in the terminal or specify an address and a port of another server, separated by a colon.

Enable the "Save password" option, and the next time you start the terminal, the last used account will be automatically connected to the server. Option "Keep personal settings and data at startup" in the [terminal settings](/en/docs/mt5/manager/settings#keep_personal) performs the same action.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">If <a href="/en/docs/mt5/manager/beginning_advanced/extended_authorization" class="topiclink">extended authentication</a> mode is enabled, a certificate and a password are required for connection.</span></li><li class="p_tableatten"><span class="f_tableatten">If connection to servers is performed via a proxy server, set its parameters in the <a href="/en/docs/mt5/manager/settings#proxy" class="topiclink">terminal settings</a>.</span></li></ul></td></tr></tbody></table>

Upon a successful authentication, the connection indicator ![Connected](/en/docs/mt5/manager/img/status_bar_connected.png "Connected") will appear in [the status bar](/en/docs/mt5/manager/status_bar) and two entries will appear in the [journal](/en/docs/mt5/manager/toolbox#journal):

1.  'login number' authorized on 'server name';
2.  'login number' manager synchronized with 'server name'.

After a successful authorization, you can begin to work with the server. If any problems occur while connecting, and you do not get one of the above messages, check all the connection settings, specified address and port of the server.

## Forced change of password [#](connect#change_password)

Upon authorization, you may be requested to change the master password of the account. Forced password change can be enabled in the trading server group or [account settings](/en/docs/mt5/manager/account_tradeaccount#change_password). The mechanism of forced change of the master password, when you first connect or on a regular basis, increases safety.

![Changing the master password](/en/docs/mt5/manager/img/change_master_password.png "Changing the master password")

Enter the new password, and then enter it again to confirm. The password should meet the following requirements:

-   It must be no shorter than the length requirement displayed in the password change dialog. The minimum password length is determined by group settings on the server, while the lowest possible value is 8 characters. The maximum length is 16 characters.

-   It must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj.

-   It should not be the same as the previous password.

[Terminal Start](/en/docs/mt5/manager/start)

[Terminal Settings](/en/docs/mt5/manager/settings)