# Placing of Pending Orders

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/pending_place

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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)Placing Pending Orders

<table class="container" cellspacing="0" cellpadding="0" border="0"><tbody><tr class="container"><td class="container" style="width:50%;"><h1>Placing of Pending Orders</h1><p class="p_txt"><span class="f_txt">To place a pending order, do one of the following actions:</span></p><ul><li class="p_ol"><span class="f_ol">In the <a href="/en/docs/mt5/android/quotes" class="topiclink">"Quotes"</a> window, select the required symbol and execute the "New order" command of the context menu.</span></li><li class="p_ol"><span class="f_ol">Tap on <img class="help" alt="Add" title="Add" width="20" height="20" src="/en/docs/mt5/android/img/symbol_add_button.png"> on the <a href="/en/docs/mt5/android/trade" class="topiclink">"Trading"</a> tab.</span></li><li class="p_ol"><span class="f_ol">If there are open positions or orders, use the commands of the context menu commands of the <a href="/en/docs/mt5/android/trade#context" class="topiclink">"Trade"</a> tab.</span></li></ul><p class="p_txt"><span class="f_txt">The following parameters are specified at this stage:</span></p><ul><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Volume</span><span class="f_ol"> — volume of an order in lots. To change the volume, use side buttons or click on the field to enter the value manually.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Symbol</span><span class="f_ol"> — the symbol for which you place a pending order.</span></li></ul></td><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="Pending order" title="Pending order" width="326" height="512" src="/en/docs/mt5/android/img/pending_place.png"></p></td></tr><tr class="container"><td class="container" colspan="2" style="width:50%;"><ul><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Trade operation type</span><span class="f_ol"> — select the <a href="/en/docs/mt5/android/trade/general_concept/order_types#pending_order" class="topiclink">type of a pending order</a>. In this field you can also switch to placing a <a href="/en/docs/mt5/android/trade/open_positions" class="topiclink">market order</a>.</span></li><li class="p_ol"><a name="stop_price" class="hmanchor"></a><span class="f_ol" style="font-weight: bold;">Price</span><span class="f_ol"> — price at which the pending order should trigger. For stop and limit orders this is the price, at which they will be placed. For Stop Limit orders, this is the price of triggering and setting of limit orders at the level specified in "Stop Limit Price".</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Stop Limit Price</span><span class="f_ol"> — this field is active only for Stop Limit orders. When the Stop Limit order triggers, a limit order will be placed at the price specified in it.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">SL</span><span class="f_ol"> — the level of <a href="/en/docs/mt5/android/trade/general_concept/order_types#stop_loss" class="topiclink">Stop Loss</a>. If you leave this field empty, this type of order will not be set.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">TP</span><span class="f_ol"> — Level <a href="/en/docs/mt5/android/trade/general_concept/order_types#take_profit" class="topiclink">Take Profit</a>. If you leave this field empty, this type of order will not be set.</span></li><li class="p_ol"><a name="fill_policy" class="hmanchor"></a><span class="f_ol" style="font-weight: bold;">Fill Policy</span><span class="f_ol"> — additional <a href="/en/docs/mt5/android/trade/general_concept/fill_policy" class="topiclink">rules of filling</a> for <a href="/en/docs/mt5/android/trade/general_concept/order_types" class="topiclink">limit and stop-limit orders</a>: "Fill or Kill", "Immediate or Cancel", "Book or Cancel" or "Return". If this box is unavailable, then the option is locked on the server;</span></li><li class="p_ol"><a name="expiration" class="hmanchor"></a><span class="f_ol" style="font-weight: bold;">Expiration</span><span class="f_ol"> — conditions of the order expiration:</span></li></ul><ul><li class="p_ol_2lev"><span class="f_ol_2lev" style="font-weight: bold;">Good Till Canceled (GTC)</span><span class="f_ol_2lev"> </span><span class="f_ol">— the order will stay in the queue until it is manually canceled.</span></li><li class="p_ol_2lev"><span class="f_ol_2lev" style="font-weight: bold;">Today</span><span class="f_ol_2lev"> </span><span class="f_ol">— the order will be valid only during the current trading day.</span></li><li class="p_ol_2lev"><span class="f_ol_2lev" style="font-weight: bold;">Date and Time</span><span class="f_ol_2lev"> </span><span class="f_ol">— the order will be valid until the specified date. When selecting this option, you will automatically switch to the date and time specification. To return to choosing the expiration type, remove the expiration date.</span></li><li class="p_ol_2lev"><span class="f_ol" style="font-weight: bold;">Date</span><span class="f_ol"> — the order will be valid until 00:00 of the specified day. If this time is not within a trading session, expiration will occur in the nearest trading time.</span></li></ul><div><div class="parent-table"><table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">The "Place" button is inactive if any of the parameters is incorrect.</span></li><li class="p_tableatten"><span class="f_tableatten">Stop Loss and Take Profit orders only trigger for open positions, not for pending orders.</span></li><li class="p_tableatten"><span class="f_tableatten">If the field "Execution" and "Expiration" fields are inactive, it means the possibility to change them is locked on the server.</span></li></ul></td></tr></tbody></table></div></div></td></tr></tbody></table>

[Modifying a Position](/en/docs/mt5/android/trade/change_positions)

[Managing Pending Orders](/en/docs/mt5/android/trade/pending_change)