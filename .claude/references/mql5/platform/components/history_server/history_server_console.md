# Console Commands

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/history_server/history_server_console

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
                -   [Structure of Directories and Files](/en/docs/mt5/platform/components/history_server/history_server_structure)
                -   [Interaction with Quote Providers](/en/docs/mt5/platform/components/history_server/history_server_datafeeds)
                -   [Quotes Filtration](/en/docs/mt5/platform/components/history_server/quotes_filtration)
                -   [Console Commands](/en/docs/mt5/platform/components/history_server/history_server_console)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[History Server](/en/docs/mt5/platform/components/history_server)Console Commands

# Console Commands

The history server component [mt5srvupdater64.exe](/en/docs/mt5/platform/components/history_server/history_server_structure) has several console commands that allow updating and activating the platform if servers are unavailable for connection via the administrator terminal.

In order to execute these commands, start file mt5srvupdater64.exe from the root directory of the history server, specifying corresponding keys:

-   /update — download updated files of all the system components, if there are such files, from the developer's update server;
-   /upgrade — install [updates](/en/docs/mt5/platform/administration/admin_update) of all the platform components. This command can be executed only of the updates have been downloaded;
-   /activate — [activate](/en/docs/mt5/platform/platform_installation/activation) the platform.

For example, after you execute command "mt5srvupdater64.exe /update /upgrade", the platform updates will be downloaded and installed.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The protocol of the update process is kept in </span><span class="f_tableatten" style="font-style: italic;"><a href="/en/docs/mt5/platform/components/history_server/history_server_structure#updater" class="topiclink">mt5srvupdater.txt</a></span><span class="f_tableatten">, located in folder </span><span class="f_tableatten" style="font-style: italic;">/history/logs/</span><span class="f_tableatten">.</span></p></td></tr></tbody></table>

[Quotes Filtration](/en/docs/mt5/platform/components/history_server/quotes_filtration)

[Backup Server](/en/docs/mt5/platform/components/backup_server)