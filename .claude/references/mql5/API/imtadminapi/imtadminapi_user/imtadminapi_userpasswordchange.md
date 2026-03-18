# IMTAdminAPI::UserPasswordChange

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userpasswordchange

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
                -   [Common Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_common)
                -   [Connection to the Server](/en/docs/mt5/api/imtadminapi/imtadminapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtadminapi/imtadminapi_network)
                -   [Server Management](/en/docs/mt5/api/imtadminapi/imtadminapi_server_manage)
                -   [Configuration Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_config)
                -   [Clients](/en/docs/mt5/api/imtadminapi/imtadminapi_clients)
                -   [Users](/en/docs/mt5/api/imtadminapi/imtadminapi_user)
                    -   [Enumerations](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_user_enum)
                    -   [UserCreate](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_usercreate)
                    -   [UserCreateArray](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_usercreatearray)
                    -   [UserAdd](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_useradd)
                    -   [UserDelete](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userdelete)
                    -   [UserDeleteBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userdeletebatch)
                    -   [UserUpdate](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userupdate)
                    -   [UserUpdateBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userupdatebatch)
                    -   [UserUpdateBatchArray](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userupdatebatcharray)
                    -   [UserRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userrequest)
                    -   [UserRequestArray](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userrequestarray)
                    -   [UserRequestByLogins](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userrequestbylogins)
                    -   [UserPasswordCheck](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userpasswordcheck)
                    -   [UserPasswordChange](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userpasswordchange)
                    -   [UserCertCreate](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_usercertcreate)
                    -   [UserCertUpdate](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_usercertupdate)
                    -   [UserCertGet](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_usercertget)
                    -   [UserCertDelete](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_usercertdelete)
                    -   [UserCertConfirm](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_usercertconfirm)
                    -   [UserArchive](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userarchive)
                    -   [UserArchiveBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userarchivebatch)
                    -   [UserArchiveRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userarchiverequest)
                    -   [UserArchiveRequestArray](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userarchiverequestarray)
                    -   [UserArchiveRequestByLogins](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userarchiverequestbylogins)
                    -   [UserBackupRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userbackuprequest)
                    -   [UserBackupRequestArray](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userbackuprequestarray)
                    -   [UserBackupRequestByLogins](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userbackuprequestbylogins)
                    -   [UserBackupList](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userbackuplist)
                    -   [UserRestore](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userrestore)
                    -   [UserRestoreBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userrestorebatch)
                    -   [UserRestoreBatchArray](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userrestorebatcharray)
                    -   [UserBalanceCheck](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userbalancecheck)
                    -   [UserBalanceCheckBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userbalancecheckbatch)
                    -   [UserExternalRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userexternalrequest)
                    -   [UserExternalSync](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userexternalsync)
                    -   [UserLogins](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userlogins)
                    -   [NotificationsSend](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_notificationssend)
                -   [Trade Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_trading)
                -   [Mail Database](/en/docs/mt5/api/imtadminapi/imtadminapi_mail)
                -   [News Database](/en/docs/mt5/api/imtadminapi/imtadminapi_news)
                -   [History Data](/en/docs/mt5/api/imtadminapi/imtadminapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtadminapi/imtadminapi_tick)
                -   [Settings Files](/en/docs/mt5/api/imtadminapi/imtadminapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtadminapi/imtadminapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_custom)
                -   [ECN](/en/docs/mt5/api/imtadminapi/imtadminapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtadminapi/imtadminapi_geo)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Administrator Interface](/en/docs/mt5/api/imtadminapi)[Users](/en/docs/mt5/api/imtadminapi/imtadminapi_user)UserPasswordChange

# IMTAdminAPI::UserPasswordChange

Change the user's password.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTAdminAPI::UserPasswordChange</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">type</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Type&nbsp;of&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;User's&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">password</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;New&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTAdminAPI.UserPasswordChange</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">EnUsersPasswords</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">type</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Type&nbsp;of&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;User's&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">password</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;New&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">AdminAPI.UserPasswordChange</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">type</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Type&nbsp;of&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;User's&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">password</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;New&nbsp;password</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

type

\[in\]  The type of a password to change is specified using the [IMTUser::EnUsersPasswords](/en/docs/mt5/api/reference_user/imtuser/imtuser_enum#enuserspasswords) enumeration.

login

\[in\]  The login of a user whose password should be changed.

password

\[in\]  A new password. The password must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj. The minimum password length is determined by group settings ([IMTConGroup::AuthPasswordMin](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_authpasswordmin)), while the lowest possible value is 8 characters. The maximum length is 16 characters.

Return Value

An indication of a successful execution is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, a corresponding error code will be returned.

[UserPasswordCheck](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userpasswordcheck)

[UserCertCreate](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_usercertcreate)