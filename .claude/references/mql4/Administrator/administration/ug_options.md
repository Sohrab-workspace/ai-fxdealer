# Common

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_options

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
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Common

# Common

The "Common" section is intended for the administration of common settings:

![Common Settings](/en/docs/mt4/administrator/img/br_common.png "Common Settings")

-   Server is the read-only information field that contains the full name of a company that owns the server, its version, build and the release date of the server. It is recommended to specify the value of this filed when applying to the support service in order to get a quicker answers to questions regarding the server operation. The license expiration date is also indicated here;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If "not activated" is displayed in this field, it means that the license of the trade platform is not activated. You should <a href="/en/docs/mt4/administrator/server_commands/activation" class="topiclink">activate</a> it.</span></p></td></tr></tbody></table>

-   Name is the visual name of the server to be seen by clients. The name of the server consists of two parts: the company name and the specific server name, the latter one given in this field. For example, the full name of the server of MetaQuotes Software named Demo Server will appear as MetaQuotes Software: Demo Server;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention! It is strongly recommended to give a unique name no more than 12 characters long to each server (the limitation in length is caused by usability of the server name displaying in the client terminal).</span></p></td></tr></tbody></table>

-   IP Address is the IP address from which the server will operate. When several IP addresses are available on the server, one can indicate a specific address or allow to use any address available;
-   Communication port is a server port for communication. This port must be indicated when logging in to the server. Any port may be indicated. Port 443 is used by it is (HTTPS port) usually permitted for use with a proxy server in local, corporate networks;
-   Time of demo is the timeout for deleting demo accounts. The accounts which have never been used for logging in to the server within the time period indicated will be deleted automatically (this applies to the accounts from \*demo\* groups);
-   Demo accounts is the type of demo accounts usage: demo accounts prohibited, prolong demo accounts from the last login, demo accounts with fixed period;
-   Account Allocation URL is the address a client is [redirected](/en/docs/mt4/administrator/administration/ug_accounts/account_allocation_url) to when opening an account from the client terminal. The link address must start with "https://" or "http://".
-   Time zone is the trade server time zone (for example, GMT+2);
-   Daylight Saving Time correction helps to permit/prohibit summer time correction;
-   End of day time means the time when the trading day ends. This is the time point when reports are generated and rollovers are added on. During end of day operations all trade operations (including balance operations and operations performed by manager accounts) on the server are disabled; an attempt to perform a trade operation will result in "Market is closed" error in the journal;
-   Rollover mode helps to close position at the end of the working day and to open a new one. "Normal" means that rollovers are added on, and all open positions remain open. "Reopen by close price" means that opened position will be forcibly closed at rollover by close price, and another one will be opened instead of it next trade day with swaps being added on the close price. "Reopen by bid" means that opened position will be forcibly closed at rollover by bid price, and another one will be opened instead of it next trade day with swaps being added on the bid price;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When swaps are charged by reopening, positions are closed at a time set in the "End of day" parameter. After closing, the positions are opened again. The open time of new (reopened) positions depends on the "Statements mode" setting of the trade server. If "End of day" option is selected, the open time of the reopened positions is as the end of day time of current trade day ("End of day"). If "Start of day" option is selected, the open time of the reopened positions is set as the start of the next trade day. At that, if the open time of a position does not match a <a href="/en/docs/mt4/administrator/administration/ug_symbols#setup_sessions" class="topiclink">trading session</a> of the symbol, then the open time is set to the start of a closest trading session. At that, if positions are reopened by current Bid price, the Bid price at the actual time of opening is used, not the price at the start of the trading session.</span></p></td></tr></tbody></table>

-   Statements mode means the time of statements generation: end of trading day (before rollovers) or start of trading day (after rollovers);
-   Monthly statements mode means the day of monthly statements generation: the last day of the current month or the first day of the next month;
-   Generate statements at weekends enables/disables generation of statements on Sundays (this option doesn't affect generation of reports on Saturdays);

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Before generating daily reports, the server checks whether there has been at least 1 trade hour for the last 24 hours (work hours are determined in the <a href="/en/docs/mt4/administrator/administration/ug_time" class="topiclink">"Time"</a> section). If there were no trade hours, the daily reports are not generated. This rule is not applied to monthly reports.</span></p></td></tr></tbody></table>

-   Keep internal emails indicates the time period in days within which the emails being not received by the users will be kept. After the expiry of the time period indicated, all emails not received by the user will be deleted;
-   Keep ticks is the time period in days, during which tick data for securities will be stored;
-   Optimization time is the time period within which the server optimization is performed. The HDDs defragmentation, as well as other useful operations aimed at the increasing the speed of server response and its reliability are performed during this period of time. It is necessary to choose the time of the lowest server load. For example, 3:39 a.m. GMT;
-   Antiflood control is used for enabling the protection against DoS attacks. The server analizes the network activity of all clients, then chooses logins with the most frequent operations, coming from the same IP address or CID (computer identifier).  
       
    If less than 7 seconds elapsed between the previous connection (attempt to connect) and the new connection, the counter of such attempts is increased. If the counter increases the value of Antiflood max. connections, this address will be temporarily blocked for 5 minutes. "xxx.xxx.xxx.xxx Flooder blocked" message is written in the log-file on the server.  
       
    During the next 15 minutes after an address is blocked, for each attempt to connect in less than 7 seconds the time of blocking will increase by 5 minutes, but the total time of blocking shall not exceed 1 hour. For the counter to be reset, more than 7 seconds should elapse between two connections from this IP address.  
       
    This response mechanism allows to easily block attack attempts. The control must be enabled. More details are available in the ["DDoS Attack Prevention in MetaTrader 4 System "](https://support.metaquotes.net/en/articles/18) article.
-   Antiflood max. connections is the number of connections the exceeding of which results in blocking the attacker's IP address/CID. For example, if the parameter is indicated as 150, as soon as the amount of connections from the same IP address/CID exceeds 150, it will be blocked. But it is important to note that a situation is possible when a group of users (e.g., dealing) operates through one proxy server (WinGate, WinRoute, etc.). In this case, all connections to the server come from the same IP address. If there are too many clients and they generate very many network queries from the same IP, the server may mistake it for DoS attack and block the address. In this case, the amount indicated in Antiflood max. connections; should be increased
-   Feeder switch timeout is the time after expiry of which the server will switch to the next feeder of the same type in the list, if there are no quotes. To increase the reliability of data providing, it is recommended to have at least two feeders of the same type connected to different providers;
-   LiveUpdate mode allows to enable or disable live update:

-   Disabled — automatic updates are disabled. When automatic updates are disabled there's still a possibility to [manually update](/en/docs/mt4/administrator/administration/ug_live_update) the platform components.
-   Enabled — in this mode the platform components will be updated automatically when the final versions of updates are released. If this mode is enabled, the check of the current program versions will be performed on Sundays after the optimization (Client Terminal, Manager's Terminal, Administrator, Data Center, Server). Should new versions be detected, automatic download and installation of programs will be performed. Live Update is usually run within 5 minutes after the optimization time is over. This check allows to update all the system components without participation of technicians.
-   Enabled with beta versions — besides the release versions, there are beta versions that are released more often. If this option is enabled, all types of updates will be installed. However, it should be noted that intermediate versions can be unstable, so they should be installed only in extreme cases.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is strongly recommended to use beta updates only in extreme cases and only on demo servers.</span></p></td></tr></tbody></table>

-   Time synchronization with indicates the server address used for time synchronization through TIME protocol. This server will provide the system with the precise time indications. After having checked the time zone, they will be used in the system;
-   IP access list of web services is a comma-separated list of IP addresses from which Web-services commands are permitted. This list may contain no more than 8 IP-addresses. Empty list means that all IP-addresses are permitted;
-   Path to accounts/orders bases is the place on HDD where accounts and orders bases are stored. As soon as the path is changed, the existing bases will automatically be sent to a new directory. It is necessary to check if you have enough space on your HDD!
-   Path to history bases is the place on HDD where history bases are stored. As soon as the path is changed, the existing bases will automatically be sent to a new directory. It is necessary to check if you have enough space on your HDD!
-   Path to log files is the place on HDD where the server logs are stored. As soon as the path is changed, the existing logs will automatically be sent to a new directory. It is necessary to check if you have enough space on your HDD!
-   Network adapter for monitoring helps to choose an adapter for monitoring network activity of the server. It is necessary to choose a network adapter through which the server will be connected to Internet.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: To change a parameter, it is necessary to select it and push the Enter button or double-click on it with the left mouse button. After having changed it, it is also necessary to push the Enter button. It is also necessary to execute the "Edit — Apply changes" menu command in the "Common" section, push the <img class="help" alt="Accept changes" title="Accept changes" width="18" height="18" src="/en/docs/mt4/administrator/img/ic_changes_apply.png"> button of the toolbar or shortcut keys Ctrl+S. The changed parameters are now sent to the server and stored at it. Any changes in IP Address, Communication port, Time zone, Summer time correction, Accounts and order bases path, History bases path and Log files path come into effect only after the server is restarted.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_ol"><span class="f_ol">It is strongly not recommended:</span></p><ul><li class="p_ol"><span class="f_ol">to change the time zone settings on the server operating for the traders' enquiries, and</span></li><li class="p_ol"><span class="f_ol">to disable Antiflood control.</span></li></ul></td></tr></tbody></table>

## Recommended Settings

-   Communication port: 443
-   Daylight saving time correction: Yes
-   End of day time: 23:59

-   Antiflood control: Yes

-   Antiflood max. connections: 150

[Administration](/en/docs/mt4/administrator/administration)

[Gateway](/en/docs/mt4/administrator/administration/gateway)