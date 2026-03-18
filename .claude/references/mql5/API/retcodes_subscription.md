# Subscriptions

> Source: https://support.metaquotes.net/en/docs/mt5/api/retcodes_subscription

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
            -   [Successful completion](/en/docs/mt5/api/retcodes_successful)
            -   [Common errors](/en/docs/mt5/api/retcodes_common)
            -   [Authentication](/en/docs/mt5/api/retcodes_authentication)
            -   [Configuration Management](/en/docs/mt5/api/retcodes_configs)
            -   [User management](/en/docs/mt5/api/retcodes_clients)
            -   [Trade management](/en/docs/mt5/api/retcodes_trades)
            -   [Report Generation](/en/docs/mt5/api/retcodes_reports)
            -   [Price Data](/en/docs/mt5/api/retcodes_price_history)
            -   [Trade Requests](/en/docs/mt5/api/retcodes_trade_request)
            -   [Dealer](/en/docs/mt5/api/retcodes_dealer)
            -   [API](/en/docs/mt5/api/retcodes_api)
            -   [Messengers](/en/docs/mt5/api/retcodes_messenger)
            -   [Subscriptions](/en/docs/mt5/api/retcodes_subscription)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Return Codes](/en/docs/mt5/api/reference_retcodes)Subscriptions

# Subscriptions

This group of codes is returned by the server when working with [subscription configurations](/en/docs/mt5/api/config_subscription) and [databases](/en/docs/mt5/api/reference_subscription):

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Constant</span></p></th><th class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable">MT_RET_SUBS_NOT_FOUND</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">15000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_subscription/imtsubscription" class="topiclink">Subscription</a> not found.</span></p></td></tr><tr class="table"><td class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable">MT_RET_SUBS_NOT_FOUND_CFG</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">15001</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_subscription/imtconsubscription" class="topiclink">Subscription configuration</a> not found.</span></p></td></tr><tr class="table"><td class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable">MT_RET_SUBS_NOT_FOUND_USER</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">15002</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">User from subscription not found.</span></p></td></tr><tr class="table"><td class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable">MT_RET_SUBS_DISABLED</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">15003</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Subscription disabled. The current status can be obtained via <a href="/en/docs/mt5/api/reference_subscription/imtsubscription/imtsubscription_status" class="topiclink">IMTSubscription::Status</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable">MT_RET_SUBS_PERMISSION_USER</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">15004</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Subscription not allowed for the user.</span></p></td></tr><tr class="table"><td class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable">MT_RET_SUBS_PERMISSION_SUBSCRIBE</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">15005</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Subscription not allowed. The availability of a subscription option is determined by the <a href="/en/docs/mt5/api/config_subscription/imtconsubscription/imtconsubscription_controlmode" class="topiclink">IMTConSubscription::ControlMode</a> property.</span></p></td></tr><tr class="table"><td class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable">MT_RET_SUBS_PERMISSION_UNSUBSCRIBE</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">15006</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Unsubscribing not allowed. The ability to unsubscribe is determined by the <a href="/en/docs/mt5/api/config_subscription/imtconsubscription/imtconsubscription_controlmode" class="topiclink">IMTConSubscription::ControlMode</a> property.</span></p></td></tr><tr class="table"><td class="table" style="width:260px;"><p class="p_fortable"><span class="f_fortable">MT_RET_SUBS_REAL_ONLY</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">15007</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Subscription only allowed for real accounts.</span></p></td></tr></tbody></table>

[Messengers](/en/docs/mt5/api/retcodes_messenger)

[Structures](/en/docs/mt5/api/reference_structures)