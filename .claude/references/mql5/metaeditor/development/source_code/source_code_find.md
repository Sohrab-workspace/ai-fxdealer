# Find and Replace

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/development/source_code/source_code_find

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

# Find and Replace

The search system in MetaEditor allows to quickly find necessary elements in the source code of programs. All the search commands are located in the ["Search"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_search) menu:

-   ![Find](/en/docs/mt5/metaeditor/img/find_icon.png "Find") Find — open the search window.
-   ![Find Next](/en/docs/mt5/metaeditor/img/find_next_icon.png "Find Next") Find Next — find the next element according to the current search request.
-   ![Find Previous](/en/docs/mt5/metaeditor/img/find_previous_icon.png "Find Previous") Find Previous — find the previous element according to the current search request.
-   ![Replace](/en/docs/mt5/metaeditor/img/replace_icon.png "Replace") Replace — open the window for replacing the searched text by a new one.
-   ![Find in Files](/en/docs/mt5/metaeditor/img/find_in_files_icon.png "Find in Files") Find in Files — open the window for [searching in different files](/en/docs/mt5/metaeditor/development/source_code/source_code_find#find_in_files).

In order to open the search window one should execute the "![Find](/en/docs/mt5/metaeditor/img/find_icon.png "Find") Find" command in the "Find and Replace" submenu, in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#find) toolbar or use the "Ctrl+F" key combination. To start the search and replacement one should execute the "![Replace](/en/docs/mt5/metaeditor/img/replace_icon.png "Replace") Replace" command in the same interface element or use the "Ctrl+H" key combination. The search parameters in the "Replace" window are the same as in the one of common searching:

![Replace](/en/docs/mt5/metaeditor/img/replace.png "Replace")

The following parameters are represented here:

-   Find What — the field where the sought word or phrase should be specified;
-   Replace With — the field where the word or phrase that will replace the found elements should be specified;
-   Match Whole Word Only — this option allows to search by the certain word form, only the word or phrases that exactly match the search request will be found;
-   Match Case — enable/disable case sensitivity when executing the search request;
-   Selected text only — enable/disable the mode of searching and replacing in a selected text only;
-   Search up — enable the mode of searching up from the current position of the cursor;
-   Find Next — this command allows to go to the next found element. The same command can be executed using the "F3" key;
-   Replace — replace the found element;
-   Replace All — replace all the found elements;
-   Cancel — close the window.

## Find in Files

This type of search allows to find elements of the source code not only in the current window but also in any other files. In order to start it one should execute the "![Find in Files](/en/docs/mt5/metaeditor/img/find_in_files_icon.png "Find in Files") Find in Files" command in the "Find and Replace" submenu, in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#find_inf_files) toolbar or use the "Ctrl+Shift+F" key combination. The following window will be opened as soon as it is done:

![Find in Files](/en/docs/mt5/metaeditor/img/find_in_files.png "Find in Files")

This window contains the following parameters and commands:

-   Find What — the field where the sough word or phrase should be specified;
-   In Files/File Types — in this field the types of files are specified using the "\*" mask, for example \*.mq5, or the names of the concrete files separated with comma;
-   In Folder — the folder in files of which it is necessary to perform the search is specified in this field. The folder can be specified manually by indicating the path to it or it can be chosen using the ![Browse](/en/docs/mt5/metaeditor/img/browse_button.png "Browse") button;

-   Match Whole Word Only — this option allows to search by a certain word form, only the word or phrases that exactly match the search request will be found;
-   Match Case — enable/disable case sensitivity when executing the search request;

-   Look in Subfolders — enable/disable searching in all subfolders of the selected folder;
-   Find — execute the search request;
-   Cancel — close the window.

Once the "Find" button is pressed the search will be performed. The results of searching in files are displayed in the corresponding tab of the ["Toolbox"](/en/docs/mt5/metaeditor/interface/toolbox/toolbox_find) window.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">If there are no results of the search request, the corresponding information is displayed in <a href="/en/docs/mt5/metaeditor/interface/toolbox/toolbox_find" class="topiclink">"Search"</a> tab.</span></p></td></tr></tbody></table>