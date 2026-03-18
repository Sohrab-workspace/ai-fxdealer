# Interaction with Servers

> Source: https://support.metaquotes.net/en/docs/mt5/api/serverapi_interaction

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)Interaction with Servers

# Interaction with Servers

The information provided in this section will help the developer to clearly understand how the server and the plugin interact.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The server can only work with the plugins, whose bit is the same as that of the server. 64-bit servers only work with 64-bit plugins</span></li><li class="p_tableatten"><span class="f_tableatten">Plugins can run on trade, history and backup servers. Access servers do not support plugins.</span></li></ul></td></tr></tbody></table>

## Initialization of Plugins

The first stage of interaction is the initialization of plugins:

1.  When starting the server scans its directories /plugins and /reports, including all subdirectories, and finds all files with the extension DLL.
2.  The server tries to load all found dll-files and call the [MTServerAbout](/en/docs/mt5/api/reference_entrypoints/mtserverabout) function in them, which returns the [MTPluginInfo](/en/docs/mt5/api/mtplugininfo) structure containing basic information about the plugin. If such a function cannot be called, then the dll-file is not a plugin.
3.  [MTPluginInfo](/en/docs/mt5/api/mtplugininfo) informs the server about the version of the API, using which the plugin was compiled. The plugin version must be supported by the server.  
    If the version of the plugin is not supported, then it will not be downloaded, and the appropriate entry will appear in the server log. In this case, you should update MetaTrader 5 Server API and recompile the plugin.

## Reading Configuration Files

After viewing the directory and identifying the plugins, the server goes through all created [plugin configurations](/en/docs/mt5/api/serverapi_configure_plugin). Further the found plugins are loaded only in accordance with the configurations created previously by the system administrator (via the administrator terminal).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">As compared with MetaTrader 4, in the fifth version of the platform, for each plugin module you can create multiple configurations with different parameters. In such a case, the server will run several instances of the plugin.</span></p></td></tr></tbody></table>

For the plugins whose configurations are created (and enabled) on the server, the [MTServerCreate](/en/docs/mt5/api/reference_entrypoints/mtservercreate) functions are called for creating plugin instances (object of the class that implements the interface [IMTServerPlugin](/en/docs/mt5/api/imtserverplugin)).

## Work of the IMTServerPlugin Interface

The [IMTServerPlugin](/en/docs/mt5/api/imtserverplugin) interface contains three methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:71px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:71px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Release</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">This method removes the created object. In general, the API objects do not count references (AddRef). Thus, when calling the IMTServerPlugin::Release method, the object is unconditionally removed, and not just the access counter is decreased.</span></p></td></tr><tr class="table"><td class="table" style="width:71px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Start</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The IMTServerPlugin::Start method is called by the server to notify the plugin about the start of operation. It passes to the plugin the </span><span class="f_Keywords">IMTServerAPI*</span><span class="f_fortable"> </span><span class="f_Param">server</span><span class="f_fortable"> parameter </span><span class="f_li">— the interface that implements the server API (the interface used for interaction with the server). The </span><span class="f_fortable">IMTServerPlugin::</span><span class="f_li">Start method is called by the server at boot time, after preparing all the databases for work. For secondary trade servers and history servers, the </span><span class="f_fortable">IMTServerPlugin::</span><span class="f_li">Start method is called after the preparation of databases and synchronization with the main trade server. Also, this method is called when <a href="/en/docs/mt5/api/serverapi_configure_plugin#enable" class="topiclink">enabling a plugin configuration</a>.</span></p><p class="p_fortable"><span class="f_li">A plugin starts processing of <a href="/en/docs/mt5/api/serverapi_simpleplugin#events" class="topiclink">events</a> only after the </span><span class="f_fortable">IMTServerPlugin::</span><span class="f_li">Start method is executed.</span></p></td></tr><tr class="table"><td class="table" style="width:71px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Stop</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">This method is called during a server shutdown (e.g. reboot) before removing a plugin. Also, the IMTServerPlugin::Stop method is called when <a href="/en/docs/mt5/api/serverapi_configure_plugin#enable" class="topiclink">disabling a plugin configuration</a>. In this method, the plugin must release all the resources it occupies, and it has no more right to access the server through </span><span class="f_Functions">IMTServerAPI</span><span class="f_fortable">. After the completion of the IMTServerPlugin::Stop method, an object can be destroyed at any time.</span></p><p class="p_fortable"><span class="f_fortable">The DLL-library of a plugin is unloaded from the memory only after all the objects that correspond to it are removed.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When restarting a server, plugins are completely unloaded and then restarted. In this case, all plugins are disabled simultaneously: they stop receiving events, Stop methods are called for them and after that all their DLL files are unloaded from the memory.</span></p></td></tr></tbody></table>

[Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)

[Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)