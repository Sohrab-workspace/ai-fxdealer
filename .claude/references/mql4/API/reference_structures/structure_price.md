# Price Data

> Source: https://support.metaquotes.net/en/docs/mt4/api/reference_structures/structure_price

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
            -   [Configuration Databases](/en/docs/mt4/api/reference_structures/structure_config)
            -   [Plugins](/en/docs/mt4/api/reference_structures/structure_plugin)
            -   [Trading](/en/docs/mt4/api/reference_structures/structure_trade)
            -   [Users](/en/docs/mt4/api/reference_structures/structure_user)
            -   [Data Feeds](/en/docs/mt4/api/reference_structures/structure_feed)
            -   [Journal](/en/docs/mt4/api/reference_structures/structure_journal)
            -   [Price Data](/en/docs/mt4/api/reference_structures/structure_price)
                -   [RateInfo](/en/docs/mt4/api/reference_structures/structure_price/rateinfo)
                -   [TickAPI](/en/docs/mt4/api/reference_structures/structure_price/tickapi)
                -   [ChartInfo](/en/docs/mt4/api/reference_structures/structure_price/chartinfo)
                -   [TickRecord](/en/docs/mt4/api/reference_structures/structure_price/tickrecord)
                -   [TickRequest](/en/docs/mt4/api/reference_structures/structure_price/tickrequest)
                -   [TickInfo](/en/docs/mt4/api/reference_structures/structure_price/tickinfo)
            -   [Mail and News](/en/docs/mt4/api/reference_structures/structure_news_mail)
            -   [Reports](/en/docs/mt4/api/reference_structures/structure_report)
            -   [Symbols](/en/docs/mt4/api/reference_structures/structure_symbol)
            -   [Auxiliary Structures](/en/docs/mt4/api/reference_structures/structure_auxiliary)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
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

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Structures](/en/docs/mt4/api/reference_structures)Price Data

# Price Data

The section contains descriptions of structures used for working with price bars and ticks.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:148px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Structure</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:148px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_structures/structure_price/rateinfo" class="topiclink">RateInfo</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Description of bars.</span></p></td></tr><tr class="table"><td class="table" style="width:148px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_structures/structure_price/tickapi" class="topiclink">TickAPI</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Tick description.</span></p></td></tr><tr class="table"><td class="table" style="width:148px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_structures/structure_price/chartinfo" class="topiclink">ChartInfo</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Description of bar requests.</span></p></td></tr><tr class="table"><td class="table" style="width:148px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_structures/structure_price/tickrecord" class="topiclink">TickRecord</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Describes the tick added by a data feed or by a dealer.</span></p></td></tr><tr class="table"><td class="table" style="width:148px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_structures/structure_price/tickrequest" class="topiclink">TickRequest</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Description of tick requests.</span></p></td></tr><tr class="table"><td class="table" style="width:148px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/reference_structures/structure_price/tickinfo" class="topiclink">TickInfo</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Tick description, used to retrieve the last tick of a symbol.</span></p></td></tr></tbody></table>

[ServerLog](/en/docs/mt4/api/reference_structures/structure_journal/serverlog)

[RateInfo](/en/docs/mt4/api/reference_structures/structure_price/rateinfo)