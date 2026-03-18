# Users

> Source: https://support.metaquotes.net/en/docs/mt4/api/server_api/server_api_user

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
            -   [Development of Plugins](/en/docs/mt4/api/server_api/server_api_dev)
            -   [Common Functions](/en/docs/mt4/api/server_api/server_api_common)
            -   [Configuration Databases](/en/docs/mt4/api/server_api/server_api_config)
            -   [Users](/en/docs/mt4/api/server_api/server_api_user)
                -   [ClientsTotal](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientstotal)
                -   [ClientsAddUser](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsadduser)
                -   [ClientsDeleteUser](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsdeleteuser)
                -   [ClientsUserInfo](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsuserinfo)
                -   [ClientsUserUpdate](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsuserupdate)
                -   [ClientsCheckPass](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientscheckpass)
                -   [ClientsChangePass](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientschangepass)
                -   [ClientsChangeBalance](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientschangebalance)
                -   [ClientsChangeCredit](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientschangecredit)
                -   [ClientsAllUsers](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsallusers)
                -   [ClientsGroupsUsers](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsgroupsusers)
                -   [ClientsCheckBalance](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientscheckbalance)
            -   [Trading](/en/docs/mt4/api/server_api/server_api_trading)
            -   [Price Data](/en/docs/mt4/api/server_api/server_api_chart)
            -   [Mail, News and Notifications](/en/docs/mt4/api/server_api/server_api_mail_news)
            -   [Daily Reports](/en/docs/mt4/api/server_api/server_api_reference_daily)
            -   [Server Services](/en/docs/mt4/api/server_api/server_api_server_services)
            -   [Hooks](/en/docs/mt4/api/server_api/server_api_hook)
        -   [Manager API](/en/docs/mt4/api/manager_api)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Server API](/en/docs/mt4/api/server_api)Users

# Users

The MetaTrader 4 Server API allows managing a client base on a trade server. You can use the Server API to add and delete users, as well as edit their data.

The following functions are available for working with the client base:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientstotal" class="topiclink">ClientsTotal</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets the number of accounts in the client base.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsadduser" class="topiclink">ClientsAddUser</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Adds a client account.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsdeleteuser" class="topiclink">ClientsDeleteUser</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Deleting a client account based on the client's login.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsuserinfo" class="topiclink">ClientsUserInfo</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets the information about the client account by a login.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsuserupdate" class="topiclink">ClientsUserUpdate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Updates a client account.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientscheckpass" class="topiclink">ClientsCheckPass</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Check a client's password.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientschangepass" class="topiclink">ClientsChangePass</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Changes a client's password.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientschangebalance" class="topiclink">ClientsChangeBalance</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Conducts balance operations on a client's account.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientschangecredit" class="topiclink">ClientsChangeCredit</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Conducts credit operations on a client's account.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsallusers" class="topiclink">ClientsAllUsers</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets the list of all clients.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientsgroupsusers" class="topiclink">ClientsGroupsUsers</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives all client accounts from the specified client group.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientscheckbalance" class="topiclink">ClientsCheckBalance</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Checks and corrects client's balance based on the trading history.</span></p></td></tr></tbody></table>

[GatewayRulesShift](/en/docs/mt4/api/server_api/server_api_config/server_api_config_gateway/cserverinterface_gatewayrulesshift)

[ClientsTotal](/en/docs/mt4/api/server_api/server_api_user/cserverinterface_clientstotal)