# MTManagerCreate

> Source: https://support.metaquotes.net/en/docs/mt5/api/managerapi_exported/mtmanagercreate

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
                -   [MTManagerVersion](/en/docs/mt5/api/managerapi_exported/mtmanagerversion)
                -   [MTManagerCreate](/en/docs/mt5/api/managerapi_exported/mtmanagercreate)
                -   [MTManagerCreateExt](/en/docs/mt5/api/managerapi_exported/mtmanagercreateext)
                -   [MTAdminCreate](/en/docs/mt5/api/managerapi_exported/mtadmincreate)
                -   [MTAdminCreateExt](/en/docs/mt5/api/managerapi_exported/mtadmincreateext)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Exported Functions](/en/docs/mt5/api/managerapi_exported)MTManagerCreate

# MTManagerCreate

The MTManagerCreate exported function creates a new instance of the [IMTManagerAPI](/en/docs/mt5/api/imtmanagerapi) interface and returns a pointer to it.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">MTManagerCreate</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">api_version</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;API&nbsp;version</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTManagerAPI**</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">manager</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;pointer&nbsp;to&nbsp;the&nbsp;interface</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

api\_version

\[out\]  The current version of Manager API supported by the server is passed in this parameter.

manager

\[out\]  A pointer to the pointer of the created [IMTManagerAPI](/en/docs/mt5/api/imtmanagerapi) interface.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

The Manager API application can use separate data directories for each manager and administrator interface (to store the local data cache). However, the application log is always written to only one data directory, which is specified during creation of the first interface (no matter whether it is a manager or an administrator interface).

For example, the first interface is created via MTManagerCreate. The path to the data directory is not specified in this function, so the application log will be stored in the default directory, i.e. in the Logs folder of the directory, in which MT5APIManager.dll is located. The log storage location will not be changed even if you explicitly specify a custom data directory when creating the second interface via [MTAdminCreateExt](/en/docs/mt5/api/managerapi_exported/mtadmincreateext).

Calling MTMangerCreate is equivalent to calling [MTMangerCreateExt](/en/docs/mt5/api/managerapi_exported/mtmanagercreateext) with the parameter datapath=NULL.

[MTManagerVersion](/en/docs/mt5/api/managerapi_exported/mtmanagerversion)

[MTManagerCreateExt](/en/docs/mt5/api/managerapi_exported/mtmanagercreateext)