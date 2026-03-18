# News

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/webapi_news

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
                    -   [Data Structure](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_data_structure)
                    -   [Send News](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_send)
                    -   [Get News Without Body](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_get)
                    -   [Get News With Body](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_body_request)
                -   [Prices](/en/docs/mt5/api/webapi_main/webapi_prices)
                -   [Daily Reports](/en/docs/mt5/api/webapi_main/webapi_daily)
                -   [Settings Files](/en/docs/mt5/api/webapi_main/webapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/webapi_main/webapi_subscription)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)News

# News

The MetaTrader 5 Web API allows receiving and sending news to terminals via the platform's internal news system. The following requests are provided:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Request</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_send" class="topiclink">/api/news/send</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Send news.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_get" class="topiclink">/api/news/get</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get a brief news description without a body.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_body_request" class="topiclink">/api/news/get_body</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the full news description with its body.</span></p></td></tr></tbody></table>

[Get Mail With Body](/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_body_request)

[Data Structure](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_data_structure)