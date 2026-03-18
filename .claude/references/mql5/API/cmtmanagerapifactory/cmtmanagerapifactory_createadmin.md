# CMTManagerAPIFactory::CreateAdmin

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createadmin

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)CreateAdmin

# CMTManagerAPIFactory::CreateAdmin

Create the administrator interface [IMTAdminAPI](/en/docs/mt5/api/imtadminapi).

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">CMTManagerAPIFactory::CreateAdmin</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">version</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Version</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTAdminAPI**</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">admin</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;administrator&nbsp;interface</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">CIMTAdminAPI&nbsp;&nbsp;</span><span class="f_Functions">SMTManagerAPIFactory.CreateAdmin</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">version</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Version</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">out&nbsp;MTRetCode</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">res</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Response&nbsp;code</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

version

\[in\]  Version of the MT5APIManager.h header file

admin

\[out\]  A pointer to the administrator interface [IMTAdminAPI](/en/docs/mt5/api/imtadminapi).

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

The Manager API application can use separate data directories for each manager and administrator interface (to store the local data cache). However, the application log is always written to only one data directory, which is specified during creation of the first interface (no matter whether it is a manager or an administrator interface).

For example, the first interface is created through the first version of CMTManagerAPIFactory::CreateAdmin, in which the path to the data directory is not specified. The application log will be stored in the default directory, i.e. in the Logs folder of the directory, in which MT5APIManager.dll is located. The log storage location will not be changed even if you explicitly specify a custom data directory when creating the second interface.

# CMTManagerAPIFactory::CreateAdmin

Creating the [IMTAdminAPI](/en/docs/mt5/api/imtadminapi) administrator interface specifying the directory where Manager API application data are to be stored.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">CMTManagerAPIFactory::CreateAdmin</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">version</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;version</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">datapath</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;data&nbsp;folder</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTAdminAPI**</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">admin</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;pointer&nbsp;to&nbsp;the&nbsp;administrator&nbsp;interface</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">CIMTAdminAPI&nbsp;&nbsp;</span><span class="f_Functions">SMTManagerAPIFactory.CreateAdmin</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">uint</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">version</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;version</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">string</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">datapath</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;data&nbsp;folder</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">out&nbsp;MTRetCode</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">res</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;response&nbsp;code</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

version

\[in\]  Version of the MT5APIManager.h header file

datapath

\[in\]  The absolute path to the directory where Manager API is to store its data (local cache, journals, etc.) is additionally specified. If NULL, the application stores data in the directory it is launched from.

admin

\[out\]  A pointer to the administrator interface [IMTAdminAPI](/en/docs/mt5/api/imtadminapi).

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

By default, Manager API stores its data in the directory it is launched from. In some cases, the need arises to re-define the data folder, for example, if the application is installed to Program Files of MS Windows Vista or higher. By default, applications installed to Program Files are not allowed to write their data to the installation folder in these systems. In this case, use a special directory in \[system disk letter\]:\\Users\\\[account name in OS\]\\AppData\\Roaming\\\[application data folder\], for example, C:\\Users\\JohnSmith\\AppData\\Roaming\\ManagerAPIApp.

The Manager API application can use separate data directories for each manager and administrator interface (to store the local data cache). However, the application log is always written to only one data directory, which is specified during creation of the first interface (no matter whether it is a manager or an administrator interface).

For example, the first interface is created through the first version of CMTManagerAPIFactory::CreateAdmin, in which the path to the data directory is not specified. The application log will be stored in the default directory, i.e. in the Logs folder of the directory, in which MT5APIManager.dll is located. The log storage location will not be changed even if you explicitly specify a custom data directory when creating the second interface.

[CreateManager](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_createmanager)

[Version](/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_version)