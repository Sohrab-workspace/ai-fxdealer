# Status Bar

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/interface/status_bar

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
            -   [Main Menu](/en/docs/mt5/platform/administrator/interface/main_menu)
            -   [Toolbar](/en/docs/mt5/platform/administrator/interface/toolbar)
            -   [Status Bar](/en/docs/mt5/platform/administrator/interface/status_bar)
            -   [Search](/en/docs/mt5/platform/administrator/interface/search)
            -   [Hot Keys](/en/docs/mt5/platform/administrator/interface/hotkeys)
            -   [Toolbox](/en/docs/mt5/platform/administrator/interface/toolbox)
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

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[User Interface](/en/docs/mt5/platform/administrator/interface)Status Bar

# Status Bar

Status bar is located in the lower part of the administrator terminal. It contains tips of program commands, the connection status and the amount of sent and received data:

![Status Bar](/en/docs/mt5/platform/img/status_bar.png "Status Bar")

The following information is shown here from left to right:

-   Command hints;
-   Status of connection to the trade server. Icon ![Connected](/en/docs/mt5/platform/img/status_bar_connected.png "Connected") means that the terminal is currently connected to the server. If connection to the terminal is not established, icon ![Not connected](/en/docs/mt5/platform/img/status_bar_disconnected.png "Not connected"). Hover over the icon to view additional connection details: ping to the trade server and packet loss. These variables measure connection quality between the terminal and the server.
-   Amount of incoming and outgoing traffic for the current session.

The status bar can be disabled by removing the check mark at the corresponding item of the ["View"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_view) menu.

## Access point changing menu [#](status_bar#access_servers)

The administrator terminal is connected to the trade server through [access servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server). When connecting, the best access point is selected (the lowest load to server, the best quality of connection to it). The best access points are automatically checked every three hours of operation.

You can also switch between access servers using the menu that is opened by clicking on the connection status or traffic data in the status bar:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Menu</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Commands</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><img class="help" alt="Access point changing menu" title="Access point changing menu" width="159" height="103" src="/en/docs/mt5/platform/img/status_bar_menu.png"></p></td><td class="table"><ul><li class="p_fortable"><img class="help" alt="Connect" title="Connect" width="17" height="9" src="/en/docs/mt5/platform/img/connect_button.png"><span class="f_fortable" style="font-weight: bold;"> Connect/<img class="help" alt="Disconnect" title="Disconnect" width="17" height="7" src="/en/docs/mt5/platform/img/disconnect_button.png"> Disconnect</span><span class="f_fortable"> — <a href="/en/docs/mt5/platform/administrator/getting_started/server_connect" class="topiclink">connect</a> or disconnect from the server.</span></li><li class="p_fortable"><img class="help" alt="Network Rescan" title="Network Rescan" width="18" height="16" src="/en/docs/mt5/platform/img/network_rescan_icon.png"><span class="f_fortable"> </span><span class="f_fortable" style="font-weight: bold;">Network Rescan</span><span class="f_fortable"> — this command is intended to manually start scanning of access points. If a server with connection quality better than the current by 30% is found, it is automatically switched to.</span></li><li class="p_fortable"><span class="f_fortable" style="font-weight: bold;">List of access servers</span><span class="f_fortable"> — below all the available access servers are displayed. The indicator of the server quality is shown before the name of each access server. In order to switch to one of the access points, click on its name. It should be noted that in the next scanning of the network, the best server will be automatically choose.</span></li></ul></td></tr></tbody></table>

[Setup](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_settings)

[Search](/en/docs/mt5/platform/administrator/interface/search)