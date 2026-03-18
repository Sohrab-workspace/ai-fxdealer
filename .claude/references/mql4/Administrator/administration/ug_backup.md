# Backup

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_backup

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Backup

# Backup

MetaTrader trading system pays much attention to realtime synchronization with reserve server and cyclic backup copying of databases.

![Backup](/en/docs/mt4/administrator/img/br_backup.png "Backup")

## Backups Created Locally

The trade server performs two types of the data backup:

-   Full backup - all trade server data is saved (account and order databases, price history, platform configuration). The data backup time is set in "Full backup time" field, while periodicity is specified in "Full backup every" one. For example, if the backup time is 00:20, while periodicity is 4 hours, then all databases will be saved once per four hours starting from 00:20: in 00:20, 04:20, 08:20, etc. It is reasonable to perform a full backup once per day, as they occupy quite a lot of space and can slow down the server's operation.
-   Short backup - only the most critical data is saved - account and order databases. Periodicity of saving that data is set in "Archival backup every" field: once per 5, 15, 30 or 60 minutes. In "Shift of archive backup time" field, you can specify the shift in minutes from the beginning of an hour when creation of short backup copies is to be launched.

All backup copies are stored in the directory specified in "Full backup to" parameter. Inside the directory, the backup copies are stored in the following way:

-   BASES - the last backup copy of the price data history.
-   CONFIG - backup copies of platform configuration files by days. The storage depth is defined by "Keep archival backups within" parameter. If the parameter's value is not specified or is less than 3 days, the copies for the last 3 days are stored.
-   ARCHIVE - the following copies are stored in the directory:

-   periodically created copies of order and user databases - files of orders\_YYYYMMDD\_HHMMSS\_backup.dat, users\_YYYYMMDD\_HHMMSS\_backup.dat forms. The storage depth is defined by "Keep archival backups within" parameter.
-   copies of order and user databases created during the full backup. The storage depth is defined by "Keep archival backups within" parameter.
-   archival account and order databases - files of orders\_archive\_YYYY.dat and users\_archive\_YYYY.dat forms.
-   files generated during the removal of one and more user accounts or one and more orders - files of orders\_YYYYMMDD\_HHMMSS\_delete.dat and users\_YYYYMMDD\_HHMMSS\_delete.dat forms. The storage depth is defined by "Keep archival backups within" parameter.
-   last day report databases - daily.dat and ind\_daily.dat files.

The server launches MetaTrader BackUp support program once a day. This program archives daily backups of databases and deletes out-dated backups according to the parameters in "Keep archival backups within".

In addition to automatic archive creation, the server can launch an external program indicated in the "Archival backup external processing" field. In addition to automatic archive creation, the server can immediately launch an external program or script (\*.bat, \*.cmd, \*.vbs and others) indicated in the "Archival backup external processing" field. When an external processor of backups has been called, it will get names of the current archives of databases of clients and orders as parameters additional to those given in the "Archival backup external processing" field.

For example, if

ftpbackup.bat myserver mylogin mypassword

has been specified in the "Archival backup external processing" field, the server will execute the command

ftpbackup.bat myserver mylogin mypassword users\_20051125\_120017\_backup.dat orders\_20051125\_120017\_backup.dat

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Warning:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">All external commands and scripts must be located in the \TOOLS sub-directory of the server directory.</span></li><li class="p_tableatten"><span class="f_tableatten">The scripts/databases to be launched must not apply to open databases of the trading system in the \BASES directory. This can result in conflicts when bases are applied to both from the server and from scripts at the same time. You should operate only with databases copied by the server in the ARCHIVE sub-directory of the directory defined by the parameters in "Full backup to".</span></li></ul></td></tr></tbody></table>

## Export historical data and charts publication

It is often necessary to export historical data, for example, when you need to make charts for publishing on the Internet in online mode. To enable cyclic export of quotes (to \*.FXH files of the \\EXPORT directory), it is necessary to indicate the list of instruments formatted as "Symbol,Period;Symbol2,Period2;" in the "Export securities" field, and to indicate the external script in "Export external processing" for further processing the exported data. Data will not be exported if the external script is not indicated. The export schedule can be indicated in the "Export external processing every" field.

