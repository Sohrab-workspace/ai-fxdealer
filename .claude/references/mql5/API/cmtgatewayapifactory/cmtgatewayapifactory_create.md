# CMTGatewayAPIFactory::Create

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_create

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
            -   [Interaction of the Platform and Gateway API](/en/docs/mt5/api/gatewayapi_interaction)
            -   [Trade Operations in Gateway API](/en/docs/mt5/api/gatewayapi_trade_processing)
            -   [Development and Debugging of Gateways](/en/docs/mt5/api/gatewayapi_develop_gateway)
            -   [Symbol and Price Translation](/en/docs/mt5/api/gatewayapi_translation)
            -   [Development of Data Feeds](/en/docs/mt5/api/gatewayapi_develop_datafeed)
            -   [.NET Implementation](/en/docs/mt5/api/gatewayapi_net)
            -   [Exported Functions](/en/docs/mt5/api/gatewayapi_exported)
            -   [CMTGatewayAPIFactory](/en/docs/mt5/api/cmtgatewayapifactory)
                -   [Initialize](/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_initialize)
                -   [Shutdown](/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_shutdown)
                -   [Create](/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_create)
                -   [LicenseCheck](/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_licensecheck)
                -   [Version](/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_version)
            -   [Main Interface](/en/docs/mt5/api/imtgatewayapi)
            -   [Event Interface](/en/docs/mt5/api/imtgatewaysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[CMTGatewayAPIFactory](/en/docs/mt5/api/cmtgatewayapifactory)Create

# CMTGatewayAPIFactory::Create

Create an instance of the [IMTGatewayAPI](/en/docs/mt5/api/imtgatewayapi) interface.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">CMTGatewayAPIFactory::Create</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTGatewayInfo&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">info</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;MTGatewayInfo&nbsp;structure</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTGatewayAPI**</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">gateway</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;pointer&nbsp;to&nbsp;the&nbsp;API&nbsp;interface</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">int</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">argc=0</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;number&nbsp;of&nbsp;command&nbsp;line&nbsp;parameters</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">wchar_t**</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">argv=NULL</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Command&nbsp;line&nbsp;parameters</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">CIMTGatewayAPI&nbsp;&nbsp;</span><span class="f_Functions">SMTGatewayAPIFactory.CreateGateway</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTGatewayInfo</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">info</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;The&nbsp;MTGatewayInfo&nbsp;structure</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string[]</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">arguments</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Command&nbsp;line&nbsp;parameters</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">out&nbsp;MTRetCode</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">res</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Response&nbsp;code</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

info

\[in\]  The [MTGatewayInfo](/en/docs/mt5/api/mtgatewayinfo) structure that describes the parameters of the gateway/data feed module.

gateway

\[out\]  A pointer to a pointer to the created instance of the [IMTGatewayAPI](/en/docs/mt5/api/imtgatewayapi) interface.

argc=0

\[in\]  The number of additional parameters of a command line that is used for running the gateway/data feed. The default value is 0.

argv=NULL

\[in\]  Additional parameters of the command line that is used for running the gateway/data feed. The default value is NULL.

Return Value

An indication of a successful execution is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred, which corresponds to the response code.

Note

Gateways/data feeds support the launch with the [additional command line parameters](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreatelocal#param). In particular, the /description command line parameter is additionally used by the history server to get the description of the gateway/data feed module. Always pass the command line parameters to the CMTGatewayAPIFactory::Create method, so that the module is correctly downloaded and managed by the history server.

When an IMTGatewayAPI instance is created using the CMTGatewayAPIFactory::Create method, it is expected that the Gateway API will receive an address and name to start the gateway:

-   in command line parameters passed to CMTGatewayAPIFactory::Create (/name:XXX /address:XXX), or
-   in the [configuration file](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_gateways/gateway_service#config) (name=XXX,  address=XXX)

If the Gateway API cannot find the parameters in any of these ways, CMTGatewayAPIFactory::Create will return [MT\_RET\_ERR\_PARAMS](/en/docs/mt5/api/retcodes_common).

If login and password are not specified in the command line, it will be impossible to connect to the gateway until it adds authentication data using [IMTGatewayAPI::ClientAdd](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_client/imtgatewayapi_clientadd).

[Shutdown](/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_shutdown)

[LicenseCheck](/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_licensecheck)