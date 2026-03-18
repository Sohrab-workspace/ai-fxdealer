# Symbols

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_symbol

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
                -   [SymbolsRefresh](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsrefresh)
                -   [SymbolsGetAll](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsgetall)
                -   [SymbolGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolget)
                -   [SymbolInfoGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolinfoget)
                -   [SymbolInfoUpdated](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolinfoupdated)
                -   [SymbolAdd](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symboladd)
                -   [SymbolHide](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolhide)
                -   [SymbolSendTick](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsendtick)
                -   [SymbolChange](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolchange)
                -   [SymbolsGroupsGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsgroupsget)
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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Symbols

# Symbols

The functions described in this section allow users to create an analogue of the "Market Watch" window in applications developed using the Manager API. The main purpose of managing the list of selected symbols is a control of the incoming price stream delivered to the application. In other words, the application only receives prices of selected symbols. It is also possible to receive and modify symbol settings, as well as add quotes.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsrefresh" class="topiclink">SymbolsRefresh</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives the list of all symbols from the trading server.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsgetall" class="topiclink">SymbolsGetAll</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets configurations of all symbols.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolget" class="topiclink">SymbolGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets the symbol configuration by the name.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolinfoget" class="topiclink">SymbolInfoGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets a short description of a symbol selected in "Market Watch".</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolinfoupdated" class="topiclink">SymbolInfoUpdated</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets a brief information about all symbols selected in "Market Watch".</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symboladd" class="topiclink">SymbolAdd</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Adds a symbol to the list of selected symbols in "Market Watch".</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolhide" class="topiclink">SymbolHide</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Removes a symbol from the list of selected symbols in "Market Watch".</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsendtick" class="topiclink">SymbolSendTick</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Adds quotes to the price stream of a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolchange" class="topiclink">SymbolChange</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Edits symbol settings (spread , execution mode, limit &amp; stop level, background color).</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsgroupsget" class="topiclink">SymbolsGroupsGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gets the description of symbol groups in pumping.</span></p></td></tr></tbody></table>

[OnlineRecordGet](/en/docs/mt4/api/manager_api/manager_api_online/cmanagerinterface_onlinerecordget)

[SymbolsRefresh](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsrefresh)