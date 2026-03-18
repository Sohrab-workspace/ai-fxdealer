# Importing and Setting Financial Instruments

> Source: https://support.metaquotes.net/en/docs/mt5/platform/migration/migration_symbols

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Migration from MetaTrader 4](/en/docs/mt5/platform/migration)Financial Instruments

# Importing and Setting Financial Instruments

Please keep in mind the following when working with MetaTrader 5 symbols:

-   Unlike MetaTrader 4, the fifth version allows you to create symbol groups (similar to Securities in MetaTrader 4) directly in Symbols section. Moreover, you can create a tree-like symbol structure.
-   In MetaTrader 5, it is not necessary to collect individual symbol into groups. However, it is still recommended to divide symbols into some logical groups to make system administration more convenient.
-   MetaTrader 5 has no limitations on the number of financial instruments and their groups.

## Importing Symbols

Use the [import of symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_import) to copy all symbols and their settings from MetaTrader 4 server to the MetaTrader 5 platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you import symbols, existing settings are converted and default values are assigned to missing settings.</span></p></td></tr></tbody></table>

![Importing symbols from MetaTrader 4 server](/en/docs/mt5/platform/img/migration_symbol.png "Importing symbols from MetaTrader 4 server")

Select "MetaTrader 4" server type and specify connection data: IP address and server port, as well as account login and password. The account used for importing symbols may be opened in any group except for a manager one ("manager"). The group, in which the account is opened, should have access to all symbols to be imported from MetaTrader 4 server.

![Importing symbols from MetaTrader 4 server](/en/docs/mt5/platform/img/migration_symbol_import.png "Importing symbols from MetaTrader 4 server")

The next window shows the list of all symbols that can be imported from MetaTrader 4 server. Selected symbols are imported to MetaTrader 5 platform after pressing Import button.

In case of successful import, the symbols appear in the Symbols section of the group, from which the import command has been called.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">By default, all imported symbols are not available for trading.</span></li><li class="p_tableatten"><span class="f_tableatten">Check the settings carefully before making any symbol available for trading.</span></li></ul></td></tr></tbody></table>

In order to distribute imported symbols among symbol groups, select the necessary symbols and drag them by mouse to a necessary group (or subgroup).

## Configuring the Symbols

All symbol settings from MetaTrader 4 are automatically converted to the appropriate symbol settings for MetaTrader 5. Since the MetaTrader 5 platform features the new parameters that are not present in MetaTrader 4, such parameter values are set to default ones for each symbols imported from MetaTrader 4.

"Percentage" value used to calculate the margin in the MetaTrader 4 symbol settings (Calculation tab) has been redefined and expanded in MetaTrader 5. Therefore, it is not imported. In MetaTrader 5, you can assign the necessary ratio for each trading operation type and direction separately:

![Margin ratios for a symbol in MetaTrader 5](/en/docs/mt5/platform/img/migration_symbol_margin.png "Margin ratios for a symbol in MetaTrader 5")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Due to differences in <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex_hedge#hedged" class="topiclink">hedged margin</a> calculation between the platforms, the hedged margin value is doubled during the import making margin calculation in MetaTrader 5 similar to the one in MetaTrader 4.</span></p></td></tr></tbody></table>

"Filtration level" in MetaTrader 4 symbol filtration settings is inserted into "Soft filtration level" in the MetaTrader 5 symbol settings. Its five-fold value is used as "hard filtration level" parameter, while the hundred-fold one — as "Discard filtration level".

![Importing filtration settings to MetaTrader 5](/en/docs/mt5/platform/img/migration_symbol_filter.png "Importing filtration settings to MetaTrader 5")

The minimum and maximum volume, as well as step in MetaTrader 5 are set by default.

## History Data Synchronization between MetaTrader 5 and MetaTrader 4

After importing the symbols, you can download history data for them from your MetaTrader 4 Server. There are some synchronization features to be considered before the start of the process:

-   In order to synchronize history data with MetaTrader 4 server, the latter should have at least one demo group. The group can be disabled.
-   MetaTrader 5 history data is stored only as 1-minute data and converted programmatically into larger timeframes on request from the client terminal, while MetaTrader 4 stores different timeframes.
-   When synchronizing with MetaTrader 4 servers, the system consistently selects the most complete data beginning from one-minute timeframe.  
    M1 data is fully taken first. Next, the system attempts to receive the missing part from H1 data. MetaTrader 4 server's hour reading is recorded to the first minute of an hour at MetaTrader 5 server. After that, the attempt is made to receive missing data from D1 timeframe. Daily data of MetaTrader 4 server (for example, 01.03.2009) is recorded to the first minute of a day at MetaTrader 5 server (for example, 01.03.2009 00:00).  
    Therefore, clients will be able to receive a complete chart for a historical period only on the timeframe, from which the data has been imported.

![Synchronization scheme](/en/docs/mt5/platform/img/synchronization_scheme.png "Synchronization scheme")

Before launching synchronization, specify the source server (your MetaTrader 4 Server) in [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization) section of MetaTrader 5 Administrator. The Symbols tab allows you to specify the symbols, the data for which is to be synchronized.

![Synchronizing history data with MetaTrader 4 server](/en/docs/mt5/platform/img/migration_sync.png "Synchronizing history data with MetaTrader 4 server")

To start synchronization, select Services -> Synchronize History in the terminal's main menu.

Data synchronization process can be tracked in the history server [journal](/en/docs/mt5/platform/administration/admin_network/network_journal). To do this, enter "Synchronization" (without the quotes) in the search bar of the filtration settings, set Full for a request type and All for an event type, specify the current day and click Request. The following journal entry indicates the completion of a synchronization process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">history</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">synchronization</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">with</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">xxx.xxx.xxx.xxx:xxx</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">finished</span></p></td></tr></tbody></table>

Synchronized data can be seen in [Charts](/en/docs/mt5/platform/administration/admin_charts) section of MetaTrader 5 Administrator.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">MetaTrader 5 has no limitations on the depth of history data and the number of symbols.</span></p></td></tr></tbody></table>

[General Settings](/en/docs/mt5/platform/migration/migration_general)

[Trade Groups](/en/docs/mt5/platform/migration/migration_group)