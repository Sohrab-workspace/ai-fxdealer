# IMTSubscription

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_subscription/imtsubscription

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Subscriptions](/en/docs/mt5/api/reference_subscription)IMTSubscription

# IMTSubscription

This interface provides access to a [trader's subscription parameters](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions/subscriptions_control).

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_release" class="topiclink">Release</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the current object.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_assign" class="topiclink">Assign</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a passed object to the current one.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_clear" class="topiclink">Clear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear an object.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_id" class="topiclink">ID</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get a unique subscription identifier.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_login" class="topiclink">Login</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the login of the client to whom the subscription belongs.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_subscription" class="topiclink">Subscription</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the subscription configuration identifier.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_status" class="topiclink">Status</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the subscription status.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_flags" class="topiclink">Flags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set additional subscription properties.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_timesubscribe" class="topiclink">TimeSubscribe</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the subscription start time.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_timerenewal" class="topiclink">TimeRenewal</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the last subscription renewal time.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_timeexpire" class="topiclink">TimeExpire</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get and set the subscription expiration time.</span></p></td></tr></tbody></table>

The IMTSubscription class contains the following enumerations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Enumeration</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_enum#enstatus" class="topiclink">EnStatus</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Possible subscription statuses.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_enum#enflags" class="topiclink">EnFlags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Flags for additional subscription properties.</span></p></td></tr></tbody></table>

[Subscriptions](/en/docs/mt5/api/reference_subscription)

[Enumerations](/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_enum)