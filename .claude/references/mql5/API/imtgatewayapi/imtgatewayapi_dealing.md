# Processing Trade Requests

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing

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
                    -   [DealerConfirmCreate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerconfirmcreate)
                    -   [DealerExecutionCreate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerexecutioncreate)
                    -   [DealerStart](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerstart)
                    -   [DealerStop](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerstop)
                    -   [DealerGetAsync](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealergetasync)
                    -   [DealerLockAsync](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerlockasync)
                    -   [DealerAnswerAsync](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealeranswerasync)
                    -   [DealerExecuteAsync](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerexecuteasync)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Gateway API](/en/docs/mt5/api/gatewayapi)[Main Interface](/en/docs/mt5/api/imtgatewayapi)Processing Trade Requests

# Processing Trade Requests

In accordance with the ideology of the MetaTrader 5 trading platform, customer request management is carried out through a queue of trade requests. A gateway written with the help of the Gateway API acts as a dealer, who works with the queue, receiving the queue status, capturing and processing trade requests, and then reporting the results of their processing.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">All the functions described in this section are used only for gateways.</span></li><li class="p_tableatten"><span class="f_tableatten">Details of working with trade operations are described in the <a href="/en/docs/mt5/api/gatewayapi_trade_processing" class="topiclink">"Trade Operations in Gateway API"</a> section.</span></li></ul></td></tr></tbody></table>

The following dealer activity functions are available:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Functions</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerconfirmcreate" class="topiclink">DealerConfirmCreate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Create request confirmation interface object.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerexecutioncreate" class="topiclink">DealerExecutionCreate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Create trade execution method of this object.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerstart" class="topiclink">DealerStart</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gateway connection to the trading platform as a dealer.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerstop" class="topiclink">DealerStop</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">DealerStart inverse method. After its successful execution the gateway will stop fulfilling the dealer functions.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealergetasync" class="topiclink">DealerGetAsync</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Capture the most early (old) request from the requests queue.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerlockasync" class="topiclink">DealerLockAsync</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Capture a request from the requests queue by ID.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealeranswerasync" class="topiclink">DealerAnswerAsync</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Return the results of the captured request processing.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerexecuteasync" class="topiclink">DealerExecuteAsync</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The platform notification on the order trade execution in the external system.</span></p></td></tr></tbody></table>

[GatewaySymbolGet](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_gateway_symbols/imtgatewayapi_gatewaysymbolget)

[DealerConfirmCreate](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerconfirmcreate)