# Find and replace

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/source_code_find

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
        -   [Projects and MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage)
        -   [MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt5/metaeditor/development)
            -   [Intelligent management](/en/docs/mt5/metaeditor/intelligent_management)
            -   [Find and replace](/en/docs/mt5/metaeditor/source_code_find)
            -   [Styler](/en/docs/mt5/metaeditor/styler)
            -   [Compilation](/en/docs/mt5/metaeditor/compile)
            -   [MQL5 Cloud Protector: Advanced protection for programs](/en/docs/mt5/metaeditor/mql5_cloud_protector)
            -   [Code debugging](/en/docs/mt5/metaeditor/debug)
            -   [Code profiling](/en/docs/mt5/metaeditor/profiling)
            -   [AI Assistant](/en/docs/mt5/metaeditor/ai_assistant)
            -   [Generating included code](/en/docs/mt5/metaeditor/generate_mqh)
            -   [Working with C++ DLL (integration with MS Visual Studio)](/en/docs/mt5/metaeditor/c_dll)
            -   [Working with Python](/en/docs/mt5/metaeditor/python)
            -   [OpenCL support](/en/docs/mt5/metaeditor/opencl)
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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)[Developing programs](/en/docs/mt5/metaeditor/development)Find and replace

# Find and replace

The MetaEditor search system allows you to quickly find necessary elements in a program text. All MetaEditor search commands are located in the [Search](/en/docs/mt5/metaeditor/main_menu_search) menu:

-   ![Find](/en/docs/mt5/metaeditor/img/find_icon.png "Find") Find... — open the search window. The same action is performed by pressing Ctrl+F.
-   ![Find Next](/en/docs/mt5/metaeditor/img/find_next_icon.png "Find Next") Find Next — find the next item matching a search query. The same action is performed by pressing F3.
-   ![Find Previous](/en/docs/mt5/metaeditor/img/find_previous_icon.png "Find Previous") Find Previous — find the previous item matching a search query. The same action is performed by pressing Shift+F3.
-   ![Replace](/en/docs/mt5/metaeditor/img/replace_icon.png "Replace") Replace... — open a window to replace the found text. The same action is performed by pressing Ctrl+H.
-   ![Find in Files](/en/docs/mt5/metaeditor/img/find_in_files_icon.png "Find in Files") Find in Files... — open the [search window by different files](/en/docs/mt5/metaeditor/source_code_find#find_in_files). The same action is performed by pressing Ctrl+Shift+F.
-   ![Go to Line](/en/docs/mt5/metaeditor/img/go_to_line_icon.png "Go to Line") Go to Line... — go to a line with a specified number.

![Replace](/en/docs/mt5/metaeditor/img/replace.png "Replace")

The find/replace window features the following parameters and commands:

-   Find what — field to enter a search word or phrase.
-   Replace with — field to enter a word or phrase that is to replace detected elements.
-   Match case — enable/disable case sensitivity when executing the search query.
-   Match whole word only — search by a particular word form: only words or phrases that exactly match the search query are found.
-   Extended with \\r \\n \\t — enable extended search with partial regular expression support. Use \\r, \\n, \\t to specify line feed and tab characters in search requests.
-   Backward direction — enable search up from the current cursor position.
-   In selection — enable/disable search and replacement only in a selected text fragment.
-   #include files — add the files, included into the current file via [#include](https://www.mql5.com/en/docs/basis/preprosessor/include), to Search and Replace. The option enables faster operations with projects consisting of multiple files. For example, to replace a text in all files, you will not need to specify their directories manually, while the editor can automatically find them through the #include directives.
-   Find Next — move to the next found element. The same action is performed by pressing F3.
-   Replace — replace a detected element.
-   Replace All — replace all detected elements.

Search and Replace useful functions:

-   If you select a text in the file and bring up the search box, the text will be automatically substituted in the "Find" field. If no text is selected, a text from the clipboard will be pasted in the "Find" field. If the clipboard is empty, the focus in the search box will be set to the "Find" field.
-   A similar behavior is implemented for the replace window: the selected text is inserted in the search field, and the cursor is moved to the "Replace with" field. Thus, you can immediately enter the required new text.
-   Search and replace results are shown in the [log](/en/docs/mt5/metaeditor/toolbox#journal). If the Toolbox window is enabled, the Journal tab will be automatically selected in it.

## Find in Files [#](source_code_find#find_in_files)

This type of search allows you to find code elements in multiple files at once, rather than in the current window only. Click ![Find in Files](/en/docs/mt5/metaeditor/img/find_in_files_icon.png "Find in Files") Find in Files... in the Search menu or press Ctrl+Shift+F.

![Find in Files](/en/docs/mt5/metaeditor/img/find_in_files.png "Find in Files")

The Find In Files window features the following parameters and commands:

-   Find what — field to enter a search word or phrase.
-   Replace with — field to enter a word or phrase that is to replace detected elements.
-   Filter — files the search is performed in. You can specify names of specific files separated by semicolons or file masks using the "\*" symbol. For example, \*.mq5 means searching all files with MQ5 extension.
-   Folder — folder the search is performed in. To select a folder, click ![Overview](/en/docs/mt5/metaeditor/img/browse_button.png "Overview"). For convenience, you can use the %terminal% macro instead of the full path to the platform data directory. For example, %terminal%\\MQL5\\Experts.
-   Look in subfolders — enable/disable search in all subfolders of a specified folder.
-   Match case — enable/disable case sensitivity when executing the search query.
-   Match whole word only — search by a particular word form: only words or phrases that exactly match the search query are found.
-   Extended with \\r \\n \\t — enable extended search with partial regular expression support. Use \\r, \\n, \\t to specify line feed and tab characters in search requests.
-   Find All — perform a search on request.
-   Replace in Files — replace found elements in all files.

Results of searching in files are displayed on the Search tab of the [Toolbox](/en/docs/mt5/metaeditor/toolbox#search) window. If the search request yields no results, the appropriate message is displayed on the Search tab.

## Search in the Community [#](source_code_find#community)

MetaEditor features the smart and high-performance search throughout [MQL5.community](https://www.mql5.com "MQL5.community") — community of traders and MQL4/MQL5 developers. The site contains a lot of useful information: [documentation](https://www.mql5.com/ru/docs "MQL5.community Documentation"), [forum](https://www.mql5.com/ru/forum "MQL5.community Forum"), [blogs](https://www.mql5.com/ru/blogs "Traders' and analysts' blogs at MQL5.community") of traders and analysts, [articles](https://www.mql5.com/ru/articles "MQL5.community Articles") related to programming and platform use. The community provides access to the huge [source code database](/en/docs/mt5/metaeditor/toolbox#codebase "MQL5.community Code Base") and [the application store](https://www.mql5.com/ru/market "Trading platform application store at MQL5.community")for the platform.

In addition to MQL5.community, the search includes other popular platforms, such as GitHub, MSDN and Stack Overflow.

![Search in the MQL5.community](/en/docs/mt5/metaeditor/img/find_community.png "Search in the MQL5.community")

Search results from external resources appear in the [toolbox window](/en/docs/mt5/metaeditor/toolbox#search):

![GitHub and MSDN search results](/en/docs/mt5/metaeditor/img/find_github.png "GitHub and MSDN search results")

Furthermore, you can immediately download source files from GitHub. Files are downloaded into a separate subdirectory of the Projects folder, named in accordance with the GitHub project name.

[Intelligent management](/en/docs/mt5/metaeditor/intelligent_management)

[Styler](/en/docs/mt5/metaeditor/styler)