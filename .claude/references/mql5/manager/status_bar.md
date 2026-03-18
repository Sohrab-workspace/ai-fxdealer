# Status Bar

> Source: https://support.metaquotes.net/en/docs/mt5/manager/status_bar

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
            -   [Main Menu](/en/docs/mt5/manager/main_menu)
            -   [Toolbar](/en/docs/mt5/manager/toolbar)
            -   [Toolbox](/en/docs/mt5/manager/toolbox)
            -   [Navigator](/en/docs/mt5/manager/navigator)
            -   [Status Bar](/en/docs/mt5/manager/status_bar)
            -   [Hot Keys](/en/docs/mt5/manager/hotkeys)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[User Interface](/en/docs/mt5/manager/interface)Status Bar

# Status Bar

A status bar is located at the bottom of the manager terminal window. It contains hints of the program commands, status of connection to the server and the amount of sent and received data:

![Status bar](/en/docs/mt5/manager/img/status_bar.png "Status bar")

From left to right the following information is shown in the bar:

-   Command tips.
-   Connection status of the [dealer](/en/docs/mt5/manager/dealing). Icon ![Dealer connected](/en/docs/mt5/manager/img/status_bar_dealer_connected.png "Dealer connected") means that the dealer is currently connected and can process trade requests. If a dealer is disabled, icon ![Dealer not connected](/en/docs/mt5/manager/img/status_bar_dealer_disconnected.png "Dealer not connected") is displayed.
-   Status of connection to a trade server. Icon ![Connected](/en/docs/mt5/manager/img/status_bar_connected.png "Connected") means that the terminal is currently connected to the server. If connection to the terminal is not established, icon ![Not connected](/en/docs/mt5/manager/img/status_bar_disconnected.png "Not connected") is displayed. Hover over the icon to view additional connection details: ping to the trade server and packet loss. These variables measure connection quality between the terminal and the server.
-   Amount of incoming and outgoing traffic for the current session.

The status bar can be disabled by removing the check mark at the corresponding item of the [View](/en/docs/mt5/manager/main_menu#view) menu.

## Menu of switching between access points [#](status_bar#access_servers)

The Manager terminal is connected to the trade server through special access servers that are part of the trading platform. When connecting, the best access point is chosen (the least server load and the best quality of connection). The automatic checking of best access point is performed every three hours of working.

You can also switch between access servers using the menu that is opened by clicking on the connection status or traffic data in the status bar:

![Menu of switching between access points](/en/docs/mt5/manager/img/status_bar_menu.png "Menu of switching between access points")

The menu contains the following commands

-   ![Connect](/en/docs/mt5/manager/img/connect_icon.png "Connect") Connect/![Disconnect](/en/docs/mt5/manager/img/disconnect_icon.png "Disconnect") Disconnect — [connect](/en/docs/mt5/manager/connect) or disconnect from the server.
-   ![Network Rescan](/en/docs/mt5/manager/img/network_rescan_icon.png "Network Rescan") Network Rescan — manually start scanning of access points. If a server with connection quality better than the current one by 30% is found, it is automatically switched to it.
-   List of access servers — all available access servers are displayed below. The indicator of the server quality is shown before the name of each access server. To switch to one of the access points, click its name. During the next scanning of the network, the best server is automatically chosen.

[Navigator](/en/docs/mt5/manager/navigator)

[Hot Keys](/en/docs/mt5/manager/hotkeys)