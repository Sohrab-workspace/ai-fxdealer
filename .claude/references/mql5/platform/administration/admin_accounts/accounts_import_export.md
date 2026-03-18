# Import of Accounts from File

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_import_export

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Accounts](/en/docs/mt5/platform/administration/admin_accounts)Import of Accounts from File

# Import of Accounts from File

The administrator terminal allows to import accounts to a trade server from CSV files. In order to do it, one should execute the "![Import from File](/en/docs/mt5/platform/img/import_button.png "Import from File") Import from File" command in the [context menu](/en/docs/mt5/platform/administration/admin_accounts#context) of the "Accounts" section.

![Import of Accounts](/en/docs/mt5/platform/img/accounts_import.png "Import of Accounts")

The following settings and commands are present in the window of account importing:

-   File — path to a \*.CSV file, from which accounts &ill be imported. You can specify the path manually or select the necessary file by pressing the "Browse" button located to the right.
-   Separator — separator of data in the file (comma, semicolon, tab or space);
-   Begin from line — in this field you can specify a line in the file starting from which the data will be imported;
-   Columns — open the window of [associating columns](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_export#columns) in the imported file with the corresponding fields in the system;
-   Use only selected items — if this option is chosen then only the lines that are currently selected in the preview window below will be imported;
-   Refresh — refresh the data in the preview window.

In order to start importing the accounts, one should press the "Apply" button. The process of importing will be displayed at the ["Journal"](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_journal) tab of the "Toolbox" window.

By a double-click on a line in the preview window, you can see how the information would look like if the account was imported. The same action can be performed using the "View" command in the context menu. Using this menu you can also enable or disable the automatic arrangement of columns and the displaying of a grid.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">All the accounts are imported as disabled. Further they can be enabled manually at the <a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit#enable" class="topiclink">"Account"</a> tab.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If passwords for accounts are not imported, <a href="/en/docs/mt5/platform/administration/admin_accounts/account_edit#password" class="topiclink">set them</a> afterwards.</span></li></ul></td></tr></tbody></table>

## Associating Columns [#](accounts_import_export#columns)

The window of associating columns is opened using the "Columns" command.

![Selecting Columns](/en/docs/mt5/platform/img/accounts_import_columns.png "Selecting Columns")

The left part contains the available columns and the right one contains the sequence of columns in the imported file. The following commands are present in the window:

-   Insert — add a selected column to the chosen ones;
-   Remove — remove a selected column from the selected ones. The "Login" field is obligatory, it cannot be removed;
-   Up — move an added column up relatively to the others;
-   Down — move an added column down relatively to the others;
-   Reset — return to default column settings.

Columns can also be moved by a double-click with the left mouse button on their names.

The sequence of selected columns is very important, since it is the way of associating them with the fields in the system. To skip one or several columns in the source file, it is necessary to use the special "Skip column" item. For example, if it is put in the third position from the top, then the third column in the imported file will be skipped.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When importing accounts exported from the MetaTrader 4 platform columns are associated automatically.</span></p></td></tr></tbody></table>

[Archive and Backup Bases](/en/docs/mt5/platform/administration/admin_accounts/accounts_archive)

[Import of Accounts from MetaTrader 5](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt)