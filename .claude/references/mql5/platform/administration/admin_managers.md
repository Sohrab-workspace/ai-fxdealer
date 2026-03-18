# Managers

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_managers

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Managers

# Managers

User logins created in the Managers section possess special rights to manage the system (edit accounts, quotes for clients, generate reports, etc.)

![Managers](/en/docs/mt5/platform/img/managers.png "Managers")

Manager accounts are all shown in a table with the following fields:

-   Login — manager's account.
-   Name — manager's name.
-   Mailbox — name of the manager's mailbox.
-   Groups — groups serviced by this manager.

Managers who have permissions to connect via the administrator terminal are marked by icon ![Administrator](/en/docs/mt5/platform/img/managers_vip_icon.png "Administrator"), all other managers - by ![Manager](/en/docs/mt5/platform/img/managers_icon.png "Manager").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Manager accounts are created only based on accounts added in the corresponding <a href="/en/docs/mt5/platform/administration/admin_accounts" class="topiclink">section</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">A manager can service only those <a href="/en/docs/mt5/platform/administration/admin_accounts" class="topiclink">accounts</a> that belong to the server, to which the <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#trade_server" class="topiclink">group</a> the manager is included to refers.</span></li></ul></td></tr></tbody></table>

In order to create or edit a manager account, press "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" and "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit", respectively. In order to delete a manager, press "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete". These commands are available in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar and in the context menu. Upon the execution of these commands, a window of manager settings will appear.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Additional general information about working with configuration records is given in the <a href="/en/docs/mt5/platform/administration/common_info/common_instructions" class="topiclink">"Working with Instructions"</a> section.</span></p></td></tr></tbody></table>

## Supervision of managers [#](admin_managers#control)

For the additional control of access to the server data, managers' search queries, data exports, copying to clipboard and table filters used are logged in the platform. The actions are logged on the Manager and Administrator terminal side and on the trading server side.

For example, if the employee exports a report or data on online accounts, clients and quotes, the following entries will be added to the server log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2020.02.06&nbsp;08:24:01.114&nbsp;&nbsp;&nbsp;&nbsp;10.25.217.106&nbsp;&nbsp;&nbsp;&nbsp;'1024':&nbsp;export&nbsp;report&nbsp;'Accounts\Accounts&nbsp;Groups'&nbsp;to&nbsp;'Accounts&nbsp;Groups&nbsp;2020_01_22&nbsp;13_00_50.html'</span><br><span class="f_CodeExample">2020.02.06&nbsp;08:24:30.865&nbsp;&nbsp;&nbsp;&nbsp;10.25.217.106&nbsp;&nbsp;&nbsp;&nbsp;'1024':&nbsp;export&nbsp;online&nbsp;trading&nbsp;accounts,&nbsp;4&nbsp;records&nbsp;to&nbsp;'Online&nbsp;Users.htm'</span><br><span class="f_CodeExample">2020.02.06&nbsp;08:24:44.756&nbsp;&nbsp;&nbsp;&nbsp;10.25.217.106&nbsp;&nbsp;&nbsp;&nbsp;'1024':&nbsp;export&nbsp;clients,&nbsp;85&nbsp;records&nbsp;to&nbsp;'Clients.csv'</span><br><span class="f_CodeExample">2020.02.06&nbsp;08:25:17.225&nbsp;&nbsp;&nbsp;&nbsp;10.25.217.106&nbsp;&nbsp;&nbsp;&nbsp;'1024':&nbsp;export&nbsp;ticks&nbsp;of&nbsp;'Gold'&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;2017.06.26,&nbsp;57895&nbsp;records&nbsp;to&nbsp;'Gold.2017_06_26.Ticks.csv'</span></p></td></tr></tbody></table>

When copying configurations to clipboard, the following entry is added to the logs:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2020.02.06&nbsp;08:24:30.865&nbsp;&nbsp;&nbsp;&nbsp;192.168.0.1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'1033':&nbsp;copy&nbsp;MetaTrader&nbsp;5&nbsp;Main&nbsp;Server&nbsp;Journal&nbsp;to&nbsp;clipboard,&nbsp;6&nbsp;records</span></p></td></tr></tbody></table>

## Common [#](admin_managers#common)

![Common](/en/docs/mt5/platform/img/managers_common.png "Common")

The following parameters are specified on this tab:

