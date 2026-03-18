# Modifying a Position

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/change_positions

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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)Modifying a Position

<table class="container" cellspacing="0" cellpadding="0" border="0"><tbody><tr class="container"><td class="container" style="width:50%;"><h1><a name="modify" class="hmanchor"></a>Modifying a Position</h1><p class="p_txt"><span class="f_txt">Modification of the current position implies changing its <a href="/en/docs/mt5/android/trade/general_concept/order_types#stop_loss" class="topiclink">Stop Loss</a> and <a href="/en/docs/mt5/android/trade/general_concept/order_types#take_profit" class="topiclink">Take Profit</a> levels.</span></p><p class="p_txt"><span class="f_txt">There are several ways to modify stop levels:</span></p><ul><li class="p_ol"><span class="f_ol">If there is an open position for a symbol, and a <a href="/en/docs/mt5/android/trade/open_positions" class="topiclink">new order</a> is placed for it, then the Stop Loss and Take Profit levels of the new order will be used for the entire position.</span></li><li class="p_ol"><span class="f_ol">Stop levels can be changed by modifying the position.</span></li></ul><p class="p_txt"><span class="f_txt">To modify position stop levels, go to the <a href="/en/docs/mt5/android/trade#context" class="topiclink">"Trade"</a> tab and run the "Modify position" command in the position context menu. This command will open a window as on the screenshot on the right.</span></p><p class="p_txt"><span class="f_txt">To change the parameter value, tap on - or + next to the field or on the field to specify a value using a keyboard</span><span class="f_ol">.</span></p></td><td class="container" style="width:50%;"><p class="p_Image"><img class="help" alt="Modifying a Position" title="Modifying a Position" width="326" height="512" src="/en/docs/mt5/android/img/position_modify.png"></p></td></tr><tr class="container"><td class="container" colspan="2" style="width:50%;"><p class="p_txt"><span class="f_txt">To modify the stop levels of a position, tap "Modify".</span></p><div><div class="parent-table"><table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">The "Modify" button is disabled until you set correct values for "<a href="/en/docs/mt5/android/trade/general_concept/order_types#stop_loss" class="topiclink">Stop Loss</a>" and "<a href="/en/docs/mt5/android/trade/general_concept/order_types#take_profit" class="topiclink">Take Profit</a>". Terms of stop levels are determined by the broker and are specified in <a href="/en/docs/mt5/android/quotes#specification" class="topiclink">symbol properties</a> (specification of contracts).</span></p></td></tr></tbody></table></div></div></td></tr></tbody></table>

[Close By](/en/docs/mt5/android/trade/closeby)

[Placing Pending Orders](/en/docs/mt5/android/trade/pending_place)