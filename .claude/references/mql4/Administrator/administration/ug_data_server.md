# Data Centers

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_data_server

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Data Centers

# Data Centers

This section is intended for creation and for operation check of public access points (data centers). A data center performs several tasks:

-   It operates as a proxy server to increase the scalability of the system  
    Receiving some common data, the Data Center caches them and sends to all online traders. This allows decreasing the load of the server since it is the sending quotes, historical data, and news that makes the largest part of the load. If the Data Center and the clients operate in the same local network, the traffic will be saved essentially.
-   Operates as a Relay Server  
    Data Centers can perform the functions of a "Relay Server" hiding the real IP-address of the server. In the case of one of the Data Centers falling out, the main server of the system will continue operating in a normal mode. Use of Data Centers enables the server to define the client's real IP-address correctly. High efficiency of the program is provided through using its own protocol allowing to check the frequency of connections and to manage them dynamically.
-   It balances common load among different access points automatically
-   It prevents DoS attacks  
    Data Centers have built-in functions of network activity of online traders. Those functions allow to define and prevent potential DoS attacks in time. Such malicious actions are blocked before they reach the main server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Note: If a Data Center is not included into the list, all inquiries coming through it will have the same IP-address. In this case, the main server may block the address and the Data Center will not be able to operate.</span></p></td></tr></tbody></table>

![Data Servers](/en/docs/mt4/administrator/img/br_data_server.png "Data Servers")

-   Server — Data Center address and port;
-   Description — description;
-   Internal IP Address — Data Center internal IP address;
-   Priority — priority. Each access point has its basic priority (0 to 255, in descending priorities) showing its accessibility. The lower the priority is, the more preferable for clients the server is. For creating virtual, temporarily non-existing servers, a special priority 255 is intended (Idle). Such servers are used as backup ones. A backup sever starts only if all other Data Centers do not function;
-   Loading — Data Center loading indicator.

To add an instruction concerning a new Data Center you should use "Add" command, or the same command in the "Edit" menu, or using the ![Add](/en/docs/mt4/administrator/img/ic_config_add.png "Add") button on the toolbar. The "Edit" command and the ![Edit](/en/docs/mt4/administrator/img/ic_config_edit.png "Edit") button allow to edit instructions, and the "Delete" button, and the ![Delete](/en/docs/mt4/administrator/img/ic_config_delete.png "Delete") — button allows to delete entries about Data Centers. When adding and editing entries, the setting window will appear:

![Data Server Setting](/en/docs/mt4/administrator/img/win_data_server.png "Data Server Setting")

-   Description — description of a Data Center;
-   Public Server Address — public IP-address of a Data Center. It is used for the connection of clients to the Data Center. You can specify domain name instead of the IP address;
-   Internal IP Address — internal IP-address of a Data Center. It used by a Data Center to connect to the main trading server;
-   Priority — priority of a Data Center.
-   Use for monitoring the trade server and failover — when enabled, the WatchDog server uses this data center to check the availability of the trade (backed up) server. This is used to automatically switch to the backup server if the trade server fails. More detailed information can be found in the [appropiate section](/en/docs/mt4/administrator/administration/ug_backup#auto).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">To avoid making changes to the client terminals every time there is a change in the server IP address, it is recommended that domain names be specified instead of IP addresses in "Public server address" field. In this case, if the location of the server (or one of the Data Centers) changes, only the corresponding entry on the DNS server of the hosting provider will need to be updated.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">It is recommended no to enable "Use for monitoring the trade server and failover" option for MetaTrader 4 WatchDog added as a data center. Also one should not enable it for non-working data centers. It increases the time of switching to backup and the amount of consumed resources.</span></li><li class="p_tableatten"><span class="f_tableatten">For the changes to take effect it is necessary <a href="/en/docs/mt4/administrator/server_commands/ug_server_restart" class="topiclink">to restart the server.</a></span></li></ul></td></tr></tbody></table>

## Data Center Priority

The preference of a data center server for client terminals to connect to a trade server is defined by its priority and connection quality. The lower the value if priority is, the more preferable the data center is. A base priority (Priority parameter) from 1 to 15 can be specified in its settings. It defines the data center preference if all other conditions are equal. The final analysis of a data center is conducted upon the ping and the current priority, which depends on the basic priority and the number of current connections.

The current priority is calculated according to the following formula: Current Priority = (Base Priority + Connections / 200),

where:

-   Current Priority is the priority at the server current moment;
-   Base Priority is the base priority set in data center parameters;
-   Connections — the number of current connections.

Every 200 client connections increase the current priority of a server by one (maximum increase is 10).

[IP Access List](/en/docs/mt4/administrator/administration/ug_access)

[Time](/en/docs/mt4/administrator/administration/ug_time)