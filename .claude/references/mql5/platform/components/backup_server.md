# Backup Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)Backup Server

# Backup Server

Servers of this type are used for creating backup copies of data that will be used in case of the trade or history server failure. They perform the following functions:

-   They provide the real-time backuping of the trade server and the history server. Each server is associated with one or more separate backup server instances which can replace it at any time.
-   They create backups of all databases every day, besides they perform regular backups of client and trade bases.
-   When backuping a history server they create real time backups of data required for correct restoring of [gateways](/en/docs/mt5/platform/administration/admin_gateways): custom settings that can be stored (at developer's discretion) in the settings.dat file in a gateway work folder, and trade executions database.
-   They provide [automatic failover](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto) in case the primary server becomes unavailable.
-   Using backup servers, you can easily [migrate servers](/en/docs/mt5/platform/components/backup_server/backup_server_switch#manual) to new hardware.
-   Backup servers enable you to quickly [restore](/en/docs/mt5/platform/components/backup_server/backup_server_restore) server operation in the manual mode even if the main trade server is unavailable, and connection to the platform via MetaTrader 5 Administrator is not possible.
-   [Replicate information](/en/docs/mt5/platform/components/backup_server/sql_export) to database managed by MySQL, MariaDB, PostgreSQL, Firebird, MSSQL or Oracle.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For server configuration details, please see the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit" class="topiclink">"Network cluster"</a> section.</span></p></td></tr></tbody></table>

[Console Commands](/en/docs/mt5/platform/components/history_server/history_server_console)

[Backup Features](/en/docs/mt5/platform/components/backup_server/backup_server_features)