# Group Types

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_groups/group_types

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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
                -   [Group Types](/en/docs/mt4/administrator/administration/ug_groups/group_types)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Groups](/en/docs/mt4/administrator/administration/ug_groups)Group Types

# Group Types

The trading platform allows to work with different types of [groups of accounts](/en/docs/mt4/administrator/administration/ug_groups). The system determines the types of groups by their names and processes them respectively. There are following types of groups:

## Demo Groups [#](group_types#demo)

Demo groups contain demo [accounts](/en/docs/mt4/administrator/administration/ug_accounts). They allow to work in a training mode without real money to perfect a trading strategy. This kind of accounts offer the same possibilities as the real ones. The difference is the demo accounts can be opened without corresponding investment, however one cannot pretend to any profit from them. Demo accounts can be opened directly from the client terminal, and the real ones only from the manager and administrator ones.

A created group is considered a demo one if its [name](/en/docs/mt4/administrator/administration/ug_groups#group_common) includes "demo" symbols (case sensitive). For example, the "demoforex", "demo-USD" and "real-demoforex-USD" groups are demo and the "Demoforex" "fx-USD" groups are not.

## Manager Groups [#](group_types#manager)

Only one manager group called "manager" can exist within a trade platform. It is created automatically and cannot be deleted. Only accounts that belong to the manager groups are able to connect to the trade servers using the manager and administrator terminals and the corresponding APIs. [Manager](/en/docs/mt4/administrator/administration/ug_managers) accounts can only be created on the basis of accounts that belong to the manager group.

## Contest Groups [#](group_types#contest)

This type is intended for conducting contests among traders. Groups are considered contest ones if their names include "contest" symbols (case sensitive). For example, "contest\_forex" or "contest-USD".

## Preliminary Group [#](group_types#perliminary)

One preliminary group called "preliminary" is automatically created on the server. Preliminary accounts are created in it when requests for opening real accounts are sent from the client terminals. Managers can track such accounts and contact the clients using contact details specified during the registration. As soon as an official agreement with a client is made, a manager can move the account to one of the reals groups, what allows the client to start working immediately.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Accounts in this group are created with certain restrictions:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">They have a zero balance.</span></li><li class="p_tableatten"><span class="f_tableatten">Trading is prohibited (even if you allow trading for the accounts in the "preliminary" group).</span></li></ul></td></tr></tbody></table>

## Coverage Groups [#](group_types#hedge)

Only one coverage group called "coverage" can exist within a trade platform. It is not created automatically, it can be created by an administrator of the server. This group is intended for creating accounts that are used for covering client positions. Summary rates by such accounts are displayed in the manager terminal.

## Real Groups [#](group_types#real)

This kind of groups contain account for working with real money. If a group doesn't fall into any category by its name among the ones mentioned above, then the system considers it a real one.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Do not use indications of different group types within the name of a group. For example, managers\demo.</span></p></td></tr></tbody></table>

## Recommendations on Naming Groups

For making the work with groups convenient it is recommend to follow several rules when giving the names to groups:

-   It is recommended to give sensible names to the demo groups because they will be visible to the clients when opening demo accounts from the client terminals. Only lower-case and upper-case letters, digits and "\_" (underline), "-" (hyphen) symbols are allowed in the group names;
-   Names of user groups of company offices should end with a certain combination of symbols and should not end with '\_' symbol. For example, '\_kzn';
-   It is possible to unite the groups by their regional (country) belonging. For example, one can add certain symbol combinations to the group names. For example, '\_ru\_'.

[Groups](/en/docs/mt4/administrator/administration/ug_groups)

[Managers](/en/docs/mt4/administrator/administration/ug_managers)