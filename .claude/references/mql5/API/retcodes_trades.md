# Trade management

> Source: https://support.metaquotes.net/en/docs/mt5/api/retcodes_trades

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
            -   [Successful completion](/en/docs/mt5/api/retcodes_successful)
            -   [Common errors](/en/docs/mt5/api/retcodes_common)
            -   [Authentication](/en/docs/mt5/api/retcodes_authentication)
            -   [Configuration Management](/en/docs/mt5/api/retcodes_configs)
            -   [User management](/en/docs/mt5/api/retcodes_clients)
            -   [Trade management](/en/docs/mt5/api/retcodes_trades)
            -   [Report Generation](/en/docs/mt5/api/retcodes_reports)
            -   [Price Data](/en/docs/mt5/api/retcodes_price_history)
            -   [Trade Requests](/en/docs/mt5/api/retcodes_trade_request)
            -   [Dealer](/en/docs/mt5/api/retcodes_dealer)
            -   [API](/en/docs/mt5/api/retcodes_api)
            -   [Messengers](/en/docs/mt5/api/retcodes_messenger)
            -   [Subscriptions](/en/docs/mt5/api/retcodes_subscription)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Return Codes](/en/docs/mt5/api/reference_retcodes)Trade management

# Trade management

This group of codes is returned by the server when working with [a database of trades](/en/docs/mt5/api/imtadminapi/imtadminapi_trading):

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Constant</span></p></th><th class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_LIMIT_REACHED</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4001</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Reached the limit on the number of orders or deals.</span></p></td></tr><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_ORDER_EXIST</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4002</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The order already exists.</span></p></td></tr><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_ORDER_EXHAUSTED</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4003</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The range of orders has been exhausted.</span></p></td></tr><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_DEAL_EXHAUSTED</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4004</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The range of deals has been exhausted.</span></p></td></tr><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_MAX_MONEY</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4005</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Reached the limit on the amount of money.</span></p></td></tr><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_DEAL_EXIST</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4006</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A deal with this ticket already exists on this trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_ORDER_PROHIBITED</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4007</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The order identifier is reserved for use on another trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_DEAL_PROHIBITED</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4008</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The deal identifier is reserved for use on another trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:230px;"><p class="p_fortable"><span class="f_fortable">MT_RET_TRADE_SPLIT_VOLUME</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">4009</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The position volume will become zero after the split operation. The error is used in the following methods:</span></p><ul><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionsplit" class="topiclink">IMTServerAPI::PositionSplit</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtadminapi/imtadminapi_trading/imtadminapi_trading_position/imtadminapi_positionsplit" class="topiclink">IMTAdmin::PositionSplit</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position/imtmanagerapi_positionsplit" class="topiclink">IMTManager::PositionSplit</a></span></li></ul><p class="p_fortable"><span class="f_fortable">If the split operation will cause a position volume to become zero, the split will not be performed, and the MT_RET_TRADE_SPLIT_VOLUME error code will be added to the 'results' return array.</span></p></td></tr></tbody></table>

[User management](/en/docs/mt5/api/retcodes_clients)

[Report Generation](/en/docs/mt5/api/retcodes_reports)