-   Login — manager login, added in the ["Accounts"](/en/docs/mt5/platform/administration/admin_accounts) section. The specified account must be included to the [managers' group](/en/docs/mt5/platform/administration/admin_groups/group_types#manager).
-   Mailbox name — name of the manager's mailbox. If the mailbox name is not specified, the manager will not be able to send emails via the [internal mailing system](/en/docs/mt5/platform/administration/mail).

In the "Groups" filed, [groups of accounts](/en/docs/mt5/platform/administration/admin_groups) that will be serviced by the manager should be specified:

-   Add — add a service group. After you press this button, a new line will appear in the window. Specify one of the groups from the list here. You can use mask "\*" and negation sign "!" to set up groups. For example, if you specify "demo\*" it will indicate all groups, whose name (including path) starts with "demo" (for example, demo\\forex, demoforex, demoforex\\usd). If you specify "!managers\*,\*,", it will indicate all groups except those, whose name starts with "managers".
-   Delete — delete a selected group.
-   Edit — edit a selected group. The same action can be performed buy double-clicking on the group.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">A manager account can be create only based on the <a href="/en/docs/mt5/platform/administration/admin_accounts" class="topiclink">account</a> included to the <a href="/en/docs/mt5/platform/administration/admin_groups/group_types#manager" class="topiclink">managers' group</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">In the manager terminal only the accounts that belong to the groups permitted for the manager are available.</span></li></ul><ul><li class="p_tableatten"><span class="f_ol">Rules for the groups are check from top to bottom. If you allow all groups in the first row, you will not be able to prohibit some of them in the next rules.</span></li><li class="p_tableatten"><span class="f_ol">A rule cannot consist of prohibition only. For example, the rule "!demo*" is not valid. A prohibition can be used together with a permission to see some other groups. For example, "!demo*,real*".</span></li></ul></td></tr></tbody></table>

## Permissions [#](admin_managers#permissions)

![Permissions](/en/docs/mt5/platform/img/managers_permissions.png "Permissions")

Managers' permissions and access to different data are set up on this tab:

-   Available logs — selecting period, logs within which will be available to the manager.
-   Available reports — selecting period, within which a manager is able to view various reports and request account trading history in the Manager terminal. In addition to this parameter, individual data depth limits from the [Reports](/en/docs/mt5/platform/administration/admin_managers#reports) section are also checked when requesting reports. The strictest limit always applies. For example, if the 'Available reports' parameter is set to '6 months' and a specific report has a limit of 90 days, the manager will only be able to request data for the past 90 days.
-   Role — here you can select one of predefined sets of permissions. Using buttons "Save As" and "Delete" you can save and delete your own sets of permissions. These sets are saved in /roles folder of the [directory](/en/docs/mt5/platform/administrator/interface/main_menu/menu_file#terminal_data), where the terminal information in the user's profile is stored on the PC.

Below the list of permissions is located. In order to enable a permission, tick off them. The following permissions are available here:

-   Connection type
    -   Connect using MetaTrader 5 Administrator — connection to the server using the administrator terminal.
    -   Connect using MetaTrader 5 Manager— connection to the server using the manager terminal.
-   Configuration setup
    -   Configure network — possibility to configure the [platform components](/en/docs/mt5/platform/administration/admin_network).
    -   Configure VPS — configuring [Sponsored VPS](/en/docs/mt5/platform/administration/integration/integration_vps) for traders.
    -   Configure mail servers — setting up [integration with email services](/en/docs/mt5/platform/administration/integration/integration_mail).
    -   Configure messengers — setting up [integration with SMS providers and messengers](/en/docs/mt5/platform/administration/integration/integration_sms).
    -   Configure KYC — setting up [integration with KYC services](/en/docs/mt5/platform/administration/integration/integration_kyc).
    -   Configure payments — configuring integration with payment systems (in development).
    -   Configure web services — access to the [Integration \\ Web services](/en/docs/mt5/platform/administration/integration/integration_web_services) section.
    -   Configure IP access list — setup of [access](/en/docs/mt5/platform/administration/security/admin_access) to the platform by IP addresses.
    -   Configure automations — setting up [automatic actions](/en/docs/mt5/platform/administration/automation) for specified scenarios.
    -   Configure server operation time — setup of the server [working hours](/en/docs/mt5/platform/administration/admin_time).
    -   Configure holidays — setting up [holidays](/en/docs/mt5/platform/administration/admin_holidays).
    -   Configure groups — setting up [groups of accounts](/en/docs/mt5/platform/administration/admin_groups).
    -   Configure allocations — setting up groups, in which traders are able to open [demo and preliminary real accounts](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups) directly from client terminals.
    -   Configure corporate links — setting up [links](/en/docs/mt5/platform/administration/admin_accounts/corporate_links) to be displayed in client terminals.
    -   Configure managers' permissions — setting up these permissions.
    -   Configure request routing — configuring [rules of routing](/en/docs/mt5/platform/administration/requests_routing) of requests.
    -   Configure gateways — configuring parameters of [gateways](/en/docs/mt5/platform/administration/admin_gateways).
    -   Configure plugins — managing [plugins](/en/docs/mt5/platform/administration/admin_plugins).
    -   Configure datafeeds — setting up [datafeeds](/en/docs/mt5/platform/administration/admin_feeds).
    -   Configure reports — setting up [reports](/en/docs/mt5/platform/administration/admin_reports).
    -   Configure symbols — setting up [financial symbols](/en/docs/mt5/platform/administration/admin_symbols).
    -   Configure history charts synchronization — setting up [synchronization of history data](/en/docs/mt5/platform/administration/admin_synchronization) with other servers.
    -   Configure ECN — setting up [ECN](/en/docs/mt5/platform/administration/ecn).
    -   Configure funds and ETF — setting up [investment funds](/en/docs/mt5/platform/administration/fund_etf).
-   Administration
    -   Access server logs — permission to request [server operation logs](/en/docs/mt5/platform/administration/admin_network/network_journal).
    -   Receive automatic server reports — permission to receive automatically generated reports on the server operation.
    -   Edit charts — permission to [edit](/en/docs/mt5/platform/administration/admin_charts#add_edit) history data on the server. To access the data, the manager also needs the "Configure symbols" permission.
    -   Send emails — permission to [send emails](/en/docs/mt5/platform/administration/mail#create) via the internal mailing system.
    -   Send news — permission to [send news](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news#send). A manager/administrator is able to send news only if their account belongs to a [group](/en/docs/mt5/platform/administration/admin_groups/groups_settings#trade_server) created at the main trade server.
    -   Export data — the ability to copy to the clipboard and export account, order, and other data from the Administrator and Manager terminals to external files. The permission does not affect the ability to [export server configurations](/en/docs/mt5/platform/administration/common_info/import_export_config) from the administrator terminal.
    -   Manage server machines — access to a menu for [managing the computer](/en/docs/mt5/platform/administration/admin_network/manage_machines) on which the platform server is running.
-   Accounts
    -   Accountant (deposit/withdraw) — permission to work with assets on accounts.
    -   Access accounts — possibility to view the list of [accounts](/en/docs/mt5/platform/administration/admin_accounts).
    -   View technical accounts — when combined with "[Show to regular managers](/en/docs/mt5/platform/administration/admin_accounts/account_edit#limits)", provides greater convenience in working with various testing and technical accounts. Disable the "Show to regular managers" permission for all technical accounts, and then disable access to technical accounts for the managers who do not configure the platform. Otherwise, such technical accounts can be confusing for managers working with clients.
    -   Manage technical accounts — with this permission, the manager can enable and disable options "[Show to regular managers](/en/docs/mt5/platform/administration/admin_accounts/account_edit#limits)" and "[Include in server reports](/en/docs/mt5/platform/administration/admin_accounts/account_edit#limits)" for a trading account. Without this permission, the manager can only see the states of the relevant options, without the ability to change them (read-only).
    -   Access the account personal details — permission to view [personal details on accounts](/en/docs/mt5/platform/administration/admin_accounts). You can separately provide access to the name, location (country, city, region, zip code), address, document number, email, phone number, and general data (other less important data: language, status, comment, MetaQuotes ID, etc.).
    -   Edit accounts — [modifying account details](/en/docs/mt5/platform/administration/admin_accounts).
    -   Delete accounts — permission to delete client accounts in the administrator and the manager terminals and via Manager API. In order to delete accounts, a manager account must also have the "Edit accounts" permission.
    -   View currently connected clients — permission to view accounts currently connected to the server.
    -   Confirm dangerous actions — confirmation dialog is displayed in the manager terminal by default when performing balance operations on a client account and during bulk order closing. In order to perform one of these actions, a randomly generated character sequence should be entered. If disabled, the actions are performed immediately with no confirmation.
    -   Push notifications — a right to send push notifications to clients' mobile devices using the manager terminal. Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 5 Mobile for [iPhone](https://download.terminal.free/cdn/mobile/mt5/ios?hl=en&utm_campaign=download&utm_source=metatrader5.help "iPhone") and [Android](https://download.terminal.free/cdn/mobile/mt5/android?hl=en&utm_campaign=download&utm_source=metatrader5.help "Android"). Detailed information is provided in the manager terminal user guide.
-   Dealing
    -   Access orders and positions — permission to view trade [orders](/en/docs/mt5/platform/administration/admin_orders), [deals](/en/docs/mt5/platform/administration/admin_deals) and [positions](/en/docs/mt5/platform/administration/admin_positions). To be able to access this data, the manager must also have the "Access accounts" permission. The "Access orders and positions" permission affects the possibility of enabling the "Modifying of orders" and "Dealer" permissions.
    -   Edit orders, positions, and deals — permission to edit any fields of [orders](/en/docs/mt5/platform/administration/admin_orders), [deals](/en/docs/mt5/platform/administration/admin_deals) and [positions](/en/docs/mt5/platform/administration/admin_positions) in the administrator and the manager terminals and via Manager API. This permission also provides access to the Exposure tab and the ability to place trading requests on behalf of the client in the Manager terminal.
    -   Delete orders, positions, and deals — permission to delete any [orders](/en/docs/mt5/platform/administration/admin_orders), [deals](/en/docs/mt5/platform/administration/admin_deals) and [positions](/en/docs/mt5/platform/administration/admin_positions) in the administrator and the manager terminals and via Manager API. In order to delete trade operations, a manager account must also have the "Edit orders, positions and deals" permission.
    -   Dealer — permission to perform trading and dealing operations in the manager terminal. Also provides access to the Exposure tab in the Manager terminal. In addition, it controls access to the availability of group position closing and splitting feature in the Manager terminal.
    -   Supervisor — permission to see the entire queue of requests coming from client groups available to the manager, and to see how the requests are processed by other dealers in the manager terminal. A manager works as a Supervisor being not connected as a dealer in the manager terminal. Once the manager has connected as a dealer, they will see only their own requests coming for processing according to the [routing rules](/en/docs/mt5/platform/administration/requests_routing).
    -   Show raw quotes without spread difference — if this permission is given, an additional command "Show raw quotes" appears in the context menu of the "Market Watch" window in the manager terminal. By enabling it, the manager will be able to see the quotes without [applying the spread settings](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_common) of the manager group.
    -   Throw in quotes — permission to throw in quotes from the manager terminal.
    -   Modify spread and execution mode — permission to modify  spread and execution mode from the manager terminal.
    -   Risk manager — permission to receive information on the total clients' positions and company's coverage positions. The parameter affects the availability of section "Summary Positions" and "Exposure" as well as of the account "Exposure" tab in the Manager terminal.
    -   Edit groups (margin settings) — permission to modify the [margin settings of groups](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_margin) via the manager terminal.
    -   Edit groups (commission settings) — permission to modify the [commission settings of groups](/en/docs/mt5/platform/administration/admin_groups/groups_comissions) via the manager terminal.
    -   Receive reports — permission to request and receive various reports on clients' operations.

-   Ultency Matching Engine
    -   Access configuration — permission to view Ultency setting, including [provider gallery](/en/docs/mt5/platform/administration/ultency/ultency_connect), [provider symbols](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols), [aggregated symbols](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols), [translations](/en/docs/mt5/platform/administration/ultency/ultency_translations), and [routing](/en/docs/mt5/platform/administration/ultency/ultency_routing).
    -   Edit configuration — permission to edit those settings, including ability to add new liquidity providers.
    -   Delete configuration — delete those settings.
    -   Service desk — use the [built-in communication system](/en/docs/mt5/platform/administration/ultency/ultency_service_desk).

-   Payments
    -   Access payments — view current and processed payments and payment accounts.
    -   Process payments — confirm and decline manually processed payments via the Manager terminal.
    -   Edit payments — edit current and processed payments and payment accounts.
    -   Delete payments — delete current and processed payments and payment accounts.
-   Back office — permission to access the [Clients](/en/docs/mt5/platform/administration/clients) section. Permissions in this section apply to both Manager and Administrator terminals.
    -   Access clients — general access to the Clients section.

-   -   Access personal details — access to clients' personal data. You can separately provide access to the name, location (country, city, region, zip code), address, document number, email, phone number, and general data (other less important data: language, status, Lead Source, Lead Campaign, etc.).

-   -   Create clients — permission to [create new client](/en/docs/mt5/platform/administration/clients#create) records manually.
    -   Edit clients — permission to edit any client data, except documents.
    -   Delete clients — permission to delete client records.
    -   KYC check — ability to [launch](/en/docs/mt5/platform/administration/clients#kyc) auto verification of client data using [integration with KYC services](/en/docs/mt5/platform/administration/integration/integration_kyc).
    -   Access documents — permission to view [clients' documents](/en/docs/mt5/platform/administration/clients#documents).
    -   Create documents — permission to add general information about documents to client records.
    -   Edit documents — permission to edit general information about documents in client records.
    -   Delete documents — permission to delete general information about documents from client records.
    -   Add files to documents — permission to add [document files](/en/docs/mt5/platform/administration/clients#documents) to client records.
    -   Delete files from documents — permission to delete document files from client records.
    -   Access comments — permission to read comments to client records and documents.
    -   Add comments — permission to add comments to clients and their documents.
    -   Delete comments — permission to delete comments to clients and documents.
-   Finteza
    -   Access to Finteza — access to the [Finteza Analytics](/en/docs/mt5/platform/administration/integration) section.
    -   View websites — view website related information from Finteza in the Analytics section of the Manager terminal.
    -   View campaigns — permission to view information on marketing campaigns from Finteza in the Analytics section of the Manager terminal.
    -   View reports — the permission is currently not used.
-   Subscriptions — access to the [Subscriptions](/en/docs/mt5/platform/administration/subscriptions) section.
    -   View subscriptions — view and edit [subscription settings](/en/docs/mt5/platform/administration/subscriptions/subscriptions_common) in the Administrator terminal, as well as view active subscriptions and the history of subscriptions in the Administrator and Manager terminal.
    -   Edit subscriptions — ability to [create](/en/docs/mt5/platform/administration/subscriptions/subscriptions_control#user_subscriptions) and [delete subscriptions](/en/docs/mt5/platform/administration/subscriptions/subscriptions_control#delete_unsubscribe) for traders in the Administrator and Manager terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Once the access rights are changed the manager is automatically reconnected for changes to take effect.</span></p></td></tr></tbody></table>

## Reports [#](admin_managers#reports)

Configure manager access to [server reports](/en/docs/mt5/platform/administration/admin_reports). Click "Add" and specify the path to the report or group of reports. Next, set the permissions to view and export report data to a file and specify the depth of information that will be available to the manager.

![Configure manager access to server reports](/en/docs/mt5/platform/img/manager_reports.png "Configure manager access to server reports")

For efficient permission categorization, create a hierarchy of reports and arrange them into directories according to their purpose. For example, you can create a separate directory with dealer transaction reports, a separate directory for marketers who are responsible database analysis and customer acquisition, etc. Such categorization will assist in configuring access rights: you will only need to specify one line with the directory path rather than specify each individual report.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When reports are requested, the system checks both the individual data depth limits from the 'Reports' section and the 'Available reports' parameter from the '<a href="/en/docs/mt5/platform/administration/admin_managers#permissions" class="topiclink">Permissions</a>' section. The strictest limit always applies. For example, if the 'Available reports' parameter is set to '6 months' and a specific report has a limit of 90 days, the manager will only be able to request data for the past 90 days.</span></p></td></tr></tbody></table>

## IP Access List [#](admin_managers#access_list)

![IP Access List](/en/docs/mt5/platform/img/managers_ip_access_list.png "IP Access List")

On this tab, you can set up the range of IP addresses, from which this manager can connect. Thus you can limit managers' access, for example, to the dealing room only.

-   Add — add a range of IP addresses. As soon as you press this button, a new line will appear in the window. In fields "From" and "To" specify the first and last IP of the range, respectively.
-   Delete — delete a selected IP range.
-   Edit — modify a selected IP range. The same action can be performed by a click on the necessary line.

To complete the creation or modification of a manager, press OK. If you press "Cancel", the window will be closed, while changes will not be saved.

## Context Menu [#](admin_managers#context)

The context menu of the "Manager" section contains the following commands:

-   Servers — using this command, one can filter the managers displayed in the list by the trade server they belong to. A list containing all trade servers of the platform will be opened as soon as it is executed.
-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new manager.
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit a selected manager.
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected manager.
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move a selected manager up relative to others.
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move a selected manager down relative to others.
-   ![Sort by Login](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort by Login") Sort by Login — sort managers by their logins. Sorting is performed on the server, not on the local MetaTrader 5 Administrator.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) the settings of managers to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) the settings of managers to a file.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window.
-   Auto Arrange — if this option is enabled the size of columns is selected automatically.
-   Grid — this option shows/hides field separators in the table with managers.

[Payments in Client Terminals](/en/docs/mt5/platform/administration/payments/payments_clients)

[Orders](/en/docs/mt5/platform/administration/admin_orders)