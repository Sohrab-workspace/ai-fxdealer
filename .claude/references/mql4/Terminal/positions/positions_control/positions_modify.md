# Modifying of Positions

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/positions/positions_control/positions_modify

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Trading](/en/docs/mt4/terminal/positions)[Trade Positions](/en/docs/mt4/terminal/positions/positions_control)Modifying of Positions

# Modifying of Positions

Modifying of the current position consists in setting of new levels of [Stop Loss](/en/docs/mt4/terminal/positions/orders) or [Take Profit](/en/docs/mt4/terminal/positions/orders) attached to it. To modify a position, one has to execute the ["Modify or Delete Order" command of the opened position context menu](/en/docs/mt4/terminal/overview/terminal/terminal_trade) or doulbe-click with the left mouse button in the fields of "Stop Loss" or "Take Profit" of the opened position line in the ["Terminal" window](/en/docs/mt4/terminal/overview/terminal/terminal_trade).

![instant_order_edit](/en/docs/mt4/terminal/img/instant_order_edit.png)

Then, one has to set new values of Stop Loss or Take Profit and press the "Modify" button.

To change the Stop Loss or Take Profit values, one has to enter the new values in the corresponding fields. To place the order in points from the current price, one has to set the desired value in the "Level" field and press the "Copy as" button. If values of these fields are zero, the minimum permissible deviation is used to be set by broker.

If Stop Loss or Take Profit level is too close to the current price, the "Modify" button will be locked. It is necessary to shift levels from the current price and re-request for position modifying. A trade position will be modified after the brokerage company has set a new value for Stop Loss or Take Profit, or both. Values in the fields of "S/L" and "T/P" will be changed in the opened position status bar in the ["Terminal — Trade" tab](/en/docs/mt4/terminal/overview/terminal/terminal_trade). At that, levels of the modified orders will be changed if the ["Show trade levels" option](/en/docs/mt4/terminal/setup/setup_charts) is enabled.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Zero values in the fields of "Stop Loss" and "Take Profit" mean that these orders were not placed.</span></p></td></tr></tbody></table>

[Open Positions](/en/docs/mt4/terminal/positions/positions_control/positions_open)

[Position Close](/en/docs/mt4/terminal/positions/positions_control/positions_close)