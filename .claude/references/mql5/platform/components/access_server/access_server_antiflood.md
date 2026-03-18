# Antiflood Control

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/access_server/access_server_antiflood

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
                -   [Structure of Directories and Files](/en/docs/mt5/platform/components/access_server/access_server_structure)
                -   [Antiflood Control](/en/docs/mt5/platform/components/access_server/access_server_antiflood)
                -   [Priority](/en/docs/mt5/platform/components/access_server/access_server_priority)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
            -   [Old WebTerminal](/en/docs/mt5/platform/components/web_terminal_old)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Access Server](/en/docs/mt5/platform/components/access_server)Antiflood Control

# Antiflood Control

The antiflood control system works on [access servers](/en/docs/mt5/platform/components/access_server). It allows protecting the trading platform from external harmful attacks. This protection system collects the database of users who send incorrect requests to the server (e.g. attempt to authorize with an incorrect login or password), as well as users who send too often requests.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Antiflood control works with all types of connections to the server including manager ones (via the manager terminal and Manager API).</span></p></td></tr></tbody></table>

The number of connections and incorrect request per time unit can be set up on the ["Access"](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#antiflood) tab of the access server:

!["Access" tab](/en/docs/mt5/platform/img/network_add_access.png ""Access" tab")

## System of Operation

The antiflood control system monitors user activity. Users are identified by their IP addresses as well as by the ID linked to their computers and operating systems. The following two activity types are controlled:

-   The total number of connections from one user  
    The system tracks if a user creates too many connections. When a user connects to the server, their connection counter is incremented by one. If the next connection occurs in less than 3 seconds, the counter is incremented. If the specified time interval is exceeded, the counter is reset. When the counter reaches the number specified in the "Connections" field, the user is blocked for 5 minutes. The blocking period increases if the connections limit is reached again. The maximum blocking period is one hour.
-   Number of invalid packets from one user  
    The system blocks brute-force attacks by analyzing authentication errors, which imply multiple login attempts with incorrect data. Also, the system detects garbage flood packets, which can be sent to the server by third-party utilities in an effort to reduce the server performance (i.e. a DoS attack). When a user sends an invalid packet to the server, the user's error counter is incremented by one. If the next invalid packet is sent in less than 5 minutes, the counter is incremented. If the specified time interval is exceeded, the counter is reset. When the counter reaches the number specified in the "Errors" field, the user is blocked for 5 minutes. The blocking period increases if the connections limit is reached again. The maximum blocking period is one hour.

The antiflood mechanism functions independently on each access server. Each server tracks its own connection and error counters and applies the appropriate restrictions when required.

The following records appear in the access server operation [Journal](/en/docs/mt5/platform/administration/admin_network/network_journal) when a user is blocked:

-   IP is blocked after N connections \[intruder\] — a user is blocked by IP if the number of connections is exceeded;
-   CID is blocked after N errors \[intruder\] — a user is blocked by CID (computer ID) if the number of errors is exceeded.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">It is strongly recommended to keep the antiflood control system enabled.</span></li><li class="p_tableatten"><span class="f_tableatten">IP addresses added to the "permit always" list in the <a href="/en/docs/mt5/platform/administration/security/admin_access" class="topiclink">corresponding section</a>, are not checked by the antiflood control system.</span></li></ul></td></tr></tbody></table>

## Retrieve IP address from X-Forwarded-For

Clients can connect to the platform through public services from various proxy servers. This may happen, for example, if you use an [Anti DDoS system](/en/docs/mt5/platform/administration/security/network_anti_ddos), such as Cloudflare. In this case, the proxy server address will be displayed for the client's IP address in [account details](/en/docs/mt5/platform/administration/admin_accounts/account_edit) and [logs](/en/docs/mt5/platform/administration/admin_network/network_journal). The same address will be used for anti-flood control system checks. To avoid this and provide real data, you can add proxy server addresses to the [firewall](/en/docs/mt5/platform/administration/security/admin_access) whitelist (the "always allow" rule). In this case, the access server will try to retrieve the user's real IP address from the X-Forwarded-For header provided by the proxy server upon connection.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Please make sure the IP addresses you are adding to the whitelist belong to trusted services, which may not transmit false addresses in requests.</span></p></td></tr></tbody></table>

[Structure of Directories and Files](/en/docs/mt5/platform/components/access_server/access_server_structure)

[Priority](/en/docs/mt5/platform/components/access_server/access_server_priority)