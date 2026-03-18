# Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols

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
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
                -   [Symbol Settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings)
                -   [Splicing Futures](/en/docs/mt5/platform/administration/admin_symbols/symbols_splice)
                -   [Import of Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_import)
                -   [Collateral Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_collateral)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Symbols

# Symbols

This section is devoted to the management of symbols in the trading system. The possibility of structuring symbols in groups is available here.

![Symbols](/en/docs/mt5/platform/img/symbols.png "Symbols")

The structure of symbols can be viewed in the left part of the administrator terminal. The right part reflects group or symbols included into a selected group of a higher order. Information about symbols is represented in four columns:

-   Symbol — symbol name;
-   Type — group of the highest order to which the symbol is included;
-   Execution — type of trade operation execution for this symbol;
-   Digits — number of decimal places in the symbol price.

## Managing Groups of Symbols [#](admin_symbols#groups)

To create a new group, select a group of higher level, in which the new group should be created. To create a rout group, select the Symbols section. After that call the context menu and execute the "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" command specifying the name of the new group.

![Groups of symbols](/en/docs/mt5/platform/img/symbol_group_add.png "Groups of symbols")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">After a group of symbols has been created, you will not be able to change its name.</span></li><li class="p_tableatten"><span class="f_tableatten">Symbol group name cannot contain any punctuation marks or special characters (allowed are ".", "_", "&amp;" and "#"). It's not recommended to use the following characters in the symbol names: &lt;, &gt;, :, ", /, |, ?, *.</span></li></ul></td></tr></tbody></table>

If you need to delete a group, select it in the right part of the "Symbols" section and press "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete" in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the [context menu](/en/docs/mt5/platform/administration/admin_symbols#context):

![Deleting a group of symbols](/en/docs/mt5/platform/img/symbol_groups_delete.png "Deleting a group of symbols")

## How to Manage Symbols [#](admin_symbols#symbols_manage)

Symbols are managed in the right part of the administrator terminal.

-   Adding  
    In order to add a symbol, enter the necessary group and execute the "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" command in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [toolbar](/en/docs/mt5/platform/administrator/interface/toolbar) or in the context menu. After that the window of [symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings) will be opened.
-   Editing  
    In order to edit a symbol, select it and execute the "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" command of the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the context menu. After that the window of [symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings) will be opened. The symbol editing window can be opened by double clicking on the symbol in the list. You can also edit several symbols [at the same time](/en/docs/mt5/platform/administration/common_info/common_instructions#groupwork). To do this, select symbols using the mouse and "Ctrl" or "Shift", and then execute the "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" command.
-   Deleting  
    In order to delete a symbol, select it and execute the "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete" command in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the context menu. You can delete several symbols at the same time, selecting them using the mouse and "Ctrl" or "Shift".
-   Sorting  
    Symbols and symbol groups can be sorted alphabetically. The feature of sorting is that it is performed on the server, not on the local MetaTrader 5 Administrator. To sort symbols execute the "![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically" command in the context menu. Once it is done, the confirmation window will appear. In it you can choose whether the symbol groups should also be sorted or not.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">We strongly recommend to perform changes of financial symbols only on weekends or holidays, when markets are closed.</span></li><li class="p_tableatten"><span class="f_tableatten">Additional general information about working with configuration records is given in the <a href="/en/docs/mt5/platform/administration/common_info/common_instructions" class="topiclink">"Working with Instructions"</a> section.</span></li></ul></td></tr></tbody></table>

## Symbol filtering and batch editing [#](admin_symbols#filter)

You can [edit the settings of multiple symbols](/en/docs/mt5/platform/administration/common_info/common_instructions#groupwork) at a time. Select the required symbols in the list and click "Edit" in the context menu.

To bulk edit symbols which are in different subcategories, use the filter tab at the bottom of the window. Specify a comma separated list of symbols or a mask, for example:

-   EURUSD, GBPJPY — two specified symbols
-   EUR\*, GBP\* — the symbols with the names beginning with EUR and GBP
-   \*USD, !GBPUSD — all symbols with USD as the second currency except for GBPUSD

Select the desired symbols from the filtered list and edit:

![To edit settings in bulk, you can select symbols by filter](/en/docs/mt5/platform/img/symbols_filter.png "To edit settings in bulk, you can select symbols by filter")

## Creating Symbol Copies [#](admin_symbols#copy)

To implement different execution conditions for the same instruments, you can create symbol copies. Select the required symbols from the list and click "Add Copy" in the context menu.

![Select Symbols to Create Copies](/en/docs/mt5/platform/img/symbols_add_copy_menu.png "Select Symbols to Create Copies")

Next, specify the postfix that will be appended to the names of all symbols in the new set. Also, define the name of the subfolder where the symbol copies will be placed.

![Creating Symbol Copies](/en/docs/mt5/platform/img/symbols_add_copy.png "Creating Symbol Copies")

After creating the symbol copies, adjust their settings as needed.

You can also create symbol copies using [batch editing](/en/docs/mt5/platform/administration/admin_symbols#filter). Select the required symbols from the list, click "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit")Edit" in the menu, and then specify the postfix in the "Symbol" field. The postfix must begin with a period (.). For example, if you select the symbols EURUSD, USDJPY, GBPUSD and add the postfix .x (EURUSD.x) in the group editing window, you will get copies of the symbols: EURUSD.x, USDJPY.x and GBPUSD.x.

## Context Menu [#](admin_symbols#context)

The context menu of the "Symbols: section contains the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — [add](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings) a new symbol.
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — [edit](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings) a selected symbol or open a selected group.
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected symbol or group.
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move a selected symbol up relative to others. This sorting is saved on the server. To sort the list of symbols temporarily, click on the heading of any column. When temporary sorting is enabled, the symbol moving up/down buttons become inactive.
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move a selected symbol down relative to others. This sorting is saved on the server. To sort the list of symbols temporarily, click on the heading of any column. When temporary sorting is enabled, the symbol moving up/down buttons become inactive.
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort alphabetically — [sort](/en/docs/mt5/platform/administration/admin_symbols#sort) configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   Automation triggers — create an [automation](/en/docs/mt5/platform/administration/automation) task for the selected event or edit an existing one. The menu displays only the triggers and tasks associated with the current section.
-   Automation actions — add an automation action to an existing task or create a new task based on the action. The menu displays only the actions associated with the current section.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) symbol settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) symbol settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from Server — start [importing symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_import) from a remote MetaTrader 5 or MetaTrader 4 server.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Charts](/en/docs/mt5/platform/img/bars_icon.png "Charts") Charts — request the [minute history](/en/docs/mt5/platform/administration/admin_charts). This opens the relevant section with the name of the selected symbol automatically specified in the request field.
-   ![Ticks](/en/docs/mt5/platform/img/ticks_icon.png "Ticks") Ticks — request the [tick history](/en/docs/mt5/platform/administration/admin_ticks). This opens the relevant section with the name of the selected symbol automatically specified in the request field.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window.
-   Auto Arrange — if this option is enabled the size of columns is selected automatically.
-   Grid — this option shows/hides field separators in the table with symbols.

[Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)

[Symbol Settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings)