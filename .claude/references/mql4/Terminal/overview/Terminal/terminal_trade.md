# Trade

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/terminal/terminal_trade

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
                -   [Trade](/en/docs/mt4/terminal/overview/terminal/terminal_trade)
                -   [Exposure](/en/docs/mt4/terminal/overview/terminal/toolbox_exposure)
                -   [Account History](/en/docs/mt4/terminal/overview/terminal/terminal_account_history)
                -   [News](/en/docs/mt4/terminal/overview/terminal/terminal_news)
                -   [Alerts](/en/docs/mt4/terminal/overview/terminal/terminal_alerts)
                -   [Mailbox](/en/docs/mt4/terminal/overview/terminal/terminal_mailbox)
                -   [Company](/en/docs/mt4/terminal/overview/terminal/toolbox_company)
                -   [Market](/en/docs/mt4/terminal/overview/terminal/toolbox_market)
                -   [Signals](/en/docs/mt4/terminal/overview/terminal/toolbox_signals)
                -   [Code Base](/en/docs/mt4/terminal/overview/terminal/toolbox_codebase)
                -   [Search](/en/docs/mt4/terminal/overview/terminal/toolbox_search)
                -   [Experts](/en/docs/mt4/terminal/overview/terminal/terminal_experts)
                -   [Journal](/en/docs/mt4/terminal/overview/terminal/terminal_journal)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Client terminal](/en/docs/mt4/terminal/overview/terminal)Trade

# Trade

The "Trade" tab contains information about the current status of the trading account, about [open positions](/en/docs/mt4/terminal/positions) and [pending orders placed](/en/docs/mt4/terminal/positions/orders).

![trade](/en/docs/mt4/terminal/img/trade.png)

All open positions can be sorted by any field. Then there is a line of the account balance and financial result of open positions followed by the list of pending orders. When a pending order triggers, a new position will be opened and the pending order line will be replaced with that of the position opened.

## Trade Operations

All trade operations are displayed as a table having the following fields (from left to right):

-   Order — the operation ticket number. It is a unique number of the trade operation;
-   Time — time of position opening. The time is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute). This is the time at which the position was opened;
-   Type — type of the trade operation. There are several types of trading operations that can appear here: "Buy" — long position, "Sell" — short position, and [pending orders named Sell Stop, Sell Limit, Buy Stop, and Buy Limit](/en/docs/mt4/terminal/positions/orders);
-   Size — the amount of lots participating in operation. The minimum amount of lots to participate in operations is defined by the brokerage company, and the maximum is limited by the deposit size;
-   Symbol — this field displays the name of the security participating in the trade operation;
-   Price — price of position opening (no to be mixed up with the current price described below). This is the price at which the position was opened;
-   S/L — the [placed Stop Loss order](/en/docs/mt4/terminal/positions/orders) level. If the order has not been placed, a zero value will be written in this field.  
    More details about working with orders can be found in the [corresponding section](/en/docs/mt4/terminal/positions/orders);
-   T/P — the [placed Take Profit order](/en/docs/mt4/terminal/positions/orders) level. If the order has not been placed, a zero value will be written in this field.  
    More details about working with orders can be found in the [corresponding section](/en/docs/mt4/terminal/positions/orders);
-   Price — the current price of the security (not to be mixed up with that of position opening described above);
-   Commission — commissions charged by the brokerage company at performing trade operations are written in this field;
-   Taxes — taxes charged when performing trade operations are written in this field;
-   Swap — charging of swaps is stored in this cell;
-   Profit — the financial result of the transaction made will be written in this field taking the current price into consideration. Positive result means that the transaction was profitable, and negative one means that it was unprofitable;
-   Comments — comments on trade operations are stored in this column. A comment can only be written at the position opening or at placing of a pending order. Comment cannot be changed at order or position modifying. Besides, the brokerage company can store a comment to a trade operation, as well.

## Trading

This tab allows not only to view the open positions and placed orders, but to manage trading activities. One can do the following here: open a new position, place a pending order, modify or delete it, and close a position. To do all this, one has to use the following context menu commands:

