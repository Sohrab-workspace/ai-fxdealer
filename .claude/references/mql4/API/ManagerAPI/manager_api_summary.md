# Summary Positions

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_summary

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
            -   [Application Development](/en/docs/mt4/api/manager_api/manager_api_dev)
            -   [Exported Functions and Factory](/en/docs/mt4/api/manager_api/manager_api_exported_factory)
            -   [Common Functions](/en/docs/mt4/api/manager_api/manager_api_common)
            -   [Connecting to the Server](/en/docs/mt4/api/manager_api/manager_api_connect)
            -   [Configuration Databases](/en/docs/mt4/api/manager_api/manager_api_config)
            -   [Server Management](/en/docs/mt4/api/manager_api/manager_api_server)
            -   [Price Data](/en/docs/mt4/api/manager_api/manager_api_chart)
            -   [Data Feeds](/en/docs/mt4/api/manager_api/manager_api_feeder)
            -   [Backup](/en/docs/mt4/api/manager_api/manager_api_backup)
            -   [Trading](/en/docs/mt4/api/manager_api/manager_api_trade)
            -   [Dealings](/en/docs/mt4/api/manager_api/manager_api_dealer)
            -   [Users](/en/docs/mt4/api/manager_api/manager_api_user)
            -   [Online Connections](/en/docs/mt4/api/manager_api/manager_api_online)
            -   [Symbols](/en/docs/mt4/api/manager_api/manager_api_symbol)
            -   [Mail, News and Notifications](/en/docs/mt4/api/manager_api/manager_api_newsmail)
            -   [Reports](/en/docs/mt4/api/manager_api/manager_api_report)
            -   [Summary Positions](/en/docs/mt4/api/manager_api/manager_api_summary)
                -   [SummaryGetAll](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetall)
                -   [SummaryGet](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summaryget)
                -   [SummaryGetByCount](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetbycount)
                -   [SummaryGetByType](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetbytype)
                -   [SummaryCurrency](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarycurrency)
            -   [Exposure](/en/docs/mt4/api/manager_api/manager_api_exposure)
            -   [Protocol Extension](/en/docs/mt4/api/manager_api/manager_api_extension)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Summary Positions

# Summary Positions

The functions described in this section allow to get information about cl;ients' summary positions and broker's hedge positions.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetall" class="topiclink">SummaryGetAll</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets information about summary positions for all symbols.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summaryget" class="topiclink">SummaryGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets information about the summary position on the symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetbycount" class="topiclink">SummaryGetByCount</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets information about the summary position by the index.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetbytype" class="topiclink">SummaryGetByType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets information about the summary positions on the symbols of a particular type.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarycurrency" class="topiclink">SummaryCurrency</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sets the currency, in which clients' summary positions for a symbol are calculated.</span></p></td></tr></tbody></table>

[DailySyncRead](/en/docs/mt4/api/manager_api/manager_api_report/cmanagerinterface_dailysyncread)

[SummaryGetAll](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetall)