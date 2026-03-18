# Start Terminal

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/launch

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
            -   [Install Terminal](/en/docs/mt5/platform/administrator/getting_started/administrator_installation)
            -   [Start Terminal](/en/docs/mt5/platform/administrator/getting_started/launch)
            -   [Structure of Directories and Files](/en/docs/mt5/platform/administrator/getting_started/structure)
            -   [Add or Remove Servers](/en/docs/mt5/platform/administrator/getting_started/server_add_delete)
            -   [Connect to Server](/en/docs/mt5/platform/administrator/getting_started/server_connect)
            -   [Change Password](/en/docs/mt5/platform/administrator/getting_started/change_password)
            -   [Live Update](/en/docs/mt5/platform/administrator/getting_started/live_update)
            -   [Uninstall Terminal](/en/docs/mt5/platform/administrator/getting_started/deinstallation)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Getting Started](/en/docs/mt5/platform/administrator/getting_started)Start Terminal

# Start Terminal

After the installation has been completed, a group of the administrator terminal programs is created in the "Start" menu, and the program shortcut is additionally located on the desktop. They will help to start the terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">You cannot run two copies of the administrator terminal from the same directory simultaneously, including running in the <a href="/en/docs/mt5/platform/administrator/getting_started/launch#console" class="topiclink">console mode</a>. If you need to run multiple terminals at the same time, install the appropriate number of programs in different directories.</span></p></td></tr></tbody></table>

The administrator terminal can be launched in two modes.

## Main launch mode [#](launch#guest)

Starting from MS Windows Vista, applications installed to Program Files are not allowed by default to store their data in the installation folder. All data should be stored in a separate Windows user directory.

Thus, if the terminal is installed in the Program Files directory and user rights to write to that directory are limited, it is run in the main mode. The main mode is also used in the following situations:

-   If the UAC (User Activity Control) system is enabled.
-   If remote connection to a computer is used (RDP, Remote Desktop Protocol).

In this mode, the editable files of the terminal are stored in a specific Windows user directory, and the immutable files are stored in Program Files. The immutable files include the executable terminal file, built-in help files, etc. Editable files are:

-   all settings of the terminal, configuration files
-   all databases (news, mails)
-   terminal operation logs
-   email templates

All the editable files of the terminal are stored in the following directory: C:\\Users\\username\\AppData\\Roaming\\MetaQuotes\\MetaTrader 5 Administrator\\instance\_id\\.

Here 'C' is the logical drive letter on which Windows is installed, "username" is the account name in the operating system under which the terminal has been installed, "instance\_id" means a unique identifier generated based on the path to the directory where you installed 0terminal.

For quick access to these folders, use the command "![Open data folder](/en/docs/mt5/platform/img/open_data_folder_button.png "Open data folder") Open Data Folder" in the [File](/en/docs/mt5/platform/administrator/interface/main_menu/menu_file) menu. Each data folder contains a special text file origin.txt. This file contains the path to the terminal installation folder, which corresponds to this data directory.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">In the main mode, the catalog where editable files are stored is different for each Windows account.</span></li><li class="p_tableatten"><span class="f_tableatten">A detailed description of the file structure of the administrator terminal and of the files purpose are given in the <a href="/en/docs/mt5/platform/administrator/getting_started/structure" class="topiclink">appropriate section</a>.</span></li></ul></td></tr></tbody></table>

## Portable Mode [#](launch#portable)

When installed to Program Files, the terminal operates by default in the main mode described above. All data are stored in a special Windows user directory. However you can force the terminal to store its data in the installation folder. To do it, run the platform in the portable mode. To use this mode, start terminal from the command line with the additional /portable key. For example, "D:\\Program Files\\MetaTrader 5 Manager\\mt5manager64.exe /portable".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To run the terminal in Portable mode, the following conditions must be met:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">If the terminal is installed in the Program Files folder, the user must have administrator rights on the computer. In addition, UAC (User Account Control) must be disabled in the operating system.</span></li><li class="p_tableatten"><span class="f_tableatten">If the terminal is installed in any other folder, the user must have permission to write data to that folder.</span></li></ul></td></tr></tbody></table>

## Console Mode [#](launch#console)

The administrator terminal can be used in the console mode, without the user interface. This mode enables the automation of some processes when operating with the trading platform.

Use the /console key to launch the terminal in the console mode:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">/console&nbsp;/server:&lt;trade&nbsp;server&nbsp;address:port&gt;&nbsp;/login:&lt;login&gt;&nbsp;/password:&lt;password&gt;&nbsp;/action:&lt;command&gt;&nbsp;[command&nbsp;arguments]</span></p></td></tr></tbody></table>

Specify platform connection details in the 'server', 'login' and 'password' parameters. The type of the cation to perform is specified in 'action':

### Server restart

Command /action:restart \[/name:<server name>\]. Optionally the server name can be specified (History, Access...). If the name is specified, the appropriate sever will be searched (case insensitive). If the name is not specified, the specified command will be performed for the currently connected server.

### Platform configuration export to JSON

Command /action:export /file:<path> \[/type:<type> /config:<mask>\]. If optional arguments are not specified, the entire configuration of the connected server is exported.

Argument /file:<path> sets the destination file path. Argument /type:<type> is used for exporting a selected configuration branch and it may have the following values:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">common</span><br><span class="f_CodeExample">network</span><br><span class="f_CodeExample">firewall</span><br><span class="f_CodeExample">time&nbsp;&nbsp;</span><br><span class="f_CodeExample">holidays</span><br><span class="f_CodeExample">groups</span><br><span class="f_CodeExample">managers</span><br><span class="f_CodeExample">routing</span><br><span class="f_CodeExample">gateways</span><br><span class="f_CodeExample">plugins</span><br><span class="f_CodeExample">feeders</span><br><span class="f_CodeExample">reports</span><br><span class="f_CodeExample">symbols</span><br><span class="f_CodeExample">spreads</span><br><span class="f_CodeExample">historysync</span></p></td></tr></tbody></table>

Argument /config:<mask> sets a search criterion to search for a particular configuration structure by a string mask (this may contain \*,!). Search by mask can be used for the configurations of servers, groups, managers, trade requests, gateways, plugins, data feeds, reports and symbols. The following rule applies to other configurations: if a mask is set, the configuration should be skipped, if no mask is specified, the configuration should be processed.

### Platform configuration import

Command /action:import /file:<path> \[/type:<type> /config:<mask>\]. All arguments are similar to those applied to exports, except for the /type argument. The [common](/en/docs/mt5/platform/administration/admin_start) branch (common platform settings) cannot be imported.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In console mode, log files are saved in the directory where the Administrator terminal executable file is located: [directory with mt5admin64.exe]\Logs\.</span></p></td></tr></tbody></table>

[Install Terminal](/en/docs/mt5/platform/administrator/getting_started/administrator_installation)

[Structure of Directories and Files](/en/docs/mt5/platform/administrator/getting_started/structure)