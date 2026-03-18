# IMTReportAPI::GeoResolveAny

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtreportapi/imtreportapi_geo/imtreportapi_georesolvebatch

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
            -   [Purpose of the Report API](/en/docs/mt5/api/reportapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/reportapi_interaction)
            -   [Configuration of Reports](/en/docs/mt5/api/reportapi_configuration)
            -   [Request for Reports](/en/docs/mt5/api/reportapi_request)
            -   [Requirements for Modules](/en/docs/mt5/api/reportapi_requirements)
            -   [Creating a Simple Report](/en/docs/mt5/api/reportapi_simple_report)
            -   [Tabular Reports](/en/docs/mt5/api/reportapi_tables)
            -   [HTML Reports](/en/docs/mt5/api/reportapi_html)
            -   [Dashboards](/en/docs/mt5/api/reportapi_dashboards)
            -   [Templates](/en/docs/mt5/api/reportapi_html_template)
            -   [Charts](/en/docs/mt5/api/reportapi_html_charts)
            -   [Memory Management](/en/docs/mt5/api/reportapi_memory_management)
            -   [Multithreading](/en/docs/mt5/api/reportapi_multithreading)
            -   [Ready-made Examples](/en/docs/mt5/api/reportapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reportapi_entrypoints)
            -   [Report Plugin Interface](/en/docs/mt5/api/imtreportcontext)
            -   [Main Interface of Reports](/en/docs/mt5/api/imtreportapi)
                -   [Enumerations](/en/docs/mt5/api/imtreportapi/imtreportapi_enum)
                -   [Common Functions](/en/docs/mt5/api/imtreportapi/imtreportapi_common)
                -   [Report Parameters](/en/docs/mt5/api/imtreportapi/imtreportapi_parameters)
                -   [HTML Reports](/en/docs/mt5/api/imtreportapi/imtreportapi_html)
                -   [Tabular Reports](/en/docs/mt5/api/imtreportapi/imtreportapi_table)
                -   [Dashboards](/en/docs/mt5/api/imtreportapi/imtreportapi_dashboard)
                -   [Configuration Databases](/en/docs/mt5/api/imtreportapi/imtreportapi_config)
                -   [Clients](/en/docs/mt5/api/imtreportapi/imtreportapi_client)
                -   [Users](/en/docs/mt5/api/imtreportapi/imtreportapi_user)
                -   [Trade Databases](/en/docs/mt5/api/imtreportapi/imtreportapi_trade)
                -   [Daily Reports](/en/docs/mt5/api/imtreportapi/imtreportapi_daily)
                -   [Price Data](/en/docs/mt5/api/imtreportapi/imtreportapi_price)
                -   [Dataset](/en/docs/mt5/api/imtreportapi/imtreportapi_dataset)
                -   [Data cache](/en/docs/mt5/api/imtreportapi/imtreportapi_cache)
                -   [Subscriptions](/en/docs/mt5/api/imtreportapi/imtreportapi_subscription)
                -   [Geo Services](/en/docs/mt5/api/imtreportapi/imtreportapi_geo)
                    -   [GeoCreate](/en/docs/mt5/api/imtreportapi/imtreportapi_geo/imtreportapi_geocreate)
                    -   [GeoResolve](/en/docs/mt5/api/imtreportapi/imtreportapi_geo/imtreportapi_georesolve)
                    -   [GeoResolveBatch](/en/docs/mt5/api/imtreportapi/imtreportapi_geo/imtreportapi_georesolvebatch)
            -   [Dashboard Interfaces](/en/docs/mt5/api/reportapi_dashboard)
            -   [Diagram Interfaces](/en/docs/mt5/api/reportapi_auxiliary)
            -   [Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)
            -   [Data Cache Interfaces](/en/docs/mt5/api/reportapi_cache)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Main Interface of Reports](/en/docs/mt5/api/imtreportapi)[Geo Services](/en/docs/mt5/api/imtreportapi/imtreportapi_geo)GeoResolveBatch

# IMTReportAPI::GeoResolveAny

Resolve a list of IP addresses of any type: IPv4 or IPv6.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTReportAPI::GeoResolveAny</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">addresses</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;array&nbsp;of&nbsp;IP&nbsp;addresses</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">addresses_total</span><span class="f_CodeExample">,&nbsp;</span><span class="f_Comments">//&nbsp;number&nbsp;of&nbsp;addresses</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">flags</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;flags</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTGeo**</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">records</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;description&nbsp;of&nbsp;IP&nbsp;addresses</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTAPIRES*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">results</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;array&nbsp;of&nbsp;results</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

addresses

\[in\]  Array of addresses of any type: IPv4 or IPv6.

addresses\_total

\[in\]  Number of addresses in the 'addresses' array.

flags

\[in\]  Additional resolution parameters in the form of flags from the [IMTGeo::EnGeoRequestFlags](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_enum#engeorequestflags) enumeration.

records

\[out\]  Description of IP addresses as an array of [IMTGeo](/en/docs/mt5/api/reference_geo/imtgeo) objects. The objects must be first created by the [IMTReportAPI::GeoCreate](/en/docs/mt5/api/imtreportapi/imtreportapi_geo/imtreportapi_geocreate) method.

results

\[out\]  Array with the address resolution results. The size of the 'results' array must not be less than that of 'addresses'.

Return Value

The [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code indicates that all specified addresses have been processed. The [MT\_RET\_ERR\_PARTIAL](/en/docs/mt5/api/retcodes_common) response code indicates that resolution results are only available for some of the addresses. Analyze the 'results' array for more details on the execution results. It contains the result of processing of each address from the 'addresses' array. The result index corresponds to the address index in the source array.

Note

In 'addresses' you can simultaneously transfer IP addresses of both types.

[GeoResolve](/en/docs/mt5/api/imtreportapi/imtreportapi_geo/imtreportapi_georesolve)

[Dashboard Interfaces](/en/docs/mt5/api/reportapi_dashboard)