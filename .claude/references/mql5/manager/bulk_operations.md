# Bulk Operations

> Source: https://support.metaquotes.net/en/docs/mt5/manager/bulk_operations

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
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
            -   [Bulk Closing](/en/docs/mt5/manager/bulk_closing)
            -   [Bulk Operations](/en/docs/mt5/manager/bulk_operations)
            -   [Bulk Payments by Positions](/en/docs/mt5/manager/bulk_payments)
            -   [Splitting Positions](/en/docs/mt5/manager/position_split)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)Bulk Operations

# Bulk Operations

The Manager terminal allows performing balance operations for multiple accounts at once, for example, pay bonuses or charge commissions en masse. A set of accounts and operation amounts can be selected manually or imported from a CSV file.

Select one or several accounts (holding Ctrl or Ctrl+Shift) and click Bulk Operations... in the context menu.

![Bulk operations](/en/docs/mt5/manager/img/bulk_operations.png "Bulk operations")

Select the type of a balance operation:

-   Balance — changing an account balance.
-   Credit — issuing and repaying a credit.
-   Charge — any additional charges.
-   Correction — correction of trading results.
-   Bonus — bonuses. Operations of this type affect the credit assets of a client (Credit field).
-   Commission — additional commissions.
-   Dividend — paying taxable dividends.
-   Franked dividends — paying non-taxable dividends (tax is paid by a company, not a client).
-   Tax — charging a tax.

You can also add a comment to be included into each payment operation. If you want to add different comments to different users, prepare a list of charges in a CSV file and then import it. Specify comments in the file, in the Comment column.

All payments are performed in the form of transactions. By default, when conducting payment operations, the platform performs certain checks to ensure that the operation will not cause the account free margin and balance to become negative or its margin level to fall below 100%. If it does, the platform will not perform the operation and will display the "No money" error. If necessary, you can disable these checks by enabling the option "Conduct balance operations without checking the free margin and the current balance on the account".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The free margin is not checked for the "Correction" operation. Be careful with withdrawal operations. If the client has open positions, and you deduct an amount greater than the free margin, Stop Out will trigger on the account.</span></p></td></tr></tbody></table>

To perform a transaction for the same amount for all clients, specify it in the Amount field and click Set. The amount will be displayed in the Amount column for all clients. In order to change the amount for a certain account, double-click it in the accounts table.

If a payment currency is different from a client deposit one, the amount is converted at the current exchange rate. Click Rates to see or modify it.

![Currency conversion rate](/en/docs/mt5/manager/img/bulk_payments_rates.png "Currency conversion rate")

To modify the rate, double-click its value.

The list of accounts and operation amounts can be imported from a CSV file. The first value in the file (before the separator) sets logins, the second one defines operation amounts. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">1001;100</span><br><span class="f_CodeExample">1002;50.20</span><br><span class="f_CodeExample">1003;70.05</span></p></td></tr></tbody></table>

Click Process to execute operations. Three entries appear in the [journal](/en/docs/mt5/manager/toolbox#journal) for each performed operation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2017.03.14&nbsp;11:27:15.867&nbsp;&nbsp;&nbsp;Trades&nbsp;&nbsp;&nbsp;'1026605':&nbsp;balance&nbsp;10.00&nbsp;Bonus&nbsp;for&nbsp;'1811955'&nbsp;done&nbsp;in&nbsp;61&nbsp;ms&nbsp;(Bonus)</span><br><span class="f_CodeExample">2017.03.14&nbsp;11:27:15.866&nbsp;&nbsp;&nbsp;Trades&nbsp;&nbsp;&nbsp;'1026605':&nbsp;accepted&nbsp;balance&nbsp;10.00&nbsp;Bonus&nbsp;for&nbsp;'1811955'</span><br><span class="f_CodeExample">2017.03.14&nbsp;11:27:15.806&nbsp;&nbsp;&nbsp;Trades&nbsp;&nbsp;&nbsp;'1026605':&nbsp;balance&nbsp;10.00&nbsp;Bonus&nbsp;for&nbsp;'1811955'</span></p></td></tr></tbody></table>

[Bulk Closing](/en/docs/mt5/manager/bulk_closing)

[Bulk Payments by Positions](/en/docs/mt5/manager/bulk_payments)