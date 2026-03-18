# Accounts

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts

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
                -   [Creating Account](/en/docs/mt5/platform/administration/admin_accounts/account_add)
                -   [Editing Account](/en/docs/mt5/platform/administration/admin_accounts/account_edit)
                -   [Preliminary Accounts](/en/docs/mt5/platform/administration/admin_accounts/preliminary_accounts)
                -   [Archive and Backup Bases](/en/docs/mt5/platform/administration/admin_accounts/accounts_archive)
                -   [Import of Accounts from File](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_export)
                -   [Import of Accounts from MetaTrader 5](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt)
                -   [Checking and Fixing Balance](/en/docs/mt5/platform/administration/admin_accounts/account_balance_check)
                -   [Account Allocation Settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups)
                -   [Corporate Links](/en/docs/mt5/platform/administration/admin_accounts/corporate_links)
                -   [Links to Depositing and Withdrawing](/en/docs/mt5/platform/administration/admin_accounts/deposit_withdrawal)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Accounts

# Accounts

This section enables management of accounts on the server: [creation](/en/docs/mt5/platform/administration/admin_accounts/account_add), [setup](/en/docs/mt5/platform/administration/admin_accounts/account_edit) and control of account trading states. Complete information is available for each client: personal data, all open positions and orders, financial status and security parameters.

![Accounts](/en/docs/mt5/platform/img/accounts.png "Accounts")

