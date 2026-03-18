# Status

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_status

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
                -   [Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Network cluster](/en/docs/mt5/platform/administration/admin_network)Status

# Status

The section displays important component operation characteristics: hardware load, database sizes, network speed and much more. These metrics should be monitored closely: hardware should always have a power reserve to ensure the maximum platform performance.

![Status](/en/docs/mt5/platform/img/status.png "Status")

## Basic Information

Basic information about the selected server is shown at the top of the window:

-   Version — server version, build number and its date.
-   Last boost — last system boot time. The server [restart](/en/docs/mt5/platform/administration/admin_network/restart) button is located in the right part.
-   Operating system — name of the operating system. The minimum recommended system is Windows Server 2016 Standard x64.
-   Processor — CPU type and its clock rate. The minimum recommended CPU type is Intel i7 4xxx 4 quad-core and above.
-   Memory — free RAM amount/total RAM.
-   Disk — free hard drive space in gigabytes. Make sure there is always enough free disk space.

## Databases

This block features information about databases on the selected server. It is only available for trading servers.

-   Groups — the total number of [groups](/en/docs/mt5/platform/administration/admin_groups) on the server.
-   Accounts — the total number of [accounts](/en/docs/mt5/platform/administration/admin_accounts) on the server.
-   Real accounts — the total number of real clients on the server, as well as the limitation on the number of clients according to the license (if any). Real accounts refer to the client records that are not included in demo\*, manager\*, preliminary\* and contest\* [groups](/en/docs/mt5/platform/administration/admin_groups/group_types). The statistics only include [enable accounts](/en/docs/mt5/platform/administration/admin_accounts/account_edit#enable) from which [trading is allowed](/en/docs/mt5/platform/administration/admin_accounts/account_edit#trading).
-   Positions — the number of [positions](/en/docs/mt5/platform/administration/admin_positions) on the trade server.
-   Orders — the number of active [orders](/en/docs/mt5/platform/administration/admin_orders) and history orders on the selected server.
-   Deals — the total number of [deals](/en/docs/mt5/platform/administration/admin_deals) executed on the selected server.

## Maximum load

This block shows the maximum server load registered during the current session:

-   Connections — statistics on the total amount of all standard operating terminal connections and temporary connections made for executing trades, downloading history or news. In the quiet market, this parameter allows determining the number of online users. It is shown for the cluster and for individual servers.

-   On access servers, connections show the number of client connections.
-   On trade server, the figure means virtual connections (clients actually connect via access servers).
-   On history servers, the metric shows connections of other components of the cluster.
-   Active sockets — the total number of TCP endpoints (with a specific IP address and port number) connected throughout the operating system. This also takes into account half-open connections when there is no connection, but the socket is still closed by the operating system.
-   Network load — total incoming and outgoing traffic, in Mbit/s. The load of the [selected network interface](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network_adapter) is measured in terms of the incoming and outgoing traffic (average value per minute). Takes into account the traffic of all programs that run on the server computer. Unexpected load spikes can easily point to DDoS attacks.
-   CPU load — total CPU load in percent. This parameter affects on how fast users and their trade operations are serviced. If the processor load regularly exceeds 50% in the middle of a work day, it is time to think of the computer upgrade. Over 85% load is critical. If the processor load is 100%, it means that the processing power is not enough for processing of tasks. However, rare spike loads are no reason to worry.
-   Memory — free RAM amount/total RAM. Availability of a large amount of free memory is extremely important for a server. This enables you to serve more users currently connected, and handle large databases. If the available memory becomes less than 100MB, the graph is colored in red.

To view the statistics in dynamics, use [monitoring](/en/docs/mt5/platform/administration/admin_network/network_monitoring) section.

## Ping

This section shows network delays between the selected server and all other components of the cluster.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Server operation statistics (network load, CPU and others) are updated during <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit#optimization" class="topiclink">optimization</a>.</span></p></td></tr></tbody></table>

## Backup last time [#](network_status#last_backup)

This section is only displayed for backup servers. It indicates the last time the backups were made.

-   Startup — at startup the backup server creates a [file copy](/en/docs/mt5/platform/components/backup_server/backup_server_features#file) of its databases which were synchronized with the main trade server in real time. This happens before the start of synchronization with the main server in case its databases are already damaged. This allows the rolling back to the previous state using the file copy.
-   Full — the time when the [file copies](/en/docs/mt5/platform/components/backup_server/backup_server_features#file) of all databases were created.
-   Archive — the time when [additional file copies](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#archive_backup_period) were created.
-   Databases synchronization — the time of the last backup of [non-core data](/en/docs/mt5/platform/components/backup_server/backup_server_features) (the initial synchronization at server startup or periodic synchronization during operation).
-   SQL synchronization — time of the last full synchronization of databases and platform configurations with the [SQL database.](/en/docs/mt5/platform/components/backup_server/sql_export). It is launched when a backup server is started or after connection to the SQL database or to the trading server is lost. After synchronization, the SQL database is updated in real time in accordance with the transactions of changes in the platform databases.

[Managing Machines](/en/docs/mt5/platform/administration/admin_network/manage_machines)

[Monitor](/en/docs/mt5/platform/administration/admin_network/network_monitoring)