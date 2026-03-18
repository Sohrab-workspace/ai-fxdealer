# Debugging

> Source: https://support.metaquotes.net/en/docs/mt5/api/serverapi_debug

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)Debugging

# Debugging

All components of the MetaTrader 5 trading platform are reliably protected and do not permit connection in debug mode. In order to facilitate the plugin development and debugging, the special debug (developer) versions of trade and history servers are available. They have functional limitations and cannot be used for real work but allow you to debug plugins instead.

## Dev server limitations

-   The same master password "Trader" and investor password "Invest" is used for all accounts including manager ones. The password that is actually set for an account will not be accepted by the server. For example, if the account master password is "abc123", you should use "Trader" instead; if the account investor password is "def456", you should use "Invest" instead.
-   The "Manager" password is always used for [connections via Web API](/en/docs/mt5/api/webapi_preparing#account_setup), regardless of the password actually set for the account.
-   [Extended authorization](https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization) via SSL certificates and [one-time passwords](https://support.metaquotes.net/en/docs/mt5/platform/administrator/getting_started/server_connect/otp) (OTP) are disabled. Even if these functions are enabled, only the Trader password can be used for authorization.
-   No [account import](https://support.metaquotes.net/en/docs/mt5/platform/migration/migration_account_trade) either from MetaTrader 4, or from MetaTrader 5.
-   Crash logs are disabled.

## Where to find the dev servers

The dev servers are distributed similarly to other components — when updating via LiveUpdate and in the installers. The executable files are placed near the server main files:

-   mt5trade64.dev.exe — dev version in the trade server installation directory.
-   mt5history64.dev.exe — dev version in the history server installation directory.

## How to debug plugins

First, compile a plugin in debug mode and copy its DLL file to the \\plugins directory of the trade or history server. Next, enable the plugin via MetaTrader 5 Administrator.

![Enabling a plugin in MetaTrader 5 Administrator](/en/docs/mt5/api/img/debug_plugin_config.png "Enabling a plugin in MetaTrader 5 Administrator")

[Profiling](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_plugins#profiling) can be of use at this stage in order to evaluate the plugin performance. The server collects its operation statistics and sends it to the journal every 5 minutes.

After enabling the plugin, open its project in Microsoft Visual Studio and go to the debugging settings: Debug -> project properties. Specify the following parameters:

-   Command — path to the debug server
-   Command Arguments — /console for running in console mode
-   Working Directory — path to the server directory

![Setting up a plugin project for debugging in Microsoft Visual Studio](/en/docs/mt5/api/img/debug_studio_settings.png "Setting up a plugin project for debugging in Microsoft Visual Studio")

Now you can start debugging.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Do not forget to re-compile the plugin and copy its new version to the \plugins directory of the server after changing the source code.</span></p></td></tr></tbody></table>

[Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)

[Ready-made Examples](/en/docs/mt5/api/serverapi_examples)