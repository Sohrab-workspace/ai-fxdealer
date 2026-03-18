# Order Types

> Source: https://support.metaquotes.net/en/docs/mt4/multiterminal/trading/ug_orders

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
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
        -   [Getting Started](/en/docs/mt4/multiterminal/getting_started)
        -   [Client Accounts](/en/docs/mt4/multiterminal/accounts)
        -   [Trading](/en/docs/mt4/multiterminal/trading)
            -   [Order Types](/en/docs/mt4/multiterminal/trading/ug_orders)
            -   [Types of Execution](/en/docs/mt4/multiterminal/trading/ug_execution)
            -   [Trade Orders](/en/docs/mt4/multiterminal/trading/trade_orders)
        -   [Analytics](/en/docs/mt4/multiterminal/analytics)
        -   [User Interface](/en/docs/mt4/multiterminal/user_interface)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MultiTerminal](/en/docs/mt4/multiterminal)[Trading](/en/docs/mt4/multiterminal/trading)Order Types

# Order Types

MultiTerminal allows to prepare requests and request the broker for execution of trading operations. Moreover, terminal allows to control and manage open positions. For these purposes, several types of trading orders are used. Order is a client's commitment to brokerage company to perform a trade operation. The following orders are used in the terminal: [Market order](/en/docs/mt4/multiterminal/trading/ug_orders#market), [Pending order](/en/docs/mt4/multiterminal/trading/ug_orders#pending), [Stop Loss](/en/docs/mt4/multiterminal/trading/ug_orders#stop_loss) and [Take Profit](/en/docs/mt4/multiterminal/trading/ug_orders#take_profit).

-   Market Order  
    Market order is a commitment to the brokerage company to buy or sell a security at the current price. Execution of this order results in opening a trade position. Securities are bought at ASK price and sold at BID price. Stop Loss and Take Profit orders (described below) can be attached to a market order. [Execution mode](/en/docs/mt4/multiterminal/trading/ug_execution) of market orders depends on the security traded.
-   Pending Order  
    Pending order is the client's commitment to the brokerage company to buy or sell a security at a pre-defined price in the future. This type of orders is used for opening a trade position provided the future quotes reach the pre-defined level. There are four types of pending orders available in the terminal:

-   -   Buy Limit — buy provided the future "ASK" price is equal to the pre-defined value. The current price level is higher than the value of the placed order. Orders of this type are usually placed in anticipation of that the security price, having fallen to a certain level, will increase;
    -   Buy Stop — buy provided the future "ASK" price is equal to the pre-defined value. The current price level is lower than the value of the placed order. Orders of this type are usually placed in anticipation of that the security price, having reached a certain level, will keep on increasing;
    -   Sell Limit — sell provided the future "BID" price is equal to the pre-defined value. The current price level is lower than the value of the placed order. Orders of this type are usually placed in anticipation of that the security price, having increased to a certain level, will fall;
    -   Sell Stop — sell provided the future "BID" price is equal to the pre-defined value. The current price level is higher than the value of the placed order. Orders of this type are usually placed in anticipation of that the security price, having reached a certain level, will keep on falling.

![Setting of Pending Orders](/en/docs/mt4/multiterminal/img/schema_pending_orders.png "Setting of Pending Orders")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Orders of Stop Loss and Take Profit can be attached to a pending order. After a pending order has triggered, its Stop Loss and Take Profit levels will be attached to the open position automatically.</span></p></td></tr></tbody></table>

-   Stop Loss  
    This order is used for minimizing losses if the security price has started to move in an unprofitable direction. If the security price reaches this level, the position will be closed automatically. Such orders are always attached to an open position or a pending order. The brokerage company can place them only together with a market or a pending order. Terminal checks long positions with BID price for meeting of this order provisions, and it does with ASK price for short positions.
-   Take Profit  
    Take Profit order is intended for gaining the profit when the security price has reached a certain level. Execution of this order results in closing a position. It is always attached to an open position or a pending order. The order can be requested only together with a market or a pending order. Terminal checks long positions with BID price for meeting of this order provisions, and it does with ASK price for short positions.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">execution prices for all trade operations are defined by the broker;</span></li><li class="p_tableatten"><span class="f_tableatten">Stop Loss and Take Profit orders can only be executed for an open position, but not for pending orders.</span></li></ul></td></tr></tbody></table>

[Trading](/en/docs/mt4/multiterminal/trading)

[Types of Execution](/en/docs/mt4/multiterminal/trading/ug_execution)