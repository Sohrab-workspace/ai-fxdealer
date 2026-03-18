# IMTManagerAPI::SubscriptionHistoryRequestByLogins

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryrequestbylogins

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
                    -   [SubscriptionCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptioncreate)
                    -   [SubscriptionCreateArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptioncreatearray)
                    -   [SubscriptionJoin](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionjoin)
                    -   [SubscriptionJoinBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionjoinbatch)
                    -   [SubscriptionCancel](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptioncancel)
                    -   [SubscriptionCancelBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptioncancelbatch)
                    -   [SubscriptionUpdate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionupdate)
                    -   [SubscriptionUpdateBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionupdatebatch)
                    -   [SubscriptionUpdateBatchArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionupdatebatcharray)
                    -   [SubscriptionDelete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptiondelete)
                    -   [SubscriptionDeleteBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptiondeletebatch)
                    -   [SubscriptionRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionrequest)
                    -   [SubscriptionRequestByID](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionrequestbyid)
                    -   [SubscriptionRequestByIDs](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionrequestbyids)
                    -   [SubscriptionRequestByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionrequestbygroup)
                    -   [SubscriptionRequestByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionrequestbylogins)
                    -   [SubscriptionHistoryCreate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistorycreate)
                    -   [SubscriptionHistoryCreateArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistorycreatearray)
                    -   [SubscriptionHistoryUpdate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryupdate)
                    -   [SubscriptionHistoryUpdateBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryupdatebatch)
                    -   [SubscriptionHistoryUpdateBatchArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryupdatebatcharray)
                    -   [SubscriptionHistoryDelete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistorydelete)
                    -   [SubscriptionHistoryDeleteBatch](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistorydeletebatch)
                    -   [SubscriptionHistoryRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryrequest)
                    -   [SubscriptionHistoryRequestByID](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryrequestbyid)
                    -   [SubscriptionHistoryRequestByIDs](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryrequestbyids)
                    -   [SubscriptionHistoryRequestByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryrequestbygroup)
                    -   [SubscriptionHistoryRequestByLogins](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryrequestbylogins)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Subscriptions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription)SubscriptionHistoryRequestByLogins

# IMTManagerAPI::SubscriptionHistoryRequestByLogins

Request subscription actions from the server by a list of logins.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::SubscriptionHistoryRequestByLogins</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">logins</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Logins</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">logins_total</span><span class="f_CodeExample">,&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;logins</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">from</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Period&nbsp;start</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;INT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">to</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Period&nbsp;end</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTSubscriptionHistoryArray*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">records</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Action&nbsp;array&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.SubscriptionHistoryRequestByLogins</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong[]</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">logins</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Logins</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">long</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">from</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Period&nbsp;start</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">long</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">to</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Period&nbsp;end</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTSubscriptionHistoryArray</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">records</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Action&nbsp;array&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

logins

\[in\]  Array of client logins.

logins\_total

\[in\]  Number of logins in the 'logins' array.

from

\[in\]  The beginning of the period for which you need to get actions. The date is specified in seconds since 01.01.1970.

to

\[in\]  The end of the period for which you need to get actions. The date is specified in seconds since 01.01.1970.

records

\[out\]  Object of an [array of subscription actions](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistoryarray). The 'records' object must be pre-created by the [IMTManagerAPI::SubscriptionHistoryCreateArray](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistorycreatearray) method.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

The method cannot be called from event handlers (any IMT\*Sink class methods).

[SubscriptionHistoryRequestByGroup](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription/imtmanagerapi_subscriptionhistoryrequestbygroup)

[Custom Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom)