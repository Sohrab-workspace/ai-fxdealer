# Backup

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_backup

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
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
        -   [Development Features](/en/docs/mt4/api/features)
        -   [Structures](/en/docs/mt4/api/reference_structures)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
        -   [Manager API](/en/docs/mt4/api/manager_api)
            -   [Application Development](/en/docs/mt4/api/manager_api/manager_api_dev)
            -   [Exported Functions and Factory](/en/docs/mt4/api/manager_api/manager_api_exported_factory)
            -   [Common Functions](/en/docs/mt4/api/manager_api/manager_api_common)
            -   [Connecting to the Server](/en/docs/mt4/api/manager_api/manager_api_connect)
            -   [Configuration Databases](/en/docs/mt4/api/manager_api/manager_api_config)
            -   [Server Management](/en/docs/mt4/api/manager_api/manager_api_server)
            -   [Price Data](/en/docs/mt4/api/manager_api/manager_api_chart)
            -   [Data Feeds](/en/docs/mt4/api/manager_api/manager_api_feeder)
            -   [Backup](/en/docs/mt4/api/manager_api/manager_api_backup)
                -   [BackupInfoUsers](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backupinfousers)
                -   [BackupInfoOrders](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backupinfoorders)
                -   [BackupRequestUsers](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprequestusers)
                -   [BackupRequestOrders](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprequestorders)
                -   [BackupRestoreUsers](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprestoreusers)
                -   [BackupRestoreOrders](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprestoreorders)
            -   [Trading](/en/docs/mt4/api/manager_api/manager_api_trade)
            -   [Dealings](/en/docs/mt4/api/manager_api/manager_api_dealer)
            -   [Users](/en/docs/mt4/api/manager_api/manager_api_user)
            -   [Online Connections](/en/docs/mt4/api/manager_api/manager_api_online)
            -   [Symbols](/en/docs/mt4/api/manager_api/manager_api_symbol)
            -   [Mail, News and Notifications](/en/docs/mt4/api/manager_api/manager_api_newsmail)
            -   [Reports](/en/docs/mt4/api/manager_api/manager_api_report)
            -   [Summary Positions](/en/docs/mt4/api/manager_api/manager_api_summary)
            -   [Exposure](/en/docs/mt4/api/manager_api/manager_api_exposure)
            -   [Protocol Extension](/en/docs/mt4/api/manager_api/manager_api_extension)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Backup

# Backup

The MetaTrader 4 Manager API allows working with backup databases of accounts and orders on the server.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backupinfousers" class="topiclink">BackupInfoUsers</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives information about backup databases of users available on the server.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backupinfoorders" class="topiclink">BackupInfoOrders</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives information about backup databases of orders available on the server.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprequestusers" class="topiclink">BackupRequestUsers</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Requests accounts from a backup.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprequestorders" class="topiclink">BackupRequestOrders</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Requests orders from a backup.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprestoreusers" class="topiclink">BackupRestoreUsers</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Recovers accounts from a backup.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprestoreorders" class="topiclink">BackupRestoreOrders</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Recovers orders from a backup.</span></p></td></tr></tbody></table>

[SrvFeedsRestart](/en/docs/mt4/api/manager_api/manager_api_feeder/cmanagerinterface_srvfeedsrestart)

[BackupInfoUsers](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backupinfousers)