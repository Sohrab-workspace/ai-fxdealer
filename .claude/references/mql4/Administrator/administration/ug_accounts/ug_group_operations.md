# Group Operations

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Accounts](/en/docs/mt4/administrator/administration/ug_accounts)Group Operations

# Group Operations

Group Operations make it possible to process a group of accounts selected in the table in the "Accounts" section (not to be confused with accounts groups, such as demoforex, contest, and others), but not individual accounts. To do so, it is necessary to execute the ["Group Operations"](/en/docs/mt4/administrator/administration/ug_accounts#group_operations) command of the context menu. Upon doing so, all available group operations are located in the same window:

![Group Operations](/en/docs/mt4/administrator/img/win_account_group.png "Group Operations")

-   Set Group transfers accounts to another group (demoforex, contest, etc.);
-   Set Leverage sets a new leverage;

-   Enable enables accounts;
-   Disable disables accounts. This option applies to newly connected accounts only, and it does not apply to those already existing. At this point, the icons of the corresponding accounts become gray;
-   Delete deletes accounts. When you delete an account, all its closed and open positions are also deleted.
-   Check balance helps to check balances of accounts. After having pressed this button, the correspondence of the client's balance and the sum of all positions profits/losses of the trader is checked. At that the window of group operations is closed. The difference between the current and the calculated balance will be displayed in Checked column in the list of accounts. In case the balances do not match, the account row will be highlighted with red color. In case there are no errors in the balances all accounts, the following messages is written to the journal: "account balances have been checked. All balances are correct.";
-   Fix balance helps to correct balances. This command calculates the sum of profits of the client's closed positions, and the result is stored as the current deposit. More detailed information is located in the ["Account Restore"](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore) section.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Transferring accounts between groups with different deposit currency is only possible if the accounts have zero balance and credit.</span></li><li class="p_tableatten"><span class="f_tableatten">An account is immediately moved from one group to another one even if there are open orders and positions (server restart is not required) on condition that the groups have the same deposit currency. After transferring, connections of all active terminals with the corresponding logins are terminated in order to apply trading group settings on the client terminal's side.</span></li></ul></td></tr></tbody></table>

[Accounts](/en/docs/mt4/administrator/administration/ug_accounts)

[Account Restore](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore)