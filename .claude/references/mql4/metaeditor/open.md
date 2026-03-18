# Launching MetaEditor

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/open

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)Launch

# Launching MetaEditor

Upon the trading platform installation, MetaEditor shortcuts appear in the Start menu and the desktop. You can also launch the editor using metaeditor.exe file in the platform installation directory.

If you select an executable program in the trading platform's Navigator and press Enter or click ![Modify](/en/docs/mt5/metaeditor/img/modify_icon.png "Modify") Modify in its context menu, MetaEditor is launched and the source code of this program is opened there at once (if it is present).

## Main launch mode [#](open#guest)

Starting from MS Windows Vista, applications installed to Program Files are not allowed to store their data in the installation folder by default. All data should be stored in a separate Windows user directory. This is the main operation mode.

Thus, if MetaEditor (the trading platform) is installed in the Program Files directory and user rights to write to that directory are limited, it is run in the main mode. The main mode is also used in the following situations:

-   If the UAC (User Activity Control) system is enabled.
-   If remote connection to a computer is used (RDP, Remote Desktop Protocol).

In this mode, the editable files are stored in a specific Windows user directory, and the immutable files are stored in Program Files. The MetaEditor executable file is also immutable, while all files in the MQL4/MQL5 directory (trading robots, indicators, scripts, source files for programming), as well as metaeditor.log are editable.

All the editable files of the platform are stored in the following directories (depending on the operating system used):

Microsoft Windows XP SP3:

-   C:\\Documents and Settings\\username\\Application Data\\MetaQuotes\\Terminal\\instance\_id\\

Microsoft Windows Vista and higher:

-   C:\\Users\\username\\AppData\\Roaming\\MetaQuotes\\Terminal\\instance\_id\\

Here 'C' is the logical drive letter on which Windows is installed, "username" is the account name in the operating system under which the platform has been installed, "instance\_id" is a unique identifier generated based on the path to the directory where the platform is installed.

For quick access to these folders, use the ![Open Data Folder](/en/docs/mt5/metaeditor/img/open_data_folder_icon.png "Open Data Folder") Open Data Folder command in the [File](/en/docs/mt5/metaeditor/main_menu_file) menu. Each data folder contains a special text file origin.txt. This file contains the path to the platform installation folder, which corresponds to this data directory.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">In the main mode, the catalog where editable files are stored is different for each Windows account.</span></p></td></tr></tbody></table>

## Portable Mode

When installed to Program Files, the platform and MetaEditor work in the main mode described above by default. All data are stored in a special Windows user directory. However you can force the platform and MetaEditor to store its data in the installation folder. To do it, run the platform in the portable mode. To use this mode, start MetaEditor from the command line with the additional /portable key. For example, "C:\\Program Files\\MyTerminal\\metaeditor.exe /portable".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To run the terminal in Portable mode, the following conditions should be met:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">If the platform is installed in the Program Files folder, the user should have administrator rights on the computer. In addition, UAC (User Account Control) should be disabled in the operating system.</span></li><li class="p_tableatten"><span class="f_tableatten">If the platform is installed in any other folder, the user should have permission to write data to that folder.</span></li></ul><p class="p_tableatten"><span class="f_tableatten">If the platform/MetaEditor has previously worked in the main mode, no files from the user directory are transferred to the installation one after launching in the Portable mode. Only new data are saved in the installation directory.</span></p><p class="p_tableatten"><span class="f_tableatten">MetaEditor launch in an incorrect mode may cause the absence of files in the <a href="/en/docs/mt5/metaeditor/navigator" class="topiclink">Navigator</a> window. When you start in normal mode, the data is requested from the folder where the executable file is stored, and in the guest mode, they are requested from the user's system folder.</span></p></td></tr></tbody></table>

[MetaEditor](/en/docs/mt4/metaeditor)

[Settings](/en/docs/mt4/metaeditor/settings)