# Market Watch

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/market_watch

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)Market Watch

# Market Watch

The securities (symbols) for which the Client Terminal gets quotes from the server are listed in the "Market Watch" window.

![market_watch](/en/docs/mt4/terminal/img/market_watch.png)

The data are represented in this window as a table having several fields. The "Symbol" field contains the security name, the fields of "Bid", "Ask", and "Time" show the corresponding prices and time of their income from the server. Values of the "Maximum" and "Minimum" fields are calculated on basis of price changes within a day. The "Market Watch" window can be opened/closed by pressing of accelerating keys of Ctrl+M, by the ["View — Market Watch" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_view) command, or by pressing of the ![Open the "Market Watch" window from the "Standard" toolbar](/en/docs/mt4/terminal/img/tb_standard_market_watch.png "Open the "Market Watch" window from the "Standard" toolbar") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).

This window allows to place [market and pending orders](/en/docs/mt4/terminal/positions/orders) and open new charts. At the right mouse button click in the "Market Watch" window, the context menu will appear where the following commands are available:

-   New Order — open the "New Order" window where one can prepare and place a market or a pending order for the symbol selected. At the order preparation, one can specify the [Stop Loss and Take Profit](/en/docs/mt4/terminal/positions/orders) levels. More details can be found in the ["Positions Opening" section](/en/docs/mt4/terminal/positions/positions_control/positions_open).  
    The "New Order" window can also be opened by double clicking on the security name in the "Market Watch" window, by the ["Tools — New Order" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools) command, by the ["Terminal — Trade — New Order" window](/en/docs/mt4/terminal/overview/terminal) context menu command, the ![New Order](/en/docs/mt4/terminal/img/tb_standard_order_new.png "New Order") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard), or by pressing of F9;
-   Chart Window — open the chart of the symbol selected. More details about working with chart windows are given in the [section of the same name](/en/docs/mt4/terminal/chart_management/charts_open).  
    The symbol chart can also be opened by the ["File — New Chart"](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) and ["Window — New Window"](/en/docs/mt4/terminal/overview/main_menu/main_menu_window) menu commands and by pressing of the ![New Chart](/en/docs/mt4/terminal/img/tb_standard_new_chart.png "New Chart") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard);
-   Tick Chart — open the tick chart of the symbol selected. Unlike normal charts, the tick chart is located directly in the "Market Watch" window. The tick chart of the selected symbol can also be viewed by switching to the tab of the same name in the same window. The tick data comes only when the account is connected. Thus, if an account was not active for a certain period of time, the tick chart may appear empty in the beginning. The tick data is stored separately for each server;

