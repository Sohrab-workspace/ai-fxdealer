# State of Orders

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/general_concept/order_state

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
        -   [Getting Started](/en/docs/mt5/android/getting_started)
        -   [Quotes](/en/docs/mt5/android/quotes)
        -   [Depth of Market](/en/docs/mt5/android/depth_of_market)
        -   [Charts](/en/docs/mt5/android/chart)
        -   [Trade](/en/docs/mt5/android/trade)
            -   [Trading Principles](/en/docs/mt5/android/trade/general_concept)
                -   [Types of Orders](/en/docs/mt5/android/trade/general_concept/order_types)
                -   [Types of Execution](/en/docs/mt5/android/trade/general_concept/execution_types)
                -   [State of Orders](/en/docs/mt5/android/trade/general_concept/order_state)
                -   [Fill Policy](/en/docs/mt5/android/trade/general_concept/fill_policy)
            -   [Opening and Closing Positions](/en/docs/mt5/android/trade/open_positions)
            -   [Close By](/en/docs/mt5/android/trade/closeby)
            -   [Modifying a Position](/en/docs/mt5/android/trade/change_positions)
            -   [Placing Pending Orders](/en/docs/mt5/android/trade/pending_place)
            -   [Managing Pending Orders](/en/docs/mt5/android/trade/pending_change)
            -   [Bulk Operations](/en/docs/mt5/android/trade/bulk_operations)
        -   [History](/en/docs/mt5/android/history)
        -   [Accounts](/en/docs/mt5/android/settings_accounts)
        -   [Mailbox](/en/docs/mt5/android/settings_mail)
        -   [News Event](/en/docs/mt5/android/settings_news)
        -   [Messages](/en/docs/mt5/android/messages)
        -   [Settings](/en/docs/mt5/android/settings)
        -   [Journal](/en/docs/mt5/android/settings_journal)
        -   [About](/en/docs/mt5/android/settings_about)
        -   [Push Notifications](/en/docs/mt5/android/push)
        -   [Tablet Version](/en/docs/mt5/android/tablet)
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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)[Trading Principles](/en/docs/mt5/android/trade/general_concept)State of Orders

# State of Orders

After an order is formed and sent to the trade server, it may pass the following stages:

-   Started — the order correctness has been checked, but it hasn't been yet accepted by a broker;
-   Placed — a dealer has accepted the order;
-   Partially filled — the order is filled partially;
-   Filled — the entire order is filled;
-   Canceled — the order is canceled by the client;
-   Rejected — the order is rejected by a dealer;
-   Expired — the order is canceled due to its expiration.

You can view the state of orders on tabs ["Trade"](/en/docs/mt5/android/trade#orders) and ["History"](/en/docs/mt5/android/history).

![State of Orders](/en/docs/mt5/android/img/order_state_scheme.png "State of Orders")

State of Orders

[Types of Execution](/en/docs/mt5/android/trade/general_concept/execution_types)

[Fill Policy](/en/docs/mt5/android/trade/general_concept/fill_policy)