# Close By

> Source: https://support.metaquotes.net/en/docs/mt5/iphone/trade/closeby

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

[MetaTrader 5](/en/docs/mt5)[iPhone/iPad](/en/docs/mt5/iphone)[Trade](/en/docs/mt5/iphone/trade)Close By

# Close By

The Close By operation allows traders to simultaneously close two opposite positions of the same financial instrument. If opposite positions have different lot values, only one of them will be left open. Its volume will be equal to the difference between the lot values of the two positions, while the direction and open price of the remaining position will be the same as the direction and open price of a larger position.

Compared to a individual closure, the Close By operation allows the trader to save one spread:

-   If the positions are closed separately, the trader pays the spread two times: the Buy position is closed at Bid, and the sell position is closed at Ask.
-   During the Close By operation, the open price of the second position is used to close the first one, and the second position is closed at the open price of the first position.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">This type of operations can only be used with the <a href="/en/docs/mt5/iphone/trade/general_concept#hedging" class="topiclink">hedging</a> mode of position accounting system.</span></p></td></tr></tbody></table>

To close a position by an opposite one:

-   Open its context menu in the Trade tab and select the appropriate command.
-   Alternatively, select the position on the chart, expand the lower trading menu upward, and switch to the corresponding tab.

![Close By](/en/docs/mt5/iphone/img/close_by.png "Close By")

Choose a position and tap 'Close'.

During the Close By operation, an order of the "close by" type is placed. The tickets of positions are specified in the order comment. A pair of opposite positions is closed by two deals of the 'out by' type. The amount of final profit/loss resulting from the closure of the two positions is only indicated in one deal.

![The Close By operation in the History of trading operations](/en/docs/mt5/iphone/img/close_by_history.png "The Close By operation in the History of trading operations")

[Opening and Closing Positions](/en/docs/mt5/iphone/trade/open_positions)

[Modifying a Position](/en/docs/mt5/iphone/trade/change_positions)