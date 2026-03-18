# Queue of Trade Requests

> Source: https://support.metaquotes.net/en/docs/mt5/manager/trade_queue

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
            -   [Dealing](/en/docs/mt5/manager/dealing)
            -   [Accounts with Margin Call/Stop Out](/en/docs/mt5/manager/margin_calls)
            -   [Queue of Trade Requests](/en/docs/mt5/manager/trade_queue)
            -   [Quoting and Symbol Management](/en/docs/mt5/manager/quotes_symbols)
            -   [Summary Positions and Coverage](/en/docs/mt5/manager/summary_positions)
            -   [Exposure](/en/docs/mt5/manager/exposure)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)Queue of Trade Requests

# Queue of Trade Requests

A manager can view the list of trade requests waiting to be processed. Also, when receiving a new client's request, the manager can see the history of the client's previous requests. A separate window is provided for that in the Manager terminal. To open it, click "![Queue](/en/docs/mt5/manager/img/queue_icon.png "Queue") Queue" in the [View](/en/docs/mt5/manager/main_menu#view) menu or on the [toolbar](/en/docs/mt5/manager/toolbar).

![Requests](/en/docs/mt5/manager/img/queue.png "Requests")

All requests pending processing are shown here. They are listed in the order they were received: from older to newer ones. The request that is currently processed by a dealer is displayed on a red background.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Requests start coming to the terminal as soon as a manager <a href="/en/docs/mt5/manager/dealing" class="topiclink">connects in the dealing mode</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">If a manager has Supervisor permission (granted in the Administrator terminal) while not connected as a dealer, then in this window, they see the entire queue of requests coming from client groups available to them.</span></li></ul></td></tr></tbody></table>

The History tab displays the history of requests of the client, whose request is currently being processed by a dealer. This allows monitoring the client's trading activity. If a request has the red background, it means it was rejected by the dealer.

In order to automatically switch to the History tab at the beginning of request processing, enable Track Requests option in the context menu. To see the [client's details](/en/docs/mt5/manager/account_overview), double-click the account or the request on any of the tabs.

[Accounts with Margin Call/Stop Out](/en/docs/mt5/manager/margin_calls)

[Quoting and Symbol Management](/en/docs/mt5/manager/quotes_symbols)