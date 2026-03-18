# IMTAdminAPI::LicenseCheck

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_licensecheck

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
                -   [Common Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_common)
                    -   [Allocate](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_allocate)
                    -   [Free](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_free)
                    -   [LoggerOut](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggerout)
                    -   [LoggerOutString](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggeroutstring)
                    -   [LoggerFlush](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggerflush)
                    -   [LoggerServerRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggerserverrequest)
                    -   [LoggerGatewayRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggergatewayrequest)
                    -   [LoggerFeederRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggerfeederrequest)
                    -   [Release](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_release)
                    -   [LicenseCheck](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_licensecheck)
                    -   [PasswordChange](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_passwordchange)
                -   [Connection to the Server](/en/docs/mt5/api/imtadminapi/imtadminapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtadminapi/imtadminapi_network)
                -   [Server Management](/en/docs/mt5/api/imtadminapi/imtadminapi_server_manage)
                -   [Configuration Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_config)
                -   [Clients](/en/docs/mt5/api/imtadminapi/imtadminapi_clients)
                -   [Users](/en/docs/mt5/api/imtadminapi/imtadminapi_user)
                -   [Trade Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_trading)
                -   [Mail Database](/en/docs/mt5/api/imtadminapi/imtadminapi_mail)
                -   [News Database](/en/docs/mt5/api/imtadminapi/imtadminapi_news)
                -   [History Data](/en/docs/mt5/api/imtadminapi/imtadminapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtadminapi/imtadminapi_tick)
                -   [Settings Files](/en/docs/mt5/api/imtadminapi/imtadminapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtadminapi/imtadminapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_custom)
                -   [ECN](/en/docs/mt5/api/imtadminapi/imtadminapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtadminapi/imtadminapi_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Administrator Interface](/en/docs/mt5/api/imtadminapi)[Common Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_common)LicenseCheck

# IMTAdminAPI::LicenseCheck

Check the application license.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTAdminAPI::LicenseCheck</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">MTLicenseCheck&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">check</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Name&nbsp;of&nbsp;the&nbsp;license&nbsp;module</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTAdminAPI.LicenseCheck</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ref&nbsp;MTLicenseCheck</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">check</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Name&nbsp;of&nbsp;the&nbsp;license&nbsp;module</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

check

\[in\]  A reference to the [MTLicenseCheck](/en/docs/mt5/api/mtlicensecheck) structure that describes the license.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred, which corresponds to the response code.

Note

License verification can only be performed after [connection to a server](/en/docs/mt5/api/imtadminapi/imtadminapi_connection/imtadminapi_connect), otherwise the method will return the [MT\_RET\_ERR\_DATA](/en/docs/mt5/api/retcodes_common) error.

## Working with licenses

MetaTrader 5 Manager API allows the protection of applications from unauthorized use. Protection considers that the application use authorization is determined in the MetaTrader 5 platform license generated by the platform developer, [MetaQuotes Ltd.](https://www.metaquotes.net/ "MetaQuotes Ltd.")

The algorithm for working with the license is described below:

-   A unique application name is defined in the program code.
-   This name must be sent to MetaQuotes Software Corp. to include it to the MetaTrader 5 platform licenses of the indicated companies.
-   The IMTAdminAPI::LicenseCheck is called, to which the filled [MTLicenseCheck](/en/docs/mt5/api/mtlicensecheck) structure is passed as a parameter. The following fields should be filled out in the structure:
    -   name — application name;
    -   random — a random sequence of up to 256 characters;
    -   random\_size — the size of the generated sequence.
-   The IMTAdminAPI::LicenseCheck method sends the specified information to the server.
-   The server checks if the use of the application with the specified name is authorized in the license.
-   The server sends the MTLicenseCheck structure back with the following additional fields filled:
    -   retcode — [verification result code](/en/docs/mt5/api/reference_retcodes);
    -   sign — the digital signature of the response code, name and random sequence.  The server signs the data with its own private key;
    -   sign\_size — data size in the sign field.
-   The application signs the same data (retcode+name+random) with its own public key and compares the result with the signature ('sign') received from the server. Thus, the authenticity of the received data is checked.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For easier license check, the Manager API factory provides a special <a href="/en/docs/mt5/api/cmtmanagerapifactory/cmtmanagerapifactory_licensecheckadmin" class="topiclink">CMTManagerAPIFactory::LicenseCheckAdmin</a> method. The main steps of the above license verification algorithm are already implemented in that method. When using the factory method, a programmer only needs to pass a pointer to the Manager API and the application name to it.</span></p></td></tr></tbody></table>

[Release](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_release)

[PasswordChange](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_passwordchange)