# Bulk Closing

> Source: https://support.metaquotes.net/en/docs/mt5/manager/bulk_closing

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
            -   [Bulk Closing](/en/docs/mt5/manager/bulk_closing)
            -   [Bulk Operations](/en/docs/mt5/manager/bulk_operations)
            -   [Bulk Payments by Positions](/en/docs/mt5/manager/bulk_payments)
            -   [Splitting Positions](/en/docs/mt5/manager/position_split)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)Bulk Closing

# Bulk Closing

The Manager terminal allows executing mass operations with trade positions for a selected symbol: close positions, delete orders and remove stop levels. To start performing bulk operations, click "![Bulk Closing](/en/docs/mt5/manager/img/bulk_closing_icon.png "Bulk Closing") Bulk Closing" in the context menu of the [Positions](/en/docs/mt5/manager/positions) or [Orders](/en/docs/mt5/manager/orders) section.

![Bulk closing](/en/docs/mt5/manager/img/bulk_closing.png "Bulk closing")

Specify the bulk operation settings:

-   Symbol — select a symbol to execute the bulk operations for.
-   Bid/Ask — Bid and Ask prices for closing positions (if the appropriate option is enabled). If you click the Update button, the current Bid and Ask prices are set here.
-   Groups — client group to execute the bulk operation for. If "\*", the operation is performed for all groups.
-   Comment — comment, which will be written to all orders and deals executed as a result of the operation.
-   Close positions — close positions for a selected symbol.
-   Delete orders — delete all pending orders for a selected symbol.
-   Clear Stop Loss and Take Profit — delete all [stop losses](/en/docs/mt5/manager/trade_principles#stop_loss) and [take profits](/en/docs/mt5/manager/trade_principles#take_profit) of the selected orders or positions. This function only sets these levels to zero, other parameters of the positions are not changed.

Depending on the type of bulk operations chosen, the lower part displays positions or pending orders for the selected symbol considering selected groups (or both positions and orders if both options are selected).

To close positions/delete orders, click Close in the lower part of the window.

The context menu of the preview of orders and positions allows configuring the list of trading operations: switch volume display mode (in lots or units) and profit (in money or points).

[Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)

[Bulk Operations](/en/docs/mt5/manager/bulk_operations)