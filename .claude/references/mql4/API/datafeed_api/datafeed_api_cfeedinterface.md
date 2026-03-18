# CFeedInterface Methods

> Source: https://support.metaquotes.net/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface

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
                -   [Connect](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_connect)
                -   [Close](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_close)
                -   [SetSymbols](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_setsymbols)
                -   [Read](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_read)
                -   [Journal](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_journal)
                -   [NewsRead](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_newsread)
                -   [NewsFree](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_newsfree)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[DataFeed API](/en/docs/mt4/api/datafeed_api)СFeedInterface Methods

# CFeedInterface Methods

The abstract class CFeedInterface provides a uniform operation of the server with any data feed regardless of its internal implementation. The server calls methods of the CFeedInterface class in a definite order, while the internal data feed implementation provides proper processing.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_connect" class="topiclink">Connect</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_dev#connect" class="topiclink">Connects</a> to a source server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_close" class="topiclink">Close</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_dev#close" class="topiclink">Closes</a> connection with the source server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_setsymbols" class="topiclink">SetSymbols</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Saves <a href="/en/docs/mt4/api/datafeed_api/datafeed_api_dev#setsymbols" class="topiclink">preferred symbols</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_read" class="topiclink">Read</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_dev#read" class="topiclink">Reads</a> the data stream.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_journal" class="topiclink">Journal</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Passing the data feed operation <a href="/en/docs/mt4/api/datafeed_api/datafeed_api_dev#journal" class="topiclink">Journal</a> to the trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_newsread" class="topiclink">NewsRead</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Reading news data of a new format.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_newsfree" class="topiclink">NewsFree</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Releasing the memory allocated for the body of a new formate newsletter.</span></p></td></tr></tbody></table>

[DsDestroy](/en/docs/mt4/api/datafeed_api/datafeed_api_exported_function/datafeed_api_dsdestroy)

[Connect](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_connect)