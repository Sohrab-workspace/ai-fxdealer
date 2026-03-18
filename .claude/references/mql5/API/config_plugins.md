# Configuration of Plugins

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_plugins

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
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
            -   [Common](/en/docs/mt5/api/config_common)
            -   [Network](/en/docs/mt5/api/config_network)
            -   [Plugins](/en/docs/mt5/api/config_plugins)
                -   [IMTConPlugin](/en/docs/mt5/api/config_plugins/imtconplugin)
                -   [IMTConPluginModule](/en/docs/mt5/api/config_plugins/imtconpluginmodule)
                -   [IMTConPluginSink](/en/docs/mt5/api/config_plugins/imtconpluginsink)
            -   [Data Feeds](/en/docs/mt5/api/config_datafeeds)
            -   [Time](/en/docs/mt5/api/config_time)
            -   [Holidays](/en/docs/mt5/api/config_holiday)
            -   [Firewall](/en/docs/mt5/api/config_firewall)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
            -   [Floating Margin](/en/docs/mt5/api/config_leverage)
            -   [Managers](/en/docs/mt5/api/config_manager)
            -   [History Synchronization](/en/docs/mt5/api/config_historysync)
            -   [Gateways](/en/docs/mt5/api/config_gateway)
            -   [Routing](/en/docs/mt5/api/config_route)
            -   [Reports](/en/docs/mt5/api/config_report)
            -   [Mail Servers](/en/docs/mt5/api/config_email)
            -   [Messengers](/en/docs/mt5/api/config_messenger)
            -   [Automations](/en/docs/mt5/api/config_automation)
            -   [VPS](/en/docs/mt5/api/config_vps)
            -   [KYC](/en/docs/mt5/api/config_kyc)
            -   [Subscriptions](/en/docs/mt5/api/config_subscription)
            -   [Funds and ETF](/en/docs/mt5/api/config_funds)
            -   [Additional Parameters](/en/docs/mt5/api/config_param)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Plugins

# Configuration of Plugins

The MetaTrader 5 API allows managing configurations of plugins in the platform and process events of configuration changes.

The following plugin interfaces are available:

-   [IMTConPlugin](/en/docs/mt5/api/config_plugins/imtconplugin)  
    An interface for configuring plugin parameters.
-   [IMTConPluginModule](/en/docs/mt5/api/config_plugins/imtconpluginmodule)  
    An interface for accessing parameters of plugin modules.
-   [IMTConPluginSink](/en/docs/mt5/api/config_plugins/imtconpluginsink)  
    An interface for handling events associated with the configuration of plugins.

The below figure shows different elements of of plugin configuration in the MetaTrader 5 Administrator, to help you understand the purpose of the interfaces:

![Working with plugins in MetaTrader 5 Administrator](/en/docs/mt5/api/img/plugin_list.png "Working with plugins in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [The name of plugin configuration](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_name).
2.  [The name of the plugin module](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_module).
3.  [Plugin provider](/en/docs/mt5/api/config_plugins/imtconpluginmodule/imtconpluginmodule_vendor).
4.  [The list of plugin configurations.](/en/docs/mt5/api/config_plugins/imtconplugin)
5.  [The plugin operation mode](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_mode).
6.  [Configuring via the manager terminal](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_flags).
7.  [Enabling plugin profiling](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_flags).
8.  [A block for configuring plugin parameters](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_parameteradd).
9.  [A server on which the plugin is running](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_server).
10.  [The name of a plugin parameter](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_parameterget)
11.  [The value of a plugin parameter](/en/docs/mt5/api/config_plugins/imtconplugin/imtconplugin_parameterget)

[OnConServerSync](/en/docs/mt5/api/config_network/imtconserversink/imtconserversink_onconserversync)

[IMTConPlugin](/en/docs/mt5/api/config_plugins/imtconplugin)