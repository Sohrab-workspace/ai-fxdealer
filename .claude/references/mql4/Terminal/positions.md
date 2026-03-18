# Trading

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/positions

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)Trading

# Trading

The fundamental and simple rule of profitable trading at financial markets is to buy cheaper and sell dearer. Thus, the entire trading activities at financial markets come to the successive operations performed to sell or buy securities. To do so, one has to open, modify, and close trade positions. Trade position is a market commitment (order), the number of bought or sold contracts for which no set-off transactions have been made. The entire trading in the terminal is implemented through trade positions.

To open a trade position, one has to make a transaction, and to close a position, one has to make an inverse operation. A position can be opened by a brokerage company at a market order or at execution of a pending order. An open position can be modified if values of the [Stop Loss and Take Profit orders](/en/docs/mt4/terminal/positions/orders) levels attached to the position are changed. Positions can be closed on the trader's demand or at execution of Stop Loss or Take Profit orders. Besides, positions can be opened, modified, or closed with an expert advisor — this mechanism is described in [another section](/en/docs/mt4/terminal/autotrading/experts).

### New trading features

The fifth generation platform supports two order accounting modes: the netting mode is adopted on exchange markets, while the hedging method can be used for Forex trading. With the netting system, the trader will be able to have only one open position of a financial instrument at a time. The volume of that position can be increased or reduced through any further operation on the same symbol. With the hedging system, any new deal on a financial instrument opens a new position. Individual Stop Loss and Take Profit levels can be set for each of the open positions.

Thus, the new platform allows you to trade both on Forex and exchanges. Time & Sales with real volumes and order levels, as well as manual trading [inside the Depth of Market](https://www.metatrader5.com/en/terminal/help/trading/depth_of_market#quick_trading) and developing scalper strategies based on the order book and liquidity are available for you in order to trade on an exchange. The expanded Depth of Market featuring volumes and the appropriate MQL5 functions allow you to develop custom symbols for intraday trading.

![dom_extended](/en/docs/mt4/terminal/img/dom_extended.png)

In the new platform, MQL5 programs work up to 20 times faster than MQL4 ones making them comparable to C++ programs. Combined with asynchronous operations, this allows the development of trading robots with a high speed of response to price changes. Such speed is required in pair trading, scalping strategies, arbitrage and other similar trading systems where fast obtaining of market data, high data processing speed and instant sending of orders are of utmost importance.

While developing such robots, you can [use real ticks](https://www.mql5.com/en/articles/2612) to test strategies trading on multiple symbols. The entire trading environment is reproduced as accurately as possible and ticks are synchronized across all used instruments up to milliseconds.

[Williams' Percent Range](/en/docs/mt4/terminal/analytics/tech_indicators/williams_percent_range)

[Order Types](/en/docs/mt4/terminal/positions/orders)