# Trade Request Processing by the Server and Call of Hooks

> Source: https://support.metaquotes.net/en/docs/mt5/api/hook_scheme

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)Request Processing on the Server

# Trade Request Processing by the Server and Call of Hooks

This section provides a description of the full path of a trade request from order placing by a client/dealer till its final processing on the server.

![Trade Request Processing Scheme](/en/docs/mt5/api/img/request_processing_scheme.png "Trade Request Processing Scheme")

1.  A client or a dealer places an order through the client or manager terminal.
2.  The server receives the trade request and validates its digital signature.
3.  The server adds the request into the initial request queue.
4.  A separate stream performs a primary verification of requests. The following is checked at this stage:

-   1.  the overall validity of the request;
    2.  the symbol specified in the request:
        -   if symbol trading is allowed for the client group;
        -   if the request time is in the trading session time;
        -   if the request time falls on holiday;
        -   if the request time is in the server operation time;
        -   if the symbol trading time has not expired;
        -   if the request has not timed out due to the absence of symbol quotes;
        -   if the specified fill type is allowed for the symbols;
    3.  if the account, from which the request has been received, is enabled;
    4.  if trading is allowed for that account;
    5.  if the account is not in the read-only mode;
    6.  if there is a connection to the history server;
    7.  Prices for the symbol are checked, current prices are received;
    8.  Request parameters are checked:
        -   volume;
        -   normalization of prices;
        -   verification of stop levels;
        -   limit on the number of orders;
        -   limit on the total volume of orders and positions;
    9.  Check for sufficient margin.

1.  After all checks and verifications, but prior to adding the order, the [HookTradeRequestAdd](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestadd) hook is called.
2.  If a request is successfully verified, the hook (hooks) returns the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) code, and the request is a request to place an order, a new order in the ["Started"](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_enum#enorderstate) state is created.
3.  After adding an order, the [OnTradeRequestAdd](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestadd) event is called.
4.  If any errors were detected during previous stages, the request is removed from the queue, and a transaction about the request deletion with a corresponding error code is sent.
5.  Verified requests are added to the routing queue, in which they are also handled in a separate thread.

-   1.  Before processing in accordance with the routing rules, the [HookTradeRequestRoute](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestroute) hook is called:
        -   If [MT\_RET\_REQUEST\_DONE](/en/docs/mt5/api/retcodes_trade_request) is returned from the hook, the request will be confirmed without using routing rules;
        -   If [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) is returned from the hook, the request will be processed in accordance with the routing rule;
        -   If a different response code is returned, the request will be rejected with the appropriate return code.
    2.  A request is analyzed in accordance with the routing rules from top to bottom.

1.  Depending on the routing rules, the request is forwarded to a dealer/gateway or it can be automatically confirmed and added to a separate server execution queue.
2.  A separate queue of requests is available for dealers. A dealer blocks an enqueued request, which the dealer is going to process. After that this request will not be visible to other dealers. The dealer then either confirms the request or rejects it using [IMTManagerAPI::DealerAnswer](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealeranswer) and passing the appropriate [response code](/en/docs/mt5/api/retcodes_trade_request) among other things in it. The following response codes highlight confirmation:

1.  1.  MT\_RET\_REQUEST\_DONE — request fulfilled.
    2.  MT\_RET\_REQUEST\_DONE\_PARTIAL — request partially fulfilled.
    3.  MT\_RET\_REQUEST\_REQUOTE — request requoted.
    4.  MT\_RET\_REQUEST\_REQUOTE\_RETURN — request requoted and returned to the queue with new prices.

1.  If a gateway processes a request on the trading platform side, it responds to the request using [IMTGatewayAPI::DealerAnswerAsync](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealeranswerasync) with the [MT\_RET\_REQUEST\_DONE](/en/docs/mt5/api/retcodes_trade_request) code. In this case, the request is added to the execution queue (13). If the gateway processes a request at the external system, it responds the request using [IMTGatewayAPI::DealerAnswerAsync](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealeranswerasync) with the [MT\_RET\_REQUEST\_PLACED](/en/docs/mt5/api/retcodes_trade_request) code. The request (order) is set to Placed, while the platform asynchronously waits for a [trade execution](/en/docs/mt5/api/reference_trading/trading_request/imtexecution) (17) at the gateway.
2.  If confirmed, the request is added to the execution queue. A separate stream executes verified requests.
3.  After an additional verification of all incoming parameters of a request, immediately before execution, the [HookTradeRequestProcess](/en/docs/mt5/api/imttradesink/imttradesink_hooktraderequestprocess) hook is called.
    1.  If [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) is returned from the hook, the request will be executed;
    2.  If a different response code is returned, the request will be rejected with the appropriate return code.
4.  If request execution implies creation of a deal, the [OnDealPerform](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink/imtdealsink_ondealperform) event is triggered.
5.  After a successful execution of a request, the [OnTradeRequestProcess](/en/docs/mt5/api/imttradesink/imttradesink_ontraderequestprocess) event is called.
6.  After receiving a response from the gateway that the order is to be processed in the external system ([IMTGatewayAPI::DealerAnswerAsync](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealeranswerasync) with the [MT\_RET\_REQUEST\_PLACED](/en/docs/mt5/api/retcodes_trade_request) code), the platform asynchronously waits for a trade execution at the gateway.
7.  As soon as the gateway generates and sends the trade execution to the platform using [IMTGatewayAPI::DealerExecuteAsync](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_dealing/imtgatewayapi_dealerexecuteasync), the [HookTradeExecution](/en/docs/mt5/api/imttradesink/imttradesink_hooktradeexecution) hook is called. The hook is called before the execution is applied.
8.  If the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) code is returned from the hook, the trade execution is applied and the [OnTradeExecution](/en/docs/mt5/api/imttradesink/imttradesink_ontradeexecution) handler is called. Otherwise, the request will be rejected with a response code returned from the hook.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The <a href="/en/docs/mt5/api/reference_trading/trading_request/imtrequestsink/imtrequestsink_onrequestdelete" class="topiclink">IMTRequestSink::OnRequestDelete</a> handler is called for all requests. It can be called at any stage of request lifetime, starting with the moment when the request is added to the server queue (<a href="/en/docs/mt5/api/reference_trading/trading_request/imtrequestsink/imtrequestsink_onrequestadd" class="topiclink">IMTRequestSink::OnRequestAdd</a>). The request deletion moment depends on how it has been handled: whether it has been executed, rejected, canceled by timeout, etc.</span></p></td></tr></tbody></table>

