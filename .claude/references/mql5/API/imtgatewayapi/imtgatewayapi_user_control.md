# Synchronizing Trading Data

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control

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
                    -   [GatewayAccountAnswer](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountanswer)
                    -   [GatewayAccountRequest](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountrequest)
                    -   [GatewayAccountSet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountset)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Main Interface](/en/docs/mt5/api/imtgatewayapi)Synchronizing Trading Data

# Synchronizing Trading Data

MetaTrader 5 Gateway API provides possibility to synchronize MetaTrader 5 client trading data with an external trading system.

## Synchronizing on Request from MetaTrader 5

If the gateway has such a functionality, the platform administrator can synchronize this data on the account management page via MetaTrader 5 Administrator:

![Synchronizing with an external system](/en/docs/mt5/api/img/gateway_synchronize.png "Synchronizing with an external system")

When clicking "Synchronize" in MetaTrader 5 Administrator or when calling IMTAdminAPI::UserExternalSync and IMTManagerAPI::UserExternalSync methods from MetaTrader 5 Manager API, [IMTGatewaySink::HookGatewayAccountRequest](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayaccountrequest) hook is called. Pending orders, positions and client balances are synchronized with an external system using the hook and [GatewayAccountAnswer](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountanswer) function.

## Synchronizing on Request from an External System

There is also the possibility to change the client data on MetaTrader 5 side without requesting the platform administrator. The complete structure looks as follows:

-   The gateway receives information that the data of some users in an external system has changed. These users have certain account number in that external system.
-   In order to define the users present in MetaTrader 5, [IMTGaewayAPI::User\*](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user) methods should be used. They allow you to receive the list of the users available to the gateway on MetaTrader 5 side, as well as the account numbers in the external trading system specified for these users.
-   After receiving the list of users, it is possible to request their status on MetaTrader 5 side. This will allow you to define if their status should be synchronized with MetaTrader 5. Request for users' status is performed using [IMTGatewayAPI::GatewayAccountRequest](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountrequest) method. The data requested using such method is passed to [IMTGatewaySink::OnGatewayAccountAnswer](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountanswer) handler.
-   [IMTGatewayAPI::GatewayAccountSet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountset) method should be used to synchronize the status of the external trading system's users with MetaTrader 5. Execution result, as well as the final status of client entries after the synchronization are passed to [IMTGatewaySink::OnGatewayAccountSet](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountset) handler.

[GatewayOrdersAnswer](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_order_control/imtgatewayapi_gatewayordersanswer)

[GatewayAccountAnswer](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control/imtgatewayapi_gatewayaccountanswer)