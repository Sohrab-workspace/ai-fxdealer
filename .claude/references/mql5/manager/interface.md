# User Interface

> Source: https://support.metaquotes.net/en/docs/mt5/manager/interface

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)User Interface

# User Interface

The MetaTrader 5 Manager interface provides access to all the necessary tools for managers and dealers. It includes various menus, toolbars, and service windows. Almost all Manager terminal commands have [hot keys](/en/docs/mt5/manager/hotkeys) to accelerate the work.

![MetaTrader 5 Manager interface](/en/docs/mt5/manager/img/interface.png)

### Main menu

The [main menu](/en/docs/mt5/manager/main_menu) provides commands for managing the terminal and working in it: enabling/disabling a dealer, configuring the terminal view, switching between windows and various interface languages, etc.

### Toolbox

[Toolbox](/en/docs/mt5/manager/toolbar) allows you to conveniently arrange the work in the terminal. Add here the most frequently used commands to execute them in a single click. Also, the toolbox features the [search](/en/docs/mt5/manager/toolbar#search) along the entire Manager terminal.

### Market Watch

The [Market Watch](/en/docs/mt5/manager/market_watch) window allows viewing price data by trading symbols: quotes, price statistics and tick chart.

### Navigator

From the ["Navigator"](/en/docs/mt5/manager/navigator), you can easily switch between the Manager terminal sections: reports, accounts, dealing, as well as groups and plugins settings. Also, from the Navigator, you can go to the [technical support](/en/docs/mt5/manager/tech_support) section.

### Online Users

The list of [accounts currently connected to the trade server](/en/docs/mt5/manager/online_accounts).

### Accounts

The total list of [accounts](/en/docs/mt5/manager/accounts) available to the current manager.

### Positions

The list of all [open positions](/en/docs/mt5/manager/positions) of clients available to the current manager.

### Orders

The list of all [existing pending orders](/en/docs/mt5/manager/orders) of clients available to the current manager.

### Toolbox

This multi-purpose window allows viewing [summary positions](/en/docs/mt5/manager/summary_positions) and [client assets](/en/docs/mt5/manager/exposure) and provides access to [news](/en/docs/mt5/manager/toolbox#news), [emails](/en/docs/mt5/manager/toolbox#mail) and [economic calendar](/en/docs/mt5/manager/economic_calendar).

It also allows you to configure [notifications on market events](/en/docs/mt5/manager/trade_alerts), view the [search](/en/docs/mt5/manager/toolbar#search) results and [terminal journal](/en/docs/mt5/manager/toolbox#journal).

### Status bar

The [status bar](/en/docs/mt5/manager/orders) displays auxiliary data: command prompts, server connection status and dealer mode connections.

The manager terminal interface is highly customizable. You can choose to display only the tools that are currently needed. For example, you may hide [Market Watch](/en/docs/mt5/manager/market_watch) and [Depth of Market](/en/docs/mt5/manager/depth_of_market), and show [Margin Call](/en/docs/mt5/manager/margin_calls) and [Queue](/en/docs/mt5/manager/trade_queue) windows.

![MetaTrader 5 Manager interface](/en/docs/mt5/manager/img/interface2.png)

### Program header

Active account, server and manager names are specified here.

### Processing client requests

A dealer may reject a trade request or execute it partially or fully. A request can be requoted or executed at the changed price within the deviation the client agrees to.

### Client's trading status

When receiving a request, the dealer immediately sees the client account status: all open positions and pending orders, as well as the overall financial status.

### Orders and positions closest to the market

The dealer always has data on positions and orders that are close to the market price. Stop loss and take profit levels of positions are tracked, as is the order price of pending orders.

### Margin Call

A separate window displays a list of accounts located close to Margin Call and Stop Out states.

### Request queue

The list of trade requests waiting to be processed by the dealer is displayed in a separate window. Here you can also view the history of trade requests of clients whose request is currently being processed.

[Terminal Deinstallation](/en/docs/mt5/manager/beginning_advanced/deinstallation)

[Main Menu](/en/docs/mt5/manager/main_menu)