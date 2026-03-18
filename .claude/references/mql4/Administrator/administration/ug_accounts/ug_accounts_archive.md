# Account Archive

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_archive

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
                -   [Group Operations](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations)
                -   [Account Restore](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore)
                -   [Account Archive](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_archive)
                -   [Account Redirection](/en/docs/mt4/administrator/administration/ug_accounts/account_allocation_url)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Accounts](/en/docs/mt4/administrator/administration/ug_accounts)Account Archive

# Account Archive

In the course of server operation, a large amount of unused accounts is accumulated: closed accounts, accounts with expended balance, etc. The most of these accounts cannot be deleted since they are necessary, for example, for settlement of disputes with customers. As a result, the databases of the server will grow with the time to significant sizes, which can negatively influence the trade server performancer.

Archives of clients' accounts and orders are intended to solve this problem: every Sunday, during optimization, the server checks all clients' records in the system for two basic parameters - ["inactivity period"](/en/docs/mt4/administrator/administration/ug_groups#inactivity_period) and ["maximum balance"](/en/docs/mt4/administrator/administration/ug_groups#maximum_balance). If there were no connections for the given account within the preset period of time and its balance does not exceed the preset value, this account with all its orders will be moved to the archive. Additional conditions for moving to the archive are absence of open positions and trade activity during the inactivity period (including withdrawals and deposits to the  account and charging agent commission).

Accounts archive represents files that appear as users\_archive\_xxxx.dat and orders\_archive\_xxxx.dat - archive file of accounts and archive file of orders, respectively, where xxxx is the year, for which the archive is created. These files are located in [database directory](/en/docs/mt4/administrator/administration/ug_options#bases_path). Their backups are created once a day when the full backup is performed.

MetaTrader 4 Administrator allows viewing and restoring data from the archive like what is made at [accounts restoring](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore) and [orders restoring](/en/docs/mt4/administrator/administration/ug_orders/ug_orders_restore). It is necessary to select in the the list of available backups databases of "users archive" to work with accounts and "orders archive" to work with orders.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Accounts that belong to demo*, manager and coverage groups are not archived. For deleting old and unused demo accounts the <a href="/en/docs/mt4/administrator/administration/ug_options" class="topiclink">Time of demo</a> options is provided.</span></li><li class="p_tableatten"><span class="f_tableatten">To be archived, an account must not connect to the server using the master password during the period specified in the <a href="/en/docs/mt4/administrator/administration/ug_groups#inactivity_period" class="topiclink">"Inactivity period"</a> field.</span></li><li class="p_tableatten"><span class="f_tableatten">A more detailed information about archiving is available in the article <a href="https://support.metaquotes.net/en/articles/148" target="_blank" class="weblink" title="Article &quot;What To Do with Accounts of Inactive Clients&quot;">"What To Do with Accounts of Inactive Clients"</a>.</span></li></ul></td></tr></tbody></table>

[Account Restore](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore)

[Account Redirection](/en/docs/mt4/administrator/administration/ug_accounts/account_allocation_url)