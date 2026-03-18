# Testing Visualization

> Source: https://support.metaquotes.net/en/docs/mt5/client/visualization

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
            -   [Expert Advisors and Custom Indicators](/en/docs/mt5/client/trade_robots_indicators)
            -   [Where to Find Trading Robots and Indicators](/en/docs/mt5/client/algotrading_get_ea_indicator)
            -   [How to Create an Expert Advisor or an Indicator](/en/docs/mt5/client/autotrading)
            -   [Strategy Testing](/en/docs/mt5/client/testing)
            -   [How the Tester Downloads Historical Data](/en/docs/mt5/client/test_preparation)
            -   [Strategy Optimization](/en/docs/mt5/client/strategy_optimization)
            -   [Testing Features](/en/docs/mt5/client/testing_features)
            -   [Testing Report](/en/docs/mt5/client/testing_report)
            -   [Testing Visualization](/en/docs/mt5/client/visualization)
            -   [Journal of Testing](/en/docs/mt5/client/tester_journal)
            -   [Optimization Types](/en/docs/mt5/client/optimization_types)
            -   [Real and Generated Ticks](/en/docs/mt5/client/tick_generation)
            -   [MetaTester and Remote Agents](/en/docs/mt5/client/metatester)
            -   [Global Variables](/en/docs/mt5/client/service_global)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)Testing Visualization

# Testing Visualization

