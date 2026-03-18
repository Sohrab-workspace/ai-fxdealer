# Terminal Settings

> Source: https://support.metaquotes.net/en/docs/mt4/multiterminal/getting_started/ug_setup

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
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
        -   [Getting Started](/en/docs/mt4/multiterminal/getting_started)
            -   [Security System](/en/docs/mt4/multiterminal/getting_started/ug_advanced_security)
            -   [Live Update](/en/docs/mt4/multiterminal/getting_started/ug_liveupdate)
            -   [Terminal Settings](/en/docs/mt4/multiterminal/getting_started/ug_setup)
        -   [Client Accounts](/en/docs/mt4/multiterminal/accounts)
        -   [Trading](/en/docs/mt4/multiterminal/trading)
        -   [Analytics](/en/docs/mt4/multiterminal/analytics)
        -   [User Interface](/en/docs/mt4/multiterminal/user_interface)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MultiTerminal](/en/docs/mt4/multiterminal)[Getting Started](/en/docs/mt4/multiterminal/getting_started)Terminal Settings

# Terminal Settings

MultiTerminal is generally set up in a special window that can be called by the ["Tools — Options"](/en/docs/mt4/multiterminal/user_interface/ug_main_menu) menu command or using accelerating keys Ctrl+O. All settings are grouped according to their tasks and located in the following tabs:

