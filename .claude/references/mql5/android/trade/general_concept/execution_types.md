# Types of Execution

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/general_concept/execution_types

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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)[Trading Principles](/en/docs/mt5/android/trade/general_concept)Types of Execution

# Types of Execution

There are four [order](/en/docs/mt5/android/trade/general_concept/order_types) execution modes in the MetaTrader 5 for Android mobile platform:

-   [Instant Execution](/en/docs/mt5/android/trade/open_positions/position_instant)  
    In this mode, the order is executed at the price offered to the broker. When sending an order to be executed, the platform automatically adds the current prices to the order. If the broker accepts the prices, the order is executed. If not, the so-called "Requote" occurs: the broker returns prices, at which the order can be executed.
-   [Request Execution](/en/docs/mt5/android/trade/open_positions/position_request)  
    In this mode, the market order is executed at the price previously received from the broker. Prices for a certain market order are requested from the broker before the order is sent. After the prices have been received, order execution at the given price can be either confirmed or rejected.
-   [Market Execution](/en/docs/mt5/android/trade/open_positions/position_market)  
    In this order execution mode, a broker makes a decision about the order execution price without any additional discussion with the trader. Sending an order in such a mode means advance consent to its execution at this price.
-   [Exchange Execution](/en/docs/mt5/android/trade/open_positions/position_exchange)  
    In this mode, trade operations conducted in the platform are sent to an external trading system (exchange). Trade operations are executed at the prices of current market offers.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Execution mode for each security is defined by the brokerage company.</span></p></td></tr></tbody></table>

[Types of Orders](/en/docs/mt5/android/trade/general_concept/order_types)

[State of Orders](/en/docs/mt5/android/trade/general_concept/order_state)