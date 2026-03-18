# IMTServerAPI::PluginCurrent

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_plugincurrent

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
                    -   [Common](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_common)
                    -   [Network](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_network)
                    -   [Plugins](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins)
                        -   [PluginCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_plugincreate)
                        -   [PluginModuleCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginmodulecreate)
                        -   [PluginParamCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginparamcreate)
                        -   [PluginSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginsubscribe)
                        -   [PluginUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginunsubscribe)
                        -   [PluginCurrent](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_plugincurrent)
                        -   [PluginAdd](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginadd)
                        -   [PluginDelete](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_plugindelete)
                        -   [PluginShift](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginshift)
                        -   [PluginTotal](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_plugintotal)
                        -   [PluginNext](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginnext)
                        -   [PluginGet](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginget)
                        -   [PluginModuleTotal](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginmoduletotal)
                        -   [PluginModuleNext](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginmodulenext)
                        -   [PluginModuleGet](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginmoduleget)
                    -   [Data Feeds](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_datafeeds)
                    -   [Time](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_time)
                    -   [Holidays](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_holiday)
                    -   [Firewall](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_firewall)
                    -   [Symbols](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_symbol)
                    -   [Spreads](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_spread)
                    -   [Groups](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group)
                    -   [Managers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_manager)
                    -   [History Synchronization](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_historysync)
                    -   [Gateways](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_gateway)
                    -   [Routing](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_route)
                    -   [Reports](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_report)
                    -   [Mail Servers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_email)
                    -   [Messengers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_messenger)
                    -   [Automation](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation)
                    -   [VPS](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_vps)
                    -   [KYC](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_kyc)
                    -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_subscription)
                    -   [Floating Margin](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_leverage)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)[Plugins](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins)PluginCurrent

# IMTServerAPI::PluginCurrent

Get the configuration of the current plugin.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::PluginCurrent</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTConPlugin*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">plugin</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;a&nbsp;plugin&nbsp;configuration</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

plugin

\[out\]  An object of plugin configuration. The plugin object must be first created using the [IMTServerAPI::PluginCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_plugincreate) method.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

This method copies the configuration data of the current plugin to the plugin object.

[PluginUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginunsubscribe)

[PluginAdd](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins/imtserverapi_pluginadd)