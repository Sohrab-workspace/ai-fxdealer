# Depth of Market

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/depth_of_market

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
            -   [Main Menu](/en/docs/mt4/terminal/overview/main_menu)
            -   [Toolbars](/en/docs/mt4/terminal/overview/toolbars)
            -   [Market Watch](/en/docs/mt4/terminal/overview/market_watch)
            -   [Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)
                -   [Quick Trading](/en/docs/mt4/terminal/overview/depth_of_market/dom_quick_trading)
            -   [Data Window](/en/docs/mt4/terminal/overview/data_window)
            -   [Navigator](/en/docs/mt4/terminal/overview/navigator)
            -   [Chart Switching Bar](/en/docs/mt4/terminal/overview/charts_bar)
            -   [Client terminal](/en/docs/mt4/terminal/overview/terminal)
            -   [Tester](/en/docs/mt4/terminal/overview/strategy_tester)
            -   [Search](/en/docs/mt4/terminal/overview/search)
            -   [Fast Navigation](/en/docs/mt4/terminal/overview/fast_nav)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)Depth of Market

# Depth of Market

The depth of market displays the current market for a trading symbol. This tool provides the ability of quick and easy order management.

![Depth of Market](/en/docs/mt4/terminal/img/dom.png "Depth of Market")

To open the Depth of Market window of a financial instrument, click "![Depth of Market](/en/docs/mt4/terminal/img/dom_icon.png "Depth of Market") Depth of Market" in the context menu of the [Market Watch](/en/docs/mt4/terminal/overview/market_watch).

## List of Prices

The main part of DOM is occupied by the list of prices. The upper part (colored in red) displays Ask prices, while the lower part (colored in blue) displays Bid prices. The best depth of market prices are the current Bid and Ask for the symbol. The next level is set as the closest level allowing placing Buy Limit and Sell Limit orders considering stop level for the symbol. Further levels are set according to the symbol's price step.

The Trading column displays trader's current trade requests and stop levels ([Stop Loss](/en/docs/mt4/terminal/positions/orders#stop_loss) and [Take Profit](/en/docs/mt4/terminal/positions/orders#take_profit)). For example:

-   BL 10 — Buy Limit order of 10 lots;
-   SL 5 — Sell Limit order of 5 lots;
-   BS 1 — Buy Stop order of 1 lot;
-   SS 3 — Sell Stop order of 3 lots;
-   sl 1 — Stop Loss level of 1 lot;
-   tp 2 — Take Profit level of 2 lots.

## Trading Commands [#](depth_of_market#trade)

Traders can send market and pending orders.

### Pending Orders

Buttons for placing pending orders are located at the right side of Trading column. The order is placed at the price with a pressed button.

-   ![Set Buy Limit/Buy Stop](/en/docs/mt4/terminal/img/dom_buy_icon.png "Set Buy Limit/Buy Stop") — if this button is pressed in the Bid prices area, a Buy Limit order at a specified price will be placed; in case it is pressed in the Ask prices area, a Buy Stop order will be placed;
-   ![Set Sell Limit/Sell Stop](/en/docs/mt4/terminal/img/dom_sell_icon.png "Set Sell Limit/Sell Stop") — if this button is pressed in the Ask prices area, a Sell Limit order at a specified price will be placed; in case it is pressed in the Bid prices area, a Sell Stop order will be placed.

### Trading Settings

The lower part of DOM contains trade operation settings:

-   sl — Stop Loss level is set for placed limit orders. This parameter is specified in points from the current price;
-   vol — the volume of created market and limit orders in lots;
-   tp — Take Profit level is set for placed limit orders. This parameter is specified in points from the current price.

### Market Orders

Market order commands are located below:

-   Sell — make a Sell deal in the size specified in "vol" field at the best available price.
-   Close — this button is enabled only if there is an open position for a selected financial instrument. It allows you to close the entire position at the best available price.
-   Buy — make a Buy deal in the size specified in "vol" field at the best available price.

## Context Menu [#](depth_of_market#context)

Depth of Market has an adaptive context menu. The set of command varies depending on where it is called.

-   Buy Limit/Sell Limit — place a Buy Limit or Sell Limit order at the price, at which the context menu is called. If you open the menu in the area of sell offers, the menu suggests the Sell Limit command, in the buy offers area it suggests the Buy Limit command.
-   Sell Stop/Buy Stop — place a Sell Stop or Buy Stop order at the price, at which the context menu is called. If you open the menu in the area of sell offers, the menu suggests the Buy Stop command, in the buy offers area it suggests the Sell Stop command.
-   Take Profit — this command appears if the user has an open position for the selected symbol and a Take Profit is set for that position. Using this command the Take Profit can be moved to the price, at which the command is called.
-   Stop Loss — this command appears if the user has an open position for the selected symbol and a Stop Loss is set for that position. Using this command the Stop Loss can be moved to the price, at which the command is called.

-   Alert — create an [alert](/en/docs/mt4/terminal/overview/terminal/terminal_alerts) for a selected price. If the context menu is called in the area of sell offers, it creates "Ask > selected price" alert, in the buy offers area it creates "Bid < selected price" alert. Alerts created from the depth of market are automatically set to [expire](/en/docs/mt4/terminal/overview/terminal/terminal_alerts#expiration) in one hour.

If the context menu is opened at the line of a limit order, a Stop Loss or a Take Profit, additional commands appear:

-   Modify — open the window of modification of a selected order;
-   Delete/Cancel — cancel a selected order.

[Market Watch](/en/docs/mt4/terminal/overview/market_watch)

[Quick Trading](/en/docs/mt4/terminal/overview/depth_of_market/dom_quick_trading)