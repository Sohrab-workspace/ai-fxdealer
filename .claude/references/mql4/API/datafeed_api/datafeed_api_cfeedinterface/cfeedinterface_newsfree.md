# CFeedInterface::NewsRead

> Source: https://support.metaquotes.net/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_newsfree

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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[DataFeed API](/en/docs/mt4/api/datafeed_api)[СFeedInterface Methods](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface)NewsFree

# CFeedInterface::NewsRead

Releasing the memory allocated for the body of a new formate newsletter.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">void&nbsp;&nbsp;</span><span class="f_Functions">CFeedInterface::NewsRead</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">FeedNews*&nbsp;</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">news</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;News&nbsp;description</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

news

\[in\]  A pointer to the [FeedNews](/en/docs/mt4/api/reference_structures/structure_feed/feednews) structure describing the news of the new format.

Return Value

TRUE should be returned if read successfully, otherwise - FALSE.

Note

The function is used to free the memory allocated for the news body in the [CFeedInterface::NewsRead](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_newsread) method.

Example

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #339966;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #339966;">//|&nbsp;Freeing&nbsp;the&nbsp;memory&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #339966;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">CSourceInterface::NewsFree(FeedNews</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">*news)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #339966;">//---&nbsp;Checking</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(news==NULL</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">||</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">news-&gt;body==NULL)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">return</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample" style="color: #339966;">//---&nbsp;delete&nbsp;body</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">delete</span><span class="f_CodeExample">[]</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">news-&gt;body;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">news-&gt;body=NULL;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

[NewsRead](/en/docs/mt4/api/datafeed_api/datafeed_api_cfeedinterface/cfeedinterface_newsread)

[Report API](/en/docs/mt4/api/report_api)