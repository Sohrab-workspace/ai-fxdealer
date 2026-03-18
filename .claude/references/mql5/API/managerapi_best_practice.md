# Recommendations for Developers

> Source: https://support.metaquotes.net/en/docs/mt5/api/managerapi_best_practice

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
        -   [Manager API](/en/docs/mt5/api/managerapi)
            -   [Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)
            -   [Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)
            -   [Getting Started](/en/docs/mt5/api/managerapi_preparing)
            -   [Ready-made Examples](/en/docs/mt5/api/managerapi_examples)
            -   [.NET Implementation](/en/docs/mt5/api/managerapi_net)
            -   [Python Implementation](/en/docs/mt5/api/managerapi_python)
            -   [Exported Functions](/en/docs/mt5/api/managerapi_exported)
            -   [CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)
            -   [Administrator Interface](/en/docs/mt5/api/imtadminapi)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
            -   [Dealer Interface](/en/docs/mt5/api/imtdealersink)
            -   [Interface of Manager API Events](/en/docs/mt5/api/imtmanagersink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)Recommendations for Developers

# Recommendations for Developers

This section contains general recommendations and solutions of typical issues programmers face when developing applications via Manager API.

## Principles of Applications

In the work of applications, there are the following main steps:

-   Loading MT5APIManager.dll using the [CMTManagerAPIFactory::Initialize](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_initialize) method of he Manager API factory.
-   Creating the manager or administrator interface using the [CMTManagerAPIFactory::CreateManager](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createmanager) or [CMTManagerAPIFactory::CreateAdmin](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createadmin) method respectively.
-   Verifying that the versions of the main header file MT5APIManager.h (the version parameter of one of the interface creation methods) and of the loaded DLL (passed by [CMTManagerAPIFactory::Version](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_version)) match.
-   Connecting an application to a server with the Connect method, using the created [administrator](/en/docs/mt5/api/imtadminapi/imtadminapi_connection/imtadminapi_connect) or [manager](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection/imtmanagerapi_connect) interface, as well as details of the manager account created on the server.
-   After the work is completed, the application is disconnected from the server using the Disconnect method.
-   Next the created interface is deleted using the Release method.
-   The last stage is unloading the DLL of the manager API from the memory using the [CMTManagerAPIFactory::Shutdown](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_shutdown) method.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">With the MetaTrader 5 Manager API, you can develop 32- and 64-bit applications using the appropriate DLLs included into the installation package.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Applications are only developed for Windows. Manager API DLLs are not suitable for developing applications for Linux or other operating systems.</span></li></ul></td></tr></tbody></table>

## Application Requirements

When developing applications, it is necessary to meet the following requirements:

-   An application should be as efficient in memory usage as possible.
-   An application should fragment memory as little as possible.
-   An application should not cause memory leaks.
-   An application must quickly return control from event handlers.
-   During calls of any \*Request methods (such as [IMTManagerAPI::SymbolRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_config/imtmanagerapi_config_symbol/imtmanagerapi_symbolrequest) or [IMTManager::GroupRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_config/imtmanagerapi_config_group/imtmanagerapi_grouprequest)), information is requested straight from the server. Too frequent requests can lead to the activation of the anti flood control system, as a result of which connection between the Manager API and the server can be lost. In order not to overload the server, control the frequency of these method calls and, if possible, use \*Get methods, which receive information from the local application cache.
-   All methods of event handling interfaces (IMT\*Sink) are called from the network thread. Therefore, any methods of the same manager or administrator interface, which send commands to the trade server (such as \*Request, \*Update, \*Delete, \*Send, etc.) are prohibited in these interfaces. Only methods working with local data (\*Get, \*Next, \*Total, etc.) can be called from event handlers.

## Working with the configuration base and database interfaces [#](managerapi_best_practice#base)

When working with [configuration base](/en/docs/mt5/api/reference_configurations) and [database](/en/docs/mt5/api/reference_bases) interfaces, please consider the following features:

-   Any \*Add, \*Update, \*Delete and \*Clear methods of these interfaces only affect the appropriate local object. To send changes to a server, you should call the corresponding \*Add or \*Update method of the Manager API. For example, the [IMTConGroup::SymbolUpdate](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_symbolupdate) method only updates a symbol configuration in the group object. To send these changes to a server, you should call the [IMTAdminAPI::GroupUpdate](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupupdate) method.

## Escaping special characters [#](managerapi_best_practice#escape)

When using special characters = (equal sign), | (vertical bar), \\ (slash) and line feed as method parameter values, you must escape them with the \\ (slash) character.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the \ (slash) character is not followed by special characters listed above, then it is processed as is.</span></p></td></tr></tbody></table>

The table below shows examples of processing escaped characters on a trading server.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Character sent to the server</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">character recognized by the server</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\=</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">=</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\|</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">|</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\(line feed)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">(line feed)</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\\</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">\</span></p></td></tr></tbody></table>

## Using Logs to Analyze Possible Problems [#](managerapi_best_practice#journal)

Logs assist in tracking application events and errors. Use Logger\* functions available in the [Administrator](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggerout) and [Manager interfaces](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerout) in crucial blocks of your application code to log information about its operation. This will make troubleshooting much easier.

By default, Manager API applications store logs under the \\logs subdirectory of the directory from which they are launched. For example, if your application runs in the 'C:\\ManagerAPI solution' directory, then the log will be located in 'C:\\ManagerAPI solution\\logs'. The files have .log extensions and are saved separately for each day. The data storage directory can be overridden when creating interfaces using the [CreateAdmin](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createadmin) and [CreateManager](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createmanager) methods.

[Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)

[Getting Started](/en/docs/mt5/api/managerapi_preparing)