# IMTConSpreadLeg::Ratio

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_ratio

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
                -   [IMTConSpread](/en/docs/mt5/api/config_spread/imtconspread)
                -   [IMTConSpreadLeg](/en/docs/mt5/api/config_spread/imtconspreadleg)
                    -   [Enumerations](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_enum)
                    -   [Release](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_release)
                    -   [Assign](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_assign)
                    -   [Clear](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_clear)
                    -   [Mode](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_mode)
                    -   [Symbol](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_symbol)
                    -   [TimeFrom](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_timefrom)
                    -   [TimeTo](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_timeto)
                    -   [Ratio](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_ratio)
                    -   [RatioDbl](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_ratiodbl)
                -   [IMTConSpreadSink](/en/docs/mt5/api/config_spread/imtconspreadsink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)[Spreads](/en/docs/mt5/api/config_spread)[IMTConSpreadLeg](/en/docs/mt5/api/config_spread/imtconspreadleg)Ratio

# IMTConSpreadLeg::Ratio

Getting symbol volume ratio (weight) in a spread leg.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">UINT64&nbsp;&nbsp;</span><span class="f_Functions">IMTConSpreadLeg::Ratio</span><span class="f_CodeExample">()</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">ulong&nbsp;&nbsp;</span><span class="f_Functions">CIMTConSpreadLeg.Ratio</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Python (Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">MTConSpreadLeg.Ratio</span></p></td></tr></tbody></table>

Return Value

Symbol volume ratio (weight) in a spread leg.

# IMTConSpreadLeg::Ratio

Setting symbol volume ratio (weight) in a spread leg.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTConSpreadLeg::Ratio</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">ratio</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;volume&nbsp;ratio</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTConSpreadLeg.Ratio</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">ratio</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;volume&nbsp;ratio</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python (Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">MTConSpreadLeg.Ratio</span></p></td></tr></tbody></table>

Parameters

open

\[in\]  Symbol volume ratio (weight) in a spread leg.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

Several symbols can be configured for each leg. A volume ratio at this spread leg can be specified for each of them.

Example:

-   leg A consists of GAZR-9.12 and GAZR-3.13 symbols having the ratios of 1 and 2 respectively
-   leg B consists of GAZR-6.13 having the ratio of 1.

To keep the client's positions in the spread, the client should open positions of 1 and 2 lots for GAZR-9.12 and GAZR-3.13 respectively to one direction and position of 1 lot for GAZR-6.13 to another direction.

[TimeTo](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_timeto)

[RatioDbl](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_ratiodbl)