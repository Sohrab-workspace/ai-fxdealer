# One Click Trading

> Source: https://support.metaquotes.net/en/docs/mt5/client/one_click_trading

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
            -   [Basic Principles](/en/docs/mt5/client/general_concept)
            -   [Depth of Market](/en/docs/mt5/client/depth_of_market)
            -   [Market Watch](/en/docs/mt5/client/market_watch)
            -   [Options Board](/en/docs/mt5/client/options_board)
            -   [Executing Trades](/en/docs/mt5/client/performing_deals)
            -   [One Click Trading](/en/docs/mt5/client/one_click_trading)
            -   [Trading Report](/en/docs/mt5/client/report)
            -   [For Advanced Users](/en/docs/mt5/client/trading_advanced)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Trading Operations](/en/docs/mt5/client/trading)One Click Trading

# One Click Trading

Trade execution speed is very important in financial trading. Traders strive to enter the market on time to catch the opportunity to profit. Trading robots can be used for high-frequency trading. However some traders still prefer to trade manually. The platform features special tools for carrying out various trading operations with just one mouse click.

## How to Perform a Deal with One Click on a Chart [#](one_click_trading#chart_deal)

A special panel allows performing instant trade operations directly on a chart. To activate it, click "![One Click Trading](/en/docs/mt5/client/img/chart_oneclick_trading_context.png "One Click Trading") One Click Trading" in the chart context menu.

You can show/hide the panel by clicking![One Click Trading](/en/docs/mt5/client/img/chart_oneclick_trading_icon.png "One Click Trading")to the left of OHLC.

![One Click Trading](/en/docs/mt5/client/img/chart_oneclick_trading.png "One Click Trading")

