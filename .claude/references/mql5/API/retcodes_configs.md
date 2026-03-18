# Configuration Management

> Source: https://support.metaquotes.net/en/docs/mt5/api/retcodes_configs

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Return Codes](/en/docs/mt5/api/reference_retcodes)Configuration Management

# Configuration Management

This group of codes is returned by the server in case [configurations](/en/docs/mt5/api/imtadminapi/imtadminapi_config) are changed:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Constant</span></p></th><th class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_LAST_ADMIN</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Deleting the last administrator configuration.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_LAST_ADMIN_GROUP</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2001</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The last group of administrators cannot be deleted.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_NOT_EMPTY</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2003</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The group contains accounts or trade operations.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_INVALID_RANGE</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2004</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Invalid range of accounts or trade operations.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_NOT_MANAGER_LOGIN</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2005</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The manager account does not belong to the manager group.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_BUILTIN</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2006</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Built-in protected configuration.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_DUPLICATE</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2007</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Duplicate configuration.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_LIMIT_REACHED</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2008</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Reached limit on the number of configurations.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_NO_ACCESS_TO_MAIN</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2009</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Incorrect network configuration.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_DEALER_ID_EXIST</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2010</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A dealer with the same ID (account number) already exists.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_BIND_ADDR_EXIST</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2011</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Connection address already exists.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_WORKING_TRADE</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2012</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">An attempt to delete a working trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_GATEWAY_NAME_EXIST</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2013</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gateway with that name already exists.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_SWITCH_TO_BACKUP</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2014</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Switch to a backup server has been initiated for the Trade/History server.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_NO_BACKUP_MODULE</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2015</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">No backup server.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_NO_TRADE_MODULE</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2016</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">No trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_NO_HISTORY_MODULE</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2017</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Ho history server.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_ANOTHER_SWITCH</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2018</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The process of switching to a backup server has already started.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_NO_LICENSE_FILE</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2019</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">No license file.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_GATEWAY_LOGIN_EXIST</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2020</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Creating a manager configuration is not possible, because the login is already used by the gateway.</span></p></td></tr><tr class="table"><td class="table" style="width:240px;"><p class="p_fortable"><span class="f_fortable">MT_RET_CFG_INVALID_COMPANY</span></p></td><td class="table" style="width:73px;"><p class="p_fortable"><span class="f_fortable">2021</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The company name does not correspond to the license or White Label. The error is returned when you try to add or save a group with the <a href="/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_company" class="topiclink">company name</a> different from the one specified in the platform license as the main or additional White Label.</span></p></td></tr></tbody></table>

[Authentication](/en/docs/mt5/api/retcodes_authentication)

[User management](/en/docs/mt5/api/retcodes_clients)