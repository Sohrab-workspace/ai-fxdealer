# Depth of Market

> Source: https://support.metaquotes.net/en/docs/mt5/client/depth_of_market

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Trading Operations](/en/docs/mt5/client/trading)Depth of Market

# Depth of Market

The Depth of Market (DOM) displays bids and asks for a particular instrument at the currently best prices (closest to the market).

The Dept of Market is different on the exchange and over-the-counter markets:

-   If an instrument is traded in the exchange mode, in which related trading operations are sent to an external trading system (an exchange), the DOM features real prices and order volumes from market participants.
-   If an instrument is traded in the over-the-counter (OTC) market, the Depth of Market can be formed based on the quotes of the broker, who may provide different prices depending on the buy or sell volume. If the broker does not provide volumes, the DOM window functions as a scalping tool, which allows placing of market and pending orders with a single click. In this case, the Depth of Market displays price levels calculated based on the Bid and Ask prices using the price change step.

For more information about prices in the Depth of Market, please see the [Price Data](/en/docs/mt5/client/trading_advanced/price_data) section.

![The depth of market displays information on buy and sell orders](/en/docs/mt5/client/img/dom.png "The depth of market displays information on buy and sell orders")

To open the depth of market of a financial instrument, click "![Depth of Market](/en/docs/mt5/client/img/dom_icon.png "Depth of Market") Depth of Market" in the context menu of the [Market Watch](/en/docs/mt5/client/market_watch).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The number of bids and offers displayed in the DOM is determined by the symbol parameters set by the broker.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The availability of the Depth of Market feature for exchange instruments is not guaranteed and depends on your broker.</span></li></ul></td></tr></tbody></table>

Operations of two types are performed from the depth of market:

