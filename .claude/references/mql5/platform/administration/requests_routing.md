# Routing

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/requests_routing

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
                -   [Actions and Conditions](/en/docs/mt5/platform/administration/requests_routing/routing_rules)
                -   [Example of Rules](/en/docs/mt5/platform/administration/requests_routing/routing_example)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Routing

# Routing

This section allows managing rules of processing clients' trade requests depending on different conditions.

![Routing](/en/docs/mt5/platform/img/routing.png "Routing")

The table of rules contains the following details:

-   Name — names of routing rules;
-   Dealers — list of dealers who process request that meet the conditions.

## Execution of Rules [#](requests_routing#execution)

Rules are executed in the direction from top to bottom. If an incoming request meets the conditions of the upper rule, it is processed according to this rule; otherwise the request is checked for meeting conditions of the second rule, and so on. A request is processed according to the rules until it is executed or passed to a dealer. For example, meeting the rule directing to delay the request execution for some time, the request will be delayed and then checked for correspondence to further rules.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any change in the routing table leads to that all request currently processed according to these rules are moved to the beginning of the table and go through all rules again.</span></p></td></tr></tbody></table>

To change the position of rules in the list, use context menu commands: "![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up" and "![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down", the same commands of the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu or buttons on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar.

If you need to add a rule or change an existing one, press "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" or "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit", respectively. They are available in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar and in the context menu. As soon as you press the button, the rule configuration window with two tabs will be opened.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Additional general information about working with configuration records is given in the <a href="/en/docs/mt5/platform/administration/common_info/common_instructions" class="topiclink">"Working with Instructions"</a> section.</span></p></td></tr></tbody></table>

## Common [#](requests_routing#common)

![Common](/en/docs/mt5/platform/img/routing_common.png "Common")

On the "Common" tab you set common parameters of the rule, as well as conditions of requests, under which they will be processed according to this rule:

