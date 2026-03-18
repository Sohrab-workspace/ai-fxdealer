# Holidays

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_holidays

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Holidays

# Holidays

In this section you can add holidays to the working time schedule both for symbol groups and separate symbols. During holidays clients can connect, watch charts and trading history, but cannot conduct trade operations.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/platform/administration/admin_feeds" class="topiclink">Data feeds</a> that receive quotes only are automatically disabled on holidays. As soon as a holiday is over, the data feeds are automatically enabled. Data feeds that receive news keep working.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Holiday settings do not affect <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps" class="topiclink">swap calculation</a>.</span></li></ul></td></tr></tbody></table>

Holidays are represented like this:

![Holidays](/en/docs/mt5/platform/img/holidays.png "Holidays")

In order to add or edit a holiday, press "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" or "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit", respectively. These buttons are located in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar and in the [context menu](/en/docs/mt5/platform/administration/admin_holidays#context). The window of holiday settings will be opened as soon as you press them.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Additional general information about working with configuration records is given in the <a href="/en/docs/mt5/platform/administration/common_info/common_instructions" class="topiclink">"Working with Instructions"</a> section.</span></p></td></tr></tbody></table>

## Common [#](admin_holidays#common)

![Common](/en/docs/mt5/platform/img/holidays_common.png "Common")

The following parameters are set up here:

-   Enable — enable/disable a holiday;
-   Every year — enable holiday repeating every year. For such holidays "\*\*\*\*" is shown instead of the year;
-   Date — date of the holiday. A date is selected via a calendar that is opened upon pressing ![Calendar](/en/docs/mt5/platform/img/calendar_button.png "Calendar"). The date can also be entered manually;
-   Work time — server work time on the holiday. If there is no working time on this day, leave zero values in these fields;
-   Description — text description of the holiday.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The delivery of quotes and trading continue until the last minute of the working time range inclusive. For example, if the specified range is from 00:00 to 18:00, then the actual working time is 00:00:00  18:00:59.</span></p></td></tr></tbody></table>

## Symbol [#](admin_holidays#symbols)

![Symbols](/en/docs/mt5/platform/img/holidays_symbols.png "Symbols")

here you should specify symbols or groups of symbols, for which this holiday will be effective:

-   Add — add symbols. As soon as you press this button, a new field will appear in this window. Click on this field and select a symbol or group from the appeared list of symbols available on the server. To specify all symbols, select the "Symbols" point. Read more details in ["Specifying Symbols"](/en/docs/mt5/platform/administration/common_info/common_mask);
-   Delete — delete a selected symbol or group of symbols;
-   Edit — edit a selected symbol or group of symbols.

To complete creation or editing of a holiday press "OK". If you press "Cancel", the window will be closed, while changes will not be saved.

In order to delete a holiday, select it and press "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete" in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit#delete) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the context menu.

## Holidays Check

Holiday rules are checked from top downward. If any rule allows trading for a symbol in the specified interval, all further rules will be ignored for this symbol-interval binding. Thus:

-   It is not possible to override an allowing rule by subsequent prohibiting rules.
-   It is possible to override a prohibiting rule by subsequent allow rules.

![Example of Holidays setup](/en/docs/mt5/platform/img/holidays_example.png "Example of Holidays setup")

Let's consider example:

-   The first rule prohibits trading for all symbols on January 1, 2014
-   The second rule allows trading for Forex group symbols from 10:00 to 12:00 on that day
-   The third rule allows trading for the same symbols from 13:00 to 22:00
-   The fourth rule prohibits trading for all symbols on January 1, 2014.

As a result, on January 1, 2014, trading will be allowed for Forex group symbols from 10:00 to 12:00 and from 13:00 to 22:00. The fourth rule is ignored for the earlier allowed intervals as the check for these intervals stopped after the rules allowing trading for them.

Thus, in order to set several trading intervals inside one time interval, you should first set a prohibitive rule followed by permissive ones.

## Context Menu [#](admin_holidays#context)

The context menu of Holidays contains the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new holiday;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit a selected holiday;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected holiday;
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move the selected holiday up relative to others;
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move the selected holiday down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) holidays settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) holidays settings to a file.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table.

[Time](/en/docs/mt5/platform/administration/admin_time)

[Leverages](/en/docs/mt5/platform/administration/leverages)