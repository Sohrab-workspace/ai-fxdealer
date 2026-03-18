# Price Data

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_chart

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
                -   [ChartRequest](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartrequest)
                -   [ChartAdd](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartadd)
                -   [ChartUpdate](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartupdate)
                -   [ChartDelete](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartdelete)
                -   [TicksRequest](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_ticksrequest)
                -   [TickInfoLast](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_tickinfolast)
                -   [HistoryCorrect](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_historycorrect)
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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Price Data

# Price Data

MetaTrader 4 Manager API contains functions for working with the history price data of the platform available in the form of one-minute bars and ticks.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartrequest" class="topiclink">ChartRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives new price data of the specified timeframe and symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartadd" class="topiclink">ChartAdd</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Adds history data of a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartupdate" class="topiclink">ChartUpdate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Edits history data of a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartdelete" class="topiclink">ChartDelete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Deletes history data of a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_ticksrequest" class="topiclink">TicksRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives tick data of a symbol for the specified period.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_tickinfolast" class="topiclink">TickInfoLast</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets last ticks of a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_historycorrect" class="topiclink">HistoryCorrect</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Starts checking and rebuilding the bars of higher timeframes based on smaller timeframe bars.</span></p></td></tr></tbody></table>

[ServerTime](/en/docs/mt4/api/manager_api/manager_api_server/cmanagerinterface_servertime)

[ChartRequest](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartrequest)