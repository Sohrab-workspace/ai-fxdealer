# IMTServerAPI::TradeSubscribe

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradesubscribe

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
            -   [Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)
            -   [Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)
            -   [Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)
            -   [Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)
            -   [Hooks](/en/docs/mt5/api/serverapi_hooks)
            -   [Request Processing on the Server](/en/docs/mt5/api/hook_scheme)
            -   [Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)
            -   [Debugging](/en/docs/mt5/api/serverapi_debug)
            -   [Ready-made Examples](/en/docs/mt5/api/serverapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reference_entrypoints)
            -   [Plugin Interface](/en/docs/mt5/api/imtserverplugin)
            -   [Main API Interface](/en/docs/mt5/api/imtserverapi)
                -   [Common Functions](/en/docs/mt5/api/imtserverapi/serverapi_common)
                -   [Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)
                -   [Clients](/en/docs/mt5/api/imtserverapi/serverapi_clients)
                -   [Users](/en/docs/mt5/api/imtserverapi/serverapi_users)
                -   [Online Connections](/en/docs/mt5/api/imtserverapi/serverapi_online)
                -   [Certificates](/en/docs/mt5/api/imtserverapi/serverapi_certificate)
                -   [Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)
                    -   [Orders](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order)
                    -   [Deals](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal)
                    -   [Positions](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position)
                    -   [Trade Requests](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request)
                        -   [TradeRequestCreate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_traderequestcreate)
                        -   [TradeRequestCreateArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_traderequestcreatearray)
                        -   [TradeConfirmCreate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeconfirmcreate)
                        -   [TradeExecutionCreate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeexecutioncreate)
                        -   [TradeSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradesubscribe)
                        -   [TradeUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeunsubscribe)
                        -   [TradeRequest](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_traderequest)
                        -   [TradeProfit](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeprofit)
                        -   [TradeProfitExt](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeprofitext)
                        -   [TradeRateBuy](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_traderatebuy)
                        -   [TradeRateSell](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_traderatesell)
                        -   [TradeMarginCheck](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_trademargincheck)
                        -   [TradeMarginCheckExt](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_trademargincheckext)
                        -   [TradeBalanceCheck](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradebalancecheck)
                        -   [TradeSubscribeEOD](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradesubscribeeod)
                        -   [TradeUnsubscribeEOD](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeunsubscribeeod)
                        -   [TradeAccountSet](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeaccountset)
                    -   [Request Processing](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_dealer)
                -   [History Data](/en/docs/mt5/api/imtserverapi/serverapi_chart)
                -   [Tick Data](/en/docs/mt5/api/imtserverapi/serverapi_ticks)
                -   [Depth of Market](/en/docs/mt5/api/imtserverapi/serverapi_book)
                -   [Mail Database](/en/docs/mt5/api/imtserverapi/serverapi_mail)
                -   [News Database](/en/docs/mt5/api/imtserverapi/serverapi_news)
                -   [Daily Reports](/en/docs/mt5/api/imtserverapi/serverapi_trading_daily)
                -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_subscription)
                -   [Server Services](/en/docs/mt5/api/imtserverapi/serverapi_server_services)
                -   [Geo Services](/en/docs/mt5/api/imtserverapi/serverapi_geo)
                -   [Dataset](/en/docs/mt5/api/imtserverapi/serverapi_dataset)
                -   [Custom Functions](/en/docs/mt5/api/imtserverapi/serverapi_custom)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
            -   [Interface of End-of-Day Events](/en/docs/mt5/api/imtendofdaysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)[Trade Requests](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request)TradeSubscribe

# IMTServerAPI::TradeSubscribe

Subscribe to events and hooks associated with trade requests.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::TradeSubscribe</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTTradeSink*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">sink</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;IMTTradeSink&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

sink

\[in\]  A pointer to the object that implements the [IMTTradeSink](/en/docs/mt5/api/imttradesink) interface.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

Subscribing to events is thread safe. One and the same interface [IMTTradeSink](/en/docs/mt5/api/imttradesink) cannot subscribe to an event twice - in this case the response code [MT\_RET\_ERR\_DUPLICATE](/en/docs/mt5/api/retcodes_common) is returned.

The object at which sink points, must remain in the memory (must not be removed) until the call of [IMTServerAPI::TradeUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeunsubscribe) or until the plugin is deleted.

[TradeExecutionCreate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeexecutioncreate)

[TradeUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request/imtserverapi_tradeunsubscribe)