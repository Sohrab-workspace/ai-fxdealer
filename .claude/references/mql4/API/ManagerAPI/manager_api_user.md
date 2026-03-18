# Users

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_user

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
            -   [Trading](/en/docs/mt4/api/manager_api/manager_api_trade)
            -   [Dealings](/en/docs/mt4/api/manager_api/manager_api_dealer)
            -   [Users](/en/docs/mt4/api/manager_api/manager_api_user)
                -   [AdmUsersRequest](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admusersrequest)
                -   [AdmBalanceCheck](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admbalancecheck)
                -   [AdmBalanceFix](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admbalancefix)
                -   [UsersRequest](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersrequest)
                -   [UserRecordsRequest](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordsrequest)
                -   [UserRecordNew](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordnew)
                -   [UserRecordUpdate](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordupdate)
                -   [UsersGroupOp](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersgroupop)
                -   [UserPasswordCheck](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userpasswordcheck)
                -   [UserPasswordSet](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userpasswordset)
                -   [UsersGet](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersget)
                -   [UserRecordGet](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordget)
                -   [UsersSyncStart](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userssyncstart)
                -   [UsersSyncRead](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userssyncread)
                -   [UsersSnapshot](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userssnapshot)
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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Users

# Users

The MetaTrader 4 Manager API allows managing a database of clients on a trade server. You can use the Server API to add and delete users, as well as edit their data.

The following functions are available for working with the client base:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admusersrequest" class="topiclink">AdmUsersRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Requests client records in accordance with the specified group or login.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admbalancecheck" class="topiclink">AdmBalanceCheck</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Checks clients' balance based on the trading history.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admbalancefix" class="topiclink">AdmBalanceFix</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Corrects clients' balance based on the trading history.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersrequest" class="topiclink">UsersRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives all client records.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordsrequest" class="topiclink">UserRecordsRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives client records in accordance with a list of logins.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordnew" class="topiclink">UserRecordNew</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Creates a client record.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordupdate" class="topiclink">UserRecordUpdate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Updates a client record.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersgroupop" class="topiclink">UsersGroupOp</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Conducting group operations to change the group and leverage of client records.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userpasswordcheck" class="topiclink">UserPasswordCheck</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Checks the master password of an account.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userpasswordset" class="topiclink">UserPasswordSet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Changes a client's password.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersget" class="topiclink">UsersGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives all client records in pumping.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordget" class="topiclink">UserRecordGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets a client record by the login in the pumping mode.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userssyncstart" class="topiclink">UsersSyncStart</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Method for internal use only. Should not be used in the development of custom applications.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userssyncread" class="topiclink">UsersSyncRead</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Method for internal use only. Should not be used in the development of custom applications.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userssnapshot" class="topiclink">UsersSnapshot</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives the list client logins available to the manager.</span></p></td></tr></tbody></table>

[DealerReset](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerreset)

[AdmUsersRequest](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admusersrequest)