# Fill Policy

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/general_concept/fill_policy

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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)[Trading Principles](/en/docs/mt5/android/trade/general_concept)Fill Policy

# Fill Policy

In addition to common rules of order execution set by a broker, a trade can indicate additional conditions in the ["Fill Policy"](/en/docs/mt5/android/trade/open_positions/position_exchange#fill_policy) field of the order placing window:

-   Fill or Kill  
    This execution policy means that an order can be executed only in the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The required volume can be filled by several offers available on the market at the moment.
-   Immediate or Cancel  
    In this case a trader agrees to execute a deal with the volume maximally available in the market within that indicated in the order. In case the order cannot be filled completely, the available volume of the order will be filled, and the remaining volume will be canceled. The possibility of using IOC orders is determined on the trade server.
-   Book or Cancel (BOC)  
    The BOC policy indicates that the order can only be placed in the Depth of Market (order book). If the order can be filled immediately when placed, this order is canceled. This policy guarantees that the price of the placed order will be worse than the current market. BOC is used to implement passive trading: it is guaranteed that the order cannot be executed immediately when placed and thus it does not affect current liquidity. This fill policy is only supported for limit and stop limit orders.
-   Return  
    This policy is only used for market (Buy and Sell), [limit and stop limit orders](/en/docs/mt5/android/trade/general_concept/order_types). If filled partially, an order with the remaining volume is not canceled, and is processed further. For market orders, the Return policy is used only in the Exchange Execution [mode](/en/docs/mt5/android/trade/general_concept/execution_types), while for limit and stop limit ones, it is applied in the Market Execution and Exchange Execution modes.

Use of fill policies depending on the execution type can be shown as the following table:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type of Execution\Fill Policy</span></p></th><th class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Fill or Kill</span></p></th><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Immediate or Cancel</span></p></th><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Book or Cancel</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Return</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Instant Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">—</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Request Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">—</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Market Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">—</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">+</span></p></td></tr><tr class="table"><td class="table" style="width:288px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Exchange Execution</span></p></td><td class="table" style="width:161px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">+</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">+</span></p></td></tr></tbody></table>

[State of Orders](/en/docs/mt5/android/trade/general_concept/order_state)

[Opening and Closing Positions](/en/docs/mt5/android/trade/open_positions)