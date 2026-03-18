# Toolbox

> Source: https://support.metaquotes.net/en/docs/mt5/manager/toolbox

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
            -   [Main Menu](/en/docs/mt5/manager/main_menu)
            -   [Toolbar](/en/docs/mt5/manager/toolbar)
            -   [Toolbox](/en/docs/mt5/manager/toolbox)
            -   [Navigator](/en/docs/mt5/manager/navigator)
            -   [Status Bar](/en/docs/mt5/manager/status_bar)
            -   [Hot Keys](/en/docs/mt5/manager/hotkeys)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[User Interface](/en/docs/mt5/manager/interface)Toolbox

# Toolbox

Toolbox is a multi-functional window. It is used for risk management and allows viewing [summary positions](/en/docs/mt5/manager/summary_positions) and [client assets](/en/docs/mt5/manager/exposure). It also provides access to [news](/en/docs/mt5/manager/toolbox#news) and [economic calendar](/en/docs/mt5/manager/economic_calendar).

In the Toolbox window, managers can configure [notifications on market events](/en/docs/mt5/manager/trade_alerts), view [search](/en/docs/mt5/manager/toolbox#search) results, as well as [journal of trade request processing](/en/docs/mt5/manager/dealing#journal) and [terminal operation](/en/docs/mt5/manager/toolbox#journal).

You can show or hide this window using the "![Toolbox](/en/docs/mt5/manager/img/toolbox_icon.png "Toolbox") Toolbox" command of the [View](/en/docs/mt5/manager/main_menu#view) window or on the [toolbar](/en/docs/mt5/manager/toolbar).

## Summary positions [#](toolbox#summary)

The Summary Positions tab contains data on client's summary open positions grouped by financial symbols. More detailed information can be found in the [appropriate section](/en/docs/mt5/manager/summary_positions).

![Summary positions](/en/docs/mt5/manager/img/toolbox_summary.png "Summary positions")

## Exposure [#](toolbox#exposure)

The Exposure tab contains the assets of clients and the covered assets of a company grouped by currencies. More detailed information can be found in the [appropriate section](/en/docs/mt5/manager/exposure).

![Exposure](/en/docs/mt5/manager/img/toolbox_exposure.png "Exposure")

## News [#](toolbox#news)

Here you can read incoming news.

![News](/en/docs/mt5/manager/img/toolbox_news.png "News")

News messages that have not been read yet are displayed in bold and are marked with icon ![Unread News](/en/docs/mt5/manager/img/unread_news_icon.png "Unread News"). Read news have icon ![Read News](/en/docs/mt5/manager/img/read_news_icon.png "Read News"). Icon ![Priority News](/en/docs/mt5/manager/img/priority_news_icon.png "Priority News") means that the news has a high priority. Double-click its name to read it. In the news preview window, there are several commands available on the toolbar. They allow you to scroll through the news, save them as HTML files (in Unicode format), as well as print them.

Release time and category is displayed for each news. Use the context menu to select the category of displayed news. Go to the Categories submenu, select the necessary ones from the list and click Settings.

![News categories](/en/docs/mt5/manager/img/news_categories.png "News categories")

### Sending news [#](toolbox#news_send)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Only managers with sufficient rights can distribute news. Such rights can be granted by a trading platform administrator.</span></li><li class="p_tableatten"><span class="f_tableatten">News can be sent only when connected to the main trade server.</span></li></ul></td></tr></tbody></table>

To send news, click "![New](/en/docs/mt5/manager/img/send_icon.png "New") New" in the context menu.

![Sending the news](/en/docs/mt5/manager/img/send_news.png "Sending the news")

The news creation window contains the following fields:

-   Subject — news subject.
-   Template — any news can be saved as a template using the context menu. For example, you can save a typical maintenance works news as a template. To get a ready-made news afterwards, simply select the template in this field.
-   High Priority — if enabled, the news will have a high priority. High priority news are marked with a special icon ![Priority News](/en/docs/mt5/manager/img/priority_news_icon.png "Priority News").
-   Language — in client and manager terminals, you can [configure the language](/en/docs/mt5/manager/settings#news_language) of incoming news. A user can choose to receive news on one of the languages. Specify a language in this field if you want to send news to a specific language group of users. If Any is set, news is sent to all users regardless of their terminal settings.
-   Category — news category name. To create a subcategory, specify its name with the "\\" character after the title of the main category. For example, "Financial news\\Free".

Below is a window for working with the news text. Commands for creating lists and inserting images, links and tables, etc. are available in the editor. To view or edit the source HTML code of the news, click ![Switch to HTML mode](/en/docs/mt5/manager/img/html_visual_button.png "Switch to HTML mode") on the toolbar.

The context menu of the text editing window contains standard commands for working with the text: Copy, Cut, Paste, Insert Hyperlink, Insert Table and Insert Image. From the context menu, you can also work with news templates.

### News templates [#](toolbox#news_template)

The Templates submenu on the context menu of the news editing window allows working with templates:

-   Save Template — save the current news text as a template in the \*.htm format. All news templates are stored in [/templates/news](/en/docs/mt5/manager/beginning_advanced/structure#news_templates) folder of the Manager terminal.
-   Load Template — open a window for selecting a previously saved template.
-   Remove Template — delete the currently selected template. Be careful, the template is deleted from your computer permanently.

## Find [#](toolbox#search)

Results of the [global search](/en/docs/mt5/manager/toolbar#search) through the Manager terminal are displayed on this tab.

![Search field](/en/docs/mt5/manager/img/search_field.png "Search field")

To view the found element, double-click on it or execute the Open command in the context menu. You will be moved to the appropriate section of the terminal.

## Log [#](toolbox#journal)

The Journal tab contains information about all manager actions in the Manager terminal: launch, connection to server, trade operations, etc. The tab displays events that occurred during the current server connection session only. To see previous entries, click ![Open](/en/docs/mt5/manager/img/open_data_folder_button.png "Open") Open in the context menu.

![Log](/en/docs/mt5/manager/img/toolbox_journal.png "Log")

Journal logs are represented in a table with the following fields:

-   Time — event date and time.
-   Source — event type: Network, server name (event related to the trade server), LiveUpdate (auto update), etc.
-   Message — event description.

Events are divided into several types and marked by special icons:

-   ![Information](/en/docs/mt5/manager/img/journal_info_icon.png "Information") — information message.
-   ![Warning](/en/docs/mt5/manager/img/journal_warning_icon.png "Warning") — warning.
-   ![Error](/en/docs/mt5/manager/img/journal_error_icon.png "Error") — error message.

Press Ctrl+C or executed the "![Copy](/en/docs/mt5/manager/img/copy_icon.png "Copy") Copy" command in the context menu to copy an entry to clipboard.

[Toolbar](/en/docs/mt5/manager/toolbar)

[Navigator](/en/docs/mt5/manager/navigator)