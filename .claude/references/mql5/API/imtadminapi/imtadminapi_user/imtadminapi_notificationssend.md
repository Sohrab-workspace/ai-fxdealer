# IMTAdminAPI::NotificationsSend

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_notificationssend

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Administrator Interface](/en/docs/mt5/api/imtadminapi)[Users](/en/docs/mt5/api/imtadminapi/imtadminapi_user)NotificationsSend

# IMTAdminAPI::NotificationsSend

Sends push-notifications to a list of MetaQuotes IDs.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTAdminAPI::NotificationsSend</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">metaquotest_ids</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;list&nbsp;of&nbsp;MetaQuotes&nbsp;IDs</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">message</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Message</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTAdminAPI.NotificationsSend</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">metaquotest_ids</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;list&nbsp;of&nbsp;MetaQuotes&nbsp;IDs</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">srting</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">message</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Message</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">AdminAPI.NotificationsSend</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">metaquotest_ids</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;The&nbsp;list&nbsp;of&nbsp;MetaQuotes&nbsp;IDs</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">message</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Message</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

metaquotes\_ids

\[in\]  A comma separated list of MetaQuotes IDs.

message

\[in\]  The text of the notification.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

Push notifications are personal messages sent over the Internet. They do not depend on the phone number or mobile network operator. Messages are delivered instantly; no need to run any applications on the receiver's device.

Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 5 Mobile for iPhone or Android.

The maximum message length is 1024 characters.

When sending to a list of MetaQuotes IDs, the company name from the Server License will be specified in the signature.

# IMTAdminAPI::NotificationsSend

Sends push-notifications to a list of logins.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTAdminAPI::NotificationsSend</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64*</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">logins</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Logins</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UNIT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">logins_total</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;logins</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">message</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Message</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTAdminAPI.NotificationsSend</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong[]</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">logins</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Logins</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">message</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Message</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">AdminAPI.NotificationsSend</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">logins</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Logins</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">message</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Message</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

logins

\[in\]  An array of logins.

logins\_total

\[in\]  The total number of logins in logins.

message

\[in\]  The text of the notification.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

Push notifications are personal messages sent over the Internet. They do not depend on the phone number or mobile network operator. Messages are delivered instantly; no need to run any applications on the receiver's device.

Messages are sent based on MetaQuotes ID, which is a unique user identifier. To obtain the ID, a user needs to install MetaTrader 5 Mobile for iPhone or Android.

The maximum message length is 1024 characters.

MetaQuotes ID must be specified in the settings of appropriate accounts ([IMTUser::MQID](/en/docs/mt5/api/reference_user/imtuser/imtuser_mqid)) in order to send messages by specifying logins.

If you send messages specifying logins, the signature will contain the name of the Owner company from the settings of the group, to which the accounts belong. Use this type for White Labels to add the correct company name in the signature.

[UserLogins](/en/docs/mt5/api/imtadminapi/imtadminapi_user/imtadminapi_userlogins)

[Trade Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_trading)