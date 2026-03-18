# Plugins

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_plugins

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
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Plugins

# Plugins

"Plugins" section is intended for controlling plugins - the server functionality extension modules in the form of DLL-files. Plugins allocate in /plugins server folder, which the server views at each start for creation of the list of existing plugins. For the plugins located in the list, it is possible to change priority by "Move Up" and "Move Down" commands the context menu.

![Plugins](/en/docs/mt4/administrator/img/br_plugins.png "Plugins")

## Plugin settings [#](ug_plugins#plugin_setup)

To change plugin settings, it is necessary to execute the "Edit — Edit" menu command or the same command of the context menu. The window with detailed settings of the plugin will appear:

![Plugins](/en/docs/mt4/administrator/img/win_plugins.png "Plugins")

-   Load at server startup — load the plugin at server startup;
-   Configurable by managers — plugin can be configured in the manager terminal if the manager account has the appropriate right.

-   Enable plugin profiling — if [profiling](/en/docs/mt4/administrator/administration/ug_plugins#profiling) is enabled, the server collects statistics on the plugin operation, which can be used to evaluate the plugin performance and identify possible problems. Do not keep this parameter permanently enabled, because it affects the performance of the plugin and the trading server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The plugin, as well as the profiling mode, is enabled/disabled after server restart.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Changes in priority of plugins (change of position) take effect after server restarting.</span></li></ul></td></tr></tbody></table>

Each plugin can contain a set of some parameters serving for adjustment of its operation. Current parameters are displayed in "Parameters:" of plugin. For changing value or name of the parameter, it is necessary to select a necessary field in the list using doubleclick. After changing the edited field, it is necessary to press Enter key. To add the new parameter, it is necessary to press "Add" button. To delete the selected parameter, it is necessary to press "Delete" button.

## Check of Plugins on Loading [#](ug_plugins#check)

When loading plugins, the trade server performs several checks. In case it detects a problem, the corresponding message is written to the server [journal](/en/docs/mt4/administrator/administration/ug_logs):

-   The server measures the number of threads in the system before and after loading a plugin. In case the number of threads increases by more than 50, it will write the corresponding message in the journal.
-   In case a plugin include the [debug section](https://support.metaquotes.net/en/articles/352 "Article: How to Improve Quality of MetaTrader 4 and MetaTrader 5 Server Plugins?"), the corresponding message will be added to the journal.
-   It checks a digital signature of plugins. If there is no signature, the corresponding message will be added to the journal. If there is a signature, the journal message will display the name of an organization, who has signed the plugin.
-   If a plugin uses Java or .NET, the journal message will recommend not using this plugin. Such recommendation is due to using Java or .NET in plugins increases the loading of the trade server.
-   After loading a plugin dll, the server checks, whether exception handlers have been substituted (SetUnhandeledExceptionFilter,\_set\_new\_mode, \_set\_new\_handler, \_set\_invalid\_parameter\_handler). In case it finds a substitution of handlers, the following message will be written to the journal: "it is recommended to remove handler replacement in the plugin as it negatively impacts the server's self-test system". This message may also appear due to compiling a plugin using Microsoft Visual Studio 6.0.

## Profiling [#](ug_plugins#profiling)

Profiling allows evaluating the performance of the plugin by measuring the time and number of plugin hook calls. Measurement is performed for each hook available in the plugin.

To start profiling, enable the corresponding option in [plugin settings](/en/docs/mt4/administrator/administration/ug_plugins#plugin_setup) and restart the trading server. After that, the server will begin to collect the plugin operation statistics and will output it to the [Journal](/en/docs/mt4/administrator/administration/ug_logs). Statistical data is output once a minute after the monitoring data. To request logs, use the "API" keyword.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The profiling mode is only recommended for the plugin testing time, because it slows down the plugin operation.</span></p></td></tr></tbody></table>

Statistics is the cumulative data on all hooks of all plugins that were called during the trading server operation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">22:10:01.382&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;API&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;'Routing.dll'&nbsp;-&nbsp;MtSrvHistoryTickApply&nbsp;profile,&nbsp;total&nbsp;time:&nbsp;0.164&nbsp;ms,&nbsp;count:&nbsp;2415,&nbsp;max:&nbsp;0.013&nbsp;ms,&nbsp;calls:&nbsp;0</span><br><span class="f_CodeExample">22:10:01.384&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;API&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;'Routing.dll'&nbsp;-&nbsp;MtSrvTradeTransaction&nbsp;profile,&nbsp;total&nbsp;time:&nbsp;305.559&nbsp;ms,&nbsp;count:&nbsp;3,&nbsp;max:&nbsp;101.911&nbsp;ms,&nbsp;calls:&nbsp;0</span></p></td></tr></tbody></table>

The following information is displayed for all hooks:

-   total time — the total time spent in the hook. Together with "count", the value allows identifying an excessive amount of hook calls.
-   count — the total number of hook calls during the plugin operation time.
-   max — the maximum time spent in the hook. The value allows tracking rare, but large delays in performance.
-   calls — the number of current calls of the hook, which the plugin has not yet exited. The value allows detecting the full freeze of the hook.

If the hook call time exceeds 50 milliseconds, the following warning is added to the journal (no more than once every 5 seconds):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">22:09:49.860&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;API&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp;'Routing.dll'&nbsp;-&nbsp;MtSrvTradeTransaction&nbsp;profile,&nbsp;call&nbsp;too&nbsp;slow&nbsp;-&nbsp;101.764&nbsp;ms,&nbsp;total&nbsp;time:&nbsp;203.648&nbsp;ms,&nbsp;count:&nbsp;2,&nbsp;max:&nbsp;101.884&nbsp;ms,&nbsp;calls:&nbsp;0</span></p></td></tr></tbody></table>

In this case, it is strongly recommended to disable the plugin and optimize it. Otherwise, the performance of the trading server can be significantly reduced or completely hang.

[Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)

[Accounts](/en/docs/mt4/administrator/administration/ug_accounts)