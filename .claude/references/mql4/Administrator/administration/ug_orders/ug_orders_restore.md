# Order Deleting and Restore

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_orders/ug_orders_restore

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
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
                -   [Order Deleting and Restore](/en/docs/mt4/administrator/administration/ug_orders/ug_orders_restore)
                -   [Order Database Optimization](/en/docs/mt4/administrator/administration/ug_orders/order_base_optimization)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Orders](/en/docs/mt4/administrator/administration/ug_orders)Order Deleting and Restore

# Order Deleting and Restore

If it is necessary to delete one or more orders, it is not enough to execute the "Delete" context menu command in the ["Orders"](/en/docs/mt4/administrator/administration/ug_orders) section. After having used it, select accounts in the ["Accounts"](/en/docs/mt4/administrator/administration/ug_accounts) section orders of which have been deleted, and execute the ["Group Operations"](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations) context menu command. Press the "Check Balance" button in the window which appears. The recalculation of balances on the rest of trade operations will now be performed and will be compared to the current value.

As a result, either "OK" or "Wrong" will be written in the "Status" field of the selected accounts in the "Accounts" section. In the first case, the balance and the result of recalculation on the operation coincide with each other. It means no other action should be taken. In the second, more probable case, the values will differ from each other. To complete the order deleting, it is necessary to execute the "Fix Balance" command in the Group Operations window. After that, "OK" will appear in the "Status" fields, and deposits will equal in the sum recalculated for operations. Only after having recalculated and compared the balances, the operation of order deleting can be considered as completed.

## Order Restore

To restore one or more orders being deleted for any reasons, it is necessary to perform the following actions:

-   [restore the deleted orders](/en/docs/mt4/administrator/administration/ug_orders/ug_orders_restore#orders)
-   [check and recalculate balances of appropriate accounts](/en/docs/mt4/administrator/administration/ug_orders/ug_orders_restore#check_fix)

### Order Restore [#](ug_orders_restore#orders)

To restore, you need backups of the order databases. These bases are created with a certain schedule (indicated in the ["Archive Backup Every"](/en/docs/mt4/administrator/administration/ug_backup#archive_backup) field of the ["Backups"](/en/docs/mt4/administrator/administration/ug_backup#archive_backup) section), and also when fifteen or more orders are deleted at the same time.

![Orders](/en/docs/mt4/administrator/img/br_orders.png "Orders")

It is necessary to request all accessible databases ("Database — More Backups") from the ["Orders"](/en/docs/mt4/administrator/administration/ug_orders) section.

![More Backups](/en/docs/mt4/administrator/img/more_backups.png "More Backups")

It is recommended to request a base having the "Delete" postfix ("More Backups", and further "Delete backups" are bases created when accounts are deleted), however, if it does not exist, it is possible to use cyclic backups. Then, having selected the desired accounts, it is necessary to execute the "Restore Accounts" context menu command. After that, the restored accounts will appear in the current base, but deposits of accounts do not consider the restored orders yet.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: If you deleted less than fifteen orders, bases having the "Delete" postfix and containing all orders will not be created, and the preceding schedule created backup may not contain all the deleted orders. This can happen if you deleted orders opened after you had stored the latest schedule created backup to the disc. In this case, it is impossible to restore orders using the cyclic backups.</span></p></td></tr></tbody></table>

### Balance Checking and Recalculating [#](ug_orders_restore#check_fix)

After the orders have been restored, the balances of the accounts and the results of the sum of trade operations are not equal. To correct this, it is necessary to execute the ["Group Operations"](/en/docs/mt4/administrator/administration/ug_accounts/ug_group_operations) context menu command in the ["Accounts"](/en/docs/mt4/administrator/administration/ug_accounts) section. Then, the "Check Balance" command should be executed. At this point, the balance for all trade operations (including the restored ones) is recalculated and compared to the current balance value. As a result, either "OK" or "Wrong" will be written in the "Status" fields of the selected accounts in the "Accounts" section. In the first case, the balance and the result of recalculation on the operation coincide with each other. It means no other actions should be taken. In the second, more probable case, the values will differ from each other. To complete the order restore, it is necessary to execute the "Fix Balance" command in the Group Operations window. After that, "OK" will appear in the "Status" fields, and deposits will equal in the sum recalculated for operations. Only after having recalculated and compared the balances, the operation of order deleting can be considered as completed.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: When deleting or restoring orders do not forget to check and recalculate balances of the accounts!</span></p></td></tr></tbody></table>

[Orders](/en/docs/mt4/administrator/administration/ug_orders)

[Order Database Optimization](/en/docs/mt4/administrator/administration/ug_orders/order_base_optimization)