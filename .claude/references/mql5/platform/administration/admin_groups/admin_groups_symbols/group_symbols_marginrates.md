# Margin rates

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_marginrates

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
                    -   [Common](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_common)
                    -   [Trade](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_trade)
                    -   [Execution](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_execution)
                    -   [Margin](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_margin)
                    -   [Margin Rates](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_marginrates)
                    -   [Swaps](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_swaps)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Groups](/en/docs/mt5/platform/administration/admin_groups)[Group Symbol Settings](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols)Margin Rates

# Margin rates

![Margin rates](/en/docs/mt5/platform/img/groups_symbols_settings_marginrate.png "Margin rates")

This section contains margin rates for various order types. The rates are set for the initial and maintenance margin individually. If there is no rate for the maintenance margin (equal to zero), the initial margin value is used instead.

-   Use default margin rate settings — use margin rate parameters specified for the symbol in the [corresponding section](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin_rates).
-   Liquidity margin rate — in the [exchange risk management model](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_exchange#assets), clients can use their own assets as collateral for open positions. The liquidity margin rate determines the amount of the current value of an asset for the specified financial instrument, which will be taken into account as collateral (accounted for in client's equity). If the value is set to 0, the instrument cannot be used as collateral.
-   Currency margin rate — rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble. The parameter is used when calculating security deposit for futures contracts ([Exchange FORTS Futures](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula#forts)) traded on Moscow Exchange ([calculating variation margin and security deposit using the current USD exchange rate](https://fs.rts.micex.ru/files/644 "Variation margin and security deposit calculation using the current US Dollar exchange rate") - in Russian). The values are sent by the Moscow Exchange when using the gateway [MetaTrader 5 to MOEX Derivatives](/en/docs/mt5/platform/components/gateways/moex_derivatives).
-   Margin rates — this table contains margin rates for various order types. The rates are set for the initial and maintenance margin individually. If there is no rate for the maintenance margin (equal to zero), the initial margin value is used instead.

-   Market buy order — multiplier for calculating margin requirements for long positions relative to the [main amount of margin](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation);
-   Market sell order — multiplier for calculating margin requirements for short positions relative to the main amount of margin;
-   Buy limit order — multiplier for calculating margin requirements for Buy Limit orders relative to the main amount of margin;
-   Sell limit order — multiplier for calculating margin requirements for Sell Limit orders relative to the main amount of margin;
-   Buy stop order — multiplier for calculating margin requirements for Buy Stop orders relative to the main amount of margin;
-   Sell stop order — multiplier for calculating margin requirements for Sell Stop orders relative to the main amount of margin;
-   Buy stop limit order — multiplier for calculating margin requirements for Buy Stop Limit orders relative to the main amount of margin;
-   Sell stop limit order — multiplier for calculating margin requirements for Sell Stop Limit orders relative to the main amount of margin.

To avoid overriding the coefficient value for a group, leave the value set to "Default". In this case, the corresponding value from the [symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin_rates) will be used. The "Use Default Settings" command applies these default values to all parameters in this section.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If the initial margin is specified, no margin calculations will be performed using the formulas specified in the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#calculation" class="topiclink">"Calculation"</a> field.</span></li><li class="p_tableatten"><span class="f_tableatten">If the maintenance margin size is not specified, the initial margin value will be used instead.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">If the <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#margin" class="topiclink">exchange risk management</a> model is used for a client group and margin rates of an instrument are set to 0, such an instrument is considered to be a non-marginable security. No margin calculations are performed for such instruments (no margin is charged).</span></li></ul></td></tr></tbody></table>

The margin rates are described in details in a [separate section](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex#rate).

[Margin](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_margin)

[Swaps](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_swaps)