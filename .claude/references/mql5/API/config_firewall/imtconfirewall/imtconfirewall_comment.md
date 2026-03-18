# IMTConFirewall::Comment

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_comment

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
                -   [IMTConFirewall](/en/docs/mt5/api/config_firewall/imtconfirewall)
                    -   [Enumerations](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_enum)
                    -   [Release](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_release)
                    -   [Assign](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_assign)
                    -   [Clear](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_clear)
                    -   [Action](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_action)
                    -   [From](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_from)
                    -   [To](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_to)
                    -   [Comment](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_comment)
                -   [IMTConFirewallSink](/en/docs/mt5/api/config_firewall/imtconfirewallsink)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)[Firewall](/en/docs/mt5/api/config_firewall)[IMTConFirewall](/en/docs/mt5/api/config_firewall/imtconfirewall)Comment

# IMTConFirewall::Comment

Get a comment to the firewall rule.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">LPCWSTR&nbsp;&nbsp;</span><span class="f_Functions">IMTConFirewall::Comment</span><span class="f_CodeExample">()</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">string&nbsp;&nbsp;</span><span class="f_Functions">CIMTConFirewall.Comment</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Python (Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">MTConFirewall.Comment</span></p></td></tr></tbody></table>

Return Value

If successful, it returns a pointer to a string with a comment to the rule. Otherwise, it returns NULL.

Note

The pointer to the resulting string is valid for the lifetime of the [IMTConFirewall](/en/docs/mt5/api/config_firewall/imtconfirewall) object.

To use the string after the object removal (call of the [IMTConFirewall::Release](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_release) method of this object), a copy of it should be created.

# IMTConFirewall::Comment

Set a comment to the firewall rule.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTConFirewall::Comment</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">comment</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Comment</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTConFirewall.Comment</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">srting</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">comment</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Comment</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python (Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">MTConFirewall.Comment</span></p></td></tr></tbody></table>

Parameters

comment

\[in\]  A comment to the firewall rule.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

The maximum comment length is 32 characters (including the end-of-line character). If a string of a greater length is assigned, it will be cut to this length.

[To](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_to)

[IMTConFirewallSink](/en/docs/mt5/api/config_firewall/imtconfirewallsink)