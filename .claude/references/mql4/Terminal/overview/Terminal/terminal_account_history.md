# Account History

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/terminal/terminal_account_history

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Client terminal](/en/docs/mt4/terminal/overview/terminal)Account History

# Account History

Information about all trade operations performed is stored in the "Account History" tab.

![terminal_window_history](/en/docs/mt4/terminal/img/terminal_window_history.png)

The entire history is displayed as a table with the following fields (from left to right):

-   Order — operation ticket number. It is the unique number of a trade operation;
-   Time — time of position opening. It is given in YYYY.MM.DD HH:MM (year.month.day hour:minute) format. This is the time when the position was opened;
-   Type — trade operation type. Only three types of trade operations can be found here: "Balance" — entering of funds in the account, "Buy" — a long position, and "Sell" — a short position;
-   Size — amount of lots participated in the operation;
-   Symbol — this field shows the name of the security participated in the operation;
-   Price — price of position opening. This is the price at which the position was opened;
-   S/L — level of the [Stop Loss order](/en/docs/mt4/terminal/positions/orders) placed. If a trade position was closed by this order, its corresponding cell will be colored in red, and "\[s/l\]" will appear in the field of comments. If no order was placed, zero value will appear in this field. On the other hand, if the an order was placed, but did not trigger, its value will still be shown in this field. At that, the cell will not be colored, and no "\[s/l\]" will be output in the field of comments. More details about working with orders are given in the [corresponding section](/en/docs/mt4/terminal/positions/orders);
-   T/P — level of the [Take Profit order](/en/docs/mt4/terminal/positions/orders) placed. If a trade position was closed by this order, its corresponding cell will be colored in green, and "\[t/p\]" will appear in the field of comments. If no order was placed, zero value will appear in this field. On the other hand, if the an order was placed, but did not trigger, its value will still be shown in this field. At that, the cell will not be colored, and no "\[t/p\]" will be output in the field of comments. More details about working with orders are given in the [corresponding section](/en/docs/mt4/terminal/positions/orders);
-   Time — time of position closing. It is given in YYYY.MM.DD HH:MM (year.month.day hour:minute) format. This is the time when the position was closed;
-   Price — price of position closing. This is the price at which the position was closed;
-   Commission — commissions charged by the brokerage company at performing trade operations are written in this field;
-   Taxes — taxes charged when performing trade operations are written in this field;
-   Swap — the swaps charged are stored in this field;
-   Profit — the financial result of transaction will be written in this field. Positive number means that the transaction was profitable, and the negative one does vice versa. The profit is shown only in the deposit currency here, unlike it is in the field of the same name in the ["Trade" tab](/en/docs/mt4/terminal/overview/terminal/terminal_trade).
-   Comments — comments on trade operations are stored in this column. A comment can be input only at opening of a position or placing an order. The comment cannot be changed when an order or a position are being modified. Besides, a comment to the trade operation can be input by the brokerage company.

You can easily display the history of performed trades on a chart. To do it, you should just drag the necessary trade on a chart via the mouse. The entering and exiting points of the trade, connected with a line, will be shown with arrows. If you hold the Shift button while dragging a trade, the entire history of trades will be placed on the chart.

## Context Menu

Commands allowing to manage the history range and data performance, as well as commands of history data export are grouped in the context menu:

