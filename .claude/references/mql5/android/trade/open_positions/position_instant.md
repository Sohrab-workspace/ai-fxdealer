# Instant Execution

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/open_positions/position_instant

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
            -   [Opening and Closing Positions](/en/docs/mt5/android/trade/open_positions)
                -   [Instant Execution](/en/docs/mt5/android/trade/open_positions/position_instant)
                -   [Request Execution](/en/docs/mt5/android/trade/open_positions/position_request)
                -   [Market Execution](/en/docs/mt5/android/trade/open_positions/position_market)
                -   [Exchange Execution](/en/docs/mt5/android/trade/open_positions/position_exchange)
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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)[Opening and Closing Positions](/en/docs/mt5/android/trade/open_positions)Instant Execution

<table class="container" cellspacing="0" cellpadding="0" border="0"><tbody><tr class="container"><td class="container" style="width:50%;"><h1>Instant Execution</h1><p class="p_txt"><span class="f_txt">In this <a href="/en/docs/mt5/android/trade/general_concept/execution_types" class="topiclink">execution mode</a>, a market order is filled at the price offered to the broker. The mobile platform </span><span class="f_ol">automatically inserts current prices in the order.</span></p><h2>Position Opening</h2><p class="p_txt"><span class="f_txt">At the first stage of opening a position, you can specify the following parameters:</span></p><ul><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Symbol</span><span class="f_ol"> — the symbol for which a trade operation should be executed. To change the symbol, tap on <img class="help" alt="Symbols" title="Symbols" width="26" height="20" src="/en/docs/mt5/android/img/symbols_button.png">.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Trade operation type</span><span class="f_ol"> — select "Instant execution" for the market operation. In this field you can also switch to placing a <a href="/en/docs/mt5/android/trade/pending_place" class="topiclink">pending order</a>.</span></li></ul></td><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="Position Opening" title="Position Opening" width="326" height="512" src="/en/docs/mt5/android/img/open_instant.png"></p></td></tr><tr class="container"><td class="container" colspan="2" style="width:50%;"><ul><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Volume</span><span class="f_ol"> — specify here the volume of a trade operation in lots. To change the volume, use side buttons or click on the field to enter the value manually.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">SL</span><span class="f_ol"> — the <a href="/en/docs/mt5/android/trade/general_concept/order_types#stop_loss" class="topiclink">Stop Loss</a> level in prices. If you leave this field empty, this type of order will not be set.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">TP</span><span class="f_ol"> — the <a href="/en/docs/mt5/android/trade/general_concept/order_types#take_profit" class="topiclink">Take Profit</a> level in prices. If you leave this field empty, this type of order will not be set.</span></li><li class="p_ol"><a name="deviation" class="hmanchor"></a><span class="f_ol" style="font-weight: bold;">deviation</span><span class="f_ol"> — the deviation of the order execution price from the specified price, on which the trader agrees. The larger this value, the less likely it is to receive a new execution price (<a href="/en/docs/mt5/android/trade/open_positions/position_instant#requote" class="topiclink">requote</a>) in response to the order execution request. If the deviation is less than or equal to the specified parameter, the order will be executed at the new price without a notice. Otherwise, a broker returns new prices, at which the order can be executed.</span></li></ul><p class="p_txt"><span class="f_txt">Once all the necessary data have been specified, tap "Sell" or "Buy". In this case an order to open a short or long positions, respectively, is sent to the broker.</span></p><div><div class="parent-table"><table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If incorrect Stop Loss and Take Profit are specified in an order, a warning "Invalid S/L or T/P" appears after you tap the Buy or Sell button and the order is not accepted.</span></p></td></tr></tbody></table></div></div></td></tr><tr class="container"><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="Requote" title="Requote" width="326" height="512" src="/en/docs/mt5/android/img/requote.png"></p></td><td class="container" style="width:50%;"><h2><a name="requote" class="hmanchor"></a>Requote <a class="anchor" href="position_instant#requote">#</a></h2><p class="p_txt"><span class="f_txt">If during order processing the symbol price has changed by an amount greater than that indicated in the <a href="/en/docs/mt5/android/trade/open_positions/position_instant#deviation" class="topiclink">"Deviation"</a> field, the dealer (the server) cannot accept the order and offers new execution prices to the trader. In this case, an appropriate message is shown:</span></p><p class="p_Image"><span class="f_Image">&nbsp;</span></p><p class="p_txt"><span class="f_txt">If the trader agrees with the new prices, he or she should tap "Accept", and the order will be executed at the new prices. If the new price does not suit, the trader taps "Reject".</span></p><p class="p_txt"><span class="f_txt">New prices are valid for a few seconds only. If the trader does not decide during that time, after tapping any button the order will be requoted again.</span></p></td></tr><tr class="container"><td class="container" style="width:50%;"><h2>Position Closing</h2><p class="p_txt"><span class="f_txt">In order to close the position you need to tap "Close position" in its context menu on the <a href="/en/docs/mt5/android/trade#context" class="topiclink">"Trade"</a> tab.</span></p><p class="p_txt"><span class="f_txt">Once you tap "Close", the position will be completely closed.</span></p></td><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="Close position" title="Close position" width="326" height="512" src="/en/docs/mt5/android/img/close_instant.png"></p></td></tr></tbody></table>

[Opening and Closing Positions](/en/docs/mt5/android/trade/open_positions)

[Request Execution](/en/docs/mt5/android/trade/open_positions/position_request)