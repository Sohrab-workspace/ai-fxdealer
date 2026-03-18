# Network Cluster

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
                -   [Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)
                -   [Hosted Access Servers](/en/docs/mt5/platform/administration/admin_network/hosted_access_server)
                -   [Restarting and Stopping Servers](/en/docs/mt5/platform/administration/admin_network/restart)
                -   [Managing Machines](/en/docs/mt5/platform/administration/admin_network/manage_machines)
                -   [Status](/en/docs/mt5/platform/administration/admin_network/network_status)
                -   [Monitor](/en/docs/mt5/platform/administration/admin_network/network_monitoring)
                -   [Journal](/en/docs/mt5/platform/administration/admin_network/network_journal)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Network cluster

# Network Cluster

This section is intended for managing all the server components of the online trading system and for [monitoring their state](/en/docs/mt5/platform/administration/admin_network/network_monitoring). All the added platform components, such as [access servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server), [history server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server), [backup servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server), etc., are displayed here.

![Network](/en/docs/mt5/platform/img/network.png "Network")

The following information about the platform components is displayed here:

-   Type — type of the server (main trade server, trade server, history server, access server or backup server);
-   Server — name of the server;
-   Address — IP address and port separated by colon;
-   Public Addresses — the list of [public IP addresses](/en/docs/mt5/platform/administration/admin_network/network_add_edit#network);
-   ID — internal [identifier of the server](/en/docs/mt5/platform/administration/admin_network/network_add_edit#identifier) that is used for recognizing it by the other platform components;
-   Connections — number of connections to the server;
-   Base Priority — [priority](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#priority), that is set for the server in its settings;
-   Current Priority — [current priority](/en/docs/mt5/platform/components/access_server/access_server_priority) of the access server;
-   CPU — processor loading (in percentage terms).

To add a new server, one should execute the "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" command in the ["Edit"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit#add) menu or the same command in the [toolbar](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) or in the context menu. To change the settings of a server, it is necessary to select it and press the "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" button or double-click on it with the left mouse button. To delete a server press the "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete" button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The process of adding and editing servers is described in the <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit" class="topiclink">separate section</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">The interaction between the servers inside the platform is described in the <a href="/en/docs/mt5/platform/components" class="topiclink">"Platform components"</a> section.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If a server in the list or in the tree has a red icon, for example <img class="help" alt="Inactive Server" title="Inactive Server" width="11" height="13" src="/en/docs/mt5/platform/img/server_inactive_icon.png">, it means that it is not connected to the main server. The possible reason can be the incorrect authorization details as well as the stopping of the corresponding service in the operating system.</span></li></ul></td></tr></tbody></table>

## Context Menu [#](admin_network#context)

The context menu of this window allows to execute the following commands:

-   ![Restart Server](/en/docs/mt5/platform/img/restart_server_button.png "Restart Server") Restart Server — [restart](/en/docs/mt5/platform/administration/admin_network/restart) a selected server.
-   ![Deploy Server](/en/docs/mt5/platform/img/deploy_icon.png "Deploy Server") Deploy Server — start [deploying](/en/docs/mt5/platform/platform_installation/deployer) a selected server with specified configuration. This command is only available for servers that are not started yet.
-   ![Swtich to backup server](/en/docs/mt5/platform/img/switch_to_bakcup_icon.png "Swtich to backup server") Switch to Backup Server — this procedure allows to make a selected backup server an active trade or history server depending on what type of server is being backed up. At that, the backed up server will become a backup server. This procedure is described in more details in ["Switching to Backup Server"](/en/docs/mt5/platform/components/backup_server/backup_server_switch).
-   ![Restart Data Feeds](/en/docs/mt5/platform/img/restart_datafeeds_button.png "Restart Data Feeds") Restart Data Feeds — restart [data feeds](/en/docs/mt5/platform/administration/admin_feeds/data_feed_restart).
-   ![Restart Gateways](/en/docs/mt5/platform/img/restart_gateways_button.png "Restart Gateways") Restart Gateways — restart [gateways](/en/docs/mt5/platform/administration/admin_gateways).
-   Manage Server Machine — a menu with commands for [managing the computer](/en/docs/mt5/platform/administration/admin_network/manage_machines) on which the platform server is running.
-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — [add](/en/docs/mt5/platform/administration/admin_network/network_add_edit) a new server.
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — [edit](/en/docs/mt5/platform/administration/admin_network/network_add_edit) a selected server.
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected server.
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move a selected server up relatively to the others.
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move a selected server down relatively to the others.
-   Automation triggers — create an [automation](/en/docs/mt5/platform/administration/automation) task for the selected event or edit an existing one. The menu displays only the triggers and tasks associated with the current section.
-   Automation actions — add an automation action to an existing task or create a new task based on the action. The menu displays only the actions associated with the current section.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) network settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) network settings to a file.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window.
-   Auto Arrange — if this option is enabled, the size of columns is selected automatically.
-   Grid — this option shows/hides grid to separate fields of the table of servers.

[Start Page](/en/docs/mt5/platform/administration/admin_start)

[Configuring Servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit)