# Enumerations

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_enum

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
            -   [Interaction of the Platform and Gateway API](/en/docs/mt5/api/gatewayapi_interaction)
            -   [Trade Operations in Gateway API](/en/docs/mt5/api/gatewayapi_trade_processing)
            -   [Development and Debugging of Gateways](/en/docs/mt5/api/gatewayapi_develop_gateway)
            -   [Symbol and Price Translation](/en/docs/mt5/api/gatewayapi_translation)
            -   [Development of Data Feeds](/en/docs/mt5/api/gatewayapi_develop_datafeed)
            -   [.NET Implementation](/en/docs/mt5/api/gatewayapi_net)
            -   [Exported Functions](/en/docs/mt5/api/gatewayapi_exported)
            -   [CMTGatewayAPIFactory](/en/docs/mt5/api/cmtgatewayapifactory)
            -   [Main Interface](/en/docs/mt5/api/imtgatewayapi)
                -   [Enumerations](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_enum)
                -   [Common Functions](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_common)
                -   [Server](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_server)
                -   [External Connection State](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_state)
                -   [Client Connection](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_client)
                -   [Quote and News Feeds](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_send)
                -   [History Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_ticks)
                -   [Users](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user)
                -   [Configuration Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_config)
                -   [Trade Databases](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading)
                -   [Trade Requests](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request)
                -   [Gateway Symbols](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_gateway_symbols)
                -   [Processing Trade Requests](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing)
                -   [Controlling Positions in External System](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_position_control)
                -   [Controlling Orders in External System](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_order_control)
                -   [Synchronizing Trading Data](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_user_control)
                -   [Mail Database](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_mail)
                -   [User Settings](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_settings)
            -   [Event Interface](/en/docs/mt5/api/imtgatewaysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Main Interface](/en/docs/mt5/api/imtgatewayapi)Enumerations

# Enumerations

The following enumerations are provided in the IMTGatewayAPI interface:

-   [IMTGatewayAPI::EnDealerRequestFlags](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_enum#endealerrequestflags)
-   [IMTGatewayAPI::EnConnectType](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_enum#enconnecttype)

## IMTGatewayAPI::EnDealerRequestFlags [#](imtgatewayapi_enum#endealerrequestflags)

The flags describing additional options for a gateway connection as a dealer are listed in IMTGatewayAPI::EnDealerRequestFlags:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">DEALER_FLAG_NONE</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0x00000000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">No additional connection flags.</span></p></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">DEALER_FLAG_AUTOLOCK</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0x00000001</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Capture new requests from the queue automatically.</span></p></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">DEALER_FLAG_USER</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0x00000002</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Additionally, get the data on the user who sent a request. In case this flag is turned on, users data will be transferred to the const IMTUser&nbsp;*user parameter of the following methods:</span></p><ul><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock" class="topiclink">IMTGatewaySink::OnDealerLock</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestnext" class="topiclink">IMTGatewayAPI::RequestNext</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestget" class="topiclink">IMTGatewayAPI::RequestGet</a></span></li></ul></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">DEALER_FLAG_ACCOUNT</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0x00000004</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Additionally, get trading account data of the user who sent a request. In case this flag is turned on, trading account data will be transferred to the const IMTAccount&nbsp;*account parameter of the following methods:</span></p><ul><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock" class="topiclink">IMTGatewaySink::OnDealerLock</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestnext" class="topiclink">IMTGatewayAPI::RequestNext</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestget" class="topiclink">IMTGatewayAPI::RequestGet</a></span></li></ul></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">DEALER_FLAG_ORDER</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0x00000008</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Additionally, get the data on the order that corresponds to the submitted request. In case this flag is turned on, the data on the order will be transferred to the const IMTOrder&nbsp;*order parameter of the following methods:</span></p><ul><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock" class="topiclink">IMTGatewaySink::OnDealerLock</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestnext" class="topiclink">IMTGatewayAPI::RequestNext</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestget" class="topiclink">IMTGatewayAPI::RequestGet</a></span></li></ul><p class="p_fortable"><span class="f_fortable">Note:</span></p><ul><li class="p_fortable"><span class="f_fortable">Actual prices in the platform are specified in the 'order' parameter without regard to translation parameters (<a href="/en/docs/mt5/api/config_gateway/imtcongatewaytranslate" class="topiclink">IMTConGatewayTranslate</a>) set for the gateway.</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">An order is created in the platform for the execution of most requests. For example, to execute a position closing request, an order is created and the execution of the order will close the position. The order data is written to the 'order' parameter of the specified methods along with the request data. Similar behavior is used for triggered SL/TP levels, Stop Out etc. However, for <a href="/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum#ta_sltp" class="topiclink">IMTRequest::TA_SLTP</a> requests, the 'order' parameter is not filled even if DEALER_FLAG_ORDER is enabled, since no order is created in the platform in this case.</span></li></ul></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">DEALER_FLAG_POSITION</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0x00000010</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Additionally, get a user position data by the </span><span class="f_ParameterDesrciption">request symbol before its execution</span><span class="f_fortable">. In case this flag is turned on, a user position data will be transferred to the const IMTPosition&nbsp;*position parameter of the following methods:</span></p><ul><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock" class="topiclink">IMTGatewaySink::OnDealerLock</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestnext" class="topiclink">IMTGatewayAPI::RequestNext</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestget" class="topiclink">IMTGatewayAPI::RequestGet</a></span></li></ul><p class="p_fortable"><span class="f_fortable">Note: Actual prices in the platform are specified in the 'position' parameter without regard to translation parameters (<a href="/en/docs/mt5/api/config_gateway/imtcongatewaytranslate" class="topiclink">IMTConGatewayTranslate</a>) set for the gateway.</span></p></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">DEALER_FLAG_EXTERNAL_ACC</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0x00000020</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Additionally get information about the account number of a client in an external trade system. In case this flag is turned on, the information about the account is filled in the <a href="/en/docs/mt5/api/reference_trading/trading_request/imtrequest" class="topiclink">IMTRequest</a> object that is passed as a parameter by the following functions:</span></p><ul><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock" class="topiclink">IMTGatewaySink::OnDealerLock</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestnext" class="topiclink">IMTGatewayAPI::RequestNext</a></span></li><li class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_trading_request/imtgatewayapi_requestget" class="topiclink">IMTGatewayAPI::RequestGet</a></span></li></ul></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">DEALER_FLAG_MARKUP_TRADES</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0x00000040</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">This flag allows automatic conversion of prices of trade operations when passing the prices from the gateway side into the MetaTrader 5 and back at the Gateway API level in accordance with the settings of <a href="/en/docs/mt5/api/config_gateway/imtcongatewaytranslate/imtcongatewaytranslate_bidmarkup" class="topiclink">IMTConGatewayTranslate::BidMarkup</a> and <a href="/en/docs/mt5/api/config_gateway/imtcongatewaytranslate/imtcongatewaytranslate_askmarkup" class="topiclink">IMTConGatewayTranslate::AskMarkup</a>. Prices of the quoting flow (including the Depth of Market) are always converted in accordance with the IMTConGatewayTranslate::BidMarkup and IMTConGatewayTranslate::AskMarkup settings.</span></p></td></tr></tbody></table>

This enumeration is used in the [IMTGatewayAPI::DealerStart](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerstart) method.

## IMTGatewayAPI::EnConnectType [#](imtgatewayapi_enum#enconnecttype)

IMTGatewayAPI::EnConnectType lists the types of platform components.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">CONNECT_TYPE_TRADE</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">CONNECT_TYPE_HISTORY</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">2</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">History server.</span></p></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">CONNECT_TYPE_ECN</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">3</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Access server.</span></p></td></tr><tr class="table"><td class="table" style="width:220px;"><p class="p_fortable"><span class="f_fortable">CONNECT_TYPE_BACKUP</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">4</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Backup server.</span></p></td></tr></tbody></table>

The enumeration is used in the following methods:

-   [IMTGatewaySink::OnServerDisconnect](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserverdisconnect)
-   [IMTGatewaySink::OnServerSynchronized](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_onserversynchronized)
-   [IMTGatewaySink::HookServerConnect](/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_hookserverconnect)

[Main Interface](/en/docs/mt5/api/imtgatewayapi)

[Common Functions](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_common)