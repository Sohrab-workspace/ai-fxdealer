# Market Watch

> Source: https://support.metaquotes.net/en/docs/mt5/manager/market_watch

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
            -   [Basic Principles](/en/docs/mt5/manager/trade_principles)
            -   [Market Watch](/en/docs/mt5/manager/market_watch)
            -   [Market Depth](/en/docs/mt5/manager/depth_of_market)
            -   [Economic Calendar](/en/docs/mt5/manager/economic_calendar)
            -   [Trading Notifications](/en/docs/mt5/manager/trade_alerts)
            -   [Working with Trading Positions](/en/docs/mt5/manager/positions)
            -   [Working with Trading Orders](/en/docs/mt5/manager/orders)
            -   [Viewing and Editing Trading Operations](/en/docs/mt5/manager/edit_trades)
            -   [For Advanced Users](/en/docs/mt5/manager/trading_advanced)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Trading Operations](/en/docs/mt5/manager/trading)Market Watch

# Market Watch

The Market Watch window provides an overview of price data of financial instruments: quotes, price statistics and tick chart. Here you can also view contract specifications, change symbol settings and throw in quotes if you have the appropriate rights. To open this window, click ![Market Watch](/en/docs/mt5/manager/img/market_watch_icon.png "Market Watch") Market Watch in the [View](/en/docs/mt5/manager/main_menu#view) menu.

## Viewing quotes of financial instruments [#](market_watch#symbols)

The Market Watch features real-time quotes of financial instruments and other price data: spread, volume, etc.

![Market Watch](/en/docs/mt5/manager/img/market_watch.png)

Financial symbol name

Bid price

Ask price

Last price

Volume of the last executed deal

Spread — the difference between the Bid and Ask prices

Time of the last quote

The displayed data can be configured in the context menu. For example, you can show the Source field — provider of the financial instrument liquidity. Also, managers can enable the display of "raw" quotes. These quotes do not consider price spreading settings of the group the manager's account belongs to. To do this, select "![Show Raw Quotes](/en/docs/mt5/manager/img/raw_quotes_icon.png "Show Raw Quotes") Show Raw Quotes". This option appears only if the "Show row quotes without spread difference" permission is given to the manager account (granted by the platform administrator).

[When receiving trade requests](/en/docs/mt5/manager/dealing), if you enable "Track requests" option in the context menu, the Market Watch window is automatically switched to a tick chart of a symbol the request has arrived for.

A double click on one of symbols will open a window for [throwing in quotes](/en/docs/mt5/manager/quotes_symbols#quotes). A symbol chart can be opened by dragging it to the chart viewing area using a mouse (Drag'n'Drop); in this case, windows of currently open charts will be closed. If you hold down Ctrl while dragging, the chart is opened in a separate [tab](/en/docs/mt5/manager/interface), and other charts remain open.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">You cannot hide financial symbols having <a href="/en/docs/mt5/manager/positions" class="topiclink">open positions</a> or <a href="/en/docs/mt5/manager/orders" class="topiclink">pending orders</a>, as well as symbols used for profit re-calculation, from the Market Watch window.</span></li><li class="p_tableatten"><span class="f_tableatten">In the High and Low columns of symbols whose charts <a href="/en/docs/mt5/manager/market_watch#charts" class="topiclink">are built at Bid prices</a>, the Bid High and Bid Low prices are displayed. If a symbol chart is constructed using Last prices, Last High and Last Low prices are shown for this symbol. If Market Watch contains at least one symbol whose chart is drawn based on Last prices, the Last column is automatically enabled in addition to High/Low.</span></li></ul></td></tr></tbody></table>

Prices in the Market Watch window have different colors:

-   Blue — the current price is higher than the previous one;
-   Red — the current price is lower than the previous one;
-   Gray — the price has not changed for the last 15 seconds.

If the [depth of market](/en/docs/mt5/manager/depth_of_market) and the Last trade price are available for a symbol, the color is determined by the Last price. Otherwise, the color is determined by the Bid price.

The individual background coloring for symbols can also be configured on the server. This enables their visual distinguishing by types, exchange and other properties. If you do not want to use the specified coloring, enable the "Use system colors" option in the context menu.

### Fast adding of symbols

To quickly add a symbol in the Market Watch, click + below the list and enter the name of the symbol. While you type in the name, the list of suitable symbols is shown.

![To quickly add a symbol, click on + at the bottom and enter the name](/en/docs/mt5/manager/img/market_watch_fast_add.png "To quickly add a symbol, click on + at the bottom and enter the name")

Information about the current number of symbols in the Market Watch and the total number of available symbols is available at the bottom of the list.

## Viewing trade statistics of financial instruments [#](market_watch#details)

To view statistics, select a financial instrument in the Symbols tab and click Details.

![Details](/en/docs/mt5/manager/img/market_watch_details.png "Details")

The statistical information includes:

-   Bid — bid price.
-   B. High — Bid High, the highest bid price for the current day.
-   B. Low — Bid Low, the lowest bid price for the current day.
-   Ask — ask price.
-   A. High — Ask High, the highest ask price for the current day.
-   A. Low — Ask Low, the lowest ask price for the current day.
-   Last — last price, at which a deal was executed.
-   L. High — Last High, the highest price, at which a deal was executed for during the current day.
-   L. Low — Last Low, the lowest price, at which a deal was executed for during the current day.
-   Volume — volume of the last executed deal.
-   V. High — Volume High, the highest deal volume for the current day.
-   V. Low — Volume Low, the lowest deal volume for the current day.
-   Deals — total number of deals executed during the current session;
-   Deals Volume — total volume of deals executed during the current session;
-   Turnover — money turnover for a symbol for the current session;
-   Open Interest — total volume of effective contracts (futures, options) which have been settled yet;
-   Buy Orders — total number of buy requests;
-   Buy volume  — total volume of buy orders;
-   Sell Orders — total number of sell requests;
-   Sell Volume — total volume of sell orders;
-   Open Price —  open price of the last (recent) session;
-   Close Price — close price of the last (recent) session;
-   Average Weighted Price — weighted average price for a session;
-   Settlement Price — settlement (clearing) price of the previous session;
-   Price Change — indicates the difference between the last price of the instrument and the close price of the last session in percentage terms. The calculation formula depends on the [symbol charting mode](/en/docs/mt5/manager/market_watch#charts):  
       
    By Last prices: ((Last - Last price at session close)/Last price at session close)\*100  
    By Bid prices: ((Bid - Bid price at session close)/Bid price at session close)\*100.  
       
    For futures symbols, the clearing price is used instead of the the session close price, if the clearing price is provided by the broker (non-zero):  
       
    By Last prices: ((Last - Clearing price)/Clearing price)\*100  
    By Bid prices: ((Bid - Clearing price)/Clearing price)\*100.  
     
-   Delta — option delta. [The Greeks](https://www.metatrader5.com/en/terminal/help/trading/options_board#greeks), which include Delta, Theta, Gamma, Vega, Po and Omega, are quantities representing the sensitivity of the option price to changes in various parameters: strike prices, volatility, etc.
-   Theta — option theta.
-   Gamma — option gamma.
-   Vega — option vega.
-   Rho — option rho.
-   Omega — option omega.
-   Sensitivity — option sensitivity. It shows by how many points the price of the option's underlying asset should change so that the price of the option changes by one point.

## Managing symbols [#](market_watch#manage)

You can show and hide symbols in the Market Watch window, as well as view their properties. To do this, click ![Symbols](/en/docs/mt5/manager/img/symbols_icon.png "Symbols") Symbols in the Market Watch window context menu.

![Symbols](/en/docs/mt5/manager/img/symbols.png "Symbols")

All symbols available in the terminal are displayed here. A double click on a symbol name is used for hiding or showing it in the Market Watch window. The same actions can be performed by selecting it and clicking Show or Hide.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">You cannot hide financial symbols having <a href="/en/docs/mt5/manager/positions" class="topiclink">open positions</a> or <a href="/en/docs/mt5/manager/orders" class="topiclink">pending orders</a>, as well as symbols used for profit re-calculation, from the Market Watch window.</span></p></td></tr></tbody></table>

[Specification](/en/docs/mt5/manager/market_watch#specification) of a selected symbol is displayed at the bottom of the window.

To quickly find a symbol, use the filter in the upper part of the window. Type the first letters of the symbol name or description in it. A list of symbols corresponding to the search string appears below.

All expired symbols are hidden to preserve a more compact display. This is particularly convenient when working on the futures market. A non-relevant symbol is the expired one, which is defined by the ["Last trade"](/en/docs/mt5/manager/market_watch#specification) parameter. This date is specified in the Expiration column of the list of symbols. To view all symbols, click "Show expired contracts".

## Viewing symbol specification [#](market_watch#specification)

The symbol contract specification window contains the terms of a symbol trading. To see the symbol specification, click "![Specification](/en/docs/mt5/manager/img/specification_icon.png "Specification") Specification" in the context menu of the Market Watch window.

![Symbol specification](/en/docs/mt5/manager/img/contract_specification.png "Symbol specification")

The following set of parameters is specified here:

-   Symbol name and description — name of a symbol and its short description. This parameter can be a link to a website containing symbol information. A pop-up tip with the link address appears when you hover the mouse over it.
-   Spread — spread in points. If the spread is floating, then the appropriate record is specified in this point (floating).
-   Digits — number of decimal places in the price of the symbol.
-   Stops level — channel of prices (in points) from the current price, inside which one cannot place [stop loss](/en/docs/mt5/manager/trade_principles#stop_loss), [take profit](/en/docs/mt5/manager/trade_principles#take_profit) and pending orders. If you try to place an order inside the channel, the server will return Invalid Stops and will not accept the order.
-   Contract size — number of units of the commodity, currency or financial asset in one lot.
-   Margin currency — currency, in which the margin requirements are calculated.
-   Profit currency — currency, in which the profit of the symbol trading is calculated.
-   Calculation — method of profit and [margin](/en/docs/mt5/manager/trading_advanced/margin_formula) calculation: Forex, Forex No Leverage, CFD, CFD Leverage, CFD Index, Futures, Exchange Futures, Exchange Stocks, Exchange MOEX Stocks, Exchange Bonds, Exchange MOEX Bonds, FORTS Futures, Collateral.
-   Chart mode — symbol chart (bar) construction mode: by last deal prices (Last) or by Bid prices. The first option is usually used for exchange instruments.
-   Tick size — minimum price change step.
-   Tick value — cost of a single price change point.
-   Initial margin — security deposit (margin) provided for a fixed-term contract to perform a one-lot deal. If the initial margin value is specified for the symbol, this is the value that is used. [Margin](/en/docs/mt5/manager/trading_advanced/margin_formula#fixed) calculation equations are not applied to the appropriate calculation type.
-   Maintenance margin — minimum security deposit (margin) a trader should have on his or her account to maintain a one-lot position.
-   Hedged margin — margin charged per one lot of [hedged](/en/docs/mt5/manager/trading_advanced/margin_forex_hedge#hedged) positions. Margin calculation mode using the larger leg for hedged positions can also be specified here.
-   Margin rate — margin rates for various order types are specified in this table. The rates are set for the initial and maintenance margin individually. If no ratio is set for the maintenance margin (set to zero), the initial margin ratio will be used for it.
    -   Market Buy Order — multiplier for calculating margin requirements for long positions relative to the [basic margin amount](/en/docs/mt5/manager/trading_advanced/margin_formula).
    -   Market Sell Order — multiplier for calculating margin requirements for short positions relative to the main amount of margin.
    -   Buy limit — multiplier for calculating margin requirements for Buy Limit orders relative to the main amount of margin.
    -   Sell limit — multiplier for calculating margin requirements for Sell Limit orders relative to the main amount of margin.
    -   Buy stop — multiplier for calculating margin requirements for Buy Stop orders relative to the main amount of margin.
    -   Sell stop — multiplier for calculating margin requirements for Sell Stop orders relative to the basic margin amount.
    -   Buy stop limit — multiplier for calculating margin requirements for Buy Stop Limit orders relative to the main amount of margin.
    -   Sell stop limit — multiplier for calculating margin requirements for Sell Stop Limit orders relative to the main amount of margin.
-   Trade — symbol trading mode (full access, long only, short only, close only). Also, trading can be completely prohibited.
-   Execution — [execution mode](/en/docs/mt5/manager/trade_principles#execution_type): Instant, Request, Market, Exchange.
-   Type of orders — types of orders placed:
    -   Good till today including SL/TP — orders that are valid only during one trading day. With the end of the day, all of the stop loss and take profit levels, as well as pending orders are deleted.
    -   Good till canceled — pending orders are preserved as a trade day changes.
    -   Good till today excluding SL/TP — only pending orders are deleted at the end of a trading day, while [stop loss](/en/docs/mt5/manager/trade_principles#stop_loss) and [take profit](/en/docs/mt5/manager/trade_principles#take_profit) levels are preserved.
-   Filling — available order [fill policies](/en/docs/mt5/manager/trade_principles#fill_policy): Fill or Kill, Immediate or Cancel, Book or Cancel, Return.
-   Expiration — available [types of expiration](/en/docs/mt5/manager/orders#expiration) of pending orders:
    -   Good till Canceled — order lifetime is unlimited.
    -   Intraday — orders are canceled at the end of the current trading.
    -   Specified time — order is canceled in a user-specified time.
    -   Date — order is canceled at the end of a day specified by a user.
-   Orders— allowed [order types](/en/docs/mt5/manager/trade_principles): market, limit, stop, stop-limit, stop loss and take profit.
-   Minimal volume — minimal volume of a deal for a symbol.
-   Maximal volume — maximal volume of a deal for a symbol.
-   Volume step — step of volume changes.
-   Swap type — type of swap calculation:
    -   In points — specified number of points of a security price.
    -   In the base currency — specified amount in a base currency of a symbol.
    -   In the margin currency — specified amount in a symbol margin currency;
    -   In the deposit currency — specified amount in a deposit currency.
    -   As a percentage of current price — specified percentage of a symbol price at the time of calculation of the swap.
    -   As a percentage of the open price — specified percentage of a position open price;
    -   In points, re-open at Close price — at the end of the trading day, a position is closed. The next day, the position is re-opened at the Close price +/- the specified number of points.
    -   In points, re-open at the Bid price — at the end of the trading day, a position is closed. The next day, the position is re-opened at the Bid price +/- the specified number of points.
-   Swap long — swap for Buy positions.
-   Swap short — swap for Sell positions.
-   3-days swap — day of the week when a triple swap is charged.
-   Category — the property is used for additional marking of financial instruments. For example, this can be the market sector to which the symbol belongs: Agriculture, Oil & Gas and others.
-   Exchange — the name of the exchange in which the security is traded.
-   CFI — instrument classification in accordance with the [ISO 10962](https://www.iso.org/standard/44799.html) standard.
-   Sector — economic sector the instrument belongs to, such as energy, finance, healthcare and others.
-   Industry — industry branch the instrument belongs to, such as sportswear and accessories, car manufacturing, restaurant business and others.
-   Country — country of the company whose shares are traded on the stock exchange.
-   Option type — call or put.
-   Underlying — the underlying symbol of the option.
-   Strike price — option strike price.

### Commission

Information on [commissions](/en/docs/mt5/manager/groups#commission) charged by a broker for the symbol deals. Calculation details are displayed here:

-   Commission may be single-level and multilevel, i.e. be equal regardless of the deal volume/turnover or can depend on their size. Appropriate data is displayed in the terminal.
-   Commission can be charged immediately upon deal execution or at the end of a trading day/month.
-   Commission can be charged depending on deal direction: entry, exit or both operation types.
-   Commission can be charged per lot or deal.
-   Commission can be calculated in money, percentage or points.

For example, the following entry means that a commission is charged immediately upon deal entry and exit. If the deal volume is from 0 to 10 lots, a commission of 1.2 USD is charged per operation. If the deal volume is 11 to 20 lots, a commission of 1.1 USD is charged per each lot of the deal.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Commission&nbsp;|&nbsp;Instant,&nbsp;volume,&nbsp;entry/exit&nbsp;deals</span><br><span class="f_CodeExample">0&nbsp;&nbsp;-&nbsp;10&nbsp;&nbsp;&nbsp;|&nbsp;1.2&nbsp;USD&nbsp;per&nbsp;deal</span><br><span class="f_CodeExample">11&nbsp;-&nbsp;20&nbsp;&nbsp;&nbsp;|&nbsp;1.1&nbsp;USD&nbsp;per&nbsp;loat</span></p></td></tr></tbody></table>

### Sessions [#](market_watch#sessions)

The lower part shows information about quoting and trading sessions of the symbol. Sessions are specified for every day of a week.

### Spreads [#](market_watch#spreads)

The margin can be charged on preferential basis in case trading positions are in spread relative to each other. The spread trading is defined as the presence of the oppositely directed positions of correlated symbols. Reduced margin requirements provide more trading opportunities for traders.

More detailed information on spread can be found in the [appropriate section](/en/docs/mt5/manager/trading_advanced/spreads).

## Editing statistical data [#](market_watch#edit)

The manager terminal allows editing statistical data on a symbol. Open its context menu and click ![Statistics](/en/docs/mt5/manager/img/statistics_edit_icon.png "Statistics") Statistics.

![Editing statistical data](/en/docs/mt5/manager/img/statistics_edit.png "Editing statistical data")

In this window, you can edit all statistical data shown in the [Details](/en/docs/mt5/manager/market_watch#details) tab. If you click Update, the current values from the server will be inserted to the fields. Click Send to save the changed values.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If you hold one of the below buttons when clicking arrows, the value will change by a certain amount:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Holding Shift — by 5 points;</span></li><li class="p_tableatten"><span class="f_tableatten">Holding Ctrl — by 10 points;</span></li><li class="p_tableatten"><span class="f_tableatten">Holding Ctrl+Shift — by 50 points.</span></li></ul></td></tr></tbody></table>

# Viewing tick data

Tick chart— the most detailed chart of symbol prices, where all received symbol quotes are shown. To view a tick chart of a symbol, select it in the [Market Watch](/en/docs/mt5/manager/market_watch) window and go to the Ticks tab.

![Ticks](/en/docs/mt5/manager/img/tick_chart.png "Ticks")

To change the horizontal chart scale, left-click on the timeline and move the cursor right or left holding the mouse button.

The context menu of the Ticks tab features the following commands:

-   Current — show data only for the last time period that can fit in the current window.
-   Request — open the window for requesting deeper tick data from the server. Specify the time interval in the new window and click OK. Data are downloaded from the server and displayed on the tab.
-   Save — save tick data in a \*.CSV file. If the Current option is enabled, the current day tick data is saved. When you select a different period, tick data for the relevant time period will be saved.
-   Auto Scroll — enable/disable automatic chart scrolling to its beginning when new ticks are received.
-   Crosshair — enable/disable the Crosshair mode of the cursor. This mode allows viewing exact prices at any point of the chart.
-   Bid Line — show/hide the bid line (red) in the chart.
-   Ask Line — show hide the ask line (blue) in the chart.
-   Last Line — show/hide the line of the last price of an executed deal (green line) for a stock exchange symbol.
-   Grid — show/hide grid in the chart.

[Basic Principles](/en/docs/mt5/manager/trade_principles)

[Market Depth](/en/docs/mt5/manager/depth_of_market)