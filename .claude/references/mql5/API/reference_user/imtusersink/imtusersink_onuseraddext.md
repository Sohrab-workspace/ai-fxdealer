# IMTUserSink::OnUserAddExt

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuseraddext

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
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
            -   [Trade](/en/docs/mt5/api/reference_trading)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
                -   [IMTUser](/en/docs/mt5/api/reference_user/imtuser)
                -   [IMTUserArray](/en/docs/mt5/api/reference_user/imtuserarray)
                -   [IMTUserSink](/en/docs/mt5/api/reference_user/imtusersink)
                    -   [OnUserAdd](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuseradd)
                    -   [OnUserAddExt](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuseraddext)
                    -   [OnUserUpdate](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserupdate)
                    -   [OnUserDelete](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserdelete)
                    -   [OnUserClean](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserclean)
                    -   [OnUserLogin](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserlogin)
                    -   [OnUserLoginExt](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserloginext)
                    -   [OnUserLogout](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserlogout)
                    -   [OnUserLogoutExt](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserlogoutext)
                    -   [OnUserChangePassword](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserchangepassword)
                    -   [OnUserSync](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onusersync)
                    -   [OnUserArchive](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserarchive)
                    -   [OnUserRestore](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserrestore)
                    -   [HookUserAdd](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuseradd)
                    -   [HookUserAddExt](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuseraddext)
                    -   [HookUserUpdate](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuserupdate)
                    -   [HookUserDelete](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuserdelete)
                    -   [HookUserLogin](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuserlogin)
                    -   [HookUserLoginExt](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuserloginext)
                    -   [HookUserChangePassword](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuserchangepassword)
                    -   [HookUserArchive](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuserarchive)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Users](/en/docs/mt5/api/reference_user)[IMTUserSink](/en/docs/mt5/api/reference_user/imtusersink)OnUserAddExt

# IMTUserSink::OnUserAddExt

An extended handler of a new account addition event. It additionally passes the passwords of the created account.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTUserSink::OnUserAddExt</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTUser*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;added&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">master_password</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Main&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">investor_password</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Investor&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

user

\[in\]  A pointer to the [IMTUser](/en/docs/mt5/api/reference_user/imtuser) added user object.

master\_password

\[in\]  The main password of the created account.

investor\_password

\[in\]  The investor password of the created account.

Note

The method is only used in the MetaTrader 5 Server API.

[OnUserAdd](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuseradd)

[OnUserUpdate](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuserupdate)