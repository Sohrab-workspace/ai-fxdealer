# Priority

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/access_server/access_server_priority

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Access Server](/en/docs/mt5/platform/components/access_server)Priority

# Priority

The preference of an access server for client terminals to connect to a trade server is defined by its priority and connection quality. The lower the value if priority is, the more preferable the access server is. A [base priority](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#priority) (from 0 to 15) can be specified in its settings. It defines the server preference if all other conditions are equal. The final analysis of an access server is conducted upon the ping and the current priority, which depends on the basic priority and the number of current connections. Also, the quality of connection to the server is shown in the client, manager and administrator terminals based on the same data:

![The connection quality of an access point](/en/docs/mt5/platform/img/access_server_preference.png "The connection quality of an access point")

The current priority is calculated according to the following formula: Current Priority = (Base Priority + Connections / 1000),

where:

-   Current Priority is the priority at the server current moment;
-   Base Priority is the base priority set in its [parameters](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#priority);
-   Connections — the number of current connections.

Every 1000 client connections increase the current priority of a server by one. The value of the current priority of access servers is available on the ["Network"](/en/docs/mt5/platform/administration/admin_network) tab.

[Antiflood Control](/en/docs/mt5/platform/components/access_server/access_server_antiflood)

[History Server](/en/docs/mt5/platform/components/history_server)