## Processing Ticks and Orders [#](hook_scheme#ticks)

This section described the procedure of how new ticks are applied to client groups, as well as how pending order and position stop levels (Stop Loss, Take Profit and Stop Out) are checked and how they trigger.

1.  The server received the XXXYYY symbol tick.
2.  The current price ([IMTPosition::PriceCurrent](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_pricecurrent)) and profit ([IMTPosition::Profit](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_profit)) of positions for the XXXYYY symbol are updated.
3.  Hitting of Stop Loss levels of open positions for the XXXYYY symbol is checked.
4.  If Stop Loss has been hit and the position activation status ([IMTPosition::ActivationMode](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_activationmode)) is equal to ACTIVATION\_NONE, an order to close a position with [IMTOrder::Reason::ORDER\_REASON\_SL](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_reason) is created and the request to activate Stop Loss is added to the server queue ([IMTRequest::Action::TA\_ACTIVATE\_SL](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum#entradeactions)).
5.  The position activation status changes to ACTIVATION\_SL.
6.  Hitting of Take Profit levels of open positions for the XXXYYY symbol is checked.
7.  If Take Profit has been hit and the position activation status ([IMTPosition::ActivationMode](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_activationmode)) is equal to ACTIVATION\_NONE, an order to close a position with [IMTOrder::Reason::ORDER\_REASON\_TP](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_reason) is created and the request to activate Take Profit is added to the server queue ([IMTRequest::Action::TA\_ACTIVATE\_TP](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum#entradeactions)).
8.  The position activation status changes to ACTIVATION\_TP.
9.  Prices of pending orders for the XXXYYY symbol are updated ([IMTOrder::PriceCurrent](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_pricecurrent)).
10.  If the order price level has been hit, its activation status ([IMTOrder::ActivationMode](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_activationmode)) is equal to ACTIVATION\_NONE and the user has enough margin to execute the order, a request to activate a pending order is added to the trade server queue ([IMTRequest::Action::TA\_ACTIVATE](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum#entradeactions) or [IMTRequest::Action::TA\_ACTIVATE\_STOPLIMIT](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum#entradeactions)).
11.  The order activation status is changed to ACTIVATION\_PENDING or ACTIVATION\_STOPLIMIT.
12.  For the [trading accounts](/en/docs/mt5/api/reference_user/imtuser) , on which profit of positions was recalculated (as per point 2) or the margin of orders for the XXXYYY symbol has changed, margin is checked.
13.  If the account falls under the Stop Out condition and the account activation state ([IMTAccount::SOActivation](/en/docs/mt5/api/reference_trading/user_account/imtaccount/imtaccount_soactivation)) is equal to ACTIVATION\_NONE, the following actions are performed:

-   -   A pending order is searched, for which the largest margin amount is required (it must have non-zero margin, while symbol trading must be allowed). If such an order is found, a request to cancel such an order is added to the trade server queue ([IMTRequest::Action::TA\_STOPOUT\_ORDER](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum#entradeactions)). The order activation state ([IMTOrder::ActivationMode](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_activationmode)) changes to ACTIVATION\_STOPOUT.
    -   If the appropriate order is not found, the server searches for a position with a largest loss (while checking if symbol trading is allowed and taking into account the [FIFO rule](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_enum#entradeflags)). If such a position is found, a request to close the position is added to the trade server queue ([IMTRequest::Action::TA\_STOPOUT\_POSITION](/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_enum#entradeactions)). Position activation state ([IMTPosition::ActivationMode](/en/docs/mt5/api/reference_trading/trading_position/imtposition/imtposition_activationmode)) changes to ACTIVATION\_STOPOUT.
    -   Account activation state ([IMTAccount::SOActivation](/en/docs/mt5/api/reference_trading/user_account/imtaccount/imtaccount_soactivation)) is set to ACTIVATION\_STOP\_OUT.

Processing of pending order activation requests, position closure by Stop Loss, Take Profit and Stop Out requests is performed similarly to processing of regular trading requests sent by traders, following the [scheme described above](/en/docs/mt5/api/hook_scheme). The request goes through the same processing steps, with the call of corresponding events and hooks.

## Removing unprocessed orders on launch

At each launch, the trade server checks open orders and performs the following:

-   Removes Started orders ([IMTOrder::ORDER\_STATE\_STARTED](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_enum#enorderstate)) — orders that have not yet been passed for processing to an external system (if the work goes via the gateway), confirmed or processed. Otherwise, they would freeze in this state, since there are no further requests for their processing.
-   Resets order activation attributes ([IMTOrder::EnOrderActivation](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_enum#enorderactivation)).
-   Checks the status of orders processed inside the platform (without sending to external systems via the gateway). If the market order ([IMTOrder::OP\_BUY](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_enum#enordertype) or [IMTOrder::OP\_SELL](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_enum#enordertype)) in Started or Partially Filled status ([IMTOrder::ORDER\_STATE\_STARTED](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_enum#enorderstate) or [IMTOrder::ORDER\_STATE\_PARTIAL](/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_enum#enorderstate)) is detected, it is removed. The following entry is added to the server journal: "unfilled order XXX (account XXX) canceled".  
       
    In the absence of such a check, market orders could freeze. For example:

-   A trader creates a request by placing an order
-   A dealer partially confirms an order and its status changes to ORDER\_STATE\_PARTIAL
-   The platform is reset
-   The order would freeze in this state, since there are no further requests for its processing

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The <a href="/en/docs/mt5/api/reference_trading/trading_order/imtorder/imtorder_externalid" class="topiclink">IMTOrder::ExternalID</a> field defines whether an order is passed to an external system or processed in the platform. If it is filled, the ordered is displayed in the external system. The server does not remove such orders. Thus, the <a href="/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_orderexternalid" class="topiclink">IMTExecution::OrderExternalID</a> field in the server's trade requests should be filled, so that the server does not remove orders from your gateway.</span></p></td></tr></tbody></table>

[Hooks](/en/docs/mt5/api/serverapi_hooks)

[Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)