# Importing Accounts

> Source: https://support.metaquotes.net/en/docs/mt5/manager/account_import

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Importing Accounts

# Importing Accounts

The Manager terminal allows you to bulk import accounts to the trading platform from text files. To do this, select "![Import](/en/docs/mt5/manager/img/import_icon.png "Import") Import" in the context menu of the account list.

![Importing accounts from the file](/en/docs/mt5/manager/img/accounts_import.png "Importing accounts from the file")

The following commands are available in the account importing window:

-   File — path to a \*.CSV file you need to import accounts from. Specify the path manually, or select the desired file using the Browse... button located to the right.
-   Separator — data separator in the file (comma, semicolon, tabulation character or space).
-   Start from Line — file line, starting from which data will be imported. For example, if you set 3, the first two lines in the file are skipped.
-   Columns — open the [data associating](/en/docs/mt5/manager/account_import#columns) window in the imported file with appropriate fields in the system.
-   Use selected items only — if enabled, only rows currently selected in the preview window below are imported.
-   Refresh — refresh data in the preview window.

To see how an account will look after the import, double-click on it in the list or click View in its context menu.

Click Apply to import accounts. Status of the import will be displayed on the [Journal](/en/docs/mt5/manager/toolbox#journal) tab of the Toolbox window.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">All accounts are imported as disabled. Later they can be manually enabled on the <a href="/en/docs/mt5/manager/account_tradeaccount#enable" class="topiclink">Account</a> tab.</span></li><li class="p_tableatten"><span class="f_tableatten">You cannot import clients' financial data (balance) and security data.</span></li><li class="p_tableatten"><span class="f_tableatten">After importing the accounts, set <a href="/en/docs/mt5/manager/account_security#password" class="topiclink">passwords</a> for them.</span></li></ul></td></tr></tbody></table>

## Associating data [#](account_import#columns)

This function allows you to match data in an imported file with the data fields of client records on the trading platform side. To start matching, click Columns in the import window.

![Selecting the columns](/en/docs/mt5/manager/img/accounts_import_columns.png "Selecting the columns")

Set the sequence of columns according to how they are located in an imported file in the right part of the window:

-   Add — add a selected available column to selected ones.
-   Remove — remove a selected column from the list of selected ones. The Login cannot be removed.
-   Up — move an added column upward relative to other columns.
-   Down — move an added column downward relative to other columns.
-   Reset — return default column settings.

You can also move columns by double-clicking on them.

The sequence of selected columns is very important, because this is the way they are associated with the fields in the system. To skip one or more columns in the source file, use the special "Skip column" item. For example, if this point is set third from top in the sequence, the third column in the imported file will be skipped.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When importing accounts exported from the MetaTrader 4 platform, field matching is determined automatically.</span></p></td></tr></tbody></table>

[Creation of Accounts](/en/docs/mt5/manager/account_create)

[Preliminary Accounts](/en/docs/mt5/manager/preliminary_accounts)