-   [Market Operations](/en/docs/mt5/client/depth_of_market#market) — buying/selling a financial instrument at the current market price;
-   [Trade Requests](/en/docs/mt5/client/depth_of_market#request) — placing various trade requests ([pending orders](/en/docs/mt5/client/general_concept#pending_order)) to buy/sell a financial instrument at a specified price (which is currently unavailable on the market).

## Market Operations [#](depth_of_market#market)

A market operation is buying/selling a financial instrument at the best price currently offered in the market.

Execute a market operation from the depth of market. Click on the appropriate [trade command](/en/docs/mt5/client/depth_of_market#pending_place) in the depth of market of the appropriate [symbol](/en/docs/mt5/client/market_watch) specifying the required amount. If ["One Click Trading"](/en/docs/mt5/client/settings#one_click) is enabled, this request is immediately sent to the server without specifying any extra conditions (trading dialog is not displayed).

Suppose we have executed a 20-lot buy operation, while the following offers are currently available in the market:

![Market offers in the depth of market](/en/docs/mt5/client/img/market_example_dom.png "Market offers in the depth of market")

Since we have requested 20 lots with the Fill or Kill condition at the market price, the required volume will be made up of the nearest market bids. If the order contained a certain price, then it would be executed only at this specified price and only in the specified volume.

You can view the history of order execution in the ["History"](/en/docs/mt5/client/performing_deals#trade_history) tab of the "Toolbox" window:

![The order is filled by several offers closest to the market](/en/docs/mt5/client/img/market_example_history.png "The order is filled by several offers closest to the market")

You see here that the final volume of 20 lots was received from a few offers closest to the market. The corresponding offers disappear from the depth of market.

## Trade Requests [#](depth_of_market#request)

Placing a trade requests means creating a [pending order](/en/docs/mt5/client/general_concept#pending_order) to buy/sell a financial instrument at a specified price, which is currently not available on the market. Depending on how requests are processed on the server, they can be displayed directly in depth of market (mostly limit requests) or wait for execution on the broker's side (mostly stop or stop limit requests) and then be converted into a market order.

Here is an example of placing a limit request to buy 3 lots of the futures contract RTS-6.13. Specify the required volume in the "vol" field and click on ![Set Buy Limit](/en/docs/mt5/client/img/dom_buy_limit_button.png "Set Buy Limit") (in the Bid price area for the Buy Limit order) or ![Set Sell Limit](/en/docs/mt5/client/img/dom_sell_limit_button.png "Set Sell Limit") (in the Ask price area for the Sell Limit order) in the "Trade" column in the line of the price, at which you wish to place an order. If ["One Click Trading"](/en/docs/mt5/client/settings#one_click) is enabled, this request is immediately sent to the server without specifying any extra conditions (trading dialog is not displayed).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Examine <a href="/en/docs/mt5/client/depth_of_market#quick_trading" class="topiclink">"Quick trading"</a> section to learn how to quickly manage orders in the depth of market.</span></p></td></tr></tbody></table>

When placed successfully, the request appears in the depth of market:

![The placed request is displayed in DOM](/en/docs/mt5/client/img/pending_dom_example.png "The placed request is displayed in DOM")

The newly placed order is displayed in the "Trade" column — BLIM 3 (Buy Limit order of 3 lots). As soon as there is a market participant ready to sell the financial instrument at the specified price, the order will be filled and will turn into a position.

### Stop and Stop Limit Orders

Usually, [Stop and Stop Limit Orders](/en/docs/mt5/client/general_concept#pending_order) (Buy Stop, Sell Stop, Buy Stop Limit and Sell Stop Limit) are not sent to an external trading system (exchange) directly as opposed to limit orders. Until reaching the [stop price](/en/docs/mt5/client/performing_deals#pending_place), these orders are processed within the MetaTrader 5 platform.

-   Upon reaching the stop price specified in a Buy Stop or Sell Stop order, an appropriate [market operation is executed](/en/docs/mt5/client/depth_of_market#market).
-   Upon reaching the stop price specified in a Buy Stop Limit or Sell Stop Limit order, an appropriate limit request is executed, which will be visible to other market participants.

## Quick Trading from the Depth of Market [#](depth_of_market#quick_trading)

The depth of market allows users to quickly manage stop levels (Stop Loss and Take Profit) and pending orders of open positions. This option is only available with the ["One Click Trading"](/en/docs/mt5/client/settings#one_click) option enabled in the trading platform settings. Trade requests are sent from the depth of market instantly without showing a trading dialog.

### Moving Stop Levels

Stop levels of open positions are displayed in the "Trade" column as TP (Take Profit) and SL (Stop Loss). These levels can be moved by mouse:

![To modify a stop level, drag it in the depth of market](/en/docs/mt5/client/img/dom_stops_move.png "To modify a stop level, drag it in the depth of market")

Move a level to the line with the required price, and it will be modified instantly.

### Deleting Stop Levels

Stop levels can be deleted from Depth of Market:

![To remove a stop level, place the cursor on it and press X](/en/docs/mt5/client/img/dom_stops_delete.png "To remove a stop level, place the cursor on it and press X")

Hover the mouse cursor over the button ![Set Sell Limit/Sell Stop](/en/docs/mt5/client/img/dom_sell_limit_button.png "Set Sell Limit/Sell Stop") (or ![Set Buy Limit/Buy Stop](/en/docs/mt5/client/img/dom_buy_limit_button.png "Set Buy Limit/Buy Stop")) to the right or to the left from the level and click Shift. The button will change its view to ![Delete level](/en/docs/mt5/client/img/dom_order_delete_button.png "Delete level"). Click the button to delete the level.

### Placing Orders [#](depth_of_market#pending_place)

[Pending orders](/en/docs/mt5/client/general_concept#pending_order) are placed using buttons ![Set Buy Limit/Buy Stop](/en/docs/mt5/client/img/dom_buy_limit_button.png "Set Buy Limit/Buy Stop") or ![Set Sell Limit/Sell Stop](/en/docs/mt5/client/img/dom_sell_limit_button.png "Set Sell Limit/Sell Stop") next to the desired price:

-   To place a Buy Limit order, click ![Set Buy Limit](/en/docs/mt5/client/img/dom_buy_limit_button.png "Set Buy Limit") in the Bid price area.
-   To place a Buy Stop order, click ![Set Buy Stop](/en/docs/mt5/client/img/dom_buy_limit_button.png "Set Buy Stop") in the Ask price area.
-   To place a Sell Limit order, click ![Set Sell Limit](/en/docs/mt5/client/img/dom_sell_limit_button.png "Set Sell Limit") in the Ask price area.
-   To place a Sell Stop order, click ![Set Sell Stop](/en/docs/mt5/client/img/dom_sell_limit_button.png "Set Sell Stop") in the Bid price area.

![To place a limit order, click the up or down arrow at the required level](/en/docs/mt5/client/img/dom_pending_place.png "To place a limit order, click the up or down arrow at the required level")

After that, an order is placed at the specified price. It has the volume set in the "vol" field, as well as Stop Loss and Take Profit levels specified in "sl" and "tp" fields, respectively.

### Modification of Orders

The depth of market allows users to easily change prices of previously set orders.

![To modify a limit order, drag it to a new level](/en/docs/mt5/client/img/dom_pending_move.png "To modify a limit order, drag it to a new level")

Move the pending order to the necessary price line. The order price changes instantly. If the Stop Loss and Take Profit levels are set for the order, they are moved by the same distance as the price.

If we drag a limit order through the ask/bid border, it will change to a stop order (Buy Limit will be replaced by Buy Stop, while Sell Limit - by Sell Stop).

![To change the order type, drag it across the border of buy and sell offers](/en/docs/mt5/client/img/dom_pending_change_type.png "To change the order type, drag it across the border of buy and sell offers")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If several same price orders are placed, they cannot be moved in the depth of market.</span></p></td></tr></tbody></table>

### Deleting Orders

To delete an order from the depth of market, hover the mouse cursor over ![Set Sell Limit/Sell Stop](/en/docs/mt5/client/img/dom_sell_limit_button.png "Set Sell Limit/Sell Stop") (or ![Set Buy Limit/Buy Stop](/en/docs/mt5/client/img/dom_buy_limit_button.png "Set Buy Limit/Buy Stop")) to the right and click Shift. The button will change its view to ![Delete level](/en/docs/mt5/client/img/dom_order_delete_button.png "Delete level"). Click the button to delete the order.

![To remove a pending order, place the cursor on it and press X](/en/docs/mt5/client/img/dom_pending_delete.png "To remove a pending order, place the cursor on it and press X")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If several same price orders are placed, the oldest one is removed first.</span></p></td></tr></tbody></table>

## Time & Sales and Tick Chart [#](depth_of_market#timesales)

Time and sales and a tick chart of exchange instruments with real transaction prices is displayed in the Depth of Market.

### Time & Sales

The Time & Sales feature provides the price and time of every trade executed on the exchange. Information on every trade includes the time when the trade was executed, its direction (buying or selling), as well as the price and volume of the trade. For easy visual analysis, different colors are used to indicate different trade directions: blue is used for Buy trades, pink for Sell trades, green means undefined direction. Trade volumes are additionally displayed in a histogram.

![Time & Sales](/en/docs/mt5/client/img/time_and_sales.png "Time & Sales")

How Time & Sales can help you understand the market

The Time & Sales feature provides tools for a more detailed market analysis. The trade direction suggests who has initiated the trade: the buyer or the seller. The volume of trades allows traders to understand the behavior of market participants: whether the trades are performed by large or small market players, as well as estimate the activity of the players. The trade execution speed and the volume of trades on various price levels help traders to estimate the importance of the levels.

How to use Time & Sales data

In addition to the visual analysis of the table, you can save the details of trades to a CSV file. Further, they can be analyzed using any other software, such as MS Excel. The file contains comma-separated data:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Time,Bid,Ask,Last,Volume,Type</span><br><span class="f_CodeExample">2016.07.06</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">16:05:04.305,89360,89370,89370,4,Buy</span><br><span class="f_CodeExample">2016.07.06</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">16:05:04.422,89360,89370,89370,2,Buy</span><br><span class="f_CodeExample">2016.07.06</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">16:05:04.422,89360,89370,89370,10,Buy</span><br><span class="f_CodeExample">2016.07.06</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">16:05:04.669,89360,89370,89370,1,Buy</span><br><span class="f_CodeExample">2016.07.06</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">16:05:05.968,89360,89370,89360,7,Sell</span></p></td></tr></tbody></table>

If you want to save data to a file, open the context menu and select "Export Ticks to CSV".

Filter by Volume

Deals with the volume less than the specified value can be hidden from the Time & Sales table. This filter allows to show only large deals in the Time & Sales window.

Double click on the first line in the Time & Sales window, specify the minimum volume in lots, and then click on any other area of ​​the Market Depth. Trades will be filtered, and the current filter value will appear in the volume column header.

![Filtering trades by volume](/en/docs/mt5/client/img/time_sales_filter.png "Filtering trades by volume")

You can also specify the minimum volume using the Time & Sales context menu.

### Tick Chart

All transactions conducted on the Exchange are plotted on this chart:

-   Red circles show Sell transactions.
-   Blue circles show Buy transactions
-   Green circles appear when the direction of the transaction is undefined. It is used when the exchange does not transmit the direction of a transaction. In this case, the direction is determined based on the price of the transaction as compared to prices bid and ask. A Buy transaction is that executed at the ask price or above, a Sell transaction is executed at the bid price or lower. The direction is undefined if the price of the transaction is between the bid and the ask.

![A tick chart with Time & Sales](/en/docs/mt5/client/img/dom.png "A tick chart with Time & Sales")

The larger the circle, the greater the volume of the transaction. Transaction volumes are also shown as a histogram below the tick chart.

Using the "Synchronize" command in the context menu, you can control the display of deals charts (circles and histogram):

-   In the synchronous mode, the deals chart is tied to the tick chart and they both have the same time scale.
-   In the independent mode, the deals chart is not tied to the tick chart, and the deals are drawn one by one.

At the top and bottom of the histogram, the total volumes of the current Buy and Sell offers are shown.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The vertical scale of the tick chart is the Market Depth (i.e. its levels). Price change ranges which are not available in market depth are displayed as straight lines on the tick chart. To view the most accurate tick chart, enable the extended mode and the display of spread values for the Market Depth.</span></p></td></tr></tbody></table>

## Toolbar [#](depth_of_market#toolbar)

To customize the appearance of the depth of market, use the toolbar at the top of the window:

-   ![Show/hide the tick chart.](/en/docs/mt5/client/img/dom_tick_chart_icon.png "Show/hide the tick chart.") — show/hide the tick chart.
-   ![Show/hide Time & Sales](/en/docs/mt5/client/img/time_and_sales_icon.png "Show/hide Time & Sales") — show/hide Time & Sales.
-   ![Bind the Market Depth to an active chart](/en/docs/mt5/client/img/dom_link_icon.png "Bind the Market Depth to an active chart") — binding the Market Depth to an active chart. Every time you switch to a chart of a financial instrument, the same instrument will be automatically enabled in the Market Depth window. So, you will not need to open the Market Depth window for each new symbol.
-   ![Switch to the advanced mode](/en/docs/mt5/client/img/dom_advanced_icon.png "Switch to the advanced mode") — switch to the advanced mode; every step of the price will be displayed in the depth of market, regardless of whether there are any offers at this price.
-   ![Show spread in the DOM](/en/docs/mt5/client/img/dom_spread_icon.png "Show spread in the DOM") — show the spread in the depth of market.
-   ![Show/hide Bid and Ask charts](/en/docs/mt5/client/img/dom_bidask_icon.png "Show/hide Bid and Ask charts") — show/hide the Bid and Ask price charts.
-   ![Show/hide trades](/en/docs/mt5/client/img/dom_timesales_icon.png "Show/hide trades") — show/hide transactions that appear in the form of circles on the tick chart.
-   ![Zoom in the chart](/en/docs/mt5/client/img/dom_zoomin_icon.png "Zoom in the chart") — zoom in the chart.
-   ![Zoom out the chart](/en/docs/mt5/client/img/dom_zoomout_icon.png "Zoom out the chart") — zoom out the chart.

Most of these commands are also available in the context menu of the Market Depth and Time & Sales windows. The context menu of the scalping Depth of Market (for non-exchange instruments) also allows switching between the volume in lots and units.

[Basic Principles](/en/docs/mt5/client/general_concept)

[Market Watch](/en/docs/mt5/client/market_watch)