For more details about charts publication refer to article [WebServices: Charts Publication](https://support.metaquotes.net/en/articles/5) at MetaQuotes Support Center.

## Real-time Backup using the MetaTrader 4 WatchDog Tool

The trade server should operate in 24/7 mode. However, it is difficult to ensure such faultless operation for a single physical server since it bears plenty of technical risks (equipment failure, power outage, etc.). MetaTrader 4 WatchDog has been designed for synchronization between the main server and the back-up server in real-time mode. It has the following functions:

-   Synchronization of executable files, plugins and data feeds
-   Synchronization of configuration files (the first one is performed at the start followed by one synchronization per 30 minutes)
-   Full synchronization of trade and client databases, as well as the daily report one (the first one is performed at the start followed by one synchronization per day)
-   Synchronization of quote history (the first one is performed at the start followed by one synchronization per 30 minutes)
-   Support for identity of trade and client databases to the main server
-   Generation of backup copies of all databases, as well as creation of configuration files (once per day)
-   Synchronization of custom directories (for example, working files of plugins and data feeds)

Thus, in case of a main server failure, a backup server can be deployed within a few minutes to continue operation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">MetaTrader 4 WatchDog replicates data according to the folders the data is stored in on the main trade server. Paths to databases (orders.dat, users.dat, history bases), logs and backup files may differ from the standard ones. WatchDog checks the availability of these paths on the backup server. If they are available, the replication is performed to the appropriate directories. Otherwise (for example, in case the bases are stored in F:\history, while the appropriate disk section is not physically present on the backup server), the replication is performed to the default directories.</span></p></td></tr></tbody></table>

To configure the backup system in real time via MetaTrader 4 WatchDog, use the following parameters in the Backup section of the Administrator terminal:

-   Sever role - sever role:

-   Standalone - backup server is not used;
-   Master - this server is being replicated;
-   Slave - this status is intended for servers restored from a backup.

-   Failover server login \- an existing [account](/en/docs/mt4/administrator/administration/ug_accounts) that will be used by MetaTrader 4 WatchDog for connecting to the trade server. The account must not belong to the "managers" group.
-   Failover server additional password - a password for additional authorization of MetaTrader 4 WatchDog on the server (the Master Password field in the MetaTrader 4 WatchDog settings).
-   Failover server IP address and port - an address and port of a server for creation of backups in the real-time mode:

-   Synchronized - backup copy synchronized with master server;
-   Synchronizing - data is being synchronized;
-   Disconnected - backup server disabled.

Before launching the MetaTrader 4 WatchDog component on the backup server, configure the main server: switch its status to Master and set address and password for the backup server (the backup server password is used in MetaTrader 4 WatchDog for additional authentication). Besides, the backup server address should be entered to the list of access points, so that client terminals are able to try to connect to it in case of the main server failure.

Make sure to restart the server after making all the changes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If MetaTrader 4 Server has the status of Master or Slave, a connection to the pair server is established before the start. If the connection is successful, the server is not launched in order to prevent the parallel operation of clients on two different servers.</span></p></td></tr></tbody></table>

### Installing and Configuring MetaTrader 4 WatchDog

By default, MetaTrader WatchDog is supplied together with MetaTrader Server and located in the server root directory (mtwdsrv.exe file). During its first launch, the setup process is activated. Simply follow the setup wizard instructions.

![Installing MetaTrader 4 WatchDog](/en/docs/mt4/administrator/img/watchdog_install.gif "Installing MetaTrader 4 WatchDog")

After the setup is complete, MetaTrader 4 WatchDog configuration window appears.

![Configuring MetaTrader 4 WatchDog](/en/docs/mt4/administrator/img/watchdog_config.png "Configuring MetaTrader 4 WatchDog")

Specify the main server address and the Master Password used for additional authentication on the server ([Failover server additional password](/en/docs/mt4/administrator/administration/ug_backup#failover_login)). Specify the account from the [Failover server login](/en/docs/mt4/administrator/administration/ug_backup#failover_login) field in the Login box, as well as the appropriate connection password - in the Password box. Next, launch MetaTrader 4 WatchDog clicking Start. Synchronization messages start appearing in the logs.

### Configuring Synchronization of Custom Directories [#](ug_backup#custom_folders)

MetaTrader 4 WatchDog allows you to synchronize not only the standard files and the platform databases, but also any custom directories and files as well. For example, many data feeds and plugins require LIC, DAT and other files for their operation. These files should also be backed up.

Specify custom directories for synchronization in the mtwdsrv.ini file located in the \[MetaTrader 4 WatchDog installation folder\]\\config. You can specify up to 64 custom directories. The paths are set relative to the trade server root.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Never specify the 'base' folder of the trade server or files from it as custom files and directories for synchronization. The server will not be able to read its databases, and WatchDog will not be able to create backup copies.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Subdirectories are not replicated. Each added directory should be specified as a separate line in mtwdsrv.ini.</span></li></ul></td></tr></tbody></table>

You can specify the filters for including or excluding files of a specified type during synchronization for each directory. A single line may contain up to three entries separated by a semicolon:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Folder=&lt;folder_path&gt;;[list&nbsp;of</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">files</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">synchronization];[list&nbsp;of</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">skipped</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">files]</span></p></td></tr></tbody></table>

Here:

-   <folder\_path> is a directory name relative to a root folder a trade server is installed at. If no file masks are specified, all files inside the directory are copied;
-   list of files for synchronization - list of copied files separated by commas. File names can be defined using masks. If the list is specified, only listed files matching the mask are copied;
-   list of skipped files - list of ignored files separated by commas. File names can be defined using masks. If the list is specified, all listed files matching the mask are skipped.

Sample entry:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Folder=plugins\HistoryPlugin;EURUSD*.*,*.lic,*.dat;*.log,*.tmp</span></p></td></tr></tbody></table>

.lic and .dat files, as well as files beginning with EURUSD are synchronized in the <server\_installation\_directory>\\plugins\\HistoryPlugin folder, while .log and .tmp files are skipped.

## Emergency Switching to the Backup Server and Restoring the Main Server

If the main server is not available via the Administrator terminal, you should switch to the backup server manually.

-   Make sure that the main server is stopped. Check if MetaTrader Server service status is set to Disabled or the server is disabled physically. Also, switch MetaTrader Server service launch type to Manual.
-   Stop MetaTrader 4 WatchDog on the backup server by the Stop dialog command or by stopping the system service.
-   If a data center has been installed and launched on the backup server along with the WatchDog service (as an additional access point of the main server), stop it as well.
-   Launch the backup server: a trade server service is installed in the system when installing MetaTrader 4 WatchDog. Launch it.
-   Start history synchronization (the backup server may not have the history for the last 30 minutes, since WatchDog synchronizes the history only once per 30 minutes).
-   Start the platform update manually from the Services menu of the Administrator terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">ATTENTION: Before you launch the backup server, make sure the main server is stopped. Otherwise, your clients may start working with different servers. For example, suppose that something has happened to your provider's Internet link, the main server is unavailable (though it works properly) and the backup server is deployed. After a while, connection to the main server is restored causing two servers to work simultaneously. In this case, call your provider and ask him to disable the main server immediately.</span></p></td></tr></tbody></table>

After the main server's operability is restored, switch back to it from the backup server. Wait for a break between trading sessions (for example, on Saturday or Sunday) and take the following steps:

-   Stop the backup server.
-   Move the following files from the backup server to the main one:

-   \*.exe files
-   database files: users.dat, orders.dat and daily.dat
-   configuration files: license.lic, access.ini, common.ini, feeders.ini, groups.ini, holidays.ini, managers.ini, plugins.ini, secgroups.ini, securities.ini, servers.ini, sync.ini, time.ini
-   plugins and their settings from the 'plugins' directory
-   history files from the 'history' folder

-   Launch the main server.
-   Launch WatchDog on the backup server.

## Switching to the Backup Server

This procedure allows you to quickly and automatically switch to the backup server (MetaTrader 4 WatchDog) instead of history or trade one. Switching is suitable for the following cases:

-   Switching to the backup server in case of the main server malfunction.
-   Trade server transfer. You just need to install MetaTrader 4 WatchDog on the new server, properly setup the backup server via MetaTrader 4 Administrator and switch to the newly installed backup server afterwards.

Switching to the backup server can be performed both [manually](/en/docs/mt4/administrator/administration/ug_backup#manual) and [automatically](/en/docs/mt4/administrator/administration/ug_backup#auto).

### Possible Data Loss [#](ug_backup#possible_loss)

MetaTrader 4 WatcDogs backs up all critical trade server data in real time. Some non-critical trade server data, as well as history server data are backuped at specific intervals. Critical and non-critical data are displayed in the table below:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Data</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trade server</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Critical (real time backup)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">User base (users.dat file in \bases folder)</span></p><p class="p_fortable"><span class="f_fortable">Order base (orders.dat file \bases folder)</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Non-critical (backup every thirty minutes)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Archive databases (orders_archive_*.dat and users_archive_*.dat files in \bases folder)</span></p><p class="p_fortable"><span class="f_fortable">Price database (*.fxh files in \history folder)</span></p><p class="p_fortable"><span class="f_fortable">Plugins (*.dll files in \plugins folder)</span></p><p class="p_fortable"><span class="f_fortable">Configuration databases (*.ini files in \config folder)</span></p><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/administrator/administration/ug_backup#custom_folders" class="topiclink">Custom folders</a></span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Non-critical (backup every day/at WatchDog reconnections)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Data feeds (*.feed and *.ini files in \datafeed folder)</span></p><p class="p_fortable"><span class="f_fortable">Mail templates (*.htm files in \</span><span class="f_ol">confirms folder)</span></p><p class="p_fortable"><span class="f_fortable">Daily report databases (daily.dat files \bases folder)</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Server migration must only be performed in non-trading hours. When switching to the backup server, it does not copy data that the main server continues to receive.</span></li><li class="p_tableatten"><span class="f_tableatten">In order to prevent important data from being lost, trading operations and changes in the client base are not allowed on the main server right after the start of switching to the backup server. The ban is valid for one minute. If the platform fails to switch to a backup server within this period, the ban is removed.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">To avoid the loss of data that is backuped every 30 minutes, restart the WatchDog. After that, the latest data backup is created. A message of the following type in the WatchDog log indicates completion of the backup copy creation: "Network: 39 Kb received / 21 Kb sent" Synchronized".</span></li></ul></td></tr></tbody></table>

### Switching [#](ug_backup#manual)

In order to switch to the backup server, execute "![Switch to backup server](/en/docs/mt4/administrator/img/switch_to_backup_icon.png "Switch to backup server") Switch to Backup" command in [Services](/en/docs/mt4/administrator/getting_started/ug_main_menu) menu. The confirmation window appears after that.

![Confirming the switching to the backup server](/en/docs/mt4/administrator/img/switch_to_backup_confirm.png "Confirming the switching to the backup server")

To launch the procedure, enter the confirmation code and click Switch. The switching is performed as follows:

-   MetaTrader 4 WatchDog installs the trade server service.
-   Updates the configuration.
-   Sends notifications to the main server.
-   The main server switches to MetaTrader 4 WatchDog mode.

After completing the switching process, a new [administered server](/en/docs/mt4/administrator/administered_servers/ug_server_add) in MetaTrader 4 Administrator should be created to connect to the trade server. To do this, specify the IP address, on which the MetaTrader 4 WatchDog server has been installed.

For the client terminals to be able to connect to the new server installed instead of MetaTrader 4 WatchDog, the ["Data Centers"](/en/docs/mt4/administrator/administration/ug_data_server) section must include:

-   either IP address of the server where MetaTrader 4 WatchDog is installed,
-   or a data center (that is capable of going through the addresses of the main and the backup servers automatically).

![Adding WatchDog to data centers](/en/docs/mt4/administrator/img/watchdog_data_center.png "Adding WatchDog to data centers")

## Switching to the Backup Server Automatically [#](ug_backup#auto)

In case of any emergency, the main server can be automatically switched to the backup one. This process is similar to switching manually but the need for switching is managed by MetaTrader 4 platform.

The necessity to switch to the backup server is defined by the monitoring ("witness") servers. The MetaTrader 4 WatchDog, as well as [data centers](/en/docs/mt4/administrator/administration/ug_data_server#witness) (with monitoring mode enabled) act as the monitoring ones. The back-up server monitors the availability of the main server in real time mode and checks if it is available for the data centers as well.

Automatic switching can be enabled in Backup section:

![Failover](/en/docs/mt4/administrator/img/trade_backup_settings.png "Failover")

"Failover server switch mode" field allows selecting one of the two options:

-   Master server is not accessible to most data centers — the number of the monitoring servers unable to access the main server should exceed the ones able to access it at least by one for the switch to occur.
-   Master server is not accessible to all data centers — the main server should be unavailable for all monitoring servers for the switch to occur.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The number of monitoring servers should not be less than 2.</span></p></td></tr></tbody></table>

In "Failover server switch timeout" parameter, you can specify the time (in seconds) during which the server should be unavailable for monitoring servers to start switching to the back-up server. Also, after this time period, the data centers start their attempts to connect to the current backup server's IP address specified in "Failover server IP address and port" parameter (trying to connect to it as to the trade server).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When measuring the time of the master server's unavailability, its cause is considered. In case of a manual restart of the server, the unavailability time is increased according to the time required for restart.</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Unexpected failure — switching is performed after the specified timeout.</span></li><li class="p_tableatten"><span class="f_tableatten">The server or the system service or the operating system is restarted by the administrator — switch time is increased by the time spent for restart. The minimum time is 30 seconds and the maximum time is 300 seconds.</span></li><li class="p_tableatten"><span class="f_tableatten">Server restart during update (<a href="/en/docs/mt4/administrator/administration/ug_live_update" class="topiclink">LiveUpdate</a>) — switch time is increased by the time spent for restart. The minimum time is 180 seconds and the maximum time is 300 seconds.</span></li></ul></td></tr></tbody></table>

In case the connection is not established by the end of the timeout, MetaTrader 4 WatchDog starts checking the monitoring data centers. To make a data center monitor the main server, enable "Use for monitoring the trade server and failover" option in its settings:

![Configuring a data center](/en/docs/mt4/administrator/img/win_data_server.png "Configuring a data center")

It is recommended no to enable this option for MetaTrader 4 WatchDog added as a data center. Also one should not enable it for non-working data centers. It increases the time of switching to backup and the amount of consumed resources.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To connect to a data center, MetaTrader 4 WacthDog uses its public address (Public server address). If the data center is not available at this address, it tries to connect to its internal address (Internal IP address) using the port specified for the public address.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If the data center is unavailable for the backup one, that does not mean that the main server is also unavailable. In this case, the number of monitoring servers is reduced.</span></li></ul></td></tr></tbody></table>

After checking the data centers, MetaTrader 4 WatchDog analyzes to how many of them the trade server is accessible/not accessible:

-   In case "Master server is not accessible to most data centers" option is selected: in order to start switching, the number of monitoring servers to whom the trade server is not accessible must be strictly greater than the number of servers to whom it is accessible (for example, 2 > 1, 3 > 2, 4 > 3). In case they are equal (for example, accessible to 2 servers and not accessible to 2 servers), switching will not be performed.
-   In case "Master server is not accessible to all data centers" option is selected: in order to start switching, the trade server must be not accessible to all monitoring servers.

If a condition is fulfilled, switching will start. In case it is not fulfilled, MetaTrader 4 WatchDog will check the monitoring data centers again. Repeated checks are performed with 10 seconds intervals (10 attempts) and then with 60 seconds intervals.

After switching the new trade server will be available at "Failover Server IP address and port". As soon as the old server is restored or its network environment is restored, it will detect the new trade server and switch itself to a backup server. The process of detecting a new (opposite) trade server is described in details below.

### Detecting Opposite Trade Server [#](ug_backup#opposite_detect)

As a trade server starts it checks whether another trade server works at the address specified in "Failover Server IP address and port". To do it, it tries to connect to this address as MetaTrader 4 WatchDog. If connected, it tries authorizing on it as MetaTrader 4 WatchDog. Successful authorization means that an opposite server is detected.

Further it analyzes the data available on the opposite server: the number of accounts, the number of orders and the last time of switching to the trade server from a backup one.

-   If the sum of accounts and orders on the current server is greater than that on the opposite server, the current server will remain trade sever and the opposite server will be switched to backup.
-   If the sum of accounts and order is equal on both servers, the date of last switching from backup is compared. If the current server has a greater date, it will remain trade server and the opposite server will be switched to backup.
-   If the sum of accounts and orders on the current server is less than that on the opposite server, the current server will be switched to backup.

### Automatic Switching of Data Centers to the New Trade Server [#](ug_backup#dc_switch)

After losing connection to the trade server, the data centers automatically try to connect to the backup server as to the main one after the time specified in "Failover server switch timeout" parameter. The data center uses the address specified in "Failover Server IP address and port" field, as well as the one specified in "Failover Server" field of the data center settings for connection:

![Data center settings](/en/docs/mt4/administrator/img/data_center.png "Data center settings")

The data center successively tries to connect to the backup server: first, at "Failover Server" address, then at "Failover Server IP address and port" one.

If connection at "Failover Server" address is successful, the data center starts using it as the main server's address (it is written to "MetaTrader 4 Server" field), while the old address of the trade server is used as the backup server's one (written to "Failover Server").

Sample settings before switching:

-   MetaTrader 4 Server - external address 1.1.1.1:443 (the trade server actually works in the local network at the address 192.168.9.1:443).
-   Failover Server - external 2.2.2.2:443 (MetaTrader 4 WatchDog actually works in the local network at 192.168.9.2:443).
-   Failover Server IP address and port - internal address 192.168.9.2:443.

The same settings after the switching:

-   MetaTrader 4 Server - 2.2.2.2:443.
-   Failover Server - 1.1.1.1:443.
-   Failover Server IP address and port - 192.168.9.1:443.

If connection at "Failover Server" address failed, the data center tries to connect to the address specified in "Failover Server IP address and port" field. If connection is successful, the data center starts using it as the main server's address (it is written to "MetaTrader 4 Server" field), while the old address of the trade server is used as the backup server's one (written to "Failover Server"). The address previously specified in "Failover Server" field is deleted, as it becomes unnecessary.

Sample settings before switching:

-   MetaTrader 4 Server - external address 1.1.1.1:443 (the trade server actually works in the local network at the address 192.168.9.1:443).
-   Failover Server - external address 2.2.2.2:443 (MetaTrader 4 WatchDog actually works in the local network at 192.168.9.2:443).
-   Failover Server IP address and port - internal address 192.168.9.2:443.

The same settings after the switching:

-   MetaTrader 4 Server - 192.168.9.2:443.
-   Failover Server - 1.1.1.1:443.
-   Failover Server IP address and port - 192.168.9.1:443.

If the data center is unable to connect to "Failover Server IP address and port" address, the cycle of connection attempts is restarted.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Specifying an additional backup server's address in "Failover Server" field of the data center settings allows using the system of automatic and manual switching in case of complex network configurations, for example, when the backup server is installed in the local network, while the data center is connected to it from the outside via a router.</span></p></td></tr></tbody></table>

### Logging Monitoring Results

You can view MetaTrader 4 WatchDog journal to control the process of monitoring the main server. The sample entry is shown below:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">1</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">11:15:53</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">unavailable</span><br><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">11:15:53</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">unavailable</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">data</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">center</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'192.168.0.117:1955'</span><br><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">11:15:53</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">and</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">unavailable</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">2</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">witnesses</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">[4</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">min]</span><br><span class="f_CodeExample">1</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">11:16:53</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">unavailable</span><br><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">11:16:53</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">unavailable</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">data</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">center</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'192.168.0.117:1955'</span><br><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">11:16:53</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">available</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">0</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">and</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">unavailable</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">2</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">witnesses</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">[5</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">min]</span><br><span class="f_CodeExample">2</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">11:16:53</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">is</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">unavailable</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">5</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">min</span><br><span class="f_CodeExample">2</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">11:16:53</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Failover</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">start</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">switching</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">to</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">master</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">mode</span></p></td></tr></tbody></table>

These entries mean as follows:

-   The main server is unavailable.

-   The main server is unavailable for the data center having IP address '192.168.0.117:1955'.
-   The main server is available for 0 witnesses and not available to 2 witnesses within 4 minutes.

-   The main server is unavailable.

-   The main server is unavailable for the data center having IP address '192.168.0.117:1955'.
-   The main server is available for 0 witnesses and not available to 2 witnesses within 5 minutes.
-   MetaTrader 4 WatchDog has started switching to the main server mode.

The entries related to switching to the backup server are saved in the separate mtfailover.log file.

[Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)

[Live Update](/en/docs/mt4/administrator/administration/ug_live_update)