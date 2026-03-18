# Common

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/settings/settings_common

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
            -   [Common](/en/docs/mt4/administrator/settings/settings_common)
            -   [Support](/en/docs/mt4/administrator/settings/settings_support)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Terminal Settings](/en/docs/mt4/administrator/settings)Common

# Common

The "Common" tab contains the connection settings of the administrator terminal and the settings of receiving news.

![Common](/en/docs/mt4/administrator/img/settings_common.png "Common")

The following options are present here:

-   Server — the name and IP address of an administered server;

-   Login — administrator's account (login). The connection to server is impossible if such account has not been opened on this server;
-   Password — administrator's password;

-   Enable proxy server — enable [connection](/en/docs/mt4/administrator/administered_servers/ug_server_login) to administrated servers through a proxy server. If this option is checked, the "Proxy..." button becomes active. Using it one can set up connection to administered servers through a [proxy server](/en/docs/mt4/administrator/settings/settings_common#proxy).

-   Save Password — permits/prohibits saving the password between program starts.

## Setting Up Connection through Proxy Server [#](settings_common#proxy)

![Proxy Server](/en/docs/mt4/administrator/img/win_server_login_proxy.png "Proxy Server")

In the "Proxy Server" window it is necessary to specify the following parameters:

-   Server — IP address and server port number separated by a colon are specified here. To the right of this field the type of proxy server is selected: HTTP, SOCKS4 or SOCKS5;
-   Login — account to access the proxy server. If login is not needed, the field should be empty
-   Password — password to access the proxy server. If password is not needed, the field should be empty.

In order to verify the correctness of the settings of connection to the proxy server, press the "Test" button. In case of receiving the message that the settings are correct it is necessary to press the "OK" button to save the settings. The error message indicates that the proxy server is set up incorrectly. To find out the reason, contact the system administrator or internet provider.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The proxy server settings affect the connection to all the administered servers in the terminal.</span></p></td></tr></tbody></table>

[Terminal Settings](/en/docs/mt4/administrator/settings)

[Support](/en/docs/mt4/administrator/settings/settings_support)