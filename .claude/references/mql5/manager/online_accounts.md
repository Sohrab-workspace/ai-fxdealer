# Online Accounts

> Source: https://support.metaquotes.net/en/docs/mt5/manager/online_accounts

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
            -   [Clients](/en/docs/mt5/manager/clients)
            -   [Online Accounts](/en/docs/mt5/manager/online_accounts)
            -   [Creation of Accounts](/en/docs/mt5/manager/account_create)
            -   [Importing Accounts](/en/docs/mt5/manager/account_import)
            -   [Preliminary Accounts](/en/docs/mt5/manager/preliminary_accounts)
            -   [Push Notifications, SMS and Mail](/en/docs/mt5/manager/communication)
            -   [Account Overview](/en/docs/mt5/manager/account_overview)
            -   [Exposure](/en/docs/mt5/manager/account_exposure)
            -   [Personal Data](/en/docs/mt5/manager/account_personal)
            -   [Account Trading Settings](/en/docs/mt5/manager/account_tradeaccount)
            -   [Balance Operations](/en/docs/mt5/manager/account_balance)
            -   [Trading Operations](/en/docs/mt5/manager/account_trading)
            -   [Account History](/en/docs/mt5/manager/account_history)
            -   [Security and Certificates](/en/docs/mt5/manager/account_security)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Online Accounts

# Online Accounts

This section contains accounts currently connected to the trade server. For convenience, each type of connection is indicated by a separate icon: ![Connecting by the desktop terminal](/en/docs/mt5/manager/img/desktop_connection_icon.png "Connecting by the desktop terminal") — desktop client terminal, ![Connecting by the Administrator terminal](/en/docs/mt5/manager/img/admin_connection_icon.png "Connecting by the Administrator terminal") — Administrator terminal, ![Connecting by the Manager terminal](/en/docs/mt5/manager/img/about_icon.png "Connecting by the Manager terminal") — Manager terminal, ![Connecting by the mobile terminal for Android](/en/docs/mt5/manager/img/android_connection_icon.png "Connecting by the mobile terminal for Android") — mobile terminal for Android, ![Signal provider](/en/docs/mt5/manager/img/signal_icon.png "Signal provider") — signal provider (connection to the account via a signal server), etc. If the user is connected to the same account from different devices/terminals, all connections will be shown as separate entries.

![Data on the accounts currently connected to the trade server](/en/docs/mt5/manager/img/online.png "Data on the accounts currently connected to the trade server")

Apart from account data, here you can view technical details on their connection. In the list of accounts, you can see an IP address a client is connected from, or a domain name if the Enable DNS Lookup option is enabled in the context menu.

For more detailed information, click Technical Details... in the context menu, as shown above. Next, enter a network command to execute in the Command field. You can specify your own command or choose one of the commonly used ones: "ping", "tracert" or "whois". After clicking Run, the result is shown below.

To forcibly disconnect a client from the server, click Drop in the context menu. After the connection is dropped, the client terminals attempt to reconnect automatically.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The Online Users tab can be hidden by pressing "Hide online users" in the <a href="/en/docs/mt5/manager/settings#online" class="topiclink">options</a> of the Manager terminal. This reduces the load on the Manager terminal and saves network traffic.</span></p></td></tr></tbody></table>

[Clients](/en/docs/mt5/manager/clients)

[Creation of Accounts](/en/docs/mt5/manager/account_create)