-   Depth Of Market — open the [depth of market](/en/docs/mt4/terminal/overview/depth_of_market) of the symbol selected;
-   Specification — open [symbol parameters](/en/docs/mt4/terminal/overview/market_watch#specification);

-   Hide — delete (hide) the symbol from the list. To minimize the traffic, it is recommended to hide unused securities from the quotes window by this command or by pressing of the Delete button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If there are <a href="/en/docs/mt4/terminal/positions" class="topiclink">open positions</a> or <a href="/en/docs/mt4/terminal/positions/orders" class="topiclink">pending orders</a> for the symbol, or its chart is open, the symbol cannot be deleted.</span></p></td></tr></tbody></table>

-   Hide All — delete all symbols from the list. This command does not apply to securities for which there are open positions or the charts of which were opened in the current working session;
-   Show All — show the list of all available securities. After this command has been executed, quotes will income for all these symbols;
-   Symbols — call the window of the same name where there is a list of all available symbols. Symbols are grouped in the window according to their types. The "Show Symbol" command allows to add necessary symbols to the quotes window, and that of "Hide Symbol" — to delete a symbol from it. The "Properties" window command allows to view the symbol parameters;
-   Sets — open the sub-menu that manages the symbol sets. The current set of symbols can be stored in this sub-menu, as well as delete or select an already existing one. This is very comfortable when working with securities of different types;

-   Spread — show/hide column that displays spread — the difference between the bid and ask prices;

-   High/Low — add the highest and the lowest values of the daily price to the quotes displayed;
-   Time — show time of incoming quotes;
-   Auto Arrange — automatic arranging of columns when changing the window size.  
    Auto Arrange can also be enabled by pressing A button;
-   Grid — show/hide the grid separating columns.  
    The grid can also be shown by pressing G button;
-   Popup Prices — open an additional quotes window. You can also open this window by pressing F10 on your keyboard. The list of symbols in this window is the same as that in the "Market Watch" window at the moment of the command execution. This means that changes in the symbol list in the "Market Watch" window does not influence that in the "Popup Prices". It is an information window, but trading operations can also be performed from it. To do so, one has to double-click with the left mouse button on the desired security. In the context menu of this window, there are commands allowing to set up data displaying parameters, enable the full screen mode, or locate the window over all others.

## Contract Specification [#](market_watch#specification)

The symbol contract specification window contains the terms of a symbol trading. To view the symbol properties, click "Specification" in its context menu in the "Market Watch" window.

![Contract Specification](/en/docs/mt4/terminal/img/specification.png "Contract Specification")

The window displays the following parameters set by a broker:

-   Spread — spread in points. If the spread is floating, the parameter is equal to 0.
-   Digits — number of decimal places in the price of the symbol;
-   Stops level — channel of prices (in points) from the current price, inside which one cannot place [Stop Loss](/en/docs/mt4/terminal/positions/orders#stop_loss), [Take Profit](/en/docs/mt4/terminal/positions/orders#take_profit) and [pending orders](/en/docs/mt4/terminal/positions/orders#pending). When placing an order inside the channel, the server will return the "Invalid Stops" message and will not accept the order;
-   Freeze Level — level for freezing orders that are close to the current price. When an order price is as close to the market price as the value specified here or less than that, modification, deletion or closing of the corresponding position or order is prohibited;
-   Contract size — number of units of the commodity, currency or financial asset in one lot;
-   Margin currency — currency in which the margin requirements are calculated;
-   Profit calculation mode — Forex, Contracts or Futures;

-   Margin calculation mode — Forex, Contracts, Futures; Contracts Index, Contracts Leverage;

-   Margin hedge — margin charged from hedged orders for 1 lot;
-   Margin percentage — determines what part of the base margin size value calculated according to the symbol type is charged;
-   Trade — permission to trade with this instrument: "Full access" allows to close and open positions; "Close only" allows only closing; "Disabled" — full prohibit to trade;
-   Execution — execution type of the symbol: Instant, Request or Market;
-   GTC mode — expiration mode of orders:

-   Pendings are good till cancel — pending orders are preserved as a trade day changes;
-   Good till today including SL/TP — orders that are valid only during one trading day. With the end of the day, all levels of Stop Loss and Take Profit, as well as pending orders are deleted.
-   Good till today excluding SL/TP — when a trade day changes, only pending orders are deleted, Stop Loss and Take Profit levels are preserved.

-   Minimal volume — minimal volume of a deal for the symbol;
-   Maximal volume — maximal volume of a deal for the symbol;
-   Volume step — step of volume changes.
-   Swap type — type of swap calculation:

-   in points — the specified number of points of the security price.
-   in the base currency — the specified amount in the base currency of the symbol.
-   in percentage terms — as a percentage per annum. The percentage is taken from the position price (per 1 lot) and divided by 360, since the swap is calculated daily;
-   in the margin currency — the specified amount in the symbol margin currency.

-   Swap long — swap for Buy positions.
-   Swap short — swap for Sell positions;

-   3-days swaps — the day of triple swap charge;

-   First trade — a day of beginning of symbol trading;
-   Last trade — a day of end of symbol trading.

The lower part shows information about quoting and trading sessions of the symbol. Sessions are specified for every day of week.

[Timeframes](/en/docs/mt4/terminal/overview/toolbars/toolbars_periodicity)

[Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)