# Opening and Closing Positions

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/open_positions

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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)Opening and Closing Positions

# Opening and Closing Positions

Opening of a [position](/en/docs/mt5/android/trade/general_concept#position) or entering the market is the primary buy or sale of a certain amount of a financial instrument. In the trading platform, this can be done by placing a [market order](/en/docs/mt5/android/trade/general_concept/order_types#market_order), as a result of which a [deal](/en/docs/mt5/android/trade/general_concept#deal) is executed. A position can also be opened at the triggering of a [pending order](/en/docs/mt5/android/trade/general_concept/order_types#pending_order).

Then, in order to profit from the difference of rates, it is necessary to close the position. When you close a trade position, an operation opposite to the first one is performed. For example, if the first trade operation was buying one lot of GOLD, then to close the position, sell one lot of the same instrument.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A position can be closed fully or partially, depending on the volume of a trade executed in the opposite direction.</span></p></td></tr></tbody></table>

There are several ways to call a dialog window for order creation:

-   In the ["Quotes"](/en/docs/mt5/android/quotes) window, select the required symbol and execute the "New order" command of the context menu.
-   If there are open positions or orders, use the commands of the context menu commands of the ["Trade"](/en/docs/mt5/android/trade#context) tab.

Performing one of these actions will open an order placing window corresponding to the [execution type](/en/docs/mt5/android/trade/general_concept/execution_types) of the selected symbol:

-   [Instant Execution](/en/docs/mt5/android/trade/open_positions/position_instant)
-   [Request Execution](/en/docs/mt5/android/trade/open_positions/position_request)
-   [Market Execution](/en/docs/mt5/android/trade/open_positions/position_market)
-   [Exchange Execution](/en/docs/mt5/android/trade/open_positions/position_exchange)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Once an order is executed, a corresponding record about an opened position appears on the "Trade" tab, and the order and the deal (deals) will appear in the "History" tab.</span></p></td></tr></tbody></table>

[Fill Policy](/en/docs/mt5/android/trade/general_concept/fill_policy)

[Instant Execution](/en/docs/mt5/android/trade/open_positions/position_instant)