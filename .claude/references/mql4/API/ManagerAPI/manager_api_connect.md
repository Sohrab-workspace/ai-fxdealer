# Connecting to the Server

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_connect

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
                -   [Connect](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_connect)
                -   [Disconnect](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_disconnect)
                -   [IsConnected](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_isconnected)
                -   [Login](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_login)
                -   [LoginSecured](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_loginsecured)
                -   [KeysSend](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_keyssend)
                -   [Ping](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_ping)
                -   [PasswordChange](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_passwordchange)
                -   [ManagerRights](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_managerrights)
            -   [Configuration Databases](/en/docs/mt4/api/manager_api/manager_api_config)
            -   [Server Management](/en/docs/mt4/api/manager_api/manager_api_server)
            -   [Price Data](/en/docs/mt4/api/manager_api/manager_api_chart)
            -   [Data Feeds](/en/docs/mt4/api/manager_api/manager_api_feeder)
            -   [Backup](/en/docs/mt4/api/manager_api/manager_api_backup)
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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Connecting to the Server

# Connecting to the Server

This section describes methods used for application connection and disconnection with the server.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_connect" class="topiclink">Connect</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_dev#connect" class="topiclink">Connection</a> to a trading server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_disconnect" class="topiclink">Disconnect</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_dev#connect" class="topiclink">Disconnects</a> from a trading server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_isconnected" class="topiclink">IsConnected</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Checks the state of <a href="/en/docs/mt4/api/manager_api/manager_api_dev#connect" class="topiclink">connection</a> to a trading server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_login" class="topiclink">Login</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_dev#connect" class="topiclink">Authentication</a> on the trading server using a manager account.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_loginsecured" class="topiclink">LoginSecured</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Sends an RSA key to a trading server while authorizing in the extended mode. The method is obsolete and not used.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_keyssend" class="topiclink">KeysSend</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Sends a public key to a trading serer for the generation of an RSA key. It is used for extended authentication. The method is obsolete and not used.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_ping" class="topiclink">Ping</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Sends a request to the trading server to test and maintain the connection of the Manager interface with the trading server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_passwordchange" class="topiclink">PasswordChange</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Changes the password for the manager account, which is used for the current connection to the trading server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_managerrights" class="topiclink">ManagerRights</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Gets the description of the permissions of the manager account, which is used for the current connection to the trading server.</span></p></td></tr></tbody></table>

[LicenseCheck](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_licensecheck)

[Connect](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_connect)