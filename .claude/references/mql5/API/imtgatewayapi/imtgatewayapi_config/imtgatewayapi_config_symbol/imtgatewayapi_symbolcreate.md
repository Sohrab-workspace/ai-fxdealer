# IMTGatewayAPI::SymbolCreate

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolcreate

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
                    -   [Common](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_common)
                    -   [Data Feeds](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_datafeeds)
                    -   [Gateways](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_gateway)
                    -   [Symbols](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol)
                        -   [SymbolCreate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolcreate)
                        -   [SymbolSessionCreate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolsessioncreate)
                        -   [SymbolSubscribe](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolsubscribe)
                        -   [SymbolUnsubscribe](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolunsubscribe)
                        -   [SymbolAddPreliminary](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symboladdpreliminary)
                        -   [SymbolUpdate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolupdate)
                        -   [SymbolDelete](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symboldelete)
                        -   [SymbolTotal](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symboltotal)
                        -   [SymbolNext](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolnext)
                        -   [SymbolGet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolget)
                    -   [Groups](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_group)
                    -   [Time](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_time)
                    -   [Network](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_network)
                    -   [Spreads](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_spread)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Main Interface](/en/docs/mt5/api/imtgatewayapi)[Configuration Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config)[Symbols](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol)SymbolCreate

# IMTGatewayAPI::SymbolCreate

Create an object of the symbol configuration.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">IMTConSymbol*&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewayAPI::SymbolCreate</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">CIMTConSymbol&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewayAPI.SymbolCreate</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Return Value

It returns a pointer to the created object that implements the [IMTConSymbol](/en/docs/mt5/api/config_symbol/imtconsymbol) interface. In case of failure, it returns NULL.

Note

The created object must be destroyed by calling the [IMTConSymbol::Release](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_release) method of this object.

[Symbols](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol)

[SymbolSessionCreate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config/imtgatewayapi_config_symbol/imtgatewayapi_symbolsessioncreate)