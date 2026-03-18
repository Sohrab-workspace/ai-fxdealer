# Trading Notifications (Alerts)

> Source: https://support.metaquotes.net/en/docs/mt5/manager/trade_alerts

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
            -   [Basic Principles](/en/docs/mt5/manager/trade_principles)
            -   [Market Watch](/en/docs/mt5/manager/market_watch)
            -   [Market Depth](/en/docs/mt5/manager/depth_of_market)
            -   [Economic Calendar](/en/docs/mt5/manager/economic_calendar)
            -   [Trading Notifications](/en/docs/mt5/manager/trade_alerts)
            -   [Working with Trading Positions](/en/docs/mt5/manager/positions)
            -   [Working with Trading Orders](/en/docs/mt5/manager/orders)
            -   [Viewing and Editing Trading Operations](/en/docs/mt5/manager/edit_trades)
            -   [For Advanced Users](/en/docs/mt5/manager/trading_advanced)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Trading Operations](/en/docs/mt5/manager/trading)Trading Notifications

# Trading Notifications (Alerts)

Alerts notify a manager of various market events. Having created alerts, one may leave the monitor as the terminal will automatically inform about the server event.

Alerts are configured on the Alerts tab of the Toolbox window. An alert can be created via the context menu or by pressing Insert.

![Trading notifications - Alerts](/en/docs/mt5/manager/img/toolbox_alerts.png)

The data of this financial instrument are used to check the alert conditions. If the Time parameter is selected as a condition, the symbol has no value.

Alert trigger condition.

Action performed when the event occurs:

-   Sound — play an audio file.
-   File — launch an executable file.

Price, volume or time an alert is triggered at.

Depending on a type of an action executed when an event occurs, this may be:

-   An audio file of \*.wav, \*.mp3 or \*.wma format.
-   An executable file of \*.exe, \*.vbs or \*.bat format.

Time between alert repetitions.

Maximum allowed number of alert repetitions.

Enable/disable a selected alert. If disabled, the alert is not removed but stops working.

Number of current signal triggers.

Notifications can be configured for the following event types (specified in the Condition field):

-   Bid < — Bid price is less than the specified value.
-   Bid > — Bid price is greater than the specified value.
-   Ask < — Ask price is less than the specified value.
-   Ask > — Ask price is greater than the specified value.
-   Last < — Last price is less than the specified value.
-   Last > — Last price is greater than the specified value.
-   Volume < — Last deal volume for the symbol is less than the specified value.
-   Volume > — Last deal volume for the symbol is greater than the specified value.
-   Time = — certain time arrival. Specify here the local time of the computer in the HH:MM format, for example: 15:00.
-   Positions > — number of client positions exceeds the set value.
-   Positions < — number of client positions is less than the set value.
-   Net Volume > — net volume is more than the set value. Net volume — difference between the volumes of clients' buy and sell positions, at that the corresponding volume on the coverage account is subtracted from the buy or sell position.
-   Net Volume < — net volume is less than the set value. Net volume — difference between the volumes of clients' buy and sell positions, at that the corresponding volume on the coverage account is subtracted from the buy or sell position.
-   Profit > — total profit (loss) at clients' positions is more than the set value.
-   Profit < — total profit (loss) at clients' positions is less than the set value.
-   Uncovered > — difference between the total profit (loss) from the clients' positions and the corresponding position on the coverage account is more than the set value.
-   Uncovered < — difference between the total profit (loss) from the clients' positions and the corresponding position on the coverage account is less than the set value.

The Test button allows to test the selected alert. To apply the changes, click OK.

[Economic Calendar](/en/docs/mt5/manager/economic_calendar)

[Working with Trading Positions](/en/docs/mt5/manager/positions)