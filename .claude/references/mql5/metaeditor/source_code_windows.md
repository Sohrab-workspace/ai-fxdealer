# Working with windows

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/source_code_windows

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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)[Workspace](/en/docs/mt5/metaeditor/workspace)Working with windows

# Working with windows

The main part of MetaEditor workspace is intended for editing source code of programs. All currently opened files are displayed as tabs. To start editing a certain file, click on its tab.

![Tabs](/en/docs/mt5/metaeditor/img/tabs.png "Tabs")

Location of file windows can be changed by [Window](/en/docs/mt5/metaeditor/main_menu_window) menu commands or [Standard](/en/docs/mt5/metaeditor/toolbar_standard#cascade) toolbar. To expand or collapse the tab, double-click its name.

The context menu of tabs features the following commands:

-   ![Compile](/en/docs/mt5/metaeditor/img/compile_icon.png "Compile") Compile — [compile](/en/docs/mt5/metaeditor/compile) the current program code.
-   ![Compile Open Files](/en/docs/mt5/metaeditor/img/compile_open_files_icon.png "Compile Open Files") Compile Open Files — compile all files currently opened for editing.
-   ![Difference of Versions](/en/docs/mt5/metaeditor/img/mql5storage_diff_icon.png "Difference of Versions") Difference of Versions — [see the current changes](/en/docs/mt5/metaeditor/mql5storage_diff) in a file compared to the latest revision received from the storage.
-   ![Revert Changes](/en/docs/mt5/metaeditor/img/mql5storage_revert_icon.png "Revert Changes") Revert Changes — revert the changes made in a local copy of a file.
-   ![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log — view the history of file changes in the [storage log](/en/docs/mt5/metaeditor/mql5storage_working#journal).
-   ![Save](/en/docs/mt5/metaeditor/img/save_icon.png "Save") Save — save a change in the current window. The same action can be performed by pressing Ctrl+S.
-   ![Close](/en/docs/mt5/metaeditor/img/close_window_button.png "Close") Close — close a selected tab. The same action can be performed by pressing Ctrl+F4 or clicking the middle mouse button on a tab name.
-   ![Close All But This](/en/docs/mt5/metaeditor/img/close_all_but_button.png "Close All But This") Close All But This — close all tabs except the current one.
-   ![Copy Full Path](/en/docs/mt5/metaeditor/img/copy_icon.png "Copy Full Path") Copy Full Path — copy the full path to the edited MQL4/MQL5 program file to clipboard.
-   ![Open Containing Folder](/en/docs/mt5/metaeditor/img/open_icon.png "Open Containing Folder") Open Containing Folder — open folder containing the current file.
-   ![Show in Navigator](/en/docs/mt5/metaeditor/img/show_in_navigator_button.png "Show in Navigator") Show in Navigator — find the file opened for editing, in the editor folder structure.

The context menu of the code editing window duplicates the [Edit](/en/docs/mt5/metaeditor/main_menu_edit) and the [Standard](/en/docs/mt5/metaeditor/toolbar_standard) toolbar commands.

[Status Bar](/en/docs/mt5/metaeditor/status_bar)

[Hot keys](/en/docs/mt5/metaeditor/hotkeys)