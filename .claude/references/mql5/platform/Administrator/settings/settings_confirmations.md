# Confirmations

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/settings/settings_confirmations

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
        -   [Terminal Settings](/en/docs/mt5/platform/administrator/settings)
            -   [Common](/en/docs/mt5/platform/administrator/settings/settings_common)
            -   [Support](/en/docs/mt5/platform/administrator/settings/settings_support)
            -   [Events](/en/docs/mt5/platform/administrator/settings/settings_events)
            -   [Confirmations](/en/docs/mt5/platform/administrator/settings/settings_confirmations)
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
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Terminal Settings](/en/docs/mt5/platform/administrator/settings)Confirmations

# Confirmations

From this section, you can enable or disable additional confirmation requests for dangerous actions executed via the Administrator terminal.

The dangerous actions include:

-   Moving configurations via drag'n'drop (to protect against accidental actions)
-   Sorting and deleting configurations; sending configuration changes to the server (the Apply command)
-   Deleting and restoring records from backup
-   Restarting cluster components

When performing any of these actions, the terminal requests additional confirmation. Confirmations can be disabled for experienced administrators, or when performing a large platform reconfiguration.

![Configuring confirmation of dangerous actions](/en/docs/mt5/platform/img/settings_confirmations.png "Configuring confirmation of dangerous actions")

The confirmation is always requested for actions applied to 10 or more entries.

[Events](/en/docs/mt5/platform/administrator/settings/settings_events)

[Manager](/en/docs/mt5/manager)