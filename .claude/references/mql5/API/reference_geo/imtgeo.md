# IMTGeo

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_geo/imtgeo

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Geo Services](/en/docs/mt5/api/reference_geo)IMTGeo

# IMTGeo

This interface provides access to information about the IP address, including the owner, geographic location, and other details.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_release" class="topiclink">Release</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the current object.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_assign" class="topiclink">Assign</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a passed object to the current one.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_clear" class="topiclink">Clear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear an object.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_ipv4from" class="topiclink">IPv4From</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the beginning of the range of IPv4 addresses.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_ipv4to" class="topiclink">IPv4To</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the end of the range of IPv4 addresses.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_ipv6from" class="topiclink">IPv6From</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the beginning of the range of IPv6 addresses.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_ipv6to" class="topiclink">IPv6To</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the end of the range of IPv6 addresses.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_continent" class="topiclink">Continent</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the continent where an IP address is located.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_country" class="topiclink">Country</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the country where an IP address is located.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_city" class="topiclink">City</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the city where an IP address is located.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_region" class="topiclink">Region</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the region where an IP address is located.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_province" class="topiclink">Province</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the province/state where an IP address is located.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_asn" class="topiclink">ASN</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the Autonomous System Number (ASN) to which an IP address belongs.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_asnorganization" class="topiclink">ASNOrganization</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the name of the autonomous system to which an IP address belongs.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_isp" class="topiclink">ISP</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the name of the internet service provider that owns an IP address.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_isporganization" class="topiclink">ISPOrganization</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the organization that owns an IP address.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_latitude" class="topiclink">Latitude</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the latitude for an IP address.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_longitude" class="topiclink">Longitude</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Getting longitude for an IP address.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_details" class="topiclink">Details</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get more information about an IP address.</span></p></td></tr></tbody></table>

The IMTGeo class contains the following enumerations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Enumeration</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:170px; height:16px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_enum#engeorequestflags" class="topiclink">EnGeoRequestFlags</a></span></p></td><td class="table" style="height:16px;"><p class="p_fortable"><span class="f_fortable">Types of data requested about an IP address.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_enum#engeorecorddetails" class="topiclink">EnGeoRecordDetails</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Flags for transmitting additional information about an IP address.</span></p></td></tr></tbody></table>

[Geo Services](/en/docs/mt5/api/reference_geo)

[Enumerations](/en/docs/mt5/api/reference_geo/imtgeo/imtgeo_enum)