# Price Data

> Source: https://support.metaquotes.net/en/docs/mt4/api/server_api/server_api_chart

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
            -   [Development of Plugins](/en/docs/mt4/api/server_api/server_api_dev)
            -   [Common Functions](/en/docs/mt4/api/server_api/server_api_common)
            -   [Configuration Databases](/en/docs/mt4/api/server_api/server_api_config)
            -   [Users](/en/docs/mt4/api/server_api/server_api_user)
            -   [Trading](/en/docs/mt4/api/server_api/server_api_trading)
            -   [Price Data](/en/docs/mt4/api/server_api/server_api_chart)
                -   [HistoryAddTick](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyaddtick)
                -   [HistoryLastTicks](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historylastticks)
                -   [HistoryPrices](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyprices)
                -   [HistoryPricesGroup](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historypricesgroup)
                -   [HistorySync](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historysync)
                -   [HistoryUpdateObsolete](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyupdateobsolete)
                -   [HistoryQuotesObsolete](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyquotesobsolete)
                -   [HistoryUpdate](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyupdate)
                -   [HistoryQuotes](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyquotes)
                -   [HistoryTicksGet](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyticksget)
            -   [Mail, News and Notifications](/en/docs/mt4/api/server_api/server_api_mail_news)
            -   [Daily Reports](/en/docs/mt4/api/server_api/server_api_reference_daily)
            -   [Server Services](/en/docs/mt4/api/server_api/server_api_server_services)
            -   [Hooks](/en/docs/mt4/api/server_api/server_api_hook)
        -   [Manager API](/en/docs/mt4/api/manager_api)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Server API](/en/docs/mt4/api/server_api)Price Data

# Price Data

MetaTrader 4 Server API contains functions for working with the history price data of the platform available in the form of one-minute bars and ticks.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyaddtick" class="topiclink">HistoryAddTick</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Adds a quote to the price stream.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historylastticks" class="topiclink">HistoryLastTicks</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives the latest symbol quotes since the start of the trading server.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyprices" class="topiclink">HistoryPrices</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Retrieves information about the current symbol prices: the current prices, the latest quote time and the direction of the last price change.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historypricesgroup" class="topiclink">HistoryPricesGroup</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives current prices of a symbol taking into account the specified group settings.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historysync" class="topiclink">HistorySync</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Starts history synchronization on the trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyupdateobsolete" class="topiclink">HistoryUpdateObsolete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">An obsolete method. Adds, edits and deletes history data of a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyquotesobsolete" class="topiclink">HistoryQuotesObsolete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">An obsolete method. Receives all bars of the specified timeframe and symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyupdate" class="topiclink">HistoryUpdate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Adds, edits and deletes history data of a symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyquotes" class="topiclink">HistoryQuotes</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives all bars of the specified timeframe and symbol.</span></p></td></tr><tr class="table"><td class="table" style="width:151px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyticksget" class="topiclink">HistoryTicksGet</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receives tick data of a symbol for the specified period.</span></p></td></tr></tbody></table>

[TradesCheckTickSize](/en/docs/mt4/api/server_api/server_api_trading/server_api_trading_check/cserverinterface_tradescheckticksize)

[HistoryAddTick](/en/docs/mt4/api/server_api/server_api_chart/cserverinterface_historyaddtick)