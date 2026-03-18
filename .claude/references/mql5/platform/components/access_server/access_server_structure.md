# Structure of Directories and Files

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/access_server/access_server_structure

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
                -   [Structure of Directories and Files](/en/docs/mt5/platform/components/access_server/access_server_structure)
                -   [Antiflood Control](/en/docs/mt5/platform/components/access_server/access_server_antiflood)
                -   [Priority](/en/docs/mt5/platform/components/access_server/access_server_priority)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
            -   [Old WebTerminal](/en/docs/mt5/platform/components/web_terminal_old)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Access Server](/en/docs/mt5/platform/components/access_server)Structure of Directories and Files

# Structure of Directories and Files

The access server is installed to folder "access\_server". This folder contains the following executable files:

-   mt5srvupdater64.exe — the executable file of the live update system of the access server;
-   mt5access64.exe — the executable file of the access server.

The main directory of the access server contains five folders: bases, config, history, liveupdate, logs.

The bases directory contains the news databases, as well as data on the server performance.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">performance\</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Monthly access server performance databases and data indexes, which are displayed on the <a href="/en/docs/mt5/platform/administration/admin_network/network_monitoring" class="topiclink">Monitoring</a> tab.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">news.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Database of news sent to clients.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">news.idx</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The index file of the news database.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">performance.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Data about the access server performance that are displayed on the <a href="/en/docs/mt5/platform/administration/admin_network/network_monitoring" class="topiclink">"Monitor"</a> tab are written to this file.</span></p></td></tr></tbody></table>

The config directory contains configuration files:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">server.ini</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Individual settings of the access server.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">servers.ini</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Settings of the internal <a href="/en/docs/mt5/platform/administration/admin_network" class="topiclink">network of servers</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">symbols.ini</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Configurations of <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings" class="topiclink">symbols</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">time.ini</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_time" class="topiclink">Time</a> settings.</span></p></td></tr></tbody></table>

The history directory contains the base of history data by symbols, which was received from the history server:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files and folders</span></p></th><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">[2 chars]\[symbol]\</span></p></td><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">yyyy.hsc</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Minute data for the symbol, divided by years. '2 chars' are the first two characters in the instrument name; 'symbol' is the name of the instrument. Arranging symbol data in different directories reduces the load on the file system and provides faster data operations.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">[2 chars]\[symbol]\</span></p></td><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">yyyy.tkc</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Tick data for the symbol, divided by years. '2 chars' are the first two characters in the instrument name; 'symbol' is the name of the instrument. Arranging symbol data in different directories reduces the load on the file system and provides faster data operations.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">tickers.dat</span></p></td><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Data by tickers.</span></p></td></tr></tbody></table>

The liveupdate directory contains the latest updates of the client, manager and administrator terminals:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mt5adm.build</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Live update of the administrator terminal. The build number is specified after the point.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mt5clw.build</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Live update of the client terminal.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mt5ckwide.build</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Live Update of MetaEditor.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mt5clwmql.build</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Live Update of the MQL5 compiler.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mt5man.build</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Live update of the manager terminal.</span></p></td></tr></tbody></table>

The logs directory keeps files of the access server operation journal, as well crash logs:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Files and folders</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Crash\crash.log.*</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The /crash directory contains server crash files. These files are automatically sent to the software developing company for detecting reasons of the crash and eliminating them.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">yyyymmdd.log</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/platform/administration/admin_network/network_journal" class="topiclink">Journal</a> files that contain all the information about events that occur on the access server. Server logs are stored in separate files for each working day. Here yyyy — year, mm — month, dd — day.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mt5srvupdater.log</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Journal files of the platform <a href="/en/docs/mt5/platform/administration/admin_update" class="topiclink">updates</a>.</span></p></td></tr></tbody></table>

[Access Server](/en/docs/mt5/platform/components/access_server)

[Antiflood Control](/en/docs/mt5/platform/components/access_server/access_server_antiflood)