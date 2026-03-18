# Protection against DDoS Attacks

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/security/network_anti_ddos

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
                -   [Certificates](/en/docs/mt5/platform/administration/security/security_certificates)
                -   [Firewall](/en/docs/mt5/platform/administration/security/admin_access)
                -   [Anti DDoS Protection](/en/docs/mt5/platform/administration/security/network_anti_ddos)
                -   [Authentication Protocols](/en/docs/mt5/platform/administration/security/authentication_protocol)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Security](/en/docs/mt5/platform/administration/security)Anti DDoS Protection

# Protection against DDoS Attacks

The access servers of the platform are provided with the [DDoS protection](/en/docs/mt5/platform/components/access_server/access_server_antiflood) mechanism. The mechanism monitors the network activity of clients in real time and blocks connections from IP addresses, on which suspicious activity is registered, such as sending too many requests or invalid data, authorization errors, etc.

Unfortunately, the mechanism cannot protect the platform against all existing types of attacks. For example, it cannot defend against attacks targeting the network infrastructure, since such attacks cannot be physically dealt with at the access server application level. Additional mechanisms are required for effective protection.

The trading platform provides a special component Anti-DDoS Proxy Server. The component enables the use of external Anti-DDoS service providers. In this case, blocking of unwanted connections is performed on the distributed network of Anti-DDoS provider's servers rather than on access servers. The Anti-DDos provider's server network actually acts as an additional component between the client and the access server.

Instead of directly connecting to access servers, all clients will be connected to the provider's public access points. Unwanted connections will be filtered in the provider's own network of servers, while legitimate connections from real clients will be forwarded to access servers.

The broker's infrastructure is practically not affected.

![Operation scheme with and without an external Anti-DDoS service provider](/en/docs/mt5/platform/img/anti_ddos_scheme.png "Operation scheme with and without an external Anti-DDoS service provider")

## Configure your access server for the operation with an external Anti-DDoS service provider [#](network_anti_ddos#hide_access)

