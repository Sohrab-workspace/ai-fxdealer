# Bulk Operations

> Source: https://support.metaquotes.net/en/docs/mt5/android/trade/bulk_operations

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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Trade](/en/docs/mt5/android/trade)Bulk Operations

# Bulk Operations

The mobile platform allows the execution of bulk operations with positions and orders. For example, you can close all open positions with a couple of clicks following an important news release in order to promptly take the profits. You can also quickly cancel all pending orders to prevent them from being triggered all at once by a sharp price spike.

Bulk operations are executed without additional user confirmations; therefore, [one-click trading](/en/docs/mt5/android/settings#one_click) should be allowed in the application settings in order to enable such operations.

## Bulk position closing

To open the bulk operations menu, tap ![Bulk Operations](/en/docs/mt5/android/img/bulk_menu.png "Bulk Operations") in the [Trade\\Positions](/en/docs/mt5/android/trade) section or select "Bulk operations" in the context menu of any position in the list:

![Bulk position closing](/en/docs/mt5/android/img/bulk_positions.png "Bulk position closing")

The list of available commands is formed automatically, depending on the selected operation and on your account type.

The following commands are always available in the menu:

-   Close all positions on hedging accounts, the system tries to [close positions by opposite ones (Close By)](/en/docs/mt5/android/trade/closeby), and then it closes the remaining positions following a regular procedure.
-   Close all profitable or all losing positions.

If you select a position, additional commands appear in the menu:

-   Close all positions for the symbol.
-   Close all positions in the same direction (on hedging accounts).
-   Close opposite positions for the same symbol (on hedging accounts). If there is no opposite operation to close the position, it will remain open.
-   Position reversal (on netting accounts). For example, if you run this command for a EURUSD buy position with a volume of two lots, you will obtain a EURUSD sell position with the same volume of two lots. In this case, a deal of four lots will be executed on your account: two lots to close the current positions and two lots to open an opposite position.

Closing procedure and restrictions:

-   For hedging accounts, the system first attempts to close positions using opposite orders. Any remaining positions are then closed using the standard procedure.

-   Positions are closed in parallel (with the exception of accounts operating under FIFO rules). If an error occurs when closing the next pair, the application may make up to two additional attempts, depending on the [type of error](/en/docs/mt5/android/trade/bulk_operations#error_type). If all attempts fail, the process will be interrupted, but any remaining positions will still be closed.
-   For accounts operating under [FIFO](https://www.metatrader5.com/en/terminal/help/trading/performing_deals#fifo) rules, positions are closed sequentially. If an error occurs while closing a position, the application may make up to two additional attempts. If all attempts fail, the process will be interrupted and any remaining positions will not be closed.
-   While closing opposite positions, the platform also closes remaining open positions. This process is performed asynchronously: the platform sends requests to close each position to the broker's trading server as quickly as possible, without waiting for confirmation of the previous closures.
-   If the server returns an error in response to a closure request, the application may make up to two additional attempts to close the position. If all attempts fail, the position will remain open, and the application will proceed with sending closure requests for the remaining positions.
-   If the application is minimized, closed, or the user navigates away from the screen, the bulk closure process will be immediately terminated. Any positions that were not closed by the application will remain open.

Depending on the type of error received during the position closure, the application may attempt to close it up to two more times:

-   If the error "No prices" is returned, or in the case of a requote when quotes for the instrument are [delayed](/en/docs/mt5/android/quotes#delay), the application will not attempt to close the position again.
-   If the error is "A close order already exists for a specified position", "Invalid volume", "Request rejected", or "Only part of the request was completed", the application will make two additional attempts to close the position.

## Bulk deletion of pending orders [#](bulk_operations#bulk_orders)

To open the bulk operations menu, tap ![Bulk Operations](/en/docs/mt5/android/img/bulk_menu.png "Bulk Operations") in the "[Trade\\Orders](/en/docs/mt5/android/trade)" section or select "Bulk operations" in the context menu of any order in the list:

![Bulk deletion of pending orders](/en/docs/mt5/android/img/bulk_orders.png "Bulk deletion of pending orders")

The list of available commands is formed automatically, depending on the selected operation and on your account type.

The following commands are always available in the menu:

-   Delete all pending orders.
-   Delete pending orders of certain types: Limit, Stop, Stop Limit

If you select a pending order, additional commands appear in the menu:

-   Delete all pending orders for the same symbol.
-   Delete all pending orders of the same type for the same symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The bulk order deletion function may not execute fully in certain cases. For example, if you minimize or close the application after sending the command, or if the connection to the server is lost, some orders may remain undeleted.</span></p></td></tr></tbody></table>

[Managing Pending Orders](/en/docs/mt5/android/trade/pending_change)

[History](/en/docs/mt5/android/history)