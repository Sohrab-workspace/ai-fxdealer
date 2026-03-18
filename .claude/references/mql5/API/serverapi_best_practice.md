# Recommendations for Developers

> Source: https://support.metaquotes.net/en/docs/mt5/api/serverapi_best_practice

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)Recommendations for Developers

# Recommendations for Developers

This section contains general recommendations and solutions of typical issues programmers face when developing plugins.

## Multithreading [#](serverapi_best_practice#multithread)

When writing a multithreaded application, a programmer must take into account some specific features of MetaTrader 5 Server API:

-   Calling Server API methods (methods of interface IMTServerAPI, e.g. the functions [IMTServerAPI::Group\*](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group), [IMTServerAPI::Symbol\*](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_symbol), etc.) is thread safe. In using them, the does not need to ensure synchronization of access for simultaneous access to the same object of the server API from different threads. In other words, methods of the IMTServerAPI interface can be simultaneously called from different threads without additional synchronization.
-   Calling of interface methods (e.g. interfaces of configuration bases: [IMTConGroup](/en/docs/mt5/api/config_group/imtcongroup), [IMTConSymbol](/en/docs/mt5/api/config_symbol/imtconsymbol), [IMTConGateway](/en/docs/mt5/api/config_gateway/imtcongateway), etc.) is not thread safe. When accessing the same object from two threads, the programmer must ensure synchronization of access.
-   It is not guaranteed that hooks and events are called sequentially. Several hooks or events (even of the same type) can be called simultaneously, and each of them will be called in a separate thread. Accordingly, the handlers of (hooks) must be thread safe.
-   Synchronous calling from events/hooks of a client base (for example, [IMTUserSink](/en/docs/mt5/api/reference_user/imtusersink)) to a trade base is forbidden in plugins. Violation of this rule may cause deadlocks and trade server crash.
-   Calling from trading events and hooks to the client base is allowed. All [IMTServerAPI::User\*](/en/docs/mt5/api/imtserverapi/serverapi_users) methods can be used except for those related to trading activity: [IMTServerAPI::UserAccountGet](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_useraccountget), [IMTServerAPI::UserDepositChange](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userdepositchange) and [IMTServerAPI::UserDepositChangeRaw](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userdepositchangeraw). The [IMTServerAPI::UserAccountGet](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_useraccountget) call is permitted only when accessing the account data for which the request was originally received.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">All the plugin components must be implemented thread-safe, except for calls of IMTServerAPI methods.</span></p></td></tr></tbody></table>

## Multithreaded interaction with the trade server [#](serverapi_best_practice#multithread_interaction)

We strongly advise you against interfering with the server threads operation and interaction logic. In particular, we urge you not to implement your own synchronization primitives affecting the server threads operation (i.e. not to use them in the [hooks](/en/docs/mt5/api/serverapi_hooks)).

When developing an application, keep in mind the following:

-   The unit of grouping data on client's open orders and positions is a client group. It manages client's open orders and positions, as well as margin status. Each group has its own synchronization primitive.
-   Trading bases (open orders, history orders, deals, positions) also feature their own synchronization primitives.
-   In general, requests are handled sequentially by a group of threads: initial control, routing and execution ones. When executing tasks, these threads access the corresponding client groups using synchronization primitives (securing exclusive access — lock) among other things.
-   Incoming quotes as well as trade symbol and group changes are handled by a separate thread pool. When executing tasks, these threads also access the corresponding client groups using synchronization primitives among other things.
-   All incoming trading executions ([IMTExecution](/en/docs/mt5/api/reference_trading/trading_request/imtexecution)) of gateways are put in a separate queue and processed by a separate thread. When handling execution, this thread accesses the corresponding client groups using synchronization primitives. Trading executions are handled by the thread sequentially in the order of their receipt.
-   A significant number of events and hooks are called under the lock, including the lock of the group synchronization primitive and the lock of a certain database (orders, positions, deals).
-   The entire interaction of trading and client databases is unidirectional - the trading base always refers to the client base, but not vice versa.

In order to avoid deadlocks when working from trading events and hooks, do the following:

-   Minimize direct (receiving data) and indirect (calculating a margin for a certain request, etc.) access to the data located in other groups: client's open orders, positions and trading account data.
-   Minimize the use of your custom synchronization primitives.
-   Do not try to directly control the interaction of server internal threads by explicitly stopping them or applying synchronization primitives.
-   The hooks and client base events (for example, [IMTUserSink::OnUser\*](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_onuseradd), [IMTUserSink::HookUser\*](/en/docs/mt5/api/reference_user/imtusersink/imtusersink_hookuseradd)) should not contain calls of the API methods associated with the trading databases (for example, [IMTServerAPI::PositionGet](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_position/imtserverapi_positionget)).
-   In [IMTDealSink](/en/docs/mt5/api/reference_trading/trading_deal/imtdealsink) events, it is only allowed to use synchronous calls of methods changing, creating and deleting only those deals which are in the same groups as the deal for which the event was received. In all other cases, you should use asynchronous calls — API methods should be called in a separate thread, and not in the thread that triggers the events of the deal database.

## Memory Management [#](serverapi_best_practice#memory_manage)

The correct approach to the use of memory is one of the key points in the development of plugins. There are the following requirements for working with memory:

-   Since the DLL modules of plugins work in the address space of the server, the plugin must be memory efficient. In addition, the plugin should have limited memory re-allocation to prevent it from too much fragmentation.
-   All interface objects are allocated using the Create methods and removed using the Release methods.
-   In cases where the API itself allocates memory (e.g., the function [IMTServerAPI::UserLogins](/en/docs/mt5/api/imtserverapi/serverapi_users/imtserverapi_userlogins), which returns a dynamic array of clients from the specified group), it is necessary to free the memory using the method [IMTServerAPI::Free](/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_free).  
    Pair to the method IMTServerAPI::Free is the method [IMTServerAPI::Allocate](/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_allocate), which allows to allocate memory.

## Working with the configuration base and database interfaces [#](serverapi_best_practice#base)

When working with [configuration base](/en/docs/mt5/api/reference_configurations) and [database](/en/docs/mt5/api/reference_bases) interfaces, please consider the following features:

-   Any \*Add, \*Update, \*Delete and \*Clear methods of these interfaces only affect the appropriate local object. To send changes to a server, you should call the corresponding \*Add or \*Update method of the Server API. For example, the [IMTConGroup::SymbolUpdate](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_symbolupdate) method only updates a symbol configuration in the group object. To send these changes to a server, you should call the [IMTServerAPI::GroupAdd](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupadd) method.

# Escaping special characters

When using special characters = (equal sign), | (vertical bar), \\ (slash) and line feed as method parameter values, you must escape them with the \\ (slash) character.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the \ (slash) character is not followed by special characters listed above, then it is processed as is.</span></p></td></tr></tbody></table>

The table below shows examples of processing escaped characters on a trading server.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Character sent to the server</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">character recognized by the server</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\=</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">=</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\|</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">|</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\(line feed)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">(line feed)</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">\\</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">\</span></p></td></tr></tbody></table>

[Request Processing on the Server](/en/docs/mt5/api/hook_scheme)

[Debugging](/en/docs/mt5/api/serverapi_debug)