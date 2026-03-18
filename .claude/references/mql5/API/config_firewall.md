# Firewall Configuration

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_firewall

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Firewall

# Firewall Configuration

A firewall is designed to protect your system from access from unwanted IP addresses. If a group of addresses is blocked, users (client, manager, administrator) with the address within the specified range will not be able to connect to the server. By default, it is assumed that all addresses are allowed.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The latest rule is applied to an address, regardless of previous instructions, except for the addresses that are always allowed. Thus, the position of each instruction in the list is a very important factor when setting access from IP addresses.</span></p></td></tr></tbody></table>

The following firewall interfaces are available:

-   [IMTConFirewall](/en/docs/mt5/api/config_firewall/imtconfirewall)  
    Interface for configuring firewall rules.
-   [IMTConFirewallSink](/en/docs/mt5/api/config_firewall/imtconfirewallsink)  
    \>Interface for handling events of changes in the firewall rules.

To help you understand the purpose of interfaces, below is a picture that shows various elements of firewall configuration in the MetaTrader 5 Administrator:

![Firewall configuration in MetaTrader 5 Administrator](/en/docs/mt5/api/img/firewall.png "Firewall configuration in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [Beginning of the range](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_from) of addresses.
2.  [End of the range](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_to) of addresses.
3.  [A comment](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_comment) to a rule.
4.  [Action](/en/docs/mt5/api/config_firewall/imtconfirewall/imtconfirewall_action) applied to the range of addresses.

[OnHolidaySync](/en/docs/mt5/api/config_holiday/imtconholidaysink/imtconholidaysink_onholidaysync)

[IMTConFirewall](/en/docs/mt5/api/config_firewall/imtconfirewall)