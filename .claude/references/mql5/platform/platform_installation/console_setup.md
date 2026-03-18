# Console Setup

> Source: https://support.metaquotes.net/en/docs/mt5/platform/platform_installation/console_setup

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
            -   [System Requirements](/en/docs/mt5/platform/platform_installation/requirements)
            -   [System Preparation](/en/docs/mt5/platform/platform_installation/installation_preparations)
            -   [Installation](/en/docs/mt5/platform/platform_installation/installation)
            -   [Activation](/en/docs/mt5/platform/platform_installation/activation)
            -   [White Label](/en/docs/mt5/platform/platform_installation/white_label)
            -   [Fast Deployment](/en/docs/mt5/platform/platform_installation/deployer)
            -   [Console Setup](/en/docs/mt5/platform/platform_installation/console_setup)
            -   [Platform Moving](/en/docs/mt5/platform/platform_installation/platform_move)
            -   [Platform Uninstall](/en/docs/mt5/platform/platform_installation/platform_uninstall)
        -   [Platform Components](/en/docs/mt5/platform/components)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Installation](/en/docs/mt5/platform/platform_installation)Console Setup

# Console Setup

Every executable file (\*.exe) of the trading platform servers possesses a certain set of console commands. Using them you can perform common actions with appropriate services in the system, as well set up connection of components when connection via the administrator terminal is impossible.

To start executing console commands, open the "Run" window of the operating system and execute the "cmd" command. In the command line go to the directory where the executable file of one of the servers is located, enter its name and specify one of the console commands. For example:

C:\\MetaTrader 5 Platform\\Access>mt5access.exe /stop

## Common Commands

The following set of console commands perform common actions and is available for executable files of [all servers](/en/docs/mt5/platform/components):

-   /start — start the service that is connected with this executable file of the server;
-   /stop —  stop the service that is connected with this executable file of the server;
-   /restart —  restart the service that is connected with this executable file of the server;
-   /console — start the service in the console mode;
-   /install \[/name:service\_name /display:displayed\_name /description:service\_description\] — install a service associating it with this executable file. For additional parameters you can specify the service name for the operating system, extended (displayed) service name for users, as well its description. If you do not specify any of parameters, the service name will be set by default;
-   /uninstall \[/name:service\_name\] — uninstall a service associated with this executable file, For an additional parameter, you can specify the service name to be uninstalled.
-   /info — show information about the server: internal identifier (ID), own address, address of the main server and binding addresses (for access servers).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Additional parameters are specified without square brackets. For example: /install /name:mt5access /display:Access server</span></p></td></tr></tbody></table>

## Setup of Servers

If incorrect settings were specified during the installation of any of components, and connection to the platform via the administrator terminal is impossible, you can re-configure the components using the console command /config. It can be executed on any server except for the main trade server. This command has the following parameters:

-   /main:address:port (for trade servers) or /main\_trade:address:port (for other servers) — IP address and port of the main trade server, separated by a colon.
-   /own:address:port — IP address and port of the server you are configuring, separated by a colon.
-   /history:address:port — the IP address and port number of the history server. The parameter is only used when configuring access servers. It enables immediate specification of the history server address, without waiting for it from the main server. This improves the speed and reliability server deployment.
-   /id:identifier — the internal identifier of the server you are configuring.
-   /password:password — the internal password of the server you are configuring.

You can specify multiple addresses separated by commas in the 'main', 'own' and 'history' parameters. For example: /main:192.168.0.1:440,\[2a00:1987:1:30::2a\]:440.

These parameters are analogous to those specified in the ["Network"](/en/docs/mt5/platform/administration/admin_network) section in the administrator terminal. After the command execution, the earlier specified parameters for the server will be overwritten.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Example: /config /main:192.168.0.1:440 /own:192.168.0.1:443 /id:3 /password:3jdaLjsQ</span></p></td></tr></tbody></table>

### Setup of Servers in the Graphical Mode

In order to start setting up a server in the graphical mode, you should run its executable file with the /gui key from the command line. For example, mt5access64.exe /gui.

![Setup in the graphical mode](/en/docs/mt5/platform/img/server_config_gui.png "Setup in the graphical mode")

