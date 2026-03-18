# User management

> Source: https://support.metaquotes.net/en/docs/mt5/api/retcodes_clients

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
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
            -   [Successful completion](/en/docs/mt5/api/retcodes_successful)
            -   [Common errors](/en/docs/mt5/api/retcodes_common)
            -   [Authentication](/en/docs/mt5/api/retcodes_authentication)
            -   [Configuration Management](/en/docs/mt5/api/retcodes_configs)
            -   [User management](/en/docs/mt5/api/retcodes_clients)
            -   [Trade management](/en/docs/mt5/api/retcodes_trades)
            -   [Report Generation](/en/docs/mt5/api/retcodes_reports)
            -   [Price Data](/en/docs/mt5/api/retcodes_price_history)
            -   [Trade Requests](/en/docs/mt5/api/retcodes_trade_request)
            -   [Dealer](/en/docs/mt5/api/retcodes_dealer)
            -   [API](/en/docs/mt5/api/retcodes_api)
            -   [Messengers](/en/docs/mt5/api/retcodes_messenger)
            -   [Subscriptions](/en/docs/mt5/api/retcodes_subscription)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Return Codes](/en/docs/mt5/api/reference_retcodes)User management

# User management

This group of codes is returned by the server when working with a database of [users](/en/docs/mt5/api/reference_user):

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Constant</span></p></th><th class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_LAST_ADMIN</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3001</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The last administrator account has been deleted.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_LOGIN_EXHAUSTED</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3002</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The range of logins has been exhausted.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_LOGIN_PROHIBITED</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3003</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The login is reserved on another server.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_LOGIN_EXIST</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3004</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The account already exists.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_SUICIDE</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3005</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">An attempt of self-deletion.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_INVALID_PASSWORD</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3006</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Incorrect account password.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_LIMIT_REACHED</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3007</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Reached the limit on the number of users.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_HAS_TRADES</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3008</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The accounts has open positions.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_DIFFERENT_SERVERS</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3009</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">An attempt to move an account to another server.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_DIFFERENT_CURRENCY</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3010</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">An attempt to move an accounts to a group with a different deposit currency.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_IMPORT_BALANCE</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3011</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Failed to import account balance.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_IMPORT_GROUP</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3012</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The account is imported with the wrong group.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_ACCOUNT_EXIST</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3013</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/reference_user/imtuser/imtuser_externalaccountadd" class="topiclink">A trading account in an external system</a> already exists for a specified login.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_IMPORT_ACCOUNT</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3014</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Failed to <a href="https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt" target="_blank" class="weblink">import</a> account's trading data.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_IMPORT_POSITIONS</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3015</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Failed to import account's trading positions.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_IMPORT_ORDERS</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3016</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Failed to import account's open orders.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_IMPORT_DEALS</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3017</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Failed to import account's deal history.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_IMPORT_HISTORY</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3018</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Failed to import account's order history.</span></p></td></tr><tr class="table"><td class="table" style="width:229px;"><p class="p_fortable"><span class="f_fortable">MT_RET_USR_API_LIMIT_REACHED</span></p></td><td class="table" style="width:74px;"><p class="p_fortable"><span class="f_fortable">3019</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Reached the limit on the number of users with the permission to connect via the API (<a href="/en/docs/mt5/api/reference_user/imtuser/imtuser_enum#enusersrights" class="topiclink">IMTUser::USER_RIGHT_API_ENABLED</a>). The current limit is 100 users.</span></p></td></tr></tbody></table>

[Configuration Management](/en/docs/mt5/api/retcodes_configs)

[Trade management](/en/docs/mt5/api/retcodes_trades)