# Operation on Weekend

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_gateways/gateway_weekend

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
                -   [Configuration of Gateways](/en/docs/mt5/platform/administration/admin_gateways/gateways_config)
                -   [Status](/en/docs/mt5/platform/administration/admin_gateways/gateway_status)
                -   [Journal of Gateways](/en/docs/mt5/platform/administration/admin_gateways/journal_gateway)
                -   [Positions](/en/docs/mt5/platform/administration/admin_gateways/gateway_positions)
                -   [Setup of Routing](/en/docs/mt5/platform/administration/admin_gateways/gateways_routing)
                -   [Setup as Service](/en/docs/mt5/platform/administration/admin_gateways/gateway_service)
                -   [Operation on Weekend](/en/docs/mt5/platform/administration/admin_gateways/gateway_weekend)
                -   [Symbol and Price Translation](/en/docs/mt5/platform/administration/admin_gateways/gateway_translation)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Gateways](/en/docs/mt5/platform/administration/admin_gateways)Operation on Weekend

# Operation on Weekend

There may be cases when the gateway should work during the weekends, for example, on Saturday. In order to allow this, implement the necessary changes to the trading platform and the gateway settings.

## Configure the platform working time

Allow the platform operation during a weekend in the [Time](/en/docs/mt5/platform/administration/admin_time) section:

![Configuring the trading platform's working time](/en/docs/mt5/platform/img/gateway_server_worktime.png "Configuring the trading platform's working time")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Change the platform working time settings back at the end of the trading day.</span></p></td></tr></tbody></table>

## Configure the gateway working time

Trading Calendar Holidays parameter used for re-defining working/non-working time is supported at all gateways on Gateway API level.

To add a non-working day, specify a value of the form +DDMMM. The date is specified as two digits, the month is specified as the first three letters of the month name in English. For example, +01JAN. To add a working day on Saturday or Sunday, specify a value of the type -DDMMM, for example, -07FEB. You can specify multiple working/non-working days, separated by semicolons, for example, + 01JAN;-07FEB.

![Configuring the gateway working time](/en/docs/mt5/platform/img/gateway_weekend.png "Configuring the gateway working time")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Delete this parameter at the end of the trading day.</span></p></td></tr></tbody></table>

Some gateways may ignore the 'Trading Calendar Holidays' parameter. It depends on their implementation and trading venue specifics:

-   The [MetaTrader 4](/en/docs/mt5/platform/components/gateways/metatrader4gateway) and [MetaTrader 5](/en/docs/mt5/platform/components/gateways/metatrader5gateway) gateways remain active on holidays and weekends regardless of the parameter. Their working hours are determined by the platform settings.
-   Gateways to liquidity providers, such as [Integral](/en/docs/mt5/platform/components/gateways/integral), [Currenex](/en/docs/mt5/platform/components/gateways/currenex) and others are disabled on holidays and weekend regardless of the parameter. It is believed that liquidity from these providers is always unavailable on weekends and holidays.
-   The [MOEX Derivatives](/en/docs/mt5/platform/components/gateways/moex_derivatives) gateways receives an operation schedule directly from the exchange and it ignores the parameter.
-   The [MOEX Securities](/en/docs/mt5/platform/components/gateways/moex_securities) and [MOEX FX](/en/docs/mt5/platform/components/gateways/moex_fx) gateways operate only on weekdays by default. The parameter can be used for these gateways.

For further details please read the relevant gateway documentation.

## Configure trade symbol working time

Add trade and quotation sessions on a weekend for trade symbols. You can edit multiple symbols simultaneously. To do that, select them in the list while holding Ctrl or Ctrl+Shift.

![Configuring trade symbol working time](/en/docs/mt5/platform/img/gateway_weekend_symbols.png "Configuring trade symbol working time")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Change the settings back at the end of the trading day.</span></p></td></tr></tbody></table>

[Setup as Service](/en/docs/mt5/platform/administration/admin_gateways/gateway_service)

[Symbol and Price Translation](/en/docs/mt5/platform/administration/admin_gateways/gateway_translation)