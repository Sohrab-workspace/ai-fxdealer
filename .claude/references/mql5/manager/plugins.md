# Managing Plugins on the Trade Server

> Source: https://support.metaquotes.net/en/docs/mt5/manager/plugins

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
            -   [Spread, Commission and Swap](/en/docs/mt5/manager/groups)
            -   [Margin](/en/docs/mt5/manager/margin)
            -   [Managing Plugins](/en/docs/mt5/manager/plugins)
            -   [Trade Server Journal](/en/docs/mt5/manager/server_journal)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)Managing Plugins

# Managing Plugins on the Trade Server

Plugins are the modules for enhancing the platform functionality. They are installed on the trade server. Plugins allow you to change the behavior of the platform's native functions, as well as add custom ones, integrate the platform with other systems, and much more. The Manager terminal enables managing plugins installed on the trade server.

Open Plugins section in the Navigator. It features the list of plugins you can manage.

![Plugins](/en/docs/mt5/manager/img/plugins.png "Plugins")

Double-click a plugin name to configure its operation parameters. The Enable option allows to enable/disable the plugin. Below are editable parameters. Their set depends on the plugin. To modify a parameter, double-click the Value field.

If you accidentally remove the parameter, it can be added again using the appropriate button. String type parameters are created by default. To select another type (integer or fractional) click the arrow on the "Add" button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">A manager can only change the settings of the plugins that are explicitly allowed to be modified on the trade server. The "Configurable by managers" option should be enabled in the configuration of such plugins.</span></li><li class="p_tableatten"><span class="f_tableatten">Each configuration of the plugin is bound to a specific trade server. Thus, the Manager can configure plugins only for the server it is currently connected to.</span></li><li class="p_tableatten"><span class="f_tableatten">Be careful when changing the plugin settings. This may significantly affect the platform performance.</span></li></ul></td></tr></tbody></table>

[Margin](/en/docs/mt5/manager/margin)

[Trade Server Journal](/en/docs/mt5/manager/server_journal)