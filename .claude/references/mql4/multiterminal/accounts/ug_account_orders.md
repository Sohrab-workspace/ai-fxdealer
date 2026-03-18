# Open Orders

> Source: https://support.metaquotes.net/en/docs/mt4/multiterminal/accounts/ug_account_orders

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
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
        -   [Getting Started](/en/docs/mt4/multiterminal/getting_started)
        -   [Client Accounts](/en/docs/mt4/multiterminal/accounts)
            -   [Adding Accounts](/en/docs/mt4/multiterminal/accounts/ug_accounts)
            -   [Connecting Accounts](/en/docs/mt4/multiterminal/accounts/ug_account_connect)
            -   [Account Details](/en/docs/mt4/multiterminal/accounts/ug_account_details)
            -   [Open Orders](/en/docs/mt4/multiterminal/accounts/ug_account_orders)
            -   [Trade History](/en/docs/mt4/multiterminal/accounts/ug_account_history)
        -   [Trading](/en/docs/mt4/multiterminal/trading)
        -   [Analytics](/en/docs/mt4/multiterminal/analytics)
        -   [User Interface](/en/docs/mt4/multiterminal/user_interface)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MultiTerminal](/en/docs/mt4/multiterminal)[Client Accounts](/en/docs/mt4/multiterminal/accounts)Open Orders

# Open Orders

Currently open positions and pending orders placed are displayed in the "Orders" tab. All trade operations are shown as a table with the following fields (from left to right):

-   Order — the operation ticket number. This is the unique number of the trade operation;
-   Login — trade account number;
-   Time — time when the position was opened. The record appears as YYYY.MM.DD HH:MM (year.month.day hour:minute). It is this time when the position was opened;
-   Type — type of the trade operation. There are some types of trade operations available: "Buy" — a long position, "Sell" — a short position, and pending orders [Sell Stop, Sell Limit, Buy Stop and Buy Limit](/en/docs/mt4/multiterminal/trading/ug_orders#pending);
-   Symbol — this field shows the name of a security used in a trade operation;
-   Lots — the amount of lots used in the operation. The minimum amount of lots allowed in operations is limited by the brokerage company, the maximum — by deposit available;
-   Price — open price of a position (not to be confused with the current price described below). It is this price at which the position was opened;
-   S/L — level of the [Stop Loss](/en/docs/mt4/multiterminal/trading/ug_orders#stop_loss) order placed. If the order is not specified, zero value will be entered in this field. If the distance between the current price and the Stop Loss level becomes less than or equal to 10 points, this field of the order is colored red. If the distance shortens to 1 point, it becomes yellow.  
    One can find more details about order management in the [corresponding section](/en/docs/mt4/multiterminal/trading/ug_orders#stop_loss);
-   T/P — level of the [Take Profit](/en/docs/mt4/multiterminal/trading/ug_orders#take_profit) order placed. If the order is not specified, zero value will be entered in this field. If the distance between the current price and the Take Profit level becomes less than or equal to 10 points then this field of the order is colored green. If the distance shortens to 1 point, it becomes yellow.  
    One can find more details about order management in the [corresponding section](/en/docs/mt4/multiterminal/trading/ug_orders#take_profit);
-   Price — the current price of the security (not to be confused with the open price of a position described above);
-   Commission — fees charged by the brokerage company for trading operations made are written in this field;
-   Taxes — taxes charged on commission;
-   Swap — swaps are fixed in this field;
-   Profit — the financial result of the trade considering the current price is given in this field. A positive value means that the trade was profitable, a negative value means that the trade was losing;
-   Expiration — expiration time for a pending order. This field must be empty for market orders and for those pending orders, for which the expiration time was not specified.
-   Comment — the order comment specified at its placing.

The profit of positions can be displayed in points, in the term currency or in the deposit currency using the context menu commands. The account trading history can be requested using the "History" command of the context menu or a corresponding button. The "Save" context menu command and the corresponding button allow saving a report about the account trading as a HTML file.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If there are connected accounts with different deposit currencies, an additional command "Summary currency" appears in the context menu. It allows choosing the currency that will be used for the representation of the total result of all accounts, also it affects the calculation of the <a href="/en/docs/mt4/multiterminal/getting_started/ug_setup#distribution" class="topiclink">allocation of the total volume between the orders</a> when opening positions</span></p></td></tr></tbody></table>

[Account Details](/en/docs/mt4/multiterminal/accounts/ug_account_details)

[Trade History](/en/docs/mt4/multiterminal/accounts/ug_account_history)