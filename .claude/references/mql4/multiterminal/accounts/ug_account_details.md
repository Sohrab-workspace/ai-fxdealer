# Account Details

> Source: https://support.metaquotes.net/en/docs/mt4/multiterminal/accounts/ug_account_details

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

[MetaTrader 4](/en/docs/mt4)[MultiTerminal](/en/docs/mt4/multiterminal)[Client Accounts](/en/docs/mt4/multiterminal/accounts)Account Details

# Account Details

After the account has been connected to the server, it is possible to view the account details. The window displaying the account details appears after selection of the "Account Details" in the "Accounts" window context menu or after a double click on the account.

The "Trade" tab of this window displays the current open positions of the account, the account balance line and the financial results of open positions, as well as pending orders placed. All trade operations are displayed as a table containing the following fields (from left to right):

-   Order — the operation ticket number. This is the unique number of the trade operation;
-   Time — time when the position was opened. The record appears as YYYY.MM.DD HH:MM (year.month.day hour:minute). It is this time when the position was opened;
-   Type — type of the trade operation. There are some types of trade operations available: "Buy" — a long position, "Sell" — a short position, and pending orders [Sell Stop, Sell Limit, Buy Stop and Buy Limit](/en/docs/mt4/multiterminal/trading/ug_orders#pending);
-   Symbol — this field shows the name of security used in a trade operation;
-   Lots — the amount of lots used in the operation. The minimum amount of lots allowed in operations is limited by the brokerage company, the maximum — by deposit available;
-   Price — open price of a position (not to be confused with the current price described below). It is this price at which the position was opened;
-   S/L — level of the [Stop Loss](/en/docs/mt4/multiterminal/trading/ug_orders#stop_loss) order placed. If the order is not specified, zero value will be entered in this field. If an order was closed by Stop Loss or the distance between the current price and the Stop Loss level of an open order is equal to 1 point, this order field will be red-colored.  
    One can find more details about order management in the [corresponding section](/en/docs/mt4/multiterminal/trading/ug_orders#stop_loss);
-   T/P — level of the [Take Profit](/en/docs/mt4/multiterminal/trading/ug_orders#take_profit) order placed. If the order is not specified, zero value will be entered in this field. If an order was closed by Take Profit or the distance between the current price and the Take Profit level of an open order is equal to 1 point, this order field will be green-colored.  
    One can find more details about order management in the [corresponding section](/en/docs/mt4/multiterminal/trading/ug_orders#take_profit);
-   Time — close time of a position. The record appears as YYYY.MM.DD HH:MM (year.month.day hour:minute). This field must be empty for open positions and pending orders placed;
-   Price — the current price of the security (not to be confused with the open price of the position described above) or the close price of a position;
-   Commission — fees charged by the brokerage company for trading operations made are written in this field;
-   Taxes — taxes charged on commission;
-   Swap — swaps are fixed in this field;
-   Profit — the financial result of the trade considering the current price is given in this field. A positive value means that the trade was profitable, a negative value means that the trade was losing;
-   Expiration — expiration time for a pending order. This field must be empty for market orders and for those pending orders, for which the expiration time was not specified.

The profit of positions can be displayed in points, in the term currency or in the deposit currency using the context menu commands. The account trading history can be requested using the "History" command of the context menu or a corresponding button. The same time the window in which you should specify one of the predefined periods or a concrete time range of the request will appear. The "Save As" context menu command and the corresponding button allow saving a report about the account trading as a HTML file.

## Security Tab [#](ug_account_details#security)

The "Security" tab of the "Account Details" window allows changing the master or the investor's password of the account. To change a password, it is necessary to enter the current password of the account, its new password, then confirm the new password and press "Change".

[Connecting Accounts](/en/docs/mt4/multiterminal/accounts/ug_account_connect)

[Open Orders](/en/docs/mt4/multiterminal/accounts/ug_account_orders)