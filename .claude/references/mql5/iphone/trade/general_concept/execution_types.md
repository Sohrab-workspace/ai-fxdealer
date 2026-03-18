# Types of Execution

> Source: https://support.metaquotes.net/en/docs/mt5/iphone/trade/general_concept/execution_types

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
        -   [Getting Started](/en/docs/mt5/iphone/getting_started)
        -   [Quotes](/en/docs/mt5/iphone/quotes)
        -   [Depth of Market](/en/docs/mt5/iphone/depth_of_market)
        -   [Chart](/en/docs/mt5/iphone/chart)
        -   [Trade](/en/docs/mt5/iphone/trade)
            -   [Trading Principles](/en/docs/mt5/iphone/trade/general_concept)
                -   [Types of Orders](/en/docs/mt5/iphone/trade/general_concept/order_types)
                -   [Types of Execution](/en/docs/mt5/iphone/trade/general_concept/execution_types)
                -   [State of Orders](/en/docs/mt5/iphone/trade/general_concept/order_state)
                -   [Fill Policy](/en/docs/mt5/iphone/trade/general_concept/fill_policy)
            -   [Opening and Closing Positions](/en/docs/mt5/iphone/trade/open_positions)
            -   [Close By](/en/docs/mt5/iphone/trade/closeby)
            -   [Modifying a Position](/en/docs/mt5/iphone/trade/change_positions)
            -   [Placing Pending Orders](/en/docs/mt5/iphone/trade/pending_place)
            -   [Managing Pending Orders](/en/docs/mt5/iphone/trade/pending_change)
            -   [Bulk Operations](/en/docs/mt5/iphone/trade/bulk_operations)
            -   [Trading Report](/en/docs/mt5/iphone/trade/report)
        -   [History](/en/docs/mt5/iphone/history)
        -   [Accounts](/en/docs/mt5/iphone/settings_accounts)
        -   [Mailbox](/en/docs/mt5/iphone/settings_mail)
        -   [News](/en/docs/mt5/iphone/settings_news)
        -   [Messages](/en/docs/mt5/iphone/settings_messages)
        -   [Push Notifications](/en/docs/mt5/iphone/push)
        -   [Settings](/en/docs/mt5/iphone/settings)
        -   [iPad Version](/en/docs/mt5/iphone/ipad)
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

[MetaTrader 5](/en/docs/mt5)[iPhone/iPad](/en/docs/mt5/iphone)[Trade](/en/docs/mt5/iphone/trade)[Trading Principles](/en/docs/mt5/iphone/trade/general_concept)Types of Execution

# Types of Execution

There are four [order](/en/docs/mt5/iphone/trade/general_concept/order_types) execution modes in the MetaTrader 5 for iPhone mobile platform:

-   [Instant Execution](/en/docs/mt5/iphone/trade/open_positions#instant)  
    In this mode, the order is executed at the price offered to the broker. When sending an order to be executed, the platform sets the current prices in the order. If the broker accepts the prices, the order is executed. If not, the so-called "Requote" occurs: the broker returns prices, at which the order can be executed.
-   [Request Execution](/en/docs/mt5/iphone/trade/open_positions#request)  
    In this mode, the market order is executed at the price previously received from the broker. Prices for a certain market order are requested from the broker before the order is sent. After the prices have been received, order execution at the given price can be either confirmed or rejected.
-   [Market Execution](/en/docs/mt5/iphone/trade/open_positions#market)  
    In this order execution mode, a broker makes a decision about the order execution price without any additional discussion with the trader. Sending an order in such a mode means advance consent to its execution at this price.
-   [Exchange Execution](/en/docs/mt5/iphone/trade/open_positions#exchange)  
    In this mode, trade operations conducted in a platform are sent to an external trading system (exchange). Trade operations are executed at the prices of current market offers.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Execution mode for each security is defined by the brokerage company.</span></p></td></tr></tbody></table>

[Types of Orders](/en/docs/mt5/iphone/trade/general_concept/order_types)

[State of Orders](/en/docs/mt5/iphone/trade/general_concept/order_state)