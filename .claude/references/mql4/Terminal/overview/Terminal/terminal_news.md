# News

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/terminal/terminal_news

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Client terminal](/en/docs/mt4/terminal/overview/terminal)News

# News

The list of income news is stored in the "News" tab.

![terminal_window_news](/en/docs/mt4/terminal/img/terminal_window_news.png)

The news topics are represented as a table and arranged according to the incoming time. The news incoming time, its topic and category are published in the table. This list is updated automatically at incoming of the latest news.

The number of news received for the last 24 hours is displayed next to the tab name.

The following commands are available in the context menu:

-   View — view the selected news. One can also read news by double-click with the left mouse button on the topic;
-   Copy — copy the news to the clipboard;

-   Categories — this command appears only if the terminal receives several categories of news. It opens the sub-menu for selecting news categories to be displayed. In order to hide a category a check near it should be removed. If terminal receives only news that belong to one category, this sub-menu is not shown. If there are additional subcategories, the "Customize" command appears. Use it for a detailed [setup](/en/docs/mt4/terminal/overview/terminal/terminal_news#customize) of news categories;

-   Category — show/hide the "Category" column;
-   Auto Arrange — automatic arrangement of columns when changing of the window size;
-   Grid — show/hide grid to separate columns.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">If there is no "News" tab in the "Terminal" window, it means that no news have income yet.</span></li><li class="p_tableatten"><span class="f_tableatten">If the "Enable news" option is disabled in <a href="/en/docs/mt4/terminal/setup/setup_server" class="topiclink">terminal settings</a>, news will not income.</span></li><li class="p_tableatten"><span class="f_tableatten">If the given account has no appropriate rights, this can be one of the reasons why news do not income or cannot be viewed.</span></li></ul></td></tr></tbody></table>

## News Categories [#](terminal_news#customize)

If there are additional subcategories, the "Customize" command appears in the "Categories" menu. Use it for a detailed [setup](/en/docs/mt4/terminal/overview/terminal/terminal_news#customize) of news categories:

![News categories](/en/docs/mt4/terminal/img/news_categories.png "News categories")

In the tree-structured list check those categories that should be displayed in the client terminal.

[Account History](/en/docs/mt4/terminal/overview/terminal/terminal_account_history)

[Alerts](/en/docs/mt4/terminal/overview/terminal/terminal_alerts)