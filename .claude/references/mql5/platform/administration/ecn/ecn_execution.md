# Order Filling

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ecn/ecn_execution

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
                -   [Forming Market Depth](/en/docs/mt5/platform/administration/ecn/ecn_dom_aggregation)
                -   [Market Depth Journal](/en/docs/mt5/platform/administration/ecn/ecn_dom_journal)
                -   [Order Matching](/en/docs/mt5/platform/administration/ecn/ecn_matching)
                -   [Order Execution](/en/docs/mt5/platform/administration/ecn/ecn_execution)
                -   [Price Translations](/en/docs/mt5/platform/administration/ecn/ecn_translation)
                -   [Matching History](/en/docs/mt5/platform/administration/ecn/ecn_matching_history)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[ECN](/en/docs/mt5/platform/administration/ecn)Order Execution

# Order Filling

As a result of [matching](/en/docs/mt5/platform/administration/ecn/ecn_matching), an opposite order of another client from within the MetaTrader 5 cluster or an order from an external system (liquidity provider) can be selected for a client order execution.

## Order execution within the trade cluster [#](ecn_execution#cluster)

When two orders are matched within the trade cluster, two opposite deals are created to fill these orders. In this case:

-   The deal volume is equal to the lowest volume of the two orders (taking into account the remaining unfilled order volume). For example, when matching orders Buy 2.00/1.00 and Sell 2.00/0.00, the volume of the deals will be equal to 1 lot.
-   The price of the deals depends on the type of the matched orders:

-   If both are limit orders, the prices of both deals will be equal to the price of the order which was placed in the ECN earlier.
-   If only one of the orders is of the limit type, its price will be used for both deals.

## Order execution at external liquidity providers [#](ecn_execution#providers)

