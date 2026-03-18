# Chart Opening

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/chart_management/charts_open

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
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
            -   [Chart Opening](/en/docs/mt4/terminal/chart_management/charts_open)
            -   [Setup](/en/docs/mt4/terminal/chart_management/charts_setup)
            -   [Chart Management](/en/docs/mt4/terminal/chart_management/charts_control)
            -   [Publishing Charts Online](/en/docs/mt4/terminal/chart_management/mql5_charts)
            -   [Quick Trading](/en/docs/mt4/terminal/chart_management/chart_trading)
            -   [Charts Print](/en/docs/mt4/terminal/chart_management/charts_print)
            -   [Deleted Charts](/en/docs/mt4/terminal/chart_management/charts_deleted)
            -   [Templates and Profiles](/en/docs/mt4/terminal/chart_management/templates)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Working with Charts](/en/docs/mt4/terminal/chart_management)Chart Opening

# Chart Opening

A chart shows the price changes for a security with the time. Charts are necessary for performing [technical analysis](/en/docs/mt4/terminal/analytics), [working of expert advisors](/en/docs/mt4/terminal/autotrading/experts) and [testing](/en/docs/mt4/terminal/autotrading/tester) thereof. Up to ninety-nine charts can be opened in the terminal at the same time.

![charts](/en/docs/mt4/terminal/img/charts.png)

A new chart can be opened by executing of the ["File — New Chart" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file), ["Window — New Window" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_window) command, or by pressing of the ![New Chart](/en/docs/mt4/terminal/img/tb_standard_new_chart.png "New Chart") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard). The list of securities available will appear at performing any of the above actions. Having selected the necessary symbol from this list, one can open its chart. New charts can also be opened from the ["Market Watch" window](/en/docs/mt4/terminal/overview/market_watch), holding Ctrl and dragging the element of the list (the symbol) from the window into any point of the workspace of the terminal, or having executed the "Chart Window" command of the context menu. All new charts are opened with the DEFAULT.TPL [template](/en/docs/mt4/terminal/chart_management/templates) created during the terminal installation. This template cannot be deleted, but it can be modified.

History data used for drawing of charts are stored on the hard disk. At opening of a chart, the data are downloaded from the disk and the last missing data are spooled from the trading server. If there are no history data for the symbol on the hard disk, the latest 512 bars of history will be downloaded. To spool the earlier data, one has to move the chart to the desired area. After the chart has been opened, information about the current quotes starts to income to the terminal. Thus, the further price changes will be shown in the real-time mode. This information will be stored in the history file and used at the reopening of this chart in future.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The "Max. bars in history" and "Max. bars in chart" parameters are defined in the <a href="/en/docs/mt4/terminal/setup/setup_charts" class="topiclink">terminal settings</a>. These parameters allow to control over the amount of history data displayed and stored on the hard disk.</span></p></td></tr></tbody></table>

## Offline Charts

Client terminal allows to work with offline charts. These charts are opened on basis of data saved on the hard disk in [HST format](/en/docs/mt4/terminal/service/history_center). They are not updated from the server. These charts turn out as very useful for working with non-standard securities or periods.

To open a new chart in offline mode, one has to execute the ["File — Open Offline" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) command. Then, a symbol must be selected in the window that appears, and the "Open" button must be pressed. The [OFFLINE.TPL template](/en/docs/mt4/terminal/chart_management/templates) is applied to the chart automatically. At that, the "(offline)" inscription will appear added in the heading of the offline chart.

At [testing an expert](/en/docs/mt4/terminal/autotrading/tester), the data file in [FXT format](/en/docs/mt4/terminal/autotrading/tester/tester_fxt) is created and used. It differs from a standard chart, but it can be opened offline.

[Working with Charts](/en/docs/mt4/terminal/chart_management)

[Setup](/en/docs/mt4/terminal/chart_management/charts_setup)