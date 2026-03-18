# Common Trading Principles

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/general_concept

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
        -   [Getting Started](/en/docs/mt5/android/getting_started)
        -   [Quotes](/en/docs/mt5/android/quotes)
        -   [Depth of Market](/en/docs/mt5/android/depth_of_market)
        -   [Charts](/en/docs/mt5/android/chart)
        -   [Trade](/en/docs/mt5/android/trade)
            -   [Trading Principles](/en/docs/mt5/android/trade/general_concept)
                -   [Types of Orders](/en/docs/mt5/android/trade/general_concept/order_types)
                -   [Types of Execution](/en/docs/mt5/android/trade/general_concept/execution_types)
                -   [State of Orders](/en/docs/mt5/android/trade/general_concept/order_state)
                -   [Fill Policy](/en/docs/mt5/android/trade/general_concept/fill_policy)
            -   [Opening and Closing Positions](/en/docs/mt5/android/trade/open_positions)
            -   [Close By](/en/docs/mt5/android/trade/closeby)
            -   [Modifying a Position](/en/docs/mt5/android/trade/change_positions)
            -   [Placing Pending Orders](/en/docs/mt5/android/trade/pending_place)
            -   [Managing Pending Orders](/en/docs/mt5/android/trade/pending_change)
            -   [Bulk Operations](/en/docs/mt5/android/trade/bulk_operations)
        -   [History](/en/docs/mt5/android/history)
        -   [Accounts](/en/docs/mt5/android/settings_accounts)
        -   [Mailbox](/en/docs/mt5/android/settings_mail)
        -   [News Event](/en/docs/mt5/android/settings_news)
        -   [Messages](/en/docs/mt5/android/messages)
        -   [Settings](/en/docs/mt5/android/settings)
        -   [Journal](/en/docs/mt5/android/settings_journal)
        -   [About](/en/docs/mt5/android/settings_about)
        -   [Push Notifications](/en/docs/mt5/android/push)
        -   [Tablet Version](/en/docs/mt5/android/tablet)
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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)Trading Principles

<table class="container" cellspacing="0" cellpadding="0" border="0"><tbody><tr class="container"><td class="container" colspan="2" style="width:50%;"><h1>Common Trading Principles</h1><p class="p_txt"><span class="f_txt">Before you proceed to study the trade functions of the platform, you must get a clear understanding of the basic terms: order, deal and position.</span></p><ul><li class="p_ol"><a name="order" class="hmanchor"></a><span class="f_ol" style="font-weight: bold;">Order</span><br><span class="f_ol">An order is an instruction given to a broker to buy or sell a financial instrument. There are two main <a href="/en/docs/mt5/android/trade/general_concept/order_types" class="topiclink">types of orders</a>: market and pending. In addition, there are special <a href="/en/docs/mt5/android/trade/general_concept/order_types#take_profit" class="topiclink">Take Profit</a> and <a href="/en/docs/mt5/android/trade/general_concept/order_types#stop_loss" class="topiclink">Stop Loss</a> orders.</span></li><li class="p_ol"><a name="deal" class="hmanchor"></a><span class="f_ol" style="font-weight: bold;">Deal</span><br><span class="f_ol">A deal is the commercial exchange (buying or selling) of a financial security. Buying is executed at the demand price (Ask), and Sell is performed at the supply price (Bid). A deal can appear resulting from the execution of a market order or triggering of a pending order. Keep in mind that in some cases, execution of an order can result in several deals.</span></li><li class="p_ol"><a name="position" class="hmanchor"></a><span class="f_ol" style="font-weight: bold;">Position</span><br><span class="f_ol">A position is a trade obligation, i.e. the number of bought or sold contracts of a financial instrument. A long position is financial security bought expecting the security price go higher. A short position is an obligation to supply a security expecting the price will fall in future.</span></li></ul><h2>General Scheme of Trade Operations</h2><ul><li class="p_ol"><span class="f_ol">From the trading platform, an order is sent to a broker to execute a deal with the specified parameters.</span></li><li class="p_ol"><span class="f_ol">On the server, correctness of an order is checked (correctness of prices, availability of funds on the account, etc.).</span></li><li class="p_ol"><span class="f_ol">Orders that have passed the check wait to be processed on the trade server. Then the order can be:</span></li></ul><ul><li class="p_ol_2lev"><span class="f_ol_2lev">executed (in one of automatic <a href="/en/docs/mt5/android/trade/general_concept/execution_types" class="topiclink">execution</a> modes or by a dealer)</span></li><li class="p_ol_2lev"><span class="f_ol_2lev">canceled upon expiry</span></li><li class="p_ol_2lev"><span class="f_ol_2lev">rejected (e.g. when money is not enough or there is no suiting offer in the market; or rejected by the dealer)</span></li><li class="p_ol_2lev"><span class="f_ol_2lev">canceled by a trader;</span></li><li class="p_ol"><span class="f_ol">Execution of a market order or triggering of a pending order results in a deal;</span></li><li class="p_ol"><span class="f_ol">If there are no positions for a symbol, conclusion of a deal results in opening of a position. If there is a position for the symbol, the deal will lead to increase or reduction of the position volume, its closure or reversal.</span></li></ul><div class="p_Image"><div><img class="help" alt="Scheme of trade operations" title="Scheme of trade operations" width="768" height="198" src="/en/docs/mt5/android/img/trading_scheme.png"><p><span class="f_Image">Scheme of trade operations</span></p></div></div></td></tr><tr class="container"><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="Execution of the two Buy deals resulted in one net position" title="Execution of the two Buy deals resulted in one net position" width="325" height="512" src="/en/docs/mt5/android/img/netting_positions.png"></p></td><td class="container" style="width:50%;"><h2><a name="position_type" class="hmanchor"></a>Position Accounting System <a class="anchor" href="general_concept#position_type">#</a></h2><p class="p_txt"><span class="f_txt">Two position accounting systems are supported in the trading platform: Netting and Hedging. The system used depends on the account and is set by the broker.</span></p><h3><a name="netting" class="hmanchor"></a>Netting System <a class="anchor" href="general_concept#netting">#</a></h3><p class="p_txt"><span class="f_txt">With this system, you can have only one common position for a symbol at the same time:</span></p><ul><li class="p_ol"><span class="f_ol">If there is an open position for a symbol, executing a deal in the same direction increases the volume of this position.</span></li><li class="p_ol"><span class="f_ol">If a deal is executed in the opposite direction, the volume of the existing position can be decreased, the position can be closed (when the deal volume is equal to the position volume) or reversed (if the volume of the opposite deal is greater than the current position).</span></li></ul></td></tr><tr class="container"><td class="container" colspan="2" style="width:50%;"><p class="p_txt"><span class="f_txt">It does not matter, what has caused the opposite deal — an executed market order or a triggered pending order.</span></p><p class="p_txt"><span class="f_txt">The above example shows execution of two EURUSD Buy deal 0.5 lots each.</span></p><p class="p_txt"><span class="f_txt">As a result of execution of these two trades, one total 1-lot position is opened.</span></p></td></tr><tr class="container"><td class="container" style="width:50%;"><h2><a name="hedging" class="hmanchor"></a>Hedging System <a class="anchor" href="general_concept#hedging">#</a></h2><p class="p_txt"><span class="f_txt">With this system, you can have multiple open positions of one and the same symbol, including opposite positions.</span></p><p class="p_txt"><span class="f_txt">If you have an open position for a symbol, and execute a new deal (or a pending order triggers), a new position is additionally opened. Your current position does not change.</span></p><p class="p_txt"><span class="f_txt">An example to the left shows execution of two EURUSD Buy deal 0.5 lots each:</span></p><p class="p_txt"><span class="f_txt">As a result of execution of these two trades, two separate positions are opened.</span></p><h3>Impact of the System Selected</h3><p class="p_txt"><span class="f_txt">Depending on the position accounting system, some of the platform functions may have different behavior:</span></p><ul><li class="p_ol"><span class="f_ol">Rules of <a href="/en/docs/mt5/android/trade/general_concept/order_types#sltp_inherit" class="topiclink">Stop Loss and Take Profit inheritance</a> also change.</span></li></ul></td><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="Execution of the two Buy deals resulted in two trading positions" title="Execution of the two Buy deals resulted in two trading positions" width="326" height="512" src="/en/docs/mt5/android/img/hedging_positions.png"></p></td></tr><tr class="container"><td class="container" colspan="2" style="width:50%;"><ul><li class="p_ol"><span class="f_ol">To <a href="/en/docs/mt5/android/trade/open_positions" class="topiclink">close a position</a> in the netting system, you should perform an opposite trading operation for the same symbol and the same volume.</span></li><li class="p_ol"><span class="f_ol">In order to close a position in the hedging system, explicitly select the "Close Position" command in the context menu of the position.</span></li><li class="p_ol"><span class="f_ol">A position cannot be reversed in the hedging system. In this case, the current position is closed and a new one with the remaining volume is opened.</span></li><li class="p_ol"><span class="f_ol">In the hedging system, a new condition for margin calculation is available — <a href="https://www.metatrader5.com/en/terminal/help/trading_advanced/margin_forex#hedging" target="_blank" class="weblink">Hedged margin</a>.</span></li></ul></td></tr></tbody></table>

[Trade](/en/docs/mt5/android/trade)

[Types of Orders](/en/docs/mt5/android/trade/general_concept/order_types)