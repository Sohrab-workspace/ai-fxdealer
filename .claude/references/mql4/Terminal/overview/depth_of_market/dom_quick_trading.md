# Quick Trading from Depth of Market

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/depth_of_market/dom_quick_trading

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)Quick Trading

# Quick Trading from Depth of Market

Depth of Market allows users to quickly manage stop levels (Stop Loss and Take Profit) and pending orders of open positions. To do this, enable ["One-click trading"](/en/docs/mt4/terminal/setup/setup_trade#one_click) in the client terminal's settings. Trade requests are sent from Depth of Market instantly without showing a trading dialog.

## Moving Stop Levels

Stop levels of open positions are displayed in Trading column as TP (Take Profit) and SL (Stop Loss). These levels can be moved by mouse:

![Moving stop levels](/en/docs/mt4/terminal/img/dom_stops_move.png "Moving stop levels")

Move the level to the line with the necessary to change it instantly.

## Deleting Stop Levels

Stop levels can be deleted from Depth of Market:

![Deleting stop levels](/en/docs/mt4/terminal/img/dom_stops_delete.png "Deleting stop levels")

Hover the mouse cursor over the button ![Set Sell Limit/Sell Stop](/en/docs/mt4/terminal/img/dom_sell_icon.png "Set Sell Limit/Sell Stop") (or ![Set Buy Limit/Buy Stop](/en/docs/mt4/terminal/img/dom_buy_icon.png "Set Buy Limit/Buy Stop") ) to the right or left from the level and click Shift. The button will change its view to ![Delete level](/en/docs/mt4/terminal/img/dom_order_delete_button.png "Delete level"). Click the button to delete the level.

## Placing Orders

[Pending orders](/en/docs/mt4/terminal/positions/orders#pending) are placed using the buttons ![Set Buy Limit/Buy Stop](/en/docs/mt4/terminal/img/dom_buy_icon.png "Set Buy Limit/Buy Stop") and ![Set Sell Limit/Sell Stop](/en/docs/mt4/terminal/img/dom_sell_icon.png "Set Sell Limit/Sell Stop") against a necessary price:

-   To place a Buy Limit order, click ![Set Buy Limit](/en/docs/mt4/terminal/img/dom_buy_icon.png "Set Buy Limit") in the Bid price area.
-   To place a Buy Stop order, click ![Set Buy Stop](/en/docs/mt4/terminal/img/dom_buy_icon.png "Set Buy Stop") in the Ask price area.

-   To place a Sell Limit order, click ![Set Sell Limit](/en/docs/mt4/terminal/img/dom_sell_icon.png "Set Sell Limit") in the Ask price area.
-   To place a Sell Stop, click ![Set Sell Stop](/en/docs/mt4/terminal/img/dom_sell_icon.png "Set Sell Stop") in the Bid price are.

![Placing a limit order](/en/docs/mt4/terminal/img/dom.png "Placing a limit order")

After that, an order will be placed at the specified price. It will have the volume set in "vol" field, as well as Stop Loss and Take Profit levels specified in "sl" and "tp" fields, respectively.

## Changing orders

Depth of Market allows users to easily change prices of previously set orders.

![Moving a limit order](/en/docs/mt4/terminal/img/dom_pending_move.png "Moving a limit order")

Move the pending order to the necessary price line. Order price will be changed instantly. If the Stop Loss and Take Profit levels are set for the order, they will be moved on the same distance as the price.

If we drag a limit order through ask/bid border, it will change to a stop order (Buy Limit will be replaced by Buy Stop, while Sell Limit - by Sell Stop).

![Changing order type](/en/docs/mt4/terminal/img/dom_pending_change_type.png "Changing order type")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If several same price orders are placed, they cannot be moved in Depth of Market.</span></p></td></tr></tbody></table>

## Deleting Orders

To delete the order from the Depth of Market, hover the mouse cursor over ![Set Sell Limit](/en/docs/mt4/terminal/img/dom_sell_icon.png "Set Sell Limit") (or ![Set Buy Limit](/en/docs/mt4/terminal/img/dom_buy_icon.png "Set Buy Limit") ) button to the right and click Shift. The button will change its view to ![Delete level](/en/docs/mt4/terminal/img/dom_order_delete_button.png "Delete level"). Click the button to delete the order.

![Delete a pending order](/en/docs/mt4/terminal/img/dom_pending_delete.png "Delete a pending order")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If several same price orders are placed, the oldest one is removed first.</span></p></td></tr></tbody></table>

[Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)

[Data Window](/en/docs/mt4/terminal/overview/data_window)