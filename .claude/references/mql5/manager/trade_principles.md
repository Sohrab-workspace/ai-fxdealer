# Basic Principles

> Source: https://support.metaquotes.net/en/docs/mt5/manager/trade_principles

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
            -   [Basic Principles](/en/docs/mt5/manager/trade_principles)
            -   [Market Watch](/en/docs/mt5/manager/market_watch)
            -   [Market Depth](/en/docs/mt5/manager/depth_of_market)
            -   [Economic Calendar](/en/docs/mt5/manager/economic_calendar)
            -   [Trading Notifications](/en/docs/mt5/manager/trade_alerts)
            -   [Working with Trading Positions](/en/docs/mt5/manager/positions)
            -   [Working with Trading Orders](/en/docs/mt5/manager/orders)
            -   [Viewing and Editing Trading Operations](/en/docs/mt5/manager/edit_trades)
            -   [For Advanced Users](/en/docs/mt5/manager/trading_advanced)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Trading Operations](/en/docs/mt5/manager/trading)Basic Principles

# Basic Principles

Before you proceed to study the trade functions of the platform, you should get a clear understanding of the basic terms: order, deal and position.

-   An order is an instruction given to a broker to buy or sell a financial instrument. There are two main [types of orders](/en/docs/mt5/manager/trade_principles): Market and Pending. In addition, there are special [Take Profit](/en/docs/mt5/manager/trade_principles#take_profit) and [Stop Loss](/en/docs/mt5/manager/trade_principles#stop_loss) levels.
-   A deal is a commercial exchange (buying or selling) of a financial security. Buying is executed at the demand price (Ask), and Sell is performed at the supply price (Bid). A deal can be opened as a result of a market order execution or a pending order triggering. Note that in some cases, execution of an order can result in several deals.
-   A position is a trade obligation, i.e. the number of bought or sold contracts of a financial instrument. A long position is financial security bought expecting the security price go higher. A short position is an obligation to supply a security expecting the price will fall in the future.

## Interrelation of orders, deals and positions

The platform allows you to easily track how a position was opened or how a deal was performed. Each trading operation has its unique ID called a "ticket". Each order and deal receive a ticket relating to their relevant position. Each deal receives a ticket of an order, by which it was concluded.

If a position was affected by multiple deals, for example in the case of a partial closing or increasing volumes, each of the deals feature the position's ticket. This makes it easy to track the entire history of the position as a whole.

If trading operations are sent to an exchange or a liquidity provider, they additionally feature an ID from an external system. This allows additional tracking of the interrelation of operations away from the platform.

![The history of opening a position can be tracked by tickets](/en/docs/mt5/manager/img/operation_connnection.png "The history of opening a position can be tracked by tickets")

# Types of orders

The Manager terminal allows performing trade operations on any accounts. In addition, the terminal allows you to control and manage the state of open positions. For this purposes, several types of trade orders are used. They are divided into two main types: market and pending. Besides them there are ["Stop Loss"](/en/docs/mt5/manager/trade_principles#stop_loss) and ["Take Profit"](/en/docs/mt5/manager/trade_principles#take_profit) orders.

## Market order [#](trade_principles#market_order)

A market order is an instruction to buy or sell a financial instrument. Execution of this order results in committing a deal. A symbol is bought at the Ask price and sold at the Bid price. The price at which the deal is conducted is determined by the [type of execution](/en/docs/mt5/manager/trade_principles#execution_type) that depends on the symbol type. Generally, a security is bought at the Ask price and sold at the Bid price.

## Pending order [#](trade_principles#pending_order)

A pending order is the client's instruction to a brokerage company to buy or sell a security under pre-defined conditions in the future. Types of pending orders:

-   Buy Limit — a trade request to buy at the Ask price that is equal to or less than that specified in the order. The current price level is higher than the value in the order. Usually this order is placed in anticipation of that the security price, having fallen to a certain level, will increase.
-   Buy Stop — a trade order to buy at the "Ask" price equal to or greater than the one specified in the order. The current price level is lower than the value in the order. Usually this order is placed in anticipation of that the security price, having reached a certain level, will keep on increasing.
-   Sell Limit — a trade order to sell at the "Bid" price equal to or greater than the one specified in the order. The current price level is lower than the value in the order. Usually this order is placed in anticipation of that the security price, having increased to a certain level, will fall.
-   Sell Stop — a trade order to sell at the "Bid" price equal to or less than the one specified in the order. The current price level is higher than the value in the order. Usually this order is placed in anticipation of that the security price, having reached a certain level, will keep on falling.
-   Buy Stop Limit — this type combines the two first types being a stop order for placing Buy Limit. As soon as the future Ask price reaches the stop-level indicated in the order (the Price field), a Buy Limit order will be placed at the level, specified in Stop Limit price field. A stop level is set above the current Ask price, while Stop Limit price is set below the stop level.
-   Sell Stop Limit — this type is a stop order for placing Sell Limit. As soon as the future Bid price reaches the stop-level indicated in the order (the Price field), a Sell Limit order will be placed at the level, specified in Stop Limit price field. A stop level is set below the current Bid price, while Stop Limit price is set above the stop level.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">For symbols with Exchange Stocks, Exchange Futures and Futures Forts <a href="/en/docs/mt5/manager/market_watch#calculation" class="topiclink">calculation modes</a>, all types of pending orders trigger according to the Last price (price of a last executed deal). In other words, an order triggers when the Last price touches the price specified in the order. But note that buying or selling as a result of triggering of an order is always performed by the Bid and Ask prices.</span></li><li class="p_tableatten"><span class="f_tableatten">In the Exchange execution mode, the price specified when placing limit orders is not verified. It can be specified above the current Ask price (for the Buy Limit orders) and below the current Bid price (for the Sell Limit orders). When placing an order with such a price, it triggers almost immediately and turns into a market one. However, unlike market orders where a trader agrees to perform a deal by a non-specified current market price, a pending order will be executed at a price no worse than the one specified.</span></li><li class="p_tableatten"><span class="f_tableatten">If during pending order activation the corresponding market operation cannot be executed (for example, the free margin on the account is not enough), the pending order will be canceled and moved to history with the Rejected status.</span></li></ul></td></tr></tbody></table>

![Pending order types](/en/docs/mt5/manager/img/order_types.png "Pending order types")

<table class="help" cellspacing="0" cellpadding="2" border="0" style="margin:0 auto; width:550px; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Current market conditions" title="Current market conditions" width="6" height="14" src="/en/docs/mt5/manager/img/order_type_red_bar.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_ImageCaption"></span><span class="f_ol">— current market state</span></p></td><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Forecast" title="Forecast" width="6" height="14" src="/en/docs/mt5/manager/img/order_type_gray_bar.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_ImageCaption"></span><span class="f_ol">— forecast</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Current price" title="Current price" width="12" height="12" src="/en/docs/mt5/manager/img/order_type_current.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— current price</span></p></td><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Order price" title="Order price" width="12" height="12" src="/en/docs/mt5/manager/img/order_type_order.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— order price</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="The price at which the pending order will be placed" title="The price at which the pending order will be placed" width="12" height="12" src="/en/docs/mt5/manager/img/order_type_trigger.png"></p></td><td colspan="3" style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— price a pending order is placed at</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; height:19px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Expected growth" title="Expected growth" width="15" height="16" src="/en/docs/mt5/manager/img/order_type_arrow_up.png"></p></td><td style="vertical-align:middle; height:19px; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— expected growth</span></p></td><td style="vertical-align:middle; width:26px; height:19px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Expected fall" title="Expected fall" width="14" height="16" src="/en/docs/mt5/manager/img/order_type_arrow_down.png"></p></td><td style="vertical-align:middle; height:19px; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— expected fall</span></p></td></tr></tbody></table>

## Take profit [#](trade_principles#take_profit)

The take profit order is intended for gaining a profit when a security price has reached a certain level. Execution of this order leads to a complete closure of the position. It is always connected to an open position or a pending order. The order can be placed only together with a market or a pending order. This order condition for long positions is checked using the Bid price (the order is always set above the current Bid price), and the Ask price is used for short positions (the order is always set below the current Ask price).

## Stop loss [#](trade_principles#stop_loss)

This order is used for minimizing losses if a security price has started to move in an unprofitable direction. If the price of the instrument reaches this level, the position is fully closed automatically. Such orders are always associated with an open position or a pending order. The order can be placed only together with a market or a pending order. This order condition for long positions is checked using the Bid price (the order is always set below the current Bid price), and the Ask price is used for short positions (the order is always set above the current Ask price).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If during take profit or stop loss activation the corresponding market operation cannot be executed (for example, it is rejected by the exchange), the order will not be deleted. It will trigger again at the next tick corresponding to the order activation conditions.</span></p></td></tr></tbody></table>

### Stop loss and take profit inheritance rules ([netting](/en/docs/mt5/manager/trade_principles#netting)): [#](trade_principles#sltp_inherit)

-   When increasing position volume or reverting the position, Take Profit and Stop Loss levels are placed according to its latest order (market or triggered pending order). In other words, in every new order of the same position stop levels replace the previous ones. If zero values are specified in the order, stop loss and take profit of a position will be deleted.
-   If a position is partially closed, stop loss and take profit are not changed by the new order.
-   If a position is fully closed, stop loss and take profit levels are deleted, because they are associated with an open position and cannot exist without it.
-   If a trade operation is executed for a symbol, for which there is a position, the current stop loss and take profit of the open position are automatically inserted in the order placing window. This is aimed to prevent accidental deletion of current stop orders.
-   During one click trading operation in the client terminal (from a panel on the chart or from the Market Watch) for the symbol, for which there is a position, the current values of stop loss and take profit are not changed.
-   On the OTC markets (Forex, CFD, Futures), when a position is moved to the next trading day (the swap), including through re-opening, the levels of stop loss and take profit remain unchanged.
-   On the exchange market, when a position is moved to the next trading day (the swap), as well as when moved to another account or during delivery, the levels of stop loss and take profit are reset.

### Stop loss and take profit inheritance rule ([hedging](/en/docs/mt5/manager/trade_principles#hedging)):

-   If a position is partially closed, stop loss and take profit are not changed by the new order.
-   If a position is fully closed, stop loss and take profit levels are deleted, because they are associated with an open position and cannot exist without it.
-   During one click trading operation in the client terminal (from a panel on the chart or Depth of Market), the stop loss and take profit levels are not set.

These rules apply both when trading manually or when placing orders from Expert Advisors (MQL5 programs) in the client terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">A trailing stop can be used in the client terminal to make a stop loss follow a price automatically.</span></li><li class="p_tableatten"><span class="f_tableatten">Triggering of a take profit and stop loss leads to a complete closure of a position.</span></li><li class="p_tableatten"><span class="f_tableatten">For symbols with Exchange Stocks, Exchange Futures and Futures Forts <a href="/en/docs/mt5/manager/market_watch#calculation" class="topiclink">calculation modes</a>, stop loss and take profit orders are triggered according to the rules of the exchange where trading is performed. Usually, Last price (price of the last performed transaction) is applied. In other words, a stop order triggers when the Last price touches a specified price. But note that buying or selling as a result of triggering of a stop order is always performed by Bid and Ask prices.</span></li></ul></td></tr></tbody></table>

## Order status [#](trade_principles#state)

After an order is formed and sent to the trade server, it may pass the following stages:

-   Started — an order's correctness was checked, but it has not been accepted by the server yet;
-   Placed — a dealer has accepted an order;
-   Partially filled — an order is filled partially;
-   Filled — an entire order is filled;
-   Canceled — an order is canceled by a client;
-   Rejected — an order is rejected by a dealer;
-   Expired — an order is canceled due to its expiration.

You can view the state of orders on the [History](/en/docs/mt5/manager/account_history) tab in the State field. The state of pending orders that have not triggered yet can be viewed on the [Overview](/en/docs/mt5/manager/account_overview#state) tab.

## Types of execution [#](trade_principles#execution_type)

Three [order](/en/docs/mt5/manager/trade_principles#market_order) execution modes are implemented in the trading platform:

-   Instant Execution  
    In this mode, a market order is executed at the price offered by a client. When an execution request is sent, the client terminal automatically inserts current prices in the order. If a dealer/server accepts the prices, the order will be executed. If the requested price is not accepted, the so-called Requote is sent — prices, at which this order can be executed, are returned to the client.
-   Request Execution  
    In this mode, a market order is executed at the price previously received from a dealer/server. Before submitting a market, prices of its execution are requested. Upon receiving them, a trader can confirm or reject the execution of the order.
-   Market Execution  
    In this mode, a decision on execution is taken by the dealer/server without the additional consent of the trader. The fact that a trader sends a market order in this mode means that the trader agrees to the price, at which it will be executed.
-   Exchange Execution  
    In this mode, trade operations conducted from the terminals are sent to an external trading system (exchange). Trade operations are executed at the prices of current market offers.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Execution mode for each financial instrument can be <a href="/en/docs/mt5/manager/quotes_symbols#properties" class="topiclink">changed</a> by a manager provided he or she has appropriate rights.</span></li><li class="p_tableatten"><span class="f_tableatten">For market orders, placed in the Manager terminal, there is no division into execution modes.</span></li></ul></td></tr></tbody></table>

## Fill policy [#](trade_principles#fill_policy)

Besides the general order execution rules that are set in symbol managers, a trader/manager can specify additional conditions in the [Fill Policy](/en/docs/mt5/manager/positions#fill_policy) field of the order placing window:

-   Fill or Kill  
    This fill policy means that an order can be filled only for the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The required volume can be filled by several offers available in the market at the moment.
-   Immediate or Cancel  
    In this case a trader/manager agrees to execute a deal with the volume maximally available in the market within that indicated in the order. If the request cannot be filled completely, an order with the available volume will be executed, and the remaining volume will be canceled. The possibility of using IOC orders should be enabled on the trade server.
-   Book or Cancel (BOC)  
    The BOC policy indicates that the order can only be placed in the Depth of Market (order book). If the order can be filled immediately when placed, this order is canceled. This policy guarantees that the price of the placed order will be worse than the current market. BOC is used to implement passive trading: it is guaranteed that the order cannot be executed immediately when placed and thus it does not affect current liquidity. This fill policy is only supported for limit and stop limit orders.
-   Return  
    This filling policy is used for market (Buy and Sell), [limit and stop limit orders](/en/docs/mt5/manager/trade_principles#pending_order). In case of partial filling, an order with remaining volume is not canceled but processed further. For market orders, the Return filling policy is used only in Exchange execution [mode](/en/docs/mt5/manager/trade_principles#execution_type), while for limit and stop limit orders, it is used in Market and Exchange execution modes.

Use of fill policies depending on the execution type can be shown as the following table:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:288px; height:3px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type of Execution\Fill Policy</span></p></th><th class="table" style="width:161px; height:3px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Fill or Kill (FOK)</span></p></th><th class="table" style="width:170px; height:3px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Immediate or Cancel (IOC)</span></p></th><th class="table" style="width:170px; height:3px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Book or Cancel (BOC)</span></p></th><th class="table" style="height:3px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Return</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Instant Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">—</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Request Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">—</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Market Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">+</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Exchange Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">+</span></p></td></tr></tbody></table>

## Position accounting system [#](trade_principles#position_system)

Two position accounting systems are supported in the trading platform: Netting and Hedging. The applied system depends on the [group settings](/en/docs/mt5/manager/groups):

![Positions accounting system](/en/docs/mt5/manager/img/group_position_system.png "Positions accounting system")

Different accounting systems are supported only for the OTC market. In the exchange market, a netting system is always used.

### Netting system [#](trade_principles#netting)

With this system, you can have only one common position for a symbol at the same time:

-   If there is an open position for a symbol, executing a deal in the same direction increases the volume of this position.
-   If a deal is executed in the opposite direction, the volume of the existing position can be decreased, the position can be closed (when the deal volume is equal to the position volume) or reversed (if the volume of the opposite deal is greater than the current position).

It does not matter, what has caused the opposite deal — an executed market order or a triggered pending order.

The below example shows execution of two EURUSD Buy deals 1 lot each:

![Execution of the two Buy deals resulted in one net position](/en/docs/mt5/manager/img/netting_positions.png "Execution of the two Buy deals resulted in one net position")

### Hedging system [#](trade_principles#hedging)

With this system, you can have multiple open positions of one and the same symbol, including opposite positions.

If you have an open position for a symbol, and execute a new deal (or a pending order triggers), a new position is additionally opened. Your current position does not change.

The below example shows execution of two EURUSD Buy deals 1 lot each:

![Execution of the two Buy deals resulted in two trading positions](/en/docs/mt5/manager/img/hedging_positions.png "Execution of the two Buy deals resulted in two trading positions")

### Impact of the system selected

Depending on the position accounting system, some of the platform functions may have different behavior:

-   Rules of [stop loss and take profit inheritance](/en/docs/mt5/manager/trade_principles#sltp_inherit) also change.
-   To [close a position](/en/docs/mt5/manager/positions#close) in the netting system, you should perform an opposite trading operation for the same symbol and the same volume. To close a position in the hedging system, explicitly select the Close Position command in the context menu of the position.
-   A position cannot be reversed in the hedging system. In this case, the current position is closed and a new one with the remaining volume is opened.
-   In the hedging system, a new condition for margin calculation is available — [Hedged margin](/en/docs/mt5/manager/trading_advanced/margin_forex_hedge#hedged).

[Trading Operations](/en/docs/mt5/manager/trading)

[Market Watch](/en/docs/mt5/manager/market_watch)