# External Connection Status

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state

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
                -   [Enumerations](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_enum)
                -   [Common Functions](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_common)
                -   [Server](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_server)
                -   [External Connection State](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state)
                    -   [StateConnect](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state/imtgatewayapi_stateconnect)
                    -   [StateTraffic](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state/imtgatewayapi_statetraffic)
                -   [Client Connection](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_client)
                -   [Quote and News Feeds](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send)
                -   [History Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_ticks)
                -   [Users](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user)
                -   [Configuration Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config)
                -   [Trade Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading)
                -   [Trade Requests](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request)
                -   [Gateway Symbols](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_gateway_symbols)
                -   [Processing Trade Requests](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing)
                -   [Controlling Positions in External System](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_position_control)
                -   [Controlling Orders in External System](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_order_control)
                -   [Synchronizing Trading Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control)
                -   [Mail Database](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_mail)
                -   [User Settings](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_settings)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Main Interface](/en/docs/mt5/api/imtgatewayapi)External Connection State

# External Connection Status

The implementation of the gateway/data feed connection to external systems, as well as the relevant connection management, is entirely the responsibility of the application developer. The Gateway API does not provide any specialized methods for this. However, it allows you to implement certain interaction with the end user:

-   Receive and use custom settings for reconnecting to an external server in case of connection loss
-   Display connection status and traffic

Gateway and data feed configurations provide settings for reconnecting in case of connection loss. The settings affect the logic of reconnecting cluster servers to gateways/data feeds (local and remote), but you can also use them to work with an external connection.

![Data feed reconnection settings](/en/docs/mt5/api/img/datafeed_timeouts.png "Data feed reconnection settings")

The settings can be obtained using the following methods:

-   [IMTConGateway::TimeoutReconnect](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_timeoutreconnect) — time period between attempts to reconnect the gateway to an external server.
-   [IMTConGateway::TimeoutAttempts](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_timeoutattempts) — the number of attempts in a series of gateway reconnections to an external server.
-   [IMTConGateway::TimeoutSleep](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_timeoutsleep) —  time period between series of gateway reconnections to an external server.
-   [IMTConFeeder::TimeoutReconnect](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_timeoutreconnect) — time period between attempts to reconnect the data feed to an external server.
-   [IMTConFeeder::TimeoutAttempts](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_timeoutattempts) — the number of attempts in a series of data feed reconnections to an external server.
-   [IMTConFeeder::TimeoutSleep](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_timeoutsleep) — time period between series of data feed reconnections to an external server.

They are described in detail in the "[Interaction with Quote Provider](https://support.metaquotes.net/ru/docs/mt5/platform/components/history_server/history_server_datafeeds)" section of the MetaTrader 5 Administrator Help. You can implement similar logic for reconnecting to an external server in your app.

Status of gateway/data feed connection to external servers is displayed in MetaTrader 5 Administrator:

-   The connection status is shown by the gateway/data feed icon in the tree
-   The amount of transmitted traffic is displayed on the "Status" page of the selected gateway/data feed

![Data feed status](/en/docs/mt5/api/img/admin_datafeed_state.png "Data feed status")

The Gateway API provides the following functions to pass these parameters to the server and then to display the relevant information to the user:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:101px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:101px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state/imtgatewayapi_stateconnect" class="topiclink">StateConnect</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Set the state of the gateway/data feed external connection.</span></p></td></tr><tr class="table"><td class="table" style="width:101px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state/imtgatewayapi_statetraffic" class="topiclink">StateTraffic</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Add the value to the external connection traffic counter.</span></p></td></tr></tbody></table>

Statistical data on the number of the passed ticks, Depth of Market changes and news is counted automatically.

[ServerConnections](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_server/imtgatewayapi_serverconnections)

[StateConnect](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state/imtgatewayapi_stateconnect)