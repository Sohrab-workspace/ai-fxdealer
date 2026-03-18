# Automations

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_automation

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
                -   [IMTConAutomation](/en/docs/mt5/api/config_automation/imtconautomation)
                -   [IMTConAutoCondition](/en/docs/mt5/api/config_automation/imtconautocondition)
                -   [IMTConAutoAction](/en/docs/mt5/api/config_automation/imtconautoaction)
                -   [IMTConAutoParam](/en/docs/mt5/api/config_automation/imtconautoparam)
                -   [IMTConAutomationSink](/en/docs/mt5/api/config_automation/imtconautomationsink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Automations

# Automations

The Automations service enables the execution of various actions in the platform based on predefined scenarios. To automate routine operations, select conditions and appropriate actions that should trigger under these conditions. Automations allow companies to streamline numerous day-to-day operations and eventually reduce manual work. For more details, please read the [MetaTrader 5 Administrator Help](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation).

The interfaces described in this section enable the management of automation settings:

-   [IMTConAutomation](/en/docs/mt5/api/config_automation/imtconautomation) — methods for receiving and editing automation configurations.
-   [IMTConAutoCondition](/en/docs/mt5/api/config_automation/imtconautocondition) — methods for managing automation task trigger conditions.
-   [IMTConAutoAction](/en/docs/mt5/api/config_automation/imtconautoaction) — methods for managing actions performed upon the triggering of automation tasks.
-   [IMTConAutoParam](/en/docs/mt5/api/config_automation/imtconautoparam) — methods for managing the parameters of actions performed upon the triggering of automation tasks.
-   [IMTConAutomationSink](/en/docs/mt5/api/config_automation/imtconautomationsink) — event handlers for automation configuration changes.

[OnMessengerSync](/en/docs/mt5/api/config_messenger/imtconmessengersink/imtconmessengersink_onmessengersync)

[IMTConAutomation](/en/docs/mt5/api/config_automation/imtconautomation)