# Data Feeds

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_feeds

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
                -   [Configuration of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/feed_setup)
                -   [Status](/en/docs/mt5/platform/administration/admin_feeds/feed_status)
                -   [Journal of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed)
                -   [Restarting Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/data_feed_restart)
                -   [Setup as Service](/en/docs/mt5/platform/administration/admin_feeds/feed_service)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Data Feeds

# Data Feeds

Data feeds deliver quotes and news from various providers. Use the data feeds to provide the following essential trading tools to your clients:

-   Real-time financial news to assist in making trading decisions
-   Price data from different exchanges and ECNs for analysis and for the development of trading strategies

The platform offers a variety of built-in [turnkey data feeds](/en/docs/mt5/platform/components/datafeeds) for integration with major data providers: Dow Jones, IBTimes, DTN and others. You can test them right away. Additional third-party solutions are featured in the [App Store](https://support.metaquotes.net/en/market/mt5/aggregation). Using the [Gateway API](https://support.metaquotes.net/en/docs/mt5/api/gatewayapi), you can create your own data feeds for integration with any data providers.

In the Data Feeds section, available solutions can be viewed in two modes: product showcase and configuration list. You can switch between them using buttons ![Showcase](/en/docs/mt5/platform/img/tile_icon.png "Showcase") and ![List](/en/docs/mt5/platform/img/list_icon.png "List").

![Data feeds](/en/docs/mt5/platform/img/data_feeds.png "Data feeds")

The product showcase provides basic information: data feed name, connection status and the amount of transmitted Market Depth and tick data. The Selected tab displays all data feeds for which you have configurations. The Available tab features all data feed modules available on the History server. You can configure them at any time.

The list mode enables the management of existing data feed configurations. It provides quick access to the main parameters:

-   Name — the name of the data feed.
-   Source — data type provided by the data feed, news (N) or quotes/Market Depth (Q).
-   Server — the address and port of the server from which the data feed receives data.
-   Symbols — [symbols](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#symbols) available to the data feed.
-   Last active — data and time of the last successful connection of the data feed to the data provider.
-   State — total transmitted ticks and Market Depth changes/the number of transmitted news items.

Using the context menu, you can adjust the set of displayed data.

## How Data Feeds Work

Data feeds are executable files (\*.exe) that run as separate processes. They are stored on the History server, in the "Datafeed" directory. Data feeds interact with the platform through the MT5APIGateway.dll library.

Data feeds connect to an external data source and transmit information to the [History server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server). From this server, data is forwarded to [Access servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_access_server) and terminals. Several sources can be used. If data delivery from one source fails, you can instantly switch to another one.

## Switching between Data Feeds [#](admin_feeds#switching)

The position of a data feed in the list defines its priority in the delivery of data: the higher the position is, the higher the priority of the feeder is. However, a server is permanently receiving information from all data feeds at once. Such a solution allows to immediately switch to another feed in case of problems. For example, several data feeds deliver quotes of the same symbol from different financial companies - the priority defines what data feed should be used. If the required data are not received from the selected feed for a certain period of time, the server automatically switches to the next data feed that provides information on the same symbol. However, as soon as data from the feed with higher priority are received, the server will switch back to it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The idle timeout of a feed is set up on the history server settings in <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server#timeout" class="topiclink">"Datafeeds timeout"</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">For symbols with the depth of market enabled the current data source (a <a href="/en/docs/mt5/platform/administration/admin_gateways" class="topiclink">gateway</a> of a data feed) is determined by the first quote that comes after starting the history server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Switching of data feeds for a symbol can be tracked in the <a href="/en/docs/mt5/platform/administration/admin_ticks#datafeed" class="topiclink">"Ticks"</a> section.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Flow of quotes for a symbol coming from a <a href="/en/docs/mt5/platform/administration/admin_gateways" class="topiclink">gateway</a> has a higher priority than a flow from a data feed. Switching to quotes from a data feed occurs in case the data flow from the gateway has stopped.</span></li><li class="p_tableatten"><span class="f_tableatten">Switching of data feeds is performed independently for each symbol.</span></li></ul></td></tr></tbody></table>

To move data feeds use "![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up" and "![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down" located in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar and in the context menu.

The process of activation of a quotes flow from a certain data feed is reflected in the history server [journal](/en/docs/mt5/platform/administration/admin_network/network_journal). To find such records, use the keyword "activation".

## Configuration of Data Feeds

In order to add or modify a data feed, press "![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add" or "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit", respectively. In order to delete a data feed, press "![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete". These commands are also available in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar and in the context menu.

To open a data feed [settings](/en/docs/mt5/platform/administration/admin_feeds/feed_setup) or view its [status](/en/docs/mt5/platform/administration/admin_feeds/feed_status), select it in the tree-like list in the "Data Feeds" section on the left.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The standard MetaTrader 5 delivery package includes several ready-to-use data feeds for receiving information from the most popular providers. These data feeds are described in <a href="/en/docs/mt5/platform/components/datafeeds" class="topiclink">separate sections</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">To view the journal of operation of data feeds, select in in the tree-like list in the "Data Feeds" section on the left and go to the <a href="/en/docs/mt5/platform/administration/admin_feeds/journal_datafeed" class="topiclink">"Journal"</a> tab.</span></li><li class="p_tableatten"><span class="f_tableatten">Additional general information about working with configuration records is given in the <a href="/en/docs/mt5/platform/administration/common_info/common_instructions" class="topiclink">"Working with Instructions"</a> section.</span></li></ul></td></tr></tbody></table>

### Possible delay in the delivery of Market Depth prices after switching gateways

To consume less resources, the history servers does not store the best prices and Market Depth values for each symbol and each available data source. For the same purpose, the Market Depth is passed from the data feed to the server in the form of changes relative to the previous state. Additionally, the full Market Dept snapshot is sent to the server no more than once every 30 seconds.

Therefore, if the main price feed is stopped and the server switches to the reserve one, the server has to wait for the first Market Depth snapshot from the data feed. During this time (up to 30 seconds), the Market Depth data is not updated.

## Context Menu [#](admin_feeds#context)

The context menu of the "Data Feed" section contains the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new data feed;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit a selected data feed;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected data feed;
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move a selected data feed up relative to others;
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move a selected data feed down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   ![Enable](/en/docs/mt5/platform/img/enable_configuration_icon.png "Enable") Enable — enable the selected configuration.
-   ![Disable](/en/docs/mt5/platform/img/disable_configuration_icon.png "Disable") Disable — disable the selected configuration.
-   Automation triggers — create an [automation](/en/docs/mt5/platform/administration/automation) task for the selected event or edit an existing one. The menu displays only the triggers and tasks associated with the current section.
-   Automation actions — add an automation action to an existing task or create a new task based on the action. The menu displays only the actions associated with the current section.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) the settings of data feeds to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) the settings of data feeds to a file.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [Search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table with the data feeds.

[Symbol and Price Translation](/en/docs/mt5/platform/administration/admin_gateways/gateway_translation)

[Configuration of Data Feeds](/en/docs/mt5/platform/administration/admin_feeds/feed_setup)