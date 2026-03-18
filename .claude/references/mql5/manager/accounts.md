# Clients and Trading Accounts

> Source: https://support.metaquotes.net/en/docs/mt5/manager/accounts

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)Clients and Trading Accounts

# Clients and Trading Accounts

The Manager terminal supports the full cycle of maintaining customers: [opening](/en/docs/mt5/manager/account_create) and configuring accounts, [depositing funds](/en/docs/mt5/manager/account_balance) and [performing trade operations](/en/docs/mt5/manager/trading). Complete information is always available for each client: [personal data](/en/docs/mt5/manager/clients#personal), all [open positions and orders](/en/docs/mt5/manager/account_overview), account financial status and [history of all operations](/en/docs/mt5/manager/account_history).

You can also see the accounts which are [currently connected](/en/docs/mt5/manager/online_accounts) to the trade server.

![The Manager terminal allows you to open and configure accounts, perform balance and trade operations and view the full history of accounts](/en/docs/mt5/manager/img/accounts_overview.png "The Manager terminal allows you to open and configure accounts, perform balance and trade operations and view the full history of accounts")

The context menu of Client, Trading Accounts and Online Users provides multiple commands:

-   The shown data can be managed using the Columns command.
-   Clients [can be informed](/en/docs/mt5/manager/communication) by using "![Notification...](/en/docs/mt5/manager/img/push_notification_icon.png "Notification...") Notification..." and "![Email...](/en/docs/mt5/manager/img/mail_create_icon.png "Email...") Email..." commands.
-   Details on clients' operations can be retrieved from [the trade server journal](/en/docs/mt5/manager/server_journal) using the "![Journal...](/en/docs/mt5/manager/img/journal_icon.png "Journal...") Journal..." command.
-   For the fast [balance check based on the operations history](/en/docs/mt5/manager/account_balance#fix) and for relevant corrections — the Balances submenu.
-   For convenient selection of customers and accounts in the list — the "Select by" submenu. Copy logins to the clipboard and click "Select By \\ Logins from Clipboard" in the context menu. Accounts with these login numbers will be instantly found and selected in the list. You can similarly use the accounts list from a text file.

The context menu also allows you to [export](/en/docs/mt5/manager/beginning_advanced/export) and [import accounts](/en/docs/mt5/manager/account_import), as well as perform [bulk operations](/en/docs/mt5/manager/bulk_operations). If Autoscroll is enabled, the list of clients and accounts is scrolled to the last one when a new trading account is added to the list. The scroll option only works if the count list is sorted by a login.

![The context menu provides multiple commands for managing accounts](/en/docs/mt5/manager/img/account_list.png "The context menu provides multiple commands for managing accounts")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Information about clients and accounts in some sections may be unavailable if a manager has not enough permissions. Permissions are appointed by the platform administrator.</span></p></td></tr></tbody></table>

## Account types [#](accounts#type)

The following account types are available in the trading platform:

-   ![Demo account](/en/docs/mt5/manager/img/demo_account_icon.png "Demo account") — demo accounts to trade in a training mode without investing real money.
-   ![Contest account](/en/docs/mt5/manager/img/contest_account_icon.png "Contest account") — accounts used in trader contests.
-   ![Preliminary account](/en/docs/mt5/manager/img/preliminary_account_icon.png "Preliminary account") — [preliminary accounts](/en/docs/mt5/manager/preliminary_accounts) for fast request of real accounts directly from client terminals.
-   ![Live account](/en/docs/mt5/manager/img/real_account_icon.png "Live account") — live accounts for real trading.
-   ![Manager account](/en/docs/mt5/manager/img/manager_account_icon.png "Manager account") — an account for working with traders and managing the platform.

The account type is determined by the [type of the group](/en/docs/mt5/manager/account_tradeaccount#group), in which the account is located:

-   Demo — the names of these groups contain "demo".
-   Manager — the names of the groups contain "manager".
-   Contest — the names of the groups contain "contest".
-   Preliminary — a group with the "preliminary" name.
-   Real — other groups that do not match the above conditions.

## Filtering accounts and clients [#](accounts#filter)

Use filters for a convenient work with clients and accounts. All [clients](/en/docs/mt5/manager/clients) and accounts available to a manager are shown by default. You may use filters to view information, which correspond to selected criteria. For example, you can set the filter to display clients from a selected country, clients, who responded to a certain marketing campaign, or accounts with a certain language.

To apply a previously created filter, select it from the Filter menu. To return to the initial list of accounts, click "Not selected".

![A menu for working with filters](/en/docs/mt5/manager/img/account_filter.png "A menu for working with filters")

To create or edit filters, click Customize. The list of all previously created filters is shown in the Filters tab. Click twice on the filter to change its parameters.

![Configuring the filters](/en/docs/mt5/manager/img/account_filter_customize.png "Configuring the filters")

Set a name of a filter and then configure parameters for filtering accounts:

-   Enabled only accounts — show only [enabled accounts](/en/docs/mt5/manager/account_tradeaccount#enable), disabled accounts will be hidden.
-   Trading — show accounts with the enabled or disabled [trading option](/en/docs/mt5/manager/account_tradeaccount#limits).
-   Country, City, Language — show accounts from a selected country, city or with a selected language. Such filters will be useful, for example, for sending information to clients in bulk via [email](/en/docs/mt5/manager/communication#mail) or [push notifications](/en/docs/mt5/manager/communication).
-   Agent account — show only accounts of a specified [agent](/en/docs/mt5/manager/account_tradeaccount#agent_account). The filter allows analyzing the work of agents.
-   Group — show only accounts from a specified group. This filter can be used for separate work with real and demo accounts.
-   Company — show accounts, in which this [company](/en/docs/mt5/manager/account_personal) is specified. Such a filter is useful for working with corporate clients.
-   MetaQuotes ID — show accounts with this [MetaQuotes ID](/en/docs/mt5/manager/account_personal#mqid) or all accounts which have any MetaQuotes ID. In the latter case, leave the field empty and invert the filter using the !["Includes" filter mode](/en/docs/mt5/manager/img/filter_include_icon.png ""Includes" filter mode") button.
-   Lead campaign, Lead source — show accounts with a specified [lead campaign and lead source](/en/docs/mt5/manager/account_personal#leadsource). This filter allows evaluating the efficiency of your marketing campaigns.
-   Comment — show accounts with a specified comment. This filter allows viewing accounts according to your own internal criteria.

The following filtering options are available for [online accounts](/en/docs/mt5/manager/online_accounts):

-   Country, City — show accounts from the selected country or city. Such filters can be useful for sending bulk notification to clients, such as [emails](/en/docs/mt5/manager/communication#mail) or [push notifications](/en/docs/mt5/manager/communication).
-   Group — show only accounts from the specified group. This filter can be used for separate work with real and demo accounts.
-   Client — show accounts with the selected connection type: desktop, mobile, and manager terminals, API, etc. Use the filter to analyze what features are used by your clients.
-   Version — show accounts which use the specified client application build. The filter can be used to identify clients using old terminal versions.
-   Balance — show accounts having the balance within the specified range. When combined with the registration date filter, this option enables detection of inactive clients.
-   Equity — show accounts having the equity within the specified range. When combined with the balance filter, this option enables detection of clients with large floating profit or loss.

The following options are available for [client](/en/docs/mt5/manager/clients) filters:

-   Country, City, Language — show clients from the selected country, city or with the selected language. Such filters are useful for comprehensive audience analysis.
-   Company — show clients, in whose accounts this [company](/en/docs/mt5/manager/clients#company) is specified. Such a filter is useful for working with corporate clients.
-   Introducer — display clients, who were introduced by the specified user (the account number is specified). The filter allows analyzing the work of agents.
-   Assigned manager — show clients managed by the [specified assigned manager](/en/docs/mt5/manager/clients#general). The filter is useful for managers, working with clients, as well as for controlling the performance of such managers.
-   Lead campaign, Lead source — show clients with the specified [lead campaign and lead source](/en/docs/mt5/manager/account_personal#leadsource). This filter allows evaluating the efficiency of your marketing campaigns.
-   Type — display only private or only corporate clients in the list.
-   Status — display clients with a selected registration status in the list. For example, the filter can show clients with incomplete registration, inactive clients, etc.

The filter can be immediately enabled from the editing window by clicking Apply.

Filters enable selection of entries not only based on fields matching the specified value, but also by the "Except" and "Not empty field" parameters. Enter the desired value in the filter field and click !["Includes" filter mode](/en/docs/mt5/manager/img/filter_include_icon.png ""Includes" filter mode"), it will change to !["Except" filter mode](/en/docs/mt5/manager/img/filter_exclude_icon.png ""Except" filter mode"). The filter will select accounts/clients, the parameters of which do not match the specified value. For example, you can use the filter to get a list of accounts, which do not belong to the specified group, as well as a list of clients without an assigned manager. In the latter case, switch the filter mode and leave the field blank.

[Hot Keys](/en/docs/mt5/manager/hotkeys)

[Clients](/en/docs/mt5/manager/clients)