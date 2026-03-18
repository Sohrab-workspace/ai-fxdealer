# Position Close

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/positions/positions_control/positions_close

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
            -   [Order Types](/en/docs/mt4/terminal/positions/orders)
            -   [Trailing Stop](/en/docs/mt4/terminal/positions/trailing)
            -   [Types of Execution](/en/docs/mt4/terminal/positions/execution)
            -   [Trade Positions](/en/docs/mt4/terminal/positions/positions_control)
                -   [Open Positions](/en/docs/mt4/terminal/positions/positions_control/positions_open)
                -   [Modifying of Positions](/en/docs/mt4/terminal/positions/positions_control/positions_modify)
                -   [Position Close](/en/docs/mt4/terminal/positions/positions_control/positions_close)
                -   [Placing of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_place)
                -   [Modifying of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_modify)
                -   [Deletion of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_delete)
            -   [Trading on Chart](/en/docs/mt4/terminal/positions/trading_chart)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Trading](/en/docs/mt4/terminal/positions)[Trade Positions](/en/docs/mt4/terminal/positions/positions_control)Position Close

# Position Close

Buying or selling of a security opens a trade position. Then, in order to gain profit of the bid-and-ask price differences, one has to close the position. The latter trade operation is reverse towards to former one. For example, if the former operation consisted in buying of one lot of GOLD, then one lot of the same symbol must be sold to close the position. Positions can be closed differently in the client terminal: It can be closing of a single position, closing of a position by an opposite position, and multiple close by several positions.

## Single Position Closing

A single open trade position will be closed automatically if prices equal to values of [Stop Loss](/en/docs/mt4/terminal/positions/orders) or [Take Profit](/en/docs/mt4/terminal/positions/orders).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: When a long position is being closed, the Bid price must equal to the value of Stop Loss or Take Profit, and Ask price must do for short positions.</span></p></td></tr></tbody></table>

To close a position manually, one has to execute the opened position context menu command of the ["Terminal — Trade" window](/en/docs/mt4/terminal/overview/terminal/terminal_trade) or double-click with the left mouse button on this position.

![instant_order_close](/en/docs/mt4/terminal/img/instant_order_close.png)

If trade operations for a certain symbol are executed [on request](/en/docs/mt4/terminal/positions/execution), one has first to receive quotes by pressing of the "Request" button. This activates the button that allows to close position.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">in the "Execution on request" mode, the offered quotes will be active for just a few seconds. If no decision has been made within these seconds, the "Close... " button will be locked again;</span></li><li class="p_tableatten"><span class="f_tableatten">client terminal allows to close positions partially. To do so, one has to specify the amount of lots less than that given for the opened position in the "Volume" field before pressing of the "Close... " button;</span></li><li class="p_tableatten"><span class="f_tableatten">broker can close positions, as well. For example, it can be done when prices reach the "Stop Out" level that was set by the broker;</span></li><li class="p_tableatten"><span class="f_tableatten">history charts are drawn only on BID prices in the terminal. At that, a part of orders shown in charts is drawn on ASK prices. To get ASK price of the latest bar shown, one has to flag "Show Ask line" option in the <a href="/en/docs/mt4/terminal/setup/setup_charts" class="topiclink">terminal settings</a>.</span></li></ul></td></tr></tbody></table>

## Close by Opposite Positions

Opposite position towards the given one is a reverse position for the same symbol. If there is one or more opposite positions among the open positions, one can close the selected position by and together with an opposite one. To do so, one has first to open the "Order" window (as described above).

![instant_order_close_met](/en/docs/mt4/terminal/img/instant_order_close_met.png)

Then, the "Close by" must be selected in the "Type" field. After that, the list of all opposite positions will appear in the lower part of the window. One has to select an opposite position in this list, and after that the "Close... " button will be activated. It allows to close two positions at the same time. Only one of two opposite positions with different amounts of lots to be traded will remain. The volume (amount of lots) of this position will equal to the difference between lots of the two closed positions, and its direction and open price (short or long) will correspond with those of the larger (in volume) of two closed positions.

## Multiple Close by Opposite Positions

Multiple close of several opposite positions allows to close more than two opposite positions at the same time. To perform this operation, one has also to open the "Order" window (as described above). Then the "Multiple close by" must be selected in the "Type" window. At that, the list of all opposite positions will appear in the lower part of the window, and the "Multiple close by... " button will be active. It allows to close opposite positions. Positions will be closed in pairs, according to the open time, and they will be closed as described above for two opposite positions. If the difference between the sums of volumes is not zero, a new position will be opened as a result of the operation, the volume being equal to this difference. The newly opened position will participate in the multiple close process, but according to its open time, and so on until all positions are closed or the last resulting position is opened.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: After opposite positions have been closed, the corresponding records will be made in the <a href="/en/docs/mt4/terminal/overview/terminal/terminal_account_history" class="topiclink">"Terminal — Account History"</a> window. At that, overhead information about closing of opposite positions will be entered in the "Comment" field.</span></p></td></tr></tbody></table>

[Modifying of Positions](/en/docs/mt4/terminal/positions/positions_control/positions_modify)

[Placing of Pending Orders](/en/docs/mt4/terminal/positions/positions_control/pending_orders_place)