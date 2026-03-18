# Format of Commands

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_https

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)Format of Commands

# Format of Commands

Web API commands are passed using standard POST and GET requests:

-   Command names and their parameters fully coincide with the [Web API protocol](/en/docs/mt5/api/webapi_main).
-   Command parameters are specified after ? and are separated using &.
-   An additional request body is passed in the JSON format.
-   The domain connected with the access server's public point is specified as the host.
-   Contents type in the request: application/x-www-form-urlencoded.

The command can be schematically represented as follows:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;/command?param1=value1&amp;param2=value2&amp;...</span><br><span class="f_CodeExample">Host:&nbsp;{domain&nbsp;bound&nbsp;to&nbsp;public&nbsp;address}</span><br><span class="f_CodeExample">Accept:&nbsp;*/*</span><br><span class="f_CodeExample">User-Agent:&nbsp;MetaTrader&nbsp;5&nbsp;Web&nbsp;API/5.2005&nbsp;(Windows&nbsp;NT&nbsp;6.2;&nbsp;x64)</span><br><span class="f_CodeExample">Connection:&nbsp;keep-alive</span><br><span class="f_CodeExample">Content-Type:&nbsp;application/x-www-form-urlencoded</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">}</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">POST&nbsp;/command?param1=value1&amp;param2=value2&amp;...</span><br><span class="f_CodeExample">Host:&nbsp;{domain&nbsp;bound&nbsp;to&nbsp;public&nbsp;address}&nbsp;</span><br><span class="f_CodeExample">Accept:&nbsp;*/*</span><br><span class="f_CodeExample">User-Agent:&nbsp;MetaTrader&nbsp;5&nbsp;Web&nbsp;API/5.2005&nbsp;(Windows&nbsp;NT&nbsp;6.2;&nbsp;x64)</span><br><span class="f_CodeExample">Connection:&nbsp;keep-alive</span><br><span class="f_CodeExample">Content-Type:&nbsp;application/x-www-form-urlencoded</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

The following data is specified in the request:

-   Host — the domain with which the public point of the access server is connected.
-   command — the name of the [command](/en/docs/mt5/api/webapi_main)
-   param1, value1, ... — additional parameters if they are used for this command.
-   { ... } — additional request body as a text in the JSON format if it is provided for the specified command. For example, when using the [/api/user/add](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_add) command, the created account parameters are passed in the additional body.  
    Some of the parameters are case-sensitive, for example, the [LeadSource and LeadCampaign](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_data_structure) fields of the trading account. Because of this, field names in a JSON body must always be passed in the case specified in the documentation. For example, the entry { ... "LEADCAMPAIGN":"website\_ad" ... } is incorrect. The correct specification is { ... "LeadCampaing":"website\_ad" ... }.

The response from the server is passed in the JSON format. The response code is always passed as the first parameter, which is followed by additional information.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{&nbsp;"retcode"&nbsp;:&nbsp;"retcode",&nbsp;"answer"&nbsp;:&nbsp;{</span><br><span class="f_CodeExample">"param1"&nbsp;:&nbsp;"value1",</span><br><span class="f_CodeExample">"param2"&nbsp;:&nbsp;"value2",</span><br><span class="f_CodeExample">...&nbsp;}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

For example, in response to the [/api/user/get](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_get) command, you will receive the response code and data concerning the requested user.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Commands, parameters and the server response are passed in the Unicode (UTF-8) format.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">All commands should be passed in the same session during and after the authentication.</span></li></ul></td></tr></tbody></table>

[Getting Started](/en/docs/mt5/api/webapi_preparing)

[Authentication](/en/docs/mt5/api/webapi_rest_authentication)