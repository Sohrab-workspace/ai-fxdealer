# Importing clients from the MetaTrader 5 server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/clients/clients_import_mt5

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
                -   [Import of Clients from MetaTrader 5](/en/docs/mt5/platform/administration/clients/clients_import_mt5)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Clients](/en/docs/mt5/platform/administration/clients)Import of Clients from MetaTrader 5

# Importing clients from the MetaTrader 5 server

You can easily import your client database from one MetaTrader 5 sever to another. You will need administrator accounts having access to clients on these two servers.

Open the clients section and click "Import from server":

![Start import from the context menu of the Clients section](/en/docs/mt5/platform/img/clients_import_mt5_login.png "Start import from the context menu of the Clients section")

Specify connection parameters:

-   Server — the IP address and port of the MetaTrader 5 server separated by a colon.
-   Login — the number of the manager account for authentication on the server.
-   Password — the account password for authentication on the server.
-   Use certificate from file — [advanced authentication](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization) can be enabled for the manager account on the source server, from which accounts are imported. A certificate is required in this case. If the certificate has previously been installed in the storage of the operating system, it will be automatically recognized by the import system. If the certificate has not been installed, enable this option and specify the path to the file manually.

-   Certificate File — click "Browse" and specify the pfx-file of the certificate. The certificate file received in the terminal is saved in /terminal data folder/profiles/server name/certificates/.
-   Certificate Password — [the password](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization#password) of the certificate.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">To import accounts, you will need an administrator account with <a href="/en/docs/mt5/platform/administration/admin_managers#clients" class="topiclink">client access permissions</a> on the source server.</span></p></td></tr></tbody></table>

## Requesting accounts

Next, specify a string to request clients from an external server. Records are filtered by the "[Preferred group](/en/docs/mt5/platform/administration/clients#preferred_group)" field. The default request is "!demo\*,!manager\*,!coverage\*,!contest\*,\*". It allows selecting all clients except those from demo and manager accounts, as well as coverage and contest groups.

After the request, the list will display the clients to be imported. Double click on a client to view how it will look like after import. This will open a standard account viewing window.

![The list of clients received from the MetaTrader 4 server](/en/docs/mt5/platform/img/clients_import_mt5_request.png "The list of clients received from the MetaTrader 4 server")

You can disable import of individual clients from the list. To do this, click on the icon at the beginning of the account row, and then it will change to![No import](/en/docs/mt5/platform/img/access_block_icon.png "No import"). You can also select or deselect all clients by using the corresponding option below the list.

If you wish to additionally import client [documents](/en/docs/mt5/platform/administration/clients#documents) and [comments](/en/docs/mt5/platform/administration/clients#comments), select the appropriate options.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the IDs of imported clients match the IDs of existing clients, new IDs will be assigned.</span></p></td></tr></tbody></table>

## Result of Import

The total number and the number of imported clients will be shown on the last step:

![Result of Import](/en/docs/mt5/platform/img/clients_import_mt5_finish.png "Result of Import")

Import details are also available in the [trade server journal](/en/docs/mt5/platform/administration/admin_network/network_journal).

[Clients](/en/docs/mt5/platform/administration/clients)

[Accounts](/en/docs/mt5/platform/administration/admin_accounts)