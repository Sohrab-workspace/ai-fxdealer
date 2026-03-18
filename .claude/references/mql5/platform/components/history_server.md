# History Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/history_server

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)History Server

# History Server

The history server processes price and news data. This server performs the following functions:

-   Receiving and filtering price and news data from gateways and datafeeds.
-   Packing price and news data.
-   Storing and providing price history in the form of 1-minute bars and ticks to other components of the platform.
-   Storing and providing the news thread.
-   Receiving, checking and distributing [Live Updates](/en/docs/mt5/platform/administration/admin_update) among the MetaTrader 5 platform components.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For server configuration details, see the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit" class="topiclink">"Network cluster"</a> section.</span></p></td></tr></tbody></table>

[Priority](/en/docs/mt5/platform/components/access_server/access_server_priority)

[Structure of Directories and Files](/en/docs/mt5/platform/components/history_server/history_server_structure)