Depending on items selected in the context menu, different [account details](/en/docs/mt5/platform/administration/admin_accounts/account_edit#personal), time and address of last access to the server, etc. are shown here. Accounts can be sorted out by any of the fields. Click on a column name to sort.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">All accounts are stored separately for each <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server" class="topiclink">trade server</a>, depending on the server the <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#trade_server" class="topiclink">group</a>, to which the account belongs, is bound to. A <a href="/en/docs/mt5/platform/administration/admin_managers" class="topiclink">manager</a> can see and manage only accounts that belong to the same server, to which the manager's account belongs.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/platform/administration/admin_accounts#type" class="topiclink">Account type</a> is determined by the group to which the account belongs.</span></li></ul></td></tr></tbody></table>

## Requesting Accounts [#](admin_accounts#request)

To request accounts use a line located in the bottom part of the window. In the field to the right of ![Find](/en/docs/mt5/platform/img/find_button.png "Find") specify accounts using one of the following methods:

-   Specify the precise number of an account or of several accounts comma separated;
-   Specify mask "\*" to request all accounts;
-   Select a [group](/en/docs/mt5/platform/administration/admin_groups) from the dropdown list to request accounts included into a certain group.

In the next field select a data base, from which accounts will be requested: current or archive. You can also specify one of backup databases created on the server by selecting "More backups". The following window will appear at that:

![Period of backups](/en/docs/mt5/platform/img/backups_period.png "Period of backups")

Specify the period for requesting backup copies:

-   Period — in this field you can choose one of the predefined request periods;
-   From — starting date of the selection. A date can be specified manually of using the calendar that is opened by pressing the ![Calendar](/en/docs/mt5/platform/img/calendar_button.png "Calendar") button;
-   To — end date of the selection.

Once a period is specified, additional items appear in the field of choosing a database — all the backup copies that were made within the specified period of time.

To display the accounts press the "Request" button.

## Working with Accounts [#](admin_accounts#manage)

To [add](/en/docs/mt5/platform/administration/admin_accounts/account_add) or [modify](/en/docs/mt5/platform/administration/admin_accounts/account_edit) an account, press the "![New](/en/docs/mt5/platform/img/add_button.png "New") New" and "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" buttons respectively. They can be found in the ["Edit"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, in the standard part of [toolbar](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) or in the [context menu](/en/docs/mt5/platform/administration/admin_accounts#context). You can also open an account for editing by a double click on it with the left mouse button. To delete an account, one should press the "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete" button.

The accounts can be modified and deleted in groups. To do it, select them in the list with the mouse while holding the "Ctrl" or "Shift" keys.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">When an account is deleted its trade history (orders and deals) is not deleted. Do not use logins of deleted account when creating new ones.</span></p></td></tr></tbody></table>

## Account types [#](admin_accounts#type)

The account type is determined by the [type of the group](/en/docs/mt5/platform/administration/admin_groups/group_types), in which the account is located. For convenience, different icons are used for different types of accounts:

-   ![Demo account](/en/docs/mt5/platform/img/demo_account_icon.png "Demo account") — demo
-   ![Preliminary account](/en/docs/mt5/platform/img/preliminary_account_icon.png "Preliminary account") — preliminary
-   ![Live account](/en/docs/mt5/platform/img/real_account_icon.png "Live account") — live
-   ![Manager account](/en/docs/mt5/platform/img/manager_account_icon.png "Manager account") — manager
-   ![Technical](/en/docs/mt5/platform/img/technica_account_icon.png "Technical") — technical (the "[Show to regular managers](/en/docs/mt5/platform/administration/admin_accounts/account_edit#limits)" permission disabled)
-   ![Disabled](/en/docs/mt5/platform/img/disabled-account-icon.png "Disabled") — disabled (the "[Enable this account](/en/docs/mt5/platform/administration/admin_accounts/account_edit#enable)" permission disabled)

## Context Menu [#](admin_accounts#context)

The context menu of the list of accounts allows executing the following commands:

-   ![New](/en/docs/mt5/platform/img/add_button.png "New") New — [create](/en/docs/mt5/platform/administration/admin_accounts/account_add) a new account.
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — [edit](/en/docs/mt5/platform/administration/admin_accounts/account_edit) a selected account.
-   ![Edit group](/en/docs/mt5/platform/img/edit_group_button.png "Edit group") Edit group — [edit](/en/docs/mt5/platform/administration/admin_groups/groups_settings) the group a selected account is located in.
-   ![Edit manager](/en/docs/mt5/platform/img/manager_account_icon.png "Edit manager") Edit manager — edit the [manager account](/en/docs/mt5/platform/administration/admin_managers), created on the basis of the selected account.
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected account. When an account is deleted, all related trading operations are automatically removed.
-   ![Request](/en/docs/mt5/platform/img/request_button.png "Request") Request — execute the [request](/en/docs/mt5/platform/administration/admin_accounts#request) of accounts.
-   ![Move to Archive](/en/docs/mt5/platform/img/move_to_archive_button.png "Move to Archive") Move to Archive — move the selected account to the [archive](/en/docs/mt5/platform/administration/admin_accounts/accounts_archive) database. When an archive or reserve database is selected, this command is changed to "![Restore](/en/docs/mt5/platform/img/restore_icon.png "Restore") Restore". Using it, you can return the account to the current database.
-   Balance — open the submenu of commands for working with [balance and credit assets](/en/docs/mt5/platform/administration/admin_accounts/account_balance_check) of an account:
    -   Check Balance — when this command is executed, the calculation of total profit/loss by all the [deals](/en/docs/mt5/platform/administration/admin_deals) of a selected account is performed. Obtained value is compared with the current balance of the account. In case the values are not equal, the following entry appears in the [journal](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_journal): ''account xxx has invalid balance: xxx.xx, valid: xxx.xx".
    -   Fix Balance — when this command is executed, the calculation of total profit/loss by all the deals of a selected account is performed. Obtained value is written as the current balance of the account. The operations of balance correction are necessary for [restoring accounts](/en/docs/mt5/platform/administration/admin_accounts/accounts_archive) and for manual correction of trade history.
-   Copy As — copy accounts selected in the list:
    -   ![Copy as lines](/en/docs/mt5/platform/img/copy_button.png "Copy as lines") Lines — copy entire selected information.
    -   List of Logins — copy the list of logins only.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export — [export](/en/docs/mt5/platform/administration/common_info/export) the selected accounts as a \*.HTM, \*.HTML or \*.CSV file.
-   ![Import from File](/en/docs/mt5/platform/img/import_button.png "Import from File") Import from File — [import](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_export) accounts from a CSV file.
-   ![Import from Server](/en/docs/mt5/platform/img/import_from_server_icon.png "Import from Server") Import from Server — [import](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt) accounts from a MetaTrader 4 or MetaTrader 5 server.
-   ![Email...](/en/docs/mt5/platform/img/mail_create_button.png "Email...") E-Mail — [send a message](/en/docs/mt5/platform/administration/mail#create) to the account owner via the internal mail system or by email.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request all [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) entries on the selected account.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window.
-   Enabled only — show only [enabled accounts](/en/docs/mt5/platform/administration/admin_accounts/account_edit#enable) in the list. Enable this option to leave only active accounts in the list.
-   Auto Arrange — if this option is enabled the size of columns is selected automatically.
-   Grid — this option shows/hides field separators in the table of accounts.
-   Columns — using this sub-menu, one can choose which [details of accounts](/en/docs/mt5/platform/administration/admin_accounts/account_edit#personal) will be displayed in the list.

[Import of Clients from MetaTrader 5](/en/docs/mt5/platform/administration/clients/clients_import_mt5)

[Creating Account](/en/docs/mt5/platform/administration/admin_accounts/account_add)