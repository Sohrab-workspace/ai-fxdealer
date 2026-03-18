# IMTServerAPI::OrderUnsubscribe

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderunsubscribe

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
                        -   [OrderCreate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordercreate)
                        -   [OrderCreateArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordercreatearray)
                        -   [OrderSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordersubscribe)
                        -   [OrderUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderunsubscribe)
                        -   [OrderAdd](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderadd)
                        -   [OrderAddBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderaddbatch)
                        -   [OrderAddBatchArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderaddbatcharray)
                        -   [OrderUpdate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderupdate)
                        -   [OrderUpdateBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderupdatebatch)
                        -   [OrderUpdateBatchArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderupdatebatcharray)
                        -   [OrderDelete](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderdelete)
                        -   [OrderDeleteBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderdeletebatch)
                        -   [OrderCancel](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordercancel)
                        -   [OrderCancelBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordercancelbatch)
                        -   [OrderGet](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderget)
                        -   [OrderGetByGroup](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordergetbygroup)
                        -   [OrderGetByGroupSymbol](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordergetbygroupsymbol)
                        -   [OrderGetByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordergetbylogins)
                        -   [OrderGetByLoginsSymbol](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordergetbyloginssymbol)
                        -   [OrderGetByTickets](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordergetbytickets)
                        -   [OrderSelectByGroup](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderselectbygroup)
                        -   [OrderSelectByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderselectbylogins)
                        -   [HistorySubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historysubscribe)
                        -   [HistoryUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyunsubscribe)
                        -   [HistoryAdd](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyadd)
                        -   [HistoryAddBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyaddbatch)
                        -   [HistoryAddBatchArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyaddbatcharray)
                        -   [HistoryUpdate](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyupdate)
                        -   [HistoryUpdateBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyupdatebatch)
                        -   [HistoryUpdateBatchArray](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyupdatebatcharray)
                        -   [HistoryDelete](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historydelete)
                        -   [HistoryDeleteBatch](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historydeletebatch)
                        -   [HistoryGet](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyget)
                        -   [HistoryGetByGroup](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historygetbygroup)
                        -   [HistoryGetByGroupSymbol](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historygetbygroupsymbol)
                        -   [HistoryGetByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historygetbylogins)
                        -   [HistoryGetByLoginsSymbol](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historygetbyloginssymbol)
                        -   [HistoryGetByTickets](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historygetbytickets)
                        -   [HistorySelectByGroup](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyselectbygroup)
                        -   [HistorySelectByLogins](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyselectbylogins)
                        -   [HistoryReopen](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyreopen)
                    -   [Deals](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal)
                    -   [Positions](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position)
                    -   [Trade Requests](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_request)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)[Orders](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order)OrderUnsubscribe

# IMTServerAPI::OrderUnsubscribe

Unsubscribe from the events and hooks associated with changes in the database of open orders.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::OrderUnsubscribe</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTOrderSink*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">sink</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;IMTOrderSink&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

sink

\[in\]  A pointer to the object that implements the [IMTOrderSink](/en/docs/mt5/api/reference_trading/trading_order/imtordersink) interface.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

This is a pair method to [IMTServerAPI::OrderSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordersubscribe). If an attempt is made to unsubscribe from the interface to which it has not subscribed, [MT\_RET\_ERR\_NOTFOUND](/en/docs/mt5/api/retcodes_common) error is returned.

[OrderSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_ordersubscribe)

[OrderAdd](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderadd)