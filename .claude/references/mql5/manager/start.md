# Terminal Start

> Source: https://support.metaquotes.net/en/docs/mt5/manager/start

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)Terminal Start

# Terminal Start

As soon as installation is complete, a group of programs of the Manager terminal is created in the Start menu, and the program shortcut is created on the desktop. Use them to run the platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">You cannot run two copies of the terminal from the same directory simultaneously. If you need to run multiple copies at the same time, install the appropriate number of programs in different directories.</span></p></td></tr></tbody></table>

There are two modes of starting the Manager terminal.

## Main launch mode [#](start#guest)

Starting from MS Windows Vista, applications installed to Program Files are not allowed to store their data in the installation folder on default. All data should be stored in a separate Windows user directory.

Thus, if the terminal is installed in the Program Files directory and the user's rights to write to that directory are limited, it is run in the main mode. The main mode is also used in the following situations:

-   If the UAC (User Activity Control) system is enabled.
-   If remote connection to a computer is used (RDP, Remote Desktop Protocol).

In this mode, the editable files of the terminal are stored in a specific Windows user directory, and the immutable files are stored in Program Files. The immutable files include executable file of the terminal, built-in help files, etc. Editable files are:

-   all settings of the terminal, configuration files
-   all databases (news, mails)
-   terminal operation [journal](/en/docs/mt5/manager/toolbox#journal)
-   email templates

All the editable files of the terminal are stored in the following directory: C:\\Users\\username\\AppData\\Roaming\\MetaQuotes\\MetaTrader 5 Manager\\instance\_id\\.

Here 'C' is the letter of the logical drive Windows OS is installed at, "username" — account name in the operating system, under which the terminal has been installed, "instance\_id" — a unique identifier generated based on the path to the directory where you installed terminal.

For quick access to these folders, use the "![Open Data Folder](/en/docs/mt5/manager/img/open_data_folder_button.png "Open Data Folder") Open Data Folder" command in the [File](/en/docs/mt5/manager/main_menu#file) menu. Each data folder contains a special origin.txt text file. This file contains the path to the terminal installation folder, which corresponds to this data directory.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">In the main mode, the catalog where editable files are stored is different for each Windows account.</span></li><li class="p_tableatten"><span class="f_tableatten">A detailed description of the platform file structure and their purpose is given in the <a href="/en/docs/mt5/manager/beginning_advanced/structure" class="topiclink">appropriate section</a>.</span></li></ul></td></tr></tbody></table>

## Portable mode [#](start#portable)

When installed to Program Files, the platform works in the main mode described above on default. All the terminal data are stored in a special Windows user directory. However, you can force the terminal to store its data in the installation folder. To do it, run the platform in the portable mode. To use this mode, start terminal from the command line with the additional /portable key. For example, "D:\\Program Files\\MetaTrader 5 Manager\\mt5manager64.exe /portable".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To run the terminal in Portable mode, the following conditions should be met:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">If the terminal is installed in the Program Files folder, a user should have administrator rights on the computer. In addition, UAC (User Account Control) should be disabled in the operating system.</span></li><li class="p_tableatten"><span class="f_tableatten">If the terminal is installed in any other folder, a user should have permission to write data to that folder.</span></li></ul></td></tr></tbody></table>

[Manager](/en/docs/mt5/manager)

[Connecting to the Server](/en/docs/mt5/manager/connect)