# Commission Calculation

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/groups_comissions/commission_calculation

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
                    -   [Commission Calculation](/en/docs/mt5/platform/administration/admin_groups/groups_comissions/commission_calculation)
                    -   [Commission Examples](/en/docs/mt5/platform/administration/admin_groups/groups_comissions/commission_examples)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Groups](/en/docs/mt5/platform/administration/admin_groups)[Commission Settings](/en/docs/mt5/platform/administration/admin_groups/groups_comissions)Commission Calculation

# Commission Calculation

The periodicity of calculation and charging of trade operation is specified in the ["Charge"](/en/docs/mt5/platform/administration/admin_groups/groups_comissions#charge) field. The following variants possible:

-   Instant — commissions are charged instantly during execution of each deal. The value of a standard commission charged instantly is displayed in the Commission field of a [deal](/en/docs/mt5/platform/administration/admin_deals). Agent commissions are charged as separate balance operations (["Agent commission" deals](/en/docs/mt5/platform/administration/admin_deals#action)).
-   Daily — the commission amount is accumulated during a day in a special field of a client record. At [the end of the day](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#end_of_day) the accumulated amount is charged from the account with a separate balance operation (a deal of the Daily commission or Daily agent commission type).
-   Monthly — the commission amount is accumulated during a month in a special field of a client record. At the end of the month the accumulated amount is charged from the account with a separate balance operation (a deal of the Monthly commission or Monthly agent commission type).

This section describes how the daily and monthly calculation of commissions is performed.

## Blocking of Assets

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The mechanism of asset blocking is implemented only for the standard commissions to guarantee the possibility of paying of commission by clients. It is not used for agent commissions since that are not charged from clients that perform trade operations.</span></p></td></tr></tbody></table>

Depending on the option chosen, the preliminary calculated amount of commission is blocked at client account during a day or a month:

-   If commission is charged for volume of a single trade operation, then its size can be calculated immediately. The corresponding volume of assets is blocked at the account.
-   If commission is charged for turnover (in money of volume), the system considers the volume of trade operations performed earlier during the current day/month. As soon as the client's daily/monthly turnover exceeds a certain level, the amount of the locked commission is immediately recalculated in accordance with the next level.

The volume of blocked assets is displayed in the row of state of client account:

![Blocked commission](/en/docs/mt5/platform/img/commission_account_state.png "Blocked commission")

Blocked assets are excluded from Equity and Free Margin. Thus they cannot be used for trading. The commission that will be blocked for a placed order is also considered when checking the free margin.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Commission is also blocked when placing all the types of pending orders. At that if a pending order is deleted, the corresponding volume of commission is unblocked. If a pending order is filled, only the commission that corresponds to the filled volume of the order stays blocked.</span></li><li class="p_tableatten"><span class="f_tableatten">Blocked assets are also released for all deleted, closed and canceled trade requests that didn't result in execution of a deal.</span></li></ul></td></tr></tbody></table>

## Charging of Commissions

The final calculation and charging of commissions are performed at the end of day or month depending on the [settings](/en/docs/mt5/platform/administration/admin_groups/groups_comissions#charge). The turnover of trade operations for the specified period is calculated. Further the final calculation of commissions is performed, and then they are summed up for each client. In case of standard commission, the total amount of commission is withdrawn from client account as a balance operation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">According to each commission configuration only one balance operation is performed for each client. The entire volume of commissions accumulated during a day/month is charged with a single deal.</span></li><li class="p_tableatten"><span class="f_tableatten">After the deal of charging the standard commission is performed the volume of blocked assets is zeroized.</span></li><li class="p_tableatten"><span class="f_tableatten">The final calculation and charging of commissions are performed at the end of day or month depending on the <a href="/en/docs/mt5/platform/administration/admin_groups/groups_comissions#charge" class="topiclink">settings</a>. This peculiarity should be considered when moving accounts between groups with different commission settings. For example, if during a trade day an account is moved from a group with commissions charged daily to a group without commissions, no commission will be charged from that account for all the operations performed on that day.</span></li></ul></td></tr></tbody></table>

In case of agent commission, the assets are charged to agent accounts using balance operations. Just the same as the standard commissions, one balance operation is performed according to each commission configuration. Balance operations are performed separately for each account, where an agent account is specified.

Account number, from operations on which an agent gets a commission, is specified as a comment to the corresponding balance deal used for accruing the agent commission. The comment is specified in the following form:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">agent</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">from</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">#xxxxxxx</span></p></td></tr></tbody></table>

![Commission deal](/en/docs/mt5/platform/img/commission_deal.png "Commission deal")

Commission deals can have the following types:

-   DAILY COMMISSION — standard commission charged daily;
-   MONTHLY COMMISSION — standard commission charged monthly;
-   DAILY AGENT COMMISSION — agent commission charged daily;
-   MONTHLY AGENT COMMISSION — agent commission charged monthly;

The "Comment" field of the deal contains text specified in the ["Description"](/en/docs/mt5/platform/administration/admin_groups/groups_comissions#description) field of the commission configuration or the number of an account, from operations on which an agent commission is charged.

[Commission Settings](/en/docs/mt5/platform/administration/admin_groups/groups_comissions)

[Commission Examples](/en/docs/mt5/platform/administration/admin_groups/groups_comissions/commission_examples)