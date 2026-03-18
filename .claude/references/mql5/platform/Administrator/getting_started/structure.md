# Structure of Directories and Files

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/structure

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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Getting Started](/en/docs/mt5/platform/administrator/getting_started)Structure of Directories and Files

# Structure of Directories and Files

This section contains the description of directory and file storing structure in the administrator terminal. In the [guest](/en/docs/mt5/platform/administrator/getting_started/launch#guest) terminal start mode storages are divided into those containing changeable and unchangeable files.

## Unchangeable Files

These files are located in /Program Files/MetaTrader 5 Administrator/. They are:

-   MT5Admin.exe — executable file of the administrator terminal;
-   Uninstall.exe — program for [deinstalling](/en/docs/mt5/platform/administrator/getting_started/deinstallation) the administrator terminal;
-   /help/\*.chm — built-in help files of the terminal.

## Changeable Files

The main directory of the terminal contains several folders: config, logs, profiles, roles, templates. The special command "![Open Data Folder](/en/docs/mt5/platform/img/open_data_folder_button.png "Open Data Folder") Open Data Folder" located in the ["File"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_file#terminal_data) of the terminal menu allows quick accessing the location of this data storage.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">All text files are of Unicode format. The corresponding software should be used for their editing.</span></p></td></tr></tbody></table>

The config directory contains the files of terminal settings, including servers added for administration:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:95px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:95px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mt5admin.ini</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Contains <a href="/en/docs/mt5/platform/administrator/settings" class="topiclink">settings</a> of the administrator terminal, all interface parameters of the terminal, last used values of window positions, etc.</span></p></td></tr><tr class="table"><td class="table" style="width:95px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">servers.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Contains parameters of <a href="/en/docs/mt5/platform/administrator/getting_started/server_connect" class="topiclink">connection</a> to the administered servers.</span></p></td></tr></tbody></table>

The logs directory contains log files of terminal operation, as well as crash logs:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:123px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Folders and Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:123px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Crash/crash.log.*</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Directory /crash contains files of terminal crashes. These files are automatically sent to the developer for finding out reasons for the crash and eliminating them.</span></p></td></tr><tr class="table"><td class="table" style="width:123px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">yyyymmdd.log</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_journal" class="topiclink">Log</a> files containing all the information about events occurring in the administrator terminal. Terminal logs are saved in separate files for each working day. Here: yyyy denotes a year, mm — month, dd — day.</span></p></td></tr></tbody></table>

The profiles directory contains databases of the terminal distributed by administered servers and some settings:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:88px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Folders</span></p></th><th class="table" style="width:226px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th><th class="table" style="width:107px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:88px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">certificates<a name="certificates" class="hmanchor"></a></span></p></td><td class="table" style="width:226px;"><p class="p_fortable"><span class="f_fortable">Contains files of certificates.</span></p></td><td class="table" style="width:107px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">*.pfx</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Files of certificates that can be installed to the system storage or e-token for further <a href="/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization" class="topiclink">authorization</a> on the server.</span></p></td></tr><tr class="table"><td class="table" rowspan="2" style="width:88px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">config</span></p></td><td class="table" rowspan="2" style="width:226px;"><p class="p_fortable"><span class="f_fortable">Contains files of settings related to this server.</span></p></td><td class="table" style="width:107px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">performance.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">File that contains the history of server performance displayed at the <a href="/en/docs/mt5/platform/administration/admin_network/network_monitoring" class="topiclink">"Monitor"</a> tab.</span></p></td></tr><tr class="table"><td class="table" style="width:107px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">symbols-*.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">List of <a href="/en/docs/mt5/platform/administration/admin_symbols" class="topiclink">symbols</a> of the server and their settings.</span></p></td></tr><tr class="table"><td class="table" style="width:88px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mail</span></p></td><td class="table" style="width:226px;"><p class="p_fortable"><span class="f_fortable">Contains mail database of the terminal.</span></p></td><td class="table" style="width:107px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mail-*.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Files of <a href="/en/docs/mt5/platform/administration/mail" class="topiclink">mail database</a> separately for each login. The login number is specified after a hyphen in the file name.</span></p></td></tr><tr class="table"><td class="table" style="width:88px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">news</span></p></td><td class="table" style="width:226px;"><p class="p_fortable"><span class="f_fortable">Contains news database of the terminal.</span></p></td><td class="table" style="width:107px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">news-*.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Files of <a href="/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news" class="topiclink">news database</a> separately for each login. The login is specified after a hyphen in the file name.</span></p></td></tr></tbody></table>

The roles folder contains sets of permissions for manager accounts:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:65px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">*.rol</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">These files contain the sets of settings of permission for the <a href="/en/docs/mt5/platform/administration/admin_managers#permissions" class="topiclink">accounts of managers</a>.</span></p></td></tr></tbody></table>

The templates directory contains templates of news and messages for sending:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Folders</span></p></th><th class="table" style="width:226px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th><th class="table" style="width:108px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mail<a name="mail_templates" class="hmanchor"></a></span></p></td><td class="table" style="width:226px;"><p class="p_fortable"><span class="f_fortable">Contains mail templates.</span></p></td><td class="table" style="width:108px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">*.htm</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">HTM-files of <a href="/en/docs/mt5/platform/administration/mail#templates" class="topiclink">mail templates</a> saved using the corresponding command in the window of message writing.</span></p></td></tr><tr class="table"><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">news<a name="news_templates" class="hmanchor"></a></span></p></td><td class="table" style="width:226px;"><p class="p_fortable"><span class="f_fortable">Contains news templates.</span></p></td><td class="table" style="width:108px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">*.htm</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">HTM-files of <a href="/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news#templates" class="topiclink">news templates</a> saved using the corresponding command in the window of news sending.</span></p></td></tr></tbody></table>

## Database Security

All terminal databases, including saved accounts (servers.dat) and mail data, are encrypted and protected against use in other platforms. The databases are bound to the operating system user account and the specific hardware configuration of the computer. If an attempt is made to transfer and open them on another machine, they will be automatically destroyed.

[Start Terminal](/en/docs/mt5/platform/administrator/getting_started/launch)

[Add or Remove Servers](/en/docs/mt5/platform/administrator/getting_started/server_add_delete)