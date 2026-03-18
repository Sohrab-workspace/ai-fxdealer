# Market Watch Window

> Source: https://support.metaquotes.net/en/docs/mt4/manager/user_interface/ug_market_watch

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
        -   [Getting Started](/en/docs/mt4/manager/getting_started)
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
            -   [Overview](/en/docs/mt4/manager/user_interface/ug_overview)
            -   [Main Menu](/en/docs/mt4/manager/user_interface/ug_main_menu)
            -   [Toolbars](/en/docs/mt4/manager/user_interface/ug_toolbars)
            -   [Market Watch Window](/en/docs/mt4/manager/user_interface/ug_market_watch)
            -   [Plugins Window](/en/docs/mt4/manager/user_interface/ug_plugins)
        -   [Articles](/en/docs/mt4/manager/articles)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[User Interface](/en/docs/mt4/manager/user_interface)Market Watch Window

# Market Watch Window

The "Market Watch" window is a service window. This is a floating window, it can be moved in the screen to be presented in a usable appearance. "Market Watch" can be opened/closed using accelerating buttons Ctrl+M, the ["View — Market Watch"](/en/docs/mt4/manager/user_interface/ug_main_menu#view) menu command, or ![Opening the "Market Watch" window form the "Standard" toolbar](/en/docs/mt4/manager/img/ic_market_watch.png "Opening the "Market Watch" window form the "Standard" toolbar") button of the ["Standard"](/en/docs/mt4/manager/user_interface/ug_toolbars#standard) toolbar. The list of financial instruments will appear in the window for which the program receives quotations from the server. After the program has been installed, the list will consist of the initial set of instruments.

![Market Watch Window](/en/docs/mt4/manager/img/marketwatch.png "Market Watch Window")

The context menu of quotations allows to execute the following commands:

-   Details — open the [Financial Instruments Details Window](/en/docs/mt4/manager/user_interface/ug_market_watch#details);
-   Quotes — [input of quotations](/en/docs/mt4/manager/user_interface/ug_market_watch#quotes);
-   Profiles — work at [Financial Instrument Profiles](/en/docs/mt4/manager/user_interface/ug_market_watch#profiles);
-   Tick Chart — switch to the tab of tick prices;
-   Hide — delete a financial instrument from the quotation window;
-   Hide All — delete all instruments from the quotation window;
-   Show All — show all instruments in the quotation window;
-   Symbols — open the [Select Symbol Window](/en/docs/mt4/manager/user_interface/ug_market_watch#symbols);
-   Track Requests — track the trading requests of clients. At this, when dealer receives a new request, the quotation window will switch to tick price tab;
-   Auto Arrange — automatic arrangement of column sizes when changing the window size;
-   Spread — show/hide spread of the financial instrument;
-   High/Low — show/hide High/Low prices;
-   Time — show/hide time of incoming last quotation;
-   Grid — show/hide grid to separate columns.

The ["Tick Chart"](/en/docs/mt4/manager/user_interface/ug_market_watch#tick_chart) of the "Market Watch" window displays tick prices for a selected instrument.

## Symbols Selection [#](ug_market_watch#symbols)

![Symbols Window](/en/docs/mt4/manager/img/mw_symbols.png "Symbols Window")

The "Symbols" command of the context menu of quotation window calls the "Symbols" window containing the list of all instruments available. The symbols are grouped in the window according to their types: "Forex", "CFDs", "Futures", "Stocks", "Indexes". The "Show" command can be used to add the desired symbols, and the "Hide" can be used to delete the symbol from the quotation window.

## Window of Symbol Details [#](ug_market_watch#details)

![Details Window](/en/docs/mt4/manager/img/mw_details.png "Details Window")

The symbol window displays summarized information about the settings of the selected symbol. When having the rights, a manager can change the performance mode, the Limit & Stop level, spread, spread distribution, smoothing and the background color of the symbol.

## Input of Quotes [#](ug_market_watch#quotes)

![Quotes Window](/en/docs/mt4/manager/img/mw_quotes.png "Quotes Window")

Execution of the "Quotes" command of context menu of quotation window opens the "Quotes" window allowing to input a quotation into the quotation flow from data feeds. When "Track request" options is enabled and dealer receives a new request, the symbol from the request will be selected automatically in the "Quotes" window.

## Symbol Profiles [#](ug_market_watch#profiles)

The manager terminal allows to create and store several symbol profiles having different settings to be used for different market situations. The "Save As..." command of the "Profiles" submenu allows to store the current settings of symbols selected in the quotes window as a profile having a certain name. For each symbol, the performance mode, the Limit & Stop level, spread, spread difference, smoothing and symbol background color are kept.

![Profiles Window](/en/docs/mt4/manager/img/mw_profile.png "Profiles Window")

The "Remove" submenu removes a previously created profile of symbols. The symbol settings themselves are not changed at this.

If market conditions change, the selection of a profile from "Profiles" submenu allows to setup symbols properties promptly according to the parameters stored in the profile.

## Tick Chart [#](ug_market_watch#tick_chart)

In the "Tick Chart" tab of the "Market Watch" window, the tick chart of the symbol is displayed. Ticks for all selected symbols are saved in the Manager terminal in files "history\\ticks\\\[symbol\]\\ticks.raw" of the directory where the terminal is placed. Once a week, the collected ticks are filed under the name in form of YYYYMMDD.ticks where YYYY - year, MM - month, DD - day of the week, the ticks of which are saved in the file.

![Tick Chart](/en/docs/mt4/manager/img/mw_ticks.png "Tick Chart")

The tick chart context menu allows the following commands to be executed:

-   Current — show the current tick chart;
-   Open — open the saved tick chart for the preceding weeks;
-   Save — save tick prices of the chart as a text file, for example, to analyze them in dispute resolutions;
-   Dealing — show dealer's answers on the tick chart;
-   Auto Scroll — enable/disable auto scrolling of the tick chart;
-   Crosshair — display the cursor as a crosshair;
-   Ask Line — show/hide ask price line;
-   Grid — show/hide grid.

Dragging the mouse in the area of the chart time scale, as well as pressing "+"/"-", allow to edit the chart scale.

If the auto scroll is disabled, the chart can be scrolled by dragging the mouse within the chart area or by pressing "Home", "End", "PgUp", "PgDown", or arrow keys.

If the Dealing option is enabled, the dealer's answers to trade requests are displayed in the tick chart as blue sections when executing requests at ask price or red sections when execution requests at bid price. If the cursor is displayed as a crosshair, the request descriptions are displayed near the cursor, too. In the tick chart, only dealer's confirmations of requests for opening or closing positions, requotes, and pending orders activation are shown. Rejected requests, Close-by requests, requests for placing pending orders and for order modifying are not displayed in the tick chart.

[Toolbars](/en/docs/mt4/manager/user_interface/ug_toolbars)

[Plugins Window](/en/docs/mt4/manager/user_interface/ug_plugins)