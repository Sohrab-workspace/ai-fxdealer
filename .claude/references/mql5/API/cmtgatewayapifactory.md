# CMTGatewayAPIFactory

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtgatewayapifactory

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)CMTGatewayAPIFactory

# CMTGatewayAPIFactory

The interfaces factory is provided in the "MT5APIateway.h" file to ease the access to the IMTGatewayAPI interface. This factory automatically downloads a necessary GatewayAPI library (32/64-bit) and gives access to the [exported functions](/en/docs/mt5/api/gatewayapi_exported).

The factory contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_initialize" class="topiclink">Initialize</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Loading of Gateway API library and all functions exported by it.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_shutdown" class="topiclink">Shutdown</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gateway API library unloading.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_create" class="topiclink">Create</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Create an instance of the <a href="/en/docs/mt5/api/imtgatewayapi" class="topiclink">IMTGatewayAPI</a> interface.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_licensecheck" class="topiclink">LicenseCheck</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gateway/data feed module usage license verification.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_version" class="topiclink">Version</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the version of the loaded Gateway API library.</span></p></td></tr></tbody></table>

Using factories in application development is optional. You can use your own implementation of corresponding functions.

[MTGatewayCreateLocal](/en/docs/mt5/api/gatewayapi_exported/mtgatewaycreatelocal)

[Initialize](/en/docs/mt5/api/cmtgatewayapifactory/cmtgatewayapifactory_initialize)