# News

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
            -   [Main Menu](/en/docs/mt5/platform/administrator/interface/main_menu)
            -   [Toolbar](/en/docs/mt5/platform/administrator/interface/toolbar)
            -   [Status Bar](/en/docs/mt5/platform/administrator/interface/status_bar)
            -   [Search](/en/docs/mt5/platform/administrator/interface/search)
            -   [Hot Keys](/en/docs/mt5/platform/administrator/interface/hotkeys)
            -   [Toolbox](/en/docs/mt5/platform/administrator/interface/toolbox)
                -   [News](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news)
                -   [Economic Calendar](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_calendar)
                -   [Search](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_search)
                -   [Journal](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_journal)
        -   [Terminal Settings](/en/docs/mt5/platform/administrator/settings)
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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[User Interface](/en/docs/mt5/platform/administrator/interface)[Toolbox](/en/docs/mt5/platform/administrator/interface/toolbox)News

# News

In this tab you can work with news messages that come to the terminal.

![News](/en/docs/mt5/platform/img/toolbox_news.png "News")

News items are displayed in the form of a table with three columns:

-   Time — the time of news coming to the terminal;
-   Subject — title of news;
-   Category — category of news.

The news messages that has not been viewed yet are displayed with the bold font and have icon ![Unread News](/en/docs/mt5/platform/img/unread_news_icon.png "Unread News"). Read messages are marked by icon ![Read News](/en/docs/mt5/platform/img/read_news_icon.png "Read News"). The ![Priority News](/en/docs/mt5/platform/img/priority_news_icon.png "Priority News") icon means that the news has a high priority. In order to read a news, one should click with the left mouse button on it.

## Context Menu [#](toolbox_news#context)

The context menu of news contains the following commands:

-   ![View](/en/docs/mt5/platform/img/view_mail_button.png "View") View — opens the window of [viewing](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news#view) news;
-   ![Create](/en/docs/mt5/platform/img/send_mail_icon.png "Create") Create — opens the window of [sending](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news#send) news;
-   Categories — opens the submenu of choosing the news categories to be displayed in the list. To disable displaying of a category, remove the check against it. If the terminal receives only one category of news this menu is not displayed. If one of the categories contains two or more subcategories then the "Customize" command appears in this submenu. Using it one can [adjust](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news#customize) the news categories more precisely;
-   Category — show/hide the Category column in the list of news;
-   Auto Arrange — if this option is enabled, the size of columns is selected automatically;
-   Grid — this option shows/hides grid to separate table fields.

## News Categories [#](toolbox_news#customize)

Using the Customize command of the [news categories](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news#categories) submenu, you can open the window of their detailed setup:

![News Categories](/en/docs/mt5/platform/img/news_categories.png "News Categories")

In the tree-like list, check the categories that shall be displayed in the administrator terminal.

## Viewing News [#](toolbox_news#view)

To start viewing news, click on its subject in the list. After that the following window will be opened:

![News Viewing](/en/docs/mt5/platform/img/news_view.png "News Viewing")

The window header contains the date and time when the news was received and its title. The main part of the window is occupied by the text of news. The toolbar that contains the following commands is located in the upper part of the window:

-   ![Save](/en/docs/mt5/platform/img/save_button.png "Save") Save —  save the news on a computer as a HTML file or a text file of the Unicode standard;
-   ![Print](/en/docs/mt5/platform/img/print_button.png "Print") Print — print the news;
-   ![Print Preview](/en/docs/mt5/platform/img/print_preview_button.png "Print Preview") Print Preview — open the preview window before printing the news;
-   ![Next](/en/docs/mt5/platform/img/next_news_button.png "Next") Next — view the next news. The same action can be performed using the "Page Up" key;
-   ![Previous](/en/docs/mt5/platform/img/previous_news_button.png "Previous") Previous — view the previous news. The same action can be performed using the "Page Down" key.

## Sending News [#](toolbox_news#send)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To be able to send news, the <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#news" class="topiclink">group</a> the manager belongs to must be allowed to work with news, and the manager must have the <a href="/en/docs/mt5/platform/administration/admin_managers#news" class="topiclink">permission to send news</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">Also a manager should belong to a <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#trade_server" class="topiclink">group</a> that is created at the main trade server.</span></li></ul></td></tr></tbody></table>

In order to write and send a news, press  "![Create](/en/docs/mt5/platform/img/send_mail_icon.png "Create") Create" in the context menu of the "News" tab.

![News Sending](/en/docs/mt5/platform/img/send_news.png "News Sending")

This window contains the following fields:

-   Subject — subject of the news;
-   Template — in this field you can specify a previously created news [template](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news#templates);
-   High priority — if this option is checked, a high priority will be assigned to the message. The priority news messages are marked with the special ![Priority News](/en/docs/mt5/platform/img/priority_news_icon.png "Priority News") icon;
-   Language — choice of the language. There is an option of receiving internal news in the terminals. A user can adjust the receiving of news only in one of the languages. The "Language" option allows to send the news by separate language groups of users. In this field you can also specify "Any", in that case the news will be sent to all users regardless of the language settings in their terminal;
-   Category — the field for entering or choosing the news category. In order to create a subcategory, specify its name with the "\\" symbols after the name of the main category. For example, "Financial news\\Free".

Below is a window for working with the news text. The editor features commands for creating lists, as well as inserting images, links and tables. To view or edit the source HTML code of the news, click ![Switch to HTML mode](/en/docs/mt5/platform/img/html_visual_button.png "Switch to HTML mode") on the toolbar.

The context menu of the text editor window contains standard commands for working with a text: Copy, Cut, Paste, Insert Link, Insert Table and Insert Image. The context menu also allows working with the news templates.

In order to send the news, press the "Send" button.

## Templates [#](toolbox_news#templates)

The Templates submenu of the context menu of the [news editing](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news#send) window allows working with templates:

-   Save Template — save the current text of the news as a template in the \*.htm format. All templates are stored in the [/templates/news](/en/docs/mt5/platform/administrator/getting_started/structure#news_templates) folder of the administrator terminal;
-   Load Template — open the window of choosing a previously created template for loading it;
-   Remove Template — remove the currently selected template.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">When executing the "Remove Template" command a template is irrecoverably deleted from PC.</span></p></td></tr></tbody></table>

[Toolbox](/en/docs/mt5/platform/administrator/interface/toolbox)

[Economic Calendar](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_calendar)