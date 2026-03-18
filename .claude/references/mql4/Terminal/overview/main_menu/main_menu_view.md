# View

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/main_menu/main_menu_view

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
            -   [Main Menu](/en/docs/mt4/terminal/overview/main_menu)
                -   [File](/en/docs/mt4/terminal/overview/main_menu/main_menu_file)
                -   [View](/en/docs/mt4/terminal/overview/main_menu/main_menu_view)
                -   [Insert](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert)
                -   [Charts](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts)
                -   [Tools](/en/docs/mt4/terminal/overview/main_menu/main_menu_tools)
                -   [Window](/en/docs/mt4/terminal/overview/main_menu/main_menu_window)
                -   [Help](/en/docs/mt4/terminal/overview/main_menu/main_menu_help)
            -   [Toolbars](/en/docs/mt4/terminal/overview/toolbars)
            -   [Market Watch](/en/docs/mt4/terminal/overview/market_watch)
            -   [Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)
            -   [Data Window](/en/docs/mt4/terminal/overview/data_window)
            -   [Navigator](/en/docs/mt4/terminal/overview/navigator)
            -   [Chart Switching Bar](/en/docs/mt4/terminal/overview/charts_bar)
            -   [Client terminal](/en/docs/mt4/terminal/overview/terminal)
            -   [Tester](/en/docs/mt4/terminal/overview/strategy_tester)
            -   [Search](/en/docs/mt4/terminal/overview/search)
            -   [Fast Navigation](/en/docs/mt4/terminal/overview/fast_nav)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Main Menu](/en/docs/mt4/terminal/overview/main_menu)View

# View

Commands managing signal windows, toolbars, and the program interface language, are grouped in this window.

![view_menu](/en/docs/mt4/terminal/img/view_menu.png)

Some of these commands are duplicated in the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard). The following commands are available in the menu:

-   Languages — call the sub-menu managing languages of the Client Terminal. Having selected a desired language, one can switch the terminal interface to this language. For the changes to take effect, the program must be restarted;
-   Toolbars — call the sub-menu managing [toolbars](/en/docs/mt4/terminal/overview/toolbars). Active toolbars are checked. Selection of a toolbar allows to enable or disable it.  
    The "Customize..." command allows to assign any buttons for any toolbars. At that, a new window containing the list of toolbar elements available. The "Insert" and "Remove" buttons allow to add or remove an element from the toolbar. The "Up" and "Down" buttons are intended for defining the location of a button in the toolbar. To reset the toolbar to appear as initially, one has to press the "Reset" button.
-   Status Bar — enable/disable status bar located in the lower part of the terminal window. This data bar contains (from left to right): menu managing [profiles](/en/docs/mt4/terminal/chart_management/templates), time and prices of the bar selected, and indicator of server connection and amounts of incoming/outgoing traffic. Having pressed on the current profile name, one can open the menu managing [profiles](/en/docs/mt4/terminal/chart_management/templates). One can store or remove profiles in this menu, as well as download those previously stored.  
    The sub-menu for managing profiles can also be called by the ["File — Profiles" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command.
-   Charts Bar — enable/disable the chart window names (tabs) bar located in the lower part of the workspace. Using this bar, one can switch among open charts fast.
-   Market Watch — open/close the ["Market Watch" signal window](/en/docs/mt4/terminal/overview/market_watch) where the current quotes are published.  
    The same action can be performed by accelerating buttons of Ctrl+M or by pressing the ![Market Watch](/en/docs/mt4/terminal/img/tb_standard_market_watch.png "Market Watch") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).
-   Data Window — open/close the ["Data Window"](/en/docs/mt4/terminal/overview/data_window). Prices of the bar selected and information about indicators imposed are published in this window.  
    The same action can be performed with accelerating buttons of Ctrl+D or by the ![Data Window](/en/docs/mt4/terminal/img/tb_standard_data_window.png "Data Window") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).
-   Navigator — open/close the ["Navigator" window](/en/docs/mt4/terminal/overview/navigator). Lists of open accounts, technical indicators, experts, custom indicators and scripts are located in the form of tree in this window.  
    The same action can be performed with accelerating buttons of Ctrl+N or by the ![Navigator](/en/docs/mt4/terminal/img/tb_standard_navigator.png "Navigator") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).
-   Terminal — open/close the ["Terminal" window](/en/docs/mt4/terminal/overview/terminal). One can manage orders and signals in this window, look through the account history, news, emails, journal of events and that of expert advisors.  
    The same action can be performed with accelerating buttons of Ctrl+T or by the ![Terminal](/en/docs/mt4/terminal/img/tb_standard_terminal.png "Terminal") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).
-   Strategy Tester — open/close the ["Tester" window](/en/docs/mt4/terminal/autotrading/tester). This window is intended for testing and optimization of expert advisors.  
    The same action can be performed with acceleration keys of Ctrl+R or the ![Strategy Tester](/en/docs/mt4/terminal/img/tb_standard_strategy_tester.png "Strategy Tester") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).
-   Full Screen — enable/disable the full screen mode. As soon as this option is enabled, toolbars and status bar will be disabled and all signal windows will be closed. The client terminal heading, main menu, workspace (charts) and the charts windows tabs remain in the screen. The repeated execution of the command returns the terminal to the initial appearance.  
    The same action can be performed with F11 button or by the ![Full Screen](/en/docs/mt4/terminal/img/tb_standard_full_screen.png "Full Screen") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).

[File](/en/docs/mt4/terminal/overview/main_menu/main_menu_file)

[Insert](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert)