# Journal

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/terminal/terminal_journal

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
                -   [Trade](/en/docs/mt4/terminal/overview/terminal/terminal_trade)
                -   [Exposure](/en/docs/mt4/terminal/overview/terminal/toolbox_exposure)
                -   [Account History](/en/docs/mt4/terminal/overview/terminal/terminal_account_history)
                -   [News](/en/docs/mt4/terminal/overview/terminal/terminal_news)
                -   [Alerts](/en/docs/mt4/terminal/overview/terminal/terminal_alerts)
                -   [Mailbox](/en/docs/mt4/terminal/overview/terminal/terminal_mailbox)
                -   [Company](/en/docs/mt4/terminal/overview/terminal/toolbox_company)
                -   [Market](/en/docs/mt4/terminal/overview/terminal/toolbox_market)
                -   [Signals](/en/docs/mt4/terminal/overview/terminal/toolbox_signals)
                -   [Code Base](/en/docs/mt4/terminal/overview/terminal/toolbox_codebase)
                -   [Search](/en/docs/mt4/terminal/overview/terminal/toolbox_search)
                -   [Experts](/en/docs/mt4/terminal/overview/terminal/terminal_experts)
                -   [Journal](/en/docs/mt4/terminal/overview/terminal/terminal_journal)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Client terminal](/en/docs/mt4/terminal/overview/terminal)Journal

# Journal

The "Journal" tab contains information about the stated actions of the trader and the client terminal within the current session.

![terminal_window_journal](/en/docs/mt4/terminal/img/terminal_window_journal.png)

Journal entries are represented in the form of a table with the following fields:

-   Time — date and time of an event;
-   Message — description of an event.

Events are also divided into the following types and consequently can be marked with different icons:

-   ![Information](/en/docs/mt4/terminal/img/journal_info_icon.png "Information") — informational message;
-   ![Warning](/en/docs/mt4/terminal/img/journal_warning_icon.png "Warning") — warning;
-   ![Error](/en/docs/mt4/terminal/img/journal_error_icon.png "Error") — error message.

The context menu of this tab contains the following commands:

-   ![Open](/en/docs/mt4/terminal/img/journal_open_icon.png "Open") Open — open the folder that contains the journal log files. Also at execution of this command the current journal entries are flushed to the log files. These files are stored in the /LOGS directory of the client terminal. File names correspond to dates of log generation — YYYYMMDD.LOG. There one can view previous entries on the terminal operation. The "Journal" tab contains only latest entries;
-   ![Copy](/en/docs/mt4/terminal/img/journal_copy_icon.png "Copy") Copy — copy a line with the information to clipboard for using it in other applications;
-   ![Viewer](/en/docs/mt4/terminal/img/journal_view_icon.png "Viewer") Viewer — open the window of a specialized program for viewing log files;

-   Clear — clear the tab deleting all current journal entries. In this case the entries aren't deleted physically, they can be viewed in log files;
-   Auto Scroll — if this option is enabled, then every time a new entry appears in the journal, the list of entries will be scrolled to the last one.

-   Auto Arrange — when this option is enabled, the size of table columns will be selected automatically in case he window size is changed;
-   Grid — show hide grid to separate table fields.

## Viewing Logs [#](terminal_journal#viewer)

The client terminal includes a special program for viewing log files. The program can be viewed by selecting the "Viewer" command of the context menu in "Journal" and ["Experts"](/en/docs/mt4/terminal/overview/terminal/terminal_experts) tabs.

![Journal viewer](/en/docs/mt4/terminal/img/journal_viewer.png "Journal viewer")

The upper part of the window contains a search line (search is performed by exact words, the search is case sensitive) and the filter of entries (Full, Errors only). Here time limits for search can also be set. After all necessary search data are specified, the "Request" button should be pressed.

The context menu of the viewer contains the same commands as that of the "Journal" tab.

[Experts](/en/docs/mt4/terminal/overview/terminal/terminal_experts)

[Tester](/en/docs/mt4/terminal/overview/strategy_tester)