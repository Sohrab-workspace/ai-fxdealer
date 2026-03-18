# IMTManagerAPI::UserGet

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userget

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
            -   [Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)
            -   [Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)
            -   [Getting Started](/en/docs/mt5/api/managerapi_preparing)
            -   [Ready-made Examples](/en/docs/mt5/api/managerapi_examples)
            -   [.NET Implementation](/en/docs/mt5/api/managerapi_net)
            -   [Python Implementation](/en/docs/mt5/api/managerapi_python)
            -   [Exported Functions](/en/docs/mt5/api/managerapi_exported)
            -   [CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)
            -   [Administrator Interface](/en/docs/mt5/api/imtadminapi)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
                -   [Common Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common)
                -   [Connection to the Server](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_network)
                -   [Configuration Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_config)
                -   [Selected Symbols](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected)
                -   [Clients](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_clients)
                -   [Users](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user)
                    -   [Enumerations](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_user_enum)
                    -   [UserCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercreate)
                    -   [UserCreateArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercreatearray)
                    -   [UserCreateAccount](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercreateaccount)
                    -   [UserCreateAccountArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercreateaccountarray)
                    -   [UserSubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usersubscribe)
                    -   [UserUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userunsubscribe)
                    -   [UserAdd](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useradd)
                    -   [UserDelete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userdelete)
                    -   [UserDeleteBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userdeletebatch)
                    -   [UserUpdate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userupdate)
                    -   [UserUpdateBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userupdatebatch)
                    -   [UserUpdateBatchArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userupdatebatcharray)
                    -   [UserTotal](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usertotal)
                    -   [UserGet](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userget)
                    -   [UserGetByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usergetbygroup)
                    -   [UserGetByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usergetbylogins)
                    -   [UserRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userrequest)
                    -   [UserRequestArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userrequestarray)
                    -   [UserRequestByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userrequestbylogins)
                    -   [UserGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usergroup)
                    -   [UserLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userlogins)
                    -   [UserPasswordCheck](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userpasswordcheck)
                    -   [UserPasswordChange](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userpasswordchange)
                    -   [UserCertCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercertcreate)
                    -   [UserCertUpdate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercertupdate)
                    -   [UserCertGet](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercertget)
                    -   [UserCertDelete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercertdelete)
                    -   [UserCertConfirm](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercertconfirm)
                    -   [UserAccountSubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useraccountsubscribe)
                    -   [UserAccountUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useraccountunsubscribe)
                    -   [UserAccountGet](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useraccountget)
                    -   [UserAccountGetByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useraccountgetbygroup)
                    -   [UserAccountGetByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useraccountgetbylogins)
                    -   [UserAccountRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useraccountrequest)
                    -   [UserAccountRequestByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useraccountrequestbylogins)
                    -   [UserAccountRequestArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useraccountrequestarray)
                    -   [UserExternalGet](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userexternalget)
                    -   [UserExternalRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userexternalrequest)
                    -   [UserExternalSync](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userexternalsync)
                    -   [UserBalanceCheck](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userbalancecheck)
                    -   [UserBalanceCheckBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userbalancecheckbatch)
                    -   [NotificationsSend](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_notificationssend)
                    -   [EmailSend](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_emailsend)
                    -   [MessengerVerifyPhone](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_messengerverifyphone)
                    -   [MessengerSend](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_messengersend)
                -   [Online Connections](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_online)
                -   [Trade Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading)
                -   [History Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick)
                -   [Mail Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_mail)
                -   [News Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_news)
                -   [Trade Activity](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations)
                -   [Market Depth](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_book)
                -   [Summary Positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_summary)
                -   [Exposure](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_exposure)
                -   [Daily Reports](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_daily)
                -   [Settings Files](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom)
                -   [ECN](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_geo)
            -   [Dealer Interface](/en/docs/mt5/api/imtdealersink)
            -   [Interface of Manager API Events](/en/docs/mt5/api/imtmanagersink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Users](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user)UserGet

# IMTManagerAPI::UserGet

Get a user by the login.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::UserGet</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Client&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTUser*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.UserGet</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Client&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTUser</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.UserGet</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">int</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Client&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\]  The login of a client.

user

\[out\]  An object of the client login. The user object must first be created using the [IMTManagerAPI::UserCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usercreate) method.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

This method copies the data of a client with the specified login to the user object. The method is valid only if the [IMTManagerAPI::PUMP\_MODE\_USERS](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_enpumpmodes) pumping mode was specified during connection.

[UserTotal](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usertotal)

[UserGetByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_usergetbygroup)