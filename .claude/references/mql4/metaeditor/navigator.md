# Navigator

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/navigator

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
        -   [Launch](/en/docs/mt4/metaeditor/open)
        -   [Settings](/en/docs/mt4/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt4/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt4/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt4/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt4/metaeditor/workspace)
            -   [Navigator](/en/docs/mt4/metaeditor/navigator)
            -   [Toolbox](/en/docs/mt4/metaeditor/toolbox)
            -   [Status Bar](/en/docs/mt4/metaeditor/status_bar)
            -   [Working with windows](/en/docs/mt4/metaeditor/source_code_windows)
            -   [Hot keys](/en/docs/mt4/metaeditor/hotkeys)
        -   [Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)
        -   [MQL4/MQL5 Wizard](/en/docs/mt4/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt4/metaeditor/development)
        -   [Working with SQL data bases](/en/docs/mt4/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt4/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt4/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt4/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt4/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt4/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt4/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt4/metaeditor/video_guides)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Workspace](/en/docs/mt4/metaeditor/workspace)Navigator

# Navigator

Navigator window allows you to work with files and folders inside the trading platform's /MQL4 or /MQL5 directories. They store trading robots, indicators and scripts, as well as source code files and other data for programming on MetaQuotes Language. Press Ctrl+D or execute ![Navigator](/en/docs/mt5/metaeditor/img/navigator_icon.png "Navigator") Navigator command of the [View](/en/docs/mt5/metaeditor/main_menu_view#navigator) window or in the [Standard](/en/docs/mt5/metaeditor/toolbar_standard#navigator) toolbar to show/hide the window.

The window resembles a file manager displaying folders and files as a tree list:

![Navigator](/en/docs/mt5/metaeditor/img/navigator.png "Navigator")

A similar structure is displayed in the Navigator window of the trading platform. For example, if you create your indicator in the MQL5\\Indicators\\MyIndicator\\ directory, you can launch it in the trading platform from the same directory.

To view the folder contents or open a source file for editing, double-click on an appropriate element in the Navigator. To re-locate a folder/file, select it and drag to a necessary directory while holding the left mouse button (Drag'n'Drop).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">External changes to directories and files (via Windows Explorer) are also displayed in the Navigator window.</span></p></td></tr></tbody></table>

## Project [#](navigator#project)

A separate Navigator tab is designed for managing [projects](/en/docs/mt5/metaeditor/projects). All used files are arranged into various categories:

-   Dependencies — include files. These are files with the source code, which are used in the project. For example, dependencies may include standard library files.
-   Headers — header files. Such files contain custom identifiers, macros, structures and other constructions used in the project.
-   Sources — source code files of the project.
-   Resources — resource files, such as images, sounds, etc.
-   Settings and files — sets of input parameters (\*.set) and other files.

Read more about how to work with projects in the [separate section](/en/docs/mt5/metaeditor/projects).

## Context menu [#](navigator#context_menu)

The following commands can be performed from the context menu:

-   ![Open](/en/docs/mt5/metaeditor/img/open_icon.png "Open") Open — open a selected file for editing. The same action can be done by double clicking on the file or by pressing Enter.
-   ![Open Folder](/en/docs/mt5/metaeditor/img/open_folder_icon.png "Open Folder") Open Folder — open a selected folder or a folder containing a selected file.
-   ![New File](/en/docs/mt5/metaeditor/img/new_icon.png "New File") New File — create a new MQL4/MQL5 program using MQL4/MQL5 Wizard.
-   ![New Project](/en/docs/mt5/metaeditor/img/project_new_icon.png "New Project") New Project — create a [new project](/en/docs/mt5/metaeditor/projects#create).
-   ![New Project from Source](/en/docs/mt5/metaeditor/img/project_from_source_icon.png "New Project from Source") New Project from Source — create a new [project from the selected source file](/en/docs/mt5/metaeditor/projects#create_source).
-   ![New Folder](/en/docs/mt5/metaeditor/img/new_folder_icon.png "New Folder") New Folder — create a new folder in the current directory. The same action can be performed by pressing Insert.
-   ![Rename](/en/docs/mt5/metaeditor/img/rename_icon.png "Rename") Rename — rename a selected file or folder. The same action can be performed by pressing F2.
-   ![Delete](/en/docs/mt5/metaeditor/img/delete_icon.png "Delete") Delete — delete a selected file or folder. The same action can be performed by pressing Delete.
-   ![Refresh](/en/docs/mt5/metaeditor/img/refresh_icon.png "Refresh") Refresh — refresh the Navigator window. If files or folders are copied to one of MQL4 or MQL5 sub-folders, these changes are automatically displayed in the Navigator window. However, you can manually re-read the file structure by executing this command or by pressing F5.
-   ![Compile](/en/docs/mt5/metaeditor/img/compile_open_files_icon.png "Compile") Compile — [compile](/en/docs/mt5/metaeditor/compile) a selected file. Executing this command for a folder results in compilation of all files contained in it.
-   ![Show All Files](/en/docs/mt5/metaeditor/img/show_all_files_icon.png "Show All Files") Show All Files — show/hide all files. If the option is disabled, the source code (\*.MQ4, \*.MQ5, \*.MQH, \*.CPP and \*.H) and text files (\*.TXT and \*.CSV) are displayed in the Navigator, while executable ones are hidden.
-   ![Activate MQL5 Storage](/en/docs/mt5/metaeditor/img/storage_enable_icon.png "Activate MQL5 Storage") Activate MQL5 Storage — start using your personal [MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage_connect) for storing source codes.
-   ![Update from Storage](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update from Storage") Update from Storage — [receive](/en/docs/mt5/metaeditor/mql5storage_working#update) the latest data revision from Storage.
-   ![Commit to Storage](/en/docs/mt5/metaeditor/img/mql5storage_commit_icon.png "Commit to Storage") Commit to Storage — [send](/en/docs/mt5/metaeditor/mql5storage_working#commit) the current data changes to Storage.
-   ![Add File or Folder](/en/docs/mt5/metaeditor/img/mql5storage_add_icon.png "Add File or Folder") Add File or Folder — [add](/en/docs/mt5/metaeditor/mql5storage_working#add) a local folder or a file to Storage. A folder or a file is added locally. Execute the Commit to Storage command to insert changes to Storage.
-   ![Delete File or Folder](/en/docs/mt5/metaeditor/img/mql5storage_delete_icon.png "Delete File or Folder") Delete File or Folder — [delete](/en/docs/mt5/metaeditor/mql5storage_working#add) a folder or a file from Storage. Deletion is performed locally (a file or a folder is deleted physically). Execute the Commit to Storage command to insert the changes to Storage.
-   ![Difference of Versions](/en/docs/mt5/metaeditor/img/mql5storage_diff_icon.png "Difference of Versions") Difference of Versions — [see the current changes](/en/docs/mt5/metaeditor/mql5storage_diff) in a file compared to the latest revision received from Storage.
-   ![Revert Changes](/en/docs/mt5/metaeditor/img/mql5storage_revert_icon.png "Revert Changes") Revert Changes — revert the changes made in a local copy of a file.
-   ![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log — show Storage log.

[Workspace](/en/docs/mt4/metaeditor/workspace)

[Toolbox](/en/docs/mt4/metaeditor/toolbox)