# Examples of Settings

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/groups_comissions/commission_examples

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Groups](/en/docs/mt5/platform/administration/admin_groups)[Commission Settings](/en/docs/mt5/platform/administration/admin_groups/groups_comissions)Commission Examples

# Examples of Settings

Let us consider some commission configuration examples.

### Standard commission

![Standard commission setting example](/en/docs/mt5/platform/img/commission_example_standard.png "Standard commission setting example")

Such a commission will be applied when any of the clients from the group performs a deal for a symbol from the "Forex" subgroup. Commission will be charged on both entry and exit deals. The amount will be debited from the trader's account immediately after the operation using a balance deal of the "Commission" type.

For each deal with a volume of up to 10 lots, 1 unit in the group's deposit currency will be charged. For deals with a volume of 11 to 20 lots, 0.9 currency units will be charged. No commission will be charged for larger deals.

### Profit commission

![Commission on profitable trades](/en/docs/mt5/platform/img/commission_example_profit.png "Commission on profitable trades")

Such a commission will be applied when a client from the group performs a profitable trade for a symbol from the "Forex" subgroup. Although no deal direction filter is set, commission will only be charged for exit deals. Entry deals do not have a financial result; therefore, they do not have profit and do no participate in calculations. The amount will be debited from the trader's account immediately after the operation using a balance deal of the "Commission" type.

For each deal with a profit up to 1,000 units of deposit currency, a commission of 0.5% of the profit amount will be charged. For example, if a deal profit is USD 540, the commission will be equal to USD 2.7. For deals with the profit from 1,001 to 10,000 units, commission will be equal to 0.6% of the profit. No commission will be charged for trades with a larger profit.

[Commission Calculation](/en/docs/mt5/platform/administration/admin_groups/groups_comissions/commission_calculation)

[Group Types](/en/docs/mt5/platform/administration/admin_groups/group_types)