# Live Update

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_update

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Live Update

# Live Update

The system of the live update of the trading platform is a reliable and efficient way to deliver the updated versions of all its components. There are three modes of the system operation. You can choose one of them on the [starting page](/en/docs/mt5/platform/administration/admin_start#update) of the server:

-   Disabled — no updates to the platform components are performed, either automatically or manually.
-   Enabled — in this mode the platform components will be [updated automatically](/en/docs/mt5/platform/administration/admin_update#auto) when the final versions of updates are released.
-   Enabled with beta versions — besides the release versions, there are beta versions that are released more often. If this option is enabled, all types of updates will be installed. However, it should be noted that intermediate versions can be unstable, so they should be installed only in extreme cases.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is strongly recommended to use beta updates only in extreme cases and only on demo servers.</span></p></td></tr></tbody></table>

The "Live Update" section contains the list of all updated components of the platform:

![Live Update](/en/docs/mt5/platform/img/admin_live_update.png "Live Update")

Information is represented as a table with the following fields:

-   Component — name of the platform component;
-   Version — current version and build number of the component;
-   Size — size of the component distribution in Kb.

## The Live Update procedure [#](admin_update#auto)

-   On each night of Saturday/Sunday, at [optimization time](/en/docs/mt5/platform/administration/admin_network/network_add_edit#optimization), the [history server](/en/docs/mt5/platform/components/history_server) starts the "mt5srvupdater64.exe" file that connects to the update server and checks the availability of updates of all the platform components;
-   If there are any updates, they are downloaded;
-   Then the history server informs other platform components about the availability of updates;
-   Server components are immediately updated automatically;
-   In terminals, a window appears that offers to [update](/en/docs/mt5/platform/administrator/getting_started/live_update) to the latest version.

The "![Start Live Update](/en/docs/mt5/platform/img/start_live_update_icon.png "Start Live Update") Start Live Update" command in the [Services](/en/docs/mt5/platform/administrator/interface/main_menu/menu_services) menu and in the context menu, allows the manual start of this process.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Terminal updates are cached on <a href="/en/docs/mt5/platform/components/access_server" class="topiclink">access servers</a> to reduce the load on the history server;</span></li><li class="p_tableatten"><span class="f_tableatten">Update files are hidden and protected by digital signatures. They are transferred through a protected channel;</span></li><li class="p_tableatten"><span class="f_tableatten">During unpacking, updates are also checked by the platform components;</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">To check the result of updating, request the entries of the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server" class="topiclink">history server</a> <a href="/en/docs/mt5/platform/administration/admin_network/network_journal#request" class="topiclink">journal</a> by the LiveUpdate type.</span></li></ul></td></tr></tbody></table>

## Update Rollback

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is not recommended to rollback to previous versions unless there is a strong necessity.</span></p></td></tr></tbody></table>

In case there is a need to rollback the trade platform to a previous version after an update, you need to keep several safety measures:

-   Before you start a rollback, make a full backup of the current state of the platform.
-   Considering that some updates are connected with conversion (change of format) of data bases and configuration files, it is prohibited to rollback only executable files of the platform components. A rollback must be made for the entire platform.
-   You should take into consideration, that some updates may introduce some changes into MetaTrader 5 API. Therefore, third-party applications developed using API should be recompiled with their proper versions.

## Context Menu [#](admin_update#context)

The following commands are available in the context menu of this section:

-   ![Start Live Update](/en/docs/mt5/platform/img/start_live_update_icon.png "Start Live Update") Start Live Update — start the updating process;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table with components.

[Mailbox](/en/docs/mt5/platform/administration/mail)

[Migration from MetaTrader 4](/en/docs/mt5/platform/migration)