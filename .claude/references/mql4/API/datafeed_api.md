# MetaTrader 4 DataFeed API

> Source: https://support.metaquotes.net/en/docs/mt4/api/datafeed_api

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
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
        -   [Development Features](/en/docs/mt4/api/features)
        -   [Structures](/en/docs/mt4/api/reference_structures)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
        -   [Manager API](/en/docs/mt4/api/manager_api)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
            -   [Development of Data Feeds](/en/docs/mt4/api/datafeed_api/datafeed_api_dev)
            -   [Exported Functions](/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function)
            -   [СFeedInterface Methods](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)DataFeed API

# MetaTrader 4 DataFeed API

The MetaTrader 4 DataFeed API allows developing news and quote data feeds.

Data Feeds are special libraries (DLL), which are used by the server to receive quotes and news. Each data feed should contain a required set of exported functions, which will call the server. At its core, a data feed is an intermediary between the MetaTrader server a data source. In most cases, the data source is represented by a provider server that uses a particular protocol. The data feeder converts data received in the protocol format into the MetaTrader 4 trading platform format.

-   [Development of Data Feeds](/en/docs/mt4/api/datafeed_api/datafeed_api_dev)
-   [Exported Functions](/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function)
-   [CFeedInterface Methods](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface)

[ExternalCommand](/en/docs/mt4/api/manager_api/manager_api_extension/cmanagerinterface_externalcommand)

[Development of Data Feeds](/en/docs/mt4/api/datafeed_api/datafeed_api_dev)