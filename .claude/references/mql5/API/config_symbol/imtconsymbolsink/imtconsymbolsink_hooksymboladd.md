# IMTConSymbolSink::HookSymbolAdd

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_hooksymboladd

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
                -   [IMTConSymbol](/en/docs/mt5/api/config_symbol/imtconsymbol)
                -   [IMTConSymbolSession](/en/docs/mt5/api/config_symbol/imtconsymbolsession)
                -   [IMTConSymbolArray](/en/docs/mt5/api/config_symbol/imtconsymbolarray)
                -   [IMTConSymbolSink](/en/docs/mt5/api/config_symbol/imtconsymbolsink)
                    -   [OnSymbolAdd](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_onsymboladd)
                    -   [OnSymbolUpdate](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_onsymbolupdate)
                    -   [OnSymbolDelete](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_onsymboldelete)
                    -   [OnSymbolSync](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_onsymbolsync)
                    -   [HookSymbolAdd](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_hooksymboladd)
                    -   [HookSymbolUpdate](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_hooksymbolupdate)
                    -   [HookSymbolDelete](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_hooksymboldelete)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
            -   [Floating Margin](/en/docs/mt5/api/config_leverage)
            -   [Managers](/en/docs/mt5/api/config_manager)
            -   [History Synchronization](/en/docs/mt5/api/config_historysync)
            -   [Gateways](/en/docs/mt5/api/config_gateway)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)[Symbols](/en/docs/mt5/api/config_symbol)[IMTConSymbolSink](/en/docs/mt5/api/config_symbol/imtconsymbolsink)HookSymbolAdd

# IMTConSymbolSink::HookSymbolAdd

Hook for adding of the new symbol.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTConSymbolSink::HookSymbolAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Manager&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTConSymbol*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_cfg</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;symbol&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTConSymbolSink.HookSymbolAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Manager&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTConSymbol&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">new_cfg</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Symbol&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\] [The login of the manager](/en/docs/mt5/api/config_manager/imtconmanager/imtconmanager_login), who is adding the new symbol. If the new symbol is being added by the plugin, 0 is specified in the parameter.

new\_cfg

\[in/out\]  A pointer the [object of the symbol to be added](/en/docs/mt5/api/config_symbol/imtconsymbol).

Return Value

In case there are no handlers if this event, [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) is returned.

If the event handler returns a code different from [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful), the symbol will not be added and the hook will not be passed to other handlers (including other plugins).

Note

The hook is called right before adding a symbol configuration to the client base. The main purpose of this hook is to modify an entry that is added, and, if necessary, to prevent the addition of unwanted records.

This method can only be used in the MetaTrader 5 Server API.

[OnSymbolSync](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_onsymbolsync)

[HookSymbolUpdate](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_hooksymbolupdate)