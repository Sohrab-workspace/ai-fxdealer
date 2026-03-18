# Balance

> Source: https://support.metaquotes.net/en/docs/mt5/manager/account_balance

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
            -   [Clients](/en/docs/mt5/manager/clients)
            -   [Online Accounts](/en/docs/mt5/manager/online_accounts)
            -   [Creation of Accounts](/en/docs/mt5/manager/account_create)
            -   [Importing Accounts](/en/docs/mt5/manager/account_import)
            -   [Preliminary Accounts](/en/docs/mt5/manager/preliminary_accounts)
            -   [Push Notifications, SMS and Mail](/en/docs/mt5/manager/communication)
            -   [Account Overview](/en/docs/mt5/manager/account_overview)
            -   [Exposure](/en/docs/mt5/manager/account_exposure)
            -   [Personal Data](/en/docs/mt5/manager/account_personal)
            -   [Account Trading Settings](/en/docs/mt5/manager/account_tradeaccount)
            -   [Balance Operations](/en/docs/mt5/manager/account_balance)
            -   [Trading Operations](/en/docs/mt5/manager/account_trading)
            -   [Account History](/en/docs/mt5/manager/account_history)
            -   [Security and Certificates](/en/docs/mt5/manager/account_security)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Balance Operations

# Balance

The Manager terminal allows performing balance operations: depositing and withdrawal of funds, credit provision, charging commissions, dividends, etc.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">"Accountant (deposit/withdraw)" permission is required for accessing the section. The permission is granted by the platform administrator.</span></p></td></tr></tbody></table>

