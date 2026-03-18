# IMTConGateway::GatewayServer

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gatewayserver

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
                    -   [Enumerations](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_enum)
                    -   [Release](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_release)
                    -   [Assign](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_assign)
                    -   [Clear](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_clear)
                    -   [Name](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_name)
                    -   [ID](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_id)
                    -   [Module](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_module)
                    -   [TradingServer](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_tradingserver)
                    -   [TradingLogin](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_tradinglogin)
                    -   [TradingPassword](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_tradingpassword)
                    -   [Gateway](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gateway)
                    -   [GatewayServer](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gatewayserver)
                    -   [GatewayLogin](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gatewaylogin)
                    -   [GatewayPassword](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gatewaypassword)
                    -   [Mode](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_mode)
                    -   [Flags](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_flags)
                    -   [Timeout](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_timeout)
                    -   [TimeoutReconnect](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_timeoutreconnect)
                    -   [TimeoutSleep](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_timeoutsleep)
                    -   [TimeoutAttempts](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_timeoutattempts)
                    -   [ParameterAdd](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parameteradd)
                    -   [ParameterUpdate](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parameterupdate)
                    -   [ParameterDelete](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parameterdelete)
                    -   [ParameterClear](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parameterclear)
                    -   [ParameterShift](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parametershift)
                    -   [ParameterTotal](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parametertotal)
                    -   [ParameterNext](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parameternext)
                    -   [ParameterGet](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_parameterget)
                    -   [SymbolAdd](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symboladd)
                    -   [SymbolUpdate](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symbolupdate)
                    -   [SymbolShift](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symbolshift)
                    -   [SymbolDelete](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symboldelete)
                    -   [SymbolClear](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symbolclear)
                    -   [SymbolTotal](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symboltotal)
                    -   [SymbolNext](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_symbolnext)
                    -   [GroupAdd](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_groupadd)
                    -   [GroupUpdate](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_groupupdate)
                    -   [GroupShift](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_groupshift)
                    -   [GroupDelete](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_groupdelete)
                    -   [GroupClear](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_groupclear)
                    -   [GroupTotal](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_grouptotal)
                    -   [GroupNext](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_groupnext)
                    -   [TranslateAdd](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translateadd)
                    -   [TranslateUpdate](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translateupdate)
                    -   [TranslateDelete](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translatedelete)
                    -   [TranslateClear](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translateclear)
                    -   [TranslateShift](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translateshift)
                    -   [TranslateTotal](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translatetotal)
                    -   [TranslateNext](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translatenext)
                    -   [TranslateGet](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translateget)
                    -   [TranslateGetSource](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_translategetsource)
                    -   [StateConnected](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_stateconnected)
                    -   [StateReceivedTicks](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_statereceivedticks)
                    -   [StateReceivedBooks](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_statereceivedbooks)
                    -   [StateTrafficIn](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_statetrafficin)
                    -   [StateTrafficOut](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_statetrafficout)
                    -   [StateTradesTotal](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_statetradestotal)
                    -   [StateTradesAverageTime](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_statetradesaveragetime)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)[Gateways](/en/docs/mt5/api/config_gateway)[IMTConGateway](/en/docs/mt5/api/config_gateway/imtcongateway)GatewayServer

# IMTConGateway::GatewayServer

Gets the address, at which the gateway will accept connections from the history and trade servers.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">LPCWSTR&nbsp;&nbsp;</span><span class="f_Functions">IMTConGateway::GatewayServer</span><span class="f_CodeExample">()</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">string&nbsp;&nbsp;</span><span class="f_Functions">CIMTConGateway.GatewayServer</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Python (Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">MTConGateway.GatewayServer</span></p></td></tr></tbody></table>

Return Value

If successful, returns a pointer to the string with the address, at which the gateway will accept connections from the history and trade servers. Otherwise, it returns NULL.

Note

The pointer to the resulting string is valid for the lifetime of the [IMTConGateway](/en/docs/mt5/api/config_gateway/imtcongateway) object.

To use the string after the object removal (call of the [IMTConGateway::Release](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_release) method of this object), a copy of it should be created.

# IMTConGateway::GatewayServer

Sets the address, at which the gateway will accept connections from the history and trade servers.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTConFeeder::GatewayServer</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">server</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Server&nbsp;address</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTConFeeder.GatewayServer</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">server</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Server&nbsp;address</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python (Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">MTConGateway.GatewayServer</span></p></td></tr></tbody></table>

Parameters

server

\[in\]  The address, at which the gateway will accept connections from the history and trade servers.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

The maximum length of the address is 128 characters (including the sign of the string end). If a string of a greater length is assigned, it will be cut to this length.

[Gateway](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gateway)

[GatewayLogin](/en/docs/mt5/api/config_gateway/imtcongateway/imtcongateway_gatewaylogin)