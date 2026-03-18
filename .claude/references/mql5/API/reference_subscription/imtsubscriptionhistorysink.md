# IMTSubscriptionHistorySink

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink

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
                -   [IMTSubscriptionArray](/en/docs/mt5/api/reference_subscription/imtsubscriptionarray)
                -   [IMTSubscriptionHistory](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistory)
                -   [IMTSubscriptionHistoryArray](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistoryarray)
                -   [IMTSubscriptionSink](/en/docs/mt5/api/reference_subscription/imtsubscriptionsink)
                -   [IMTSubscriptionHistorySink](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink)
                    -   [OnSubscriptionHistoryAdd](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink/imtsubscriptionhistorysink_onsubscriptionhistoryadd)
                    -   [OnSubscriptionHistoryUpdate](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink/imtsubscriptionhistorysink_onsubscriptionhistoryupdate)
                    -   [OnSubscriptionHistoryDelete](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink/imtsubscriptionhistorysink_onsubscriptionhistorydelete)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Subscriptions](/en/docs/mt5/api/reference_subscription)IMTSubscriptionHistorySink

# IMTSubscriptionHistorySink

The IMTSubscriptionHistorySink class contains event handlers related to changes in the subscription action database.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:180px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:180px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink/imtsubscriptionhistorysink_onsubscriptionhistoryadd" class="topiclink">OnSubscriptionHistoryAdd</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Event handler for adding a subscription action to the database.</span></p></td></tr><tr class="table"><td class="table" style="width:180px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink/imtsubscriptionhistorysink_onsubscriptionhistoryupdate" class="topiclink">OnSubscriptionHistoryUpdate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Subscription action change event handler.</span></p></td></tr><tr class="table"><td class="table" style="width:180px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink/imtsubscriptionhistorysink_onsubscriptionhistorydelete" class="topiclink">OnSubscriptionHistoryDelete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Event handler for deleting a subscription action from the database.</span></p></td></tr></tbody></table>

[OnSubscriptionCancel](/en/docs/mt5/api/reference_subscription/imtsubscriptionsink/imtsubscriptionsink_onsubscriptioncancel)

[OnSubscriptionHistoryAdd](/en/docs/mt5/api/reference_subscription/imtsubscriptionhistorysink/imtsubscriptionhistorysink_onsubscriptionhistoryadd)