# MTGatewayCreateLocal

> Source: https://support.metaquotes.net/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreatelocal

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
                -   [MTGatewayVersion](/en/docs/mt5/api/gatewayapi_exported/mtgatewayversion)
                -   [MTGatewayCreate](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreate)
                -   [MTGatewayCreateLocal](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreatelocal)
            -   [CMTGatewayAPIFactory](/en/docs/mt5/api/cmtgatewayapifactory)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Exported Functions](/en/docs/mt5/api/gatewayapi_exported)MTGatewayCreateLocal

# MTGatewayCreateLocal

MTGatewayCreateLocal exported function creates a new [IMTGatewayAPI](/en/docs/mt5/api/imtgatewayapi) interface copy with predetermined parameters submitted in the command line and returns a pointer to it.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">MTGatewayCreate</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTGatewayInfo&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">info</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Reference&nbsp;to&nbsp;MTGatewayInfo</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTGatewayAPI**</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">gateway</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Pointer&nbsp;to&nbsp;a&nbsp;pointer&nbsp;o&nbsp;the&nbsp;interface</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">int</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">argc</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Number&nbsp;of&nbsp;command&nbsp;line&nbsp;parameters</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">wchar_t**</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">argv</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Command&nbsp;line&nbsp;parameters</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

info

\[out\] A reference to the [MTGatewayInfo](/en/docs/mt5/api/mtgatewayinfo) structure.

gateway

\[out\]  A pointer to a pointer to the created [IMTGatewayAPI](/en/docs/mt5/api/imtgatewayapi) interface.

argc

\[in\]  Number of [command line parameters](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreatelocal#param).

argv

\[in\] [Parameters of the command line](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreatelocal#param) that launched the gateway/data feed.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred, which corresponds to the response code.

Note

This function type is called instead of [MTGatewayCreate](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreate), in case additional parameters were indicated in a command line during the run of a gateway/data feed executable file. Parameters of the command line are passed to the argc and argv parameters. The following additional running parameters are possible:

-   /name:XXX — the name of the gateway/data feed that will be used for the folder, in which the application data (like operation logs) will be stored. This folder is created in the directory where the executable file of the gateway/data feed is located.
-   /address:XXX — the default address on which the server port GatewayAPI runs;
-   /login:XXX — the default login that will be used for connecting history and trade servers to a gateway/data feed.
-   /password:XXX — the default password that will be used for connecting history and trade servers to a gateway/data feed.
-   /timezone:XXX — time zone in minutes (for example, GMT +01:00 corresponds to 60, GMT -01:00 corresponds to -60), that will be used in gateway/data feed settings.
-   /timecorrect — if this parameter is used, DST adjustment is enabled.
-   /standalone — when this flag is enabled, the [IMTGatewaySink::OnGatewayShutdown](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayshutdown) event handler, which notifies of trading platform shutdown, will not be called.
-   /description — the history server runs a gateway/data feed with this parameter, when it is required to get the description of the gateway/data feed module. The description is used for including the module in the list of available gateways/data feeds when creating/modifying the corresponding configuration via MetaTrader 5 Administrator. In addition, the description is used for convenient managing the gateway/data feed settings via MetaTrader 5 Administrator — this description determines modes of the gateway/data feed operation, its default setting, etc. The description represents a [MTGatewayInfo](/en/docs/mt5/api/mtgatewayinfo) structure.

Additional parameters are passed in a command line from a history server. The implemented feature of passing command line parameters eliminates the necessity to parse string parameters, initialize the time zone and generate the description of the gateway/data feed. Additional parameters can be passed only to the gateways/data feeds, which are managed by the server history.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The address, on which the gateway/data feed runs, and the parameters of the account for connecting to it are provided to facilitate application debugging.</span></p></td></tr></tbody></table>

[MTGatewayCreate](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreate)

[CMTGatewayAPIFactory](/en/docs/mt5/api/cmtgatewayapifactory)