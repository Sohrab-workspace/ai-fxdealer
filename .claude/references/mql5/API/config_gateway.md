# Gateway Configuration

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_gateway

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
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
            -   [Common](/en/docs/mt5/api/config_common)
            -   [Network](/en/docs/mt5/api/config_network)
            -   [Plugins](/en/docs/mt5/api/config_plugins)
            -   [Data Feeds](/en/docs/mt5/api/config_datafeeds)
            -   [Time](/en/docs/mt5/api/config_time)
            -   [Holidays](/en/docs/mt5/api/config_holiday)
            -   [Firewall](/en/docs/mt5/api/config_firewall)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
            -   [Floating Margin](/en/docs/mt5/api/config_leverage)
            -   [Managers](/en/docs/mt5/api/config_manager)
            -   [History Synchronization](/en/docs/mt5/api/config_historysync)
            -   [Gateways](/en/docs/mt5/api/config_gateway)
                -   [IMTConGateway](/en/docs/mt5/api/config_gateway/imtcongateway)
                -   [IMTConGatewayModule](/en/docs/mt5/api/config_gateway/imtcongatewaymodule)
                -   [IMTConGatewayTranslate](/en/docs/mt5/api/config_gateway/imtcongatewaytranslate)
                -   [IMTConGatewaySink](/en/docs/mt5/api/config_gateway/imtcongatewaysink)
            -   [Routing](/en/docs/mt5/api/config_route)
            -   [Reports](/en/docs/mt5/api/config_report)
            -   [Mail Servers](/en/docs/mt5/api/config_email)
            -   [Messengers](/en/docs/mt5/api/config_messenger)
            -   [Automations](/en/docs/mt5/api/config_automation)
            -   [VPS](/en/docs/mt5/api/config_vps)
            -   [KYC](/en/docs/mt5/api/config_kyc)
            -   [Subscriptions](/en/docs/mt5/api/config_subscription)
            -   [Funds and ETF](/en/docs/mt5/api/config_funds)
            -   [Additional Parameters](/en/docs/mt5/api/config_param)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Gateways

# Gateway Configuration

Gateways are used for integrating the MetaTrader 5 platform with external trading systems. Gateways allow to transmit trade operations to external systems, as well as transmit quotes and news from them.

The following gateway interfaces are available:

-   [IMTConGateway](/en/docs/mt5/api/config_gateway/imtcongateway)  
    An interface that provides access to all the main parameters of the gateway.
-   [IMTConGatewayModule](/en/docs/mt5/api/config_gateway/imtcongatewaymodule)  
    An interface that provides access to the parameters of the gateway module.
-   [IMTConGatewayTranslate](/en/docs/mt5/api/config_gateway/imtcongatewaytranslate)  
    An interface that provides access to the settings for converting symbols and quotes received via the gateway.
-   [IMTConGatewaySink](/en/docs/mt5/api/config_gateway/imtcongatewaysink)  
    An interface is used for handling gateway events.

The below figure shows different elements of gateway configuration in the MetaTrader 5 Administrator, to help you understand the purpose of the interfaces:

![The gateway configuration in MetaTrader 5 Administrator](/en/docs/mt5/api/img/gateways.png "The gateway configuration in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [The name of gateway configuration](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_name).
2.  [Gateway ID](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_id).
3.  [Gateway operation mode](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_flags).
4.  [Address of the server of the external trading system](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_tradingserver).
5.  The gateway status.
6.  [The state of the gateway configuration](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_mode).
7.  [The gateway module](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_module).
8.  [Gateway server address](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gatewayserver).
9.  [A login for authentication on the gateway server](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gatewaylogin).
10.  [A password for authentication on the gateway server](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gatewaypassword).
11.  [A login to authorize on the external server](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_tradinglogin).
12.  [A password to authorize on the external server](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_tradingpassword).
13.  [Configuration of groups](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_groupadd), trade operations from which will be processed by the gateway.
14.  [Configuration of symbols](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symboladd), for which the gateway will transmit quotes and process trade operations.
15.  [Configuration of parameters for conversion](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translateadd) of price data transmitted by the gateway.
16.  [Setup of gateway parameters](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parameteradd).
17.  [Setup of gateway timeouts](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_timeout).

[OnHistorySyncSync](/en/docs/mt5/api/config_historysync/imtconhistorysyncsink/imtconhistorysyncsink_onhistorysyncsync)

[IMTConGateway](/en/docs/mt5/api/config_gateway/imtcongateway)