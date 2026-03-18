# Import of Accounts from MetaTrader 5 Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Accounts](/en/docs/mt5/platform/administration/admin_accounts)Import of Accounts from MetaTrader 5

# Import of Accounts from MetaTrader 5 Server

You can easily import your account database from one MetaTrader 5 sever to another, including accounts' trading operations and history. You will need administrator accounts having access to accounts, groups and trading operations on these two servers.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can also <a href="/en/docs/mt5/platform/migration/migration_account_trade" class="topiclink">import accounts and trading operations from the MetaTrader 4 server</a>.</span></p></td></tr></tbody></table>

Open the [Accounts](/en/docs/mt5/platform/administration/admin_accounts) section in MetaTrader 5 and click "Import from Server":

![Start import from the context menu of the Accounts section](/en/docs/mt5/platform/img/migration_start.png "Start import from the context menu of the Accounts section")

Specify connection parameters:

-   Server Type — MetaTrader 5.
-   Server — the IP address and port of the MetaTrader 5 server separated by a colon.
-   Login — the number of the manager account for authentication on the server.
-   Password — the account password for authentication on the server.
-   Use certificate from file — [advanced authentication](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization) can be enabled for the manager account on the source server, from which accounts are imported. A certificate is required in this case. If the certificate has previously been installed in the storage of the operating system, it will be automatically recognized by the import system. If the certificate has not been installed, enable this option and specify the path to the file manually.

-   Certificate File — click "Browse" and specify the pfx-file of the certificate. The certificate file received in the terminal is saved in /terminal data folder/profiles/server name/certificates/.
-   Certificate Password — [the password](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization#password) of the certificate.

To import accounts, you should have an administrator or manager account on the source server, with the following [access permissions](/en/docs/mt5/platform/administration/admin_managers#accounts):

-   Connection type: MetaTrader 5 Administrator or MetaTrader 5 Manager
-   Accounts section: "Accountant", "Access accounts", "Access account personal details"
-   Dealing section: Access to trading orders (if import includes trading history)

For security purposes, you should grant to the manager account the access only to specific trading account groups for import. Also you should disable the entire group of "Configuration settings" permission and allow connections only from a certain address. After the accounts import is complete, you can disable the manager account if it is not used for other purposes.

On the receiving server, you should have an administrator account (Connection type: MetaTrader 5 Administrator) with the same permissions along with the permission to access group settings.

![Import of Accounts](/en/docs/mt5/platform/img/import_wizard.png "Import of Accounts")

## Requesting accounts

The next step is to request the accounts that you want to import from the source server. Enter your request in the "Choose groups" field. Here you can specify a comma separated list of logins or a more complex query using the "\*" masks and the "!" negation symbol.

The "Choose groups" field contains the default request of "!demo\*,!manager\*,!coverage\*,!contest\*,\*", which allows to select all accounts except from groups of demo and manager accounts, as well as coverage and contest groups.

To execute the request click "Request".

![The list of accounts received from the MetaTrader 4 server](/en/docs/mt5/platform/img/migration_accounts.png "The list of accounts received from the MetaTrader 4 server")

An account having a red background cannot be imported to the server. The following reasons are possible:

-   The group of the account on the source server and the current server have different [position accounting types](/en/docs/mt5/platform/administration/admin_groups/group_position) (hedging and netting). Try to select another group in the "Move to group" field.
-   The currency of the account deposit does not match the deposit currency of the group to which you want to import the account.
-   An account with the same number already exists on the current server or on one of other trade servers of the platform.
-   The account number is out of the [range of accounts](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#accounts) allowed for the current server.
-   The symbol, for which the account to import has orders or positions, does not exist on the server.
-   The symbol, for which the account to import has orders or positions, had different numbers of decimal places on the source and target servers.
-   The group of the account does not match any group on the server. In this case, you should specify in the appropriate field the group to move accounts to.

Information about the reason for not inability to import an account is available in the tooltip that appears when you hover the mouse over the account line.

Double click on an account to view how it would look like after import. This will open a standard [account viewing](/en/docs/mt5/platform/administration/admin_accounts/account_edit) window.

You can disable import of individual accounts from the list. To do this, click on the icon at the beginning of the account row, and then it will change to![No import](/en/docs/mt5/platform/img/access_block_icon.png "No import").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Depending on import settings, the login of a migrated account can be preserved or converted with an offset. For example, login 101980 is converted to 1101980, if the parameter "Login shift" is set to 1 000 000. If login shift is applied, the numbers of <a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit#agent_account" class="topiclink">agent accounts</a> in client records are shifted by the same value.</span></p></td></tr></tbody></table>

## Import Settings

## To import trading operations of selected clients, enable the "Import balance, trades and trade history" option. All available orders, deals and positions of the client will be imported.

You can also specify additional parameters:

-   Move to group — choose the [group](/en/docs/mt5/platform/administration/admin_groups) to import accounts to. The administrator executing the import procedure only has access to the groups on the server, to which the administrator account belongs. The list of groups available to the administrator can also be limited in [manager account](/en/docs/mt5/platform/administration/admin_managers#groups) settings.
-   Login shift — you can specify a number, by which all numbers of imported account will be shifted. The shift can be wither positive or negative. For example, 1000 or -100.

## Result of Import

The total number and the number of imported accounts will be shown on the last step:

![Result of Import](/en/docs/mt5/platform/img/migration_result.png "Result of Import")

Import details are also available in the trade server journal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">After import, the appropriate accounts on the source server must be disabled or set to the "read-only" mode to avoid trading state mismatch with the new MetaTrader 5 server.</span></li><li class="p_tableatten"><span class="f_tableatten">After completing the import for accounts having open positions, you can see the differences in equity and free margin in the Manager terminal. This may happen if quotes in the new MetaTrader 5 platform are significantly different from the ones in the source platform or a data feed is not configured. The Manager terminal calculates these values in real time according to the current prices in the platform. In the Administrator terminal, there are no differences (the values coincide with the source server) since data are taken directly from the accounts and are not recalculated.</span></li></ul></td></tr></tbody></table>

## Client connection and passwords

Random passwords are generated for imported accounts. Hashes of account passwords that were used on the source server are saved in the client record. They are used for verification during the first account connect in MetaTrader 5.

During the first connection to the imported account, the client will attempt to connect using the old password. Upon entering the incorrect password (since a new random password has been generate), a welcome dialog will be displayed:

![A welcome dialog for the client after migration to MetaTrader 5](/en/docs/mt5/platform/img/migration_client_side.png "A welcome dialog for the client after migration to MetaTrader 5")

The old account password that was used on the source server should be specified here. The client will not be able to continue without this password. A new password should be set here, which will later be used to connect to the account.

If authenticated successfully, the dialog will not be displayed again, and the client will work as usual.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can set a new password for the imported account via the administrator or manager terminal and provide it to the client. The welcome dialog will not be displayed in this case. After password change, the hash of the password used on the source server is deleted from the client record.</span></p></td></tr></tbody></table>

## Import Features

Accounts are imported in packages each containing 100 account. If an account from the package could not be imported, you will need to repeat the import. If errors occur, the previous state will not be restored. The accounts and trading operations from the package successfully imported before the error will not be removed. Before re-import, remove them manually in the following order:

-   ORDERS
-   Deals
-   Positions
-   Accounts

Importing may take a long time: it depends on the database size and your Internet connection speed.

[Import of Accounts from File](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_export)

[Checking and Fixing Balance](/en/docs/mt5/platform/administration/admin_accounts/account_balance_check)