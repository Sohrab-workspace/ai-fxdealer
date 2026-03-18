# Plugins

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_plugins

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Plugins

# Plugins

Plugins are special modules for extending the set of functions of a trading platform as DLL files. Plugins can also be used to change algorithms of some operations performed by servers. For example, they can be used to change calculation of margin or swaps. [MetaTrader 5 Server API](https://support.metaquotes.net/en/docs/mt5/api/serverapi) is used to create plugins.

Each plugin is [set up](/en/docs/mt5/platform/administration/admin_plugins#module) for a certain server. To view plugins configured for a server, select it in the tree located in the left part of the terminal.

![Select Server](/en/docs/mt5/platform/img/plugin_server_select.png "Select Server")

## Installing plugins

Plugins are configured separately for each server. Copy the plugin DLL file to the [/plugins](/en/docs/mt5/platform/components/trade_server/trade_server_structure#plugins) directory of the corresponding trade or history server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When the server starts, it loads all the plugin DLLs in the /plugins directory and all of its subdirectories. The libraries are loaded even if the platform does not have the corresponding plugin configurations. In this regard, we strongly recommend against storing files you plan to use in these directories.</span></p></td></tr></tbody></table>

## Adding and Editing Plugins [#](admin_plugins#add_edit)

For the plugin to start working, create a configuration for it. Select ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add on the [toolbar](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) or in the [context menu](/en/docs/mt5/platform/administration/admin_holidays#context). To edit the settings of an added plugin, click ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit.

This section support group editing of plugin configurations. To do it, select several plugins by holding Ctrl or Ctrl+Shift, and then start editing them. Using the group editing you can enable and disable plugins in bulk. Additional general information about working with configuration records is given in the ["Working with Instructions"](/en/docs/mt5/platform/administration/common_info/common_instructions) section.

Arrange plugins in the required order, as this affects the [hook processing order](https://support.metaquotes.net/ru/docs/mt5/api/serverapi_hooks). The higher the plugin is in the list, the earlier it receives the hook.

### Common [#](admin_plugins#common)

![Editing Plugin Configuration](/en/docs/mt5/platform/img/plugin_edit.png "Editing Plugin Configuration")

Set plugin settings:

-   Enable — enable/disable the plugin. The plugin starts operating immediately after the option is enabled and the configuration is saved. To get started, server restart is not required. If you disable the option, the server will completely unload the plugin from memory. This enables update of plug-in DLL files without the need to reload the platform.
-   Configurable by managers — if this option is enabled, it will be possible to change the settings of the plugin via the manager terminal. To be able to change the plugin settings, a manager account must have the ["Setup of plugins"](/en/docs/mt5/platform/administration/admin_managers#permissions) permission enabled.
-   Enable plugin profiling — after enabling the [profiling](/en/docs/mt5/platform/administration/admin_plugins#profiling), the server will start collecting the statistics on the plugin, what allows estimating its performance and detecting possible problems of its operation. It is not recommended to keep this option always enabled, as profiling decreases the plugin performance.
-   Name — name of the plugin configuration;
-   Module — in the first field select one of plugin modules. This field displays all the plugins located in the [/plugins](/en/docs/mt5/platform/components/trade_server/trade_server_structure#plugins) directory of the trade server specified in the field.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Each configuration of plugin is bound to certain <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server" class="topiclink">trade server</a>, thus it affects only its operation accordingly.</span></p></td></tr></tbody></table>

Parameters

The block of managing external parameters of the plugin is available in the bottom part of the window. Such parameters can be implemented during the development of plugin modules; they allow managing them from the outside.

The following commands are used for managing parameters:

-   Add — add a new parameter. A line appears upon pressing this button. Specify the parameter name in the "Parameter" field, and the value of this parameter in the "Value" field. String type parameters are created by default. To select another type (integer or fractional) click the arrow on the "Add" button.
-   Edit — edit a selected parameter. The same action can be performed by a double click on the required field.
-   Delete — delete a selected parameter.

### Information [#](admin_plugins#info)

![Information](/en/docs/mt5/platform/img/plugin_information.png "Information")

This tab displays various information on the plugin module: description, copyright, author, version of the plugin module and version of MetaTrader 5 Server API used for developing this plugin.

## Profiling [#](admin_plugins#profiling)

The profiling is enabled using the "Enable plugin profiling option" in the plugin settings. This procedure allows estimating the plugin performance by measuring the time of calls of hooks and event handlers within the plugin. The time is estimated separately for each hook and handler in the plugin.

After enabling the profiling, the server will start gathering the statistics on the plugin operation and outputting the results in the [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) every 5 minutes. To request the journal records, use "Profile" keyword.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">It is recommended to enable profiling during testing only, as it slows down plugins.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Profiling should be enabled before enabling the plugin. If the plugin is already enabled, it should be re-launched after enabling profiling. This is necessary for the correct data collection.</span></li></ul></td></tr></tbody></table>

The following information is gathered during profiling:

-   Hook/event handler state — two states are possible: active state (the hook/event handler was executing during estimation), unactive state (the hook/event handler was not executing during estimation). If a hook/handler stays in the active state for more than 5 seconds, a message about a possible deadlock is displayed (the second line in the example). If a hook/handler stays active for more than 0.5 seconds, a message informing that the hook/handler is too slow is displayed (third line in the example).

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;unactive&nbsp;state</span><br><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;possible&nbsp;deadlock:&nbsp;6000&nbsp;msc&nbsp;in&nbsp;active&nbsp;state</span><br><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;too&nbsp;slow:&nbsp;max&nbsp;process&nbsp;time&nbsp;1000&nbsp;msc</span></p></td></tr></tbody></table>

-   Number of calls — the total number of calls of the hook/handler during the plugin operation.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;5&nbsp;calls&nbsp;</span></p></td></tr></tbody></table>

-   Time of last call — time of the last call of the hook/handler accurate to millisecond.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;last&nbsp;call&nbsp;at&nbsp;2013.06.26&nbsp;14:09:37.603</span></p></td></tr></tbody></table>

-   Minimal execution time — minimal time of execution of the hook/handler (in milliseconds) during the plugin operation.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;time&nbsp;min&nbsp;&nbsp;&nbsp;0&nbsp;msc</span></p></td></tr></tbody></table>

-   Maximal execution time — maximal time of execution of the hook/handler (in milliseconds) during the plugin operation.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;time&nbsp;max&nbsp;&nbsp;&nbsp;2&nbsp;msc</span></p></td></tr></tbody></table>

-   Average execution time — average time of execution of the hook/handler (in milliseconds) during the plugin operation.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;time&nbsp;avg&nbsp;&nbsp;&nbsp;0&nbsp;msc</span></p></td></tr></tbody></table>

-   Total execution time — total time of execution of the hook/handler (all calls in milliseconds) during the plugin operation.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">14:10:01&nbsp;&nbsp;&nbsp;&nbsp;Simple&nbsp;Plugin&nbsp;&nbsp;&nbsp;&nbsp;Profile&nbsp;IMTConSymbolSink::OnSymbolUpdate:&nbsp;time&nbsp;total&nbsp;&nbsp;&nbsp;0&nbsp;msc</span></p></td></tr></tbody></table>

## Context Menu [#](admin_plugins#context)

The context menu of the "Plugins" section contains the following commands:

-   ![Add](/en/docs/mt5/platform/img/add_button.png "Add") Add — add a new plugin configuration;
-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit a selected plugin configuration;
-   ![Delete](/en/docs/mt5/platform/img/delete_button.png "Delete") Delete — delete a selected plugin configuration;
-   ![Move Up](/en/docs/mt5/platform/img/move_up_button.png "Move Up") Move Up — move a selected plugin configuration up relative to others;
-   ![Move Down](/en/docs/mt5/platform/img/move_down_button.png "Move Down") Move Down — move a selected plugin configuration down relative to others;
-   ![Sort Alphabetically](/en/docs/mt5/platform/img/sort_symbols_icon.png "Sort Alphabetically") Sort Alphabetically — sort configurations alphabetically. Please note that sorting is done on the server, not in the local terminal.
-   ![Enable](/en/docs/mt5/platform/img/enable_configuration_icon.png "Enable") Enable — enable the selected configuration.
-   ![Disable](/en/docs/mt5/platform/img/disable_configuration_icon.png "Disable") Disable — disable the selected configuration.
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) the settings of plugins to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) the settings of plugins to a file.
-   ![Journal](/en/docs/mt5/platform/img/journal_icon.png "Journal") Journal — request [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) according to the selected configuration. This will open the trade server logs section, with the name of the selected configuration automatically specified in the query field. You will only need to press the request button.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open a [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators in the table .

[Setup as Service](/en/docs/mt5/platform/administration/admin_feeds/feed_service)

[Reports](/en/docs/mt5/platform/administration/admin_reports)