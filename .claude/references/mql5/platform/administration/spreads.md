# Spreads

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/spreads

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Spreads

# Spreads

This section allows users to configure the charging of the margin in case client's trading positions are in a spread to one another. Being in a spread means the presence of the oppositely directed positions on related symbols. Reduced margin requirements for positions in a spread present traders with wider trading opportunities.

![Spreads](/en/docs/mt5/platform/img/spreads.png "Spreads")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Spread settings are only used on <a href="/en/docs/mt5/platform/administration/admin_groups/group_position#netting" class="topiclink">netting</a> accounts.</span></p></td></tr></tbody></table>

## Creating and Editing a Spread

To create a Spread, click "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" or "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" in ["Edit"](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu of ["Standard"](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) panel or in the context menu of this section.

![Editing a spread](/en/docs/mt5/platform/img/spread_edit.png "Editing a spread")

### Margin Calculation Type

First of all, a type of margin charging should be specified for a spread.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">For all calculations types except Maximal, the specified margin is charged per unit of spread — specified combination of positions. If any part of the position does not fit in the spread, an additional margin is charged according to <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin" class="topiclink">symbol</a> settings. If the client's current positions have the volume the mentioned combination fits in several times, the charged margin is increased appropriately. For example, two instruments A and B are in a spread with the ratio of 1 and 2. If a client has positions by those instruments of 3 and 4 lots respectively, the total margin will be equal to the doubled value of the spread configuration (two spreads: 1 lot of A and 2 lots of B, 1 lot of A and 2 lots of B) plus the margin for one left lot of A instrument.</span></li><li class="p_tableatten"><span class="f_tableatten">The values are displayed in the margin currency (excluding CME Inter Spread where ratios are specified). It is assumed that the margin currency of all spread symbols is the same.</span></li></ul></td></tr></tbody></table>

Value

When this type is selected, the appropriate margin values that will be charged at the specified combination of positions are set in "Initial margin" and "Maintenance margin" fields.

Example:

-   Initial and maintenance margins are set at 2 000;
-   two symbols (GAZR-9.12 having the ratio of 2 and GAZR-3.13 having the ratio of 1) form the spread;

When a client has an opposite directed positions at GAZR-9.12 and GAZR-3.13 with the volume 2 and 1 lot respectively, the margin of 2 000 units will be charged. With the volume of 4 and 2 lots, the margin of 4 000 units will be charged.

Maximal

When this type is selected, the values of initial and maintenance margins will be calculated for each spread leg. The calculation is performed by summing up the margin requirements for all symbols of the leg. The margin requirements of the leg having a greater value will be used for the spread.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In this mode the total volume of positions on each side is considered, not only covered volume. Ratio for symbols in the spread legs cannot be specified in this mode.</span></p></td></tr></tbody></table>

Example:

-   two symbols GAZR-9.12 and GAZR-3.13 form the spread;
-   for GAZR-9.12 symbol, the values of initial and maintenance margins are equal to 2 000;
-   for GAZR-3.13 symbol, the values of initial and maintenance margins are equal to 2 100.

When a client has an opposite directed positions at GAZR-9.12 and GAZR-3.13 with the volume of 2 and 1 lot respectively, the margin of 4 000 units will be charged.

CME Inter Spread

When this option is selected, ratios (multipliers) for the appropriate margin types should be selected in "Initial" and "Maintenance" fields. The final value of the margin is defined by summing up the margin requirements for all spread symbols and multiplying the obtained value by the specified ratio.

Example:

-   two symbols (GAZR-9.12 having leg A and ratio of 2 and GAZR-3.13 having leg B and the ratio of 1) form the spread;
-   for GAZR-9.12 symbol, the values of initial and maintenance margins are equal to 2 000;
-   for GAZR-3.13 symbol, the values of initial and maintenance margins are equal to 2 100;
-   The ratios of 0.5 are specified in spread settings in Initial and Maintenance fields.

The final value of the initial and maintenance margins will be calculated the following way: (2 000 \* 2 + 2 100) \* 0.5 = 3 050.

CME Intra Spread

When this option is selected, the margin is calculated the following way: the difference between the total margin of A leg symbols and the total margin of B leg symbols is calculated (the difference in absolute magnitude is used, so that it does not matter what leg is a deductible one). According to the type of the calculated margin, the value specified in "Initial" or "Maintenance" field is added to the obtained difference.

Example:

-   two symbols (GAZR-9.12 having leg A and ratio of 2 and GAZR-3.13 having leg B and the ratio of 1) form the spread;
-   for GAZR-9.12 symbol, the values of initial and maintenance margins are equal to 2 000;
-   for GAZR-3.13 symbol, the values of initial and maintenance margins are equal to 2 100;
-   The values of 500 are specified in spread settings in Initial and Maintenance fields.

Maintenance and initial margin will be calculated the following way: (2 000 \* 2 - 2 100) + 500 = 2 400.

### Spread Legs

The next step is configuring spread legs. The legs are oppositely directed positions in a spread — buy or sell. To create a leg, click "Add".

![Creating a spread leg](/en/docs/mt5/platform/img/spread_leg.png "Creating a spread leg")

Select A or B leg to be configured. The leg type is not connected to some definite position direction (buy or sell). Note that client's positions at all leg's symbols should be either long or short.

Several symbols can be configured for each leg. A volume ratio at this spread leg can be specified for each of them.

Example:

-   leg A consists of GAZR-9.12 and GAZR-3.13 symbols having the ratios of 1 and 2 respectively
-   leg B consists of GAZR-6.13 symbol having the ratio of 1.

To keep the client's positions in the spread, the client should open positions of 1 and 2 lots for GAZR-9.12 and GAZR-3.13 respectively to one direction and position of 1 lot for GAZR-6.13 to another direction.

Symbols for a leg can be specified as some definite symbol ("Symbol" option) or as an underlying asset ("Basis") in case there are quite a lot of symbols in the spread.

If an underlying asset is specified for the leg, all symbols with this underlying asset are considered ("Basis" field in [symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common)). In this case, symbols can be additionally filtered by the time of their operation (specified in "From" and "To" fields of ["Sessions"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions) tab). To do this, specify the time interval in "Start period" and "End period" fields. To be able to use the symbol, its expiration date ("To" field) should be in the specified interval. To make the date open, uncheck the box in the Start or End period field.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the start and end dates are not specified, all symbols with the specified underlying asset will be used without considering their expiration date.</span></p></td></tr></tbody></table>

## Context Menu [#](spreads#context)

The context menu of "Spreads" section contains the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new spread configuration;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit the selected configuration;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete the selected configuration;
-   ![Move up](/en/docs/mt5/platform/img/move_up_button.png "Move up") Move up — move the selected configuration up relative to others;
-   ![Move down](/en/docs/mt5/platform/img/move_down_button.png "Move down") Move down — move the selected configuration down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) the settings of spreads to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) the settings of spreads to a file.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled, the size of columns will be selected automatically;
-   Grid — show/hide grid to separate the table fields.

[Collateral Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_collateral)

[1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)