# Trade Positions

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/positions/positions_control

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
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
            -   [Order Types](/en/docs/mt4/terminal/positions/orders)
            -   [Trailing Stop](/en/docs/mt4/terminal/positions/trailing)
            -   [Types of Execution](/en/docs/mt4/terminal/positions/execution)
            -   [Trade Positions](/en/docs/mt4/terminal/positions/positions_control)
                -   [Open Positions](/en/docs/mt4/terminal/positions/positions_control/positions_open)
                -   [Modifying of Positions](/en/docs/mt4/terminal/positions/positions_control/positions_modify)
                -   [Position Close](/en/docs/mt4/terminal/positions/positions_control/positions_close)
                -   [Placing of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_place)
                -   [Modifying of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_modify)
                -   [Deletion of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_delete)
            -   [Trading on Chart](/en/docs/mt4/terminal/positions/trading_chart)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Trading](/en/docs/mt4/terminal/positions)Trade Positions

# Trade Positions

The fundamental and simple rule of profitable trading at financial markets is to buy cheaper and sell dearer. Thus, the entire trading activities at financial markets come to the successive operations performed to sell or buy securities. To do so, one has to open, modify, and close trade positions. Trade position is a market commitment (order), the number of bought or sold contracts for which no set-off transactions have been made. The entire trading in the terminal is implemented through trade positions. Client Terminal gives a large amount of opportunities in controlling and managing trade positions. Trader gives instructions ([orders](/en/docs/mt4/terminal/positions/orders)), and brokerage company opens or closes a position. Managing trade positions consists in:

-   [opening of a position](/en/docs/mt4/terminal/positions/positions_control/positions_open) — buying or selling of a security as a result of a market or a pending order execution;
-   [modifying of a position](/en/docs/mt4/terminal/positions/positions_control/positions_modify) — changing of the [Stop Loss](/en/docs/mt4/terminal/positions/orders) and [Take Profit](/en/docs/mt4/terminal/positions/orders) levels attached to the open position;
-   [placing of pending orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_place) — placing of pending orders like Buy Limit, Buy Stop, Sell Limit, or Sell Stop;
-   [modifying and deletion of pending orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_delete) — modifying or deletion of pending orders that did not trigger;
-   [closing of a position](/en/docs/mt4/terminal/positions/positions_control/positions_close) — buying or selling a security in order to close the existing open position.

[Types of Execution](/en/docs/mt4/terminal/positions/execution)

[Open Positions](/en/docs/mt4/terminal/positions/positions_control/positions_open)