# Specifying Symbols and Groups

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/common_info/common_mask

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[General Information](/en/docs/mt5/platform/administration/common_info)Specifying Symbols and Groups

# Specifying Symbols and Groups

A standard way of specifying [symbols](/en/docs/mt5/platform/administration/admin_symbols) and [groups](/en/docs/mt5/platform/administration/admin_groups) is used in different sections of the server administration:

![Symbols Specifying](/en/docs/mt5/platform/img/symbol_indication.png "Symbols Specifying")

The mask ("\*" symbol) and paths to financial instruments and groups are used here, since they can have certain hierarchy in the system. For example, there is a group of instruments "Forex" that has symbols in it divided into the "Majors" and "Crosses" sections. In order to specify all the symbols from the "Majors" group, the following entry is necessary — "Forex\\Major\\\*". This kind of paths are substituted automatically if a group or symbol is chosen from the list. The "\*" symbol means all the instrument/groups from the specified group.

## "\*" Mask and "!" Negation Sign [#](common_mask#mask)

The "\*" mask and the '!' negation sign are used for making extended requests. For example, they can be used when specifying symbols to be translated from a [data feed](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#symbols) or a [gateway](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#translation), when specifying symbols for the [synchronization of price data](/en/docs/mt5/platform/administration/admin_synchronization#symbols) and when [configuring holidays](/en/docs/mt5/platform/administration/admin_holidays#symbols). Here are several examples of specification:

-   ,\*, — all the symbols;
-   ,EUR\* —  all the symbols where EUR is the base currency;
-   ,EUR\*,!EURUSD — all the symbols where EUR is the base currency except EURUSD;
-   ,EURUSD,GBPUSD — only specified symbols. One can specify any number of symbols separated by comma;
-   ,\*USD — all the symbols where USD is the quoting currency.

To exclude symbols using "!" on data feeds and gateways, you should specify the full path of these symbols. For example, to specify all symbols from the Cboe FX subgroup, except for the EURUSD symbol located in the same subgroup, use the string "Cboe FX\\\*,!Cboe FX\\EURUSD". The string "Cboe FX\\\*,!EURUSD" will be invalid. Also, the exception does not work for a single "\*" mask. It always allows all symbols:

-   Forex\\\*,!Forex\\EURUSD — all symbols in the Forex subgroup, except EURUSD.
-   \*,!Forex\\EURUSD — all symbols. The EURUSD symbol will not be excluded.

[Working with Instructions](/en/docs/mt5/platform/administration/common_info/common_instructions)

[Data Export](/en/docs/mt5/platform/administration/common_info/export)