# Import of Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/symbols_import

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
                -   [Symbol Settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings)
                -   [Splicing Futures](/en/docs/mt5/platform/administration/admin_symbols/symbols_splice)
                -   [Import of Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_import)
                -   [Collateral Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_collateral)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Symbols](/en/docs/mt5/platform/administration/admin_symbols)Import of Symbols

# Import of Symbols

Using the administrator terminal you can import [symbols](/en/docs/mt5/platform/administration/admin_symbols) with all their settings from any remote servers of MetaTrader 5 or MetaTrader 4.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">In order to import symbols from another server, there should be any active account (demo or real, but not a manager one).</span></p></td></tr></tbody></table>

To start importing symbols use the "![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from Server" command of the [context menu](/en/docs/mt5/platform/administration/admin_symbols#context) of the Symbols section. After that the following window will appear:

![Import of symbols](/en/docs/mt5/platform/img/import_wizard.png "Import of symbols")

On the first step specify the details of the server from which symbols and details for connecting it will be imported:

-   Server Type — in this field you should select the type of the server from which symbols will be imported: MetaTrader 5 or MetaTrader 4;
-   Server — IP address and port of the server separated by a colon;
-   Login — login for authorizing on the server;
-   Password — password for authorizing on the server;
-   Use certificate from file — if symbols are imported from a MetaTrader 5 server with the enabled mode of [extended authorization](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization), connection using the details of the account specified above will requite a confirmed certificate. If the certificate has been installed in the operating system storage, it will be automatically recognized by the importing system. If the certificate hasn't been installed yet, this option should be enabled and path to the file should be specified manually;

-   Certificate file — press "Browse" and specify the pfx file of the certificate. The file certificate obtained in the terminal is saved to /terminal data folder/profiles/server name/certificates/.
-   Certificate Password — [password](/en/docs/mt5/platform/administrator/getting_started/server_connect/extended_authorization#password) of the certificate.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Import in the extended authorization mode is available only from MetaTrader 5 servers.</span></li><li class="p_tableatten"><span class="f_tableatten">Symbols from a MetaTrader 4 server are imported to the current selected <a href="/en/docs/mt5/platform/administration/admin_symbols#groups" class="topiclink">group</a>. When importing from a MetaTrader 5 server, location of groups is preserved the same as that on the source server.</span></li></ul></td></tr></tbody></table>

After you have specified all the data, press "Next". In case of a successful connection to the server, the list of available symbols will appear in the next window:

![Selecting symbols](/en/docs/mt5/platform/img/symbols_import_choose.png "Selecting symbols")

There are several ways to select symbols:

-   By double clicking on a symbol icon - the icon will become yellow at that;
-   By double clicking on a group icon - all symbols on the group will be selected at that;
-   Using the "Select all" button.

Here you can also view [settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings) of imported symbols. To do it click twice on their names. To start the import press "Done".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If you enable the "Overwrite existing symbols" option, then in case the name of an imported symbol matches one of the existing symbols, all its settings will be overwritten (including path in the hierarchy). If this option is disabled, such symbols will not be imported.</span></li><li class="p_tableatten"><span class="f_tableatten">All symbols are imported with the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#trade_disabled" class="topiclink">disabled</a> trading possibility;</span></li><li class="p_tableatten"><span class="f_tableatten">After importing symbols, please check their settings.</span></li></ul></td></tr></tbody></table>

## Specifics of Import

When importing symbols from a MetaTrader 4 server, parameters are converted, while missing parameters are assigned default values:

-   [Filters](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_filtration)  
    The filtering level of a symbol from MetaTrader 4 is set as [soft](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_filtration#soft_filtration). The hard filtering is 5 times larger, while the discard level is 100 times larger.
-   [Volumes](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#volumes)  
    Default volume levels are set.

Symbols from a MetaTrader 4 server are imported to the current [group](/en/docs/mt5/platform/administration/admin_symbols#groups). When importing symbols from a MetaTrader 5 server location of symbols by groups is preserved the same as that on the source server.

[Splicing Futures](/en/docs/mt5/platform/administration/admin_symbols/symbols_splice)

[Collateral Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_collateral)