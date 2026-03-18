# News

> Source: https://support.metaquotes.net/en/docs/mt4/manager/news_mail/ug_news

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
            -   [Mailbox](/en/docs/mt4/manager/news_mail/ug_mail)
            -   [News](/en/docs/mt4/manager/news_mail/ug_news)
            -   [Support](/en/docs/mt4/manager/news_mail/ug_toolbox_support)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Mail, News and Support](/en/docs/mt4/manager/news_mail)News

# News

The "News" tab of the "Toolbox" window allows to look through the published news, as well as to add recent news in both text format and HTML format.

![News window](/en/docs/mt4/manager/img/tb_news.png "News window")

-   View — open a news to look it through; at this the body of the news is requested from the server;
-   Send — add a news to the news flow;
-   Auto Arrange — automatic arrangement of column sizes when the window sizes are changed;
-   Grid — show/hide grid to separate columns.

## Adding a News (News window) [#](ug_news#news)

![Adding a news](/en/docs/mt4/manager/img/add_news.png "Adding a news")

The "News" window allows to add a news to the news flow. It is necessary to input the news category, its topic, and its body in either text format or HTML format. If necessary, it can be indicated that the news has a high priority. Unread news having a high priority are fixed in the top of the news list in the "News" tab of the "Toolbox" window of client terminal. News-templates are located in "templates\\news" subfolder as plain text files or html files.

In the "Language" field, you can choose the language to be assigned to the news. This allows organizing direct mailing taking into account the appropriate settings. The languages of received news are set up for the groups of accounts via the administrator terminal. If "Any language" is set, the news will correspond to all languages. This news will be received by all clients regardless of their language settings.

The "Send" command sends the news to the news flow.

[Mailbox](/en/docs/mt4/manager/news_mail/ug_mail)

[Support](/en/docs/mt4/manager/news_mail/ug_toolbox_support)