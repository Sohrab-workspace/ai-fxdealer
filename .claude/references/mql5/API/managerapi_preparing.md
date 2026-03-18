# Preparation for work

> Source: https://support.metaquotes.net/en/docs/mt5/api/managerapi_preparing

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
            -   [Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)
            -   [Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)
            -   [Getting Started](/en/docs/mt5/api/managerapi_preparing)
            -   [Ready-made Examples](/en/docs/mt5/api/managerapi_examples)
            -   [.NET Implementation](/en/docs/mt5/api/managerapi_net)
            -   [Python Implementation](/en/docs/mt5/api/managerapi_python)
            -   [Exported Functions](/en/docs/mt5/api/managerapi_exported)
            -   [CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)
            -   [Administrator Interface](/en/docs/mt5/api/imtadminapi)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
            -   [Dealer Interface](/en/docs/mt5/api/imtdealersink)
            -   [Interface of Manager API Events](/en/docs/mt5/api/imtmanagersink)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)Getting Started

# Preparation for work

To work through the MetaTrader 5 Manager API, prepare a special account on the trade server. The account be used to authorize the Manager API client using the [IMTAdmin::Connect](/en/docs/mt5/api/imtadminapi/imtadminapi_connection/imtadminapi_connect) and[IMTManager::Connect](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_connect) methods.

-   [Creating an account](/en/docs/mt5/api/managerapi_preparing#account_create)
-   [Configure access to symbols](/en/docs/mt5/api/managerapi_preparing#symbols)
-   [Manager configuration](/en/docs/mt5/api/managerapi_preparing#manager_configuration)
-   [Configuring the Access Server](/en/docs/mt5/api/managerapi_preparing#access)

## Creating an account [#](managerapi_preparing#account_create)

To create an account, navigate to the relevant MetaTrader 5 Administrator section and click "Add". The account must be created in the Managers group.

![Creating an account](/en/docs/mt5/api/img/webapi_account_create.png "Creating an account")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Operation with the <a href="/en/docs/mt5/api/serverapi_debug" class="topiclink">debug server version</a> always uses password "Manager" regardless of the password actually set for the account.</span></p></td></tr></tbody></table>

## Configure access to symbols [#](managerapi_preparing#symbols)

The list of [symbols](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols) for which the Manager API client can receive information is determined by the settings of the group to which the manager account belongs.

![Access to symbols is determined by the manager group settings](/en/docs/mt5/api/img/webapi_account_symbols.png "Access to symbols is determined by the manager group settings")

## Manager configuration [#](managerapi_preparing#manager_configuration)

When creating an account in the Managers group, MetaTrader 5 Administrator immediately creates a manager configuration based on this account. This is a special account add-on over extending account permissions.

Open this configuration under the "Clients and accounts \\ Managers" section. The configuration can be found by the account number or by name.

![Create a manager account](/en/docs/mt5/api/img/webapi_manager_create.png "Create a manager account")

On the Common tab, specify [groups](/en/docs/mt5/api/webapi_main/webapi_config/webapi_groups) with which the Manager API client can work. In fact, they define access to accounts and trading operations.

On the Permissions tab, configure access restrictions for the Manager API client.

![Permission settings](/en/docs/mt5/api/img/webapi_manager_permissions.png "Permission settings")

The manager account used for the Manager API client has the following permissions:

-   Connect using MetaTrader 5 Administrator — allows [administrator connection](/en/docs/mt5/api/imtadminapi) to the trading server, used in the Manager API.
-   Connect using MetaTrader 5 Manager — allows [manager connection](/en/docs/mt5/api/imtmanagerapi) to the trading server, used in the Manager API. The permission must be enabled.
-   Configuration setup — determines the type of configurations which can be changed via the Manager API.
-   Send email — allows the account to [send emails](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_mail) via the internal mail system.
-   Send news — allows the account to [send newsletters](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_news).
-   Accountant — enables access to perform [balance operations](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations/imtmanagerapi_dealing/imtmanagerapi_dealerbalance) on client account.
-   Access accounts — permission to [request account information](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user) (without access to personal data).
-   Access account personal details — permission to view the following personal details of accounts:

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
-   Comments
-   ID
-   Status
-   API User Data
-   Trading account numbers in external systems
-   Change accounts — permission to [add](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_useradd) and [edit](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userupdate) accounts.
-   Delete accounts — permission to [delete](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user/imtmanagerapi_userdelete) accounts.
-   Access orders and positions — permission to view client [orders](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_order), [deals](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_deal) and [positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading/imtmanagerapi_trading_position).
-   Edit orders, positions and deals — permission to edit the relevant trading operations.
-   Delete orders, positions and deals — permission to edit the relevant trading operations.
-   Back Office — access to the [client](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_clients) database.
-   Subscriptions — access to the [subscriptions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription) service.

On the "List of allowed IP addresses" tab, you can further restrict the Manager API client connection by IP addresses.

# Configuring the Access Server

To allow connections to the trading platform via the Manager API, enable the corresponding option in the access server settings:

![Allow Web API connections](/en/docs/mt5/api/img/webapi-access-enable.png "Allow Web API connections")

[Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)

[Ready-made Examples](/en/docs/mt5/api/managerapi_examples)