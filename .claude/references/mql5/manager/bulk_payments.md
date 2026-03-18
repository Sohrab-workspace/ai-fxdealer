# Bulk Payments by Positions

> Source: https://support.metaquotes.net/en/docs/mt5/manager/bulk_payments

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)Bulk Payments by Positions

# Bulk Payments by Positions

Unlike ordinary [bulk balance operations](/en/docs/mt5/manager/bulk_operations), here you can calculate payments for actual traders' positions at a specified date. The function is primarily developed for calculating and paying dividends to shareholders according to the number of shares each of them has in possession.

Calculation and payments are performed for the positions status as of the selected date. If the date is different from the current one, data on actual clients' positions is taken from daily reports. Therefore, daily reports generation should be enabled for each client group separately on a trade server for such cases.

Click "Bulk Payments..." in the context menu of the Positions section and specify the following parameters:

-   The instruments of the positions for which the payments will be made. One symbol or a group of symbols can be selected from the list. Optionally, you can specify a comma separated list of trading instruments or groups of symbols. For example, Forex\\\*, CFD\\\*, Metals\\GOLD.
-   The client groups for which the payments will be made.
-   Payment settlement date.

Click "Request" to display data on clients' positions for the selected symbols in the list. The data is taken from the last daily report available on the server at a specified date. To enable calculation for current positions, uncheck the Date field.

![Bulk payments by positions](/en/docs/mt5/manager/img/bulk_payments.png "Bulk payments by positions")

The volume of short and long positions in lots is displayed for each client. If hedging accounts are present among others, use a net volume for calculating payments (volume difference between buy and sell positions). To do this, enable the "Calculate using net positions" option.

By default, when conducting payment operations, the platform performs certain checks to ensure that the operation will not cause the account free margin and balance to become negative or its margin level to fall below 100%. If it does, the platform will not perform the operation and will write the "No money" error in the Status column. If necessary, you can disable these checks by enabling the option "Conduct balance operations without checking the free margin and the current balance on the account".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Be careful when disabling margin and balance checks. Such payment operations may cause Margin Call or Stop Out on client accounts.</span></p></td></tr></tbody></table>

Specify a payment amount per each position lot and the payment currency. If a payment currency is different from a client deposit one, the amount is converted at the exchange rate valid during the daily report generation time. Click Rates to see or modify it.

![Currency conversion rate](/en/docs/mt5/manager/img/bulk_payments_rates.png "Currency conversion rate")

To modify the rate, double-click its value.

The Tax field allows you to enter a percentage value to be deducted from a payment amount. For example, if the payment amount is 100 USD, while the Tax field is set to 3, clients are paid 97 USD per each position lot.

Next, select the operation type:

-   Balance — changing an account balance.
-   Credit — issuing and repaying a credit.
-   Charge — any additional charges.
-   Correction — correction of trading results.
-   Bonus — bonuses. Operations of this type affect the credit assets of a client (Credit field).
-   Commission — additional commissions.
-   Dividend — paying taxable dividends.
-   Franked dividends — paying non-taxable dividends (tax is paid by a company, not a client).
-   Tax — charging a tax.

A comment may additionally be added to be included into each payment operation. All payments are performed in the form of transactions.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The free margin is not checked for the "Correction" operation. Be careful with withdrawal operations. If the client has open positions, and you deduct an amount greater than the free margin, Stop Out will trigger on the account.</span></p></td></tr></tbody></table>

Click Calculate to see preliminary payment results. They are displayed in the Amount Buy and Amount Sell (or Amount when using net positions).

![Preliminary calculation of the payments](/en/docs/mt5/manager/img/bulk_payments_setup.png "Preliminary calculation of the payments")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any payment amount can be changed manually. Double-click the amount and enter a new value.</span></p></td></tr></tbody></table>

Make sure the amounts are correct and click Process. Payments are performed using balance operations of a selected type with a specified comment. Successfully paid amounts are highlighted in green. If a payment is not performed, it is highlighted in red. An error description can be seen in a tooltip.

![Payment results](/en/docs/mt5/manager/img/bulk_payments_result.png "Payment results")

[Bulk Operations](/en/docs/mt5/manager/bulk_operations)

[Splitting Positions](/en/docs/mt5/manager/position_split)