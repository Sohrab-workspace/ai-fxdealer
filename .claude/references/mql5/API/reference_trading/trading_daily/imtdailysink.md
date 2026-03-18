# IMTDailySink

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
            -   [Trade](/en/docs/mt5/api/reference_trading)
                -   [General Principles](/en/docs/mt5/api/reference_trading/general_concept)
                -   [Orders](/en/docs/mt5/api/reference_trading/trading_order)
                -   [Deals](/en/docs/mt5/api/reference_trading/trading_deal)
                -   [Positions](/en/docs/mt5/api/reference_trading/trading_position)
                -   [Accounts](/en/docs/mt5/api/reference_trading/user_account)
                -   [Trade Requests](/en/docs/mt5/api/reference_trading/trading_request)
                -   [Summary Positions](/en/docs/mt5/api/reference_trading/trading_summary)
                -   [Assets](/en/docs/mt5/api/reference_trading/trading_exposure)
                -   [Daily Reports](/en/docs/mt5/api/reference_trading/trading_daily)
                    -   [IMTDaily](/en/docs/mt5/api/reference_trading/trading_daily/imtdaily)
                    -   [IMTDailyArray](/en/docs/mt5/api/reference_trading/trading_daily/imtdailyarray)
                    -   [IMTDailySink](/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink)
                        -   [OnDailyAdd](/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailyadd)
                        -   [OnDailyUpdate](/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailyupdate)
                        -   [OnDailyDelete](/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailydelete)
                        -   [OnDailyClear](/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailyclean)
                        -   [OnDailySync](/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailysync)
            -   [Clients](/en/docs/mt5/api/reference_client)
            -   [Users](/en/docs/mt5/api/reference_user)
            -   [Online Connections](/en/docs/mt5/api/reference_online)
            -   [Certificates](/en/docs/mt5/api/reference_certificate)
            -   [Price Data](/en/docs/mt5/api/reference_ticks)
            -   [Depth of Market](/en/docs/mt5/api/reference_dom)
            -   [Mail Database](/en/docs/mt5/api/reference_mail)
            -   [News Database](/en/docs/mt5/api/reference_news)
            -   [Byte Stream](/en/docs/mt5/api/reference_bytestream)
            -   [ECN](/en/docs/mt5/api/reference_ecn)
            -   [Subscriptions](/en/docs/mt5/api/reference_subscription)
            -   [Geo Services](/en/docs/mt5/api/reference_geo)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Database Interfaces](/en/docs/mt5/api/reference_bases)[Trade](/en/docs/mt5/api/reference_trading)[Daily Reports](/en/docs/mt5/api/reference_trading/trading_daily)IMTDailySink

# IMTDailySink

The IMTDailySink class contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:104px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:104px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailyadd" class="topiclink">OnDailyAdd</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of adding a new daily report.</span></p></td></tr><tr class="table"><td class="table" style="width:104px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailyupdate" class="topiclink">OnDailyUpdate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of updating a daily report.</span></p></td></tr><tr class="table"><td class="table" style="width:104px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailydelete" class="topiclink">OnDailyDelete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of removing a daily report.</span></p></td></tr><tr class="table"><td class="table" style="width:104px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailyclean" class="topiclink">OnDailyClean</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of clearing of a client's daily reports.</span></p></td></tr><tr class="table"><td class="table" style="width:104px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailysync" class="topiclink">OnDailySync</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A handler of the event of synchronization of a database of daily reports.</span></p></td></tr></tbody></table>

The methods of the IMTDailySink interface are used in Server and Report API only.

[SearchRight](/en/docs/mt5/api/reference_trading/trading_daily/imtdailyarray/imtdailyarray_searchright)

[OnDailyAdd](/en/docs/mt5/api/reference_trading/trading_daily/imtdailysink/imtdailysink_ondailyadd)