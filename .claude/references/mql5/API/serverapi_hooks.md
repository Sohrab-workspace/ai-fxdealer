# Hooks

> Source: https://support.metaquotes.net/en/docs/mt5/api/serverapi_hooks

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)Hooks

# Hooks

Some interfaces of the server API contain methods-hooks that allow to influence the behavior of the server when processing an event. To help you better understand their essence, here is a table comparing the properties of hooks and [events](/en/docs/mt5/api/serverapi_simpleplugin#events).

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Events</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Hooks</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Sent upon the fact of an action.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Sent before an action.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Is intended only for notifications.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Allows influencing the action performed.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">All parameters of methods-events are constant. Accordingly, they can be read but cannot be changed.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Some parameters are not constant. Accordingly, they can be changed.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">All subscribers receive event notifications.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Hooks are handles in the order of <a href="/en/docs/mt5/api/config_plugins" class="topiclink">configurations of plugins</a>. Within a plugin, handling is performed in the order of subscribing to an appropriate interface.</span></p><p class="p_fortable"><span class="f_fortable">Hook is handled until the first method that returns code other than <a href="/en/docs/mt5/api/retcodes_successful" class="topiclink">MT_RET_OK</a> (except otherwise stated). In this case, the hook is not forwarded to next methods.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Methods of events are of the "void" type.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Methods-hooks will always return one of the <a href="/en/docs/mt5/api/reference_retcodes" class="topiclink">return codes</a>.</span></p></td></tr></tbody></table>

Here is a diagram of hook handling:

![Handling Hooks](/en/docs/mt5/api/img/hook_processing.png "Handling Hooks")

[Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)

[Request Processing on the Server](/en/docs/mt5/api/hook_scheme)