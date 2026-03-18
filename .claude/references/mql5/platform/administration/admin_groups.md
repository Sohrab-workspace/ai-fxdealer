# Groups

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups

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
                -   [Group Settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings)
                -   [Group Symbol Settings](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols)
                -   [Commission Settings](/en/docs/mt5/platform/administration/admin_groups/groups_comissions)
                -   [Group Types](/en/docs/mt5/platform/administration/admin_groups/group_types)
                -   [Import of Groups](/en/docs/mt5/platform/administration/admin_groups/group_import)
                -   [Extended Authentication Setup](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication)
                -   [Position Accounting Systems](/en/docs/mt5/platform/administration/admin_groups/group_position)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Groups

# Groups

All the system users are divided into groups. There can be no users on the server, who are not included into any of groups. The system contains the following default structure of groups:

-   demo — section for [demo](/en/docs/mt5/platform/administration/admin_groups/group_types#demo) groups;

-   demoforex — groups of demo groups for FOREX
-   managers — section for [manager](/en/docs/mt5/platform/administration/admin_groups/group_types#manager) groups;

-   administrators — group of administrators' accounts (maximal permissions in the system);
-   dealers — group of dealer accounts;
-   real — section for [real](/en/docs/mt5/platform/administration/admin_groups/group_types#real) groups;

-   real — group of accounts for live trading.
-   preliminary — group where [preliminary](/en/docs/mt5/platform/administration/admin_groups/group_types#preliminary) accounts are created, when a request for opening a real account is sent from the client terminal.

![Groups](/en/docs/mt5/platform/img/groups.png "Groups")

The groups are represented in a table with the following fields:

-   Group — group title;
-   Server — [trade server](/en/docs/mt5/platform/administration/admin_network) that serves this group;
-   Authorization — method of authorization fro this group;
-   Currency — default [deposit currency](/en/docs/mt5/platform/administration/admin_groups/groups_settings#currency) for this group. Then you can change the deposit currency for any account.

## Hierarchy of Groups [#](admin_groups#hierarchy)

Groups of accounts can be divided into sections and sub-sections depending on their types. There are three default sections: "demo", "managers" and "real". Group sections are created when groups are created.

![Adding a Section](/en/docs/mt5/platform/img/group_section_add.png "Adding a Section")

In the "Groups" section select "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" which will open a dialog window. In the ["Name"](/en/docs/mt5/platform/administration/admin_groups/groups_settings#name) field specify path to the group. For example, if you specify "real\\IB\\realUSD" in section "real" the sub-section "IB" will be created with group "realUSD" inside it. If one or several higher level sections do not exist by the moment of group creation, they will be created.

in order to delete a sections, delete all groups inside it.

## Managing Groups

Groups management is performed in the right part of the administrator terminal.

-   Add  
    In order to add a group, enter the corresponding section and execute the "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" command in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [toolbar](/en/docs/mt5/platform/administrator/interface/toolbar) or in the context menu. After that the window of [group setting](/en/docs/mt5/platform/administration/admin_groups/groups_settings) will be opened.
-   Edit  
    In order to edit a group, select it and execute the "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" command in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [toolbar](/en/docs/mt5/platform/administrator/interface/toolbar) or in the context menu.  After that the window of [group setting](/en/docs/mt5/platform/administration/admin_groups/groups_settings) will be opened. The group editing window can be called by a double left click on its name in the list. You can also edit several groups [together](/en/docs/mt5/platform/administration/common_info/common_instructions#groupwork). To do this select them using the mouse and keys "Ctrl" or "Shift", and execute command "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit".
-   Delete  
    In order to delete a group, select it and execute the "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete" command in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or the context menu. You can delete several groups at once by selecting them using the mouse and keys "Ctrl" or "Shift".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">You can't delete a group that contains at least one <a href="/en/docs/mt5/platform/administration/admin_accounts" class="topiclink">account</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Additional general information about working with configuration records is given in the <a href="/en/docs/mt5/platform/administration/common_info/common_instructions" class="topiclink">"Working with Instructions"</a> section.</span></li></ul></td></tr></tbody></table>

## Context Menu [#](admin_groups#context)

The context menu in the list of groups allows executing the following commands:

-   Servers — using this command, one can filter the groups displayed in the list by the trade server they belong to. A list containing all trade servers of the platform will be opened as soon as it is executed.
-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new group;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit a selected group;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected group;
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move a selected group up relative to others;
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move a selected group down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   Automation triggers — create an [automation](/en/docs/mt5/platform/administration/automation) task for the selected event or edit an existing one. The menu displays only the triggers and tasks associated with the current section.
-   Automation actions — add an automation action to an existing task or create a new task based on the action. The menu displays only the actions associated with the current section.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) group settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) group settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_from_server_icon.png "Import") Import from Server — start [importing groups](/en/docs/mt5/platform/administration/admin_groups/group_import) from a remote MetaTrader 5 or MetaTrader 4 server;
-   Request —  open the sub-menu for requesting [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) entries for the selected group:

-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request all journal entries on the group;
-   Orders — request journal entries about the [orders](/en/docs/mt5/platform/administration/admin_orders) of the group;
-   Deals — request journal entries about the [deals](/en/docs/mt5/platform/administration/admin_deals) of the group;
-   Positions — request journal entries about the [positions](/en/docs/mt5/platform/administration/admin_positions) of the group;
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table with groups.

[Leverages](/en/docs/mt5/platform/administration/leverages)

[Group Settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings)