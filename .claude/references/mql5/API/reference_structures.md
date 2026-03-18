# Structures

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_structures

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
            -   [MTProxyInfo](/en/docs/mt5/api/mtproxyinfo)
            -   [MTLicenseCheck](/en/docs/mt5/api/mtlicensecheck)
            -   [MTTick](/en/docs/mt5/api/mttick)
            -   [MTTickShort](/en/docs/mt5/api/mttickshort)
            -   [MTTickRate](/en/docs/mt5/api/mttickrate)
            -   [MTTickStat](/en/docs/mt5/api/mttickstat)
            -   [MTMailRange](/en/docs/mt5/api/mtmailrange)
            -   [MTLogRecord](/en/docs/mt5/api/mtlogrecord)
            -   [MTChartBar](/en/docs/mt5/api/mtchartbar)
            -   [MTBookItem](/en/docs/mt5/api/mtbookitem)
            -   [MTBook/MTBookDiff](/en/docs/mt5/api/mtbook)
            -   [MTGatewayInfo](/en/docs/mt5/api/mtgatewayinfo)
            -   [MTNews](/en/docs/mt5/api/mtnews)
            -   [MTEconomicEvent](/en/docs/mt5/api/mteconomicevent)
            -   [MTReportInfo](/en/docs/mt5/api/mtreportinfo)
            -   [MTReportParam](/en/docs/mt5/api/mtreportparam)
            -   [MTReportServerInfo](/en/docs/mt5/api/mtreportserverinfo)
            -   [MTPluginInfo](/en/docs/mt5/api/mtplugininfo)
            -   [MTPluginParam](/en/docs/mt5/api/mtpluginparam)
            -   [MTServerInfo](/en/docs/mt5/api/mtserverinfo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)Structures

# Structures

The MetaTrader 5 API provides several pre-defined structures that are designed for storing and passing of service information: Virtually all APIs use the same structures.

-   [MTProxyInfo](/en/docs/mt5/api/mtproxyinfo) — parameters of connection through a proxy server.
-   [MTLicenseCheck](/en/docs/mt5/api/mtlicensecheck) — Information for verifying the license.
-   [MTTick](/en/docs/mt5/api/mttick) — a full description of a tick.
-   [MTTickShort](/en/docs/mt5/api/mttickshort) — a brief description of a tick.
-   [MTTickRate](/en/docs/mt5/api/mttickrate) — a brief description of a tick.
-   [MTTickStat](/en/docs/mt5/api/mttickstat) — description of statistical information about ticks.
-   [MTMailRange](/en/docs/mt5/api/mtmailrange) — a range of recipients of a mailing list.
-   [MTLogRecord](/en/docs/mt5/api/mtlogrecord) — description of a log entry.
-   [MTChartBar](/en/docs/mt5/api/mtchartbar) — description of a chart bar.
-   [MTBookItem](/en/docs/mt5/api/mtbookitem) — description of an element of the Depth of Market.
-   [MTBook/MTBookDiff](/en/docs/mt5/api/mtbook) — description of the Depth of Market.
-   [MTGatewayInfo](/en/docs/mt5/api/mtgatewayinfo) — gateway/data feed module parameters.
-   [MTNews](/en/docs/mt5/api/mtnews) — news description.
-   [MTEconomicEvent](/en/docs/mt5/api/mteconomicevent) — description of a news of the economic calendar.
-   [MTReportInfo](/en/docs/mt5/api/mtreportinfo) — initial information about the report module.
-   [MTReportParam](/en/docs/mt5/api/mtreportparam) — module parameters.
-   [MTReportServerInfo](/en/docs/mt5/api/mtreportserverinfo) — information about the trading platform and the server.
-   [MTPluginInfo](/en/docs/mt5/api/mtplugininfo) — initial information about the plugin.
-   [MTPluginParam](/en/docs/mt5/api/mtpluginparam) — default parameters of the plugin.
-   [MTServerInfo](/en/docs/mt5/api/mtserverinfo) — information about the trading platform and the server.

[Subscriptions](/en/docs/mt5/api/retcodes_subscription)

[MTProxyInfo](/en/docs/mt5/api/mtproxyinfo)