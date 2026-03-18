# IMTManagerAPI::CustomCommand

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom/imtmanagerapi_customcommand

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
                    -   [CustomCommand](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom/imtmanagerapi_customcommand)
                    -   [CustomCreateStream](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom/imtmanagerapi_customcreatestream)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Manager Interface](/en/docs/mt5/api/imtmanagerapi)[Custom Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom)CustomCommand

# IMTManagerAPI::CustomCommand

Sends a custom command to the server.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::CustomCommand</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCVOID</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">indata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Input&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">indata_len</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Size&nbsp;of&nbsp;input&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPVOID&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">outdata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Output&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">outdata_len</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Size&nbsp;of&nbsp;output&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">byte[]&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.CustomCommand</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">byte[]</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">indata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Input&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">out&nbsp;MTRetCode</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">res</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Response&nbsp;code</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

indata

\[in\]  Data returned to the server.

indata\_len

\[in\]  Size of data to pass in bytes.

outdata

\[out\]  A reference to the data returned in response to the command.

outdata\_len

\[out\]  A reference to the size of data returned in response to the command.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

An appropriate plugin must be installed in the server for processing custom commands ([IMTCustomSink::HookManagerCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookmanagercommand)).

It is recommended to use this variant of the function only when working with small and infrequent data transmissions. The second variant of the function described below is adapted for transmission of large amount of data.

# IMTManagerAPI::CustomCommand

Sends a custom command to the server.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTManagerAPI::CustomCommand</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTByteStream*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">indata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Input&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTByteStream*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">outdata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Output&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTManagerAPI.CustomCommand</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTByteStream</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">indata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Input&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTByteStream</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">outdata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Output&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

indata

\[in\]  A pointer to the [object of a byte stream](/en/docs/mt5/api/reference_bytestream/imtbytestream) passed to the server.

outdata

\[out\]  A pointer to the [object of a byte stream](/en/docs/mt5/api/reference_bytestream/imtbytestream) returned in response to the command.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error has occurred that corresponds to the response code.

Note

An appropriate plugin must be installed in the server for processing custom commands. ([IMTCustomSink::HookManagerCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookmanagercommand)).

For transmission of large amount of data and for frequent transmissions it is recommended to use this exact variant of the function.

[Custom Functions](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom)

[CustomCreateStream](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_custom/imtmanagerapi_customcreatestream)