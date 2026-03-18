# Subscriptions

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/webapi_subscription

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
            -   [Getting Started](/en/docs/mt5/api/webapi_preparing)
            -   [Format of Commands](/en/docs/mt5/api/webapi_https)
            -   [Authentication](/en/docs/mt5/api/webapi_rest_authentication)
            -   [Escaping Special Characters](/en/docs/mt5/api/webapi_screening)
            -   [Maintaining Connections](/en/docs/mt5/api/webapi_pings)
            -   [Protocol Extension](/en/docs/mt5/api/webapi_protocol_extension)
            -   [Examples](/en/docs/mt5/api/webapi_examples)
            -   [Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)
                -   [Configuration Databases](/en/docs/mt5/api/webapi_main/webapi_config)
                -   [Trading](/en/docs/mt5/api/webapi_main/webapi_trading)
                -   [Users](/en/docs/mt5/api/webapi_main/webapi_users)
                -   [Clients](/en/docs/mt5/api/webapi_main/webapi_client)
                -   [Mail](/en/docs/mt5/api/webapi_main/webapi_mail)
                -   [News](/en/docs/mt5/api/webapi_main/webapi_news)
                -   [Prices](/en/docs/mt5/api/webapi_main/webapi_prices)
                -   [Daily Reports](/en/docs/mt5/api/webapi_main/webapi_daily)
                -   [Settings Files](/en/docs/mt5/api/webapi_main/webapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/webapi_main/webapi_subscription)
                    -   [Data Structure](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_data_structure)
                    -   [Subscribe](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_join)
                    -   [Unsubscribe](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_cancel)
                    -   [Add to Database](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_add)
                    -   [Update in Database](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_update)
                    -   [Delete from Database](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_delete)
                    -   [Get Subscriptions](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_get)
                    -   [Check Existence](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_exist)
                    -   [Add to History](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_history_add)
                    -   [Update in History](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_history_update)
                    -   [Delete from History](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_history_delete)
                    -   [Get from History](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_history_get)
                -   [Common Requests](/en/docs/mt5/api/webapi_main/webapi_common_request)
                -   [Outdated version of Rest API](/en/docs/mt5/api/webapi_main/webapi_old)
                -   [PHP Implementation of Protocol](/en/docs/mt5/api/webapi_main/php)
                -   [.NET Implementation of Protocol](/en/docs/mt5/api/webapi_main/net)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)Subscriptions

# Subscriptions

With the "Subscriptions" service, you can offer additional paid services to traders directly through the client terminals. For example, you can sell subscriptions for high-quality market data from well-known providers, offer personal manager services to assist traders in understanding the basics of trading, deliver one-time services such as position transferring or currency conversion, and much more. For more details, please read the [MetaTrader 5 Administrator Help](https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions).

The requests described in this section enable the management of subscriptions on traders' accounts:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Request</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_join" class="topiclink">/api/subscription/join</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Add a subscription for a user.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_cancel" class="topiclink">/api/subscription/cancel</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Cancel a user subscription user.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_add" class="topiclink">/api/subscription/add</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Add a user subscription directly to the server database.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_update" class="topiclink">/api/subscription/update</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Edit a user subscription directly in the server database.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_delete" class="topiclink">/api/subscription/delete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete a user subscription directly from the server database.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_get" class="topiclink">/api/subscription/get</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get a user subscription user.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_exist" class="topiclink">/api/subscription/exist</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Check if the user has a subscription to the specified service.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_history_add" class="topiclink">/api/subscription/history/add</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Add a user subscription action directly to the server database.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_history_update" class="topiclink">/api/subscription/history/update</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Edit a user subscription action directly in the server database.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_history_delete" class="topiclink">/api/subscription/history/delete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete a user subscription action directly from the server database.</span></p></td></tr><tr class="table"><td class="table" style="width:210px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_history_get" class="topiclink">/api/subscription/history/get</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get a history of user's subscription actions.</span></p></td></tr></tbody></table>

The format, in which the subscription data is passed, is described in the "[Data Structure](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_data_structure)" section.

[Delete](/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_delete)

[Data Structure](/en/docs/mt5/api/webapi_main/webapi_subscription/webapi_subscription_data_structure)