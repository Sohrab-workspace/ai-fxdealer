# Placing of Pending Orders

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/positions/positions_control/pending_orders_place

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Trading](/en/docs/mt4/terminal/positions)[Trade Positions](/en/docs/mt4/terminal/positions/positions_control)Placing of Pending Orders

# Placing of Pending Orders

To place a pending order, one has to open the "Order" window. This can be done by the ["Tools — New Order" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools) command, the ![New Order](/en/docs/mt4/terminal/img/tb_standard_order_new.png "New Order") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard), by pressing of F9, by the "New Order" command of the ["Market Watch"](/en/docs/mt4/terminal/overview/market_watch) and ["Terminal — Trade"](/en/docs/mt4/terminal/overview/terminal/terminal_trade) window context menus, as well as by double-clicking on the symbol name in the ["Market Watch"](/en/docs/mt4/terminal/overview/market_watch) window. "Pending Order" must be selected in the "Type" field of this window.

![instant_order_late](/en/docs/mt4/terminal/img/instant_order_late.png)

Further, a security (symbol) must be selected, the volume and values of [Stop Loss](/en/docs/mt4/terminal/positions/orders) and [Take Profit](/en/docs/mt4/terminal/positions/orders) orders must be specified. If necessary, a comment can be written in the field of the same name. In the "Pending Order" fields one has to:

-   Type — select a type of [pending order](/en/docs/mt4/terminal/positions/orders): Buy Limit, Buy Stop, Sell Limit, or Sell Stop;
-   at price — set the price level at which the order must trigger;
-   Expiry — set the expiry time of the order. If the order has not triggered by this time, it will be deleted automatically.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Order may not expire earlier than in 10 minutes!</span></p></td></tr></tbody></table>

The "Place" button will send the order to be executed what is performed in two stages. First, the brokerage company places the order after it has been sent. At that, a line containing the number and status of the pending order will appear in the ["Terminal — Trade"](/en/docs/mt4/terminal/overview/terminal/terminal_trade) tab. If the "Show trade levels" option is enabled, levels of the placed pending order (including levels of Stop Loss and Take Profit) will be shown in the chart. At the second stage, if prices correspond with the order provisions, it will be deleted and a trade position will be opened instead of it. The trade position ticket will coincide with the pending order ticket. These changes will be shown in the ["Terminal — Trade" window](/en/docs/mt4/terminal/overview/terminal/terminal_trade).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Stop Loss and Take Profit orders trigger only at open positions, but not at pending orders.</span></p></td></tr></tbody></table>

[Position Close](/en/docs/mt4/terminal/positions/positions_control/positions_close)

[Modifying of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_modify)