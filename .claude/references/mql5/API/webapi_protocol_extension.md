# Protocol Extension

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_protocol_extension

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)Protocol Extension

# Protocol Extension

The MetaTrader 5 API protocol is extensible. In addition to standard [commands of manager connection](/en/docs/mt5/api/webapi_main), a Web client can send any other text commands to a server. However, handling of such commands must be implemented on the server side.

Custom Web API commands can be handled using a server plugin created with the MetaTrader 5 Server API. For this purpose, the Server API provides a special hook [IMTCustomSink::HookWebAPICommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookwebapicommand).

Consider an example of sending a custom command:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">POST&nbsp;/echo</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample"></span><span class="f_CodeExample">text</span><span class="f_CodeExample"></span><span class="f_CodeExample">:&nbsp;</span><span class="f_CodeExample"></span><span class="f_CodeExample">Request/Reply&nbsp;request</span><span class="f_CodeExample"></span><span class="f_CodeExample">,</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample"></span><span class="f_CodeExample">seq</span><span class="f_CodeExample"></span><span class="f_CodeExample">:&nbsp;1</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

The command can be handled on the plugin side as follows:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">MTAPISTR&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cmd={},request{};</span><br><span class="f_CodeExample">MTAPIRES&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;retcode;</span><br><span class="f_CodeExample">//---&nbsp;Check&nbsp;that&nbsp;this&nbsp;is&nbsp;our&nbsp;command</span><br><span class="f_CodeExample">if(CMTStr::CompareNoCase(command,L"ECHO")!=0)</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;return(MT_RET_OK_NONE);</span><br><span class="f_CodeExample">//---&nbsp;Check&nbsp;the&nbsp;content</span><br><span class="f_CodeExample">if(indata-&gt;WebReadCommand(cmd)!=MT_RET_OK)</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;//---&nbsp;Error</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;return(MT_RET_ERR_DATA);</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span><br><span class="f_CodeExample">//---&nbsp;Read&nbsp;the&nbsp;request</span><br><span class="f_CodeExample">retcode=indata-&gt;ReadStr(request);</span><br><span class="f_CodeExample">if(retcode!=MT_RET_OK)</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;//---&nbsp;Error</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;return(MT_RET_ERR_DATA);</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span><br><span class="f_CodeExample">//---&nbsp;Processing&nbsp;a&nbsp;custom&nbsp;command&nbsp;with&nbsp;custom&nbsp;parameters</span><br><span class="f_CodeExample">if(CMTStr::Compare(request,L"{text:&nbsp;Request/Reply&nbsp;request,&nbsp;seq:&nbsp;1&nbsp;}")!=0)</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;//---&nbsp;Error</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;return(MT_RET_ERR_DATA);</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span><br><span class="f_CodeExample">//---&nbsp;Send&nbsp;a&nbsp;response</span><br><span class="f_CodeExample">retcode=outdata-&gt;AddStr(L"{text:&nbsp;Request/Reply&nbsp;reply,&nbsp;seq:&nbsp;1}");</span><br><span class="f_CodeExample">if(retcode!=MT_RET_OK)</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;//---&nbsp;Error</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;return(retcode);</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span><br><span class="f_CodeExample">//---&nbsp;Success</span><br><span class="f_CodeExample">return(MT_RET_OK);</span></p></td></tr></tbody></table>

The command will return the following in response to the command:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;&nbsp;"retcode"&nbsp;:&nbsp;"0&nbsp;Done",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"answer"&nbsp;:&nbsp;{text:&nbsp;Request/Reply&nbsp;reply,&nbsp;seq:&nbsp;1}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

Further details about the handling of custom commands is available under the [IMTCustomSink::HookWebAPICommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookwebapicommand) section.

## Reserved Names of Commands

There are special names reserved for use in the trading platform. These names cannot be used for custom commands:

-   AUTH\_\*
-   USER\_\*
-   TRADE\_\*
-   TIME\_\*
-   GROUP\_\*
-   ORDER\_\*
-   POSITION\_\*
-   DEAL\_\*
-   HISTORY\_\*
-   TICK\_\*
-   MAIL\_\*
-   NEWS\_\*
-   COMMON\_\*
-   QUIT\*
-   TEST\_TRADE
-   TEST\_ACCESS

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When extending the protocol, it is recommended that you use command names that will not intersect with the commands implemented on the side of MetaTrader 5 servers or any other third-party plugins. For example, you can use the company name in the command name: MYCOMPANY_MYCOMMAND.</span></p></td></tr></tbody></table>

[Maintaining Connections](/en/docs/mt5/api/webapi_pings)

[Examples](/en/docs/mt5/api/webapi_examples)