-   New Order — a new order. The orders managing window will appear at this command. A new position can be opened and a pending order can be placed in it. At that, the following must be specified: the security, amount of lots, order type (market order or a pending one), as well as [Stop Loss and Take Profit order](/en/docs/mt4/terminal/positions/orders) levels. More details about placing of orders can be found in the ["Control over Trade Positions"](/en/docs/mt4/terminal/positions/positions_control) section;
-   Close Order — close a trade position. This command becomes active only if the context menu has been called at an open position. The order managing window appears at this command, as well. This window displays not only "Sell" and "Buy" buttons, but also the "Close#XXXXXXX ..." button (where XXXXXXX is the position ticket number). Besides, having executed this command, one can close the selected positions together with the hedged ones. More details about closing of positions can be found in the [corresponding section](/en/docs/mt4/terminal/positions/positions_control/positions_close);
-   Modify or Delete Order — change the ["Stop Loss"](/en/docs/mt4/terminal/positions/orders#stop_loss) and ["Take Profit"](/en/docs/mt4/terminal/positions/orders#take_profit) values of open positions or the pending order price. If the Stop Loss and Take Profit levels specified are too close to the current price, the error message will appear, and the levels will not be placed. Their values must be changed to be not so close to the current price, and then they can be placed again. More details about modifying of orders can be found in the [section of the same name](/en/docs/mt4/terminal/positions/positions_control/positions_modify);
-   Trailing Stop — place, modify, or delete the ["Trailing Stop"](/en/docs/mt4/terminal/positions/trailing) level. Having selected the corresponding level in the menu, one can activate the trailing stop with the given parameter. The "None" value is used for disabling of the order. "Delete All" — disable all trailing stops. More details about trailing stops are given in the ["Trailing Stop" section](/en/docs/mt4/terminal/positions/trailing);

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The "Trailing Stop" command may be missing in the context menu, in case using that function is disabled on the broker's side.</span></p></td></tr></tbody></table>

-   Profit — show profit/loss as points, as term currency, or as deposit currency. Changes in this parameter are displayed in the "Profit" field. If the parameter of "show profit in the term currency" (quote currency) is selected had, there are, for example, open positions for USDJPY, the profit will be shown in Japanese Yens;
-   Commissions — show/hide the "Commissions" column where the commission for each of the performed trade operations will be displayed;
-   Taxes — show/hide the "Taxes" column to display the tax for each trade operation;
-   Comments — show/hide the "Comment" column. Comments to trade operations are written in this column. A comment can be written only if a position is being opened or an order is being placed. It cannot be changed at modifying of an order or of a position. Besides, the brokerage company can write a comment to a trade operation;
-   Auto Arrange — automatic arrangement of columns at changing of the window size;
-   Grid — show/hide grid to separate columns.

Accelerating keys of Ctrl+F9 switch the the focus in the "Terminal — Trade" window. After they have been pressed, one can trade with the keyboard.

## One Click Trading [#](terminal_trade#one_click)

The tab provides the possibility to [close positions](/en/docs/mt4/terminal/positions/positions_control/positions_close) and [delete pending orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_delete) by a single mouse click. This function is available in case the following conditions are met:

-   ["One click trading"](/en/docs/mt4/terminal/setup/setup_trade#one_click) option is enabled in the terminal settings;
-   [execution type](/en/docs/mt4/terminal/positions/execution) of the symbol, by which position is closed — "Instant" or "Market".

![Closing positions and deleting orders by a single mouse click](/en/docs/mt4/terminal/img/trade_one_click.png "Closing positions and deleting orders by a single mouse click")

"Profit" column of each open position and trading order has the button ![Close position/Delete order](/en/docs/mt4/terminal/img/close_delete_button.png "Close position/Delete order"). If you click the button for a position, it will be immediately closed without additional confirmations. If you click the button for a pending order, it will be immediately removed without additional confirmations.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If it is impossible to perform a deal in one click ("One click trading" option is disabled or <a href="/en/docs/mt4/terminal/positions/execution" class="topiclink">"Request" execution mode</a> is used for a symbol), clicking the button <img class="help" alt="Close position/Delete order" title="Close position/Delete order" width="9" height="8" src="/en/docs/mt4/terminal/img/close_delete_button.png"> will lead to the standard <a href="/en/docs/mt4/terminal/positions/positions_control/positions_close" class="topiclink">position closing</a> or <a href="/en/docs/mt4/terminal/positions/positions_control/pending_orders_delete" class="topiclink">order deleting</a> dialog.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">When a getting a requote, the corresponding message is written to the <a href="/en/docs/mt4/terminal/overview/terminal/terminal_journal" class="topiclink">terminal journal</a> and the <a href="/en/docs/mt4/terminal/setup/setup_events" class="topiclink">requote sound</a> is played.</span></li></ul></td></tr></tbody></table>

[Client terminal](/en/docs/mt4/terminal/overview/terminal)

[Exposure](/en/docs/mt4/terminal/overview/terminal/toolbox_exposure)