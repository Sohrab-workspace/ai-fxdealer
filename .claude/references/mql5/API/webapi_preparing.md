# Before You Begin

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_preparing

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
            -   [Getting Started](/en/docs/mt5/api/webapi_preparing)
            -   [Format of Commands](/en/docs/mt5/api/webapi_https)
            -   [Authentication](/en/docs/mt5/api/webapi_rest_authentication)
            -   [Escaping Special Characters](/en/docs/mt5/api/webapi_screening)
            -   [Maintaining Connections](/en/docs/mt5/api/webapi_pings)
            -   [Protocol Extension](/en/docs/mt5/api/webapi_protocol_extension)
            -   [Examples](/en/docs/mt5/api/webapi_examples)
            -   [Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)Getting Started

# Before You Begin

Before you begin to work with the MetaTrader 5 Web API, prepare a special account on a trade server. This account is used for [authorizing](/en/docs/mt5/api/webapi_rest_authentication) a Web client.

-   [Creating an Account](/en/docs/mt5/api/webapi_preparing#account_create)
-   [Configuring the account](/en/docs/mt5/api/webapi_preparing#account_setup)
-   [Configuring access to symbols](/en/docs/mt5/api/webapi_preparing#symbols)
-   [Configuring the Manager](/en/docs/mt5/api/webapi_preparing#manager_configuration)
-   [Configuring the Access Server](/en/docs/mt5/api/webapi_preparing#access)
-   [Setup of operation via HTTPS](/en/docs/mt5/api/webapi_preparing#https)

## Creating an Account [#](webapi_preparing#account_create)

To create an account, navigate to the relevant MetaTrader 5 Administrator section and click "Add". The account must be created in the Managers group.

![Creating an Account](/en/docs/mt5/api/img/webapi_account_create.png "Creating an Account")

## Configuring the account [#](webapi_preparing#account_setup)

Set the API password in the "Security" tab:

![API Password](/en/docs/mt5/api/img/webapi_account_security.png "API Password")

Enter your password in the appropriate field and click "Change". This password is used for [connecting](/en/docs/mt5/api/webapi_rest_authentication#client_start) a Web client to a trade server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When working with the <a href="/en/docs/mt5/api/serverapi_debug" class="topiclink">debug server version</a>, the Manager password is always used regardless of the password actually set for the account.</span></p></td></tr></tbody></table>

## Configuring Access to Symbols [#](webapi_preparing#symbols)

The list of [symbols](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols) for which the Web client can access information is determined by the settings of the group which the manager account belongs to.

![Access to symbols is determined by the manager group settings](/en/docs/mt5/api/img/webapi_account_symbols.png "Access to symbols is determined by the manager group settings")

## Configuring the Manager [#](webapi_preparing#manager_configuration)

When creating an account in the Managers group, MetaTrader 5 Administrator immediately creates a manager configuration based on this account. This is a special account add-on over extending account permissions.

Open this configuration under "Clients and accounts \\ Managers". The configuration can be found by the account number or by name.

![Creating a Manager Account](/en/docs/mt5/api/img/webapi_manager_create.png "Creating a Manager Account")

On the Common tab, specify [groups](/en/docs/mt5/api/webapi_main/webapi_config/webapi_groups) that the web client can work with. In fact, they define access to accounts and trading operations.

In the "Permissions" tab, set up access restrictions for a Web client.

![Configuring Permissions](/en/docs/mt5/api/img/webapi_manager_permissions.png "Configuring Permissions")

The following permissions apply to the account used for a Web client:

-   Connection using MetaTrader 5 Administrator — enables the administrator connection to a trade server, which is used in the Web API. This permission is required for adding/modifying configurations of [groups](/en/docs/mt5/api/webapi_main/webapi_config/webapi_groups/webapi_group_add) and [symbols](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_add).
-   Connect using MetaTrader 5 Manager — enables the manager connection to a trade server, which is used in the Web API. This permission must necessarily be enabled.
-   Configuration setup — defines the types of configurations that can be changed through the Web API.
-   Sending emails — allows to [send messages](/en/docs/mt5/api/webapi_main/webapi_mail/webapi_mail_send) through the internal mailing system.
-   Sending news — allows to [send news](/en/docs/mt5/api/webapi_main/webapi_news/webapi_news_send).
-   Accountant — allows to perform [balance operations](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_trade/webapi_trade_balance) on client accounts.
-   Access to accounts — allows to [request information about accounts](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_get) (without access to personal data).
-   Access to personal data of accounts — allows to view personal data of accounts.

-   Name
-   Bank Account
-   Phone Password
-   Country
-   City
-   State
-   Zip/Postal code
-   Address
-   Phone
-   Email
-   Comment
-   ID
-   Status
-   API Data
-   Trade accounts in external systems
-   Modify accounts — allows to [add](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_add) and [modify](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_update) accounts.
-   Delete accounts — allows to [delete](/en/docs/mt5/api/webapi_main/webapi_users/webapi_user_delete) accounts.
-   Access to trade orders — this permission allows viewing [orders](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_orders), [deals](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_deal) and [positions](/en/docs/mt5/api/webapi_main/webapi_trading/webapi_positions) of clients.
-   Edit orders, positions and deals — allows the deletion of any orders, deals and positions.
-   Delete orders, positions and deals — allows the deletion of any orders, deals and positions.
-   Back office — access permissions to the [client](/en/docs/mt5/api/webapi_main/webapi_client) database.
-   Subscriptions — access permissions to the [Subscriptions](/en/docs/mt5/api/webapi_main/webapi_subscription) service.

In the "List of allowed IP addresses", you can additionally restrict connection of a Web client based on IP address.

# Configuring the Access Server

To allow connections to the trading platform via the Web API, enable the corresponding option in the access server settings:

![Allow Web API connections](/en/docs/mt5/api/img/webapi-access-enable.png "Allow Web API connections")

This setting affects normal connections and [connections via HTTPS](/en/docs/mt5/api/webapi_https).

## Setup of operation via HTTPS [#](webapi_preparing#https)

All connections to the trading platform are established through access servers. Support for connection over HTTPS is implemented on access servers (HTTP is not connected). Therefore, they can act as a web server.

To enable connection to the access server via HTTPS, at least one of its [public addresses](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit#public) must be associated with a certain domain, i.e. the host to which POST and GET requests will be implemented. For this purpose, the appropriate entry must be specified on the DNS server. For example, if you want to implement operation via the host abc.broker.com, the following entry should be added to DNS: "XXX.XXX.XXX.XXX abc.broker.com", where XXX.XXX.XXX.XXX is the public address of the access server.

Since only protected TLS connections (HTTPS) are supported, an SSL certificate must be installed on the access server for the appropriate domain. Use the "Integrations \\ Web Services \\ SSL Certificates" section of the MetaTrader 5 Administrator to upload and manage certificates:

![Configuring SSL certificates for connecting to an access server via HTTPS](/en/docs/mt5/api/img/ssl-certificates.png "Configuring SSL certificates for connecting to an access server via HTTPS")

These settings apply to all access servers. Changes in the list of certificates are applied instantly, so you do not need to restart the servers.

Connections from multiple domains can be supported on one server ([the SNI mode](https://ru.wikipedia.org/wiki/Server_Name_Indication)). In this case, the corresponding SSL certificate must be installed for each of them. When connecting, the client specifies the address to connect to. The access server checks all installed certificates and automatically provides the necessary one to the client:

-   First, the server tries to find a certificate for an exactly matching domain.
-   If not, it tries to find the most suitable one using mask "\*".
-   If the certificate could not be found, the server returns the first certificate from the list.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When using self-signed certificates on the Web API client side, add them in the list of trusted certificates or allow the use of untrusted certificates.</span></p></td></tr></tbody></table>

[Web API](/en/docs/mt5/api/webapi)

[Format of Commands](/en/docs/mt5/api/webapi_https)