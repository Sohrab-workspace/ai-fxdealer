# Importing and Setting Trade Groups

> Source: https://support.metaquotes.net/en/docs/mt5/platform/migration/migration_group

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
            -   [General Settings](/en/docs/mt5/platform/migration/migration_general)
            -   [Financial Instruments](/en/docs/mt5/platform/migration/migration_symbols)
            -   [Trade Groups](/en/docs/mt5/platform/migration/migration_group)
            -   [Import of Accounts and Trades](/en/docs/mt5/platform/migration/migration_account_trade)
            -   [Manager Accounts](/en/docs/mt5/platform/migration/migration_manager)
            -   [Data Feeds](/en/docs/mt5/platform/migration/migration_datafeed)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Migration from MetaTrader 4](/en/docs/mt5/platform/migration)Trade Groups

# Importing and Setting Trade Groups

[Group](/en/docs/mt5/platform/administration/admin_groups) parameters in MetaTrader 5 provide more flexibility as compared to MetaTrader 4. The total number of groups in MetaTrader 5 is not limited.

MetaTrader 5 supports the same functions as MetaTrader 4 except for a few functions related to hedging. MetaTrader 5 does not have the "Multiple Close by orders" and "Auto close-out" functions.

## Import of Groups

Use the [import of groups](/en/docs/mt5/platform/administration/admin_groups/group_import) to copy all groups and their settings from MetaTrader 4 server to the MetaTrader 5 platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When you import groups, existing settings are converted and default values are assigned to missing settings.</span></li><li class="p_tableatten"><span class="f_tableatten">Trade settings of symbols for the groups are not imported.</span></li><li class="p_tableatten"><span class="f_tableatten">Groups from the MetaTrader 4 server are imported into the currently selected groups section.</span></li></ul></td></tr></tbody></table>

![Importing groups from MetaTrader 4 server](/en/docs/mt5/platform/img/migration_group_import.png "Importing groups from MetaTrader 4 server")

Select "MetaTrader 4" server type and specify connection data: IP address and server port, as well as account login and password. The account used for importing symbols should be opened in the manager group and have Administrator right.

![Importing groups from MetaTrader 4 server](/en/docs/mt5/platform/img/migration_group_import2.png "Importing groups from MetaTrader 4 server")

The next window shows the list of all groups that can be imported from MetaTrader 4 server. Selected groups are imported to MetaTrader 5 platform after pressing Import button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">After importing, check the settings of all groups.</span></li><li class="p_tableatten"><span class="f_tableatten">All groups <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#trade_server" class="topiclink">are bound</a> to the main trade server. After importing the binding can be changed.</span></li><li class="p_tableatten"><span class="f_tableatten">Only new groups are imported. Settings of existing groups of the same name are not overwritten.</span></li></ul></td></tr></tbody></table>

## Account Group Settings

MetaTrader 5 platform group settings have more tabs. This is due to the fact that MetaTrader 5 features additional group settings not present in MetaTrader 4. Most MetaTrader 4 settings have remained in MetaTrader 5.

![MetaTrader 5 client groups have more settings](/en/docs/mt5/platform/img/migration_group.png "MetaTrader 5 client groups have more settings")

## Individual Symbol Settings

MetaTrader 5 features considerably expanded [trading symbol settings redefining](/en/docs/mt5/platform/administration/admin_groups/groups_settings#symbols) options.

![MetaTrader 5 allows you to redefine plenty of trading symbol parameters](/en/docs/mt5/platform/img/migration_group_symbol.png "MetaTrader 5 allows you to redefine plenty of trading symbol parameters")

## Commission Settings

In MetaTrader 5, [commission](/en/docs/mt5/platform/administration/admin_groups/groups_settings#commissions) settings can be found on a separate tab. The number of settings has significantly increased: charging time, dependence on trade volume and turnover, etc.

![In MetaTrader 5, commission settings are located on a separate tab](/en/docs/mt5/platform/img/migration_group_commission.png "In MetaTrader 5, commission settings are located on a separate tab")

## Processing Trade Requests

Now, trade request execution settings are not limited to three types ("Manual only, no automation", "Automatic only" and "Manual, but automatic if no dealers online") like in MetaTrader 4. [Routing](/en/docs/mt5/platform/administration/requests_routing) section introduced in MetaTrader 5 allows you to create custom rules and conditions with virtually any combination of settings and execution types.

![Configuring trade requests execution](/en/docs/mt5/platform/img/migration_group_routing.png "Configuring trade requests execution")

[Financial Instruments](/en/docs/mt5/platform/migration/migration_symbols)

[Import of Accounts and Trades](/en/docs/mt5/platform/migration/migration_account_trade)