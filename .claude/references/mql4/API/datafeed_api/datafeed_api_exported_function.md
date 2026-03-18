# Exported Functions

> Source: https://support.metaquotes.net/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function

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
                -   [DsVersion](/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dsversion)
                -   [DsCreate](/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dscreate)
                -   [DsCreateExt](/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/dscreateext)
                -   [DsDestroy](/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dsdestroy)
            -   [СFeedInterface Methods](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[DataFeed API](/en/docs/mt4/api/datafeed_api)Exported Functions

# Exported Functions

There are three exported data feed functions, which the server may call. If at least one of these functions is missing, the server will refuse to work with the data feed.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dsversion" class="topiclink">DsVersion</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Returns the description of a Data Feed.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dscreate" class="topiclink">DsCreate</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Passes a pointer to the newly created <a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface" class="topiclink">CFeedInterface</a> class.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/dscreateext" class="topiclink">DsCreateExt</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Passes a pointer to the newly created <a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_close" class="topiclink">CFeedInterface</a> class. An extended version additionally passing the server build and settings.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dsdestroy" class="topiclink">DsDestroy</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Destroys a data source object that was earlier created using<a href="/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dscreate" class="topiclink">DsCreate</a> and deletes it from the list of data sources.</span></p></td></tr></tbody></table>

[Development of Data Feeds](/en/docs/mt4/api/datafeed_api/datafeed_api_dev)

[DsVersion](/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dsversion)