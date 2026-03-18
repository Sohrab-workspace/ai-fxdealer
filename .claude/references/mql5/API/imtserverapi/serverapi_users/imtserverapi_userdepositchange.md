# IMTServerAPI::UserDepositChange

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userdepositchange

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
            -   [Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)
            -   [Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)
            -   [Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)
            -   [Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)
            -   [Hooks](/en/docs/mt5/api/serverapi_hooks)
            -   [Request Processing on the Server](/en/docs/mt5/api/hook_scheme)
            -   [Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)
            -   [Debugging](/en/docs/mt5/api/serverapi_debug)
            -   [Ready-made Examples](/en/docs/mt5/api/serverapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reference_entrypoints)
            -   [Plugin Interface](/en/docs/mt5/api/imtserverplugin)
            -   [Main API Interface](/en/docs/mt5/api/imtserverapi)
                -   [Common Functions](/en/docs/mt5/api/imtserverapi/serverapi_common)
                -   [Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)
                -   [Clients](/en/docs/mt5/api/imtserverapi/serverapi_clients)
                -   [Users](/en/docs/mt5/api/imtserverapi/serverapi_users)
                    -   [UserCreate](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_usercreate)
                    -   [UserCreateAccount](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_usercreateaccount)
                    -   [UserSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_usersubscribe)
                    -   [UserUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userunsubscribe)
                    -   [UserAdd](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_useradd)
                    -   [UserDelete](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userdelete)
                    -   [UserUpdate](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userupdate)
                    -   [UserTotal](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_usertotal)
                    -   [UserGet](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userget)
                    -   [UserGroup](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_usergroup)
                    -   [UserLogins](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userlogins)
                    -   [UserPasswordCheck](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userpasswordcheck)
                    -   [UserPasswordChange](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userpasswordchange)
                    -   [UserDepositChange](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userdepositchange)
                    -   [UserDepositChangeRaw](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userdepositchangeraw)
                    -   [UserArchive](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userarchive)
                    -   [UserArchiveGet](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userarchiveget)
                    -   [UserArchiveLogins](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userarchivelogins)
                    -   [UserRestore](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userrestore)
                    -   [NotificationsSend](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_notificationssend)
                    -   [UserAccountGet](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_useraccountget)
                -   [Online Connections](/en/docs/mt5/api/imtserverapi/serverapi_online)
                -   [Certificates](/en/docs/mt5/api/imtserverapi/serverapi_certificate)
                -   [Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)
                -   [History Data](/en/docs/mt5/api/imtserverapi/serverapi_chart)
                -   [Tick Data](/en/docs/mt5/api/imtserverapi/serverapi_ticks)
                -   [Depth of Market](/en/docs/mt5/api/imtserverapi/serverapi_book)
                -   [Mail Database](/en/docs/mt5/api/imtserverapi/serverapi_mail)
                -   [News Database](/en/docs/mt5/api/imtserverapi/serverapi_news)
                -   [Daily Reports](/en/docs/mt5/api/imtserverapi/serverapi_trading_daily)
                -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_subscription)
                -   [Server Services](/en/docs/mt5/api/imtserverapi/serverapi_server_services)
                -   [Geo Services](/en/docs/mt5/api/imtserverapi/serverapi_geo)
                -   [Dataset](/en/docs/mt5/api/imtserverapi/serverapi_dataset)
                -   [Custom Functions](/en/docs/mt5/api/imtserverapi/serverapi_custom)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
            -   [Interface of End-of-Day Events](/en/docs/mt5/api/imtendofdaysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Users](/en/docs/mt5/api/imtserverapi/serverapi_users)UserDepositChange

# IMTServerAPI::UserDepositChange

Conduct balance operation on a user account.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::UserDepositChange</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;User's&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;double</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">value</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Amount</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">action</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Type&nbsp;of&nbsp;action</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">comment</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Comment</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT64&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal_id</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Deal&nbsp;ID</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\]  The login of a user, on whose account the balance operation is be conducted.

value

\[in\]  The amount to add to an account or subtract from it. A positive value means that funds will be added, a negative value means withdrawal.

action

\[in\]  Type of the balance operation. The type is specified using the following values of the [IMTDeal::EnDealAction](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_enum#endealaction) enumeration:

-   DEAL\_BALANCE — a balance operation.

-   DEAL\_CREDIT — a credit operation.
-   DEAL\_CHARGE — additional adding/withdrawing.
-   DEAL\_CORRECTION — corrective operations.
-   DEAL\_BONUS — adding bonuses.
-   DEAL\_COMMISSION — charging commissions.

comment

\[in\]  A comment to a balance operation. The maximum comment length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

deal\_id

\[out\]  The ID of the deal in which a balance operation was executed.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, a corresponding error code will be returned.

Note

Operations with deposit are represented as deals. The ID of the deal in which a balance operation was executed.

In case the deal type is incorrect, the code [MT\_RET\_ERR\_PARAMS](/en/docs/mt5/api/retcodes_common) is returned.

An amount of money accrued/withdrawn with a single operation cannot exceed 1000000000. In case this value is exceeded, the code [MT\_RET\_TRADE\_MAX\_MONEY](/en/docs/mt5/api/retcodes_trades) is returned.

An amount of withdrawal cannot exceed the current free margin (regardless of the balance operation type). In case this amount is exceeded the code [MT\_RET\_REQUEST\_NO\_MONEY](/en/docs/mt5/api/retcodes_trade_request) is returned.

An amount of withdrawal during a credit operation (TYPE=IMTDeal::DEAL\_CREDIT) cannot exceed the amount of previously issued credit assets. In case this amount is exceeded the code [MT\_RET\_REQUEST\_NO\_MONEY](/en/docs/mt5/api/retcodes_trade_request) is returned.

An amount of withdrawal during any balance operation cannot exceed the current balance. In case this amount is exceeded the code [MT\_RET\_REQUEST\_NO\_MONEY](/en/docs/mt5/api/retcodes_trade_request) is returned.

Balance operations can also be conducted by sending [IMTRequest::TA\_DEALER\_BALANCE](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum) type requests to the requests queue using the [IMTServerAPI::TradeRequest](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_traderequest) method.

The method cannot be called from trade event handlers and hooks. For example, from [IMTDealSink::OnDealUpdate](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealupdate).

[UserPasswordChange](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userpasswordchange)

[UserDepositChangeRaw](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userdepositchangeraw)