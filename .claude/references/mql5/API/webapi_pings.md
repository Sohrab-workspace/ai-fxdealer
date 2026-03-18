# Connection Maintenance

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_pings

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)Maintaining Connections

# Connection Maintenance

The access server operates as a 'stateful' service: you should first [authenticate](/en/docs/mt5/api/webapi_rest_authentication) and then maintain connection until you complete operation (the Keep-Alive connection). Re-authentication will be required in case of connection loss.

The connection type should be indicated as "keep-alive" in all passed commands:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;/command?param1=value1&amp;param2=value2&amp;...</span><br><span class="f_CodeExample">Host:&nbsp;{domain&nbsp;bound&nbsp;to&nbsp;public&nbsp;address}</span><br><span class="f_CodeExample">Accept:&nbsp;*/*</span><br><span class="f_CodeExample">User-Agent:&nbsp;MetaTrader&nbsp;5&nbsp;Web&nbsp;API/5.2005&nbsp;(Windows&nbsp;NT&nbsp;6.2;&nbsp;x64)</span><br><span class="f_CodeExample">Connection:&nbsp;keep-alive</span><br><span class="f_CodeExample">Content-Type:&nbsp;application/x-www-form-urlencoded</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

If no packets were received from a client for 180 seconds, the server breaks connection. Thus, the further execution of commands will be impossible until you complete the [authentication](/en/docs/mt5/api/webapi_rest_authentication) procedure.

In order to maintain a connection to the server, a Web client must send empty commands/packets (called "pings") to the server. The optimal time between sending pings is 20 seconds. You should not send pings too often.

In the Rest API, you can use the [/api/test/access](/en/docs/mt5/api/webapi_pings#test_access) query for these purposes.

PHP and .NET implementations provide separate methods to maintain the connection:

-   [MTWebAPI::Ping](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_connect_disconnect/php_ping)
-   [MTWebAPI.Ping](/en/docs/mt5/api/webapi_main/net/net_mtwebapi/net_connect_disconnect/net_ping)

When using the text API, an empty packet (a packet with an empty body and the zero packet continuation flag) should be sent. Packet number should be in the range specified for the client commands (0-3FFF).

Examples of empty packets of a client:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">000000010</span><br><span class="f_CodeExample">000000640</span></p></td></tr></tbody></table>

The MetaTrader 5 Access Server also automatically sends empty packets to a client every 20 seconds. Number of such commands are in the range 4000-7FFF.

Examples of empty packets of a server:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">000042680</span><br><span class="f_CodeExample">000062170</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note that sending of empty commands are sent from the server does not depend on sending of responses to the commands of a Web client. These packets are received in one mixed stream.</span></p></td></tr></tbody></table>

## Check connection status [#](webapi_pings#test_access)

To check the Web client connection with the platform access server, as well as to verify the response to sent requests, send the /api/test/access command.

### Rest API

Request Format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;/api/test/access</span><br><span class="f_CodeExample">POST&nbsp;/api/test/access</span></p></td></tr></tbody></table>

Response Format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{&nbsp;"retcode"&nbsp;:&nbsp;"xxxx&nbsp;yyyy"&nbsp;}</span></p></td></tr></tbody></table>

### Raw API

Request Format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">TEST_ACCESS\r\n</span></p></td></tr></tbody></table>

Response Format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">TEST_ACCESS|RETCODE=xxxx&nbsp;yyyy|\r\n</span></p></td></tr></tbody></table>

### Response Parameters

-   retcode — if successful, the [response code](/en/docs/mt5/api/retcodes_successful) 0 is returned. Otherwise, an error code is returned.

## Quit Operation

To terminate the connection between the Web client and the trading platform, send the /api/quit command.

### Rest API

Request format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;/api/quit</span><br><span class="f_CodeExample">POST&nbsp;/api/quit</span></p></td></tr></tbody></table>

Response format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{&nbsp;"retcode"&nbsp;:&nbsp;"xxxx&nbsp;yyyy"&nbsp;}</span></p></td></tr></tbody></table>

### Raw API

Request format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">QUIT\r\n</span></p></td></tr></tbody></table>

Response format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">QUIT|RETCODE=xxxx&nbsp;yyyy|\r\n</span></p></td></tr></tbody></table>

[Escaping Special Characters](/en/docs/mt5/api/webapi_screening)

[Protocol Extension](/en/docs/mt5/api/webapi_protocol_extension)