# Trailing Stop

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/positions/trailing

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Trading](/en/docs/mt4/terminal/positions)Trailing Stop

# Trailing Stop

Stop Loss is intended for reducing of losses where the symbol price moves in an unprofitable direction. If the position becomes profitable, [Stop Loss](/en/docs/mt4/terminal/positions/orders) can be manually shifted to a break-even level. To automate this process, Trailing Stop was created. This tool is especially useful when price changes strongly in the same direction or when it is impossible to watch the market continuously for some reason.

![trailing_stop_menu](/en/docs/mt4/terminal/img/trailing_stop_menu.png)

Trailing Stop is always attached to an open position and works in client terminal, not at the server like Stop Loss, for example. To set the trailing stop, one has to execute the open position context menu command of the same name in the ["Terminal" window](/en/docs/mt4/terminal/overview/terminal/terminal_trade). Then one has to select the desirable value of distance between the Stop Loss level and the current price in the list opened. Only one trailing stop can be set for each open position.

After the above actions have been performed, at incoming of new quotes, the terminal checks whether the open position is profitable. As soon as profit in points becomes equal to or higher than the specified level, command to place the [Stop Loss order](/en/docs/mt4/terminal/positions/orders) will be given automatically. The order level is set at the specified distance from the current price. Further, if price changes in the more profitable direction, trailing stop will make the Stop Loss level follow the price automatically, but if profitability of the position falls, the order will not be modified anymore. Thus, the profit of the trade position is fixed automatically. After each automatic [Stop Loss order modification](/en/docs/mt4/terminal/positions/positions_control/positions_modify), a record will be made in the [terminal journal](/en/docs/mt4/terminal/overview/terminal/terminal_journal).

Trailing stop can be disabled by setting "None" in managing menu. And trailing stops of all open positions and pending orders will be disabled if the "Delete All" command of the same menu has been executed.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Trailing Stop works in the client terminal, not in the server (like Stop Loss or Take Profit). This is why it will not work, unlike the above orders, if the terminal is off. In this case, only the Stop Loss level will trigger that has been set by trailing stop.</span></li><li class="p_tableatten"><span class="f_tableatten">Trailing Stop is processed once per tick. If multiple orders with Trailing Stop are open for one symbol, only the trailing stop of the latest open order is processed.</span></li></ul></td></tr></tbody></table>

[Order Types](/en/docs/mt4/terminal/positions/orders)

[Types of Execution](/en/docs/mt4/terminal/positions/execution)