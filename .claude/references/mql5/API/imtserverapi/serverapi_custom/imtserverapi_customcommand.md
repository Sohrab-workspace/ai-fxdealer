# IMTServerAPI::CustomCommand

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_custom/imtserverapi_customcommand

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
                -   [Common Functions](/en/docs/mt5/api/imtserverapi/serverapi_common)
                -   [Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)
                -   [Clients](/en/docs/mt5/api/imtserverapi/serverapi_clients)
                -   [Users](/en/docs/mt5/api/imtserverapi/serverapi_users)
                -   [Online Connections](/en/docs/mt5/api/imtserverapi/serverapi_online)
                -   [Certificates](/en/docs/mt5/api/imtserverapi/serverapi_certificate)
                -   [Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)
                -   [History Data](/en/docs/mt5/api/imtserverapi/serverapi_chart)
                -   [Tick Data](/en/docs/mt5/api/imtserverapi/serverapi_ticks)
                -   [Depth of Market](/en/docs/mt5/api/imtserverapi/serverapi_book)
                -   [Mail Database](/en/docs/mt5/api/imtserverapi/serverapi_mail)
                -   [News Database](/en/docs/mt5/api/imtserverapi/serverapi_news)
                -   [Daily Reports](/en/docs/mt5/api/imtserverapi/serverapi_trading_daily)
                -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_subscription)
                -   [Server Services](/en/docs/mt5/api/imtserverapi/serverapi_server_services)
                -   [Geo Services](/en/docs/mt5/api/imtserverapi/serverapi_geo)
                -   [Dataset](/en/docs/mt5/api/imtserverapi/serverapi_dataset)
                -   [Custom Functions](/en/docs/mt5/api/imtserverapi/serverapi_custom)
                    -   [CustomSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_custom/imtserverapi_customsubscribe)
                    -   [CustomUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_custom/imtserverapi_customunsubscribe)
                    -   [CustomCreateStream](/en/docs/mt5/api/imtserverapi/serverapi_custom/imtserverapi_customcreatestream)
                    -   [CustomCommand](/en/docs/mt5/api/imtserverapi/serverapi_custom/imtserverapi_customcommand)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Custom Functions](/en/docs/mt5/api/imtserverapi/serverapi_custom)CustomCommand

# IMTServerAPI::CustomCommand

A custom command can only be sent to another plugin running within the same cluster. Using this method, you can implement your own data exchange mechanism between the servers of your platform:

-   On one server, create a plugin that sends custom commands using IMTServerAPI::CustomCommand.
-   On the second server, create a plugin that processes commands using [IMTCustomSink::HookPluginCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookplugincommand).

This enables the transfer of any data between them. For example, from a plugin on the main trading server, you can request data on positions from a non-main trading server. Such a request cannot be implemented using standard means since each server uses its own databases. Accordingly, each plugin has access only to its specific database.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::CustomCommand</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">server_id</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;server&nbsp;ID</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCVOID</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">indata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;input&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">indata_len</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;input&nbsp;data&nbsp;size</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPVOID&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">outdata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;output&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">UINT&amp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">outdata_len</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;output&nbsp;data&nbsp;size</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

server\_id

\[in\]  The ID of the server to which the command is sent. Corresponds to [IMTConServer::Id](/en/docs/mt5/api/config_network/imtconserver/imtconserver_id).

indata

\[in\]  Data transmitted to the server.

indata\_len

\[in\]  Input data size in bytes.

outdata

\[out\] A reference to the data returned in response to the command. After use, the memory must be freed using [IMTServerAPI::Free](/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_free).

outdata\_len

\[out\]  A reference to the output data size in bytes.

Return Value

The response code sent by the plugin that processed the custom command. If no plugin processed the command in 30 seconds, the response code [MT\_RET\_OK\_NONE](/en/docs/mt5/api/retcodes_successful) will be returned. In case of an error in sending the command, an appropriate response code will be returned.

Note

To process a custom command, a plugin implementing the [IMTCustomSink::HookPluginCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookplugincommand) hook must be installed on the server.

You can send custom commands to plugins running on any servers within your cluster, including the server from which the command is sent.

The method is synchronous. Control is returned to the plugin only after the command processing is complete. Therefore, it is strongly recommended not to call the method from hooks and event handlers.

This function variant is recommended only for infrequent transmission of small amounts of data. The function variant described below is specifically adapted for transmitting large amounts of data.

Sending a large number of commands and a large volume of data can negatively impact the interaction speed between servers in the cluster, affecting the transmission of trading data, ticks, etc. This can be especially noticeable when sending commands between non-main trading servers. Since there is no direct connection between them, all interactions are routed through the main server.

# IMTServerAPI::CustomCommand

Send a custom command to the server.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::CustomCommand</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">server_id</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;server&nbsp;ID</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTByteStream*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">indata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;input&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTByteStream*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">outdata</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;output&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

server\_id

\[in\]  The ID of the server to which the command is sent. Corresponds to [IMTConServer::Id](/en/docs/mt5/api/config_network/imtconserver/imtconserver_id).

indata

\[in\]  A pointer to the [data stream object](/en/docs/mt5/api/reference_bytestream/imtbytestream) transmitted to the server.

outdata

\[out\]  A pointer to the [data steam object](/en/docs/mt5/api/reference_bytestream/imtbytestream) returned in response to the command.

Return Value

The response code sent by the plugin that processed the custom command. If no plugin processed the command, the response code [MT\_RET\_OK\_NONE](/en/docs/mt5/api/retcodes_successful) will be returned. In case of an error in sending the command, an appropriate response code will be returned.

Note

To process a custom command, a plugin implementing the [IMTCustomSink::HookPluginCommand](/en/docs/mt5/api/imtcustomsink/imtcustomsink_hookplugincommand) hook must be installed on the server.

The method is synchronous. Control is returned to the plugin only after the command processing is complete. Therefore, it is strongly recommended not to call the method from hooks and event handlers.

When transferring large volumes of data, as well as when sending data frequently, you should use this particular version of the function.

Sending a large number of commands and a large volume of data can negatively impact the interaction speed between servers in the cluster, affecting the transmission of trading data, ticks, etc. This can be especially noticeable when sending commands between non-main trading servers. Since there is no direct connection between them, all interactions are routed through the main server.

[CustomCreateStream](/en/docs/mt5/api/imtserverapi/serverapi_custom/imtserverapi_customcreatestream)

[Interface of Server Events](/en/docs/mt5/api/imtserversink)