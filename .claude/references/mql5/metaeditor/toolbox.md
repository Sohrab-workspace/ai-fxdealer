# Toolbox

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/toolbox

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
        -   [Launch](/en/docs/mt5/metaeditor/open)
        -   [Settings](/en/docs/mt5/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt5/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt5/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt5/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt5/metaeditor/workspace)
            -   [Navigator](/en/docs/mt5/metaeditor/navigator)
            -   [Toolbox](/en/docs/mt5/metaeditor/toolbox)
            -   [Status Bar](/en/docs/mt5/metaeditor/status_bar)
            -   [Working with windows](/en/docs/mt5/metaeditor/source_code_windows)
            -   [Hot keys](/en/docs/mt5/metaeditor/hotkeys)
        -   [Projects and MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage)
        -   [MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt5/metaeditor/development)
        -   [Working with SQL data bases](/en/docs/mt5/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt5/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt5/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt5/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt5/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt5/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt5/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt5/metaeditor/video_guides)
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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)[Workspace](/en/docs/mt5/metaeditor/workspace)Toolbox

# Toolbox

Toolbox is a multifunctional window. It shows the results of various actions performed in MetaEditor: [compilation](/en/docs/mt5/metaeditor/toolbox#errors), [search](/en/docs/mt5/metaeditor/toolbox#search), [profiling](/en/docs/mt5/metaeditor/toolbox#profile) and [debugging](/en/docs/mt5/metaeditor/toolbox#debug). Besides, it provides access to the extensive [library of source codes](/en/docs/mt5/metaeditor/toolbox#codebase) and [articles about MQL4/MQL5 programming](/en/docs/mt5/metaeditor/toolbox#articles).

The [Journal](/en/docs/mt5/metaeditor/toolbox#journal) tab informs of actions performed in MetaEditor, for example, the ones performed during MQL5 Storage operation.

You can show or hide this window using the ![Toolbox](/en/docs/mt5/metaeditor/img/toolbox_icon.png "Toolbox") Toolbox command of the [View](/en/docs/mt5/metaeditor/main_menu_view#toolbox) window or in the [Standard](/en/docs/mt5/metaeditor/toolbar_standard#toolbox) toolbar to show/hide the window.

## Errors [#](toolbox#errors)

The tab displays the program [compilation](/en/docs/mt5/metaeditor/compile) logs: data on applied files, errors and warnings.

![Errors](/en/docs/mt5/metaeditor/img/toolbox_errors.png "Errors")

The log contains the following data:

-   Description — event description. Icons show a type of an event: ![Error](/en/docs/mt5/metaeditor/img/error_icon.png "Error") — error, ![Warning](/en/docs/mt5/metaeditor/img/warning_icon.png "Warning") — warning, ![Information](/en/docs/mt5/metaeditor/img/info_icon.png "Information") — information message.
-   File — name of a processed file. When hovering a mouse cursor, a tooltip indicating the full file path appears.
-   Line — number of a line containing an error or a warning.
-   Column — number of a column containing an error or a warning.

Double-click an error message, to open an appropriate file. The cursor is immediately set to the error location. A similar action is performed using the ![Go to Line](/en/docs/mt5/metaeditor/img/go_to_line_icon.png "Go to Line") Go to Line command in the context menu.

## Search [#](toolbox#search)

Results of the [search in files](/en/docs/mt5/metaeditor/source_code_find) and [MQL5.community](/en/docs/mt5/metaeditor/toolbar_search) are displayed in this tab.

MetaEditor features the smart and high-performance search throughout [MQL5.community](https://www.mql5.com "MQL5.community") — community of traders and MQL4/MQL5 developers. The site contains all kinds of useful information: [documentation](https://www.mql5.com/en/docs "MQL5.community Documentation"), [forum](https://www.mql5.com/en/forum "MQL5.community forum"), [blogs](https://www.mql5.com/en/blogs "Traders' and analysts' blogs at MQL5.community") of traders and analysts, [articles](https://www.mql5.com/en/articles "MQL5.community Articles") related to programming and platform use. The community provides access to the huge [source code database](/en/docs/mt5/metaeditor/toolbox#codebase "MQL5.community Code Base") and [the application store](https://www.mql5.com/en/market "Trading platform application store at MQL5.community") for the platform.

In addition to MQL5.community, the search includes other popular platforms, such as GitHub, MSDN and Stack Overflow.

The search is performed using the [toolbar](/en/docs/mt5/metaeditor/toolbar_search) and the Online Search command in the [Help menu](/en/docs/mt5/metaeditor/main_menu_search). Search results are conveniently displayed by categories:

![Search](/en/docs/mt5/metaeditor/img/toolbox_search.png "Search")

To have the most recent publications displayed at the top of the list, enable the "Sort by date" option to the right of the categories.

Search in files is performed using the [toolbar](/en/docs/mt5/metaeditor/toolbar_search) and "Find..." command in the [Search menu](/en/docs/mt5/metaeditor/main_menu_search). Results are displayed in the following form:

-   File — name of a file where a search query line is found with a full file path.
-   Line — number of a file line where a necessary phrase is found.
-   Text — found text. The entire structure where the phrase has been found is displayed here.

![Results of searching in files](/en/docs/mt5/metaeditor/img/toolbox_find_in_files.png "Results of searching in files")

To go to the found text, double-click the file name. A similar action is performed using the ![Go to Line](/en/docs/mt5/metaeditor/img/go_to_line_icon.png "Go to Line") Go to Line command in the context menu.

## Profiler [#](toolbox#profile)

This tab displays results of [profiling](/en/docs/mt5/metaeditor/profiling) a program's source code. Profiling allows you to optimize a source code by detecting the slowest fragments in it.

![Profiler](/en/docs/mt5/metaeditor/img/toolbox_profiler.png)

Function name

Number of a line the function description starts from

Number of function calls performed during profiling

Time spent on the function execution: in milliseconds and as a percentage of a total time spent for executing all functions

Graphical representation of a time spent for the function execution

Context menu:

-   Open — move to a line or a function in a source code file. The same can be done by double-clicking or pressing Enter.
-   Expand All — expand all collapsed functions.
-   Collapse All — collapse all expanded functions.
-   Functions by Lines — switch to viewing profiling results [by lines.](/en/docs/mt5/metaeditor/profiling#lines)
-   Functions by Calls — switch to viewing profiling results [by calls.](/en/docs/mt5/metaeditor/profiling#calls)
-   Export — export profiling results in Open XML (MS Office Excel), HTML (Internet Explorer) or CSV (Text file).
-   Auto Arrange — enable/disable automatic sizing of fields. The same action can be done by pressing A.
-   Grid — show/hide grid to separate fields. The same action can be done by pressing G.

Find detailed instructions on profiling in a [separate section](/en/docs/mt5/metaeditor/profiling).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The tab is not displayed before starting profiling using the <img class="help" alt="Start Profiling" title="Start Profiling" width="15" height="12" src="/en/docs/mt5/metaeditor/img/start_profiling_icon.png"> Start Profiling of the <a href="/en/docs/mt5/metaeditor/main_menu_debug" class="topiclink">Debug</a> menu or in the <a href="/en/docs/mt5/metaeditor/toolbar_standard" class="topiclink">Standard</a> toolbar.</span></p></td></tr></tbody></table>

## Debug [#](toolbox#debug)

The Debug tab is displayed only when the [process](/en/docs/mt5/metaeditor/debug) is launched. The window is divided into two parts. The left one displays the [call stack](/en/docs/mt5/metaeditor/debug#stack), while the right one — [values of observed expressions](/en/docs/mt5/metaeditor/debug#watch):

![Debug](/en/docs/mt5/metaeditor/img/toolbox_debug.png "Debug")

### Call stack

The following data on the call stack is shown:

-   File — name and path of a file the function is called from.
-   Function — name of a function, within which the current program execution step is conducted.
-   Line — number of a line the program execution is stopped at.

If not a single breakpoint is enabled and no [step-by-step debugging](/en/docs/mt5/metaeditor/debug#step) commands are executed, the left part remains empty. The context menu allows you to show and hide the grid separating fields and set auto sizing of columns.

### Observing expressions

The right part of the Debug window is intended for [observing expression values](/en/docs/mt5/metaeditor/debug#watch) during debugging:

-   Expression — tracked expression name.
-   Value — tracked expression value.
-   Type — expression type.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">If the expression value is not defined or not calculated at the moment, the appropriate field displays "Unknown identifier". The icons for these expressions look like this: <img class="help" alt="Unknown identifier" title="Unknown identifier" width="16" height="16" src="/en/docs/mt5/metaeditor/img/unknown_identifier_icon.png">.</span></p></td></tr></tbody></table>

To add an expression to the observation, select it in the source code of the program and click ![Add Watch](/en/docs/mt5/metaeditor/img/add_watch_icon.png "Add Watch") Add Watch in the context menu. Also, the observed expression can be added through the context menu of the tab: click ![Add](/en/docs/mt5/metaeditor/img/add_watch_icon.png "Add") Add and specify the expression name.

## Articles [#](toolbox#articles)

The tab provides access to an extensive library of [articles on MQL4/MQL5 programming](https://www.mql5.com/en/articles) published on [MQL5.community](https://www.mql5.com "MQL5.community") website. Articles are an excellent guide for creating applications, since they cover a lot of practical tasks involving algorithmic trading. New articles are published every week.

![Articles](/en/docs/mt5/metaeditor/img/toolbox_articles.png "Articles")

All articles are conveniently divided into categories by subjects, for example, trading, indicators, Expert Advisors, strategy tester, etc. You can sort out articles by categories via the context menu. To view an article, double-click its name or click ![View](/en/docs/mt5/metaeditor/img/article_view_icon.png "View") View in the context menu. The article will be opened in a separate browser window.

Before reading the article, you can view its brief description. To do this, hover the cursor over its name.

## Code Base [#](toolbox#codebase)

The tab provides access to the [library of MQL4/MQL5 source codes](https://www.mql5.com/en/code). The Code Base contains thousands of trading robots, indicators and scripts. Studying a source code of ready-made programs helps to better understand the principles of programming. They can also be used as a basis for your own development.

![Code Base](/en/docs/mt5/metaeditor/img/toolbox_codebase.png "Code Base")

Name, short description, rating (defined by MQL5.community users) and publication date are displayed for each program. To view detailed information about the program on the website, double-click on it. To download the program, click ![Download](/en/docs/mt5/metaeditor/img/download_icon.png "Download") Download in the context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The program file is downloaded to /MQL4 or /MQL5 directory subfolder according to the program's category. For example, all EAs are saved to /MQL5/Experts (or /MQL4/Experts).</span></li><li class="p_tableatten"><span class="f_tableatten">After the download, the MQL4/MQL5 program is automatically <a href="/en/docs/mt5/metaeditor/compile" class="topiclink">compiled</a>.</span></li></ul></td></tr></tbody></table>

All programs are divided into several categories marked with the corresponding icons:

-   ![Expert Advisor](/en/docs/mt5/metaeditor/img/ea_icon.png "Expert Advisor") — Expert Advisors
-   ![Indicator](/en/docs/mt5/metaeditor/img/indicator_icon.png "Indicator") — indicators
-   ![Script](/en/docs/mt5/metaeditor/img/script_icon.png "Script") — scripts
-   ![Library](/en/docs/mt5/metaeditor/img/library_icon.png "Library") — libraries

Use the context menu to sort out programs by categories.

## Public projects [#](toolbox#public_projects)

Each [shared project](/en/docs/mt5/metaeditor/projects#shared) in MQL5 Storage has publicity settings: the project can be private or open to other users. All projects you can join are displayed in the separate Public Projects tab:

![Public projects](/en/docs/mt5/metaeditor/img/toolbox_projects.png "Public projects")

Title, description, author name, number of changes (commits) and creation date are displayed for each project.

To participate in the project, click ![Join](/en/docs/mt5/metaeditor/img/project_public_join_icon.png "Join") Join. After that, the project will appear in the Shared Projects section. Then click ![Update from Storage](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update from Storage") Update from Storage in the context menu of the project in order to download it to your computer. Details on public projects are described in the [separate section](/en/docs/mt5/metaeditor/projects#public).

## Log [#](toolbox#journal)

The journal tab informs you of actions performed in MetaEditor, for example, the ones performed in [MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage), as well as notifications on the availability of the new MQL4/MQL5 language or MetaEditor Reference, etc.

![Journal](/en/docs/mt5/metaeditor/img/toolbox_journal.png "Journal")

The journal displays the following information:

-   Time — event date and time.
-   Source — event type: Storage (MQL5 Storage), help (reference guide), etc.
-   Message — event description.

All events are divided into three types marked by an appropriate icon:

-   ![Information](/en/docs/mt5/metaeditor/img/journal_info_icon.png "Information") — information message
-   ![Warning](/en/docs/mt5/metaeditor/img/journal_warning_icon.png "Warning") — warning
-   ![Error](/en/docs/mt5/metaeditor/img/journal_error_icon.png "Error") — error message

To go to the MetaEditor journal file (metaeditor.log), click ![Open](/en/docs/mt5/metaeditor/img/open_icon.png "Open") Open in the context menu. When running this command, the current journal entries are saved in a file. The journal file is saved in the /Logs directory of the trading platform.

[Navigator](/en/docs/mt5/metaeditor/navigator)

[Status Bar](/en/docs/mt5/metaeditor/status_bar)