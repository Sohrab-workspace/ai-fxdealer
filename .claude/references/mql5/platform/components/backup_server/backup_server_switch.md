# Switching to Backup Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/backup_server_switch

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
                -   [Backup Features](/en/docs/mt5/platform/components/backup_server/backup_server_features)
                -   [Switching to Backup Server](/en/docs/mt5/platform/components/backup_server/backup_server_switch)
                -   [Restoring Server](/en/docs/mt5/platform/components/backup_server/backup_server_restore)
                -   [SQL Export](/en/docs/mt5/platform/components/backup_server/sql_export)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
            -   [Old WebTerminal](/en/docs/mt5/platform/components/web_terminal_old)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Backup Server](/en/docs/mt5/platform/components/backup_server)Switching to Backup Server

# Switching to Backup Server

The MetaTrader 5 platform can automatically monitor the availability of trade and history servers. The monitoring is performed by the backup server itself as well as by access servers. Each server monitors the availability of the main server and polls other monitoring servers to check whether the main server is available to them.

If the main server is unavailable for some time, the platform will automatically switch to the backup server. The downtime is minimal, while switching usually takes less than a minute.

In the platform, you can also [switch to a backup server manually](/en/docs/mt5/platform/components/backup_server/backup_server_switch#manual). In case of a failure of the history server or a non-main trade server, you can quickly switch to the backup server in the automated mode. The same procedure provides for an easy migration of servers to new hardware. You will only need to properly setup the backup server via MetaTrader 5 Administrator, use the [fast deployment](/en/docs/mt5/platform/platform_installation/deployer) procedure and switch to the newly installed backup server afterwards.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/platform/components/backup_server/backup_server_features" class="topiclink">All critical trade and history server data</a> is backed up in real time. Some non-critical trade server data, as well as history server data are backed up every hour. When switching to the backup server, critical data obtained during the procedure may be lost (the procedure itself usually takes less than a minute). Therefore, we strongly recommend that you switch to the backup server only outside of working hours.</span></p></td></tr></tbody></table>

## Switching to the Backup Server Automatically [#](backup_server_switch#auto)

Automatic switching to a backup server allows minimizing the platform unavailability time in case of emergency situations. The platform automatically monitors the performance of its components and switches to backup servers if necessary.

The necessity to switch to the backup server is defined by the monitoring ("witness") servers. The backup server itself and access servers (with monitoring mode enabled) act as the monitoring ones. The backup server monitors the availability of the master server in real time mode and checks if it is available for the access servers as well.

Automatic switching can be enabled in the master server's settings (either a trade or a history one):

![Failover](/en/docs/mt5/platform/img/trade_backup_settings.png "Failover")

There are two scenarios for determining the unavailability of the main server:

-   Server is not accessible to most access servers — the number of the monitoring servers unable to access the master server should exceed the ones able to access it at least by one for the switch to occur.  If you have configured five monitoring servers, the main server should be unavailable to at least three of them, or to four of six monitoring servers. If you are using two monitoring servers (the minimum allowed number), the main server should be unavailable for both of them.
-   Server is not accessible to all access servers — the master server should be unavailable for all monitoring servers for the switch to occur.If you have configured five monitoring servers, the main server should be unavailable to all of them.

If several backup servers are used for one main server, then each of the backup servers will start switching to the master server mode in case of the main server failure. The last switched server will be used as the main server, while all the rest of them will switch back to backup mode.

If a certain backup server should not be used for automatic switching, disable in its settings the following option: ["Use this backup server for failover"](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#failover). This may be needed if the backup server is used only for [exporting data to SQL database](/en/docs/mt5/platform/components/backup_server/sql_export).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The number of monitoring servers should not be less than 2.</span></li><li class="p_tableatten"><span class="f_tableatten">It is recommended to install access servers on different computers (different data centers), separate from the main and history servers. This will provide the most relevant server monitoring data.</span></li></ul></td></tr></tbody></table>

In "Switch timeout" parameter, you can specify the time (in seconds) during which the server should be unavailable for monitoring servers to start switching to the back-up server. Also, after this time period, other platform components start their attempts to connect to the [access points](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) of the current backup server (trying to connect to it as to the master one).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When measuring the time of the master server's unavailability, its cause is considered. In case of a manual restart of the server, the unavailability time is increased according to the time required for restart.</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Unexpected failure — switching is performed after the specified timeout.</span></li><li class="p_tableatten"><span class="f_tableatten">The server or the system service or the operating system is restarted by the administrator — switch time is increased by the time spent for restart. The minimum time is 30 seconds and the maximum time is 300 seconds.</span></li><li class="p_tableatten"><span class="f_tableatten">Server restart during update (<a href="/en/docs/mt5/platform/administration/admin_update" class="topiclink">LiveUpdate</a>) — switch time is increased by the time spent for restart. The minimum time is 180 seconds and the maximum time is 300 seconds.</span></li></ul></td></tr></tbody></table>

To make an access server a monitoring one, enable "Use this server for monitoring the cluster and failover" option in the server's settings:

![Access server settings](/en/docs/mt5/platform/img/network_add_access.png "Access server settings")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If the access server is unavailable for the backup one, that does not mean that the master server is also unavailable. In this case, the number of monitoring servers is reduced.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">In case of the master and other servers' simultaneous failure, the master server is restored first.</span></li></ul></td></tr></tbody></table>

### Features of Connecting to Monitoring Servers

The backup server uses the following algorithm for connecting to the monitoring servers:

-   As soon as the main server becomes unavailable for the backup server, the backup server checks all monitoring servers one by one and trues to connect to them.
-   First, the backup server tries to connect to the monitoring server via the local address if available. Connection to a local address is performed if [listen addresses](/en/docs/mt5/platform/administration/admin_network/network_add_edit#bind) of the backup and access servers are located in 10.\*, 172.16.\* — 172.31.\* or 192.168\* subnet. The first three octets in their addresses should coincide. In that case, both servers are deemed to be located in a single subnet, and the backup server tries to connect directly to the listen address of the access server. Example: the backup server has 192.168.0.100:1951 listen address, while the access one - 192.168.0.105:1950.
-   If connection via the local address has failed, the backup server uses [public points](/en/docs/mt5/platform/administration/admin_network/network_add_edit#public) of the access server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In order for the switch to occur as fast as possible, all access servers should be available. There should be no disabled servers among the monitoring ones. The backup server spends 5 seconds trying to connect to a non-existent address.</span></p></td></tr></tbody></table>

### Using Several Backup Servers

If several backup servers are used for a single main one, then each of the backup servers starts switching to the master server mode in case of the main server's failure. The last switched server is used as the master one, while all the rest of them switch back to backup server mode.

### Logging Monitoring Results

You can request the backup server's log using "Failover" keyword to control the process of monitoring the master server. Sample entries:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2013.09.09</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">09:07:33</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'1'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'Trade&nbsp;Main'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span><br><span class="f_CodeExample">2013.09.09</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">09:07:33</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'1'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'Trade&nbsp;Main'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">witness</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'2'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'Access&nbsp;Point&nbsp;1'</span><br><span class="f_CodeExample">2013.09.09</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">09:07:34</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'1'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'Trade&nbsp;Main'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">witness</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'6'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'Access&nbsp;Point&nbsp;2'</span><br><span class="f_CodeExample">2013.09.09</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">09:07:54</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">witness</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">access</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'7'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">not</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span><br><span class="f_CodeExample">2013.09.09</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">09:07:54</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'1'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'Trade&nbsp;Main'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">witness</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'11'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'Access&nbsp;Point&nbsp;3</span><br><span class="f_CodeExample">2013.09.09</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">09:07:54</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'1'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'Trade&nbsp;Main'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">4</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">witnesses</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">and</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">unavailable</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">witnesses</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">[0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">min]</span></p></td></tr></tbody></table>

These entries mean as follows:

-   Master server with identifier 1 is available.
-   Master server with identifier 1 is available for monitoring server 2 named Access Point 1.
-   Master server with identifier 1 is available for monitoring server 6 named Access Point 2.
-   Monitoring server with identifier 7 is unavailable for the backup server.
-   Master server with identifier 1 is available for monitoring server 11 named Access Point 3.
-   Master server is available for 4 witnesses and not available to 0 witnesses. The time, during which the server has been unavailable, is shown in brackets.

### Working after Switching to the Backup Server

After the backup server has switched to the trading one, the client terminals scan public access points of the access server in order to connect to it. The time of going through the access points depends on the following factors:

-   Actual accessibility of the public point for a client. If an address is not available for the client (for example, a local IP address is specified in the settings as a public access point), the terminal spends 10 seconds trying to connect to it. An attempt to connect to the next access point is made only in 10 seconds.
-   The number of the access server addresses unavailable for clients. For example, if two local addresses 192.168.0.100 and 192.168.0.101, as well as an external one - access.server.com (available external address of the server) are specified among the public access points, the client terminals will first spend 20 seconds trying to connect to local addresses before successfully connecting to the external one.
-   Availability of the trade and history servers for the access one. The access server goes through the access points of the trade and history servers according to their [network settings](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network). Correctness of the network settings defines how quickly the access server becomes ready for work.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended that the access servers having local IP addresses in the list of <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit#public" class="topiclink">public points</a> are made available only for the administrators and managers working in the same local network. To do this, uncheck all options except "Allow administrator connection" and "Allow manager connection" ones in the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#permissions" class="topiclink">Permissions</a> tab of the access server.</span></p></td></tr></tbody></table>

## Manual Switching to a Backup Server and Migration of Servers [#](backup_server_switch#manual)

In the platform, it is possible switch to a backup server from the main one manually. It is a quick and automatic procedure. In addition to emergency cases, the procedure can be used for migrating servers to new hardware.

Install the backup server on the computer, to which you plan to migrate the server. After installing and launching the backup server, it is recommended to let it operate for a few days on the new machine to make sure it operates well.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If you want to avoid the loss of data that is backed up every hour, the backup server should be restarted before switching to it. The server creates the latest data backup. While the server is busy backing up data, the following sign is displayed on its icon <img class="help" alt="Backup in process" title="Backup in process" width="8" height="8" src="/en/docs/mt5/platform/img/backup_server_backuping_icon.png"> (the icon itself has the following look <img class="help" alt="Backup in process" title="Backup in process" width="16" height="16" src="/en/docs/mt5/platform/img/backup_server_backuping_icon2.png">). Start switching to the backup server only after the backup process is complete.</span></li><li class="p_tableatten"><span class="f_tableatten">Server migration must only be performed in non-trading hours. During the switching procedure, the main server continues to receive data, which will not be copied to the backup server.</span></li><li class="p_tableatten"><span class="f_tableatten">In order to prevent important information from being lost, trading and changes in the client base are not allowed on the main server right after the start of switching to the backup server. The ban is valid for one minute. If the platform fails to switch to a backup server within this period, the ban is removed.</span></li></ul></td></tr></tbody></table>

Execute "![Switch to backup server](/en/docs/mt5/platform/img/switch_to_bakcup_icon.png "Switch to backup server") Switch to backup server" command:

![Switching to the backup server](/en/docs/mt5/platform/img/switching_to_backup.png "Switching to the backup server")

To avoid accidental switching, the platform requires an additional confirmation. In the dialog that appears, enter the required characters and click "Switch".

![Confirming the switching to the backup server](/en/docs/mt5/platform/img/switch_to_backup_confirm.png "Confirming the switching to the backup server")

After the procedure is complete, you will see that the trade/history server has changed places with the backup server in Network section.

## The Features of the Switching Procedure [#](backup_server_switch#features)

On the backup server's side, the switching process is performed as follows:

-   The backup server stops Windows service.
-   It also updates the network settings of the platform. The servers exchange roles, while the main server becomes the backup one, and the backup server starts operating as the main trade server:

-   -   The network settings (IP addresses, outgoing address, public points) and the name of the former backup server are set for the main server in the platform configuration.
    -   The IP address and the name of the former main server are set for the backup server in the platform configuration.
    -   On the servers, only their internal IDs change. The ID of the former main server is set for the new backup server, and the ID of the former backup server is set for the new main one.

![Changes in the Platform Configuration](/en/docs/mt5/platform/img/switch_to_backup_server_change.png "Changes in the Platform Configuration")

-   The master server's Windows service is installed
-   Notification is sent to the master server, waiting for confirmation.
-   The master server's Windows service is launched.
-   The former backup server's Windows service is deleted.

If the backup server has been active during the switch, it is switched to the backup mode:

-   The master server's Windows service is stopped.
-   Network settings are updated similar to how it is done for the backup server.
-   The backup server's Windows service is installed and launched.
-   The former master server's Windows service is deleted.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If the former master server was inactive during the switch to the backup one (for example, the server computer was shut down) and the copy restored from backup is already working by the moment the server is restored, the former master server switches to the backup mode automatically (unless switching to a backup server is prohibited in its <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#backup" class="topiclink">settings</a>).</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Physically (on the hard drive), the new trade/history server operates from the former backup server's directory, while the new backup server operates from the trade/history server's one.</span></li></ul></td></tr></tbody></table>

[Backup Features](/en/docs/mt5/platform/components/backup_server/backup_server_features)

[Restoring Server](/en/docs/mt5/platform/components/backup_server/backup_server_restore)