-   Enable this rule — to make a rule effective, tick this field;
-   Name — name of the rule;
-   Perform action — select the [action](/en/docs/mt5/platform/administration/requests_routing/routing_rules#action) that should be executed with regard to the request that meets the rule conditions. For some actions an additional filed appears to the right of this one (for example, number of seconds and ticks for a delay);
-   Where request is — select a rule condition by the [type of request](/en/docs/mt5/platform/administration/requests_routing/routing_rules#request). In order to select or deselect all elements in the list, click the right mouse button;
-   Where order is — select a rule condition by the [type of order](/en/docs/mt5/platform/administration/requests_routing/routing_rules#order). In order to select or deselect all elements in the list, click the right mouse button;
-   Where conditions are — select [additional conditions](/en/docs/mt5/platform/administration/requests_routing/routing_rules#condition) to choose requests.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The rule conditions are taken into account according the to principle of "AND". In other words, in order for a request to be processed according to the rule, it must meet all the conditions specified in this rule.</span></li><li class="p_tableatten"><span class="f_tableatten">The rule conditions must not contradict each other. For example, if you indicate the following two group conditions in one rule: \real* and demo\*, none of the trading requests will correspond to this rule. A request cannot belong to a demo account and a real one at the same time.</span></li></ul></td></tr></tbody></table>

A separate block is included for adding additional conditions. If you press "Add" a new line will be created in the table. Indicate the following in it:

-   Type — parameter, according to which the condition will be checked;
-   Condition — condition of rule triggering (equal, not equal, etc.);
-   Value — value the condition parameter is compared to.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Be attentive when specifying conditions, For example, if you select the "Symbol" type, you can't set the condition "more than or equal to" (&gt;=), etc. Otherwise the condition is incorrect and is not processed.</span></p></td></tr></tbody></table>

To edit an additional condition, select it and press "Edit" or double click on one of its parameters. To delete a condition press the "Delete" button or the Delete key.

## Dealers [#](requests_routing#dealers)

![Dealers](/en/docs/mt5/platform/img/routing_dealers.png "Dealers")

There is an [action](/en/docs/mt5/platform/administration/requests_routing#action) performed by the request, at which it is sent to a dealer or a gateway to be handled - "Process to dealers". Requests processed by such a rule are enqueued to be processed by dealers specified in this tab.

-   Add — add a dealer. A new line appears in the table as soon as you press this button. In the "Login" field select one of [managers' accounts](/en/docs/mt5/platform/administration/admin_managers) from the list. Only accounts with permissions to [modify orders](/en/docs/mt5/platform/administration/admin_managers#modify_orders) are shown in this list. The "Name" field is filled out automatically;
-   Delete — delete a selected dealer. The same action can be performed by pressing the "Delete" key;
-   Edit — edit a selected point. The same action can be performed by a double click on the field the login is specified in.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Only a <a href="/en/docs/mt5/platform/administration/admin_gateways" class="topiclink">gateway</a> or a manager account with the <a href="/en/docs/mt5/platform/administration/admin_managers#dealing_permission" class="topiclink">"Dealing"</a> permission can be added to the list of dealers.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The list of dealers provides a special "ECN" item. Use this option to forward trade requests to <a href="/en/docs/mt5/platform/administration/ecn/ecn_matching" class="topiclink">ECN matching</a>.</span></li></ul></td></tr></tbody></table>

To save the settings press "OK". If you press "Cancel", the changes will not be saved.

### Sending requests to multiple dealers [#](requests_routing#multiple_dealers)

You can configure routing rules to forward request to multiple dealers/gateways at a time. For example, you can be using several gateway instances to connect to the same external system. in this case, each of the gateways uses its own account in the trading system, to which only operations from certain MetaTrader 5 accounts are forwarded.

![Multiple gateways in one rule](/en/docs/mt5/platform/img/routing_multiple_dealers.png "Multiple gateways in one rule")

In such cases, the routing system attempts to automatically send the request to the appropriate gateway.

1\. The server determines gateway/dealer priority: to which one the request should be sent in the first place. This is done based on the [external accounts data of the account](/en/docs/mt5/platform/administration/admin_accounts/account_edit#trade_accounts) from which the request is received.

![Gateway priority is determined using external accounts](/en/docs/mt5/platform/img/routing_multiple_dealers_accounts.png "Gateway priority is determined using external accounts")

If the gateway from the routing rule is indicated in symbol settings, the request will be forwarded to this gateway.

If the gateway refuses the request for some reason or returns it, the request will be forwarded to other gateways. The gateway that captures the request first will process it.

2\. If a certain dealer/gateway refuses to process the request (for example, if processing contradicts the gateway's internal logic), the request is deleted from the dealer's/gateway's list. After that the request can be picked up by another dealer/gateway from the rule list.

For example:

-   The rule sets the action "Process to online dealers". Two gateways are indicated in the dealers list: gateway 1 and gateway 2.
-   Both gateways are currently online. A request is assigned to these connections.
-   Gateway 1 picks up the request and refuses it.
-   The requests is removed from the gateway 1 list and is forwarded to gateway 2.
-   Gateway 2 captures the request and processes it.

If gateway 2 also refuses the request, it will be deleted from the its list as well. Since there will be no gateways left to process the request, the server will reject the request and will add a corresponding log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">request</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">rejected,</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">due</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">all</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">assigned</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">dealers</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">returned</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">request</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">in</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">queue</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">(instant</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">buy</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">4</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">EURUSD</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">at</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">1.08700)</span></p></td></tr></tbody></table>

General example for the operation scheme:

-   If the request is assigned to only one gateway (and to no one else) in the rule, the request goes to this gateway.
-   If multiple gateways are assigned in the rule (and only gateways), the request goes to the one whose ID is found in the external accounts list. Gateways are checked in the same order as they are indicated in the rule.
-   If there is no such a gateway, the request is sent to the first gateway in the rule list (for which the request has not been deleted and is available).
-   If multiple gateways and dealers are assigned in the rule, gateways are checked first (in the same order used in group settings): gateways specified in the external accounts list of the account are searched. If such a gateway is found, the request is sent to that gateway.
-   If the gateway refuses the gateway, it will be processed according to the rules specified above.
-   If no priority gateway is found, the request will be passed to the gateway or dealer who first captures the request from the queue.

## Context Menu [#](requests_routing#context)

The context menu of the "Routing" tab allows executing the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new rule;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit a selected rule;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected rule;
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move a selected rule up relative to others;
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move a selected rule down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   ![Enable](/en/docs/mt5/platform/img/enable_configuration_icon.png "Enable") Enable — enable the selected configuration.
-   ![Disable](/en/docs/mt5/platform/img/disable_configuration_icon.png "Disable") Disable — disable the selected configuration.
-   Automation triggers — create an [automation](/en/docs/mt5/platform/administration/automation) task for the selected event or edit an existing one. The menu displays only the triggers and tasks associated with the current section.
-   Automation actions — add an automation action to an existing task or create a new task based on the action. The menu displays only the actions associated with the current section.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) routing settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) routing settings to a file.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table with the rules.

[Matching History](/en/docs/mt5/platform/administration/ecn/ecn_matching_history)

[Actions and Conditions](/en/docs/mt5/platform/administration/requests_routing/routing_rules)