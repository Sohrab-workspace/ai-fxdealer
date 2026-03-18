# Working with Instructions

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/common_info/common_instructions

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
                -   [Trading System](/en/docs/mt5/platform/administration/common_info/general_concept)
                -   [Price Data](/en/docs/mt5/platform/administration/common_info/price_data)
                -   [Working with Instructions](/en/docs/mt5/platform/administration/common_info/common_instructions)
                -   [Specifying Symbols and Groups](/en/docs/mt5/platform/administration/common_info/common_mask)
                -   [Data Export](/en/docs/mt5/platform/administration/common_info/export)
                -   [Import/Export Settings](/en/docs/mt5/platform/administration/common_info/import_export_config)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[General Information](/en/docs/mt5/platform/administration/common_info)Working with Instructions

# Working with Instructions

There are several methods of working with instructions in different sections of platform administration. Depending on the selected section of administering, the instruction can be an [account](/en/docs/mt5/platform/administration/admin_accounts), a [group](/en/docs/mt5/platform/administration/admin_groups), a [holiday](/en/docs/mt5/platform/administration/admin_holidays), a directive that allows or prohibits [access](/en/docs/mt5/platform/administration/security/admin_access), etc.

## Creating Instructions on the Basis of Existing Ones

In order to avoid specifying common parameters of an instruction each time it is created, one can create it on the basis of an existing one by changing its key parameter. For example, if you open the "EURUSD" [symbol](/en/docs/mt5/platform/administration/admin_symbols) for editing by a double click of the mouse or using the "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" command, change its name to "EURGBP" and save it, you will get a new symbol with the settings similar to "EURUSD".

Key fields for different instructions are listed below:

-   [IP Access](/en/docs/mt5/platform/administration/security/admin_access) — "From", "To";
-   [Holidays](/en/docs/mt5/platform/administration/admin_holidays) — "Date", "Time", "Description";
-   [Groups](/en/docs/mt5/platform/administration/admin_groups/groups_settings) — "Name";
-   [Managers](/en/docs/mt5/platform/administration/admin_managers#common) — "Login";
-   [Routing](/en/docs/mt5/platform/administration/requests_routing) — "Name";
-   [Gateways](/en/docs/mt5/platform/administration/admin_gateways) — "Name";
-   [Plugins](/en/docs/mt5/platform/administration/admin_plugins) — "Name";
-   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#common) — "Name";
-   [Symbols](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common) — "Symbol";
-   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization#common) — "Server".

## Group Work with Instructions [#](common_instructions#groupwork)

The administrator terminal allows to change the settings of instructions of a selected section in bulk. To do it, one should select the necessary   instructions using the mouse with "Shift" and "Ctrl" keys and start editing them by executing the "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" command.

Some fields may be blocked when opening multiple instructions for editing. This means that those fields cannot be changed for multiple instructions simultaneously:

![Disabled Fields at Editing Settings](/en/docs/mt5/platform/img/group_work_symbols.png "Disabled Fields at Editing Settings")

At that the values of the very upper instruction are displayed in the rest of the fields. Any value of edited instructions is changed only if the user changes its value. All the other fields remain unchanged.

[Price Data](/en/docs/mt5/platform/administration/common_info/price_data)

[Specifying Symbols and Groups](/en/docs/mt5/platform/administration/common_info/common_mask)