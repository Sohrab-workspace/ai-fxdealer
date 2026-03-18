# Group Types

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/group_types

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
                -   [Group Settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings)
                -   [Group Symbol Settings](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols)
                -   [Commission Settings](/en/docs/mt5/platform/administration/admin_groups/groups_comissions)
                -   [Group Types](/en/docs/mt5/platform/administration/admin_groups/group_types)
                -   [Import of Groups](/en/docs/mt5/platform/administration/admin_groups/group_import)
                -   [Extended Authentication Setup](/en/docs/mt5/platform/administration/admin_groups/group_extended_authentication)
                -   [Position Accounting Systems](/en/docs/mt5/platform/administration/admin_groups/group_position)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Groups](/en/docs/mt5/platform/administration/admin_groups)Group Types

# Group Types

The trading platform allows to work with different types of [groups of accounts](/en/docs/mt5/platform/administration/admin_groups). The system determines the types of groups by their names and processes them respectively. There are following types of groups:

## Demo Groups [#](group_types#demo)

Demo groups contain demo [accounts](/en/docs/mt5/platform/administration/admin_accounts). They allow to work in a training mode without real money to perfect a trading strategy. This kind of accounts offer the same possibilities as the real ones. The difference is that the demo accounts can be opened without corresponding investment, however such accounts cannot be used for earning real money. Demo accounts can be opened directly from the client terminal, and the real ones are only opened from the manager and administrator terminals.

A created group is considered a demo one if its [name](/en/docs/mt5/platform/administration/admin_groups/groups_settings) (including path) includes "demo" symbols (case sensitive). For example, the "demo\\forex", "demo-USD" and "real\\demoforex-USD" groups are demo and the "Demoforex" "fx-USD" groups are not.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Add demo groups to the "<a href="/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups" class="topiclink">Account allocation</a>" section to enable your clients to open accounts in these groups directly via client terminals.</span></p></td></tr></tbody></table>

## Manager Groups [#](group_types#manager)

Groups are considered manager ones if their names (including path) include "manager" symbols (case sensitive). For example, "manager\_CFD" or "manager\_real". Only accounts that belong to the manager groups are able to connect to the trade servers using the manager and administrator terminals and the corresponding APIs. [Manager](/en/docs/mt5/platform/administration/admin_managers) accounts can only be created on the basis of accounts that belong to the manager groups.

## Contest Groups [#](group_types#contest)

This type is intended for conducting contests among traders. Groups are considered contest ones if their names (including path) include "contest" symbols (case sensitive). For example, "contest\_forex" or "contest\\USD".

Contest accounts cannot be opened from terminals, as they can only be created by the broker.

Contest accounts are marked with a blue icon in client terminals. When a trader is connected to such an account, the "Contest account" title is displayed in the terminal window header. In some of the [reports](/en/docs/mt5/platform/administration/admin_reports) contest accounts are shown in separate groups. Contest accounts operate similarly to demo ones.

## Preliminary Group [#](group_types#preliminary)

One preliminary group called "preliminary" is automatically created on the server. [Preliminary accounts](/en/docs/mt5/platform/administration/admin_accounts/preliminary_accounts) are created in it when requests for opening real accounts are sent from the client terminals. Managers can track such accounts and contact the clients using contact details specified during the registration. As soon as an official agreement with a client is made, a manager can move the account to one of the reals groups, what allows the client to start working immediately.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#symbols" class="topiclink">Trading is prohibited</a> for all symbols in the preliminary group.</span></li><li class="p_tableatten"><span class="f_tableatten">All accounts are created with zero balance in the preliminary group.</span></li><li class="p_tableatten"><span class="f_tableatten">When opening an account in such a group, a client receives an email based on the <a href="/en/docs/mt5/platform/components/trade_server/mail_templates" class="topiclink">special template</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Add preliminary groups to the "<a href="/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups" class="topiclink">Account allocation</a>" section to enable your clients to request live accounts directly via client terminals.</span></li></ul></td></tr></tbody></table>

## Coverage Groups [#](group_types#hedge)

Groups are considered as coverage ones if their names (including path) include "coverage" symbols (case sensitive). For example, "coverage\\forex". This type of groups is intended for creating accounts that are used for covering client positions. Summary rates by such accounts are displayed in the manager terminal. A more detailed information is given in a [separate section](/en/docs/mt5/platform/components/gateways/metatrader5gateway#coverage).

## Real Groups [#](group_types#real)

This kind of groups contain account for working with real money. If a group doesn't fall into any category by its name among the ones mentioned above, then the system considers it a real one.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If the groups in the system have certain hierarchy then their <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#name" class="topiclink">names</a> contain the corresponding paths to them. That path is an essential part of a group name and it is considered when determining its type. For example, all the sub-groups of the "manager" group will be considered as manager ones.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Do not use indications of different group types within the name of a group. For example, managers\demo.</span></li></ul></td></tr></tbody></table>

## Recommendations on Naming Groups

For making the work with groups convenient it is recommend to follow several rules when giving the names to groups:

-   It is recommended to give sensible names to the demo groups because they will be visible to the clients when opening demo accounts from the client terminals. Only lower-case and upper-case letters, digits and "\_" (underline), "-" (hyphen) symbols are allowed in the group names;
-   Names of user groups of company offices should end with a certain combination of symbols and should not end with '\_' symbol. For example, '\_kzn';
-   It is possible to unite the groups by their regional (country) belonging. For example, one can add certain symbol combinations to the group names. For example, '\_ru\_'.

[Commission Examples](/en/docs/mt5/platform/administration/admin_groups/groups_comissions/commission_examples)

[Import of Groups](/en/docs/mt5/platform/administration/admin_groups/group_import)