In the [Strategy Tester](/en/docs/mt5/client/testing) of the trading platform, you can test Expert Advisors and indicators in the visual mode. This mode allows to visualize exactly how the Expert Advisor performs trade operations during backtesting. Each trade of a financial instrument is displayed on its [chart](/en/docs/mt5/client/visualization#chart). In the visual testing mode, you can test the operation of an [indicator](/en/docs/mt5/client/testing#indicator) using historical data. This feature allows to easily test the operation of demo versions of indicators downloaded from the [Market](/en/docs/mt5/client/market).

## Start [#](visualization#start)

To start the visual testing:

-   Enable the "Visualization" option in the [Strategy Tester](/en/docs/mt5/client/testing#settings) settings. When you select testing of [indicators](/en/docs/mt5/client/trade_robots_indicators), the visualization is enabled automatically.
-   Disable [the optimization mode](/en/docs/mt5/client/testing#settings), because visualization is only available in the testing mode.
-   Make sure that one of [local agents](/en/docs/mt5/client/strategy_optimization#agents) is used for testing. If [a remote agent](/en/docs/mt5/client/strategy_optimization#farm) is selected for testing, choose a local one using the "![Select](/en/docs/mt5/client/img/agent_select_icon.png "Select") Select" command in its context menu.

If all of the above conditions are met, clicking on the "Start" button opens [the visualization window](/en/docs/mt5/client/visualization#view).

## Viewing the Testing Process [#](visualization#view)

Testing Visualizer runs in a separate window:

![Testing Visualization](/en/docs/mt5/client/img/visualization.png "Testing Visualization")

Information about the testing process is available in several forms:

-   [Price chart](/en/docs/mt5/client/visualization#chart), where trade operations are shown.
-   [Market Watch](/en/docs/mt5/client/visualization#market_watch), which shows prices generated during testing.
-   [Data Window](/en/docs/mt5/client/visualization#data_window), where you can view information about a selected point on the chart.
-   The multifunctional [Toolbox](/en/docs/mt5/client/visualization#toolbox) window that displays trade operations performed by an Expert Advisor during testing and logs of the visualizer.

## Chart [#](visualization#chart)

A chart is the primary means of testing process visualization. It is similar to conventional [charts](/en/docs/mt5/client/charts) of the platform, but has a number of specific features:

-   The chart is based on price data [generated](/en/docs/mt5/client/tick_generation) during testing.
-   All trade operations performed by an Expert Advisor during testing are shown on the chart. Trading operations are displayed using the "Buy sign" and "Sell sign" [objects](/en/docs/mt5/client/objects/arrows).
-   Only the basic chart settings (type, grid, scale) are available.
-   A list of symbols available in the chart mode is limited to the main testing symbol, as well as the symbols whose data are used by the Expert Advisor.
-   [The chart timeframe](/en/docs/mt5/client/charts#operations) cannot be changed. The [period](/en/docs/mt5/client/testing#settings) selected in the settings is used for the main testing chart. Periods requested by the Expert Advisor are used for other symbols.
-   To switch between symbols, use the "View — Charts" menu.
-   The chart allows you to view the behavior of the indicator based on historical data, for example, when testing a demo version of the indicator downloaded from the [Market](/en/docs/mt5/client/market).

![Chart](/en/docs/mt5/client/img/visualization_chart.png "Chart")

### Using a Template

You can change the appearance of a chart, show indicators or graphical objects on it using [templates](/en/docs/mt5/client/charts_advanced/templates_profiles). For a template to be applied, its name must match the name of the tested Expert Advisor. The template should be placed in folder [/profiles/templates](/en/docs/mt5/client/start_advanced/structure) of the trading platform.

## Market Watch [#](visualization#market_watch)

The Market Watch window shows prices generated during testing. It is similar to the Market Watch of the [trading platform](/en/docs/mt5/client/market_watch), but has some specific features. To show/hide this window, use the Market Watch command in the View menu or press Ctrl+M.

The Symbols tab features the current price information of financial instruments. The list of displayed symbols is limited to the [main testing symbol](/en/docs/mt5/client/testing#settings), as well as the symbols whose data are used by the Expert Advisor.

The window header contains the current time of testing.

![Market Watch](/en/docs/mt5/client/img/visualization_mw.png "Market Watch")

The Ticks tab contains a chart of prices [generated](/en/docs/mt5/client/tick_generation) during testing. The number of displayed ticks is limited to 64 thousand.

## Data Window [#](visualization#data_window)

This window is used to display information about the prices (OHLC), date and time of a bar, spread, volume and [indicators](/en/docs/mt5/client/indicators). Here you can quickly find information about a particular bar and applied indicators at a selected point of the chart. The window can be enabled or disabled by clicking "Data Window" in the View menu or pressing Ctrl+D.

![Data Window](/en/docs/mt5/client/img/data_window.png "Data Window")

The upper part of the window contains the name of a financial instrument and the chart period. Information about the current cursor position on the chart is shown below. Information about [indicators](/en/docs/mt5/client/indicators) open in separate subwindows is shown in separate blocks.

## Toolbox [#](visualization#toolbox)

Toolbox is a multifunctional window, in which you can view an Expert Advisor's trading activity during testing, as well as view the journal of [a testing agent](/en/docs/mt5/client/strategy_optimization#agents). To show/hide this window, use the Toolbox command in the View menu or press Ctrl+T keys.

The Toolbox window consists of several tabs:

-   [Trade](/en/docs/mt5/client/visualization#toolbox_trade) — current positions and pending orders.
-   [History](/en/docs/mt5/client/visualization#toolbox_history) — the history of deals and orders.
-   [Operations](/en/docs/mt5/client/visualization#toolbox_operations) — a list of trading operations requested by the Expert Advisor.
-   [Journal](/en/docs/mt5/client/visualization#toolbox_journal) — the journal of a testing agent.

### Trade [#](visualization#toolbox_trade)

The "Trade" tab contains information about the current state of the trading account, [open positions](/en/docs/mt5/client/performing_deals#position_open) and placed [pending orders](/en/docs/mt5/client/performing_deals#pending). All open positions can be sorted by any field. To do this, click on its name.

![Trading](/en/docs/mt5/client/img/visualization_trade.png "Trading")

Positions

Positions are shown in a table with the following fields:

-   Symbol — a financial instrument of the open position.
-   Time — position opening time. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Type — position type: "Buy" — long, "Sell" — short.
-   Volume — volume of a trade operation (in lots or units);
-   Price — the price of a deal, as a result of which the position was opened. If the opened position is a result of execution of several deals, then this field displays their weighted average price: (price of deal 1 \* volume of deal 1 + ... + price of deal N \* volume of deal N) / (volume of deal 1 + ... + volume of deal N). The number of characters in this field is determined by the number of characters in the price of the symbol plus three additional characters;
-   S/L — the [Stop Loss](/en/docs/mt5/client/general_concept#stop_loss) level of the current position. If this order was not placed, a zero value is shown in the field;
-   T/P — the [Take Profit](/en/docs/mt5/client/general_concept#take_profit) level of the current position. If this order was not placed, a zero value is shown in the field;
-   Price — the current price of the financial symbol.
-   Commission — commission charged for the execution of the trade operation;
-   Swap — amount of swaps charged;
-   Profit — the financial result of a deal taking into account the current price is written in this field. A positive result indicates the profitability of the deal, negative indicates loss.

Account state

The current account state is shown below the open trading positions:

-   Balance — amount of money on the account, the results of currently open positions are not included.
-   Equity — the amount of money taking into account the results of the currently open positions;
-   Margin — money required to cover open positions.
-   Free Margin — the free amount of money that can be used to maintain open positions;
-   Margin Level — percentage of the account equity to the margin volume;
-   Total of deals — total financial result of all open positions. With the positive result of positions, icon ![Balance increase](/en/docs/mt5/client/img/balance_up_icon.png "Balance increase") is shown, with negative — ![Balance decrease](/en/docs/mt5/client/img/balance_down_icon.png "Balance decrease").

Pending orders

Placed pending orders are shown below the current account state:

-   Symbol — the financial instrument of the pending order.
-   Order — the ticket number (a unique identifier) of the pending order;
-   Time — pending order placing time. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Type — [type of the pending order](/en/docs/mt5/client/general_concept#pending_order): "Sell Stop", "Sell Limit", "Buy Stop", "Buy Limit", "Buy Stop Limit" or "Sell Stop Limit";
-   Volume — volume requested in the pending order, and volume covered by the deal (in lots or units).
-   Price — price reaching which the pending order will trigger.
-   S/L — level of the placed [Stop Loss order](/en/docs/mt5/client/general_concept#stop_loss). If this order was not placed, a zero value is shown in the field;
-   T/P — level of the set [Take Profit](/en/docs/mt5/client/general_concept#take_profit) order. If this order was not placed, a zero value is shown in the field;
-   Price — the current price of the financial symbol.
-   Comment — comments to the pending order;
-   State — in the last column, the current [status](/en/docs/mt5/client/general_concept#order_state) of the pending order is shown: "Started", "Placed", etc.

## History [#](visualization#toolbox_history)

The history of trade operations is available in the History tab. There are three modes of viewing the history of trade operations: only deals, only orders, deals and orders; you can switch between them in the context menu.

### Orders [#](visualization#order)

![Orders](/en/docs/mt5/client/img/visualization_history_orders.png "Orders")

The history of placed orders is displayed in a table with the following fields:

-   Time — order placing time. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Order — ticket number (a unique identifier) of a trade operation;
-   Symbol — a financial instrument of the order;
-   Type — trading operation type: "Buy" — a long position, "Sell" — a short position or names of [Pending orders](/en/docs/mt5/client/general_concept#pending_order) "Sell Stop", "Sell Limit", "Buy Stop", "Buy Limit", "Buy Stop Limit" and "Sell Stop Limit".
-   Volume — volume requested in the order (in lots or units). The minimal volume and its change step are limited by a brokerage company, the maximal one — by the deposit size.
-   Price — price specified in the order at which the trade operation should be executed.
-   S/L — level of the placed [Stop Loss order](/en/docs/mt5/client/general_concept#stop_loss). If the trade position of the order has closed, the cell is colored red, and a record "\[s/l\]" appears in the comment box. If this order was not placed, a zero value is recorded in this field;
-   T/P — level of the set [Take Profit](/en/docs/mt5/client/general_concept#take_profit) order. If the trade position of the order has closed, the cell is colored green, and a record "\[t/p\]" appears in the comment box . If this order was not placed, a zero value is recorded in this field;
-   State — order [placing result](/en/docs/mt5/client/general_concept#order_state): "Filled", "Partial", "Canceled" etc.
-   Comment — comments to orders are written here.

The lower line shows the summary of orders: total quantity, number of filled and canceled orders.

### Deals [#](visualization#deal)

![Deals](/en/docs/mt5/client/img/visualization_history_deals.png "Deals")

The history of deals is also displayed in a table with the following fields:

-   Time — time of the deal. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Deal — ticket number (a unique identifier) of a deal.
-   Order — ticket number (a unique identifier) of the order, the trade was executed for. Several deals can correspond to one order, if the required volume specified in the order was not covered by one market offer;
-   Symbol — a financial instrument of the deal.
-   Type — type of a trade operation: "Buy" — a buy deal, "Sell" — a sell deal;
-   Direction — direction of the deal relative to the current position on a particular symbol: "in", "out" or "in/out".
-   Volume — volume of an executed deal (in lots or units).
-   Price — the price at which the deal was executed;
-   Commission — commission charged for the deal execution;
-   Profit — the financial result of the position exiting. For entry deals, zero profit is shown.

The bottom line shows the trade execution results relative to the initial deposit:

-   Profit — profit or loss relative to the initial deposit. For losses, the ![Loss](/en/docs/mt5/client/img/balance_down_icon.png "Loss") sign is shown in this field, for profit — ![Profit](/en/docs/mt5/client/img/balance_up_icon.png "Profit");
-   Deposit — the amount of deposit;
-   Withdrawal — amount withdrawn from the account.

The value of the current balance of the account is shown at the end of the line.

### Orders and Trades [#](visualization#orders_deals)

![History](/en/docs/mt5/client/img/visualization_history_ordersdeals.png "History")

In this mode, orders and deals are displayed as a tree that shows how exactly the trade requests were processed.

## Operations [#](visualization#toolbox_operations)

All trade requests made by an Expert Advisor during testing are shown in the Operations tab. In addition to buy and sell requests, you can track the modifications of pending orders, stop levels of positions, etc.

![Operations](/en/docs/mt5/client/img/visualization_operations.png "Operations")

The history of trade operations is displayed in a table with the following fields:

-   Time — time of the trade operation request. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Ticket — ticket number (unique number) of a trade operation;
-   Symbol — the symbol of a requested trade operation;
-   Action — type of a requested action (instant execution of a trade operation, modification of stop levels, etc.);
-   Type — direction of a trade operation (buy or sell);
-   Volume — the volume of a requested trade operation;
-   Price — the price at which the trade operation is requested;
-   S/L — the [Stop Loss](/en/docs/mt5/client/general_concept#stop_loss) level in a trade request;
-   T/P — the [Take Profit](/en/docs/mt5/client/general_concept#take_profit) level in a trade request;
-   Comment — a comment to a request.

## Journal [#](visualization#toolbox_journal)

This tab contains the logs of the [agent](/en/docs/mt5/client/strategy_optimization#agents) that is used for testing an Expert Advisor. All actions of the agent and the Expert Advisor during testing are logged in the Journal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">As long as the visualizer is open, the logs of testing agents are not sent to the <a href="/en/docs/mt5/client/testing" class="topiclink">Strategy Tester</a> of the trading platform. Nevertheless, they can be viewed via the trading platform using the "Journals of local agents" command in the context menu.</span></p></td></tr></tbody></table>

![Journal](/en/docs/mt5/client/img/visualization_journal.png "Journal")

Log entries consist of two parts:

-   Date — date and time of the event;
-   Message — description of the event.

[Testing Report](/en/docs/mt5/client/testing_report)

[Journal of Testing](/en/docs/mt5/client/tester_journal)