# Restoring Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/backup_server_restore

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Backup Server](/en/docs/mt5/platform/components/backup_server)Restoring Server

# Restoring Server

If the main trade server fails, you will not be able to switch to the backup server manually using the MetaTrader 5 Administrator, because you will not be able to connect to the server. Managing other cluster components will also be impossible. The system of [automatic switching to the backup server](/en/docs/mt5/platform/components/backup_server/backup_server_switch#auto) allows avoiding such a situation. However, if the system was not enabled, you will need to recover the server manually:

1\. Go to the computer where the main trade server is installed, and stop the system service if it runs. The default name of the main trade server service is mt5tmsrv. It can be stopped in the Control Panel — Administrative Tools — Services, as well as using the command line:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">net&nbsp;stop&nbsp;mt5tmsrv</span><br><span class="f_CodeExample">or</span><br><span class="f_CodeExample">D:\MetaTrader&nbsp;5&nbsp;Platform\Main&nbsp;Trade\mt5trade64.exe&nbsp;/stop.</span></p></td></tr></tbody></table>

If the computer is down (is unavailable), skip this step. However, once the computer is back up, please make sure that the old trade server service has not been restarted.

2\. Go to the computer where the backup server is installed, and stop the system service. The default name of the backup server service is mt5bsrv. It can also be stopped using the Control Panel or the command line:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">net&nbsp;stop&nbsp;mt5bsrv</span><br><span class="f_CodeExample">or</span><br><span class="f_CodeExample">D:\MetaTrader&nbsp;5&nbsp;Platform\Backup&nbsp;Main&nbsp;Trade\mt5backup64.exe&nbsp;/stop.</span></p></td></tr></tbody></table>

3\. Run the backup server file from the command line with the /gui parameter. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">D:\MetaTrader&nbsp;5&nbsp;Platform\Backup&nbsp;Main&nbsp;Trade\mt5backup64.exe&nbsp;/gui.</span></p></td></tr></tbody></table>

Click Restore in the window that appears.

![Server Configuration](/en/docs/mt5/platform/img/backup_server_gui.png "Server Configuration")

After that, the recovery process is started. Other components of the cluster will automatically switch to the new main server.

![Restoring Main Trade Server](/en/docs/mt5/platform/img/restore_main_server.png "Restoring Main Trade Server")

The process of restoring is run automatically in several steps:

-   Configuring Main Trader Server  
    At this stage, the IP address and port of the main server are replaced with those of the backup server, which are displayed in the upper part of the window. [The password and identifier](/en/docs/mt5/platform/administration/admin_network/network_add_edit#identifier) are not changed.
-   Installing Main Trade Server service
-   Uninstalling Backup Server service
-   Starting Main Trade Server service

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Before you launch the backup server, make sure the main server is stopped. Otherwise, your clients may start working with different servers. For example, your main server and access server are located at the same provider. The provider has issues with the internet connection and the servers became unavailable. The backup server is deployed in this case. After a while, connection to the main server is restored causing two servers to work simultaneously. In this case, contact your provider and request the immediate disabling of the main server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If one of the stages cannot be completed, all the changes made during restoring will be rolled back.</span></li><li class="p_tableatten"><span class="f_tableatten">As soon as restoring is finished, it is recommended to setup a new <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server" class="topiclink">backup server</a>.</span></li></ul></td></tr></tbody></table>

After the recovery of the main trade server, you will be able to connect to the cluster via MetaTrader 5 Administrator. Other components can be switched to backup servers in a regular way through the interface. For example, if the history server was installed on the same machine, you can switch to the backup server by running the appropriate command in its context menu.

The described procedure can also be used to restore other servers, including additional trade servers and history server. When restoring servers, new configuration data will be sent to the main trade server. A restored server will connect to the cluster without additional settings, and you will be able to control it via MetaTrader 5 Administrator.

![Restoring History Server](/en/docs/mt5/platform/img/restore_history_server.png "Restoring History Server")

[Switching to Backup Server](/en/docs/mt5/platform/components/backup_server/backup_server_switch)

[SQL Export](/en/docs/mt5/platform/components/backup_server/sql_export)