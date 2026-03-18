# Backup Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Network cluster](/en/docs/mt5/platform/administration/admin_network)[Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)Backup Server

# Backup Server

Backup servers allow creating backup copies in case of failure of a history or trade servers. The backup server performs the following functions:

-   It provides real-time backup of a trade server and a history server. Each server is associated with one or more separate backup server instances which can replace it at any time.
-   It creates backup copies of all data bases every day, and regularly creates backups of client and trade databases.
-   When a history server is backed up it creates real time backups of data required for correct restoring of [gateways](/en/docs/mt5/platform/administration/admin_gateways): custom settings that can be stored (at developer's discretion) in the settings.dat file in a gateway work folder, and trade executions database.
-   They provide [automatic failover](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto) in case the primary server becomes unavailable.
-   Using backup servers, you can easily [migrate servers](/en/docs/mt5/platform/components/backup_server/backup_server_switch#manual) to new hardware.
-   Backup servers enable you to quickly [restore](/en/docs/mt5/platform/components/backup_server/backup_server_restore) server operation in the manual mode even if the main trade server is unavailable, and connection to the platform via MetaTrader 5 Administrator is not possible.
-   They [replicate information](/en/docs/mt5/platform/components/backup_server/sql_export) to database managed by MySQL, MariaDB, PostgreSQL, Firebird, MSSQL or Oracle.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The process of restoring servers is described in a <a href="/en/docs/mt5/platform/components/backup_server/backup_server_restore" class="topiclink">separate section</a>.</span></p></td></tr></tbody></table>

Settings on the ["Common"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#common), ["Network"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network) and ["Service"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#service) tabs are similar for all types. The backup server setup window contains three more tabs.

## Backup [#](network_backup_server#backup)

![Backup](/en/docs/mt5/platform/img/network_add_backup.png "Backup")

The following parameters are available on this tab:

-   Master server — name of the server whose backups should be created, and the [login](/en/docs/mt5/platform/administration/admin_network/network_add_edit#identifier) (ID) of this server;
-   Use this backup server for failover — the trading platform features [an automated failover system](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto), which switches to a backup server in case of main server failure. By default, the platform can switch to any of existing backup servers. If a certain backup server should not be used by the automatic failover system, disable this option for that server. This may be needed if the backup server is used only for [exporting data to SQL database](/en/docs/mt5/platform/components/backup_server/sql_export). You can disable the "Enable backups" option for such servers - this will save resources required for the creation of backup copies in a disk.  
    The option only disables switching to that server in the automated mode. If necessary, you can switch to this backup server [in manual mode](/en/docs/mt5/platform/components/backup_server/backup_server_switch#manual).
-   Synchronize journals with master server — the backup server is a copy of the backed up one since it stores the same data as the main server, including log files. If you only use the backup server for [data export to SQL](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql), you can disable log synchronization with the primary server to save disk space.
-   Enable backups — apart from synchronizing with the main server in real time, the backup server creates [database file copies](/en/docs/mt5/platform/components/backup_server/backup_server_features#file) on the disk on a daily basis. Such copies allow [restoring](/en/docs/mt5/platform/components/backup_server/backup_server_features#restore) the main server status on a specific day. Disable this option to avoid creating file copies. It does not affect data synchronization with the main server in real time. The backup server will still remain a full copy of the main one. Creating file copies can be disabled if the server is used only for [exporting data to SQL](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql).
-   Backups path — the path on the computer where the file copies of of the databases will be saved. Do not specify the trading platform installation directory here.
-   Backup time — time of creating file copies.
-   Additional backups — frequency of creating additional file copies. By default, file copies are created every 24 hours, but you can set this to happen more often — once per hour or once per 4 hours. Keep in mind that this will require more server resources and more disk space. This option is only available for the backup of trading servers; backup copies of history servers are always created once every 24 hours.
-   Keep backups — file copies storage period. All backup copies older than a period specified in this field are automatically deleted. The parameter is not available for backup servers replicating history servers. They keep only one last state of price databases. It is impossible to store several states for different days due to the large size of the databases.
-   Enable ticks backups — copies of [ticks](/en/docs/mt5/platform/administration/admin_ticks) are created once a day during a full backup. The backup is performed incrementally — the first copy stores the full data cast, while subsequent ones contain only the changes relative to the first copy, which significantly reduces the volume of files. The copies are stored in the \\ticks directory where they are arranged in subdirectories by days, for example, ticks\\2015.11.17, ticks\\2015.11.18, etc. By default, the option is disabled since tick data takes much space.  
       
    For manual tick data recovery, copy the folders with backup copies to the new history server consistently beginning with the oldest. For example, suppose that the backup server has the folders: ticks\\2015.11.17, ticks\\2015.11.18, and ticks\\2015.11.19. First, copy the contents of ticks\\2015.11.17 to the \\ticks directory of the history server. Then, overwrite the contents with the data from the ticks\\2015.11.18 folder, and after doing that - by the contents from the ticks\\2015.11.19 folder.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In addition to creating periodic and full databases backups, the backup servers make starting database copies. Such copies are created before the initial synchronization with the primary server in case its database is damaged. Starting backups have the *start postfix. Initial synchronization is performed during the first connection to the primary server after the backup server start or restart. After the initial synchronization, the backup server will receive data on changes made in the primary server, in real time.</span></p></td></tr></tbody></table>

## SQL Export [#](network_backup_server#sql)

![SQL Export](/en/docs/mt5/platform/img/network_backup_sql.png "SQL Export")

A backup server can export its databases to an SQL database in real-time mode. Considering that data backup is also performed in real-time mode, all data stored in the backup server is sent to SQL database almost immediately.

The following database management systems (DBMS) can be used to export data:

-   Microsoft SQL Server 2005, 2008, 2008 R2, 2012, 2014, 2016, 2017, 2019, 2022
-   MySQL 5.6, 5.7, 8.0, 8.1
-   MariaDB (all versions)
-   Oracle 11g, 12c, 18c, 19c, 21c, 23ai
-   PostgreSQL 8.4 - 17

The backup server supports the export of the following data:

-   configurations: [trading symbols](/en/docs/mt5/platform/administration/admin_symbols) and [groups of clients](/en/docs/mt5/platform/administration/admin_groups)
-   client bases: total [client base](/en/docs/mt5/platform/administration/admin_accounts) and client trading account status
-   trading bases: [orders](/en/docs/mt5/platform/administration/admin_orders), [deals](/en/docs/mt5/platform/administration/admin_deals), [positions](/en/docs/mt5/platform/administration/admin_positions)
-   trading history bases: orders and deals history

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">A full description of the exported data is in the <a href="/en/docs/mt5/platform/components/backup_server/sql_export" class="topiclink">"SQL Export"</a> section.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If you use a backup server only for exporting data to SQL, disable the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#failover" class="topiclink">"Use the backup server for failover"</a> option. Otherwise the server can switch to the primary server mode and will stop exporting data. You may also disable the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#enable_backups" class="topiclink">"Enable backups"</a> option to save resources required for the creation of backup copies in a disk.</span></li></ul></td></tr></tbody></table>

The following parameters should be specified for export setup:

-   Type — type of DBMS, to which data will be exported;
-   Server — address of the server with installed DBMS. Address format may vary for different DBMS. Examples for each type of DBMS are given below;
-   Login — login for connection to a database;
-   Password — password for connection to a database;
-   Data Folder — database name in DBMS, to which the data will be exported. A database should be created in advance. Examples of how to set up this parameter are given below.

Data export process can be monitored via a backup server [Journal](/en/docs/mt5/platform/administration/admin_network/network_journal) using SQL keyword to request the entries.

## SQL Settings [#](network_backup_server#sql_settings)

![SQL Settings](/en/docs/mt5/platform/img/backup_sql_settings.png "SQL Settings")

Data export to a database using SQL can be configured on this tab.

-   Export history orders and deals into separate tables by years — by default, historical orders, deals and daily reports are exported into three separate tables. However, over time, the platform's databases can grow significantly, causing the tables in the SQL database to grow accordingly. If this option is enabled, the data will be additionally split into separate tables by years. You will have separate tables for each year for historical orders, trades and daily reports. This will reduce the load on the server by reducing the table sizes, as well as speed up queries to the database.  
    When enabling this option, modify your SQL queries against the database accordingly. For more information about exported tables, please see ["SQL Export"](/en/docs/mt5/platform/components/backup_server/sql_export).

-   Export additional tables for daily reports — [daily reports](/en/docs/mt5/platform/components/trade_server/daily_reports) store information about the end-of-day status of the trader's open positions and pending orders. You can export this data to an SQL database.  
    Please note that the export of these tables will only begin after the relevant options are enabled. For previously exported daily data, position and order information will not be updated. If you need to export all data, save data from the custom columns (if any) of the mt5\_daily tables and remove these tables from the SQL database. In this case, the backup server will re-export all daily data, including position and order information. Full data replication may take a considerable amount of time, so we recommend performing this operation only on weekends.

-   Do not export users and trades from demo groups — when the option is enabled, accounts from [demo groups](/en/docs/mt5/platform/administration/admin_groups/group_types#demo), as well as trade operations (orders, deals and positions) of these accounts will not be exported to SQL base. This helps to reduce the load on database and increase the speed of queries.
-   Refresh prices and trade profits every N minutes — to reduce the consumption of resources you can limit the rate of exporting the price and profit data. The data include [symbol prices](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_prices), current prices of [positions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_positions) and [orders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_orders), floating profit of positions and almost all information in the table of the [state of trade account](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_accounts).

Click "OK" to complete a backup server creation or editing. If you click "Cancel", the window will be closed without saving changes.

### Sample Data Export Settings for Various DBMS Types

Microsoft SQL Server

![Configuring data export to Microsoft SQL Server](/en/docs/mt5/platform/img/sql_export_mssql.png "Configuring data export to Microsoft SQL Server")

Sample parameter settings when configuring data export to Microsoft SQL Server:

-   Type — Microsoft SQL Server 2005 - 2022.
-   Server — address of the server (IP address or domain name) with the installed DBMS, MSSQL copy name and a port for connection (optional). For example, localhost\\SQLExpress:5000, 192.168.0.1\\SQLExpress.
-   Login — sa. Account used for connection should have the rights to create/edit/delete tables and data.
-   Password  — some\_password.
-   Data Folder — specific name of the database where the data is exported. For example, metatrader5. The database should be created in advance.

MySQL / MariaDB

![Configuring data export to MySQL](/en/docs/mt5/platform/img/sql_export_mysql.png "Configuring data export to MySQL")

Sample parameter settings when configuring data export to MySQL (similar parameters are used for MariaDB):

-   Type — MySQL 5.x & MariaDB 5.x - 11.x.
-   Server — address of the server (IP address or domain name) with the installed DBMS and a port for connection (optional). For example, 192.168.0.100:5000, sqlserver.company.net.
-   Login — sysdba. Account used for connection should have the rights to create/edit/delete tables and data;
-   Password  — some\_password;
-   Data Folder — name of the database (schema) where the data is exported. For example, metatrader5. The database should be created in advance.

## Folders [#](network_backup_server#folders)

The server allows synchronizing not only the standard files and the platform databases, but also any custom directories and files as well. For example, many data feeds and plugins require LIC, DAT and other files for their operation. These files should also be backed up.

![Configuring backup of custom directories](/en/docs/mt5/platform/img/network_add_backup_folder.png "Configuring backup of custom directories")

Specify custom directories for backup on the Folders tab.

-   Folder — path to the folder files from which should be backed up. Paths are specified relative to the installation directory of the primary server.
-   Masks — comma-separated list of copied files. File names can be defined using masks. If the list is specified, only listed files matching the mask are copied. Otherwise, all files from the directory will be copied.
-   Exclude — comma-separated list of ignored files. File names can be defined using masks. If the list is specified, only files from the list and the ones matching the mask will be skipped.
-   Subfolders — whether or not to back up subdirectories in the specified folder.

Example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Folder=plugins\HistoryPlugin</span><br><span class="f_CodeExample">Masks=EURUSD*.*,*.lic,*.dat;</span><br><span class="f_CodeExample">Exclude=*.log,*.tmp</span></p></td></tr></tbody></table>

.lic and .dat files, as well as files beginning with EURUSD are synchronized in the <server\_installation\_directory>\\plugins\\HistoryPlugin folder, while .log and .tmp files are ignored.

[Access Server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server)

[Hosted Access Servers](/en/docs/mt5/platform/administration/admin_network/hosted_access_server)