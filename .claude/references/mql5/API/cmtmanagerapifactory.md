# CMTManagerAPIFactory

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtmanagerapifactory

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
                -   [Initialize](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_initialize)
                -   [Shutdown](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_shutdown)
                -   [CreateManager](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createmanager)
                -   [CreateAdmin](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createadmin)
                -   [Version](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_version)
                -   [LicenseCheckAdmin](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_licensecheckadmin)
                -   [LicenseCheckManager](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_licensecheckmanager)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)CMTManagerAPIFactory

# CMTManagerAPIFactory

For easy access to the IMTManagerAPI interface, a [factory of interfaces](/en/docs/mt5/api/cmtmanagerapifactory) is implemented in the MT5Manager.h file. The factory automatically loads the appropriate library (32/64-bit) Manager API and provides access to exported functions.

The Manager API factory performs the basic functions of applications — initialization and deinitialization, as well as creation of interfaces of the Manager API. It contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_initialize" class="topiclink">Initialize</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Initialize the Manager API.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_shutdown" class="topiclink">Shutdown</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Unload DLL from the Manager API.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createmanager" class="topiclink">CreateManager</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Create the manager interface.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createadmin" class="topiclink">CreateAdmin</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Create the administrator interface.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_version" class="topiclink">Version</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the version of the Manager Manager API.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_licensecheckadmin" class="topiclink">LicenseCheckAdmin</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Check whether the Manager API application use is authorized.</span></p></td></tr><tr class="table"><td class="table" style="width:140px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_licensecheckmanager" class="topiclink">LicenseCheckManager</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Check whether the Manager API application use is authorized.</span></p></td></tr></tbody></table>

Using factories in application development is optional. You can use your own implementation of corresponding functions.

[MTAdminCreateExt](/en/docs/mt5/api/managerapi_exported/mtadmincreateext)

[Initialize](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_initialize)