-   [Server](/en/docs/mt4/multiterminal/getting_started/ug_setup#server) — setting up parameters of connection to the server, configuring of the used proxy server and Data Centers, as well as other important settings;
-   [Trade](/en/docs/mt4/multiterminal/getting_started/ug_setup#trade) — parameters of opening new orders by default. They include: financial instrument (symbol), the amount of lots, lots allocation mode, and deviation;
-   [Email](/en/docs/mt4/multiterminal/getting_started/ug_setup#email) — setting up email parameters. If there is a necessity to send messages by email directly from the terminal, the parameters of the mailbox to be used must be set up;
-   [Events](/en/docs/mt4/multiterminal/getting_started/ug_setup#events) — setting up signals informing about system events. Signals informing about connection unavailability, news incomes, and others, simplify the work very much.

## Server [#](ug_setup#server)

Practically, the entire work of the Terminal is based on data (news and quotes) continuously incoming from the server. If a terminal does not receive quotes, it is impossible to trade with it. Server tab contains settings of the server connection.

-   Server  
    It is necessary to select one of available servers from this list.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">MultiTerminal does not allow switching between the servers of different companies, because it is strongly binded to the servers of a certain company.</span></p></td></tr></tbody></table>

-   Proxy Server  
    Connection to internet through a proxy server can be another reason for which the server cannot be connected to. A proxy server is an intermediate between the trader's computer and the trading server. It is mostly used by internet providers or by local networks. If a connection problem occurs, you should turn to your systems administrator or to the internet provider. If a proxy is used, the terminal must be set up in a corresponding way. Setting of "Enable proxy server" checkbox will enable proxy server support and activate the "Proxy..." button. Pressing of this button will open the window where proxy server parameters should be specified (these data can be given by the system administrator or by internet provider):

-   -   Server — proxy server address and type (HTTP, SOCKS5, or SOCKS4);
    -   Login — a user login for access to the proxy server. If login is not needed, this field must remain empty;
    -   Password — a password for access to the proxy server. If password is not needed, this field must remain empty.  
        After the parameters have been specified, it is recommended to press the "Test" button to check how the settings work. If they have been tested successfully, the "OK" button must be pressed in order the settings to be effective. Error message means that the proxy server was set up incorrectly. To find out about the reasons, the system administrator or internet provider must be contacted again.

-   Personal data  
    Terminal is intended to manage a set of client accounts. When [adding accounts](/en/docs/mt4/multiterminal/accounts/ug_accounts) it is necessary to specify login (account number) and password. After an account has been added and if "Keep personal settings and data at startup" option is enabled, its password will be stored at the hard disk. When connecting the account to the server, this password will be used to connect the account automatically. If the option is disabled, a password must be entered manually at each connection of the account. Also, all personal mails, received by the internal mail system, will be deleted if option is disabled.
-   News  
    Terminal allows to receive financial news promptly. They start to income just after connection to the server. No news issued when the terminal is disconnected will income in it. To enable news delivering, it is necessary to flag "Enable news".

## Trade [#](ug_setup#trade)

Settings used for orders opening are grouped in the Trade tab. Parameters input here facilitate opening of orders and cannot cause critical changes in the terminal operation.

-   Symbol by Default  
    The "Symbol by default" option allows to define the symbol value when a trading operation is performed. The "Last used" parameter means that the symbol of the latest trade operation will be set automatically. For the same symbol to be set repeatedly, the "Default" parameter must be enabled, and the necessary symbol must be chosen from the list.
-   Lots by Default  
    In the similar way, the initial amount of lots can be defined ("Lots by default" option): "Last used" is a parameter used in the previous operation, and "by default" is a constant, manually set value.
-   Lots Allocation  
    When placing new orders, it is necessary to specify the total lots allocation for all accounts. The specified total lots will be distributed among accounts according to the specified lots allocation method:

-   -   Predefined volume — it will be necessary to specify manually the lots amount for each order when placing the order, later this predefined volume will apply at placing orders.
    -   Total volume for each order — the total lots will apply at placing each order.
    -   Equal parts — the total lots will be allocated among all orders in equal parts.
    -   By equity ratio — the total lots will be allocated among orders based on the ratio between equities of accounts.
    -   By free margin ratio — the total lots will be allocated among orders on the ratio between free margins of accounts.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><a name="distribution" class="hmanchor"></a><span class="f_tableatten">Attention:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">The "Lots Allocation" option allows defining of the method to allocate lots among accounts at placing orders: "the last used value" — parameter used in the preceding operation, or "by default" — lots allocation method defined manually.</span></li><li class="p_tableatten"><span class="f_tableatten">When the total volume is allocated between orders on accounts with different deposit currencies based on equity ratio or free margin ratio, the equity or free margin are adduced to the Summary Currency that can be chosen in the context menus of the <a href="/en/docs/mt4/multiterminal/accounts/ug_account_connect" class="topiclink">Accounts</a> panel and of the <a href="/en/docs/mt4/multiterminal/accounts/ug_account_orders" class="topiclink">Orders</a> or <a href="/en/docs/mt4/multiterminal/accounts/ug_account_history" class="topiclink">History</a> tabs.</span></li></ul></td></tr></tbody></table>

-   Deviation  
    The symbol price can change within the ordering time. As a result, the price of the prepared order will not correspond with the market one, and position will not be opened. The "Deviation" option helps to avoid this. Maximum permissible deviation from the value given in the order can be specified in this field. If prices do not correspond, the program will modify the order by itself what allows to open a new position.

## Email [#](ug_setup#email)

In the Email tab, the electronic mailbox is set up. Later on, these settings will be used to send message by a triggered [alert](/en/docs/mt4/multiterminal/analytics/ug_alerts). To start setting up of e-mail, the "Enable" must be enabled and the following fields must be filled out:

-   SMTP server — address of the SMTP server used and port. The given server will be used for sending messages. The entry must have the following format "\[internet address-server address\]:\[port number\]". For example, "192.168.0.1:443", where "192.168.0.1" is the server address, and "443" is the port number;
-   SMTP login — login to authorize at the mail server;
-   SMTP password — authorization password;
-   From — e-mail address from which messages will be sent;
-   To — e-mail address to which messages will be sent.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Only one e-mail address may be specified for either of fields "From" and "To". Several e-mails given with or without separators will not be accepted.</span></p></td></tr></tbody></table>

"Test" sends a test message using the settings specified to test their workability. If it has been tested successfully, the "OK" button must be pressed to apply these settings. If test is unsuccessful, it is recommended to check all settings and resend the test message.

## Events [#](ug_setup#events)

Signals of system events can be set up in the terminal (not to be mixed up with [alerts](/en/docs/mt4/multiterminal/analytics/ug_alerts)). It is a very convenient tool informing about changes in the terminal status. Signals can be set up in this tab. For this to be done, the "Enable" option must be enabled first. At that, a table containing the list of system events and corresponding actions will become active. System events are:

-   Connect — connection to the server. Signal of successful connection to the server;
-   Disconnect — no connection to the server. Signal of interrupted connection to the server;
-   Email Notify — notifying about an incoming mail. If this signal has triggered, it is recommended to check the ["Toolbox — Mailbox"](/en/docs/mt4/multiterminal/user_interface/ug_mailbox) window;
-   Timeout — a certain time range is predefined for performing trade operations. If this range has been exceeded for some reason, the operation will not be performed, and this signal will trigger;
-   OK — trade operation has been successfully performed. No errors occurred during performing of this operation;
-   News — receiving of news. If this signal has triggered, it is recommended to check the ["Toolbox — News"](/en/docs/mt4/multiterminal/analytics/ug_news) window;
-   Requote — price changed during preparation of a trade operation.

If there is a need to disable any of the signals, it is necessary to double-click on its name or icon with the left mouse button. Another double click will activate it again. After the signal has triggered, the file specified in the "Action" field of the corresponding event will run. A double click on the file name allows to change the file. After double-clicking a pop-up list of available files to be assigned for the event will appear. Selection of any file from this list and further Enter button pressing means that it is assigned to the corresponding event. To confirm all changes made, one has to press the "OK" button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Any file executable in the operation system can be assigned to the event.</span></p></td></tr></tbody></table>

[Live Update](/en/docs/mt4/multiterminal/getting_started/ug_liveupdate)

[Client Accounts](/en/docs/mt4/multiterminal/accounts)