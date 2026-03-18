# MTGatewayCreate

> Source: https://support.metaquotes.net/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreate

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Exported Functions](/en/docs/mt5/api/gatewayapi_exported)MTGatewayCreate

# MTGatewayCreate

MTGatewayCreate exported function creates a new [IMTGatewayAPI](/en/docs/mt5/api/imtgatewayapi) interface copy and returns a pointer to it.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">MTGatewayCreate</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTGatewayInfo&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">info</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Reference&nbsp;to&nbsp;MTGatewayInfo</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTGatewayAPI**</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">gateway</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Pointer&nbsp;to&nbsp;a&nbsp;pointer&nbsp;o&nbsp;the&nbsp;interface</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

info

\[out\] A reference to the [MTGatewayInfo](/en/docs/mt5/api/mtgatewayinfo) structure.

gateway

\[out\]  A pointer to a pointer to the created [IMTGatewayAPI](/en/docs/mt5/api/imtgatewayapi) interface.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

[MTGatewayVersion](/en/docs/mt5/api/gatewayapi_exported/mtgatewayversion)

[MTGatewayCreateLocal](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreatelocal)