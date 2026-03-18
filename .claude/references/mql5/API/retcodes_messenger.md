# Instant messengers

> Source: https://support.metaquotes.net/en/docs/mt5/api/retcodes_messenger

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Return Codes](/en/docs/mt5/api/reference_retcodes)Messengers

# Instant messengers

The server returns codes from this group when sending messages via instant messengers.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:250px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Constant</span></p></th><th class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:250px;"><p class="p_fortable"><span class="f_fortable">MT_RET_MESSENGER_INVALID_PHONE</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">14000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">An invalid phone number is specified. The number must be specified in the format +[country code][number], for example: +74951113594. The should be specified without spaces.</span></p></td></tr><tr class="table"><td class="table" style="width:250px;"><p class="p_fortable"><span class="f_fortable">MT_RET_MESSENGER_NOT_MOBILE</span></p></td><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable">14001</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A landline phone number is specified instead of a mobile one. Mobile phone numbers must be specified when sending messages. Messages cannot be delivered to other phone numbers.</span></p></td></tr></tbody></table>

The codes are used for the following methods:

-   [IMTServerAPI::MessengerSend](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_messenger/imtserverapi_messengersend)
-   [IMTAdminAPI::MessengerSend](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_messenger/imtadminapi_messengersend)
-   [IMTManagerAPI::MessengerSend](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_messengersend)
-   [/messenger\_send](/en/docs/mt5/api/webapi_main/webapi_config/webapi_messenger/webapi_messenger_send)

[API](/en/docs/mt5/api/retcodes_api)

[Subscriptions](/en/docs/mt5/api/retcodes_subscription)