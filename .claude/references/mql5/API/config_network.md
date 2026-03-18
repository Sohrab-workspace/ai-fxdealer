# Network Configuration

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_network

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
            -   [Common](/en/docs/mt5/api/config_common)
            -   [Network](/en/docs/mt5/api/config_network)
                -   [IMTConServer](/en/docs/mt5/api/config_network/imtconserver)
                -   [IMTConServerTrade](/en/docs/mt5/api/config_network/imtconservertrade)
                -   [IMTConServerHistory](/en/docs/mt5/api/config_network/imtconserverhistory)
                -   [IMTConServerBackup](/en/docs/mt5/api/config_network/imtconserverbackup)
                -   [IMTConBackupFolder](/en/docs/mt5/api/config_network/imtconbackupfolder)
                -   [IMTConServerAccess](/en/docs/mt5/api/config_network/imtconserveraccess)
                -   [IMTConServerAntiDDoS](/en/docs/mt5/api/config_network/imtconserverantiddos)
                -   [IMTConClusterState](/en/docs/mt5/api/config_network/imtconclusterstate)
                -   [IMTConServerRange](/en/docs/mt5/api/config_network/imtconserverrange)
                -   [IMTConServerAddressRange](/en/docs/mt5/api/config_network/imtconserveraddressrange)
                -   [IMTConServerSink](/en/docs/mt5/api/config_network/imtconserversink)
            -   [Plugins](/en/docs/mt5/api/config_plugins)
            -   [Data Feeds](/en/docs/mt5/api/config_datafeeds)
            -   [Time](/en/docs/mt5/api/config_time)
            -   [Holidays](/en/docs/mt5/api/config_holiday)
            -   [Firewall](/en/docs/mt5/api/config_firewall)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
            -   [Floating Margin](/en/docs/mt5/api/config_leverage)
            -   [Managers](/en/docs/mt5/api/config_manager)
            -   [History Synchronization](/en/docs/mt5/api/config_historysync)
            -   [Gateways](/en/docs/mt5/api/config_gateway)
            -   [Routing](/en/docs/mt5/api/config_route)
            -   [Reports](/en/docs/mt5/api/config_report)
            -   [Mail Servers](/en/docs/mt5/api/config_email)
            -   [Messengers](/en/docs/mt5/api/config_messenger)
            -   [Automations](/en/docs/mt5/api/config_automation)
            -   [VPS](/en/docs/mt5/api/config_vps)
            -   [KYC](/en/docs/mt5/api/config_kyc)
            -   [Subscriptions](/en/docs/mt5/api/config_subscription)
            -   [Funds and ETF](/en/docs/mt5/api/config_funds)
            -   [Additional Parameters](/en/docs/mt5/api/config_param)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Network

# Network Configuration

Network configuration means the management of settings of the the server components of the platform: main and ordinary trade servers, history and access servers, backup servers.

The following interfaces of the configuration of platform components are available:

-   [IMTConServer](/en/docs/mt5/api/config_network#imtconserver)
-   [IMTConServerTrade](/en/docs/mt5/api/config_network#imtconservertrade)
-   [IMTConServerHistory](/en/docs/mt5/api/config_network#imtconserverhistory)
-   [IMTConServerBackup](/en/docs/mt5/api/config_network#imtconserverbackup)
-   [IMTConBackupFolder](/en/docs/mt5/api/config_network/imtconbackupfolder)
-   [IMTConServerAccess](/en/docs/mt5/api/config_network#imtconserveraccess)
-   [IMTConServerAntiDDoS](/en/docs/mt5/api/config_network/imtconserverantiddos)
-   [IMTConClusterState](/en/docs/mt5/api/config_network/imtconclusterstate)
-   [IMTConServerRange](/en/docs/mt5/api/config_network#imtconserverrange)
-   [IMTConServerAddressRange](/en/docs/mt5/api/config_network/imtconserveraddressrange)
-   [IMTConServerSink](/en/docs/mt5/api/config_network#imtconsserversink)

The below figure shows different elements of configuration of the platform components in the MetaTrader 5 Administrator, to help you understand the purpose of the interfaces:

![The network configuration in MetaTrader 5 Administrator](/en/docs/mt5/api/img/network_configuration.png "The network configuration in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [Server Type](/en/docs/mt5/api/config_network/imtconserver/imtconserver_type).
2.  [Server Name](/en/docs/mt5/api/config_network/imtconserver/imtconserver_name).
3.  [Server Address](/en/docs/mt5/api/config_network/imtconserver/imtconserver_address).
4.  [Server ID](/en/docs/mt5/api/config_network/imtconserver/imtconserver_id).
5.  [Base priority of the Access Server](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_priority).
6.  [The current priority of the Access Server](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_prioritycurrent).
7.  [The current level of CPU](/en/docs/mt5/api/config_network/imtconserver/imtconserver_cputotal).
8.  [The list of all server configurations](/en/docs/mt5/api/config_network/imtconserver).

The detailed examples of configurations of the platform components are shown below.

## IMTConServerRange [#](config_network#imtconserverrange)

The [IMTConServerRange](/en/docs/mt5/api/config_network/imtconserverrange) interface is used to set the ranges of accounts, orders and deals on trade servers.

![Set the range of a trade server in MetaTrader 5 Administrator](/en/docs/mt5/api/img/network_range.png "Set the range of a trade server in MetaTrader 5 Administrator")

The figure shows a tab of configuration of accounts range of a trade server in MetaTrader 5 Administrator:

1.  [Beginning of the range](/en/docs/mt5/api/config_network/imtconserverrange/imtconserverrange_from).
2.  [End of the range](/en/docs/mt5/api/config_network/imtconserverrange/imtconserverrange_to).

## IMTConServerTrade [#](config_network#imtconservertrade)

The [IMTConServerTrade](/en/docs/mt5/api/config_network/imtconservertrade) interface contains methods for managing settings that are specific to Trade Servers.

![Set a trade server in MetaTrader 5 Administrator](/en/docs/mt5/api/img/network_trade.png "Set a trade server in MetaTrader 5 Administrator")

The figure shows the following elements of trade server setup in MetaTrader 5 Administrator:

1.  [Mode of operation with demo accounts](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_demomode).
2.  [Time of the day end](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_overnighttime).
3.  [Days of operations associated with the end of the trading day](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_overnightdays).
4.  [Daily report generation mode](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_overnightmode).
5.  [Monthly report generation mode](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_overmonthmode).
6.  [Setting the range of accounts](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_loginsrangeadd).
7.  [Setting the range of orders](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_ordersrangeadd).
8.  [Setting the range of deals](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_dealsrangeadd).

## IMTConServerHistory [#](config_network#imtconserverhistory)

The [IMTConServerHistory](/en/docs/mt5/api/config_network/imtconserverhistory) interface contains methods for managing settings that are specific to History Servers.

![Setting a History Server in MetaTrader 5 Administrator](/en/docs/mt5/api/img/network_history.png "Setting a History Server in MetaTrader 5 Administrator")

The figure shows the following elements of History Server setup in MetaTrader 5 Administrator:

1.  [Data feed timeouts](/en/docs/mt5/api/config_network/imtconserverhistory/imtconserverhistory_datafeedstimeout).
2.  [Maximum number of news](/en/docs/mt5/api/config_network/imtconserverhistory/imtconserverhistory_newsmax).

## IMTConServerBackup [#](config_network#imtconserverbackup)

The [IMTConServerBackup](/en/docs/mt5/api/config_network/imtconserverbackup) interface contains methods for managing settings that are specific to Backup Servers.

![Setting a Backup Server in MetaTrader 5 Administrator](/en/docs/mt5/api/img/network_backup.png "Setting a Backup Server in MetaTrader 5 Administrator")

The figure shows the following elements of Backup Server setup in MetaTrader 5 Administrator:

1.  [A server to back up](/en/docs/mt5/api/config_network/imtconserverbackup/imtconserverbackup_masterserver).
2.  [The backup path](/en/docs/mt5/api/config_network/imtconserverbackup/imtconserverbackup_backuppath).
3.  [The frequency of backup](/en/docs/mt5/api/config_network/imtconserverbackup/imtconserverbackup_backupperiod).
4.  [A period to keep backups](/en/docs/mt5/api/config_network/imtconserverbackup/imtconserverbackup_backupttl).
5.  [Time to create full backups](/en/docs/mt5/api/config_network/imtconserverbackup/imtconserverbackup_backupfulltime).

## IMTConServerAccess [#](config_network#imtconserveraccess)

The [IMTConServerAccess](/en/docs/mt5/api/config_network/imtconserveraccess) interface contains methods for managing settings that are specific to Access Servers.

![Setting an Access Server in MetaTrader 5 Administrator](/en/docs/mt5/api/img/network_access.png "Setting an Access Server in MetaTrader 5 Administrator")

The figure shows the following elements of Access Server setup in MetaTrader 5 Administrator:

1.  [Server priority](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_priority).
2.  [Enable/disable antiflood control](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_antifloodenabled).
3.  [Number of connections](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_antifloodconnects).
4.  [Maximum number of news](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_newsmax).
5.  [Number of incorrect connections](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_antiflooderrors).
6.  [Setup of allowed types of connections](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_accessflags).
7.  [Setup of serviced Trade Servers](/en/docs/mt5/api/config_network/imtconserveraccess/imtconserveraccess_serversadd).

## IMTConServer [#](config_network#imtconserver)

The [IMTConServer](/en/docs/mt5/api/config_network/imtconserver) interface contains methods for managing settings that are common to all types of servers.

![Common parameters of servers in MetaTrader 5 Administrator](/en/docs/mt5/api/img/network_common.png "Common parameters of servers in MetaTrader 5 Administrator")

The figure shows the following server parameters in MetaTrader 5 Administrator:

1.  [Version](/en/docs/mt5/api/config_network/imtconserver/imtconserver_version), [build](/en/docs/mt5/api/config_network/imtconserver/imtconserver_build) and [build date](/en/docs/mt5/api/config_network/imtconserver/imtconserver_builddate) of the server.
2.  [Time of the last server boot](/en/docs/mt5/api/config_network/imtconserver/imtconserver_lastboottime).
3.  [Version of the operating system](/en/docs/mt5/api/config_network/imtconserver/imtconserver_os).
4.  [Processor type](/en/docs/mt5/api/config_network/imtconserver/imtconserver_cpu).
5.  [The amount of RAM](/en/docs/mt5/api/config_network/imtconserver/imtconserver_memoryfree).
6.  [The amount of disk space](/en/docs/mt5/api/config_network/imtconserver/imtconserver_hddfree).
7.  [Maximum number of connections](/en/docs/mt5/api/config_network/imtconserver/imtconserver_connectsmax).
8.  [Maximum load of the network](/en/docs/mt5/api/config_network/imtconserver/imtconserver_networkmax).
9.  [Maximum CPU load](/en/docs/mt5/api/config_network/imtconserver/imtconserver_cpuusagemax).
10.  [Minimum amount of free memory](/en/docs/mt5/api/config_network/imtconserver/imtconserver_memoryfreemin).
11.  The spead of data [reading](/en/docs/mt5/api/config_network/imtconserver/imtconserver_hddspeedread) and [writing](/en/docs/mt5/api/config_network/imtconserver/imtconserver_hddspeedwrite) to a hard disk.
12.  The level of [fragmentation](/en/docs/mt5/api/config_network/imtconserver/imtconserver_hddfragments) of server files.

## IMTConsServerSink [#](config_network#imtconsserversink)

The [IMTConServerSink](/en/docs/mt5/api/config_network/imtconserversink) interface contains the handlers of events of changes in the configurations of the platform components.

[OnCommonSync](/en/docs/mt5/api/config_common/imtconcommonsink/imtconcommonsink_oncommonsync)

[IMTConServer](/en/docs/mt5/api/config_network/imtconserver)