Parameters that are set here are the same as in the console mode:

-   Server IPv4\\IPv6 address — colon separated IP address and port of the configured server;
-   Server ID — the internal identifier of the server you are configuring;
-   Password — the internal password of the server you are configuring;
-   Main Trade server — IP address and port of the main trade server, separated by a colon.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When launching the backup server setup, the Restore command becomes available in the configuration window. It can be used to restore a server that was backed up by the selected server. Find more details about the server recovery <a href="/en/docs/mt5/platform/components/backup_server/backup_server_restore" class="topiclink">here</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">Use only the /gui_main key to configure the main trade server. When using the /gui key, the main server becomes a secondary one.</span></li></ul></td></tr></tbody></table>

### Linking to NUMA Nodes [#](console_setup#numa)

You can link specific servers to the required [NUMA nodes](https://en.wikipedia.org/wiki/Non-uniform_memory_access). How to link:

-   Stop the server.
-   Call the command 'mt5trade64.exe /modify /numa\_node:X' indicating the node number instead of X. Repeat for other servers.
-   Start the server.

## Setup of the Main Trade Server

To configure the main trade server, a separate console command /config\_main with the below parameters is used:

-   /main:address:port — IP address and port of the [main trade server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server), separated by a colon;
-   /access:address:port — IP address and port of an [access server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server), separated by a colon;
-   /history:address:port — IP address and port of a [history server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server), separated by a colon;
-   /backup:address:port — IP address and port of a [backup server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server), separated by a colon;
-   /password:password —  the internal password that will be set to all the above mentioned servers.

In addition, [internal IDs](/en/docs/mt5/platform/administration/admin_network/network_add_edit#identifier) will be automatically assigned to all servers: "1" to the trade server, "2" to the access server, "3" to the history server, and "4" to the backup server.

### Setup of the Main Trade Server in the Graphical Mode

To start setting up a main trade server in the graphical mode, you should start its executable file with the /gui\_main key from the command line. For example, mt5trade64.exe /gui\_main.

![Setup in the Graphical Mode](/en/docs/mt5/platform/img/server_config_gui_main.png "Setup in the Graphical Mode")

The appeared window contains the list of servers which settings are already present at the main trade server. Three commands are provided for managing the servers:

-   Add — add a server configuration;
-   Edit — change configuration of a selected server;
-   Delete — delete configuration of a selected server. When deleting a configuration, the physical deletion of the server form the computer is not performed.

The windows of settings contain the main parameters of servers, that are set through the administrator terminal in the ["Network"](/en/docs/mt5/platform/administration/admin_network/network_add_edit#common) section:

![Settings of Server](/en/docs/mt5/platform/img/server_config_gui_main_settings.png "Settings of Server")

Additional column Used is displayed for the ranges of accounts, orders and deals. It displays the current use of the range.

![The Range of Accounts](/en/docs/mt5/platform/img/server_config_gui_main_used.png "The Range of Accounts")

You can stop using the current range by specifying the last value from Used field in To field. After that, create a new range.

Parameters set when configuring the main trade server are checked for correctness:

-   Adding a duplicate main or history server — there can be only one server of each type in a cluster.
-   Specifying incorrect ranges of logins, orders and deals.
-   Creating more trade servers than allowed by the license. Such servers will not work.
-   Deleting main server (deleting directly or changing its type).
-   Deleting a working trade server.
-   Changing networks settings so that the main server will become inaccessible to the administrator. For example, deleting the last access server.

In all the cases mentioned above the administrator will get the corresponding warning when trying to save the changes.

## Rebinding a Cluster to Another IP Address

When changing an IP address on the server the MetaTrader 5 cluster is installed at, rebinding to a new address is done as follows:

-   Execute /gui\_main command for the main trading server and replace the addresses of all cluster components with new ones.
-   Execute /gui command for the history server and replace the addresses of the history and main servers with new ones.
-   Execute /gui for the access server and replace the addresses of the access and the main servers with new ones.

[Fast Deployment](/en/docs/mt5/platform/platform_installation/deployer)

[Platform Moving](/en/docs/mt5/platform/platform_installation/platform_move)