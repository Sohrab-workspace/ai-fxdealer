# Trading on Chart

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/positions/trading_chart

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Trading](/en/docs/mt4/terminal/positions)Trading on Chart

# Trading on Chart

The client terminal allows traders to perform trading operations right on the symbol's [chart](/en/docs/mt4/terminal/chart_management). Combined with [one click trading function](/en/docs/mt4/terminal/setup/setup_trade#one_click), this enables users to open, modify and close positions quickly, as well as manage pending orders.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_Normal"><span class="f_txt">If <a href="/en/docs/mt4/terminal/setup/setup_trade#one_click" class="topiclink">One click trading option</a> is enabled in the terminal settings, trading commands described in this section are executed without additional confirmation (trading dialog is not displayed).</span></p></td></tr></tbody></table>

## One Click Trading Panel [#](trading_chart#quick_trading)

A special panel has been implemented to allow performing trading operations right on the chart. To activate it, execute "![One Click Trading](/en/docs/mt4/terminal/img/chart_oneclick_trading_context.png "One Click Trading") One Click Trading" in the chart's context menu.

You can show/hide the panel by clicking ![One Click Trading](/en/docs/mt4/terminal/img/chart_oneclick_trading_icon.png "One Click Trading") icon to the left of OHLC.

![One Click Trading](/en/docs/mt4/terminal/img/chart_oneclick_trading.png "One Click Trading")

Using this panel you can instantly send buy or sell [market orders](/en/docs/mt4/terminal/positions/orders) with specified volumes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When trading in the <a href="/en/docs/mt4/terminal/positions/execution" class="topiclink">instant execution</a> mode, the acceptable <a href="/en/docs/mt4/terminal/positions/positions_control/positions_open" class="topiclink">deviation</a> of price in the orders is set according to the <a href="/en/docs/mt4/terminal/setup/setup_trade" class="topiclink">"Deviation"</a> option.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">When a getting a requote, the corresponding message is written to the <a href="/en/docs/mt4/terminal/overview/terminal/terminal_journal" class="topiclink">terminal journal</a> and the <a href="/en/docs/mt4/terminal/setup/setup_events" class="topiclink">requote sound</a> is played.</span></li></ul></td></tr></tbody></table>

## Placing Pending Orders [#](trading_chart#pending_place)

Pending orders can be placed from the chart using Trading submenu of the chart's context menu:

![Menu for trading on the chart](/en/docs/mt4/terminal/img/chart_trading_menu.png "Menu for trading on the chart")

Place mouse cursor on the necessary price level on the chart and execute the appropriate command to install a pending order in the context menu.

According to the cursor's position, available [order types](/en/docs/mt4/terminal/positions/orders) are displayed in the menu. If the menu is activated above the current price, user can place Sell Limit and Buy Stop orders. If the menu is activated below the current price, Buy Limit and Sell Stop orders can be placed.

Available distance between the selected and current price for the symbol is additionally checked ("Stops level").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The volume for the orders placed is selected via the <a href="/en/docs/mt4/terminal/positions/trading_chart#quick_trading" class="topiclink">quick trading panel on the chart</a>.</span></p></td></tr></tbody></table>