![Conducting balance operations on the client's account](/en/docs/mt5/manager/img/account_balance.png "Conducting balance operations on the client's account")

To conduct a balance operation, set the following parameters:

-   Operation — type of operation:

-   Balance — changing an account balance.
-   Credit — issuing and repaying a credit.
-   Charge — any additional charges.
-   Correction — correction of trading results.
-   Bonus — bonuses. Operations of this type affect the credit assets of a client ([Credit](/en/docs/mt5/manager/account_overview#state) field).
-   Commission — additional commissions.
-   Dividend — paying taxable dividends.
-   Franked dividends — paying non-taxable dividends (tax is paid by a company).
-   Tax — charging a tax.
-   Amount — amount of money deposited or withdrawn from an account.
-   Comment — text comment to an operation. In this field, you can choose one of the earlier created comments, or write a new one.

There are two types of directions for each operation type — depositing to an account or withdrawal. A blue button is used for depositing (in operations), red one — for withdrawals (out operations).

By default, when conducting balance operations the platform performs checks to make sure they do not cause the account free margin and balance to become negative. If it does, the platform will not perform the operation and will display the "No money" error. If necessary, you can disable these checks by enabling the option "Conduct balance operations without checking the free margin and the current balance on the account".

Due to the funds accounting specifics, margin and balance are not checked on accounts with the "[for Stock Exchange, based on margin discount rates](/en/docs/mt5/manager/margin#risk)" risk management model.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">All balance transactions in the system are passed as <a href="/en/docs/mt5/manager/trade_principles#deal" class="topiclink">deals</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">You cannot withdraw an amount greater than the current value of an account free margin or balance.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The free margin is not checked for the "Correction" operation. Be careful with withdrawal operations. If the client has open positions, and you deduct an amount greater than the free margin, Stop Out will trigger on the account.</span></li></ul></td></tr></tbody></table>

## History of operations

The history of balance operations conducted earlier is located at the bottom of the window:

-   Time — time when the operation was conducted. When depositing to an account, at the beginning of this field, ![Balance increase](/en/docs/mt5/manager/img/balance_up_icon.png "Balance increase") icon is shown, when withdrawing — ![Balance decrease](/en/docs/mt5/manager/img/balance_down_icon.png "Balance decrease").
-   Deal — unique operation ID in the system.
-   Type — operation type.
-   Amount — operation amount.
-   Comment — operation comment.

To view a history of balance operations, set a period and click Request at the bottom of the window. To enable/disable display of milliseconds, grid or comments in the history of operations, use the context menu.

## Account status [#](account_balance#account_state)

The account status bar is displayed under the list of balance operations. It contains the following information:

-   Balance — money on the account, not considering results of currently open positions (deposit).
-   Credit — amount of funds provided to a client by a broker as a loan. The trading platform does not have a function of charging an interest for credit assets. Credit assets can be deposited and withdrawn at the [Balance](/en/docs/mt5/manager/account_balance) tab.
-   Blocked — client group can be set up so that a profit earned by a trader during a day cannot be used for trading (it is not accounted in the free margin). This blocked profit is displayed in the Blocked field. At the end of the trading day, this profit is unblocked and deposited to the account balance.
-   Equity — equity is calculated as Balance + Credit - Commission +/- Floating profit/loss - Blocked.
-   Margin — money required to cover open positions and pending orders.
-   Free — the following parameters are displayed here:

-   Free Margin — free amount of money that can be used to maintain open positions. It is calculated as Equity - Margin. Depending on the client group settings, the equity value may or may not consider: floating profit, floating loss or floating profit and floating loss together.
-   Margin Level — percentage of the account equity to the margin volume (Equity / Margin \* 100).

in case of a positive result of current open positions, at the beginning of the account, status bar icon ![Balance increase](/en/docs/mt5/manager/img/balance_up_icon.png "Balance increase") is shown, in case of a negative one — ![Balance decrease](/en/docs/mt5/manager/img/balance_down_icon.png "Balance decrease").

## Balance check and correction [#](account_balance#fix)

In the Manager terminal, you can easily check the balance and the state of credit funds on accounts based on the [history of deals](/en/docs/mt5/manager/account_history#deals). Such operations can be required after the manual history correction, for example, as a result of failures or abnormal situations.

To perform a check, go to the "Accounts" section and enable the "Balance / Checked" and "Credit / Checked" columns via the context menu.

![Enable the "Balance / Checked" and "Credit / Checked" columns in the accounts section](/en/docs/mt5/manager/img/check_balance_columns.png "Enable the "Balance / Checked" and "Credit / Checked" columns in the accounts section")

Select one or several accounts, for which you want to check the balance and credit funds, and execute the "Balance — Check Balance" command. If an incorrect balance or credit funds value is revealed, the appropriate account will be highlighted in red.

![Balance and credit funds check results](/en/docs/mt5/manager/img/check_balance_result.png "Balance and credit funds check results")

Two values will be displayed in "Balance" and "Credit" columns: the current balance/credit funds value will be displayed on the left, while the value calculated using the deals history is shown on the right.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The credit funds are checked based on the <a href="/en/docs/mt5/manager/account_history#deals" class="topiclink">"Credit" type</a> deals.</span></p></td></tr></tbody></table>

The check result is also displayed in the [journal](/en/docs/mt5/manager/toolbox#journal). If the calculated value differs from the current one, the following message will appear in the journal:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">account</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">xxx</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">has</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">invalid</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">balance:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">xxx.xx,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">valid:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">xxx.xx</span></p></td></tr></tbody></table>

To correct the balance/credit funds value, select the desired account and execute "Balance — Fix Balance" command in the context menu. After that the calculated balance/credit value will be inserted as the current one. The correction result will be written to the journal:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">balance&nbsp;of&nbsp;account&nbsp;'1030390'&nbsp;has&nbsp;been&nbsp;fixed&nbsp;from&nbsp;9&nbsp;968.70&nbsp;to&nbsp;9&nbsp;999.80</span></p></td></tr></tbody></table>

[Account Trading Settings](/en/docs/mt5/manager/account_tradeaccount)

[Trading Operations](/en/docs/mt5/manager/account_trading)