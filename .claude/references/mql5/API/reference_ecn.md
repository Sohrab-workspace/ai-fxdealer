# The ECN

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_ecn

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
                -   [IMTECNMatching](/en/docs/mt5/api/reference_ecn/imtecnmatching)
                -   [IMTECNMatchingArray](/en/docs/mt5/api/reference_ecn/imtecnmatchingarray)
                -   [IMTECNFilling](/en/docs/mt5/api/reference_ecn/imtecnfilling)
                -   [IMTECNFillingArray](/en/docs/mt5/api/reference_ecn/imtecnfillingarray)
                -   [IMTECNProvider](/en/docs/mt5/api/reference_ecn/imtecnprovider)
                -   [IMTECNProviderArray](/en/docs/mt5/api/reference_ecn/imtecnproviderarray)
                -   [IMTECNHistoryMatching](/en/docs/mt5/api/reference_ecn/imtecnhistorymatching)
                -   [IMTECNHistoryMatchingArray](/en/docs/mt5/api/reference_ecn/imtecnhistorymatchingarray)
                -   [IMTECNHistoryFilling](/en/docs/mt5/api/reference_ecn/imtecnhistoryfilling)
                -   [IMTECNHistoryFillingArray](/en/docs/mt5/api/reference_ecn/imtecnhistoryfillingarray)
                -   [IMTECNHistoryDeal](/en/docs/mt5/api/reference_ecn/imtecnhistorydeal)
                -   [IMTECNHistoryDealArray](/en/docs/mt5/api/reference_ecn/imtecnhistorydealarray)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)ECN

# The ECN

MetaTrader 5 API provides access to [built-in ECN](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn) databases. Functions from these section enable the detailed analysis of the current matching queue and history, of operations with liquidity providers and other data.

-   [IMTECNMatching](/en/docs/mt5/api/reference_ecn/imtecnmatching) — [matching order](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#matching_orders_current) object interface.
-   [IMTECNMatchingArray](/en/docs/mt5/api/reference_ecn/imtecnmatchingarray) — interface for the array of matching orders.
-   [IMTECNFilling](/en/docs/mt5/api/reference_ecn/imtecnfilling) — [filling order](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#filling_orders_current) object interface.
-   [IMTECNFillingArray](/en/docs/mt5/api/reference_ecn/imtecnfillingarray) — interface for the array of filling orders.
-   [IMTECNProvider](/en/docs/mt5/api/reference_ecn/imtecnprovider) — interface for the [provider](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching#providers) via which the requests are executed.
-   [IMTECNProviderArray](/en/docs/mt5/api/reference_ecn/imtecnproviderarray) — interface for an array of providers.
-   [IMTECNHistoryMatching](/en/docs/mt5/api/reference_ecn/imtecnhistorymatching) — interface for the [matching order](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#matching_orders) object from history.
-   [IMTECNHistoryMatchingArray](/en/docs/mt5/api/reference_ecn/imtecnhistorymatchingarray) — interface for an array of objects of matching orders from history.
-   [IMTECNHistoryFilling](/en/docs/mt5/api/reference_ecn/imtecnhistoryfilling) — interface for the [filling order](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#filling_orders) object from history.
-   [IMTECNHistoryFillingArray](/en/docs/mt5/api/reference_ecn/imtecnhistoryfillingarray) — interface for an array of objects of filling orders from history.
-   [IMTECNHistoryDeal](/en/docs/mt5/api/reference_ecn/imtecnhistorydeal) — interface for the object of a [deal](https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_matching_history#deals) from the ECN history.
-   [IMTECNHistoryDealArray](/en/docs/mt5/api/reference_ecn/imtecnhistorydealarray) — interface for an array of objects of deals from the ECN history.

[WebReadParamDouble](/en/docs/mt5/api/reference_bytestream/imtbytestream/imtbytestream_webreadparamdouble)

[IMTECNMatching](/en/docs/mt5/api/reference_ecn/imtecnmatching)