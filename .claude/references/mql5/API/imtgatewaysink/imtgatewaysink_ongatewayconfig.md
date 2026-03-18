# IMTGatewaySink::OnGatewayConfig

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayconfig

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
                -   [OnServerDisconnect](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserverdisconnect)
                -   [OnServerSynchronized](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversynchronized)
                -   [OnServerSymbolAdd](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversymboladd)
                -   [OnServerSymbolDelete](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversymboldelete)
                -   [OnGatewayConfig](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayconfig)
                -   [OnGatewayStart](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewaystart)
                -   [OnGatewayStop](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewaystop)
                -   [OnGatewayShutdown](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayshutdown)
                -   [OnGatewayAccountSet](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountset)
                -   [OnGatewayAccountAnswer](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewayaccountanswer)
                -   [OnDealerAnswer](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealeranswer)
                -   [OnDealerLock](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock)
                -   [HookServerConnect](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookserverconnect)
                -   [HookGatewayPositionsRequest](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewaypositionsrequest)
                -   [HookGatewayPositionsCheck](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewaypositionscheck)
                -   [HookGatewayOrdersRequest](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayordersrequest)
                -   [HookGatewayAccountRequest](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookgatewayaccountrequest)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Event Interface](/en/docs/mt5/api/imtgatewaysink)OnGatewayConfig

# IMTGatewaySink::OnGatewayConfig

A handler of the event of passing a gateway own configuration from a history server connected to it.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewaySink::OnGatewayConfig</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConGateway*</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">config</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Gateway&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewaySink.OnGatewayConfig</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTConGateway</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">config</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Gateway&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\]  The login, from which a platform component was connected.

\*config

\[in\] [The gateway configuration object](/en/docs/mt5/api/config_gateway/imtcongateway).

Note

During the connection a history server passes the gateway settings specified in the platform for it.

Do not confuse connection login with server ID (IMTConServer::ID). This login is specified in the gateway settings ([IMTConGateway::Login](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_tradinglogin)). The login is always equal to 1000 for local gateways.

The passed configuration contains the list of symbols ([IMTConFeeder::Symbol\*](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_symboladd)), for which the history server is ready to receive quotes from a data feed. The following factors are considered:

-   The symbol settings should not contain the source ([IMTConSymbol::Source](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_source)). Otherwise, the quotes are copied from it.
-   Receiving quotes from data sources ([IMTConSymbol::TICK\_REALTIME](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#entickflags)) should be enabled in the symbol settings. Otherwise, only quotes thrown in by dealers via the Manager terminals are accepted.
-   The "Quotes" or "Quotes and News" mode ([IMTConFeeder::FEED\_FLAG\_QUOTES](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_enum#enfeedersmode)) should be used for a data feed. Otherwise, the data feed quotes are rejected.

If any of the above conditions is not met, the corresponding symbols are not passed in the configuration.

# IMTGatewaySink::OnGatewayConfig

A handler of the event of passing a data feed own configuration from a history server connected to it.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">IMTGatewaySink::OnGatewayConfig</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConFeeder*</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">config</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Data&nbsp;feed&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;void&nbsp;&nbsp;</span><span class="f_Functions">CIMTGatewaySink.OnGatewayConfig</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTConFeeder&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">config</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Data&nbsp;feed&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\]  The login, from which a platform component was connected.

\*config

\[in\] [Data feed configuration object](/en/docs/mt5/api/config_datafeeds/imtconfeeder).

Note

History servers of different MetaTrader 5 trading platforms can connect to the same data feed. During the connection a history server passes the data feed settings specified in the platform for it.

Do not confuse connection login with server ID (IMTConServer::ID). This login is specified in the data feed settings ([IMTConFeeder::Login](/en/docs/mt5/api/config_datafeeds/imtconfeeder/imtconfeeder_feedlogin)). The login is always equal to 1000 for local data feeds.

The passed configuration contains the list of symbols ([IMTConGateway::Symbol\*](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symboladd)), for which the history server is ready to receive quotes from a gateway. The following factors are considered:

-   The symbol settings should not contain the source ([IMTConSymbol::Source](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_source)). Otherwise, the quotes are copied from it.
-   Receiving quotes from data sources ([IMTConSymbol::TICK\_REALTIME](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#entickflags)) should be enabled in the symbol settings. Otherwise, only quotes thrown in by dealers via the Manager terminals are accepted.
-   The "Trade and Quote" mode (the [IMTConGateway::GATEWAY\_FLAG\_IGNORE\_QUOTES](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_enum#engatewaymode) flag is not enabled) should be used for a gateway. Otherwise, the gateway quotes are rejected.

If any of the above conditions is not met, the corresponding symbols are not passed in the configuration.

[OnServerSymbolDelete](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversymboldelete)

[OnGatewayStart](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ongatewaystart)