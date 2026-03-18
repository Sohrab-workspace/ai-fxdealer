# Open Positions

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/positions/positions_control/positions_open

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Trading](/en/docs/mt4/terminal/positions)[Trade Positions](/en/docs/mt4/terminal/positions/positions_control)Open Positions

# Open Positions

Opening of a position, or entering the market, is the first buying or selling of a certain amount of the security traded. Position can be opened either by execution of a [market order](/en/docs/mt4/terminal/positions/orders#market) or by automatic triggering of a [pending order](/en/docs/mt4/terminal/positions/orders#pending).

## Market Order

To open a position using a market order, one has to execute the ["Tools — New Order" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools) command, press the ![New Order](/en/docs/mt4/terminal/img/tb_standard_order_new.png "New Order") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard), press F9, or double-click on the symbol name in the ["Market Watch"](/en/docs/mt4/terminal/overview/market_watch) window. One can also execute the "New Order" context menu command of the windows of ["Market Watch"](/en/docs/mt4/terminal/overview/market_watch) and ["Terminal — Trade"](/en/docs/mt4/terminal/overview/terminal/terminal_trade). At that, the "Order" window will open that is used for managing trade positions.

![instant_order](/en/docs/mt4/terminal/img/instant_order.png)

When opening a position, one has to:

-   Symbol — select a security symbol for which the position is to be opened;
-   Volume — specify the trade volume (amount of lots);
-   Stop Loss — set the Stop Loss level (optionally);
-   Take Profit — set the Take Profit level (optionally);

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Zero values of <a href="/en/docs/mt4/terminal/positions/orders" class="topiclink">Stop Loss/Take Profit</a> orders mean that the orders have not been placed at all.</span></p></td></tr></tbody></table>

-   Comment — write a comment (optionally). The comment length may not exceed 25 characters. The brokerage company may add a comment not above 6 characters long, or it can completely replace the existing one. After a position has been opened, the comment cannot be changed;
-   Type — the [execution mode](/en/docs/mt4/terminal/positions/execution) specified by the broker for the given symbol is displayed in this filed on default. You can also choose the "Pending order" in the list here, which allows you to go to [placing a pending order](/en/docs/mt4/terminal/positions/positions_control/pending_orders_place).
-   Enable maximum deviation from quoted price — enable/disable the use of deviation. If a broker requotes the price of order execution, the deviation of the new price from the quoted before will be calculated. At that, if the deviation is below or equal to the specified parameter, the order will be executed at the new price without any additional notifying. Otherwise, the broker returns new prices at which the order can be executed;
-   Maximum deviation — the value of maximum permissible deviation in pips.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Price deviation at placing of orders is used only in the <a href="/en/docs/mt4/terminal/positions/execution" class="topiclink">instant execution mode</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The trade window displays current best Bid and Ask price (except for the Execution on Request mode).</span></li></ul></td></tr></tbody></table>

After all necessary data have been specified, one has to press the "Sell" or "Buy" button. At that, the order for opening of a short or long position, respectively, will be sent to the broker.

Once the order is sent the window will display the result of its execution — a successful trade operation or a reason why it has not been executed. If the ["One click trading"](/en/docs/mt4/terminal/setup/setup_trade#one_click) option is enabled and the order has been successfully executed the trading window is closed right away without displaying the execution result.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If orders for a given symbol are <a href="/en/docs/mt4/terminal/positions/execution" class="topiclink">executed at request</a>, it is necessary to press the "Request" button to receive quotes first. Quotes offered after requesting will be active for just a few seconds. If no decision is made within these seconds, "Sell" and "Buy" buttons will be locked again.</span></p></td></tr></tbody></table>

If the [Stop Loss](/en/docs/mt4/terminal/positions/orders) or [Take Profit](/en/docs/mt4/terminal/positions/orders) level is too close to the current price at opening of a position, the message of "Invalid S/L or T/P" will appear. It is necessary to shift levels from the current price and re-request for placing of the order. A trade position will be opened after the brokerage company has made a trade and set Stop Loss and Take Profit. At that, the status bar of the opened position will appear in the ["Terminal — Trade" tab](/en/docs/mt4/terminal/overview/terminal/terminal_trade), and open price, [Stop Loss and Take Profit](/en/docs/mt4/terminal/positions/orders) levels will be shown in the chart (if the ["Show trade levels" option](/en/docs/mt4/terminal/setup/setup_charts) is enabled).

## Pending Orders

To open a position with a pending order, one has to place it first as described in the ["Placing of Pending Order" section](/en/docs/mt4/terminal/positions/positions_control/pending_orders_place). If the current prices meet its provisions, the [pending order](/en/docs/mt4/terminal/positions/orders) will be executed automatically, i.e., a new trade position will be opened. At that, the status bar of the pending order will be deleted in the ["Terminal — Trade" tab](/en/docs/mt4/terminal/overview/terminal/terminal_trade), and the newly opened position status bar will appear. If [Stop Loss and Take Profit](/en/docs/mt4/terminal/positions/orders#stop_loss) orders were attached to the pending order, they will be attached to the new position automatically.

[Trade Positions](/en/docs/mt4/terminal/positions/positions_control)

[Modifying of Positions](/en/docs/mt4/terminal/positions/positions_control/positions_modify)