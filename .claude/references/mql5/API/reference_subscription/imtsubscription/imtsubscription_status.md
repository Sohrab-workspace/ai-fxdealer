# IMTSubscription::Status

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_status

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
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
                -   [IMTSubscription](/en/docs/mt5/api/reference_subscription/imtsubscription)
                    -   [Enumerations](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_enum)
                    -   [Release](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_release)
                    -   [Assign](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_assign)
                    -   [Clear](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_clear)
                    -   [ID](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_id)
                    -   [Login](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_login)
                    -   [Subscription](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_subscription)
                    -   [Status](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_status)
                    -   [Flags](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_flags)
                    -   [TimeSubscribe](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_timesubscribe)
                    -   [TimeRenewal](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_timerenewal)
                    -   [TimeExpire](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_timeexpire)
                -   [IMTSubscriptionArray](/en/docs/mt5/api/reference_subscription/imtsubscriptionarray)
                -   [IMTSubscriptionHistory](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistory)
                -   [IMTSubscriptionHistoryArray](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistoryarray)
                -   [IMTSubscriptionSink](/en/docs/mt5/api/reference_subscription/imtsubscriptionsink)
                -   [IMTSubscriptionHistorySink](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Subscriptions](/en/docs/mt5/api/reference_subscription)[IMTSubscription](/en/docs/mt5/api/reference_subscription/imtsubscription)Status

# IMTSubscription::Status

Get the subscription status.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">UINT&nbsp;&nbsp;</span><span class="f_Functions">IMTSubscription::Status</span><span class="f_CodeExample">()</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">uint&nbsp;&nbsp;</span><span class="f_Functions">CIMTSubscription.Status</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Return Value

[IMTSubscription::EnStatus](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_enum#enstatus) enumeration values.

# IMTSubscription::Status

Set the subscription status.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTSubscription::Status</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">state</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Subscription&nbsp;status</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTSubscription.Status</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">state</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Subscription&nbsp;status</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

state

\[in\]  Subscription status. To pass the status, use the [IMTSubscription::EnStatus](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_enum#enstatus) enumeration.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred corresponding to the response code.

[Subscription](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_subscription)

[Flags](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_flags)