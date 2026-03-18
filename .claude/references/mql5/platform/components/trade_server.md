# Trading Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/trade_server

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
                -   [Structure of Directories and Files](/en/docs/mt5/platform/components/trade_server/trade_server_structure)
                -   [Mail Templates](/en/docs/mt5/platform/components/trade_server/mail_templates)
                -   [Daily Reports](/en/docs/mt5/platform/components/trade_server/daily_reports)
                -   [SendMail Utility](/en/docs/mt5/platform/components/trade_server/sendmail)
                -   [Return Errors](/en/docs/mt5/platform/components/trade_server/returned_errors)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)Trade Server

# Trading Server

The system has two types of trading servers: one main server server and additional ones. The main trading server serves trading operations and manages the entire system configuration.

The trading server performs the following functions:

-   Storing and management of clients' records.
-   Authentication and authorization of client connections.
-   Storing and management of trade records.
-   Check, management and execution of trade requests.
-   Management of the internal mailing system.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">One main trading server and the unlimited number of additional ones can be configured in the system.</span></li><li class="p_tableatten"><span class="f_tableatten">For server configuration details, please see the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit" class="topiclink">"Network cluster"</a> section.</span></li></ul></td></tr></tbody></table>

[Platform Components](/en/docs/mt5/platform/components)

[Structure of Directories and Files](/en/docs/mt5/platform/components/trade_server/trade_server_structure)