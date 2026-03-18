# Journal

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_journal

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
            -   [Toolbars](/en/docs/mt4/terminal/overview/toolbars)
            -   [Market Watch](/en/docs/mt4/terminal/overview/market_watch)
            -   [Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)
            -   [Data Window](/en/docs/mt4/terminal/overview/data_window)
            -   [Navigator](/en/docs/mt4/terminal/overview/navigator)
            -   [Chart Switching Bar](/en/docs/mt4/terminal/overview/charts_bar)
            -   [Client terminal](/en/docs/mt4/terminal/overview/terminal)
            -   [Tester](/en/docs/mt4/terminal/overview/strategy_tester)
                -   [Setup](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup)
                -   [Properties](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_properties)
                -   [Results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_results)
                -   [Graph](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_charts)
                -   [Report](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_report)
                -   [Journal](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_journal)
                -   [Optimization Results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_results)
                -   [Optimization Graph](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_charts)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Tester](/en/docs/mt4/terminal/overview/strategy_tester)Journal

# Journal

Messages about the expert testing process, including all trade operations, are published in the "Journal" tab automatically.

This journal is rather similar to [that of the "Terminal — Expert Advisors" window](/en/docs/mt4/terminal/overview/terminal/terminal_experts), except for that messages informing about expert testing, but not its working at the market , are published in this Tester Journal. After the expert has been tested, these data will be output in the separate /TESTER/LOGS directory. The tester journal files are stored in the /EXPERTS/LOGS directory, filenames being correspondent with the date of logs — YYYYMMDD.LOG.

![strategy_tester_journal](/en/docs/mt4/terminal/img/strategy_tester_journal.png)

Journal entries are represented as a table with the following fields:

-   Time — date and time of an event;
-   Message — description of the event.

Events are divided into several types, which are marked by special icons:

-   ![Information](/en/docs/mt4/terminal/img/journal_info_icon.png "Information") — information;
-   ![Warning](/en/docs/mt4/terminal/img/journal_warning_icon.png "Warning") — warning;
-   ![Error](/en/docs/mt4/terminal/img/journal_error_icon.png "Error") — error message.

The following commands can be execute from the context menu of this tab:

-   ![Open](/en/docs/mt4/terminal/img/journal_open_icon.png "Open") Open — open the folder with the log files of the journal. Besides that, when this command is executed, all current journal records are saved to log files. These files are stored in the /TESTER/LOGS directory of the client terminal. File names correspond to the date when the journal was formed — YYYYMMDD.LOG. thus you can view previous records of the terminal operation. Only latest entries are displayed on the "Journal" tab;
-   ![Copy](/en/docs/mt4/terminal/img/journal_copy_icon.png "Copy") Copy — Copy the line with the information to clipboard for further using it in other applications;
-   Clear All Journals Logs — delete all the log files of the strategy tester (/TESTER/LOGS). The Journal tab is cleared and all the log files are deleted from the specified folders when this commands is executed.
-   ![Viewer](/en/docs/mt4/terminal/img/journal_view_icon.png "Viewer") Viewer — Open the window of the special program for [viewing log files](/en/docs/mt4/terminal/overview/terminal/terminal_journal#viewer);
-   Auto Scroll — if this option is enabled, the list of entries will be automatically scrolled to the latest entry as a new message appears in the journal.
-   Auto Arrange — if this option is enabled, size of the table columns will be selected automatically when the window size is changed;
-   Grid — show/hide grid to separate fields.

More details can be found in the sections of ["testing Expert Advisors"](/en/docs/mt4/terminal/autotrading/tester) and ["Optimization"](/en/docs/mt4/terminal/autotrading/tester_optimization).

[Report](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_report)

[Optimization Results](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_opt_results)