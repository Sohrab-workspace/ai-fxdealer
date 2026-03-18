# Access Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Network cluster](/en/docs/mt5/platform/administration/admin_network)[Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)Access Server

# Access Server

Access servers are used as intermediate links between clients and a trade server. The access server performs the following functions:

-   Processing of incoming client connections;
-   Packaging authorization requests and passing them to a trade server;
-   Checking activity of client connections, protecting the trade server from attacks and overloading;
-   Saving history data, depth of market and news, providing them to clients and thus reducing the load to the history server;
-   Providing client terminals with LiveUpdate.

Settings on the ["Common"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#common), ["Network"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) and ["Service"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#service) tabs are the same for all the server types. The access server setup window contains three more tabs.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To quickly add an access point in a high trading activity region, <a href="/en/docs/mt5/platform/administration/admin_network/hosted_access_server" class="topiclink">order Access Server Hosting from MetaQuotes</a> directly via the Administrator terminal. The new point will become available within 30 seconds.</span></p></td></tr></tbody></table>

## Access [#](network_access_server#access)

![Access](/en/docs/mt5/platform/img/network_add_access.png "Access")

The following parameters are set up on the "Access" tab:

-   Priority is the basic priority of the access server. A server can have basic priority from 0 to 15. The access server preference for client connections is calculated based on the current priority and quality of connection to the server. The current priority depends on the basic priority and the number of current connections to the server. The lower the priority number is, the higher its preference for client connections is. Find more details about the calculation of the current priority in a [separate section](/en/docs/mt5/platform/components/access_server/access_server_priority).
-   Enable antiflood control — enable [defense from DoS attacks](/en/docs/mt5/platform/components/access_server/access_server_antiflood). The server analyses the network activity of all clients in real time mode by selecting connections with most frequent operations that come from one IP address. If such an attack is detected, the attacking IP address is moved to a temporary list of banned addresses. At a repeated attack, the ban period is extended. This mechanism allows to easily block attack attempts. The control has the following parameters:

-   Connections — the maximum number of server connections from one IP address within a certain time period, after which the address will be temporarily banned.
-   Errors — number of unsuccessful connection attempts, after which the address will be temporarily banned.
-   Maximum news — maximum number of news messages that are stored on the access server.
-   Use this server for monitoring the cluster and failover — when enabled, the backup servers use this server to check the availability of the main (backed up) ones. This is used to automatically switch to the backup server if the main one fails. More detailed information can be found in the [appropriate section](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Enabling of the antiflood control is required.</span></li><li class="p_tableatten"><span class="f_tableatten">The antiflood mechanism functions independently on each access server. Each server tracks its own connection and error counters and applies the appropriate restrictions when required.</span></li><li class="p_tableatten"><span class="f_tableatten">If you need to create a virtual, temporarily not existing servers, use the "Idle" priority. Such servers are standby ones. They are connected to only if all other servers do not operate.</span></li></ul></td></tr></tbody></table>

## Permissions [#](network_access_server#permissions)

![Permissions](/en/docs/mt5/platform/img/network_add_permissions.png "Permissions")

Here you can set up types of connections allowed for the access server:

-   Client terminals — desktop, mobile and web.
-   Terminals operating on a [built-in VPS](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#vps), as well as Ultency servers.
-   Manager terminals.
-   Administrator terminals.
-   Applications developed using [Manager API](https://support.metaquotes.net/ru/docs/mt5/api/managerapi).
-   Web Terminal. When the Web Terminal is disabled, all web functionality (HTTPS) on the access server is deactivated. In particular, connections via the Web API will no longer be possible.
-   Services operating through [Web API](https://support.metaquotes.net/ru/docs/mt5/api/webapi).

### Creating fast dedicated access points for built-in VPS [#](network_access_server#vps)

You can create fast, dedicated access points to connect [VPS terminals](/en/docs/mt5/platform/administration/integration/integration_vps). This will significantly improve the high frequency trading capabilities on your server. By using a widespread distributed network and automatically identifying the server closest to the broker, VPS terminals achieve exceptionally low latency when connecting. Setting up a dedicated access server for these terminals will further enhance speed and enable traders to engage in true high-frequency trading.

To set up a dedicated access point:

-   Restrict standard client connections, allowing connections only for VPS / Ultency.
-   Enable the "Use as a dedicated access point only for MetaTrader 5 VPS / Ultency" option. This prevents the access server from appearing to client terminals, while physical connections remain technically possible. As a result, standard client terminals will not attempt to connect since they will not know the server address.

### Additional security for hosted servers

[Hosting access servers](/en/docs/mt5/platform/administration/admin_network/hosted_access_server) is entirely secure. All transmitted data is encrypted, and the access server does not store account databases, passwords, or any other trading account information. For added protection, you can enable the "Hide login details from logs" option. This prevents account numbers from being displayed in the access server [log](/en/docs/mt5/platform/administration/admin_network/network_journal). If necessary, this option can be temporarily disabled for troubleshooting, but we recommend keeping it enabled for maximum security.

## Servers [#](network_access_server#servers)

![Servers](/en/docs/mt5/platform/img/network_add_servers.png "Servers")

On this tab you should select [trade servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server) to connect to through the selected access server. To allow connections to certain servers, tick ![Allow](/en/docs/mt5/platform/img/access_permit_icon.png "Allow") near them. You can select all or select none of servers using the corresponding buttons.

[History Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server)

[Backup Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server)