After executing the command, [Order window](/en/docs/mt4/terminal/positions/positions_control/pending_orders_place) will appear allowing users to adjust its parameters more precisely. If ["One click trading"](/en/docs/mt4/terminal/setup/setup_trade#one_click) option is enabled in the terminal settings, orders are placed at a specified price instantly without displaying the trading dialog.

## Managing Stop Levels on the Chart [#](trading_chart#stops_chart)

Enable "Show trade levels" option in the [terminal settings](/en/docs/mt4/terminal/setup/setup_charts) to be able to change Stop Loss and Take Profit levels on the chart.

To set stop levels, click with the left mouse button on a position level and drag it up (Take Profit for buy position or Stop Loss for a sell position) or down (Stop Loss for a buy position or Take Profit for a sell position). Release the mouse button once the cursor is at the required price.

To modify the level on the chart, left-click on it and drag the level up or down to the required value holding the mouse button (Drag'n'Drop):

![Modification on the chart](/en/docs/mt4/terminal/img/modify_position_chart.png "Modification on the chart")

When moving a level there is a tooltip displaying potential profit (or loss) in the deposit currency and pips that can be obtained if the level triggers.

After setting the level, [position modification](/en/docs/mt4/terminal/positions/positions_control/positions_modify) window will appear allowing users to adjust the level more precisely. If ["One click trading"](/en/docs/mt4/terminal/setup/setup_trade#one_click) option is enabled in the terminal settings, modification is performed instantly without displaying the trading dialog.

## Managing Pending Orders on the Chart [#](trading_chart#pending_chart)

Enable "Show trade levels" option in the [terminal settings](/en/docs/mt4/terminal/setup/setup_charts) to be able to change pending orders on the chart.

For pending orders, it is possible to modify [Stop Loss](/en/docs/mt4/terminal/positions/orders) and [Take Profit](/en/docs/mt4/terminal/positions/orders) levels separately, as well as modify the order price along with stop levels:

-   In order to modify a stop level on the chart, left-click the necessary level and drag it up or down to the required value holding the mouse button (Drag'n'Drop).
-   Drag the price line to modify the entire order. In this case, both a price and a stop level will be relocated.

![Modifying a pending order on the chart](/en/docs/mt4/terminal/img/modify_pending_order_chart.png "Modifying a pending order on the chart")

When moving an order there is a tooltip displaying the distance to the current price in the deposit currency and pips.

After setting the level, [order modification](/en/docs/mt4/terminal/positions/positions_control/pending_orders_modify) window will appear allowing users to adjust the level more precisely. If ["One click trading"](/en/docs/mt4/terminal/setup/setup_trade#one_click) option is enabled in the terminal settings, modification is performed instantly without displaying the trading dialog.

## Position's Context Menu on the Chart [#](trading_chart#position_context)

![Position's menu on the chart](/en/docs/mt4/terminal/img/chart_position_context.png "Position's menu on the chart")

You can change and close your positions, as well as set trailing stops using position's context menu on the chart:

-   ![Modify or delete](/en/docs/mt4/terminal/img/modify_delete_order_icon.png "Modify or delete") Modify — open [position modification](/en/docs/mt4/terminal/positions/positions_control/positions_modify) window;
-   ![Close position](/en/docs/mt4/terminal/img/close_position_icon.png "Close position") Close — open position closing window. If ["One click trading"](/en/docs/mt4/terminal/setup/setup_trade#one_click) option is enabled in the terminal settings, position is closed instantly without displaying the trading dialog;
-   Trailing Stop — open the menu of [Trailing Stop](/en/docs/mt4/terminal/positions/trailing) level selection for a position.

## Order's Context Menu on the Chart [#](trading_chart#pending_context)

![Order's menu on the chart](/en/docs/mt4/terminal/img/chart_pending_context.png "Order's menu on the chart")

You can change or remove your pending orders, as well as set a trailing stop using pending order's context menu on the chart:

-   ![Modify or delete](/en/docs/mt4/terminal/img/modify_delete_order_icon.png "Modify or delete") Modify — open the window of [the selected order modification](/en/docs/mt4/terminal/positions/positions_control/pending_orders_modify);
-   ![Delete order](/en/docs/mt4/terminal/img/delete_order_icon.png "Delete order") Delete — open the window for deleting the selected order. If ["One click trading"](/en/docs/mt4/terminal/setup/setup_trade#one_click) option is enabled in the terminal settings, deletion is performed instantly without displaying the trading dialog;
-   Trailing Stop — open the menu of [Trailing Stop](/en/docs/mt4/terminal/positions/trailing) level selection for an order.

[Deletion of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_delete)

[Auto Trading](/en/docs/mt4/terminal/autotrading)