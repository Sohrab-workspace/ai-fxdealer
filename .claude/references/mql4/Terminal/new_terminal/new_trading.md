# Trading Features

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/new_terminal/new_trading

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
            -   [Trading](/en/docs/mt4/terminal/new_terminal/new_trading)
            -   [Charts](/en/docs/mt4/terminal/new_terminal/new_charts)
            -   [MQL5](/en/docs/mt4/terminal/new_terminal/new_mql5)
            -   [Tools](/en/docs/mt4/terminal/new_terminal/new_tools)
            -   [Strategy Tester](/en/docs/mt4/terminal/new_terminal/new_tester)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[New trading features](/en/docs/mt4/terminal/new_terminal)Trading

# Trading Features

In the fifth version of the terminal, trading mechanisms have undergone significant changes as compared to the fourth one. All these changes are aimed at enhancing the use of the trading platform. With the new terminal, traders can trade on any stock exchanges and through any ECN. The trading platform has already received the status of an independent software vendor (ISV) for a number of stock exchanges, including SMX, GBOT, CitiBank, Currenex, DGCX, Integral, etc. Further plans are aimed at integration with the major stock exchanges around the world.

## New Trading System

The fourth version of the trading terminal uses the order-based system allowing traders to have several positions for one symbol, including the oppositely directed ones. Protective Stop Loss and Take Profit levels can be set for each open order. These levels will be applied only to that particular order. A separate swap is charged for each open order. This swap depends on volume and direction.

The fifth version uses position-based system. For each symbol, only one position (long or short) can be open at any given moment of time. Thus, if you have a position to buy 1 lot of a financial instrument and sell one lot of this instrument, the position will be closed. If you have a position to buy 1 lot of a financial instrument and buy one more lot, you will have one position of 2 lots.

Protective Stop Loss and Take Profit levels can be set for an open position and a pending order. But unlike the previous version, when a pending order is activated, its Stop Loss and Take Profit levels will be set for the position at this symbol. In other words, specified SL/TP values for the position will be overwritten by the pending order.

## Six Types of Pending Orders

In addition to the market, limit and stop orders, the fifth version of the trading platform supports two more types of pending orders - Buy Stop Limit and Sell Stop Limit. When such an order triggers, the appropriate type of the limit order is placed. New types of orders enhance the possibilities of implementing trading strategies.

## One-Click Trading

The speed of conducting trade operations is very important in trading. The new terminal provides the possibility of instant trading in just one click. This feature is available in the Market Watch window:

![One-Click Trading](/en/docs/mt4/terminal/img/new_one_click.png "One-Click Trading")

Besides, traders can close positions and remove pending orders from Toolbox window.

## Modification of Trade Levels on the Chart

MetaTrader 5 provides the opportunity to change the price of pending orders, as well as of Stop Loss and Take Profit orders directly on the chart. Now, seeing the current situation in the market, you can easily [drag a trade level](https://www.metatrader5.com/en/terminal/help/trading/one_click_trading#pending_change "Moving trading levels using a mouse") in the desired area and then adjust its value more precisely:

![Moving trading levels using a mouse](/en/docs/mt4/terminal/img/new_trade_levels.png "Moving trading levels using a mouse")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">One-click trading from chart and managing trade levels on chart features has become available since the build 600 of the client terminal.</span></p></td></tr></tbody></table>

[New trading features](/en/docs/mt4/terminal/new_terminal)

[Charts](/en/docs/mt4/terminal/new_terminal/new_charts)