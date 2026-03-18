# Code Base

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/terminal/toolbox_codebase

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Client terminal](/en/docs/mt4/terminal/overview/terminal)Code Base

# Code Base

This tab allows accessing the code base published at [MQL4.community](https://www.mql5.com/en/code/mt4 "MQL4.community") right from the client terminal. Selecting a necessary [MQL4 application](/en/docs/mt4/terminal/autotrading/mql4) at this tab, you can download it and attach to the chart right away.

![Code Base](/en/docs/mt4/terminal/img/toolbox_codebase.png "Code Base")

The applications are displayed in the form of a list containing the following information:

-   Name — name of an MQL4 application. Icons at the beginning of rows display application types:

-   ![Expert Advisor](/en/docs/mt4/terminal/img/ea_icon.png "Expert Advisor") — [Expert Advisors](/en/docs/mt4/terminal/autotrading/experts);
-   ![Indicator](/en/docs/mt4/terminal/img/indicator_icon.png "Indicator") — [Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators);
-   ![Script](/en/docs/mt4/terminal/img/script_icon.png "Script") — [Scripts](/en/docs/mt4/terminal/autotrading/scripts).

-   Description — description of an MQL4 application.
-   Rating — rating of an application given by other users.

To open an application page at the [MQL4.community](https://www.mql5.com/en/code/mt4 "MQL4.community") website, double-click on it in the list.

## Downloading Applications [#](toolbox_codebase#download)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any application in Code Base can be quickly launched by simply dragging it on a chart from this tab. The application will be downloaded to and saved in a folder corresponding to its type (for example, [terminal installation folder]\Experts\), compiled and launched on the selected chart.</span></p></td></tr></tbody></table>

To download an application, execute the "![Download](/en/docs/mt4/terminal/img/download_icon.png "Download") Download" command in the [context menu](/en/docs/mt4/terminal/overview/terminal/toolbox_codebase#context). The downloading will start as soon as you do it.

Applications are saved in the folders that correspond to the application type. For example, Expert Advisors are saved in the folder \[terminal\_installation\_folder\]/Experts/. Once the downloading is over, the window of application launching is opened:

![Running an application](/en/docs/mt4/terminal/img/codebase_run.png "Running an application")

If you click "OK", the application will be launched on the current chart.

## Context Menu [#](toolbox_codebase#context)

The context menu of this section contains the following commands:

-   ![View](/en/docs/mt4/terminal/img/codebase_view_icon.png "View") View — view a selected application at the [MQL4.community](https://www.mql5.com/en/code/mt4 "MQL4.community") website;
-   ![Download](/en/docs/mt4/terminal/img/download_icon.png "Download") Download — [download](/en/docs/mt4/terminal/overview/terminal/toolbox_codebase#download) a selected application to your computer;
-   ![Order your own indicator](/en/docs/mt4/terminal/img/order_job_icon.png "Order your own indicator") Order your own Expert Advisor/indicator/script — go to ordering a development of an MQL4 program at the [freelance service "Jobs" at MQL5.community](https://www.mql5.com/en/job "Development of any MQL5 programs at the freelance service \"Jobs\" at MQL5.community").
-   ![Expert Advisors](/en/docs/mt4/terminal/img/ea_icon.png "Expert Advisors") Expert Advisors — enable/disable displaying of Expert Advisors in the list;
-   ![Indicators](/en/docs/mt4/terminal/img/indicator_icon.png "Indicators") Indicators — enable/disable displaying of indicators in the list;
-   ![Scripts](/en/docs/mt4/terminal/img/script_icon.png "Scripts") Scripts — enable/disable displaying of scripts in the list;
-   Auto Arrange — when this option is enabled, the size of table columns will be selected automatically in case the window size is changed;

-   Grid — show or hide grid to separate table fields.

[Signals](/en/docs/mt4/terminal/overview/terminal/toolbox_signals)

[Search](/en/docs/mt4/terminal/overview/terminal/toolbox_search)