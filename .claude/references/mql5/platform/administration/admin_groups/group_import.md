# Import of Groups

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/group_import

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
                -   [Group Settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings)
                -   [Group Symbol Settings](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols)
                -   [Commission Settings](/en/docs/mt5/platform/administration/admin_groups/groups_comissions)
                -   [Group Types](/en/docs/mt5/platform/administration/admin_groups/group_types)
                -   [Import of Groups](/en/docs/mt5/platform/administration/admin_groups/group_import)
                -   [Extended Authentication Setup](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication)
                -   [Position Accounting Systems](/en/docs/mt5/platform/administration/admin_groups/group_position)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Groups](/en/docs/mt5/platform/administration/admin_groups)Import of Groups

# Import of Groups

Using the Administrator terminal, you can import groups from other MetaTrader 4 and MetaTrader 5 servers. In order to proceed with the import, select "![Import](/en/docs/mt5/platform/img/import_from_server_icon.png "Import") Import" in the context menu of the ["Groups"](/en/docs/mt5/platform/administration/admin_groups) section.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Groups can be imported only if the administrator is connected to the main trade server.</span></p></td></tr></tbody></table>

![Import of Groups](/en/docs/mt5/platform/img/import_wizard_group.png "Import of Groups")

The first step is to specify the details of the server from which the groups will be imported, as well as details of the account to connect to it:

-   Server Type — select here the type of the server from which groups will be imported: MetaTrader 5 or MetaTrader 4.
-   Server — the IP address and the port number of the server, separated by a colon.
-   Login — the number of the manager account for authentication on the server.
-   Password — the account password for authentication on the server.
-   Use certificate from file — if accounts are imported from a MetaTrader 5 server with the [extended authorization](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization) mode enabled, you will need a confirmed certificate to connect using the above specified account details. If the certificate has previously been installed in the storage of the operating system, it will be automatically recognized by the import system. If the certificate has not been installed, you must enable this option and specify the path to it file manually.

-   Certificate File — click "Browse" and specify the pfx-file of the certificate. The certificate file received in the terminal is saved in /terminal data folder/profiles/server name/certificates/.
-   Certificate Password — [the password](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization#password) of the certificate.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Import in the extended authorization mode is possible only from MetaTrader 5 servers.</span></li><li class="p_tableatten"><span class="f_tableatten">To import groups, you must have a manager account with the <a href="/en/docs/mt5/platform/administration/admin_managers#permissions" class="topiclink">"Configuring Groups"</a> permission on the source server.</span></li></ul></td></tr></tbody></table>

Once all the details are specified, press the "Next" button. In the case of a successful connection to the server, the list of available groups appears in the next window:

![Selecting groups](/en/docs/mt5/platform/img/group_import.png "Selecting groups")

How to select groups:

-   Double click on its icon, and the icon will become bright.
-   Double click on the section icon, in this case all groups from the section are selected.
-   Click on the "Select All" button.

Here you can also view [settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings) of groups to import. To do this, double click on their names. To start the import, click the "Done".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">After importing, check the settings of all groups.</span></li><li class="p_tableatten"><span class="f_tableatten">All groups <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#trade_server" class="topiclink">are bound</a> to the main trade server. After importing the binding can be changed.</span></li><li class="p_tableatten"><span class="f_tableatten">Only new groups are imported. Settings of existing groups of the same name are not overwritten.</span></li></ul></td></tr></tbody></table>

## Features of Import from MetaTrader 4

There are some specific features of import from MetaTrader 4 servers:

-   When you import groups from the MetaTrader 4 server, existing settings are converted, and default values are assigned to missing settings.
-   When you import groups from the MetaTrader 4 server, trade settings of symbols for the groups are not imported.
-   Groups from the MetaTrader 4 server are imported into the currently selected groups section. When importing groups from the MetaTrader 5 server, their hierarchy is preserved.

[Group Types](/en/docs/mt5/platform/administration/admin_groups/group_types)

[Extended Authentication Setup](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication)