# MtSrvManagerProtocol

> Source: https://support.metaquotes.net/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_extension/mtsrvmanagerprotocol

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
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
        -   [Development Features](/en/docs/mt4/api/features)
        -   [Structures](/en/docs/mt4/api/reference_structures)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
            -   [Development of Plugins](/en/docs/mt4/api/server_api/server_api_dev)
            -   [Common Functions](/en/docs/mt4/api/server_api/server_api_common)
            -   [Configuration Databases](/en/docs/mt4/api/server_api/server_api_config)
            -   [Users](/en/docs/mt4/api/server_api/server_api_user)
            -   [Trading](/en/docs/mt4/api/server_api/server_api_trading)
            -   [Price Data](/en/docs/mt4/api/server_api/server_api_chart)
            -   [Mail, News and Notifications](/en/docs/mt4/api/server_api/server_api_mail_news)
            -   [Daily Reports](/en/docs/mt4/api/server_api/server_api_reference_daily)
            -   [Server Services](/en/docs/mt4/api/server_api/server_api_server_services)
            -   [Hooks](/en/docs/mt4/api/server_api/server_api_hook)
                -   [Plugin Initialization/Deinitialization](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_plugin_info)
                -   [Plugin Configuration](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_plugin_config)
                -   [Auxiliary Structures](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_auxiliary)
                -   [Client Database](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_user)
                -   [Data Feeds](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_feeder)
                -   [Configuration Databases](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_config)
                -   [Trading](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_trade)
                -   [Commission and Rollovers](/en/docs/mt4/api/server_api/server_api_hook/server_api_commission_rollover)
                -   [Trading Reports](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_statement)
                -   [Dealings](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_dealer)
                -   [Price Data](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_history)
                -   [Mail and News](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_mail_news)
                -   [Protocol Extension](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_extension)
                    -   [MtSrvTelnet](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_extension/mtsrvtelnet)
                    -   [MtSrvTelnetExt](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_extension/mtsrvtelnetext)
                    -   [MtSrvManagerProtocol](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_extension/mtsrvmanagerprotocol)
        -   [Manager API](/en/docs/mt4/api/manager_api)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Server API](/en/docs/mt4/api/server_api)[Hooks](/en/docs/mt4/api/server_api/server_api_hook)[Protocol Extension](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_extension)MtSrvManagerProtocol

# MtSrvManagerProtocol

Intercepts execution of a manager's custom command.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">int&nbsp;APIENTRY&nbsp;&nbsp;</span><span class="f_Functions">MtSrvManagerProtocol</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;ULONG&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">ip</span><span class="f_CodeExample">,</span><span class="f_Param">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;</span><span class="f_Comments">//&nbsp;IP&nbsp;address</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UserInfo*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">us</span><span class="f_CodeExample">,</span><span class="f_Param">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;</span><span class="f_Comments">//&nbsp;Manager</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;unsigned&nbsp;char*&nbsp;&nbsp;</span><span class="f_Param">in_data</span><span class="f_CodeExample">,</span><span class="f_Param">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Request</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;int&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">in_size</span><span class="f_CodeExample">,</span><span class="f_Param">&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Request&nbsp;size</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">unsigned&nbsp;char**&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">out_data</span><span class="f_CodeExample">,</span><span class="f_Param">&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Response</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">int*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">out_size&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Response&nbsp;size</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

ip

\[out\]  The IP address of the manager that has sent the custom command.

manager

\[out\]  The [UserInfo](/en/docs/mt4/api/reference_structures/structure_user/userinfo) structure that describes the manager account.

in\_data

\[out\]  The buffer of the data passed to the server.

in\_size

\[out\]  The size of the in\_data buffer.

out\_data

\[in\]  A pointer to data returned in response to the command. You should first allocate memory for the returned data using the [HEAP\_ALLOC](/en/docs/mt4/api/server_api/server_api_common/server_api_common_memory/heap_alloc) macro.

out\_size

\[in\]  Size of out\_data.

Return Value

TRUE means that the data is processed, the response should be passed in the out\_data parameter. FALSE means that the plugin cannot process the request.

Note

The hook is called during the call of the [CManagerInterface::ExternalCommand](/en/docs/mt4/api/manager_api/manager_api_extension/cmanagerinterface_externalcommand)manager interface function.

Recommendation: in case an error occurs while processing data within the hook, the error description should be sent to out\_data and TRUE should be returned. FALSE is used when the plugin does not process the manager command.

The hook must return a response to the manager command as soon as possible. The operation is performed in the thread processing manager connection commands. If the hook does not return a response within three minutes, the manager connection will be closed.

[MtSrvTelnetExt](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_extension/mtsrvtelnetext)

[Manager API](/en/docs/mt4/api/manager_api)