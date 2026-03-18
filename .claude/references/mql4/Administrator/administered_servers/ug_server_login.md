# Login to Server

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administered_servers/ug_server_login

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Managed Servers](/en/docs/mt4/administrator/administered_servers)Login to Server

# Login to Server

Before starting server administration it is necessary to login to it. The "File — Login to Server" command, the corresponding context menu command, or ![Login to Server](/en/docs/mt4/administrator/img/ic_server_login.png "Login to Server") button of the toolbar will open the "Authorization" window:

![Login to Server](/en/docs/mt4/administrator/img/win_server_login.png "Login to Server")

-   Server is the server address and port;
-   Description is the server description;
-   Login is the administrator's account (login). The connection to server is impossible if such account has not been opened on this server;
-   Password is the administrator's password;
-   Enable proxy server — enable support of connection via proxy server. Pressing of the "Proxy..." button will open the window where proxy server parameters should be specified (these data can be given by the systems administrator or by internet provider):

![Proxy settings](/en/docs/mt4/administrator/img/win_server_login_proxy.png "Proxy settings")

-   -   Server — proxy server address and port and type (HTTP, SOCKS5, or SOCKS4);
    -   Login — a user login for access to the proxy server. If login is not needed, this field must remain empty;
    -   Password — a password for access to the proxy server. If password is not needed, this field must remain empty.

After the parameters have been specified, it is recommended to press the "Test" button to check how the settings work. If they have been tested successfully, the "OK" button must be pressed in order the settings to be effective. Error message means that the proxy server was set up incorrectly. To find out about the reasons, the system administrator or internet provider must be contacted again.

-   Save Password helps to permit/prohibit saving the password.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: Before connecting to the server, it is necessary to <a href="/en/docs/mt4/administrator/administered_servers/ug_server_add" class="topiclink">add</a> it to the tree of servers available for administering.</span></p></td></tr></tbody></table>

After successful authorization, the indicator of connection in the status line will be replaced with "Connected", and three messages will appear in "Journal":

1.  connected means that connection has been successfully established;
2.  login (x.xx, #yyyyyyyy) means that you have been logged in server of x.xx version with #yyyyyyyy session number;
3.  all configurations have been refreshed means that all configurations have been received from the server.

After successful completion of the authorization process, you can start working. If any problems occur during authorization and you do not receive at least one of three messages in Journal, the administration program will disconnect you forcibly from the server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: On server installing, an account of administrator will be created automatically (Login: 1; Password: manager). After the first authorization it is necessary to change the password or to create a new administrator's account and delete the above-mentioned one.</span></p></td></tr></tbody></table>

[Add or Remove Server](/en/docs/mt4/administrator/administered_servers/ug_server_add)

[Change Password](/en/docs/mt4/administrator/administered_servers/ug_server_password)