Once an order is matched with the price level of an external liquidity provider, it is forwarded to that provider for execution. For this, the ECN module creates a trade request to place a new order in accordance with [symbol settings in the external system](https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_gateway_symbols), which were received from the gateway, as well as [filling parameters](/en/docs/mt5/platform/administration/ecn/ecn_execution#filling) specified in the triggered matching rules.

Trading requests generated by ECN for liquidity providers are added to the request queue and are processed by the gateways similarly to regular requests from trade servers in the cluster. There are some specific features connected with the [MetaTrader 5 Gateway API](https://support.metaquotes.net/en/docs/mt5/api/gatewayapi), which should be taken into account when developing gateways for the platform:

1.  Instead of the [login of the client](https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_request/imtrequest/imtrequest_login) who created the request, the ECN specifies its own dealer identifier, which is equal to the UINT64\_MAX constant.
2.  The ECN [does not pass](https://support.metaquotes.net/en/docs/mt5/api/imtgatewaysink/imtgatewaysink_ondealerlock) information related to the [client](https://support.metaquotes.net/en/docs/mt5/api/reference_user/imtuser), [trading account](https://support.metaquotes.net/en/docs/mt5/api/reference_trading/user_account/imtaccount), [order](https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_order/imtorder) and [position](https://support.metaquotes.net/en/docs/mt5/api/reference_trading/trading_position/imtposition) when sending a trade request.
3.  The gateway must not use the source [ECN symbol configuration in the platform](/en/docs/mt5/platform/administration/admin_symbols) to check a request or make any decisions, since the ECN generates requests which are not linked to the platform and it takes into account [the symbol configuration in the external system](https://support.metaquotes.net/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_gateway_symbols).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The ECN does not store information about MetaTrader 5-side client positions. Any operation which the ECN forwards to an external liquidity provider is a regular Buy or Sell order. It does not matter which action the client performs: enters or exits the market. Therefore, we recommended using only netting accounts to connect gateways to external systems. In this case, all individual operations on the same symbol forwarded to an external system will be treated as one cumulative position. If you use a hedging account, new positions will be created for each order, while old positions will not be closed.</span></p></td></tr></tbody></table>

### Execution settings [#](ecn_execution#filling)

Set up execution parameters to be applied with liquidity providers using [matching rules](/en/docs/mt5/platform/administration/ecn/ecn_matching#settings):

![Additional order filling rules](/en/docs/mt5/platform/img/ecn_matching_filling.png "Additional order filling rules")

Matching method

The ECN supports two methods for selecting the second side of a deal in matching: time-based and Round-Robin. In the first case, the side is selected according to the age of orders: preference is given to the orders which were placed in the Market Depth earlier. Within the Roound-Robin algorithm, the second part for matched orders is determined evenly among all available liquidity providers. This algorithm ignores the opposite order creation time. The system matches bids and asks in a circular order, among all available providers, without time priority.

For more details on matching please visit the [appropriate section](/en/docs/mt5/platform/administration/ecn/ecn_matching#second_side).

Filling method

In the "Filling method" field, you should specify the type of requests to be forwarded to the external liquidity provider:

-   Limit orders — operations will be forwarded as limit orders with an expiration as per the "Filling maximum time" setting. The price will be equal to the one specified in the client order or the current market price (depends on the [execution mode](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution) selected for the ECN symbol). This mode helps in avoiding large slippage.
-   Market orders — operations will be forwarded as orders with the Market Execution mode.
-   Source order type — the type of orders forwarded to an external system will be selected in accordance with the initial order type: market orders will be forwarded as market operations, and limit orders will be sent as limit orders.

Filling attempts

Here you specify the maximum number of attempts to fill an order in accordance with this rule.

Matching of trading orders can fail. For example, an external system may offer for the operation the price that exceeds [maximum deviation](/en/docs/mt5/platform/administration/ecn/ecn_execution#deviation). In this case, the source order is returned to the Market Depth and its filling attempts counter is increased.

If the limit of attempts is exceeded, ECN will switch to processing the next rule, which is suitable for the given order.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_Normal"><span class="f_tableatten">0 means no limitations.</span></li><li class="p_Normal"><span class="f_tableatten">If only one matching rule is set, the number of filling attempts is actually unlimited. Upon the limit excess, the ECN will always proceed to the same matching rule processing.</span></li></ul></td></tr></tbody></table>

Filling maximum time

This is the maximum time, within which the external system (provider) is allowed to fill the matched trade request. If the order remains unfilled in the external system after the specified time, a command is sent to the external system to delete the order. After order cancellation in the external system, the remaining volume is returned to the Marked Depth for further matching. The [filling attempts](/en/docs/mt5/platform/administration/ecn/ecn_execution#attempts) counter of the source ECN order (the client request for which matching is performed) is increased by one in this case.

Deviation

This parameter is used only when operations are sent as Instant Execution and Request Execution orders.

In case of an instant execution, an acceptable deviation is specified in the request sent to the external system.

When a requote from an external system is received, ECN checks if the new price is within the specified deviation. If the deviation is not exceeded, the ECN sends to the provider a new request at the requoted prices. If the provider accepts the prices, the request is executed. In case of a repeated requote, the deviation will be checked according to the first request (i.e. the price of the original order).

If the deviation is exceeded, the execution is terminated. In this case, the order is returned to the Market Depth and an error is written to the log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2018.12.05&nbsp;15:40:57.714&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#417689&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;confirm&nbsp;prices&nbsp;1.50740&nbsp;/&nbsp;1.50766&nbsp;deviation&nbsp;4&nbsp;is&nbsp;greater&nbsp;than&nbsp;maximum&nbsp;1</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.50744]</span></p></td></tr></tbody></table>

The number of [filling attempts](/en/docs/mt5/platform/administration/ecn/ecn_execution#attempts) is increased by one. Then, the ECN will try to resend the order.

During request execution, the ECN first requests prices from the external system. After receiving the price, the ECN checks if the price is within the allowed deviation. If the deviation is not exceeded, the ECN sends to the provider an order at the requoted prices.

If the deviation is exceeded, the execution is terminated. In this case, the order is returned to the Market Depth and an error is written to the log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2018.12.05&nbsp;15:49:08.370&nbsp;&nbsp;ECN&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#417690&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;confirm&nbsp;prices&nbsp;1.50789&nbsp;/&nbsp;1.50817&nbsp;deviation&nbsp;2&nbsp;is&nbsp;greater&nbsp;than&nbsp;maximum&nbsp;1</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[prices&nbsp;for&nbsp;EURCAD.ECN&nbsp;4.00]</span></p></td></tr></tbody></table>

The number of [filling attempts](/en/docs/mt5/platform/administration/ecn/ecn_execution#attempts) is increased by one. Then, the ECN will try to resend the order.

Maximum slippages

Specify here the maximum deviation of the execution price provided by the external system from the requested price.

-   Profitable — the number of points by which the price may deviate from the requested one, in the profitable direction for the client.
-   Losing — the number of points by which the price may deviate from the requested one, in the unprofitable direction for the client.

After the actual deal execution in the external system, the ECN compares its price with the initially requested one ([taking into account translation settings](/en/docs/mt5/platform/administration/ecn/ecn_translation#general)). If the price is within the allowed deviation, the deal will be executed on the platform side at the requested price. If deviation is exceeded, the ECN executes the deal at the price of actual execution on the external provider side.

Suppose, the values of 5 are set both for the profitable and losing slippage. The ECN passes to the external system the Buy Limit order at the price of 1.14053, and the system executes a deal at the price of 1.1405, i.e. at a 2-point better price. Such slippage is acceptable. On the platform side, the order will be executed at the initial price of 1.14053.

If the deal price exceeded the deviation, the ECN would execute the order in the platform at that specific price (1.14051).

### Execution rules for symbols having different price accuracy on the platform and external system side [#](ecn_execution#digits)

If the accuracy of security prices on the external system side differs from that in the trading platform, this difference will be taken into account when creating trading requests to be sent to gateways and when processing deals from external systems.

Lower accuracy in the platform

If the accuracy on the platform side is lower, decimal places are added to the prices sent to the external system. Consider the following example. The price accuracy on the platform side is 4 decimal places, while the external system provides prices with 5 decimal places. When sending an order with the price of 1.1329, the price will be converted to 1.13290.

The following rules apply for deal price rounding:

-   Buy deal prices are rounded up to the symbol accuracy on the platform side.
-   Sell deal prices are rounded down to the symbol accuracy on the platform side.

Thus, the broker can only have a positive balance discrepancy with the external system, in contrast to rounding performed by the common rules.

Higher accuracy in the platform

If the accuracy in the platform is higher, during order sending to an external system the prices will be rounded according to the following rules:

-   Buy orders are rounded down to the symbol accuracy on the platform side.
-   Sell orders are rounded up to the symbol accuracy on the platform side.

Thus clients' limit orders will always be filled on the provider's side and in MetaTrader 5 at a price which is not worse than that specified in the order. This is not possible when rounding according to common rules.

Consider the following example. The price accuracy on the platform side is 5 decimal places, while the external system provides prices with 4 decimal places. When executing a client Sell order at the price of 1.12919, an order with the price of 1.1291 (rounded down) will be placed in the external system. A similar Buy request would be placed as an order with the price of 1.1292 (rounded up).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Check of the <a href="/en/docs/mt5/platform/administration/ecn/ecn_execution#deviation" class="topiclink">maximum deviation</a> of the execution price in the "Instant" and "Request" modes as well as of the price <a href="/en/docs/mt5/platform/administration/ecn/ecn_execution#slippage" class="topiclink">slippage</a> is performed based on the symbol accuracy set in the MetaTrader 5 trading platform (whenever applicable, the prices are rounded according to the above rules).</span></p><p class="p_tableatten"><span class="f_tableatten">The acceptable price deviation in the request sent to the liquidity provider is specified with the provider's accuracy (taking into account the rounding of the request price and the allowed prices according to the above rules).</span></p></td></tr></tbody></table>

Examples: Lower accuracy in the platform

The accuracy of EURCAD.ECN in the MetaTrader 5 trading platform is equal to 4 decimal places. The liquidity provider has a 5-digit accuracy. The symbol execution mode is Instant.

Maximum deviation is 2 points, maximum profitable/losing slippage = 1/1.

![Example of execution settings](/en/docs/mt5/platform/img/ecn_matching_digits_example1.png "Example of execution settings")

1\. The client places an order: #418239 buy limit 0.10 EURCAD.ECN at 1.4977, ECN matches it with 'MetaTrader 5 Gateway ECN':

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;11:35:27.553&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;request&nbsp;received&nbsp;(#418239&nbsp;buy&nbsp;limit&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4977)</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:27.553&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#418239&nbsp;buy&nbsp;limit&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4977&nbsp;added</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:27.556&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;request&nbsp;answered&nbsp;-&nbsp;Placed&nbsp;(#418239&nbsp;buy&nbsp;limit&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4977)</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:27.561&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;request&nbsp;new&nbsp;order&nbsp;#418239</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:27.561&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;added&nbsp;order&nbsp;#418239,&nbsp;buy&nbsp;limit&nbsp;0.10&nbsp;&nbsp;at&nbsp;1.4977&nbsp;[based&nbsp;on&nbsp;order&nbsp;'']</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:27.561&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;matched&nbsp;0.10&nbsp;at&nbsp;1.49764,&nbsp;#418239&nbsp;buy&nbsp;limit&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4977&nbsp;vs&nbsp;sell&nbsp;limit&nbsp;10.00&nbsp;at&nbsp;1.49764&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN',&nbsp;by&nbsp;rule&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'</span></p></td></tr></tbody></table>

The Instant request with the price of 1.49770 is formed for the gateway, which then returns a re-quote with the price of 1.49754:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;11:35:27.588&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418239&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;added&nbsp;(instant&nbsp;buy&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49770)</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:27.588&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418239&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;taken&nbsp;(instant&nbsp;buy&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49770)</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:41.393&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418239&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;confirmed:&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">Requote&nbsp;(1.49736/1.49754)</span><span class="f_CodeExample">&nbsp;(instant&nbsp;buy&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49770)</span></p></td></tr></tbody></table>

ECN rounds the potential buy deal price of 1.49754 up to 4-digit accuracy — 1.4976. The deviation from initial price (1 point) is within the allowed deviation of 2 points and thus a new Instant request for the gateway is formed using new prices:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;11:35:41.393&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418239&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;returned&nbsp;for&nbsp;confirm,&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">price&nbsp;corrected&nbsp;from&nbsp;1.4977&nbsp;to&nbsp;1.4976</span><span class="f_CodeExample">,&nbsp;client&nbsp;deviation:&nbsp;2&nbsp;(instant&nbsp;buy&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49770)(1.49736&nbsp;/&nbsp;1.49754)</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:41.395&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418239&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;added&nbsp;(instant&nbsp;buy&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">1.49754</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:41.396&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418239&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;taken&nbsp;(instant&nbsp;buy&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">1.49754</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:43.191&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418239&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;confirmed:&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">Done&nbsp;at&nbsp;1.49754</span><span class="f_CodeExample">&nbsp;(instant&nbsp;buy&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49754)</span></p></td></tr></tbody></table>

The gateway confirms the buy request at a new price of 1.49754. The ECN rounds up the deal price in MetaTrader 5 to 4 decimal places: 1.4976. The resulting profitable slippage from the order price of 1.4977 (1 point) is within the allowed value of 1 point, so the order is filled at the initial price of 1.4977.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;11:35:43.191&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">order&nbsp;filled&nbsp;0.10&nbsp;at&nbsp;1.4977</span><span class="f_CodeExample">&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN',&nbsp;#418239&nbsp;buy&nbsp;limit&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4977</span><br><span class="f_CodeExample">2019.02.12&nbsp;11:35:43.193&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;filled&nbsp;order&nbsp;#418239,&nbsp;buy&nbsp;0.10&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4977&nbsp;[based&nbsp;on&nbsp;deal&nbsp;'']</span></p></td></tr></tbody></table>

2\. The client places an order: #418242 instant sell 1.00 EURCAD.ECN at 1.4967, ECN matches it with 'MetaTrader 5 Gateway ECN':

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.961&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;request&nbsp;received&nbsp;(#418242&nbsp;instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4967)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.961&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#418242&nbsp;sell&nbsp;limit&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4967&nbsp;added</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.964&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;request&nbsp;answered&nbsp;-&nbsp;Placed&nbsp;(#418242&nbsp;instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4967)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.964&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;request&nbsp;new&nbsp;order&nbsp;#418242</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.965&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;added&nbsp;order&nbsp;#418242,&nbsp;sell&nbsp;1.00&nbsp;&nbsp;at&nbsp;1.4967&nbsp;[based&nbsp;on&nbsp;order&nbsp;'']</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.965&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;matched&nbsp;1.00&nbsp;at&nbsp;1.49679,&nbsp;#418242&nbsp;sell&nbsp;limit&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4967&nbsp;vs&nbsp;buy&nbsp;limit&nbsp;10.00&nbsp;at&nbsp;1.49679&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN',&nbsp;by&nbsp;rule&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'</span></p></td></tr></tbody></table>

The Instant request with the price of 1.49670 is formed for the gateway, which then returns a re-quote with the price of 1.49679:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.965&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418242&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;added&nbsp;(instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49670)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.966&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418242&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;taken&nbsp;(instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49670)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.968&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418242&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;confirmed:&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">Requote&nbsp;(1.49679/1.49707)</span><span class="f_CodeExample">&nbsp;(instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49670)</span></p></td></tr></tbody></table>

ECN rounds the potential buy deal price of 1.49679 down, to 4-digit accuracy — 1.4967. There is no deviation from the initial order price of 1.4967, so Instant request with the new prices is formed for the gateway. This request is again requoted with the price of 1.49701:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.968&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418242&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;returned&nbsp;for&nbsp;confirm,&nbsp;price&nbsp;corrected&nbsp;from&nbsp;1.4967&nbsp;to&nbsp;1.4967,&nbsp;client&nbsp;deviation:&nbsp;2&nbsp;(instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49670)(1.49679&nbsp;/&nbsp;1.49707)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.969&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418242&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;added&nbsp;(instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49679)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:31.969&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418242&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;taken&nbsp;(instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49679)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:42.768&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418242&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;confirmed:&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">Requote&nbsp;(1.49701/1.49703)</span><span class="f_CodeExample">&nbsp;(instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49679)</span></p></td></tr></tbody></table>

ECN rounds the potential buy deal price of 1.49701 down, to 4-digit accuracy — 1.4970. The deviation from the original order price of 1.4967 is 3 points, which is greater than the allowed value of 2 points. The order is returned to the Market Depth and is then totally canceled, since its fill policy us Fill or Kill:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;12:04:48.350&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418242&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;confirm&nbsp;prices&nbsp;1.49701&nbsp;/&nbsp;1.49703&nbsp;deviation&nbsp;3&nbsp;is&nbsp;greater&nbsp;than&nbsp;maximum&nbsp;2&nbsp;[instant&nbsp;sell&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49679]</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:48.352&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;failed&nbsp;to&nbsp;fill&nbsp;1.00&nbsp;at&nbsp;1.49679&nbsp;on&nbsp;MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN&nbsp;(5),&nbsp;#418242&nbsp;sell&nbsp;limit&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4967&nbsp;(attempts&nbsp;1)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:48.353&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#418242&nbsp;sell&nbsp;limit&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4967&nbsp;returned&nbsp;to&nbsp;book,&nbsp;remaind&nbsp;canceled</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:04:48.354&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#418242&nbsp;sell&nbsp;limit&nbsp;1.00&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.4967&nbsp;canceled</span></p></td></tr></tbody></table>

Examples: Higher accuracy in the platform

The accuracy of EURCAD.ECN in the MetaTrader 5 trading platform is equal to 6 decimal places. The liquidity provider has a 5-digit accuracy. The symbol execution mode is Instant.

Maximum deviation is 9 points, maximum profitable/losing slippage = 5/5.

![Example of execution settings](/en/docs/mt5/platform/img/ecn_matching_digits_example2.png "Example of execution settings")

1\. The client places an order: #418249 buy limit 0.50 EURCAD.ECN at 1.497566, ECN matches it with 'MetaTrader 5 Gateway ECN':

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;12:42:29.148&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;request&nbsp;received&nbsp;(#418249&nbsp;buy&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">1.497566</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:42:29.148&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#418249&nbsp;buy&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.497566&nbsp;added</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:42:29.150&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;request&nbsp;answered&nbsp;-&nbsp;Placed&nbsp;(#418249&nbsp;buy&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.497566)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:42:29.151&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;request&nbsp;new&nbsp;order&nbsp;#418249</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:42:29.151&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;added&nbsp;order&nbsp;#418249,&nbsp;buy&nbsp;limit&nbsp;0.50&nbsp;&nbsp;at&nbsp;1.497566&nbsp;[based&nbsp;on&nbsp;order&nbsp;'']</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:42:51.141&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;matched&nbsp;0.50&nbsp;at&nbsp;1.49756,&nbsp;#418249&nbsp;buy&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.497566&nbsp;vs&nbsp;sell&nbsp;limit&nbsp;10.00&nbsp;at&nbsp;1.49756&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN',&nbsp;by&nbsp;rule&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'</span></p></td></tr></tbody></table>

An Instant request is formed for the gateway with the rounded down price of 1.49756. The gateway confirms it at this price:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;12:42:51.142&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418249&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;added&nbsp;(instant&nbsp;buy&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49756)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:42:51.145&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418249&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;taken&nbsp;(instant&nbsp;buy&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49756)</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:43:12.878&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418249&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;confirmed:&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">Done&nbsp;at&nbsp;1.49756</span><span class="f_CodeExample">&nbsp;(instant&nbsp;buy&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49756)</span></p></td></tr></tbody></table>

The price converted to 6 decimal places 1.497560 provides a positive slippage of 6 points from the initial price of 1.497566. It is beyond the maximum profitable slippage of 5 points and the order is executed at the price of 1.497560:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;12:43:12.878&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">order&nbsp;filled&nbsp;0.50&nbsp;at&nbsp;1.497560</span><span class="f_CodeExample">&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN',&nbsp;#418249&nbsp;buy&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.497566</span><br><span class="f_CodeExample">2019.02.12&nbsp;12:43:12.879&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;filled&nbsp;order&nbsp;#418249,&nbsp;buy&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.497560&nbsp;[based&nbsp;on&nbsp;deal&nbsp;'']</span></p></td></tr></tbody></table>

2\. The client placed an order: #418259 instant sell 0.50 EURCAD.ECN at 1.496100, ECN matched it with 'MetaTrader 5 Gateway ECN':

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;13:23:46.316&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;request&nbsp;received&nbsp;(#418259&nbsp;instant&nbsp;sell&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">1.496100</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:46.316&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#418259&nbsp;sell&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.496100&nbsp;added</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:46.326&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;request&nbsp;answered&nbsp;-&nbsp;Placed&nbsp;(#418259&nbsp;instant&nbsp;sell&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.496100)</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:46.333&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;request&nbsp;new&nbsp;order&nbsp;#418259</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:46.334&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;execution&nbsp;sent&nbsp;-&nbsp;added&nbsp;order&nbsp;#418259,&nbsp;sell&nbsp;0.50&nbsp;&nbsp;at&nbsp;1.496100&nbsp;[based&nbsp;on&nbsp;order&nbsp;'']</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:46.338&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;matched&nbsp;0.50&nbsp;at&nbsp;1.49610,&nbsp;#418259&nbsp;sell&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.496100&nbsp;vs&nbsp;buy&nbsp;limit&nbsp;30.00&nbsp;at&nbsp;1.49610&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN',&nbsp;by&nbsp;rule&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'</span></p></td></tr></tbody></table>

An Instant request is formed for the gateway with the rounded up price of 1.496106. The gateway sends a re-quote of 1.49611:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;13:23:51.373&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418259&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;added&nbsp;(instant&nbsp;sell&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">1.49610</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:51.373&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418259&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;taken&nbsp;(instant&nbsp;sell&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49610)</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:51.378&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418259&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;request&nbsp;confirmed:&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">Requote&nbsp;(1.49611/1.49638)</span><span class="f_CodeExample">&nbsp;(instant&nbsp;sell&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49610)</span></p></td></tr></tbody></table>

The potential deal price is converted to 6 decimal places — 1.496110. Deviation from the original order price 1.496100 is 10 points, which is greater than the allowed value of 9 points. The order is returned to the Market Depth and is then totally canceled, since its fill policy us Fill or Kill:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2019.02.12&nbsp;13:23:51.380&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;filling&nbsp;order&nbsp;#418259&nbsp;on&nbsp;'MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN'&nbsp;-&nbsp;confirm&nbsp;prices&nbsp;1.49611&nbsp;/&nbsp;1.49638&nbsp;</span><span class="f_CodeExample" style="background-color: #b8cde5;">deviation&nbsp;10&nbsp;is&nbsp;greater&nbsp;than&nbsp;maximum&nbsp;9</span><span class="f_CodeExample">&nbsp;[instant&nbsp;sell&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.49610]</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:51.384&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;failed&nbsp;to&nbsp;fill&nbsp;0.50&nbsp;at&nbsp;1.49610&nbsp;on&nbsp;MetaTrader&nbsp;5&nbsp;Gateway&nbsp;ECN&nbsp;(5),&nbsp;#418259&nbsp;sell&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.496100&nbsp;(attempts&nbsp;1)</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:51.394&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#418259&nbsp;sell&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.496100&nbsp;returned&nbsp;to&nbsp;book,&nbsp;remaind&nbsp;canceled</span><br><span class="f_CodeExample">2019.02.12&nbsp;13:23:51.397&nbsp;&nbsp;&nbsp;&nbsp;ECN&nbsp;&nbsp;&nbsp;&nbsp;'2002':&nbsp;order&nbsp;#418259&nbsp;sell&nbsp;limit&nbsp;0.50&nbsp;EURCAD.ECN&nbsp;at&nbsp;1.496100&nbsp;canceled</span></p></td></tr></tbody></table>

[Order Matching](/en/docs/mt5/platform/administration/ecn/ecn_matching)

[Price Translations](/en/docs/mt5/platform/administration/ecn/ecn_translation)