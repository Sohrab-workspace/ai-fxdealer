# Manager Accounts

> Source: https://support.metaquotes.net/en/docs/mt5/platform/migration/migration_manager

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
            -   [General Settings](/en/docs/mt5/platform/migration/migration_general)
            -   [Financial Instruments](/en/docs/mt5/platform/migration/migration_symbols)
            -   [Trade Groups](/en/docs/mt5/platform/migration/migration_group)
            -   [Import of Accounts and Trades](/en/docs/mt5/platform/migration/migration_account_trade)
            -   [Manager Accounts](/en/docs/mt5/platform/migration/migration_manager)
            -   [Data Feeds](/en/docs/mt5/platform/migration/migration_datafeed)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Migration from MetaTrader 4](/en/docs/mt5/platform/migration)Manager Accounts

# Manager Accounts

The essential difference between the MetaTrader 5 system from the MetaTrader 4 server is an ability to create multiple manager\\\* groups. This means that it is now possible to divide manager accounts so that different symbols (symbol groups) are available to them. Besides, they may receive different news, have different security settings and connect to different trade servers.

After installing the MetaTrader 4 server, the manager "1" with the highest server access level rights is created. In MetaTrader 5 platform, such an account is created by default as well but it has the login "1000".

Similarly to the fourth platform version, [open an account](/en/docs/mt5/platform/administration/admin_accounts/account_add) in the manager group and add a new entry in the [Managers](/en/docs/mt5/platform/administration/admin_managers) section to create a manager account in MetaTrader 5. After that, configure the rights.

## Setting the Manager Rights

Most MetaTrader 4 access rights have retained their functions in MetaTrader 5. When you start working in MetaTrader 5, you are able to open manager accounts identical to MetaTrader 4 server ones in terms of access right settings.

-   Login, Groups and Email fields on the MetaTrader 4 server match the [Common](/en/docs/mt5/platform/administration/admin_managers#common) tab settings of MetaTrader 5 manager account.
-   "Access Rights" block corresponds to the [Permissions](/en/docs/mt5/platform/administration/admin_managers#permissions) tab in MetaTrader 5.
-   "IP filter" field matches the "IP Access List" tab.

![Manager settings in MetaTrader 4 and MetaTrader 5](/en/docs/mt5/platform/img/migration_manager.png "Manager settings in MetaTrader 4 and MetaTrader 5")

The table below shows the correlation between MetaTrader 4 and MetaTrader 5 access rights:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">MetaTrader 4</span></p></th><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">MetaTrader 5</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Manager (add/edit/delete accounts)</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Access accounts</span></p><p class="p_fortable"><span class="f_fortable">Access the account personal details</span></p><p class="p_fortable"><span class="f_fortable">Edit accounts</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Administrator (full access to server configuration)</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">It corresponds to enabling all permissions.</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Reports</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Receive reports</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Internal mail system</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Send emails</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Send news</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Send news</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Connections (show online clients)</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">View currently connected clients</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Configure server plugins</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Configure plugins</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Access to technical support page</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Access technical support page</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Push notifications</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Push notifications</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Supervise trades</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Access orders and positions</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Accountant (deposit/credit/withdrawal money)</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Accountant (deposit/withdraw)</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Risk manager</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Risk manager</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Journals (direct access to server journals)</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Access server logs</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Edit prices, spreads, execution types</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Throw in quotes</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Personal details</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Access the account personal details</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Automatic server reports</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Receive automatic server reports</span></p></td></tr><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Access to Applications Market</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Access to Applications Market</span></p></td></tr></tbody></table>

## Request Routing

The MetaTrader 5 manager settings have no parameters similar to symbol routing table of MetaTrader 4. However, the identical parameters can be configured in a separate [Routing](/en/docs/mt5/platform/administration/requests_routing) section of the Administrator terminal. The new section allows configuring routing in MetaTrader 5 in a more flexible and efficient manner.

Below you can see how to reproduce the settings of the MetaTrader 4 routing table in the MetaTrader 5 Routing section. In our example, the manager "1" is responsible for processing all trade requests with the volumes from 0 to 10 lots at "Forex" group symbols on MetaTrader 4 server:

![MetaTrader 4 request routing table](/en/docs/mt5/platform/img/migration_manager_routing.png "MetaTrader 4 request routing table")

First, create a custom rule and set conditions for processing trade operations. Then use the Dealers tab to specify the manager who will process trade requests that meet the rule conditions.

![Configuring trade requests routing to the manager](/en/docs/mt5/platform/img/migration_manager_routing2.png "Configuring trade requests routing to the manager")

Specify the following parameters:

-   Rule name.
-   Perform action — "Process to dealers". Enable "skip this rule if no dealers online" option to avoid missing trade requests if there are no managers online. In this case, if there is no appropriate manager online, all requests meeting the rule are processed according to the next rule in the list (with the lower priority).
-   Select All for "Where request is:" and "Where order is:" options.
-   Add the following rules for "Where conditions are:" section:

-   "Client group" — set "real\\real" in order to limit the manager operation by processing client requests from the real account group.
-   "Request volume" — this condition corresponds to the level of maximum and minimum lots of the MetaTrader 4 routing table (from 0 to 10).
-   "Symbols" — select Forex symbols similar to the MetaTrader 4 settings.

Next, add the manager "1000" on the Dealers tab of the rule. Please note that you can assign more than one dealer for a single rule.

[Import of Accounts and Trades](/en/docs/mt5/platform/migration/migration_account_trade)

[Data Feeds](/en/docs/mt5/platform/migration/migration_datafeed)