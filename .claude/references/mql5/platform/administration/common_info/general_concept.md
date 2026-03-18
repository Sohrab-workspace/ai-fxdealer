# Trading System

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/common_info/general_concept

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
                -   [Trading System](/en/docs/mt5/platform/administration/common_info/general_concept)
                -   [Price Data](/en/docs/mt5/platform/administration/common_info/price_data)
                -   [Working with Instructions](/en/docs/mt5/platform/administration/common_info/common_instructions)
                -   [Specifying Symbols and Groups](/en/docs/mt5/platform/administration/common_info/common_mask)
                -   [Data Export](/en/docs/mt5/platform/administration/common_info/export)
                -   [Import/Export Settings](/en/docs/mt5/platform/administration/common_info/import_export_config)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[General Information](/en/docs/mt5/platform/administration/common_info)Trading System

# Trading System

Before you proceed with administration of the platform, please get acquainted with the basics of its trading system.

## Trade Operation Types

The platform has three types of trade operations: [order](/en/docs/mt5/platform/administration/admin_orders), [deal](/en/docs/mt5/platform/administration/admin_deals) and [position](/en/docs/mt5/platform/administration/admin_positions). There is a separate section to manage each of them in the administrator terminal.

-   An order is an instruction given to a broker to buy or sell a financial instrument. There are two main [types of orders](/en/docs/mt5/platform/administration/common_info/general_concept#order_type): Market and Pending. In addition, there are special [Take Profit](/en/docs/mt5/platform/administration/common_info/general_concept#take_profit) and [Stop Loss](/en/docs/mt5/platform/administration/common_info/general_concept#stop_loss) levels.
-   A deal is the commercial exchange (buying or selling) of a financial security. Buying is executed at the demand price (Ask), and Sell is performed at the supply price (Bid). A deal can be opened as a result of market order execution or pending order triggering. Note that in some cases, execution of an order can result in several deals.
-   A position is a trade obligation, i.e. the number of bought or sold contracts of a financial instrument. A long position is financial security bought expecting the security price go higher. A short position is an obligation to supply a security expecting the price will fall in future.

## Interrelation of orders, deals and positions

The platform allows you to easily track how a position was opened or how a deal was performed. Each trading operation has its unique ID called a "ticket". Each order and deal receive a ticket relating to their relevant position. Each deal receives a ticket of an order, by which it was concluded.

If a position was affected by multiple deals, for example in the case of a partial closing or increasing volumes, each of the deals feature the position's ticket. This makes it easy to track the entire history of the position as a whole.

If trading operations are sent to an exchange or a liquidity provider, they additionally feature an ID from an external system. This allows additional tracking of the interrelation of operations away from the platform.

![The history of opening a position can be tracked by tickets](/en/docs/mt5/platform/img/operation_connnection.png "The history of opening a position can be tracked by tickets")

## A General Scheme of Trading Operations

-   From the client terminal, an order is sent to a broker to execute a deal with the specified parameters;
-   The correctness of an order is checked on the server (correctness of prices, availability of funds on the account, etc.);
-   Orders that have passed the check wait to be processed on the trade server. Then the order can be:

-   executed (in one of automatic [execution](/en/docs/mt5/platform/administration/common_info/general_concept#execution_type) modes or by a dealer)
-   canceled upon expiry
-   rejected (e.g. when money is not enough or there is no suiting offer in the market; or rejected by the dealer)
-   canceled by a trader;
-   A deal is the result of the execution of a market order or triggering of a pending order;
-   If there are no positions for a symbol, conclusion of a deal results in opening of a position. If there is a position for the symbol, the deal can increase or reduce the position volume, close the position or reverse it.

![Scheme of trade operations: from order creation to execution by broker](/en/docs/mt5/platform/img/trading_scheme.png "Scheme of trade operations: from order creation to execution by broker")

## Position Accounting System [#](general_concept#position_type)

Two position accounting systems are supported in the trading platform: Netting and Hedging. The system used is determined by the [client group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk).

### Netting System [#](general_concept#netting)

With this system, you can have only one common position for a symbol at the same time:

-   If there is an open position for a symbol, executing a deal in the same direction increases the volume of this position.
-   If a deal is executed in the opposite direction, the volume of the existing position can be decreased, the position can be closed (when the deal volume is equal to the position volume) or reversed (if the volume of the opposite deal is greater than the current position).

It does not matter, what has caused the opposite deal — an executed market order or a triggered pending order.

The below example shows execution of two EURUSD Buy deal 1 lot each:

![Execution of the two Buy deals resulted in one net position.](/en/docs/mt5/platform/img/netting_positions.png "Execution of the two Buy deals resulted in one net position.")

Execution of both deals resulted in one common position of 2 lots.

### Hedging System [#](general_concept#hedging)

With this system, you can have multiple open positions of one and the same symbol, including opposite positions.

If you have an open position for a symbol, and execute a new deal (or a pending order triggers), a new position is additionally opened. Your current position does not change.

The below example shows execution of two EURUSD Buy deal 1 lot each:

![Execution of the two Buy deals resulted in two trading positions.](/en/docs/mt5/platform/img/hedging_positions.png "Execution of the two Buy deals resulted in two trading positions.")

Execution of these deals resulted in opening two separate positions.

### Impact of the System Selected

Depending on the position accounting system, some of the platform functions may have different behavior:

-   [Stop Loss and Take Profit inheritance](/en/docs/mt5/platform/administration/common_info/general_concept#sltp_inherit) rules change.
-   To close a position in the netting system, you should perform an opposite trading operation for the same symbol and the same volume. To close a position in the hedging system, explicitly select the "Close Position" command in the context menu of the position.
-   A position cannot be reversed in the hedging system. In this case, the current position is closed and a new one with the remaining volume is opened.
-   In the hedging system, a new condition for margin calculation is available — [Hedged margin](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex_hedge#hedged).

## Types of Orders [#](general_concept#order_type)

The trading platform allows to prepare and issue requests for the broker to execute trading operations. In addition, the platform allows to control and manage open positions. Several types of trading orders are used for these purposes. An order is a trader's instruction to the broker to perform a trade operation. In the platform, orders are divided into two main types: market and pending. In addition, there are special [Stop Loss](/en/docs/mt5/platform/administration/common_info/general_concept#stop_loss) and [Take Profit](/en/docs/mt5/platform/administration/common_info/general_concept#take_profit) orders.

### Market Order [#](general_concept#market_order)

A market order is an instruction given to a brokerage company to buy or sell a financial instrument. Execution of this order results in the execution of a deal. The price at which the deal is executed is determined by the [type of execution](/en/docs/mt5/platform/administration/common_info/general_concept#execution_type) that depends on the symbol type. Generally, a security is bought at the Ask price and sold at the Bid price.

### Pending Order [#](general_concept#pending_order)

A pending order is the trader's instruction to a brokerage company to buy or sell a security in future under pre-defined conditions. The following types of pending orders are available:

-   Buy Limit — a trade request to buy at the Ask price that is equal to or less than that specified in the order. The current price level is higher than the value specified in the order. Usually this order is placed in anticipation of that the security price will fall to a certain level and then will increase;
-   Buy Stop — a trade order to buy at the "Ask" price equal to or greater than the one specified in the order. The current price level is lower than the value specified in the order. Usually this order is placed in the anticipation that the price will reach a certain level and will continue to grow;
-   Sell Limit — a trade order to sell at the "Bid" price equal to or greater than the one specified in the order. The current price level is lower than the value specified in the order. Usually this order is placed in anticipation of that the security price will increase to a certain level and will fall then;
-   Sell Stop — a trade order to sell at the "Bid" price equal to or less than the one specified in the order. The current price level is higher than the value in the order. Usually this order is placed in anticipation of that the security price will reach a certain level and will keep on falling.
-   Buy Stop Limit — this type is the combination of the first two types, being a stop order to place a Buy Limit order. As soon as the future Ask price reaches the stop-level indicated in the order (the Price field), a Buy Limit order will be placed at the level, specified in Stop Limit price field. A stop level is set above the current Ask price, while Stop Limit price is set below the stop level.
-   Sell Stop Limit — this order is a stop order to place a Sell Limit order. As soon as the future Bid price reaches the stop-level indicated in the order (the Price field), a Sell Limit order will be placed at the level, specified in Stop Limit price field. A stop level is set below the current Bid price, while Stop Limit price is set above the stop level.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">For symbols with Exchange Stocks, Exchange Futures and Futures Forts <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#calculation" class="topiclink">calculation modes</a>, all types of pending orders are triggered according to the rules of the exchange where trading is performed. Usually, Last price (price of the last performed transaction) is applied. In other words, an order triggers when the Last price touches the price specified in the order. But note that buying or selling as a result of triggering of an order is always performed by the Ask and Bid prices respectively.</span></li><li class="p_tableatten"><span class="f_tableatten">In the "Exchange execution" mode, the price specified when placing limit orders is not verified. It can be specified above the current Ask price (for the Buy Limit orders) and below the current Bid price (for the Sell Limit orders). When placing an order with such a price, it triggers almost immediately and turns into a market one. However, unlike market orders where a trader agrees to perform a deal by a non-specified current market price, a pending order will be executed at a price no worse than the one specified.</span></li><li class="p_tableatten"><span class="f_tableatten">If during pending order activation the corresponding market operation cannot be executed (for example, the free margin on the account is not enough), the pending order will be canceled and moved to history with the "Rejected" status.</span></li></ul></td></tr></tbody></table>

![Types of pending orders](/en/docs/mt5/platform/img/order_types.png "Types of pending orders")

<table class="help" cellspacing="0" cellpadding="2" border="0" style="margin:0 auto; width:550px; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Current market state" title="Current market state" width="6" height="14" src="/en/docs/mt5/platform/img/order_type_red_bar.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— current market state</span></p></td><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Forecast" title="Forecast" width="6" height="14" src="/en/docs/mt5/platform/img/order_type_gray_bar.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— forecast</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Current price" title="Current price" width="12" height="12" src="/en/docs/mt5/platform/img/order_type_current.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— current price</span></p></td><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Order price" title="Order price" width="12" height="12" src="/en/docs/mt5/platform/img/order_type_order.png"></p></td><td style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— order price</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Price, reaching which a pending order will be placed" title="Price, reaching which a pending order will be placed" width="12" height="12" src="/en/docs/mt5/platform/img/order_type_trigger.png"></p></td><td colspan="3" style="vertical-align:middle; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— price, reaching which a pending order will be placed</span></p></td></tr><tr><td style="vertical-align:middle; width:26px; height:19px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Expected growth" title="Expected growth" width="15" height="16" src="/en/docs/mt5/platform/img/order_type_arrow_up.png"></p></td><td style="vertical-align:middle; height:19px; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable"></span><span class="f_ol">— expected growth</span></p></td><td style="vertical-align:middle; width:26px; height:19px; padding:2px; border:none"><p class="p_fortable"><img class="help" alt="Expected fall" title="Expected fall" width="14" height="16" src="/en/docs/mt5/platform/img/order_type_arrow_down.png"></p></td><td style="vertical-align:middle; height:19px; padding:2px; border:none"><p class="p_fortable"><span class="f_fortable">— expected fall</span></p></td></tr></tbody></table>

### Take Profit [#](general_concept#take_profit)

The Take Profit order is intended for gaining the profit when the security price reaches a certain level. Execution of this order results in the complete closing of the entire position. It is always connected to an open position or a pending order. The order can be requested only together with a market or a pending order. This order condition for long positions is checked using the Bid price (the order is always set above the current Bid price), and the Ask price is used for short positions (the order is always set below the current Ask price).

### Stop Loss [#](general_concept#stop_loss)

This order is used for minimizing losses if the security price moves the wrong direction. If the security price reaches this level, the entire position is closed automatically. Such orders are always associated with an open position or a pending order. They can be requested only together with a market or a pending order. This order condition for long positions is checked using the Bid price (the order is always set below the current Bid price), and the Ask price is used for short positions (the order is always set above the current Ask price).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If during Take Profit or Stop Loss activation the corresponding market operation cannot be executed (for example, it is rejected by the exchange), the order will not be deleted. It will trigger again at the next tick corresponding to the order activation conditions.</span></p></td></tr></tbody></table>

### Rules of Stop Loss and Take Profit inheritance ([netting](/en/docs/mt5/platform/administration/common_info/general_concept#netting)): [#](general_concept#sltp_inherit)

-   When a position volume is increased or the position is reversed, Take Profit and Stop Loss are placed according to its latest order (market or triggered pending order). In other words, stop levels in each subsequent order of the same position replace previous ones. If zero values are specified in the order, Stop Loss and Take Profit of a position will be deleted.
-   If a position is partially closed, Stop Loss and Take Profit are not changed by the new order.
-   If a position is fully closed, the Stop Loss and Take Profit levels are deleted, because they are associated with an open position and cannot exist without it.
-   When a trade operation is executed for a symbol, for which there is a position, the current Stop Loss and Take Profit of the open position are automatically inserted in the order placing window. This is aimed to prevent accidental deletion of current stop orders.
-   During one click trading operation (from a panel on the chart or from the Market Watch) for the symbol, for which there is a position, the current values of Stop Loss and Take Profit are not changed.
-   On the OTC markets (Forex, CFD, Futures), when a position is moved to the next trading day (the swap), including swap through re-opening, the levels of Stop Loss and Take Profit remain unchanged.
-   On the exchange market, when a position is moved to the next trading day (the swap), as well as when moved to another account or during delivery, the levels of Stop Loss and Take Profit are reset.

### Stop Loss and Take Profit inheritance rule ([hedging](/en/docs/mt5/platform/administration/common_info/general_concept#hedging)):

-   If a position is partially closed, Stop Loss and Take Profit are not changed by the new order.
-   If a position is fully closed, the Stop Loss and Take Profit levels are deleted, because they are associated with an open position and cannot exist without it.
-   t0>During one click trading operation (from a panel on the chart or Depth of Market), the Stop Loss and Take Profit levels are not set.

These rules apply both when trading manually and when placing orders from Expert Advisors (MQL5 programs).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Activation of Take Profit or Stop Loss results in the complete closing of the entire position.</span></li><li class="p_tableatten"><span class="f_tableatten">For symbols with Exchange Stocks, Exchange Futures and Futures Forts <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#calculation" class="topiclink">calculation modes</a>, Stop Loss and Take Profit orders are triggered according to the rules of the exchange where trading is performed. Usually, Last price (price of the last performed transaction) is applied. In other words, a stop-order triggers when the Last price touches the specified price. However note that buying or selling as a result of activation of a stop-order is always performed by the Bid and Ask prices.</span></li></ul></td></tr></tbody></table>

## State of Orders [#](general_concept#order_state)

After an order has been formed and sent to a trade server, it can undergo the following stages:

-   Started — the order correctness has been checked, but it hasn't been yet accepted by the broker;
-   Placed — a dealer has accepted the order;
-   Partially filled — the order is filled partially;
-   Filled — the entire order is filled;
-   Canceled — the order is canceled by the client;
-   Rejected — the order is rejected by a dealer;
-   Expired — the order is canceled due to its expiration.

You can view the state of orders in the [corresponding section](/en/docs/mt5/platform/administration/admin_orders#state).

![The order status shows the current order processing step](/en/docs/mt5/platform/img/order_state_scheme.png "The order status shows the current order processing step")

## Types of Execution [#](general_concept#execution_type)

Four [order execution modes](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution) are available in the trading platform:

-   Instant Execution  
    In this mode, an order is executed at the price offered to a broker. When sending an order to be executed, the platform automatically adds the current prices to the order. If the broker accepts the prices, the order is executed. If the broker does not accept the requested price, a "Requote" is sent — the broker returns prices, at which this order can be executed.
-   Request Execution  
    In this mode, a market order is executed at the price previously received from a broker. Prices for a certain market order are requested from the broker before the order is sent. After the prices have been received, order execution at the given price can be either confirmed or rejected.
-   Market Execution  
    In this order execution mode, a broker makes a decision about the order execution price without any additional discussion with a trader. Sending an order in such a mode means advance consent to its execution at this price.
-   Exchange Execution  
    In this mode, trade operations conducted in the trading platform are sent to an external trading system (exchange). Trade operations are executed at the prices of current market offers.

## Fill Policy [#](general_concept#fill_policy)

In addition to common rules of order execution set by a broker, a trader can indicate additional conditions. The available fill policies are determined by the [symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#fill_policy).

-   Fill or Kill (FOK)  
    This fill policy means that an order can be filled only in the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The required volume can be filled by several offers available in the market at the moment.
-   Immediate or Cancel (IOC)  
    In this case a trader agrees to execute a deal with the volume maximally available in the market within that indicated in the order. In case the order cannot be filled completely, the available volume of the order will be filled, and the remaining volume will be canceled. The possibility of using IOC orders is determined on the trade server.
-   Book or Cancel (BOC)  
    The BOC policy indicates that the order can only be placed in the Depth of Market (order book). If the order can be filled immediately when placed, this order is canceled. This policy guarantees that the price of the placed order will be worse than the current market. BOC is used to implement passive trading: it is guaranteed that the order cannot be executed immediately when placed and thus it does not affect current liquidity. This fill policy is only supported for limit and stop limit orders.
-   Return  
    This policy is only used for market (Buy and Sell), [limit and stop limit orders](/en/docs/mt5/platform/administration/common_info/general_concept#pending_order). If filled partially, an order with the remaining volume is not canceled, and is processed further. For market orders, the Return policy is used only in the Exchange Execution [mode](/en/docs/mt5/platform/administration/common_info/general_concept#execution_type), while for limit and stop limit ones, it is applied in the Market Execution and Exchange Execution modes.

Use of fill policies depending on the execution type can be shown as the following table:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type of Execution/Fill Policy</span></p></th><th class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Fill or Kill</span></p></th><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Immediate or Cancel</span></p></th><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Book or Cancel</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Return</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Instant Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">—</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Request Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">—</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Market Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">+</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Exchange Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">+</span></p></td></tr></tbody></table>

[General Information](/en/docs/mt5/platform/administration/common_info)

[Price Data](/en/docs/mt5/platform/administration/common_info/price_data)