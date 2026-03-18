# Interaction of the Platform and Gateway API

> Source: https://support.metaquotes.net/en/docs/mt5/api/gatewayapi_interaction

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)Interaction of the Platform and Gateway API

# Interaction of the Platform and Gateway API

The MetaTrader 5 trading platform exchanges data with the Gateway API using the client-server technology, where the platform acts as a client and the Gateway API acts as a server. To protect the Gateway API server from unauthorized connection authorization is used. Parameters of the server port of the Gateway API are specified in the Gateway Server field, and authentication parameters are set in the Gateway Login and Gateway Password fields of the gateway or data feed (via the MetaTrader 5 Administrator or the appropriate interfaces — [IMTConFeeder](/en/docs/mt5/api/config_datafeeds/imtconfeeder) and [IMTConGateway](/en/docs/mt5/api/config_gateway/imtcongateway)).

The process of starting the gateway/data feed begins after completing presets and including its configuration in the MetaTrader 5 Administrator. Below is the sequence of actions performed during the start:

-   The [IMTGatewayAPI::Start](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_server/imtgatewayapi_start) method is called to start the server port of the Gateway API. After that, the Gateway API begins to accept incoming connections from the platform components. The process of data synchronization between the platform and the Gateway API begins.
-   First a history server is connected to the Gateway API. It passes the configuration of the gateway/data feed. At this stage, the work of the Gateway API is defined: whether it will operate as a gateway or as a data feed. Until the history server is connected, other components cannot be connected.
-   If an application is a data feed, other components of the platform are not connected. Transmission of quotes and/or news begins.
-   If the application is a gateway, then the main trading server additionally connects to the Gateway API. It passes the trading platform settings of symbols, groups, etc.
-   Further, all other trading servers of the platform are connected.
-   After synchronization the [IMTGatewaySink::OnGatewayStart](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewaystart) event is called.

[Gateway API](/en/docs/mt5/api/gatewayapi)

[Trade Operations in Gateway API](/en/docs/mt5/api/gatewayapi_trade_processing)