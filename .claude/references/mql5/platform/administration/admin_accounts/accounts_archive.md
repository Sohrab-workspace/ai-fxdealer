# Archive and Backup Bases

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_archive

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Accounts](/en/docs/mt5/platform/administration/admin_accounts)Archive and Backup Bases

# Archive and Backup Bases

During the operation of a trade server a a lot of unused accounts are accumulated in the system. Most of them cannot be deleted, because they are necessary, for example, for solving disputes with clients. The archive database allows:

-   To store the accounts that are not necessary to be maintained at the moment (for example, inactive accounts with insignificant deposits where trading is impossible);
-   To quickly restore accounts from the archive for resuming the work with them;
-   To decrease the server load for servicing the accounts, because the request to the archive database are not performed while working.

The archive databases are stored on the [trade server](/en/docs/mt5/platform/components/trade_server), in separate files by years.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The archive of accounts does not affect trading operations. Orders, trades and positions are not deleted from current databases.</span></p></td></tr></tbody></table>

## Working with Accounts Archive

-   Moving account to the archive  
    To move an account to archive, select it in the [Accounts](/en/docs/mt5/platform/administration/admin_accounts) section and click "![Move to archive](/en/docs/mt5/platform/img/move_to_archive_button.png "Move to archive") Move to archive" in the [context menu](/en/docs/mt5/platform/administration/admin_accounts#to_archive).
-   Restoring account from the archive  
    To restore an account from the archive, navigate to the [Account](/en/docs/mt5/platform/administration/admin_accounts#request) section, select the archive database, and request an account from the database by its number. Once you have found an account, select it in the list and click "![Restore](/en/docs/mt5/platform/img/restore_icon.png "Restore") Restore" in the [context menu](/en/docs/mt5/platform/administration/admin_accounts#context). After that, perform [balance check and correction](/en/docs/mt5/platform/administration/admin_accounts/account_balance_check) for the account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Restored accounts are not deleted from the archive.</span></li><li class="p_tableatten"><span class="f_tableatten">If an account is moved to archive again after it has been restored, new information about it will replace the one that is stored in the archive.</span></li></ul></td></tr></tbody></table>

## Backup Bases of Accounts

[Backup copies](/en/docs/mt5/platform/components/backup_server/backup_server_features#file) are copies of the account database at certain points in time. They are created daily on the [backup server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#enable_backups). To get the list of available backup copies, select "More backups..." and specify a time period:

![Requesting backup copies](/en/docs/mt5/platform/img/accounts_backup_request.png "Requesting backup copies")

As soon as the period is specified, additional items with the dates of creation of backup copies will appear in the list of database selection. After selecting the necessary database, [request](/en/docs/mt5/platform/administration/admin_accounts#request) accounts from it. Using the "![Restore](/en/docs/mt5/platform/img/restore_icon.png "Restore") Restore" command of the context menu, any account can be easily returned back to the current database in the same state as when the backup copy was created.

[Preliminary Accounts](/en/docs/mt5/platform/administration/admin_accounts/preliminary_accounts)

[Import of Accounts from File](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_export)