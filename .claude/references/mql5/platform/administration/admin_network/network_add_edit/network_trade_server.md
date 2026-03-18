# Trading Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
                -   [Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)
                    -   [Trade Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server)
                    -   [History Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server)
                    -   [Access Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server)
                    -   [Backup Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server)
                -   [Hosted Access Servers](/en/docs/mt5/platform/administration/admin_network/hosted_access_server)
                -   [Restarting and Stopping Servers](/en/docs/mt5/platform/administration/admin_network/restart)
                -   [Managing Machines](/en/docs/mt5/platform/administration/admin_network/manage_machines)
                -   [Status](/en/docs/mt5/platform/administration/admin_network/network_status)
                -   [Monitor](/en/docs/mt5/platform/administration/admin_network/network_monitoring)
                -   [Journal](/en/docs/mt5/platform/administration/admin_network/network_journal)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Network cluster](/en/docs/mt5/platform/administration/admin_network)[Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)Trade Server

# Trading Server

There are two types of trade servers in the system - the main one and all other additional ones. Plus to trade server functions, the main server implements system configuration management and management of other servers. The trade server performs the following functions:

-   Storage and management of client records
-   Authentication and authorization of client connections
-   Storage and management of trade records
-   Checking, management and execution of trade requests
-   Management of the internal mailing system

The procedure of setting up the main and other trade servers are similar. Settings on the ["Common"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#common), ["Network"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) and ["Service"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#service) tabs are the same for all server types. The trade server setup window contains four more tabs.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Only one main trade server can exist in a system.</span></li><li class="p_tableatten"><span class="f_tableatten">The installation of the main and additional trade servers is described in the <a href="/en/docs/mt5/platform/platform_installation/installation" class="topiclink">corresponding section</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">There is a number of <a href="/en/docs/mt5/platform/platform_installation/installation#trade" class="topiclink">special features</a> of adding secondary trade servers to the system.</span></li></ul></td></tr></tbody></table>

## Demo [#](network_trade_server#demo)

![Demo](/en/docs/mt5/platform/img/network_add_demo.png "Demo")

This tab is intended for setting up the parameters of working with demo account on the trade server:

-   Demo accounts — type of working with demo accounts. Three variants are available:
    -   Disable — opening new demo accounts via client terminals will be impossible on this server. At that demo accounts can still be opened via administrator and manager terminals and via API.
    -   Prolong from the last login — with each connection to a demo account, its expiration date will be increased by the time specified in "Time of demo" if the account hasn't expired by the time of connection. Only connections using the Master password (not the Investor one) are considered.
    -   With fixed period — demo accounts will be active for the time period specified in "Time of demo";
-   Time of demo — number of days when the demo accounts opened on this server will be active.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If you disable opening new demo accounts (select the option "Disable""), then demo accounts opened earlier will work according to the option "Prolong from the last login".</span></p></td></tr></tbody></table>

Expired demo accounts are deleted every Sunday [during optimization](/en/docs/mt5/platform/administration/admin_network/network_add_edit#optimization). The following entries appear in the trade server journal during deletion:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2017.06.04&nbsp;03:57:02.626&nbsp;ClientBase&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepare&nbsp;demo&nbsp;accounts&nbsp;for&nbsp;clean</span><br><span class="f_CodeExample">2017.06.04&nbsp;03:57:02.626&nbsp;ClientBase&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'1008':&nbsp;demo&nbsp;account&nbsp;added&nbsp;to&nbsp;clean&nbsp;[80&nbsp;days]</span><br><span class="f_CodeExample">2017.06.04&nbsp;03:57:02.626&nbsp;ClientBase&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepare&nbsp;demo&nbsp;accounts&nbsp;for&nbsp;clean&nbsp;finished&nbsp;[1&nbsp;users]</span><br><span class="f_CodeExample">2017.06.04&nbsp;03:57:02.626&nbsp;TradeCenter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;demo&nbsp;clean&nbsp;started&nbsp;[1&nbsp;logins]</span><br><span class="f_CodeExample">2017.06.04&nbsp;03:57:02.626&nbsp;TradeCenter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;demo&nbsp;clean&nbsp;finished</span></p></td></tr></tbody></table>

The deletion of a demo account also deletes its trading operations.

## End of Day [#](network_trade_server#eod)

![End of Day](/en/docs/mt5/platform/img/network_add_eod.png "End of Day")

This tab is intended for setting up the end of day time and the generation of daily and monthly statements.

-   End of day time — time of the trading day end, when the generation of [statements](/en/docs/mt5/platform/administration/admin_groups/groups_settings#reports), charging of [swaps](/en/docs/mt5/platform/administration/admin_groups/groups_settings#swaps), [interest rate](/en/docs/mt5/platform/administration/admin_groups/groups_settings#interest) and [commissions](/en/docs/mt5/platform/administration/admin_groups/groups_comissions) is performed. The execution of the procedures is started on the 59th second of the specified time.
-   End of day schedule — in this field, specify days when the operations connected with the end of a trading day are performed. The generation of reports, charging of swaps, interest rate and commissions is performed on these days only. This option does not affect the generation of monthly statements.
-   Rollover schedule — by default, [rollover calculations](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps) are not performed on Saturday and Sunday (even if these days are specified in the "End of day" parameter). When work days are shifted to weekend, you may adjust the operation of the trading platform accordingly. For example, if a work day is shifted from Monday to Saturday, you can enable rollover calculation on Saturday. However, note that traders' rollover will be calculated eight times for that week, instead of seven: five simple swaps and one three-day swap. To compensate for the extra rollover, explicitly disable rollover calculation on Monday. Otherwise, rollover will be charged even if you set up a [holiday](/en/docs/mt5/platform/administration/admin_holidays) on that day and disable trading in the [server schedule](/en/docs/mt5/platform/administration/admin_time). On the next day (Tuesday), rollover settings should be reset to the original state.  
    In addition to enabling rollover calculation, make sure to enable "End of Day" for that day. Otherwise, rollover will not be charged.
-   Daily statements — time when daily statements are generated: at the end of a trade day (before swaps, interest rate and commissions are charged) or at the beginning of a trade day (after swaps, interest rate and commissions are charged).
-   Last end of day — the date and time of the last end of day. When generating the last daily statement, the server uses trading data beginning from the specified date.
-   Previous end of day — the date and time of the previous end of day. Daily statements include a client's trading status for the previous trading day. The server uses the specified date to calculate it.
-   Monthly statements — month closing date on which the monthly reports should be generated: the last day of the current month of the first day of the next month.
-   Last end of month — the date and time of the last end of month. When generating the last monthly statement, the server uses trading data beginning from the specified date.
-   Previous end of month — the date and time of the previous end of month. Daily statements include a client's trading status for the previous trading month. The server uses the specified date to calculate it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is strongly not recommended to change the dates of the last and the previous ends of day and month. Edit them only in case of emergency (for example, if the server emergency shutdown during the generation of daily/monthly statements has led to incorrect dates).</span></p></td></tr></tbody></table>

### The order of end-of-day/month service operations

During the end-of-day, clients and managers are forbidden to perform any trading operations, including balance operations. On any attempt, the server will return the "Market closed" error.

The order of service operations depends on the report generation mode: at the end or at the beginning of the day. The performed actions also depend on whether the end of the trading day (as determined by the "End of day" parameter) and end of month (as determined by the actual end of month) fall on this day.

When generating reports at the end of the day:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Condition</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Operation</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1. Beginning of the 'end of day' at the time specified in the "<a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#end_of_day" class="topiclink">End of day</a>" parameter under server settings</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">2. Beginning of the 'end of month' at the time specified in the "<a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#end_of_day" class="topiclink">End of day</a>" parameter under server settings</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">3. Beginning of operations for each group:</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">4. Calculation and settlement of commissions (including agent commission) with the "<a href="/en/docs/mt5/platform/administration/admin_groups/groups_comissions#charge" class="topiclink">Daily</a>" calculation mode</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">5. Calculation and settlement of commissions (including agent commission) with the "<a href="/en/docs/mt5/platform/administration/admin_groups/groups_comissions#charge" class="topiclink">Monthly</a>" calculation mode</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">6. Calculation of interest on available funds and saving them in the client record</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">7. Calculation and of the accumulated interest on available funds and depositing it to the balance</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">8. Generation of daily reports</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">9. Updating of the previous day balances (used in daily/monthly reports)</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">10. Generation of monthly reports</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">11. Update of previous month balances (used in daily/monthly reports)</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">12. Calculation of swaps</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">13. End of operations for each group</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">14. End of "end of day"</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">15. End of "end of month"</span></p></td></tr></tbody></table>

When generating reports at the beginning of the day:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Condition</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Operation</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">1. Beginning of the 'end of day' at the time specified in the "<a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#end_of_day" class="topiclink">End of day</a>" parameter under server settings</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">2. Beginning of the 'end of month' at the time specified in the "<a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#end_of_day" class="topiclink">End of day</a>" parameter under server settings</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">3. Beginning of operations for each group:</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">4. Calculation and settlement of commissions (including agent commission) with the "<a href="/en/docs/mt5/platform/administration/admin_groups/groups_comissions#charge" class="topiclink">Daily</a>" calculation mode</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">5. Calculation and settlement of commissions (including agent commission) with the "<a href="/en/docs/mt5/platform/administration/admin_groups/groups_comissions#charge" class="topiclink">Monthly</a>" calculation mode</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">6. Calculation of interest on available funds and saving them in the client record</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">7. Calculation and of the accumulated interest on available funds and depositing it to the balance</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">8. Calculation of swaps</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">9. Generation of daily reports</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">10. Updating of the previous day balances (used in daily/monthly reports)</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">11. Generation of monthly reports</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">12. Update of previous month balances (used in daily/monthly reports)</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">13. End of operations for each group</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the trading day</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">14. End of "end of day"</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable">If there is end of the month</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">15. End of "end of month"</span></p></td></tr></tbody></table>

## Accounts [#](network_trade_server#accounts)

![Accounts Range](/en/docs/mt5/platform/img/network_add_accounts_range.png "Accounts Range")

Here you set up the range from which logins will be generated at the opening of new accounts. In order to add a range, press "Add". After that a new line will appear in the window. In "From" column, specify the first account that will be serviced in this range, and specify the last one in "To". In order to modify an already existing range, double click on the necessary field or select it and press "Edit". To delete a selected range, press "Delete".

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Account ranges on different trade servers must not coincide. We strongly recommend to strictly plan the distribution of accounts between servers.</span></li><li class="p_tableatten"><span class="f_tableatten">The range indication is obligatory. Otherwise, it will be impossible to create accounts on &nbsp;the server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The last value of the range must be greater by 1 000 than the highest number of account already allocated on the server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The ranges should not be changed during trading time. After changing them, restart the platform.</span></li></ul></td></tr></tbody></table>

## Orders [#](network_trade_server#orders)

![Orders Range](/en/docs/mt5/platform/img/network_add_orders_range.png "Orders Range")

Here you should set up the range, from which numbers of orders set on this trade server will be allocated. In order to add a range, press "Add". After that, a new line will appear in the window. In "From" column, specify the first order that will be serviced in this range, and specify the last one in "To". In order to modify an already existing range, double click on the necessary field or select it and press "Edit". To delete a selected range, press "Delete".

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Orders ranges on different trade servers must not coincide. We strongly recommend to strictly plan the distribution of orders between servers.</span></li><li class="p_tableatten"><span class="f_tableatten">The range indication is obligatory. Otherwise, it will be impossible to set orders on the server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The last value of the range must be greater by 1 000 than the highest number of order already placed on the server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The range or orders is also used for assigning tickets to <a href="/en/docs/mt5/platform/administration/admin_positions" class="topiclink">positions</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The ranges should not be be changed during trading time. After changing them, restart the platform.</span></li></ul></td></tr></tbody></table>

## Deals [#](network_trade_server#deals)

![Deals Range](/en/docs/mt5/platform/img/network_add_deals_range.png "Deals Range")

Here you should set up the range, from which numbers of deals executed on this trade server will be set. In order to add a range, press "Add". After that, a new line will appear in the window.  In "From" column, specify the first deal that will be serviced in this range, and specify the last one in "To". In order to modify an already existing range, double click on the necessary field or select it and press "Edit". To delete a selected range, press "Delete".

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Deals ranges on different trade servers must not coincide. We strongly recommend to strictly plan the distribution of orders between servers.</span></li><li class="p_tableatten"><span class="f_tableatten">The deals range indication is obligatory. Otherwise, it will be impossible to set orders on the server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The last value of the range must be greater by 1 000 than the highest number of deal already performed on the server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The ranges should not be be changed during trading time. After changing them, restart the platform.</span></li></ul></td></tr></tbody></table>

## Failover [#](network_trade_server#backup)

![Failover](/en/docs/mt5/platform/img/trade_backup_settings.png "Failover")

Here you can specify the parameters of the [automatic switching to the backup server](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto) in case the current one fails. The necessity to switch to the backup server is defined by the monitoring ("witness") servers. The backup server itself and access servers (with [monitoring mode](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#witness) enabled) act as the monitoring ones. The backup server monitors the availability of the master server in real time mode and checks if it is available for the access servers as well.

-   Switch mode — mode of switching to the backup server:
    -   Off — automatic switch to the backup server is disabled.
    -   Server is not accessible to most access servers — the number of the monitoring servers unable to access the master server should exceed the ones able to access it at least by one for the switch to occur.
    -   Server is not accessible to all access servers — the master server should be unavailable for all monitoring servers for the switch to occur.
-   Switch timeout — here you can specify the time (in seconds) during which the server should be unavailable for monitoring servers to start switching to the back-up server. Also, after this time period, other platform components start their attempts to connect to the [access points](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) of the current backup server (trying to connect to it as to the main one).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">More detailed information about switching to the backup server can be found in the <a href="/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto" class="topiclink">separate section</a>.</span></p></td></tr></tbody></table>

To complete creating or editing a trade server press "OK". If you press "Cancel", the window will be closed, while settings will not be saved.

[Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)

[History Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server)