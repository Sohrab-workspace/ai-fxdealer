# Add or Remove Server

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administered_servers/ug_server_add

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
            -   [Add or Remove Server](/en/docs/mt4/administrator/administered_servers/ug_server_add)
            -   [Login to Server](/en/docs/mt4/administrator/administered_servers/ug_server_login)
            -   [Change Password](/en/docs/mt4/administrator/administered_servers/ug_server_password)
            -   [System Requirements](/en/docs/mt4/administrator/administered_servers/requirements)
            -   [System Preparation](/en/docs/mt4/administrator/administered_servers/installation_preparations)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Managed Servers](/en/docs/mt4/administrator/administered_servers)Add or Remove Server

# Add or Remove Server

The program allows to administer several servers simultaneously. The tree of available servers is located in the left part of the program window. To start administering a server, it is necessary to add a new server to the tree by performing the "File — Add server" menu command or a corresponding context menu command.

![Add Server](/en/docs/mt4/administrator/img/win_server_add.png "Add Server")

-   Server is the IP address or domain name of the desired server and the port number. If the port number has not been indicated, the value of 443 will be input on default;
-   Description is the server description or name (no longer than 128 characters). This information will be shown in the list of servers in the left part of the program window;
-   Login is the administrator's account (login) through which the server is connected. The connection is impossible if such an account is not opened on the server;
-   Password is the administrator's password;
-   Save password helps to save a password.

At this stage, it is not necessary to indicate the login and the password. These data will be requested when administrator's [authorization](/en/docs/mt4/administrator/administered_servers/ug_server_login) is performed.

If there are several servers added, you can move them relative to each other in the tree-structured list. ![Move up](/en/docs/mt4/administrator/img/ic_config_up.png "Move up") and ![Move down](/en/docs/mt4/administrator/img/ic_config_down.png "Move down") buttons of the "Edit" menu and of the toolbar are used for this purpose.

## Remove Server [#](ug_server_add#server_delete)

Any server can be removed from Administrator. The "Server — Remove Server" command or a corresponding context menu command will remove the server. The server can be added to the program again and its administration can be started later.

[Managed Servers](/en/docs/mt4/administrator/administered_servers)

[Login to Server](/en/docs/mt4/administrator/administered_servers/ug_server_login)