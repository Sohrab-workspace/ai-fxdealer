# IMTManagerAPI::LoggerFlush

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerflush

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
                -   [Common Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common)
                    -   [Allocate](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_allocate)
                    -   [Free](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_free)
                    -   [LoggerOut](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerout)
                    -   [LoggerOutString](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggeroutstring)
                    -   [LoggerFlush](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerflush)
                    -   [LoggerServerRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerserverrequest)
                    -   [Release](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_release)
                    -   [LicenseCheck](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_licensecheck)
                    -   [PasswordChange](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_passwordchange)
                -   [Connection to the Server](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_network)
                -   [Configuration Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_config)
                -   [Selected Symbols](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_selected)
                -   [Clients](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_clients)
                -   [Users](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_user)
                -   [Online Connections](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_online)
                -   [Trade Databases](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trading)
                -   [History Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_tick)
                -   [Mail Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_mail)
                -   [News Database](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_news)
                -   [Trade Activity](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_trade_operations)
                -   [Market Depth](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_book)
                -   [Summary Positions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_summary)
                -   [Exposure](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_exposure)
                -   [Daily Reports](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_daily)
                -   [Settings Files](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom)
                -   [ECN](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_geo)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Common Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common)LoggerFlush

# IMTManagerAPI::LoggerFlush

The function for flushing the file buffer of the local journal of the manager interface to a disk.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">void&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::LoggerFlush</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">void&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.LoggerFlush</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">ManagerAPI.LoggerFlush</span><span class="f_CodeExample">()</span></p></td></tr></tbody></table>

[LoggerOutString](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggeroutstring)

[LoggerServerRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerserverrequest)