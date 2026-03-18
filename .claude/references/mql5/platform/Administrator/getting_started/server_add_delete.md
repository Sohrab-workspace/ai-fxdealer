# Add or Remove Servers

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/server_add_delete

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
            -   [Install Terminal](/en/docs/mt5/platform/administrator/getting_started/administrator_installation)
            -   [Start Terminal](/en/docs/mt5/platform/administrator/getting_started/launch)
            -   [Structure of Directories and Files](/en/docs/mt5/platform/administrator/getting_started/structure)
            -   [Add or Remove Servers](/en/docs/mt5/platform/administrator/getting_started/server_add_delete)
            -   [Connect to Server](/en/docs/mt5/platform/administrator/getting_started/server_connect)
            -   [Change Password](/en/docs/mt5/platform/administrator/getting_started/change_password)
            -   [Live Update](/en/docs/mt5/platform/administrator/getting_started/live_update)
            -   [Uninstall Terminal](/en/docs/mt5/platform/administrator/getting_started/deinstallation)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
        -   [Terminal Settings](/en/docs/mt5/platform/administrator/settings)
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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Getting Started](/en/docs/mt5/platform/administrator/getting_started)Add or Remove Servers

# Add or Remove Servers

The administrator terminal allows managing operation of several servers. Servers and commands for working with them are located in the form of a tree in the left part of the terminal.

## Adding a Server

To add a server, one should execute the  "![Add Server](/en/docs/mt5/platform/img/add_server_button.png "Add Server") Add Server" command in the ["File"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_file#add) menu or use the similar context menu command of the left part of the terminal. After that the following window will appear:

![Server](/en/docs/mt5/platform/img/add_server.png "Server")

In this window the following fields should be filled out:

-   Server — IP-address or domain name of the necessary server and its port number. If port number is not specified then port 443 is used on default;
-   Description — description or name of the server (not more than 128 symbols). This information will be displayed in the tree of servers in the left part of the terminal window;
-   Login — administrator account (login), using which connection to the server will be performed. If such an account has not been created on the server, connection is impossible;
-   Password — administrator password;
-   Save password — save password between program restarts.

It is not necessary to specify "Login" and "Password" when adding a server. These details will be requested when [connecting](/en/docs/mt5/platform/administrator/getting_started/server_connect) to it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Password to the server must be no less than six symbols long and contain at least two of three types of symbols (uppercase letters, lowercase letters and digits).</span></p></td></tr></tbody></table>

If there are several servers added to the administrator terminal, they can be moved relatively to each other in the tree-like list. To do that, one should use the ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") and ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") buttons of the ["Edit"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu.

## Deleting a Server

In order to delete a server, execute the "![Delete Server](/en/docs/mt5/platform/img/delete_server_button.png "Delete Server") Delete Server" command in the ["File"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_file#delete) menu or the similar context menu command in the left part of the administrator terminal. Further you can add this server again and start administering it.

[Structure of Directories and Files](/en/docs/mt5/platform/administrator/getting_started/structure)

[Connect to Server](/en/docs/mt5/platform/administrator/getting_started/server_connect)