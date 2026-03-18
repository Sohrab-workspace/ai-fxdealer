# Terminal Start and Data Structure

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/userguide/start_comm

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
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
            -   [Install Terminal](/en/docs/mt4/terminal/userguide/installation)
            -   [Install on Mac OS](/en/docs/mt4/terminal/userguide/install_mac)
            -   [Install on Linux](/en/docs/mt4/terminal/userguide/install_linux)
            -   [Terminal Start and Data Structure](/en/docs/mt4/terminal/userguide/start_comm)
            -   [Opening of Accounts](/en/docs/mt4/terminal/userguide/open_an_account)
            -   [Authorization](/en/docs/mt4/terminal/userguide/authorization)
            -   [OTP](/en/docs/mt4/terminal/userguide/otp)
            -   [Live Update](/en/docs/mt4/terminal/userguide/liveupdate)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Getting Started](/en/docs/mt4/terminal/userguide)Terminal Start and Data Structure

# Terminal Start and Data Structure

After installation has been completed, a group of Client Terminal programs will be created in the "Start" menu, and the program shortcut will additionally appear on the desktop. They will help to start client terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Two copies of the Client Terminal are prohibited to be started from the same directory simultaneously. To start several terminals simultaneously, it is necessary to <a href="/en/docs/mt4/terminal/userguide/installation" class="topiclink">install</a> the corresponding amount of programs in different directories.</span></p></td></tr></tbody></table>

Starting from build 600 the client terminal features the new structure and location of the client terminal files. Now, MQL4 applications are placed in separate directories according to the program type (Expert Advisors, indicators or scripts). In most cases, the terminal data is now stored in a special data folder separated from the terminal installation location. In this article, we will describe in details how data is transferred, as well as the reasons for introducing the new storage system.

## Why Has the New Data Storage System Been Implemented

Microsoft Windows XP released 13 years ago allows applications to write their own data at the place of their installation even if the latter took place in Program Files system folder. A user should only have an administrator permission to write data to any folder.

When working in 64-bit systems, separate installation directories are provided for 32 and 64-bit programs: Program Files and Program Files (x86). Operation features described in the article apply to both directories.

Starting from Windows Vista, Microsoft has introduced a restriction on writing to Program Files directory. If [User Account Control](https://learn.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview "User Account Control") (UAC) system is enabled, programs are not allowed to store their data in Program Files folder. All data should be located in a separate user directory. This limitation has been introduced in order to protect users against malicious programs and to prevent applications under one user account to change or damage the same program's data necessary for another user account. Since that time, security requirements in Microsoft operating systems have been tightening further. In particular, starting with Windows 8, UAC system cannot be disabled even if "Never notify" option is selected in its settings.

Microsoft has implemented [virtualization process](https://msdn.microsoft.com/en-us/library/bb756960.aspx "virtualization process") in order to provide compatibility with older applications when using UAC. If a program tries to save its data to Program Files directory, the data is actually (physically) saved to a separate folder having the following look - C:\\Users\\<user-name>\\AppData\\Local\\VirtualStore\\Program Files, while Windows File Explorer shows the files as if they are saved in the installation directory. Microsoft claims that this mode has been provided only for compatibility and can be removed later.

In order to comply with Microsoft recommendations, the data storage structure has been changed in the client terminal starting from build 600. Now, the terminal will also save its data in a user directory.

## User Data Directory [#](start_comm#data_folder)

In the new version, all data of a certain user working with a certain copy of the terminal are stored in a special place called terminal data folder. This folder can be found on a system disk (a disk with installed Windows operating system) along the following path:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">C:\Users\User_account_name\AppData\Roaming\MetaQuotes\Terminal\Instance_id</span></p></td></tr></tbody></table>

where:

-   С: — name of a system disk;
-   User\_account\_name — user's account for working in Windows;
-   Instance\_id — unique name of the folder where all the user's data for working with a certain copy of the terminal is stored. A unique name consists of 16 characters. The name is generated based on the path to the terminal installation directory, since the path to the terminal installation directory cannot be explicitly used as a folder name. Significant length of the unique name is explained by the fact that multiple copies of the terminal can be installed on a single PC.

"Open Data Folder" command in File menu of the terminal allows searching and opening the data folder.

![Open Data Folder](/en/docs/mt4/terminal/img/terminal_data_folder.png "Open Data Folder")

The root of each terminal data folder also contains origin.txt file where you can find the path to the installation folder of the terminal this data refers to. This allows users to match each terminal data folder with a certain terminal installation directory, for example, in case when several copies of the terminal are installed by a user. This type of working with the terminal when the data folder is separated from the installation one is the main mode.

For more convenience, an entry containing the path to the data folder is made in the terminal's journal each time the terminal is launched. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2014.02.10</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">12:48:28.477</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Data</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Folder:</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">C:\Users\JohnSmith\AppData\Roaming\MetaQuotes\Terminal\9F86138A4E27C7218E9EC98A5F8D8CA1</span></p></td></tr></tbody></table>

## Copying MQL4 Application Files When Updating to Terminal Build 600 and Higher

When the newly updated terminal is launched, it checks if the data folder is present. If the data folder is not present yet, then it is created. If that folder is different from the installation one, the terminal's regular data (standard MQL4 programs, historical data, configuration files, templates, etc.) is copied into it. The files that are not changed during the terminal operation (executable files, mql.dll compiler, sound files, etc.) are left in the installation directory. The terminal data folder is different from the installation one in the following cases:

-   UAC system is enabled. The exception is when the terminal is installed on a portable device (external hard drive, usb flash drive, etc.).
-   Current PC user has limited rights to write data to the installation directory.
-   A user is working via remote connection (RDP).

If none of the above conditions is satisfied, the terminal data is stored in the installation directory.

Then, the user files are moved to the data folder. At this stage, the directory where the terminal's user data has been stored is determined. If the data has been stored in the terminal installation folder, they are copied the following way:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Source folder in the installation directory</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Contents</span></p></th><th class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Destination folder in the terminal data directory</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Expert Advisors (trading robots)</span></p><p class="p_fortable"><span class="f_fortable">Note: only files from the root \experts directory are copied. No subdirectories are copied, since it is impossible to reliably determine their contents</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Experts</span></p></td></tr><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts\indicators</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Custom indicators</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Indicators</span></p></td></tr><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts\scripts</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Scripts (MQL4 applications for a single run on the chart)</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Scripts</span></p></td></tr><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts\include</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Source code MQH and MQ4 files implemented into other programs</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Include</span></p></td></tr><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts\libraries</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Libraries in the form of MQ4 source codes and EX4 executable files compiled from them. They are used for the dynamic call of the functions contained there by other MQL4 programs</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Libraries</span></p></td></tr><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts\files</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Special "file sandbox". MQL4 applications are allowed to execute file operations only within this directory</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Files</span></p></td></tr><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts\logs</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Log files of MQL4 applications</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Logs</span></p></td></tr><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts\presets</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Files of presets for MQL4 applications</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Presets</span></p></td></tr><tr class="table"><td class="table" style="width:275px;"><p class="p_fortable"><span class="f_fortable">\experts\images</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Image files for being used in resources</span></p></td><td class="table" style="width:340px;"><p class="p_fortable"><span class="f_fortable">\MQL4\Images</span></p></td></tr></tbody></table>

Next, it is checked whether the client terminal has stored data in virtualization directory (the operating system's virtual storage described above). If the terminal has been installed in Program Files directory and the operating system is Windows Vista or higher, the terminal data is most probably stored in that directory. If the data is found, it is copied according to the above table.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The files are copied and not moved during the migration. The copied files are not deleted from the source folders.</span></p></td></tr></tbody></table>

During the migration, the entries containing source and destination paths of the copied files are made in the terminal's journal. To view all the logs, open Journal tab of Terminal window and execute Open command in the context menu. The folder containing the terminal log files will open.

If the migration has been completed successfully for the current terminal copy, it is not repeated any more during subsequent terminal updates. If the data folder is different from the installation one, and custom MQL4 applications have been copied together with the standard files during the migration, the following dialog window appears:

![Migration completed successfully](/en/docs/mt4/terminal/img/migration.png "Migration completed successfully")

## Portable Mode

Portable launch mode is provided for the terminal operation on portable devices and non-system directories, as well as for working in Windows XP. When launched in this mode, the terminal tries to save its data in the installation folder. However, using Portable mode does not guarantee that an operating system will allow storing data in the installation folder (for example, if the terminal is installed in Program Files directory and UAC system is enabled).

The following conditions should be met for working in Portable mode:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Installation directory</span></p></th><th class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Operating system</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Requirements</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">Program Files or another system directory (for example, Windows)</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows XP</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Permission to write to the installation folder</span></p></td></tr><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">Another non-system directory</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows XP</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Permission to write to the installation folder</span></p></td></tr><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">External hard drive, usb flash drive, etc.</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows XP</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The terminal will always be launched in Portable mode.</span></p></td></tr><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">Program Files or another system directory (for example, Windows)</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows Vista\Windows 7</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Launching the terminal as administrator and disabled UAC</span></p></td></tr><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">Another non-system directory</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows Vista\Windows 7</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Permission to write to the installation folder</span></p></td></tr><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">External hard drive, usb flash drive, etc.</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows Vista\Windows 7</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The terminal will always be launched in Portable mode.</span></p></td></tr><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">Program Files or another system directory (for example, Windows)</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows 8 and higher</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">It is impossible to use Portable mode, as UAC system cannot be disabled</span></p></td></tr><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">Another non-system directory</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows 8 and higher</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Permission to write to the installation folder</span></p></td></tr><tr class="table"><td class="table" style="width:404px;"><p class="p_fortable"><span class="f_fortable">External hard drive, usb flash drive, etc.</span></p></td><td class="table" style="width:179px;"><p class="p_fortable"><span class="f_fortable">Windows 8 and higher</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The terminal will always be launched in Portable mode.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">It is not recommended to use Portable mode in case you use Windows Vista or higher, and the terminal is installed in Program Files. This mode is provided for the terminal operation on portable devices and Windows XP.</span></li><li class="p_tableatten"><span class="f_tableatten">If you have updated the terminal and all the data has been copied to a separate user data folder, it is also not recommended to switch to Portable mode.</span></li><li class="p_tableatten"><span class="f_tableatten">You should manually copy the data to the installation folder in order to use Portable mode after copying the data in the user data folder. Launching the terminal in Portable mode does not copy the data from the data folder to the installation one.</span></li></ul></td></tr></tbody></table>

In order to launch the terminal in Portable mode, use "/portable" key. For more convenience, you can create an additional terminal launch shortcut with the appropriate name on your desktop and add the key directly to the shortcut:

![Launching MetaTrader 4 in Portable mode](/en/docs/mt4/terminal/img/terminal_portable.png "Launching MetaTrader 4 in Portable mode")

[Install on Linux](/en/docs/mt4/terminal/userguide/install_linux)

[Opening of Accounts](/en/docs/mt4/terminal/userguide/open_an_account)