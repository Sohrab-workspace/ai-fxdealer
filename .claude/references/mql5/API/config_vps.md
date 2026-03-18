# MetaTrader VPS — a virtual hosting service for traders

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_vps

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
            -   [Routing](/en/docs/mt5/api/config_route)
            -   [Reports](/en/docs/mt5/api/config_report)
            -   [Mail Servers](/en/docs/mt5/api/config_email)
            -   [Messengers](/en/docs/mt5/api/config_messenger)
            -   [Automations](/en/docs/mt5/api/config_automation)
            -   [VPS](/en/docs/mt5/api/config_vps)
                -   [IMTConVPS](/en/docs/mt5/api/config_vps/imtconvps)
                -   [IMTConVPSRule](/en/docs/mt5/api/config_vps/imtconvpsrule)
                -   [IMTConVPSCondition](/en/docs/mt5/api/config_vps/imtconvpscondition)
                -   [IMTConVPSGroup](/en/docs/mt5/api/config_vps/imtconvpsgroup)
                -   [IMTConVPSSink](/en/docs/mt5/api/config_vps/imtconvpssink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)VPS

# MetaTrader VPS — a virtual hosting service for traders

The [Virtual Hosting](https://support.metaquotes.net/en/docs/mt5/client/virtual_hosting) service is extremely important for traders. It enables 24/7 operation of trading robots and [copied signals](https://www.mql5.com/en/signals), without the need to keep the PC turned on permanently. Furthermore, users do not have to worry about the hardware and connections. The service is available directly from the client terminals, so traders can start using it in just a few clicks. The service ensures minimal network delays between the terminal and the broker's server, as the system selects the nearest hosting server automatically.

Sponsored Hosting is a great tool for attracting new traders. Start providing a free useful service to your clients and create a competitive edge to attract more traders. Furthermore, by providing stable and continuous trading 24/7 for existing clients, you will increase trading volumes.

Find out more about the service in the [MetaTrader 5 Administrator Help files](https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_vps).

The interfaces described in this section enable the management of the VPS sponsorship settings:

-   [IMTConVPS](/en/docs/mt5/api/config_vps/imtconvps) — methods for obtaining and changing Sponsored VPS settings.
-   [IMTConVPSRule](/en/docs/mt5/api/config_vps/imtconvpsrule) — methods for obtaining and changing rules in Sponsored VPS settings.
-   [IMTConVPSCondition](/en/docs/mt5/api/config_vps/imtconvpscondition) — methods for working with conditions in VPS allocation rules.
-   [IMTConVPSGroup](/en/docs/mt5/api/config_vps/imtconvpsgroup) — methods for obtaining and changing groups in which the Sponsored VPS is available.
-   [IMTConVPSSink](/en/docs/mt5/api/config_vps/imtconvpssink) — event handlers for changes in Sponsored VPS settings.

[OnAutomationSync](/en/docs/mt5/api/config_automation/imtconautomationsink/imtconautomationsink_onautomationsync)

[IMTConVPS](/en/docs/mt5/api/config_vps/imtconvps)