-   All History — show the entire account history. At this command execution, the whole financial history of the account will appear in the screen without any limitations by time;
-   Last 3 Months — show only the last 3-months history. The history of orders is requested by their close time;
-   Last Month — show only the last month history. The history of orders is requested by their close time;
-   Custom Period — show history for the selected period. At this command execution, the window that manages the history range will appear where one can select one of the pre-defined ranges (the "Period" field) or specify them manually in the fields of "From" and "to". The history of orders is requested by their close time;
-   Save as Report — save the account history as a [report](/en/docs/mt4/terminal/overview/terminal/terminal_account_history#report) in the form of the HTML file. At that, a window allowing to select a path for saving of the file will appear;
-   Save as Detailed Report — save the account history as a [report](/en/docs/mt4/terminal/overview/terminal/terminal_account_history#report) in the form of the HTML file. A detailed report differs from a normal one for an additional set of parameters. After this command has been executed, a window allowing to select a path for saving the file will appear;
-   Commissions — show/hide the "Commissions" column;
-   Taxes — show/hide the "Taxes" column;
-   Comments — show/hide the "Comments" column. Comments to trade operations are stored in this column. A comment can only be input at opening of a position or at placing of an order. Besides, the brokerage company can write a comment to the trade operation, as well;
-   Auto Arrange — automatic arrangement of column sizes at changing of the window size;
-   Grid — show/hide grid for separating of columns.

## Reports [#](terminal_account_history#report)

The upper part of the report contains general information about the account. Then the trades details are given that are separated into closed trades (Closed Transactions), open trades (Open Trades) and pending orders (Working Orders). The number of the fields displayed depends on the report type chosen (common or detailed).

-   Ticket — ticket number of a trading position;
-   Open Time — time of position opening;
-   Type — trade type (sell, buy, s/l, t/p, modify, close at stop, etc.);
-   Size — amount of lots traded;
-   Item — security traded;
-   Price — open price of a trading position;
-   S/L — the value of Stop Loss;
-   T/P — the value of Take Profit;
-   Close Time — time of position closing;
-   Price — price of position closing;
-   Commission — commissions charged by the brokerage company at performing the trade operation;
-   Taxes — taxes charged at performing trade operation;
-   Swap — swaps charged;
-   Profit — the financial result of the transaction.

For pending orders, an additional column, "Market Price", appears. The current market price as of the report generation is specified in it.

The summary about the financial performance of the account is located below (Summary):

-   Deposit/Withdrawal — information about the deposits and withdrawals of the account;
-   Credit Facility — information about the credit funds on the account;
-   Closed Trade P/L — total profit/loss by all closed trades of the account;
-   Floating P/L — current profit/loss by all opened trades of the account;
-   Balance — balance of the account;
-   Equity — equity of the account;
-   Margin — the account margin for open trades;
-   Free Margin — the account free margin.

The report also contains the balance diagram and the statistical information about the account:

-   Total Net Profit — financial result of all trades. This index represents a difference between the "Gross Profit" and "Gross Loss";
-   Gross Profit — the sum of all profitable trades in terms of money;
-   Gross Loss — the sum of all unprofitable trades in terms of money;
-   Profit Factor — the ratio between gross profit and gross loss in per cents. The one value means that profit equals to loss;
-   Expected Payoff — the expected payoff. This statistically calculated index represents the average profit/loss factor of a trade. It can also be considered for representing the expected profit/loss factor of the next trade;
-   Absolute Drawdown — the largest loss below the initial deposit value;
-   Maximal Drawdown — the largest loss from the local maximum in the deposit currency and in percents of the deposit;
-   Relative Drawdown — the largest loss in percents of the maximum balance value and its corresponding money value;
-   Total trades — the total amount of trade positions;
-   Short Positions (won %) — the amount of short positions and percentage of won thereof;
-   Long Positions (won %) — the amount of long positions and percentage of won thereof;
-   Profit Trades (% of total) — the amount of profitable trade positions and their percentage in the total trades;
-   Loss trades (% of total) — the amount of loss trade positions and their percentage in the total trades;
-   Largest profit trade — the largest profit among all profitable positions;
-   Largest loss trade — the largest loss among all unprofitable positions;
-   Average profit trade — average profit value for a trade (the sum of profits divided by the amount of profitable trades);
-   Average loss trade — average loss value for a trade (the sum of losses divided by the amount of unprofitable trades);
-   Maximum consecutive wins ($) — the longest series of profitable trade positions and the sum of their wins;
-   Maximum consecutive losses ($) — the longest series of unprofitable trade positions and the sum of their losses;
-   Maximal consecutive profit (count) — the maximum profit of a series of profitable trades and the amount of profitable trades corresponding with it;
-   Maximal consecutive loss (count) — the maximum loss of a series of unprofitable trades and the amount of unprofitable trades corresponding with it;
-   Average consecutive wins — the average amount of profitable positions in consecutive profitable series;
-   Average consecutive losses — the average amount of unprofitable positions in consecutive unprofitable series.

[Exposure](/en/docs/mt4/terminal/overview/terminal/toolbox_exposure)

[News](/en/docs/mt4/terminal/overview/terminal/terminal_news)