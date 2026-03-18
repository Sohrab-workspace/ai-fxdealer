# Dealings

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_dealer

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
                -   [DealerSwitch](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerswitch)
                -   [DealerRequestGet](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerrequestget)
                -   [DealerSend](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealersend)
                -   [DealerReject](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerreject)
                -   [DealerReset](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerreset)
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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Dealings

# Dealings

The MetaTrader 4 Manager API allows you to perform dealing using a special set of functions. The functions described in this section allow connecting to a queue of requests on a trading server, selecting requests from the queue and processing them in accordance with preset algorithms.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerswitch" class="topiclink">DealerSwitch</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Switching the manager interface to the dealing mode.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerrequestget" class="topiclink">DealerRequestGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives a trade request to process from the queue.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealersend" class="topiclink">DealerSend</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Confirms or requots a trade request.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerreject" class="topiclink">DealerReject</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Rejects a trade request.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerreset" class="topiclink">DealerReset</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns a trade request to the queue to allow another dealer process the request.</span></p></td></tr></tbody></table>

[TradesSnapshot](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_service/cmanagerinterface_tradessnapshot)

[DealerSwitch](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerswitch)