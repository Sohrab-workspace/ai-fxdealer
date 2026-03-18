# MTWebAPI::Ping

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect/php_ping

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
                -   [Common Requests](/en/docs/mt5/api/webapi_main/webapi_common_request)
                -   [Outdated version of Rest API](/en/docs/mt5/api/webapi_main/webapi_old)
                -   [PHP Implementation of Protocol](/en/docs/mt5/api/webapi_main/php)
                    -   [MTWebAPI Class](/en/docs/mt5/api/webapi_main/php/mtwebapi)
                        -   [Connect/Disconnect](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect)
                            -   [Connect](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect/php_connect)
                            -   [Disconnect](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect/php_disconnect)
                            -   [IsConnected](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect/php_isconnected)
                            -   [Ping](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect/php_ping)
                        -   [Logging Management](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_logging)
                        -   [Service Commands](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_service)
                        -   [Common Configuration](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_common)
                        -   [Timing](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_time)
                        -   [Groups](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_group)
                        -   [Symbols](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_symbol)
                        -   [Clients](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_user)
                        -   [Orders](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_order)
                        -   [Deals](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_deal)
                        -   [Positions](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_position)
                        -   [Trade](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_trade)
                        -   [Mailbox](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_mail)
                        -   [News Event](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_news)
                        -   [Prices](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_tick)
                        -   [Custom Commands](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_custom)
                    -   [Examples](/en/docs/mt5/api/webapi_main/php/php_examples)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)[PHP Implementation of Protocol](/en/docs/mt5/api/webapi_main/php)[MTWebAPI Class](/en/docs/mt5/api/webapi_main/php/mtwebapi)[Connect/Disconnect](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect)Ping

# MTWebAPI::Ping

If no packets were received from a client for 120 seconds, the server breaks connection. Thus, the further execution of commands will be impossible until you complete the [authentication](/en/docs/mt5/api/webapi_rest_authentication) procedure.

This feature allows you to send empty packets to the server (called "pings").

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">MTWebAPI::Ping</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

The optimal time between sending pings is 20 seconds. You should not send pings too often.

[IsConnected](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect/php_isconnected)

[Logging Management](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_logging)