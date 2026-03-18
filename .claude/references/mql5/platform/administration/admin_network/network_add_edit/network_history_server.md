# History Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Network cluster](/en/docs/mt5/platform/administration/admin_network)[Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)History Server

# History Server

History server is a part of the online trading platform. It is used for:

-   Receiving, filtering and packing price and news data
-   Storing and providing price history as minute bars and ticks
-   Storing and providing the price thread
-   Receiving, checking and distributing Live Updates among MetaTrader 5 servers

Information that comes from [data feeds](/en/docs/mt5/platform/administration/admin_feeds) is passed to the history server and is then resent to [access servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server) and [trade servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server). Settings on the ["Common"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#common), ["Network"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) and ["Service"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#service) tabs are the same for all the server types. The history server setup window contains one more tab - History.

## History [#](network_history_server#history)

![History](/en/docs/mt5/platform/img/network_add_history.png "History")

The following parameters are set up on this tab:

-   Datafeeds timeout — the period of time (in seconds), within which a server is waiting for history data (quotes and news) from a [data feed](/en/docs/mt5/platform/administration/admin_feeds) or a [gateway](/en/docs/mt5/platform/administration/admin_gateways). If no data have been received within this period, the server switches over to another data feed. Minimum timeout is 10 seconds. Changing this setting requires a server restart.
-   Maximum news — the maximum number of news messages that can be stored on the history server.

## Failover [#](network_history_server#backup)

![Failover](/en/docs/mt5/platform/img/history_failover.png "Failover")

Here you can specify the parameters of the [automatic switching to the backup server](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto) in case the current one fails. The necessity to switch to the backup server is defined by the monitoring ("witness") servers. The backup server itself and access servers (with [monitoring mode](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#witness) enabled) act as the monitoring ones. The backup server monitors the availability of the master server in real time mode and checks if it is available for the access servers as well.

-   Switch mode — mode of switching to the backup server:

-   -   Off — automatic switch to the backup server is disabled.
    -   Server is not accessible to most access servers — the number of the monitoring servers unable to access the master server should exceed the ones able to access it at least by one for the switch to occur.
    -   Server is not accessible to all access servers — the master server should be unavailable for all monitoring servers for the switch to occur.
-   Switch timeout — here you can specify the time (in seconds) during which the server should be unavailable for monitoring servers to start switching to the back-up server. Also, after this time period, other platform components start their attempts to connect to the [access points](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) of the current backup server (trying to connect to it as to the main one).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">More detailed information about switching to the backup server can be found in the <a href="/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto" class="topiclink">separate section</a>.</span></p></td></tr></tbody></table>

To complete creation or editing of a history server, press "OK". If you press "Cancel", the window will be closed, while changes won't be saved.

[Trade Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server)

[Access Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server)