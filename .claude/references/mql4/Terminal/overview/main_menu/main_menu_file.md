# File

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/main_menu/main_menu_file

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Main Menu](/en/docs/mt4/terminal/overview/main_menu)File

# File

Commands for working with charts, managing profiles, storing history data and charts are collected in this menu, as well as charts printing properties.

![file_menu](/en/docs/mt4/terminal/img/file_menu.png)

The following commands are available in the menu:

-   New Chart — open a new chart window for the symbol. At the command execution, the list of available symbols will appear. Having selected a symbol from the list, one can open a new chart.  
    The same actions can be performed by the ![New Chart](/en/docs/mt4/terminal/img/tb_standard_new_chart.png "New Chart") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).
-   Open Offline — open a symbol chart offline. By this command, one will be able to select a necessary file with its history data being stored. At that, the new quotes for this symbol will not be shown in the chart. Offline chart opening can be useful at [testing expert advisors](/en/docs/mt4/terminal/autotrading/tester).
-   Open Deleted — restore a deleted chart. The deleted charts will be restored if the "Save deleted charts to reopen" is enabled in the [terminal settings](/en/docs/mt4/terminal/setup/setup_charts). All deleted charts templates are stored in the /DELETED directory. At this command execution, these templates are called, and the corresponding chart will be opened.
-   Profiles — open sub-menu for managing profiles. Profiles can be stored or deleted from this sub-menu, as well as previously stored ones can be downloaded.  
    This profile managing sub-menu can also be called by the ![Call menu of profile management](/en/docs/mt4/terminal/img/tb_standard_profile.png "Call menu of profile management") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard).  
    More details can be found in the ["Profiles and Templates" section](/en/docs/mt4/terminal/chart_management/templates).
-   Close — close the current chart.
-   Save As — save history data as a text file in "CSV", "PRN", or "HTM" format.
-   Save As Picture... — save the chart in "BMP" or "GIF" format. Once you have pressed it, the window containing the alternatives of a terminal area to be saved appears: "Active workspace", "Active chart (as is)", and "Active chart" showing the specific size.  
    The same actions can be performed by the chart context menu command of the same name.

-   Open Data Folder — [open the folder](/en/docs/mt4/terminal/userguide/start_comm) there the client terminal stores its data: price history, configuration files, MQL4 programs, etc.

-   Open an Account — open a new demo account. Such accounts can be opened without placing of any money onto the deposit and allow to test the own trading system well.  
    To open an account, one can also execute the context menu command of the same name of the ["Navigator — Accounts" window](/en/docs/mt4/terminal/overview/navigator) or press the Insert button.
-   Login to Trade Account — [authorize](/en/docs/mt4/terminal/userguide/authorization). At this command execution, the terminal tries to connect to the server using the account selected. After successful authorization, quotes and news will start to income, and one can start trading.  
    It is possible to authorize having executed the "Login" command of the context menu of the ["Navigator — Accounts" window](/en/docs/mt4/terminal/overview/navigator) or double-click on the account name.

-   Login to MQL5.community — open the [settings](/en/docs/mt4/terminal/setup/settings_mql5community) of the trading platform to login to [MQL5.community](https://www.mql5.com/ "MQL5.community") and get additional services.

-   Print Setup... — general setup of printing parameters — printing device, page size and orientation, etc.
-   Print Preview — preview the chart before printing it. The settings of the selected printer are used at this. This command helps to preview before printing whether all desired data can be printed with the settings given.  
    The same actions can be performed having pressed the ![Chart Preview](/en/docs/mt4/terminal/img/tb_standard_print_prev.png "Chart Preview") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard) or having executed the chart context menu command of the same name.
-   Print... — print a chart. If the "Color Print" option is enabled in the [program settings](/en/docs/mt4/terminal/setup/setup_charts), the chart can be printed in color, not as a black-and-white one.  
    The same actions can be performed by pressing of the ![Chart Print](/en/docs/mt4/terminal/img/tb_standard_print.png "Chart Print") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard), accelerating buttons of Ctrl+P or by execution of the ["Print" chart context menu](/en/docs/mt4/terminal/chart_management/charts_control#context) command.
-   Exit — the terminal shutdown.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If the terminal is shut down, the <a href="/en/docs/mt4/terminal/autotrading/experts" class="topiclink">expert advisors</a> and <a href="/en/docs/mt4/terminal/positions/trailing" class="topiclink">Trailing Stops</a> will not be executed.</span></p></td></tr></tbody></table>

[Main Menu](/en/docs/mt4/terminal/overview/main_menu)

[View](/en/docs/mt4/terminal/overview/main_menu/main_menu_view)