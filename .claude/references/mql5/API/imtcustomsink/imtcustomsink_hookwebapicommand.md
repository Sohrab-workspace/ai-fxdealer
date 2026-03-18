# IMTCustomSink::HookWebAPICommand

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookwebapicommand

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
            -   [Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)
            -   [Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)
            -   [Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)
            -   [Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)
            -   [Hooks](/en/docs/mt5/api/serverapi_hooks)
            -   [Request Processing on the Server](/en/docs/mt5/api/hook_scheme)
            -   [Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)
            -   [Debugging](/en/docs/mt5/api/serverapi_debug)
            -   [Ready-made Examples](/en/docs/mt5/api/serverapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reference_entrypoints)
            -   [Plugin Interface](/en/docs/mt5/api/imtserverplugin)
            -   [Main API Interface](/en/docs/mt5/api/imtserverapi)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
                -   [HookManagerCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookmanagercommand)
                -   [HookWebAPICommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookwebapicommand)
                -   [HookPluginCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookplugincommand)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
            -   [Interface of End-of-Day Events](/en/docs/mt5/api/imtendofdaysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)HookWebAPICommand

# IMTCustomSink::HookWebAPICommand

A hook of an event of execution of a [Web client's custom command](/en/docs/mt5/api/webapi_protocol_extension).

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTCustomSink::HookWebAPICommand</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">session</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Session&nbsp;identifier</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">ip</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;IP&nbsp;address&nbsp;of&nbsp;the&nbsp;Web&nbsp;client</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConManager*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">manager</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;manager&nbsp;configuration</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">command</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;command&nbsp;of&nbsp;the&nbsp;Web&nbsp;client</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTByteStream*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">indata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Input&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTByteStream*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">outdata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Output&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

session

\[in\]  A unique ID of Web client connection session. This identifier does not change during the connection session. Each ID is unique for the entire cluster of the platform and is never repeated.

ip

\[in\]  The IP address of the manager who has sent the custom command.

manager

\[in\]  The object of configuration of a manager account using which the Web client connects.

command

\[in\]  A command sent by a Web client.

indata

\[in\] [The object of the data stream](/en/docs/mt5/api/reference_bytestream/imtbytestream) sent to the server.

outdata

\[out\]  A pointer to the [object of the data stream](/en/docs/mt5/api/reference_bytestream/imtbytestream) returned in response to the command.

Return Value

If the hook does not handle the event, it returns [MT\_RET\_OK\_NONE](/en/docs/mt5/api/retcodes_successful). If the event is handled, the return code is forwarded to the Web client together with the outdata buffer.

Note

The hook is called consistently in accordance with the order of plugins in the list until the first plugin that has returned a response code other than [MT\_RET\_OK\_NONE](/en/docs/mt5/api/retcodes_successful).

## Features of Client Command Processing in Web API

When reading and sending commands through the indata and outdata parameters respectively, it is necessary to consider the format of Web API commands:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">COMMAND|PARAM1=VALUE1|PARAM2=VALUE2|\r\n</span><br><span class="f_CodeExample">additional_body</span></p></td></tr></tbody></table>

A command can consist of three elements:

-   A text command of the Web API — in response to a request, the server generates forms this part of the command, which is identical to the received command.
-   Command parameters and their values ​​— each command can have multiple parameters, separated by the character "|". The end of a command is the newline character "\\r\\n". In response to a request, the server automatically generates one additional parameter: RETCODE=response code returned from a hook.
-   An additional body — this part is used only in commands sent from a server to a client.

The PHP and .NET Web API implementations for sending custom commands feature the [MTWebAPI::CustomSend](/en/docs/mt5/api/webapi_main/php/mtwebapi/php_custom/php_customsend) and [MTWebAPI.CustomSend](/en/docs/mt5/api/webapi_main/net/net_mtwebapi/net_custom/net_customsend) methods respectively.

### The Order of Reading Input Data

To read input data from indata methods, the WebRead\* methods of the [IMTByteStream](/en/docs/mt5/api/reference_bytestream/imtbytestream) interface are used. Methods should be called in the order that corresponds to the format of Web API commands:

-   Reading a command — the [IMTByteStream::WebReadCommand](/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_webreadcommand) method.
-   Reading the parameter name — [IMTByteStream::WebReadParamName](/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_webreadparamname).
-   Reading the parameter value — one of the [IMTByteStream::WebReadParam\*](/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_webreadparamstr) methods, which corresponds to the value type.
-   Then the name and value of each of the remaining parameters is read one by one using the methods described above. After all parameters are read, in response to the IMTByteStream::WebReadParamName method, the server returns the [MT\_RET\_ERR \_NOTFOUND](/en/docs/mt5/api/retcodes_common) response code.
-   To read the additional body of commands, common reading methods [IMTByteStream::Read\*](/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_read) are used.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When calling the <a href="/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_readreset" class="topiclink">IMTByteStream::ReadReset</a> method, command reading should be started in the order described above.</span></p></td></tr></tbody></table>

An Example of Data Reading:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MTAPISTR</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">cmd={0},name={0},myparam1={0};</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MTAPISTR</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">retcode;</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Check&nbsp;if&nbsp;this&nbsp;is&nbsp;our&nbsp;command</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(CMTStr::CompareNoCase(command,L</span><span class="f_CodeExample" style="color: #a31515;">"MYCOMMAND"</span><span class="f_CodeExample">)!=0)</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_OK_NONE);</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Necessarily&nbsp;read&nbsp;the&nbsp;command</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;It&nbsp;will&nbsp;match&nbsp;what&nbsp;was&nbsp;passed&nbsp;in&nbsp;command</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(indata-&gt;WebReadCommand(cmd)!=MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Error</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_DATA);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Read&nbsp;parameters</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">while</span><span class="f_CodeExample">((retcode=indata-&gt;WebReadParamName(name))==MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Is&nbsp;this&nbsp;MYPARAM1?</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(CMTStr::CompareNoCase(name,L</span><span class="f_CodeExample" style="color: #a31515;">"MYPARAM1"</span><span class="f_CodeExample">)==0)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Get&nbsp;the&nbsp;value</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(indata-&gt;WebReadParamStr(myparam1)!=MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Error</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_DATA);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;We&nbsp;don't&nbsp;know&nbsp;other&nbsp;parameters,&nbsp;skip&nbsp;them</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(indata-&gt;WebReadParamSkip()!=MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Error</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_DATA);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Are&nbsp;parameters&nbsp;over&nbsp;or&nbsp;is&nbsp;there&nbsp;any&nbsp;error?</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(retcode!=MT_RET_ERR_NOTFOUND)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Error</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERR_DATA);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

### The Order of Generation of Output Data

When forming output data (outdata), it should be taken into account that the server automatically generates the necessary part of the response command:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">Received&nbsp;command|RETCODE=Response&nbsp;code&nbsp;of&nbsp;the&nbsp;hook|</span></p></td></tr></tbody></table>

-   The remaining parameters must be formed by using the [IMTByteStream::WebAddParam\*](/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_webaddparamstr) methods.
-   To complete work with parameters, call the [IMTByteStream::WebAddParamFinalize](/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_webaddparamfinalize) method. In fact, it adds the line break character \\r\\n, which means the end of the main body of a command.
-   Next, using the [IMTByteStream::Add\*](/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_add) methods you can create an additional body of a command.

An Example of Data Forming:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Add&nbsp;our&nbsp;own&nbsp;output&nbsp;parameter</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(outdata-&gt;WebAddParamStr(L</span><span class="f_CodeExample" style="color: #a31515;">"MYRESULT"</span><span class="f_CodeExample">,L</span><span class="f_CodeExample" style="color: #a31515;">"HELLO&nbsp;WORLD!!!"</span><span class="f_CodeExample">)!=MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Error</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERROR);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Finalize&nbsp;parameters</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(outdata-&gt;WebAddParamFinalize()!=MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Error</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERROR);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;A&nbsp;structure&nbsp;with&nbsp;our&nbsp;additional&nbsp;parameters</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MyData</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">data={0};</span><br><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Add&nbsp;as&nbsp;an&nbsp;additional&nbsp;body</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(outdata-&gt;Add(&amp;data,</span><span class="f_CodeExample" style="color: #0000ff;">sizeof</span><span class="f_CodeExample">(data))!=MT_RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #008000;">//---&nbsp;Error</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">return</span><span class="f_CodeExample">(MT_RET_ERROR);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

### Reserved Names of Commands

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

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When extending the Web API protocol, it is recommended that you use command names that will not intersect with the commands implemented on the side of MetaTrader 5 servers or any other third-party plugins. For example, you can use the company name in the command name: MYCOMPANY_MYCOMMAND.</span></p></td></tr></tbody></table>

[HookManagerCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookmanagercommand)

[HookPluginCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookplugincommand)