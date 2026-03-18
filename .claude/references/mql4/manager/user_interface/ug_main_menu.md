# Main Menu

> Source: https://support.metaquotes.net/en/docs/mt4/manager/user_interface/ug_main_menu

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[User Interface](/en/docs/mt4/manager/user_interface)Main Menu

# Main Menu

The main menu of the program represents a set of menus at lower levels located below main window heading. The basic commands and functions to be executed in the program are collected in the main menu.

## "File" Menu [#](ug_main_menu#file)

-   ![Connect to the server](/en/docs/mt4/manager/img/ic_server_login.png "Connect to the server") Connect... — authorization. While this command is executed, an attempt to connect to the selected server will be undertaken. If the access with the given account is not permitted on the server, no connection will succeed.
-   ![Disconnect from server](/en/docs/mt4/manager/img/ic_server_disconnect.png "Disconnect from server") Disconnect — disconnection from the server. Before finishing work at Manager, it is recommended to disconnect of the server.
-   ![Connect Dealer](/en/docs/mt4/manager/img/ic_dealer_connect.png "Connect Dealer") Connect Dealer — connection of a dealer.
-   ![Disconnect Dealer](/en/docs/mt4/manager/img/ic_dealer_disconnect.png "Disconnect Dealer") Disconnect Dealer — disconnection of a dealer.
-   ![Connect Coverage](/en/docs/mt4/manager/img/ic_connect_coverage.png "Connect Coverage") Connect Coverage — connect hedging account.
-   ![Disconnect Coverage](/en/docs/mt4/manager/img/ic_disconnect_coverage.png "Disconnect Coverage") Disconnect Coverage — disconnect hedging account.
-   ![New Account](/en/docs/mt4/manager/img/ic_new_account.png "New Account") New Account... — add a new account. On this command, a window appears requesting information about the account to be added.
-   ![Save As](/en/docs/mt4/manager/img/ic_save_as.png "Save As") Save As — save data as a text file having "HTM" extension.
-   ![Print](/en/docs/mt4/manager/img/ic_print.png "Print") Print... — print.
-   ![Print Preview](/en/docs/mt4/manager/img/ic_print_preview.png "Print Preview") Print Preview — preview before printing.
-   Print Setup... — common print setup.
-   ![Open Data Folder](/en/docs/mt4/manager/img/open_data_folder_icon.png "Open Data Folder") Open Data Folder — open the data directory of the manager terminal. This is a convenient command for operation under MS Windows Vista and above, where programs by default store data in the Windows user directory, and not in the installation directory. The data storage directory has the following path: C:\\Users\\\[username\]\\AppData\\Roaming\\MetaQuotes\\MetaTrader 4 Manager\\\[terminal instance id\]\\.
-   Exit — close the program.

## "Edit" Menu [#](ug_main_menu#edit)

-   ![Copy](/en/docs/mt4/manager/img/ic_copy.png "Copy") Copy — copy data into clipboard.
-   ![Find](/en/docs/mt4/manager/img/ic_find.png "Find") Find — finding a list element according to the given criterion.
-   ![Find Next](/en/docs/mt4/manager/img/ic_find_next.png "Find Next") Find Next... — continue the search and find the next list element.

## "View" Menu [#](ug_main_menu#view)

-   Languages — call the submenu for management the languages of the client terminal. The changes are valid after the program has been restarted.
-   Toolbars — call the menu of management the toolbars. The toolbars already set are ticked off. The "Customize" command allows to adjust toolbars.
-   Status Bar — enable/disable the status bar located at the bottom of the terminal window.
-   ![Market Watch](/en/docs/mt4/manager/img/ic_market_watch.png "Market Watch") Market Watch — open/close the ["Market Watch" window](/en/docs/mt4/manager/user_interface/ug_market_watch). The same action can be performed using the accelerating buttons Ctrl+M or ![Market Watch](/en/docs/mt4/manager/img/ic_market_watch.png "Market Watch") button of ["Standard"](/en/docs/mt4/manager/user_interface/ug_toolbars#standard) toolbar.
-   ![Margin Calls](/en/docs/mt4/manager/img/ic_margin_call.png "Margin Calls") Margin Calls — open/close ["Margin Calls"](/en/docs/mt4/manager/request_processing/ug_win_queue#margin_call) window. The same action can be performed using accelerating buttons Ctrl+L.
-   ![Queue](/en/docs/mt4/manager/img/ic_queue.png "Queue") Queue — open/close ["Queue"](/en/docs/mt4/manager/request_processing/ug_win_queue) window. The same action can be performed using accelerating buttons Ctrl+Q.
-   ![Plugins](/en/docs/mt4/manager/img/ic_plugins.png "Plugins") Plugins — open/close [Plugins](/en/docs/mt4/manager/user_interface/ug_plugins) window. The same action can be performed using accelerating buttons Ctrl+U.
-   ![Toolbox](/en/docs/mt4/manager/img/ic_toolbox.png "Toolbox") Toolbox — open/close "Toolbox" window. The same action can be performed using accelerating buttons Ctrl+T or the ![Terminal](/en/docs/mt4/manager/img/ic_toolbox.png "Terminal") button of the "Standard" toolbar.
-   ![Full Screen](/en/docs/mt4/manager/img/ic_fullscreen.png "Full Screen") Full Screen — enable/disable full-screen mode. When this option is enabled, toolbars and status bar are disabled, and all service windows are closed. At the next execution of the command the return to the initial status occurs. The same action can be performed using F11 button or ![Full Screen](/en/docs/mt4/manager/img/ic_fullscreen.png "Full Screen") button of ["Standard"](/en/docs/mt4/manager/user_interface/ug_toolbars#standard) toolbar.

## "Tools" Menu [#](ug_main_menu#tools)

-   ![New Coverage Order](/en/docs/mt4/manager/img/ic_coverage_order.png "New Coverage Order") New Coverage Order — open new hedging order.
-   ![Options](/en/docs/mt4/manager/img/ic_options.png "Options") Options... — open setup window for program properties.

## "Window" Menu [#](ug_main_menu#window)

-   ![Online Users](/en/docs/mt4/manager/img/ic_online_users.png "Online Users") Online users — switch the active window to "Online" tab.
-   ![Accounts](/en/docs/mt4/manager/img/ic_accounts.png "Accounts") Accounts — switch the active window to "Accounts" tab.
-   ![Orders](/en/docs/mt4/manager/img/ic_orders.png "Orders") Orders — switch the active window to "Orders" tab.
-   ![Dealer](/en/docs/mt4/manager/img/ic_dealer.png "Dealer") Dealer — switch the active window to "Dealer".
-   ![Reports](/en/docs/mt4/manager/img/ic_reports.png "Reports") Reports — switch the active window to "Reports" tab.
-   ![History Reports](/en/docs/mt4/manager/img/ic_history_reports.png "History Reports") History reports — switch the active window to "History reports" tab.
-   ![Journal](/en/docs/mt4/manager/img/ic_journal.png "Journal") Journal — switch the active window to "Journal" tab.

## "Help" Menu [#](ug_main_menu#help)

-   Contents — open the built-in directory containing the Userguide. F1 button performs the same action.
-   MetaQuotes Web Site — open homepage.
-   MetaQuotes Support Center — open page of MetaQuotes Software Corp. technical support.
-   ![About](/en/docs/mt4/manager/img/ic_about.png "About") About MetaTrader Manager... — about the program.

[Overview](/en/docs/mt4/manager/user_interface/ug_overview)

[Toolbars](/en/docs/mt4/manager/user_interface/ug_toolbars)