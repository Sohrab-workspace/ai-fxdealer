# IMTManagerAPI::UserAdd

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useradd

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Users](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user)UserAdd

# IMTManagerAPI::UserAdd

Add a client record.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::UserAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTUser*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">master_pass</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;master&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">investor_pass</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;investor&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.UserAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTUser</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">master_pass</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;master&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">investor_pass</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;investor&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.UserAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;client&nbsp;record</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">master_pass</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;The&nbsp;master&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">investor_pass</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;The&nbsp;investor&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

user

\[in\]\[out\]  An object of the client record.

master\_pass

\[in\]  The master password of an account. The password must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj. The minimum password length is determined by group settings ([IMTConGroup::AuthPasswordMin](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_authpasswordmin)), while the lowest possible value is 8 characters. The maximum length is 16 characters.

investor\_pass

\[in\]  The investor password of an account. The password must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj. The minimum password length is determined by group settings ([IMTConGroup::AuthPasswordMin](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_authpasswordmin)), while the lowest possible value is 8 characters. The maximum length is 16 characters.

Return Value

An indication of a successful execution is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, a corresponding error code will be returned.

Note

In case no login is specified for a record (is equal to 0), the server will automatically allocate a login from the available range and will assign it to the user record. In case there are no more available ranges of logins, the [MT\_RET\_USR\_LOGIN\_EXHAUSTED](/en/docs/mt5/api/retcodes_clients) error is returned.

The following parameters must be filled in the user record you are adding: [IMTUser::Group](/en/docs/mt5/api/reference_user/imtuser/imtuser_group) and [IMTUser::Leverage](/en/docs/mt5/api/reference_user/imtuser/imtuser_leverage), as well as [IMTUser::FirstName](/en/docs/mt5/api/reference_user/imtuser/imtuser_firstname) or [IMTUser::LastName](/en/docs/mt5/api/reference_user/imtuser/imtuser_lastname). To allow an account to be used in client terminals, enable the [IMTUser::USER\_RIGHT\_ENABLED](/en/docs/mt5/api/reference_user/imtuser/imtuser_enum#enusersrights) right for that account.

When calling the method, a check is made whether the entry already exists. If the account already exists, the [MT\_RET\_USR\_LOGIN\_EXIST](/en/docs/mt5/api/retcodes_clients) error is returned. A key field for comparison is the user login [IMTUser::Login](/en/docs/mt5/api/reference_user/imtuser/imtuser_login).

A user can be added on a trade server only from the applications that run in the same trade server. For all other applications the response code [MT\_RET\_USR\_LOGIN\_PROHIBITED](/en/docs/mt5/api/retcodes_clients) will be returned.

Before adding, the correctness of the record is checked. If the record is incorrect, the error code [MT\_RET\_ERR\_PARAMS](/en/docs/mt5/api/retcodes_common) is returned.

[UserUnsubscribe](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userunsubscribe)

[UserDelete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userdelete)