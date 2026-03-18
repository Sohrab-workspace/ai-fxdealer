# Access Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/access_server

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)Access Server

# Access Server

Access servers are proxy servers and the platform firewalls at the same time. They perform the following functions:

-   Processing of incoming client connections.
-   Packing authorization requests and sending them to the trade server.
-   Checking activity of client connections protecting the trade server from attacks and overload ([antiflood control](/en/docs/mt5/platform/components/access_server/access_server_antiflood)).
-   Saving history data, depth of market and news, and translate them to clients, thus reducing the load to the history server.
-   Cashing and providing [Live Update](/en/docs/mt5/platform/administration/admin_update) to terminals.
-   [Monitoring](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#witness) the operation of the history and trade servers.

The unlimited number of access servers can exist for each trade server. Terminals are switched between them automatically, depending on the [priority](/en/docs/mt5/platform/components/access_server/access_server_priority) settings.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">For server configuration details, see the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit" class="topiclink">"Network cluster"</a> section.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Use the <a href="/en/docs/mt5/platform/administration/admin_network/hosted_access_server" class="topiclink">Access Server hosting from MetaQuotes</a> to quickly and safely deploy an access server in the desired region.</span></li></ul></td></tr></tbody></table>

[Return Errors](/en/docs/mt5/platform/components/trade_server/returned_errors)

[Structure of Directories and Files](/en/docs/mt5/platform/components/access_server/access_server_structure)