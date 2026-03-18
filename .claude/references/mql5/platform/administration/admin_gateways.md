# Gateways

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways

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
                -   [Configuration of Gateways](/en/docs/mt5/platform/administration/admin_gateways/gateways_config)
                -   [Status](/en/docs/mt5/platform/administration/admin_gateways/gateway_status)
                -   [Journal of Gateways](/en/docs/mt5/platform/administration/admin_gateways/journal_gateway)
                -   [Positions](/en/docs/mt5/platform/administration/admin_gateways/gateway_positions)
                -   [Setup of Routing](/en/docs/mt5/platform/administration/admin_gateways/gateways_routing)
                -   [Setup as Service](/en/docs/mt5/platform/administration/admin_gateways/gateway_service)
                -   [Operation on Weekend](/en/docs/mt5/platform/administration/admin_gateways/gateway_weekend)
                -   [Symbol and Price Translation](/en/docs/mt5/platform/administration/admin_gateways/gateway_translation)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Gateways

# Gateways

Gateways integrate MetaTrader 5 with external trading systems. With this integration, you can provide the possibility for your traders to execute trading operations on almost any exchange. They will receive quotes and will execute trades in their familiar terminal while all their operations will be forwarded to an external system.

The platform offers a variety of built-in [turnkey gateways](/en/docs/mt5/platform/components/gateways) for integration with exchanges and trading systems. You can test them right away. Additional third-party solutions are featured in the [App Store](https://support.metaquotes.net/en/market/mt5/aggregation). Using the [Gateway API](https://support.metaquotes.net/en/docs/mt5/api/gatewayapi), you can create your own gateways for integration with any trading systems.

In the Gateway section, available solutions can be viewed in two modes: product showcase and configuration list. You can switch between them using buttons ![Showcase](/en/docs/mt5/platform/img/tile_icon.png "Showcase") and ![List](/en/docs/mt5/platform/img/list_icon.png "List").

![List of gateways](/en/docs/mt5/platform/img/gateways.png "List of gateways")

The product showcase provides basic information: gateway name, connection status and the amount of transmitted Market Depth and tick data. The Selected tab displays all gateways for which you have configurations. The Available tab features all gateway modules available on the History server. You can configure them at any time.

The list mode enables the management of existing gateway configurations. It provides quick access to the main parameters:

-   Name — gateway name.
-   Mode — gateway operation mode: receives quotes (Q), processes operations (T), or both.
-   Server — the address of the external trading system server to which the gateway connects.
-   Groups — [groups](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#groups) available to the gateway.
-   Symbols — [symbols](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#symbols) available to the gateway.
-   Last active — data and time of the last successful connection of the gateway to the external system.
-   ID — gateway identifier used to identify trade requests processed by this gateway.
-   Status — connection status and the number of trading operations processed by the gateway/total transmitted ticks and Market Depth changes.

Using the context menu, you can adjust the set of displayed data.

## How Gateways Work

The interaction of gateways and servers is performed through the special library MT5APIGateway.dll.

For receiving quotes and news, the gateway connects to the [history server](/en/docs/mt5/platform/components/history_server). At that the priority of transmission of quotes for a symbol is determined in the same way as for [data feeds](/en/docs/mt5/platform/administration/admin_feeds) — by the position of configuration of the gateway in the list. This is described in more details in a [separate section](/en/docs/mt5/platform/components/history_server/history_server_datafeeds).

To perform trade operations, all [trade servers](/en/docs/mt5/platform/components/trade_server) of the platform connect to the gateway.

![Scheme of Gateway Operation](/en/docs/mt5/platform/img/gateway_server_scheme.png "Scheme of Gateway Operation")

## Switching between Gateway [#](admin_gateways#switching)

The position of a gateway in the list defines its priority in the delivery of data: the higher the position is, the higher the priority of the gateway is. However, a server is permanently receiving information from all gateway at once. Such a solution allows to immediately switch to another gateway in case of problems. For example, several gateways deliver quotes of the same symbol from different financial companies - the priority defines what gateway should be used. If the required data are not received from the selected gateway for a certain period of time, the server automatically switches to the next gateway that provides information on the same symbol. However, as soon as data from the gateway with higher priority are received, the server will switch back to it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The idle timeout of a gateway is set up on the history server settings in <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server#timeout" class="topiclink">"Datafeeds timeout"</a>.</span></li><li class="p_tableatten"><span class="f_tableatten">For symbols with the depth of market enabled the current data source (a gateway of a <a href="/en/docs/mt5/platform/administration/admin_feeds" class="topiclink">data feed</a>) is determined by the first quote that comes after starting the history server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Switching of gateways for a symbol can be tracked in the <a href="/en/docs/mt5/platform/administration/admin_ticks#datafeed" class="topiclink">"Ticks"</a> section.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Flow of quotes for a symbol coming from a gateway has a higher priority than a flow from a <a href="/en/docs/mt5/platform/administration/admin_feeds" class="topiclink">data feed</a>. Switching to quotes from a data feed occurs in case the data flow from the gateway has stopped.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Switching of gateways is performed independently for each symbol.</span></li></ul></td></tr></tbody></table>

The process of activation of a quotes flow from a certain gateway is reflected in the history server [journal](/en/docs/mt5/platform/administration/admin_network/network_journal). To find such records, use the keyword "activation".

### Possible delay in the delivery of Market Depth prices after switching gateways

To consume less resources, the history servers does not store the best prices and Market Depth values for each symbol and each available data source. For the same purpose, the Market Depth is passed from the data feed to the server in the form of changes relative to the previous state. Additionally, the full Market Dept snapshot is sent to the server no more than once every 30 seconds.

Therefore, if the main price feed is stopped and the server switches to the reserve one, the server has to wait for the first Market Depth snapshot from the data feed. During this time (up to 30 seconds), the Market Depth data is not updated.

## Setting Up Gateways

The gateways are configured in two steps:

-   [Configuration of a gateway](/en/docs/mt5/platform/administration/admin_gateways/gateways_config) — configuration of the gateway itself;
-   [Setting up the routing](/en/docs/mt5/platform/administration/admin_gateways/gateways_routing) — setting up the routing of trade requests to be processed by the gateway.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_Normal"><span class="f_tableatten">To view the logs of gateways, </span><span class="f_txt">select it in the tree-like list in the left part of the terminal and go to the <a href="/en/docs/mt5/platform/administration/admin_gateways/journal_gateway" class="topiclink">"Journal"</a> tab.</span></p></td></tr></tbody></table>

## Context Menu [#](admin_gateways#context)

The context menu of the "Gateways" section contains the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new gateway;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit the selected gateway;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete the selected gateway;
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move the selected gateway up relative to others;
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move the selected gateway down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   ![Enable](/en/docs/mt5/platform/img/enable_configuration_icon.png "Enable") Enable — enable the selected configuration.
-   ![Disable](/en/docs/mt5/platform/img/disable_configuration_icon.png "Disable") Disable — disable the selected configuration.
-   Automation triggers — create an [automation](/en/docs/mt5/platform/administration/automation) task for the selected event or edit an existing one. The menu displays only the triggers and tasks associated with the current section.
-   Automation actions — add an automation action to an existing task or create a new task based on the action. The menu displays only the actions associated with the current section.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) the settings of gateways to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) the settings of gateways to a file.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [Search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table with the gateways.

[Positions](/en/docs/mt5/platform/administration/admin_positions)

[Configuration of Gateways](/en/docs/mt5/platform/administration/admin_gateways/gateways_config)