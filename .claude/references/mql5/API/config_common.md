# Common Configuration

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_common

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
                -   [IMTConCommon](/en/docs/mt5/api/config_common/imtconcommon)
                -   [IMTConAccountAllocation](/en/docs/mt5/api/config_common/imtconaccountallocation)
                -   [IMTConAccountAgreement](/en/docs/mt5/api/config_common/imtconaccountagreement)
                -   [IMTConCommonSink](/en/docs/mt5/api/config_common/imtconcommonsink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Common

# Common Configuration

The common configuration basically includes the information specified in the license, as well as the mode of the platform components update.

The following interfaces of common parameters are available:

-   [IMTConCommon](/en/docs/mt5/api/config_common/imtconcommon) — configure common platform parameters.
-   [IMTConAccountAllocation](/en/docs/mt5/api/config_common/imtconaccountallocation) — configure [account allocations](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_accounts/account_allocation_groups).
-   [IMTConAccountAgreement](/en/docs/mt5/api/config_common/imtconaccountagreement) — configure agreements for account allocations.
-   [IMTConCommonSink](/en/docs/mt5/api/config_common/imtconcommonsink) — interface for handling common configuration change events.

The below figure shows different elements of the common configuration in MetaTrader 5 Administrator, to help you understand the purpose of the interfaces.

![Common Configuration](/en/docs/mt5/api/img/common_configuration.png "Common Configuration")

The following elements are shown above:

1.  [The name of the platform owner](/en/docs/mt5/api/config_common/imtconcommon/imtconcommon_owner).
2.  [The full name of the platform](/en/docs/mt5/api/config_common/imtconcommon/imtconcommon_namefull).
3.  [License expiry date](/en/docs/mt5/api/config_common/imtconcommon/imtconcommon_expirationlicense).
4.  [Platform limit on groups](/en/docs/mt5/api/config_common/imtconcommon/imtconcommon_limitgroups).
5.  [The number of real clients in the platform](/en/docs/mt5/api/config_common/imtconcommon/imtconcommon_totalusersreal).
6.  [The number of trades in the platform](/en/docs/mt5/api/config_common/imtconcommon/imtconcommon_totaldeals).
7.  [Platform components update mode](/en/docs/mt5/api/config_common/imtconcommon/imtconcommon_liveupdatemode).

[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)

[IMTConCommon](/en/docs/mt5/api/config_common/imtconcommon)