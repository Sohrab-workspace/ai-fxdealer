# IMTGeo::ASN

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_asn

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
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
            -   [Trade](/en/docs/mt5/api/reference_trading)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
                -   [IMTGeo](/en/docs/mt5/api/reference_geo/imtgeo)
                    -   [Enumerations](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_enum)
                    -   [Release](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_release)
                    -   [Assign](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_assign)
                    -   [Clear](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_clear)
                    -   [IPv4From](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_ipv4from)
                    -   [IPv4To](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_ipv4to)
                    -   [IPv6From](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_ipv6from)
                    -   [IPv6To](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_ipv6to)
                    -   [Continent](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_continent)
                    -   [Country](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_country)
                    -   [City](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_city)
                    -   [Region](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_region)
                    -   [Province](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_province)
                    -   [ASN](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_asn)
                    -   [ASNOrganization](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_asnorganization)
                    -   [ISP](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_isp)
                    -   [ISPOrganization](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_isporganization)
                    -   [Latitude](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_latitude)
                    -   [Longitude](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_longitude)
                    -   [Details](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_details)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Geo Services](/en/docs/mt5/api/reference_geo)[IMTGeo](/en/docs/mt5/api/reference_geo/imtgeo)ASN

# IMTGeo::ASN

Get the [Autonomous System Number](https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_\(%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82\)) (ASN) to which an IP address belongs.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">UINT64&nbsp;&nbsp;</span><span class="f_Functions">IMTGeo::ASN</span><span class="f_CodeExample">()</span><span class="f_Keywords">&nbsp;&nbsp;const</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">ulong&nbsp;&nbsp;</span><span class="f_Functions">CIMTGeo.ASN</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Return Value

The Autonomous System Number (ASN) to which an IP address belongs.

[Province](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_province)

[ASNOrganization](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_asnorganization)