Using this panel you can instantly send buy or sell [market orders](/en/docs/mt5/client/general_concept#market_order) with specified volumes.

## How to Protect a Market Position by Take Profit and Stop Loss with a Single Mouse Action [#](one_click_trading#chart_set_sltp)

You can quickly set Stop Loss and Take Profit for a position on a chart. Click on the position level and drag it up or down. Depending on the direction of the position and dragging direction, a user is prompted to set either Stop Loss or Take Profit.

When you move a level, a tooltip appears displaying potential profit (or loss) in the deposit currency and pips that can be obtained if the level triggers.

![Setting Stop Loss and Take Profit on a chart](/en/docs/mt5/client/img/set_sltp_chart.png "Setting Stop Loss and Take Profit on a chart")

To modify the level on a chart, left-click on it and drag the level up or down to the required value holding the mouse button (Drag'n'Drop):

![Modification on the chart](/en/docs/mt5/client/img/modify_position_chart.png "Modification on the chart")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Modification of Stop Loss and Take Profit on a chart is only available if the "Show trade levels" option is enabled in the <a href="/en/docs/mt5/client/settings#trade_levels" class="topiclink">platform settings</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">Modification of Stop Loss and Take profit on a chart is disabled if you enable the <a href="/en/docs/mt5/client/settings#trade_levels" class="topiclink">"Disable dragging of trade levels"</a> option in the platform settings.</span></li></ul></td></tr></tbody></table>

## How to Quickly Lock the Profit/Loss of a Position [#](one_click_trading#close_position)

To quickly close a position and take its current profit/loss, use the "Trade" tab in the Toolbox window.

![One Click Closure](/en/docs/mt5/client/img/one_click_close_position.png "One Click Closure")

The "Profit" column of each open position has the button![Close position/Delete order](/en/docs/mt5/client/img/close_delete_button.png "Close position/Delete order"). If you click the button for a position, it will be immediately closed without additional confirmation.

## How To Quickly Set a Pending Order at the Desired Level on the Chart [#](one_click_trading#pending_place)

Pending orders can be placed from the chart using the [Trading](/en/docs/mt5/client/charts_advanced/charts_manage#trading) submenu of the chart context menu:

![Trading menu on a chart](/en/docs/mt5/client/img/chart_trading_menu.png "Trading menu on a chart")

Place the mouse cursor on the necessary price level on the chart and execute the appropriate context menu command to set a pending order.

Depending on the cursor position, available [order types](/en/docs/mt5/client/general_concept#pending_order) are displayed in the menu. If the menu is activated above the current price, a user can place Sell Limit and Buy Stop orders. If the menu is activated below the current price, Buy Limit and Sell Stop orders can be placed.

Available distance between the selected and current price for the symbol is additionally checked ("[Stop level](/en/docs/mt5/client/market_watch#specification)").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The order volume to set is selected on the <a href="/en/docs/mt5/client/one_click_trading#chart_deal" class="topiclink">quick trading panel on the chart</a>.</span></p></td></tr></tbody></table>

After executing the command, the [Order window](/en/docs/mt5/client/performing_deals#pending_place) appears allowing the user to adjust its parameters more precisely. If ["One Click Trading"](/en/docs/mt5/client/settings#one_click) option is enabled in the platform settings, orders are placed at a specified price instantly without displaying the trading dialog.

## How to Quickly Change the Price of a Pending Order on the Chart [#](one_click_trading#pending_change)

Modification of pending orders on a chart is only available if the "Show trade levels" option is enabled in the [platform settings](/en/docs/mt5/client/settings#trade_levels).

For pending orders, it is possible to modify [Stop Loss](/en/docs/mt5/client/general_concept#stop_loss) and [Take Profit](/en/docs/mt5/client/general_concept#take_profit) levels separately, as well as modify the order price along with stop levels:

-   For the separate modification of stop levels on a chart, left-click the necessary level and drag it to the desired value (Drag'n'Drop).
-   Drag the price line to modify the entire order. In this case, both the price and the stop level are moved.

![Pending order modification on a chart](/en/docs/mt5/client/img/modify_pending_order_chart.png "Pending order modification on a chart")

When you move an order, a tooltip appears displaying the distance from the current price in the deposit currency and pips.

Once a level is set, the [order modification](/en/docs/mt5/client/performing_deals#pending_modify) appears allowing users to adjust the level more precisely. If [One Click Trading](/en/docs/mt5/client/settings#one_click) is enabled in the platform settings, modification is performed instantly without displaying the trading dialog.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Changing pending orders on the chart can be disabled by enabling <a href="/en/docs/mt5/client/settings#trade_levels" class="topiclink">"Disable dragging of trade levels"</a> option in the platform settings.</span></p></td></tr></tbody></table>

## How to Remove a Pending Order in One Click [#](one_click_trading#pending_delete)

To quickly delete a pending order, use the "Trade" tab in the Toolbox window.

![Deleting a pending order with one click](/en/docs/mt5/client/img/one_click_delete_pending.png "Deleting a pending order with one click")

The state column of each order has the button ![Close position/Delete order](/en/docs/mt5/client/img/close_delete_button.png "Close position/Delete order"). When pressed on the order line, the order is deleted without additional confirmation.

## How to Remove Stop Loss or Take Profit with One Click [#](one_click_trading#sl_tp_delete)

To quickly delete Stop Loss or Take Profit of a position, use the "Trade" tab of the Toolbox window.

![Deleting Stop Loss and Take Profit with One Click](/en/docs/mt5/client/img/one_click_delete_sltp.png "Deleting Stop Loss and Take Profit with One Click")

In the S/L or T/P column click ![Close position/Delete order](/en/docs/mt5/client/img/close_delete_button.png "Close position/Delete order"). The appropriate level is deleted without any further confirmation.

## One Click Trading in the Depth of Market and Market Watch [#](one_click_trading#dom_mw)

The One Click Trading options are also available in the depth of market and the Market Watch. For details, refer to the appropriate sections:

-   [Quick Trading from the Depth of Market](/en/docs/mt5/client/depth_of_market#quick_trading)
-   [One Click Trading in Market Watch](/en/docs/mt5/client/market_watch#trading)

## Features of One Click Trading [#](one_click_trading#notes)

A window of the agreement appears when you first try to make a deal with one click.

![One Click Trading Terms and Conditions](/en/docs/mt5/client/img/one_click_disclaimer.png "One Click Trading Terms and Conditions")

If you accept the conditions, tick "I Accept these Terms and Conditions" option and click "OK". If you do not accept the conditions, click "Cancel" and do not use the "One Click Trading" function.

You can pre-allow the one-click trading option in the [platform settings](/en/docs/mt5/client/settings#agreement).

When performing operations with one click, you should be aware of some of its features:

-   One Click Trading is available in all [execution modes](/en/docs/mt5/client/general_concept#execution_type) except for "Request" execution. In the latter case, a standard trade dialog appears.
-   In the [Instant Execution](/en/docs/mt5/client/general_concept#execution_type) mode, the allowable price [deviation](/en/docs/mt5/client/performing_deals#deviation) in orders is set in accordance with the ["Use deviation"](/en/docs/mt5/client/settings#trade) option.
-   [The Fill Policy](/en/docs/mt5/client/general_concept#fill_policy) is selected based on the trading instrument [execution mode](/en/docs/mt5/client/general_concept#execution_type): for exchange execution it is always "Return", for market execution it is either "Fill or Kill" or "Immediate or Cancel" (depending on what policy is allowed for the symbol), for instant and request execution it is always "Fill or Kill".
-   When a requote is received, an appropriate message is added to the platform [journal](/en/docs/mt5/client/start_advanced/journal) and a [requote sound](/en/docs/mt5/client/settings#events) is played.

The quotes are displayed on the one-click trading panel buttons the following way:

-   The decimal point between the numbers of different size is not displayed to save space. The font size is used as a separator instead.
-   In three-digit quotes, the first and second digits are highlighted, while in five-digit quotes — the third and fourth ones. The last two digits are highlighted in other cases.

[Executing Trades](/en/docs/mt5/client/performing_deals)

[Trading Report](/en/docs/mt5/client/report)