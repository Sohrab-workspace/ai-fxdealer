# Escape Character

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_screening

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)Escaping Special Characters

# Escape Character

When using special characters = (equal), | (vertical bar), \\ (backslash) and linefeed, the escape character \\ (backslash) should be used before them.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If \ (backslash) is not followed by any of the special characters mentioned above, it is processed as is.</span></p></td></tr></tbody></table>

The below table shows examples of how the escape sequences are handled on the trade server.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Sent character</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Character recognized by the server</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\=</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">=</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\|</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">|</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\(linefeed)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">(linefeed)</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\\</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">\</span></p></td></tr></tbody></table>

Examples:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="font-style: italic;">//---&nbsp;</span><span class="f_CodeExample">As&nbsp;a&nbsp;result&nbsp;of&nbsp;the&nbsp;request,&nbsp;the&nbsp;user&nbsp;name&nbsp;will&nbsp;be&nbsp;changed&nbsp;to&nbsp;John|Smith</span><br><span class="f_CodeExample">/api/user/update?login=1000&amp;name=John\|Smith</span><br><span class="f_CodeExample">//---&nbsp;when&nbsp;requesting&nbsp;a&nbsp;group&nbsp;using&nbsp;the&nbsp;/api/group/get&nbsp;command,&nbsp;the&nbsp;path&nbsp;to&nbsp;the&nbsp;group&nbsp;can&nbsp;be&nbsp;specified&nbsp;in&nbsp;two&nbsp;ways:</span><br><span class="f_CodeExample">/api/group/get?group=manager\administrators</span><br><span class="f_CodeExample">/api/group/get?group==manager\\administrators</span></p></td></tr></tbody></table>

When using PHP, the forward slashes in the JSON body of the request must be escaped twice:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">$result=$request-&gt;Post('/api/user/update?login=10098',</span><br><span class="f_CodeExample">'{&nbsp;&nbsp;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"Group"</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"demo\\\\demoforex"</span><br><span class="f_CodeExample">}');</span></p></td></tr></tbody></table>

If you use spaces in request URLs, replace them with %20. For example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">GET&nbsp;/api/user/add?name=John%20Smith&amp;pass_main=1Rp0#jahr&amp;pass_investor=lOp3$qnm&amp;group=demo&amp;leverage=100</span></p></td></tr></tbody></table>

[Authentication](/en/docs/mt5/api/webapi_rest_authentication)

[Maintaining Connections](/en/docs/mt5/api/webapi_pings)