# Close By

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/closeby

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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)Close By

# Close By

The Close By operation allows traders to simultaneously close two opposite positions of the same financial instrument. If opposite positions have different lot values, only one of them will be left open. Its volume will be equal to the difference between the lot values of the two positions, while the direction and open price of the remaining position will be the same as the direction and open price of a larger position.

Compared to a individual closure, the Close By operation allows the trader to save one spread:

-   If the positions are closed separately, the trader pays the spread two times: the Buy position is closed at Bid, and the sell position is closed at Ask.
-   During the Close By operation, the open price of the second position is used to close the first one, and the second position is closed at the open price of the first position.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">This type of operations can only be used with the <a href="/en/docs/mt5/android/trade/general_concept#hedging" class="topiclink">hedging</a> mode of position accounting system.</span></p></td></tr></tbody></table>

Long-tap on a position in order to call the context menu and select the Close By option.

![Close By](/en/docs/mt5/android/img/close_by.png "Close By")

Choose a position and tap "Close".

During the Close By operation, an order of the "close by" type is placed. The tickets of the positions to close are specified in the order comment. A pair of opposite positions is closed by two deals of the "out by" type. The amount of final profit/loss resulting from the closure of the two positions is only indicated in one deal.

![The Close By operation in the History of trading operations](/en/docs/mt5/android/img/close_by_history.png "The Close By operation in the History of trading operations")

[Exchange Execution](/en/docs/mt5/android/trade/open_positions/position_exchange)

[Modifying a Position](/en/docs/mt5/android/trade/change_positions)