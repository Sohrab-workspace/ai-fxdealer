# Accounts Restore

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Accounts](/en/docs/mt4/administrator/administration/ug_accounts)Account Restore

# Accounts Restore

Accounts can be restored completely or partially. What is the difference? The complete restore will apply when all client's data have been lost, including trade operations. The partial restore will apply when only account data has been lost (user's name, address, etc.). If you have deleted an account by mistake, or when you need to perform complete restore for any other reason, you should carry out the following actions:

1.  [restore the account data ("Accounts" section)](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore#account)
2.  [restore the account orders ("Orders" section)](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore#orders)
3.  [check and recalculate the restored account balance](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore#check_fix)

For partial restore, it is necessary to [carry out only the first action](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore#account).

You should use the "Find" window to find the necessary client's account on the given criterion among the results of the data base request. You can activate this window using "Ctrl+F" buttons.

## Account Data Restore [#](ug_accounts_restore#account)

You need [accounts bases](/en/docs/mt4/administrator/administration/ug_backup#archive_backup) for restoring the account data. These bases are created within a certain schedule (indicated in the ["Archive backup every"](/en/docs/mt4/administrator/administration/ug_backup#archive_backup) field of the ["Backups"](/en/docs/mt4/administrator/administration/ug_backup) section). They are stored when any account is being deleted.

![Accounts](/en/docs/mt4/administrator/img/br_accounts_restore.png "Accounts")

[Any base](/en/docs/mt4/administrator/administration/ug_backup#bases) fits for restore if it contains information about the necessary account. First, you should request the base in the ["Accounts"](/en/docs/mt4/administrator/administration/ug_accounts) section. As soon as the desired account is found in bases you will have to execute the "Restore Accounts" context menu command. After that, you can find the restored account in the current base ("Current Account Base" in the "Database" field). Take into consideration, please, the deposit of the account having been restored is still zero. It is not a problem since you can restore your balance, as well, if you know all trade operations.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: It is recommended to request bases created after having deleted accounts (files having the "Deleted" postfix). Requesting all databases can cause unnecessary server load, and, moreover, it is difficult to retrieve necessary information in a large amount of data. It is also recommended not to request all the bases, but to request only backups created approximately at the time of the account deletion.</span></p></td></tr></tbody></table>

## Orders Restore [#](ug_accounts_restore#orders)

The technique of orders restore is rather similar to that of [account restore](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_restore#account), except for that, in most cases, not all, but the latest order base containing trade operations of the selected account is necessary. The fact is that it is the latest base that contains information of all trade operations of the deleted account. Normally, when the account is being restored, it is a base having the "delete" postfix and information about the time of the account deletion. All orders and positions not yet closed at the moment of deletion are stored in it.

![Orders Bases](/en/docs/mt4/administrator/img/br_orders.png "Orders Bases")

To find a desired base, it is necessary to select "More Backups" in the "Database" field of the ["Orders"](/en/docs/mt4/administrator/administration/ug_orders) section:

![More Backups](/en/docs/mt4/administrator/img/more_backups.png "More Backups")

You should check the "Delete backups" field and choose the request range in the "Number of Backups" field. Then you should find the latest base having the "delete" postfix and containing information of operations of the desired account (the time of base creation can help you in doing this). To restore orders it is necessary to execute the "Restore orders" command, having selected all (or just some of) operations. The last task of complete restore is collation of orders and the account, and balance recalculation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Account orders of the account group which did not exist after the server had been started cannot be restored. At this stage, unlike order, the account of a non-existing group can be restored.</span></li><li class="p_tableatten"><span class="f_tableatten">restore of orders for a non-existing account is impossible.</span></li></ul></td></tr></tbody></table>

## Balance Check and Recalculation [#](ug_accounts_restore#check_fix)

After having restored the account and its orders you see that balance is still zero. To correct it, you should execute the ["Group Operations"](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations) context menu command in the ["Accounts"](/en/docs/mt4/administrator/administration/ug_accounts) section. Then you should execute the "Check balance" command. The balance recalculation for the restored trade operations (including initial deposit at the account opening) and collation of the balance and the current balance value will be performed. As a result, there will be either "OK" or "Wrong" written in the "Accounts" section in the "Status" field of the selected account. In the first case, the balance and the result of recalculation on operations coincide. In the second case, values differ, this is a standard situation at complete restoring proves. To complete it for the account, it is necessary to execute the "Fix Balance" command in the group operations window. The result is that there is "OK" written in the "Status" field, and the deposit is equal to the amount resulting from recalculation on operations.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Do not forget to check and recalculate balances when restoring accounts!</span></p></td></tr></tbody></table>

[Group Operations](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations)

[Account Archive](/en/docs/mt4/administrator/administration/ug_accounts/ug_accounts_archive)