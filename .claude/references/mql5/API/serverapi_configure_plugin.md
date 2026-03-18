# Configuration of Plugins

> Source: https://support.metaquotes.net/en/docs/mt5/api/serverapi_configure_plugin

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
            -   [Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)
            -   [Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)
            -   [Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)
            -   [Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)
            -   [Hooks](/en/docs/mt5/api/serverapi_hooks)
            -   [Request Processing on the Server](/en/docs/mt5/api/hook_scheme)
            -   [Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)
            -   [Debugging](/en/docs/mt5/api/serverapi_debug)
            -   [Ready-made Examples](/en/docs/mt5/api/serverapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reference_entrypoints)
            -   [Plugin Interface](/en/docs/mt5/api/imtserverplugin)
            -   [Main API Interface](/en/docs/mt5/api/imtserverapi)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
            -   [Interface of End-of-Day Events](/en/docs/mt5/api/imtendofdaysink)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)Configuration of Plugins

# Configuration of Plugins

In order for the server to start to use the plugin, you need to add its configuration via the administrator terminal:

![Plugins](/en/docs/mt5/api/img/admin_plugin_list.png "Plugins")

To add or change the configuration of a plugin, click "![Add](/en/docs/mt5/api/img/add_button.png "Add")Add" and "![Edit](/en/docs/mt5/api/img/edit_button.png "Edit")Edit", respectively. They can be found in the Edit menu, on the toolbar or in the context menu. When clicking them, the following window appears:

![Editing the plugin settings](/en/docs/mt5/api/img/plugin_edit.png "Editing the plugin settings")

Fill in the following fields in this window:

-   Enable — enable/disable the plugin. The plugin starts operating immediately after the option is enabled and the configuration is saved. To get started, server restart is not required. If you disable the option, the server will completely unload the plugin from memory. This enables update of plug-in DLL files without the need to reload the platform.
-   Configurable by managers — if this option is enabled, it will be possible to change the settings of the plugin via the manager terminal. To be able to change the plugin settings, a manager account must have the [IMTConManager::RIGHT\_CFG\_PLUGINS](/en/docs/mt5/api/config_manager/imtconmanager/imtconmanager_enum#enmanagerrights) permission enabled.
-   Enable plugin profiling — after enabling the [profiling](/en/docs/mt5/api/serverapi_configure_plugin#enable), the server will start collecting the statistics on the plugin, what allows estimating its performance and detecting possible problems of its operation. It is not recommended to keep this option always enabled, as profiling decreases the plugin performance.
-   Name — the name of the plugin configuration.
-   Module — select one of the plugin modules in the first field. This field displays all the plugins that are located in the folders /plugins and /reports of the server selected in the next field.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Each configuration of the plugin is bound to a specific server and thus influences the operation only of this server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">In case of any change in plugin settings, the server will try to reinitialize (call <a href="/en/docs/mt5/api/imtserverplugin/imtserverplugin_start" class="topiclink">IMTServerPlugin::Start</a>) all enabled plugins, which previously failed to initialize.</span></li></ul></td></tr></tbody></table>

Parameters

The block of managing external parameters of the plugin is available in the bottom part of the window. Such parameters can be implemented during the development of plugin modules; they allow managing them from the outside.

The following commands are used for managing parameters:

-   Add — add a new parameter. A line appears upon pressing this button. Specify the parameter name in the "Parameter" field, and the value of this parameter in the "Value" field. String type parameters are created by default. To select another type (integer or fractional) click the arrow on the "Add" button.
-   Edit — edit a selected parameter. The same action can be performed by a double click on the required field.
-   Delete — delete a selected parameter.

### Information [#](serverapi_configure_plugin#info)

![Information](/en/docs/mt5/api/img/plugin_information.png "Information")

This tab displays various information on the plugin module: description, copyright, author, version of the plugin module and version of MetaTrader 5 Server API used for developing this plugin.

## Profiling [#](serverapi_configure_plugin#profiling)

The profiling is enabled using the "Enable plugin profiling option" in the plugin settings. This procedure allows estimating the plugin performance by measuring the time of calls of hooks and event handlers within the plugin. The time is estimated separately for each hook and handler in the plugin.

After enabling the profiling, the server will start gathering the statistics on the plugin operation and outputting the results in the [journal](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_journal) every 5 minutes. To request the journal records, use "Profile" keyword.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">It is recommended to enable profiling during testing only, as it slows down plugins.</span></li><li class="p_tableatten"><span class="f_tableatten">Profiling should be enabled before enabling the plugin. If the plugin is already enabled, it should be re-launched after enabling profiling. This is necessary for the correct data collection.</span></li></ul></td></tr></tbody></table>

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

[Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)

[Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)