Choose an access server, to which the connections via the Anti-DDoS provider will be redirected. It is recommended to install and configure a new access server, because its address must not be publicly known (otherwise attackers will be able to directly attack this server). If you have an access server that was never visible to clients (had the [Idle priority](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#priority) or [client connections were disabled](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server#permissions) in its settings), you may use this server.

The 'Use as dedicated access point only for MetaTrader 5 VPS / Ultency connections' option is available for servers that work with an external Anti-DDoS provider.

![Hiding an access server from terminals](/en/docs/mt5/platform/img/anti_ddos_hide_access.png "Hiding an access server from terminals")

Enable this option for the access server, to which connections will be redirected. The server will be hidden from all terminals, including client, manager and administrator, and will not be displayed in the list of access points. Not knowing the address of the server, attackers will not be able to perform an attack.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">By hiding a server, you do not disable the possibility to connect to it. Terminals can connect to this server if the address is specified manually, and the Anti-DDoS provider can redirect client connections to it.</span></p></td></tr></tbody></table>

## Choose an Anti-DDoS service provider and receive necessary data

You should contact the Anti-DDoS provider and sign an appropriate agreement.

-   You will need to provide information about the [public address](/en/docs/mt5/platform/administration/admin_network/network_add_edit#public) of your access server to your Anti-DDoS provider.
-   The provide will allocate one or more public addresses, to which your clients will be connected. These addresses should be specified in the [Anti DDoS Proxy Server settings](/en/docs/mt5/platform/administration/security/network_anti_ddos#public) in the 'Public Addresses' field.
-   Also you will be provided with ranges of proxy server addresses through which client connections will be forwarded to access servers. These ranges should also be specified in the Anti DDoS Proxy Server settings (tab [Source Subnets](/en/docs/mt5/platform/administration/security/network_anti_ddos#range). The ranges are used as an additional protection measure: connections forwarded by the Anti-DDoS provider will only be accepted from these addresses.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The platform supports the following service providers — <a href="https://support.metaquotes.net/en/market/product/194" target="_blank" class="weblink">Akamai</a>, <a href="https://support.metaquotes.net/en/market/product/477" target="_blank" class="weblink">Qrator</a>, <a href="https://support.metaquotes.net/en/market/product/478" target="_blank" class="weblink">Cloudflare</a>. Support for other providers will be added soon.</span></p></td></tr></tbody></table>

## Configure the Anti DDoS Proxy Server component in MetaTrader 5

After you receive the required information, add the Anti-DDoS Proxy Server component in the Network Cluster section. Set a name for this component. Note that this name will be used for the display access points in client terminals. Do not use phrases like Anti DDoS etc., the point should look like a regular access server.

Also set the internal ID; passwords are not used for this component.

![Added the Anit DDoS Proxy Server component](/en/docs/mt5/platform/img/anti_ddos_add.png "Added the Anit DDoS Proxy Server component")

Next, on the Network tab, specify:

-   Priority — the basic priority for the access points of the Anti-DDoS provider, from 0 to 15. It is similar to priority settings of access servers. Preference of a server for client connections is calculated based on the basic priority and the quality of connection with the server (ping). The lower the priority is, the more preferred the server is for clients.
-   Public addresses — one or more public access points through which clients connect to the platform (via the provider's network). These points are prvided to you by the Anti DDoS service provider.

![Anti-DDoS Proxy Server settings](/en/docs/mt5/platform/img/anti_ddos_settings.png "Anti-DDoS Proxy Server settings")

On the "Source Subnets" tab, set the range of addresses for the provider's proxy servers. Connections forwarded by the Anit-DDoS provider from these addresses will be accepted.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Anti-DDoS Proxy Server will work even if you do not specify provider's proxy ranges. However, we strongly recommend specifying the ranges, otherwise, connections from any addresses will be allowed in the Anti DDOS provider mode.</span></p></td></tr></tbody></table>

## Check the accessibility of the Anti-DDoS server in terminals

After configuration Anti DDoS, the server will be available for client connections. The provider's server is displayed as a regular access point in client terminals:

![Access points in the client terminal](/en/docs/mt5/platform/img/anti_ddos_terminal_points.png "Access points in the client terminal")

## How to Hide Access Servers

After the configuration of the Anti-DDoS proxy server, the provider's access point will be available for all terminals, including client, manager and administrator. However, your access points will still be available to these terminals. If a server address is publicly available, attackers can find out this address and perform an attack. In order to protect from possible attacks, you can hide access servers. This can be done by enabling the option 'Hide server from all types of terminals (connections will be allowed)'.

![Hiding an access server from terminals](/en/docs/mt5/platform/img/anti_ddos_hide_access.png "Hiding an access server from terminals")

The server will be hidden from all terminals and will not be displayed in the list of access points. Not knowing the address of the server, attackers will not be able to perform an attack.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">By hiding a server, you do not disable the possibility to connect to it. Terminals can connect to this server if the is specified manually, and the Anti-DDoS provider will be able to forward client connections to it.</span></p></td></tr></tbody></table>

## How to identify connections through the Anti-DDoS provider

Forwarded client connections are received from the Anti-DDoS provider's addresses. However, the real original addresses of clients are also known, since this information is transmitted by the provider. The proper original client's address is written to the platform logs and [client records](/en/docs/mt5/platform/administration/admin_accounts/account_edit) (e.g. in the Last IP parameter).

Check the [access server journal](/en/docs/mt5/platform/administration/admin_network/network_journal) to find out if the client is connected via the Anti DDoS provider:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2017.10.13&nbsp;17:42:08.441&nbsp;84.101.15.116&nbsp;&nbsp;&nbsp;'1814046':&nbsp;login&nbsp;(Client&nbsp;build&nbsp;1674,&nbsp;cid:&nbsp;13ea0a897463ba4aeb76db5d8cdc4afa,&nbsp;ping:&nbsp;108.83&nbsp;ms,&nbsp;</span><span class="f_CodeExample" style="background-color: #dce6f2;">anti&nbsp;ddos&nbsp;server:&nbsp;81.230.104.100</span><span class="f_CodeExample">)</span></p></td></tr></tbody></table>

[Firewall](/en/docs/mt5/platform/administration/security/admin_access)

[Authentication Protocols](/en/docs/mt5/platform/administration/security/authentication_protocol)