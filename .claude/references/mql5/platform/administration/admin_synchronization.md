# Synchronization

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_synchronization

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
                -   [Synchronization Features](/en/docs/mt5/platform/administration/admin_synchronization/synchronization_features)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Synchronization

# Synchronization

Deep high-quality history is essential for traders. Historical data is used for technical analysis, as well as for creating and testing trading strategies. If you do not provide historical data, potential clients are likely to choose your competitors who do provide history.

With the MetaTrader 5 platform, you can easily solve the missing data issue. Minute bar and tick history on your server can be quickly synchronized with any other MetaTrader 5 and MetaTrader 4 server. For more details, please read the article [Deep Price History in MetaTrader 5 in a Few Clicks](https://support.metaquotes.net/en/articles/377).

![Synchronization](/en/docs/mt5/platform/img/synchronization.png "Synchronization")

## Setup

Data synchronization is performed through a regular client connection to an external MetaTrader 4/5 server. To access the data, you should open a demo account on the source server. The only special requirement for this account is ability to access trading symbols which your are going to synchronize. Connect to the external server via a client terminal using the created account to check all symbols available on this server. Next, execute the Symbols command in the context menu of the Market Watch window.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Please note that price data is protected as intellectual property. Therefore you should make sure that you have all the necessary agreements before you proceed with the synchronization.</span></li><li class="p_tableatten"><span class="f_tableatten">By default, your platform is already ready to synchronize data with the MetaQuotes-Demo server, and the corresponding configuration is available in the settings. This server stores deep history for 35 Forex pairs, 35 CFDs, as well as XAUUSD and XAGUSD metal price data. Historical data include Bid prices, spreads (which actually means the availability of Ask prices), and tick volumes. We recommend running synchronization by executing the "<img class="help" alt="Synchronize History" title="Synchronize History" width="14" height="14" src="/en/docs/mt5/platform/img/synchronize_history_button.png"> Synchronize History" command from the Services menu. This will provide the minimum required data to your traders. For more details, please read the article <a href="https://support.metaquotes.net/en/articles/377" target="_blank" class="weblink">Deep Price History in MetaTrader 5 in a Few Clicks</a>.</span></li></ul></td></tr></tbody></table>

Prior to starting synchronization, please make sure that the system time of your MetaTrader 5 server is accurate. The use of correct time will prevent discrepancies in quotes. Check platform settings under the [Time](/en/docs/mt5/platform/administration/admin_time#synchronization) section.

After completing the preparation, create a new configuration. Click ![Add](/en/docs/mt5/platform/img/add_button.png "Add")Add" in the toolbar and proceed with the setup.

### Common [#](admin_synchronization#common)

![Common](/en/docs/mt5/platform/img/synchronization_common.png "Common")

Specify here data for connection to the external server and synchronization parameters:

-   Enable — enable or disable synchronization with this server.
-   Server — server address and port separated by a colon.
-   Type — the type of the server, with which synchronization will be conducted - MetaTrader 4 or MetaTrader 5.
-   Login — the account number on the server with which you synchronize. Use a regular client account having access to required symbols, for connection.
-   Password — password to the account on the server with which you synchronize.
-   Mode — synchronization mode: Replace (replace all data and add what is missing), Merge (add only missing data).
-   Synchronize — data type to synchronize: [charts](/en/docs/mt5/platform/administration/admin_charts), [ticks](/en/docs/mt5/platform/administration/admin_ticks) or both.
-   Time zone correction — if MetaTrader servers are located in different time zones, the time in the received data can be corrected. The system can determine the time correction automatically. Optionally, the relevant value can be specified manually. Values from -24:00 to 24:00 are valid. Please see [Time zone correction](/en/docs/mt5/platform/administration/admin_synchronization/synchronization_features#time_zone) for further details.
-   Limits — time interval for history data synchronization. If this option is enabled, fields for entering starting and ending dates will be active. You can specify the date using your keyboard or a calendar that is opened at a click on button ![Calendar](/en/docs/mt5/platform/img/calendar_button.png "Calendar").
-   Check quotation sessions — if this option is enabled, then the [quotation sessions](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions) set for the symbols in your trading platform will be considered during the synchronization of history data. If a source server has price data that falls outside of quotation sessions of your symbols, such data will not be synchronized (will be ignored). Thus only the price data within the set quotation sessions is imported in the platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">When conducting synchronization, take into account <a href="/en/docs/mt5/platform/administration/admin_synchronization/synchronization_features#features" class="topiclink">specific features</a> of this process for MetaTrader 5 and MetaTrader 4 servers.</span></p></td></tr></tbody></table>

## Symbols [#](admin_synchronization#symbols)

![Symbols](/en/docs/mt5/platform/img/synchronization_symbols.png "Symbols")

Specify here symbols, history data of which will be synchronized:

-   Add — add a symbol or a group of symbols. After you press this button, a new field will appear. A click on this field will open a list where you should specify a symbol or group of symbols from those available on the server. For more details please read ["Symbol specification"](/en/docs/mt5/platform/administration/common_info/common_mask).
-   Delete — delete a selected symbol.
-   Edit — modify a selected symbol. The same action can be performed by a double click on an entry.

If you enable the option "Synchronize symbols that use specified symbols as a source", the system will additionally synchronize historical data for the symbols for which one of the selected symbols is specified in the [Source](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#source) field.

## Synchronization launch

To start synchronization, click "![Synchronize History](/en/docs/mt5/platform/img/synchronize_history_button.png "Synchronize History") Synchronize History" in the [Services](/en/docs/mt5/platform/administrator/interface/main_menu/menu_services) menu. The process will run for all [enabled configurations](/en/docs/mt5/platform/administration/admin_synchronization#enable). If there is currently no need to synchronize with any server, disable its configuration before starting.

To control the process and to view the result, request server [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) for the "Synchronization" keyword. The log appears as follows:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">'1000':</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">start</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">history</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">synchronization</span><br><span class="f_CodeExample">history</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">synchronization</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">with</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'access.metatrader5.com'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">'EURUSD'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">synchronization</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">history</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">synchronization</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">with</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">'access.metatrader5.com'</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">finished</span></p></td></tr></tbody></table>

## Context Menu [#](admin_synchronization#context)

The following commands are available in the context menu of Synchronization:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new synchronization server;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — change a selected synchronization server;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected synchronization server;
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move a selected server up relative to others;
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move a selected server down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   ![Enable](/en/docs/mt5/platform/img/enable_configuration_icon.png "Enable") Enable — enable the selected configuration.
-   ![Disable](/en/docs/mt5/platform/img/disable_configuration_icon.png "Disable") Disable — disable the selected configuration.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) synchronization settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) synchronization settings to a file.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [Search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table with synchronization servers.

[Split Stocks](/en/docs/mt5/platform/administration/admin_ticks/split_ticks)

[Synchronization Features](/en/docs/mt5/platform/administration/admin_synchronization/synchronization_features)