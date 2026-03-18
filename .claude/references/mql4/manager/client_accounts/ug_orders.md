# Orders

> Source: https://support.metaquotes.net/en/docs/mt4/manager/client_accounts/ug_orders

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
        -   [Getting Started](/en/docs/mt4/manager/getting_started)
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
            -   [Adding a New Account](/en/docs/mt4/manager/client_accounts/ug_new_accounts)
            -   [Accounts](/en/docs/mt4/manager/client_accounts/ug_accounts)
            -   [Online](/en/docs/mt4/manager/client_accounts/ug_online)
            -   [Orders](/en/docs/mt4/manager/client_accounts/ug_orders)
            -   [Sending Notifications](/en/docs/mt4/manager/client_accounts/push_notifications)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
        -   [Articles](/en/docs/mt4/manager/articles)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Client Accounts](/en/docs/mt4/manager/client_accounts)Orders

# Orders

In the "Orders" section, the information about all trades of any account can be requested.

![Orders](/en/docs/mt4/manager/img/br_orders.png "Orders")

To make the process more convenient, all accounts are accumulated in a table having adjustable cells. The following fields are available:

-   Deal — order number;
-   Login — account number;
-   Time — time of position opening;
-   Type — type of operation (buy, sell, sell limit, buy limit, buy stop, sell stop);
-   Symbol — financial instrument;
-   Volume — volume of the position;
-   Price — open price of the position;
-   S/L — the level of Stop-Loss order set;
-   T/P — the level of Take-Profit order set;
-   Price — the current market price;
-   Commission — commission amount;
-   Taxes — taxes for commission;
-   Swap — swaps calculated;
-   Profit — profit made on the trade operation;
-   Expiration — the expiration time of the pending order;
-   Reason — a reason of placing the order:

-   Client — the order is placed manually by a client via the client terminal;
-   Expert — the order is placed by a client using an Expert Advisor;
-   Dealer — the order is placed by a dealer via the manager terminal;
-   Signal — the order is placed as a result of copying a [trade signal](https://www.mql5.com/en/signals) according to a subscription in the client terminal;

-   Gateway — the order is placed via the MetaTrader 4 STP gateway.

-   Comment — the comment.

The context menu allows to execute the following commands:

-   Account Details — open the management window for the account orders;
-   Order Details — open the window of the deal;
-   Bulk Closing... — [bulk closing](/en/docs/mt4/manager/client_accounts/ug_orders#bulk) of all positions by symbol;
-   Journal — switch to the "Journal" tab to request logs for selected order;
-   Find — find an account in the account list;
-   Copy — copy the selected accounts from the list in the clipboard;
-   Save — save the report about opened orders as not processed. Only the information that is currently displayed in the list of orders will be saved in the report. To change the report contents you should specify the columns to be displayed using the "Columns" command described below;
-   Auto Arrange — automatic arrangement of column sizes when the window sizes are changed;
-   Grid — show/hide grid to separate columns;
-   Columns — select columns to be shown.

## Account Orders (Trades tab) [#](ug_orders#trades)

![Trades tab](/en/docs/mt4/manager/img/account_trades.png "Trades tab")

The "Trades" tab includes the client's order list.

The following commands are available on the order tab:

-   Deposit/Withdrawal — deposit money to a client's account or withdraw money from the account. The following window will appear after you press this button:

![Deposit/Withdrawal](/en/docs/mt4/manager/img/deposit_withdrawal.png "Deposit/Withdrawal")

Specify the amount in the "Value" field and a comment for the operation in the "Comment" field. Additionally, in the "Expiration date" field, specify the credit expiration date. It is added to the "Close time" field of the accrual balance transaction. The credit is not canceled automatically upon expiration. This date is used for the "Credit Facility" report. Based on the report, the manager should decides whether to cancel or leave the credit on the account.

To make a transaction, click "Credit In" or "Credit Out".

-   Credit Facility — give a credit or cancel an earlier provided credit. The following window will appear after you press this button:

![Credit Facility](/en/docs/mt4/manager/img/credit_facility.png "Credit Facility")

Here you should also specify the amount of money in the "Value" field and a comment to the operation in the "Comment" field. In addition to it you should specify the date of the credit expiration at the "Expiration date" field. Then you can perform the operation using the "Credit In" or "Credit Out" buttons.

The credit expiration date is saved in the "Close time" field of the corresponding balance operation.

-   Close All — [close all hedged positions](/en/docs/mt4/manager/client_accounts/ug_orders#close_all) of the account for the same symbol;
-   History — request history of the client's transactions;
-   Save As — save the statement for the account transactions.

Context menu allows to execute the following commands:

-   Details — open order details window;
-   History — request trade history;
-   Save Report — save the statement for the account;
-   Save Detailed Report — save detailed statement for the account;
-   Close Time — show/hide close time column;
-   Commission — show/hide commission column;
-   Taxes — show/hide taxes column;
-   Expiration — show/hide expiration of pending order column;
-   Comment — show/hide comment column;
-   Auto Arrange — automatic arrangement of column sizes when the window sizes are changed;
-   Grid — show/hide grid to separate columns.

Double click on the order opens the window of order details.

## Exposure (Exposure tab) [#](ug_orders#exposure)

On this tab, a manager can view the current assets of a client combined by currencies.

![Exposure](/en/docs/mt4/manager/img/account_exposure.png "Exposure")

The information is displayed in the from of a table that contains the following fields:

-   Asset — the name of a currency or symbol;
-   Volume — the volume of a client's position (in units) by the given position or symbol considering leverage;
-   Rate — the rate of currency or symbol to the deposit currency;
-   Deposit Currency — this column displays the amount of actually spent deposit currency (leverage is not considered) on buying/selling a currency or a symbol;
-   Graph — the graphical displaying of client's position in the deposit currency (long positions are displayed in blue stripes and short positions are displayed in red ones).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The assets of an account by the deposit currency are displayed considering free margin.</span></p></td></tr></tbody></table>

### Diagram [#](ug_orders#diagram)

There is a possibility of viewing the information by long and short positions in the form of a diagram. To switch between diagrams, one should press on their names or use the context menu.

### Account State

The line of the current state of an account is displayed below the information about assets:

-   Balance — money on the account, not accounting for the results of currently open positions;
-   Equity — money accounting for the results of the currently open positions;
-   Margin — money required to cover open positions;
-   Free Margin — volume of free funds that can be used for covering open positions;
-   Margin Level — percent ratio of equity on the account and required margin.

### Context Menu

The context menu of this tab allows executing the following commands:

-   Diagram — open the submenu of diagram managing:

-   Long Positions — show the circle diagram by long positions;
-   Short Positions — show the diagram by short positions;
-   Hide — hide the diagram;

-   Grid — show/hide grid to separate table fields;
-   Auto Arrange — enable/disable automatic resizing of columns in case window size is changed.

## Transaction (Deal window) [#](ug_orders#deal)

![Deal window](/en/docs/mt4/manager/img/account_deal.png "Deal window")

The detailed information of the transaction is displayed in the Order window: order number (ticket), order type, symbol, volume, time of opening, opening price, the set levels of Stop Loss and Take Profit, commission, calculated swaps, current market price, floating profit/loss.

The following commands are available in the deal window:

-   Modify — modify Stop Loss, Take Profit, and the opening price of the order;
-   Change — change the order comment;
-   Delete — delete an order;
-   Close — close the opened order;
-   Activate — process a pending order;
-   Close by — in the presence of an opposite order, close the order by another order.

## Closing all hedged positions (Close All Hedged Positions window) [#](ug_orders#close_all)

![Close All Hedged Positions window](/en/docs/mt4/manager/img/account_close_all.png "Close All Hedged Positions window")

Close All command allows to close all hedged positions of the account for the same symbol.

## New Order (New Order tab) [#](ug_orders#new)

New Order tab of the window of account management allows to place a new order.

![New Order tab](/en/docs/mt4/manager/img/account_new_order.png "New Order tab")

When placing an order, it is necessary to indicate the volume, symbol, and the transaction opening price; if necessary, Stop Loss, Take Profit, and comments can be given. For a pending order, it is also necessary to indicate the type of the order, and the expiry date of the order, if required. To set out an order, it is necessary to execute the "Buy" command for buying, the "Sell" command for selling, or the "Place" command for placing a pending order. When trading by a telephone you can specify the whole amount of the requested lots (Requested volume) and then successively change the account's login when placing a new order.

## Bulk closing (Close All Positions By Symbol window) [#](ug_orders#bulk)

After expiration of the Futures Contract, all positions for the defined symbol must be closed. "Close All Positions" window that can be called by executing the "Bulk closing" command of the context menu of the orders list allows closing all positions for the selected symbol.

![Close All Positions window](/en/docs/mt4/manager/img/bulk_closing.png "Close All Positions window")

For all positions to be closed, one has to select a symbol and specify bid and ask at which positions will be closed. If pending orders for this symbol must be closed, as well, the 'Delete pending orders' option must be checked. If different groups of accounts have different spread and positions for accounts from different groups must be closed at different prices, one can filter positions by the accounts group having selected the group in the pop-up list. One can comment on the orders closing, if necessary. If you need only to delete the pending orders and not to close all positions, you should check the "Delete pending orders" box and uncheck the "Close positions" box.

[Online](/en/docs/mt4/manager/client_accounts/ug_online)

[Sending Notifications](/en/docs/mt4/manager/client_accounts/push_notifications)