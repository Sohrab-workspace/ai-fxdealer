# Activation

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/server_commands/activation

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
            -   [Server and Data Feeds Restart](/en/docs/mt4/administrator/server_commands/ug_server_restart)
            -   [Synchronization of Charts](/en/docs/mt4/administrator/server_commands/ug_sync)
            -   [Starting LiveUpdate](/en/docs/mt4/administrator/server_commands/ug_liveupdate)
            -   [Activation](/en/docs/mt4/administrator/server_commands/activation)
        -   [Administration](/en/docs/mt4/administrator/administration)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Server Administration Commands](/en/docs/mt4/administrator/server_commands)Activation

# Activation

A license provided for installation of the platform is non-activated and has a limitation: no more than 100 users can be created. If the current number of users exceeds this amount, new accounts cannot be created.

If the server license is not activated, the "Server" field on the "Common" displays "not activated":

![The server license is not activated](/en/docs/mt4/administrator/img/license_not_activated.png "The server license is not activated")

To activate the license, execute the "![Activate](/en/docs/mt4/administrator/img/activate_button.png "Activate") Activate" command in the "[Services"](/en/docs/mt4/administrator/getting_started/ug_main_menu) menu. After typing a confirmation code the activation process starts. The following actions are performed during activation:

-   A request is sent to the update server of the developer company;
-   In case of successful license checking, a new activated license is generated; it is bound to the configuration of server where the platform is installed;
-   Activated license is sent back to the trade server;

-   The server is restarted.

If the license is activated, the "Server" field on the "Common" displays its expiration date - "expires at ...":

![The license is acitvated](/en/docs/mt4/administrator/img/license_activated.png "The license is acitvated")

## Reactivation

A reactivation of the license is required in the following situations:

-   hardware changes on the server where the platform is installed;
-   re-installation of the operating system;
-   switching to a reserve server.

[Starting LiveUpdate](/en/docs/mt4/administrator/server_commands/ug_liveupdate)

[Administration](/en/docs/mt4/administrator/administration)