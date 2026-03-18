# Market Execution

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/open_positions/position_market

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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)[Opening and Closing Positions](/en/docs/mt5/android/trade/open_positions)Market Execution

<table class="container" cellspacing="0" cellpadding="0" border="0"><tbody><tr class="container"><td class="container" style="width:50%;"><h1>Market Execution</h1><p class="p_txt"><span class="f_txt">In the <a href="/en/docs/mt5/android/trade/general_concept/execution_types" class="topiclink">Market Execution</a> mode, a trader agrees to execute a deal at the price offered by a broker.</span></p><h2>Position Opening</h2><p class="p_txt"><span class="f_txt">Fill out the following fields in the order placing window:</span></p><ul><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Symbol</span><span class="f_ol"> — the symbol for which a trade operation should be executed. To change the symbol, tap on <img class="help" alt="Symbols" title="Symbols" width="26" height="20" src="/en/docs/mt5/android/img/symbols_button.png">.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Volume</span><span class="f_ol"> — volume of an order in lots. To change the volume, use side buttons or click on the field to enter the value manually.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">Trade operation type</span><span class="f_ol"> — select the appropriate item for the "Market Execution" mode. In this field you can also switch to placing a <a href="/en/docs/mt5/android/trade/pending_place" class="topiclink">pending order</a>.</span></li></ul></td><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="An order in the Market Execution mode" title="An order in the Market Execution mode" width="326" height="512" src="/en/docs/mt5/android/img/open_market.png"></p></td></tr><tr class="container"><td class="container" colspan="2" style="width:50%;"><ul><li class="p_ol"><span class="f_ol" style="font-weight: bold;">SL</span><span class="f_ol"> — the <a href="/en/docs/mt5/android/trade/general_concept/order_types#stop_loss" class="topiclink">Stop Loss</a> level in prices. If you leave this field empty, this type of order will not be set.</span></li><li class="p_ol"><span class="f_ol" style="font-weight: bold;">TP</span><span class="f_ol"> — the <a href="/en/docs/mt5/android/trade/general_concept/order_types#take_profit" class="topiclink">Take Profit</a> level in prices. If you leave this field empty, this type of order will not be set.</span></li><li class="p_ol"><a name="fill_policy" class="hmanchor"></a><span class="f_ol" style="font-weight: bold;">Fill Policy</span><span class="f_ol"> — additional <a href="/en/docs/mt5/android/trade/general_concept/fill_policy" class="topiclink">rules of order filling</a>: "Fill or Kill" or "Immediate or Cancel". If this box is not active, then the option is locked on the server.</span></li></ul><p class="p_txt"><span class="f_txt">A click on "Sell by Market" or "Buy by Market" creates an order to a broker to execute a Sell or Buy deal respectively at the broker defined price.</span></p><div><div class="parent-table"><table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the "Execution" box is not active, then the option is locked on the server.</span></p></td></tr></tbody></table></div></div></td></tr><tr class="container"><td class="container" style="width:50%;"><br></td><td class="container" style="width:50%;"><br></td></tr><tr class="container"><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="Close by Market" title="Close by Market" width="326" height="512" src="/en/docs/mt5/android/img/close_market.png"></p></td><td class="container" style="width:50%;"><h2>Position Closing</h2><p class="p_txt"><span class="f_txt">In order to close the position you need to tap "Close position" in its context menu on the <a href="/en/docs/mt5/android/trade#context" class="topiclink">"Trade"</a> tab.</span></p><p class="p_txt"><span class="f_txt">Once you tap "Close by Market", the position will be completely closed.</span></p></td></tr></tbody></table>

[Request Execution](/en/docs/mt5/android/trade/open_positions/position_request)

[Exchange Execution](/en/docs/mt5/android/trade/open_positions/position_exchange)