# Types of Orders

> Source: https://support.metaquotes.net/en/docs/mt5/iphone/trade/general_concept/order_types

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
        -   [Getting Started](/en/docs/mt5/iphone/getting_started)
        -   [Quotes](/en/docs/mt5/iphone/quotes)
        -   [Depth of Market](/en/docs/mt5/iphone/depth_of_market)
        -   [Chart](/en/docs/mt5/iphone/chart)
        -   [Trade](/en/docs/mt5/iphone/trade)
            -   [Trading Principles](/en/docs/mt5/iphone/trade/general_concept)
                -   [Types of Orders](/en/docs/mt5/iphone/trade/general_concept/order_types)
                -   [Types of Execution](/en/docs/mt5/iphone/trade/general_concept/execution_types)
                -   [State of Orders](/en/docs/mt5/iphone/trade/general_concept/order_state)
                -   [Fill Policy](/en/docs/mt5/iphone/trade/general_concept/fill_policy)
            -   [Opening and Closing Positions](/en/docs/mt5/iphone/trade/open_positions)
            -   [Close By](/en/docs/mt5/iphone/trade/closeby)
            -   [Modifying a Position](/en/docs/mt5/iphone/trade/change_positions)
            -   [Placing Pending Orders](/en/docs/mt5/iphone/trade/pending_place)
            -   [Managing Pending Orders](/en/docs/mt5/iphone/trade/pending_change)
            -   [Bulk Operations](/en/docs/mt5/iphone/trade/bulk_operations)
            -   [Trading Report](/en/docs/mt5/iphone/trade/report)
        -   [History](/en/docs/mt5/iphone/history)
        -   [Accounts](/en/docs/mt5/iphone/settings_accounts)
        -   [Mailbox](/en/docs/mt5/iphone/settings_mail)
        -   [News](/en/docs/mt5/iphone/settings_news)
        -   [Messages](/en/docs/mt5/iphone/settings_messages)
        -   [Push Notifications](/en/docs/mt5/iphone/push)
        -   [Settings](/en/docs/mt5/iphone/settings)
        -   [iPad Version](/en/docs/mt5/iphone/ipad)
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

[MetaTrader 5](/en/docs/mt5)[iPhone/iPad](/en/docs/mt5/iphone)[Trade](/en/docs/mt5/iphone/trade)[Trading Principles](/en/docs/mt5/iphone/trade/general_concept)Types of Orders

# Types of Orders

The MetaTrader 5 mobile platform allows users to prepare and issue requests for the broker to execute trading operations. In addition, the platform allows to control and manage open positions. For this purposes, several types of trade orders are used. An order is an instruction of a brokerage firm's client to conduct a trade operation. In the terminal, orders are divided into two main types: market and pending. Besides them there are ["Stop Loss"](/en/docs/mt5/iphone/trade/general_concept/order_types#stop_loss) and ["Take Profit"](/en/docs/mt5/iphone/trade/general_concept/order_types#take_profit) orders.

## Market Orders [#](order_types#market_order)

A market order is an instruction given to a brokerage company to buy or sell a financial instrument. Execution of this order results in committing a deal. The price at which the deal is conducted is determined by the [type of execution](/en/docs/mt5/iphone/trade/general_concept/execution_types) that depends on the symbol type. Generally, a security is bought at the Ask price and sold at the Bid price.

## Pending Orders [#](order_types#pending_order)

A pending order is the trader's instruction to a brokerage company to buy or sell a security in future under pre-defined conditions. Types of pending orders:

-   Buy Limit — a trade request to buy at the Ask price that is equal to or less than that specified in the order. The current price level is higher than the value in the order. Usually this order is placed in anticipation of that the security price, having fallen to a certain level, will increase.
-   Buy Stop — a trade order to buy at the "Ask" price equal to or greater than the one specified in the order. The current price level is lower than the value in the order. Usually this order is placed in anticipation of that the security price, having reached a certain level, will keep on increasing.
-   Sell Limit — a trade order to sell at the "Bid" price equal to or greater than the one specified in the order. The current price level is lower than the value in the order. Usually this order is placed in anticipation of that the security price, having increased to a certain level, will fall.
-   Sell Stop — a trade order to sell at the "Bid" price equal to or less than the one specified in the order. The current price level is higher than the value in the order. Usually this order is placed in anticipation of that the security price, having reached a certain level, will keep on falling.
-   Buy Stop Limit — this type combines the two first types being a stop order for placing Buy Limit. As soon as the future Ask price reaches the stop-level indicated in the order (the Price field), a Buy Limit order will be placed at the level, specified in Stop Limit price field. A stop level is set above the current Ask price, while Stop Limit price is set below the stop level.
-   Sell Stop Limit — this type is a stop order for placing Sell Limit. As soon as the future Bid price reaches the stop-level indicated in the order (the Price field), a Sell Limit order will be placed at the level, specified in Stop Limit price field. A stop level is set below the current Bid price, while Stop Limit price is set above the stop level.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">For symbols with Exchange Stocks, Exchange Futures and Futures Forts <a href="/en/docs/mt5/iphone/quotes#specification" class="topiclink">calculation modes</a>, all the types of pending orders trigger according to the Last price (price of a last executed deal). In other words, an order triggers when the Last price touches the price specified in the order. But note that buying or selling as a result of triggering of an order is always performed by the Bid and Ask prices.</span></li><li class="p_tableatten"><span class="f_tableatten">In the Exchange execution mode, the price specified when placing limit orders is not verified. It can be specified above the current Ask price (for the Buy Limit orders) and below the current Bid price (for the Sell Limit orders). When placing an order with such a price, it triggers almost immediately and turns into a market one. However, unlike market orders where a trader agrees to perform a deal by a non-specified current market price, a pending order will be executed at a price no worse than the one specified.</span></li><li class="p_tableatten"><span class="f_tableatten">If an appropriate market operation cannot be executed when a pending order triggers (e.g. there is not enough margin), the pending order is canceled and moved to history with the Rejected status.</span></li></ul></td></tr></tbody></table>

![Pending Order Types](/en/docs/mt5/iphone/img/order_types.png "Pending Order Types")

<table class="help" cellspacing="0" cellpadding="2" border="0" style="margin:0 auto; width:550px; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Current market conditions" title="Current market conditions" width="6" height="14" src="/en/docs/mt5/iphone/img/order_type_red_bar.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— Current market state</span></p></td><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Forecast" title="Forecast" width="6" height="14" src="/en/docs/mt5/iphone/img/order_type_gray_bar.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— Forecast</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Current price" title="Current price" width="12" height="12" src="/en/docs/mt5/iphone/img/order_type_current.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— Current price</span></p></td><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Order price" title="Order price" width="12" height="12" src="/en/docs/mt5/iphone/img/order_type_order.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— order price</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="The price at which the pending order will be placed" title="The price at which the pending order will be placed" width="12" height="12" src="/en/docs/mt5/iphone/img/order_type_trigger.png"></p></td><td colspan="3" style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— the price, reaching which the pending order will be placed</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; height:19px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Expected growth" title="Expected growth" width="15" height="16" src="/en/docs/mt5/iphone/img/order_type_arrow_up.png"></p></td><td style="vertical-align:middle; height:19px; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— Expected growth</span></p></td><td style="vertical-align:middle; width:26px; height:19px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Expected fall" title="Expected fall" width="14" height="16" src="/en/docs/mt5/iphone/img/order_type_arrow_down.png"></p></td><td style="vertical-align:middle; height:19px; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— expected fall</span></p></td></tr></tbody></table>

## Take Profit [#](order_types#take_profit)

The Take Profit order is intended for gaining the profit when the security price has reached a certain level. Execution of this order leads to a complete closure of the position. It is always connected to an open position or a pending order. The order can be placed only together with a market or a pending order. This order condition for long positions is checked using the Bid price (the order is always set above the current Bid price), and the Ask price is used for short positions (the order is always set below the current Ask price).

## Stop Loss [#](order_types#stop_loss)

This order is used for minimizing of losses if the security price has started to move in an unprofitable direction. If the price of the instrument reaches this level, the position is fully closed automatically. Such orders are always associated with an open position or a pending order. The order can be placed only together with a market or a pending order. This order condition for long positions is checked using the Bid price (the order is always set below the current Bid price), and the Ask price is used for short positions (the order is always set above the current Ask price).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Take Profit and Stop Loss levels are placed for a position according to its latest order (market or triggered pending order). In other words, in every new order of the same position stop levels replace previous ones.</span></li><li class="p_tableatten"><span class="f_tableatten">Triggering of Take Profit and Stop Loss leads to a complete closure of a position.</span></li><li class="p_tableatten"><span class="f_tableatten">For symbols with Exchange Stocks, Exchange Futures and Futures Forts <a href="/en/docs/mt5/iphone/quotes#specification" class="topiclink">calculation modes</a>, Stop Loss and Take Profit orders trigger according to the Last price (price of a last executed deal). In other words, a stop-order triggers when the Last price touches the specified price. But note that buying or selling as a result of triggering of a stop-order is always performed by the Bid and Ask prices.</span></li><li class="p_tableatten"><span class="f_tableatten">If during Take Profit or Stop Loss activation the corresponding market operation cannot be executed (for example, it is rejected by the exchange), the order will not be deleted. It will trigger again at the next tick corresponding to the order activation conditions.</span></li></ul></td></tr></tbody></table>

## Stop Loss and Take Profit inheritance rules ([netting](/en/docs/mt5/iphone/trade/general_concept#netting)): [#](order_types#sltp_inherit)

-   When increasing position volume or reverting the position, Take Profit and Stop Loss levels are placed according to its latest order (market or triggered pending order). In other words, in every new order of the same position stop levels replace previous ones. If zero values are specified in the order, Stop Loss and Take Profit of a position will be deleted.
-   If a position is partially closed, Stop Loss and Take Profit are not changed by the new order.
-   If a position is fully closed, the Stop Loss and Take Profit levels are deleted, because they are associated with an open position and cannot exist without it.
-   If a trade operation is executed for a symbol, for which there is a position, the current Stop Loss and Take Profit of the open position are automatically inserted in the order placing window. This is aimed to prevent accidental deletion of current stop orders.
-   During one click trading operation executed from the [Market Depth](/en/docs/mt5/iphone/depth_of_market) for the symbol, for which there is a position, the current values of Stop Loss and Take Profit are not changed.
-   On the OTC markets (Forex, Futures), when a position is moved to the next trading day (the swap), including through re-opening, the levels of Stop Loss and Take Profit are remain unchanged.
-   On the exchange market, when a position is moved to the next trading day (the swap), as well as when moved to another account or during delivery, the levels of Stop Loss and Take Profit are reset.

## Stop Loss and Take Profit inheritance rules ([hedging](/en/docs/mt5/iphone/trade/general_concept#hedging)):

-   If a position is partially closed, Stop Loss and Take Profit are not changed by the new order.
-   If a position is fully closed, the Stop Loss and Take Profit levels are deleted, because they are associated with an open position and cannot exist without it.
-   During one click trading operation executed from the [Depth of Market](/en/docs/mt5/iphone/depth_of_market), the Stop Loss and Take Profit levels are not set.

[Trading Principles](/en/docs/mt5/iphone/trade/general_concept)

[Types of Execution](/en/docs/mt5/iphone/trade/general_concept/execution_types)