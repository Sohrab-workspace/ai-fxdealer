# Server

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/setup_server

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
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
            -   [Server](/en/docs/mt4/terminal/setup/setup_server)
            -   [Charts](/en/docs/mt4/terminal/setup/setup_charts)
            -   [Objects](/en/docs/mt4/terminal/setup/setup_objects)
            -   [Trade](/en/docs/mt4/terminal/setup/setup_trade)
            -   [Expert Advisors](/en/docs/mt4/terminal/setup/setup_experts)
            -   [Notifications](/en/docs/mt4/terminal/setup/settings_notifications)
            -   [Email](/en/docs/mt4/terminal/setup/setup_email)
            -   [FTP](/en/docs/mt4/terminal/setup/setup_publisher)
            -   [Events](/en/docs/mt4/terminal/setup/setup_events)
            -   [Community](/en/docs/mt4/terminal/setup/settings_mql5community)
            -   [Signals](/en/docs/mt4/terminal/setup/settings_signals)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)Server

# Server

This tab contains the most important settings changes in which can cause serious troubles in the terminal operation as far as the full disconnection. The client terminal is initially configured in the way providing normal, trouble-free operation. Thus, it is highly recommended not to change any parameters in this window needlessly.

![options_server](/en/docs/mt4/terminal/img/options_server.png)

In the "Settings — Server" window, it is possible:

-   [to choose a server to connect to](/en/docs/mt4/terminal/setup/setup_server#server);
-   [to configure the proxy server](/en/docs/mt4/terminal/setup/setup_server#proxy);
-   [to specify and change passwords](/en/docs/mt4/terminal/setup/setup_server#passwords);
-   [to enable export of quotes through DDE protocol](/en/docs/mt4/terminal/setup/setup_server#dde);
-   [to enable income of news](/en/docs/mt4/terminal/setup/setup_server#news).

## Server [#](setup_server#server)

Practically, the entire work of the Client Terminal is based on data (news and quotes) continuously incoming from the server. If a client terminal does not receive quotes, it is impossible to trade with it. In such a mode, the terminal allows just to analyze the existing data with indicators and line studies and test expert advisors. This situation can emerge for a number of reasons, one of them is incorrect setting of the server connection.

For connecting the client terminal to the server, the exact server IP address (or domain name) and port must be known. After the program has been installed, all these data will be specified, there is usually no need to change them. However, if there is a need to connect to another server, its address and port must be given in the "Server" field. The data must be given in the following format: "\[internet address of the server\] : \[port number\]" (without spaces). For example: "192.168.0.1:443", where "192.168.0.1" is the server address, and "443" is the port number. After the data have been input, the "OK" button must be pressed.

The newly set server address and port number are stored on the hard disk. These data do not influence the operation of the client terminal until an attempt to open a new account is made. It is this moment when the terminal starts using of these given address and port number. The new server address will be added to the list of servers during [account registration](/en/docs/mt4/terminal/userguide/open_an_account), and it can be chosen. If connection to the server succeeds, the new account will be opened. Otherwise, it is recommended to check all settings and try to reconnect.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Incorrect connection setting is not the only reason for which a new account cannot be opened.</span></p></td></tr></tbody></table>

## Proxy Server [#](setup_server#proxy)

Connection to internet through a proxy server can be another reason for which the server cannot be connected to. A proxy server is an intermediate between the trader's computer and the trading server. It is mostly used by internet providers or by local networks. If a connection problem occurs, you should turn to your systems administrator or to the internet provider. If a proxy is used, the terminal must be set up in a corresponding way. Setting of "Enable proxy server" checkbox will enable proxy server support and activate the "Proxy..." button. Pressing of this button will open the window where proxy server parameters should be specified (these data can be given by the systems administrator or by internet provider):

![proxy_server](/en/docs/mt4/terminal/img/proxy_server.png)

-   Server — proxy server address and type (HTTP, SOCKS5, or SOCKS4);
-   Login — a user login for access to the proxy server. If login is not needed, this field must remain empty;
-   Password — a password for access to the proxy server. If password is not needed, this field must remain empty.

After the parameters have been specified, it is recommended to press the "Test" button to check how the settings work. If they have been tested successfully, the "OK" button must be pressed in order the settings to be effective. Error message means that the proxy server was set up incorrectly. To find out about the reasons, the system administrator or internet provider must be contacted again.

## Account and Login [#](setup_server#passwords)

Client terminal can connect to the server and work only using an account. There are login (the account number), master and investor passwords in the Client Terminal. To be authorized, one needs an account number and one of two passwords. The master password allows the full access to the account, while the investor one gives only a limited access. Being authorized with the investor password gives the right to look through charts, perform technical analysis and test expert advisors, but not trade. Investor password is a convenient tool showing the trading process at this given account.

After the account has been opened and if "Keep personal settings and data at startup" option is enabled, its data (number, master and investor passwords) will be stored at the hard disk. At the program restart, these data will be used to connect the account automatically. If the option is disabled, a password must be entered manually at each restart of the terminal. Also if you disable this option, the information about previously used account and saved passwords will be deleted upon the next restart of the terminal.

The current account number and password are specified in the fields of "Login" and "Password". Data of another account can be input in these fields, then, after the "OK" button has been pressed, the terminal will try to authorize it. If authorization was not successfully completed, the data given should be checked and re-authorized. If this does not help, the Technical Support service should be contacted.

Having pressed the "Change" button, one can specify new passwords in the window appeared. Doing so, one has to know the current password. It can be found in the [message](/en/docs/mt4/terminal/overview/terminal/terminal_mailbox) sent from the server after [registration of a demo account](/en/docs/mt4/terminal/userguide/open_an_account). The new password is input in the corresponding field. If the "Change investor (read only) password" option is enabled, the investor (not master) password will be changed.

![change_password](/en/docs/mt4/terminal/img/change_password.png)

## Data Export through DDE Protocol [#](setup_server#dde)

Quotes delivered to the terminal can be exported to other applications through "DDE" (Dynamic Data Exchange) protocol. To enable export of quotes, the "Enable DDE server" option must be enabled and the "OK" button must be pressed. Data delivery will start immediately. More details about export of quotes can be found in the [corresponding section](/en/docs/mt4/terminal/service/dde).

## News [#](setup_server#news)

Terminal allows to receive financial news promptly. They start to income just after connection to the server. No news issued when the terminal was disconnected will income in it. To enable news delivering, it is necessary to flag "Enable news". In the ["Terminal" window](/en/docs/mt4/terminal/overview/terminal), the ["News" tab](/en/docs/mt4/terminal/overview/terminal/terminal_news) will appear in which news will be delivered as they are issued.

![terminal_news](/en/docs/mt4/terminal/img/terminal_news.png)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If the "Enable news" option is enabled, but no news were issued, the "News" tab will not appear in the "Terminal" window.</span></p></td></tr></tbody></table>

[Client Terminal Settings](/en/docs/mt4/terminal/setup)

[Charts](/en/docs/mt4/terminal/setup/setup_charts)