# Basic Margin Calculation

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula

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
                    -   [Common](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common)
                    -   [Currency](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_currency)
                    -   [Quotes](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_filtration)
                    -   [Trade](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade)
                        -   [Margin Calculation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation)
                            -   [Basic Margin Calculation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula)
                            -   [Retail Forex, CFD, Futures — Netting](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex)
                            -   [Retail Forex, CFD, Futures — Hedging](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex_hedge)
                            -   [Stock Exchange](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_exchange)
                        -   [Profit Calculation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/profit_calculation)
                        -   [Conversion](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/conversion)
                    -   [Futures](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_futures)
                    -   [Options](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_options)
                    -   [Bonds](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_bonds)
                    -   [Execution](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution)
                    -   [Margin](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin)
                    -   [Margin Rates](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin_rates)
                    -   [Swaps](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps)
                    -   [Sessions](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Symbols](/en/docs/mt5/platform/administration/admin_symbols)[Symbol Settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings)[Trade](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade)[Margin Calculation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation)Basic Margin Calculation

# Basic Margin Calculation

The trading platform provides several margin requirement calculation types depending on the financial instrument. You can select the calculation type in [Calculation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#calculation) field of Trade tab. Margin calculation formula for each instrument depends on the [risk management formula](/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk) used for the client group.

The basic calculation is only the first stage in the calculation of the final margin value. The value calculated by formulas is always converted to the deposit currency, after which the margin rate and other parameters are additionally applied. A detailed calculation scheme is provided in separate sections for each risk management system:

-   [Retail Forex, CFD, Futures — Netting](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex)
-   [Retail Forex, CFD, Futures — Hedging](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex_hedge)
-   [Exchange Model](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_exchange)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin#initial" class="topiclink">Initial Margin</a> parameter value is specified in symbol settings, this value will be used. The formulas described in this section will not be applied.</span></p></td></tr></tbody></table>

## Forex

The margin for Forex market symbols is calculated using the following equation:

All modes: Volume in lots \* Contract size / Leverage

For example, let's calculate the margin requirements for buying one lot of EURUSD, while [the size of one contract](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#contract_size) is 100,000 and the leverage is 1:100. After placing the appropriate values to the equation, we will obtain the following result:

1 \* 100000 / 100 = EUR 1000

So, now we have the margin requirements value in [base currency](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_currency#base_currency) (or [margin currency](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_currency#margin_currency)) of the symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Generally, margin requirements currency and symbol's base currency are the same. If the margin currency is different, calculation results are displayed in that currency instead of the symbol's base one.</span></li><li class="p_tableatten"><span class="f_tableatten">In this mode, a client leverage is taken into account even if a <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_formula#fixed" class="topiclink">fixed margin</a> is set.</span></li></ul></td></tr></tbody></table>

## Forex No Leverage [#](margin_formula#noleverage)

This type of calculation is also used for Forex symbols. But unlike the previous one, it does not take into account the client's leverage:

All modes: Volume in lots \* Contract size

For example, let's calculate the margin requirements for buying one lot of EURUSD, while [the size of one contract](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#contract_size) is 100,000 and the leverage is 1:100. After placing the appropriate values to the equation, we will obtain the following result:

1 \* 100,000 = EUR 100,000

So, now we have the margin requirements value in base currency (or margin currency) of the symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Generally, margin requirements currency and symbol's base currency are the same. If the margin currency is different, calculation results are displayed in that currency instead of the symbol's base one.</span></p></td></tr></tbody></table>

## CFDs [#](margin_formula#cfd)

The margin requirements for CFDs are calculated using the following equation:

All modes: Volume in lots \* Contract size \* Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell ones.

For example, let's calculate the margin requirements for buying one lot of oil, the size of the contract is 100 barrels, the current Ask price is USD 80. After placing the appropriate values to the equation, we will obtain the following result:

1 \* 100 \* 80 = USD 8,000

So, now we have the margin value in base currency (or margin currency) of the symbol.

## CFD Leverage

The leverage is also considered in this type of margin requirement calculation for CFDs:

All modes: Volume in lots \* Contract size \* Open market price / Leverage

## CFD Index [#](margin_formula#cfd_index)

For index CFDs, the margin requirements are calculated according to the following equation:

All modes: Volume in lots \* Contract size \* Open market price \* Tick value / Tick size

In addition to the usual calculation for CFDs, the formula takes into account the tick [value](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#tick_price) to tick [size](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#tick_size) ratio.

## Futures, Exchange Futures [#](margin_formula#futures)

There are two types of the margin requirements for futures contracts:

-   Initial margin is the amount that must be available on the account at the moment of attempting to enter the market. Further maintenance of the same sum may not be obligatory.
-   Maintenance margin is the minimum amount that must be available on the account for holding a position open.

Both values are specified in [Margin](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin) tab of the symbol settings. The final size of the margin depends on the volume:

Volume in lots \* Initial margin

Volume in lots \* Maintenance margin

The calculation is the same in all risk management modes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the amount of the maintenance margin is not specified, the initial margin value will be used instead.</span></p></td></tr></tbody></table>

## Exchange Options [#](margin_formula#options)

There are two types of margin requirements for futures contracts:

-   Initial margin is the amount that must be available on the account at the moment of attempting to enter the market. Further maintenance of the same amount may not be obligatory.
-   Maintenance margin is the minimum amount that must be available on the account for holding a position open.

Both values are specified in [Margin](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin) tab of the symbol settings. The final size of the margin depends on the volume:

Volume in lots \* Initial margin

Volume in lots \* Maintenance margin

If the amount of the maintenance margin is not specified, the initial margin value will be used instead. If neither the initial nor the maintenance margin is specified, the appropriate value will be calculated according to the following formula:

Volume in lots \* Contract size \* Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell deals.

The same calculation method is applied for all risk management modes.

## Exchange Stocks, Exchange MOEX Stocks [#](margin_formula#stocks)

The margin requirements for stocks are calculated using the following equation:

Retail Forex, CFD, Futures: Volume in lots \* Contract size \* Open market price

Retail Forex, CFD, Futures with hedged position: Volume in lots \* Contract size \* Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell ones.

For example, let's calculate the margin requirements for buying one lot of oil, the size of the contract is 100 barrels, the current Ask price is USD 80. After placing the appropriate values to the equation, we will obtain the following result:

1 \* 100 \* 80 = USD 8,000

So, now we have the margin value in base currency (or margin currency) of the symbol.

In the "Stock Exchange, based on margin discount rates" mode, margin for stocks is calculated as an indicative value, for assessing the trading account state relative to available positions. In this case, the margin amount is not blocked on the account and therefore does not reduce available funds. For details, please see the [appropriate section](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_exchange).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The only difference for the Exchange Stocks and Exchange MOEX Stocks modes is the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_exchange#corrected" class="topiclink">calculation of the adjusted initial margin</a> when using the exchange model for risk management.</span></p></td></tr></tbody></table>

## Exchange Bonds, Exchange MOEX Bonds [#](margin_formula#bonds)

The bond margin is calculated as part of the position value. Bond prices are provided as a face value percentage, so the position value is calculated as follows:

Retail Forex, CFD, Futures: Volume in lots \* Contract size \* Face value \* Open price / 100

Retail Forex, CFD, Futures with hedged position: Volume in lots \* Contract size \* Face value \* Open price / 100

The part of the position value to be reserved for maintenance is determined by [margin rates](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin_rates).

In the "Stock Exchange, based on margin discount rates" mode, bond margin is calculated as an indicative value, for assessing the trading account state relative to available positions. In this case, the margin amount is not blocked on the account and therefore does not reduce available funds. For details, please see the [appropriate section](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_exchange).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The position value is calculated in the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_currency#base_currency" class="topiclink">symbol's base currency</a> (not in the profit currency).</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The only difference for the Exchange Bonds and Exchange MOEX Bonds modes is the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_exchange#corrected" class="topiclink">calculation of the adjusted initial margin</a> when using the exchange model for risk management.</span></li></ul></td></tr></tbody></table>

## Exchange FORTS Futures [#](margin_formula#forts)

The margin for the futures contracts of the Moscow Exchange derivative section is calculated separately for each symbol: First, the margin is calculated for the open position and all Buy orders. Then the margin for the same position and all Sell orders is calculated. The calculation is the same in all risk management modes.

MarginBuy  = MarginPos + Sum(MarginBuyOrder)

MarginSell = MarginPos + Sum(MarginSellOrder))

The largest one of the calculated values is used as the final margin value for the symbol.

Thus, the same position is used in the calculation of both values. In the first formula (which includes Buy orders), the position margin is calculated as follows:

MarginPos  = Volume \* (InitialMarginBuy  + (Open Price - SettlementPrice) \* Tick Value / Tick Size \* (1 + 0.01 \* Margin Currency Rate))

The volume is used with a positive sign for long positions and with a negative sign for short positions.

In the second formula (which includes Sell orders), the position margin is calculated as follows:

MarginPos = Volume \* (InitialMarginSell + (SettlementPrice - Open Price) \* Tick Value / Tick Size \* (1 + 0.01 \* Margin Currency Rate))

The volume is used with a positive sign for short positions and with a negative sign for long positions.

This approach provides the trader a discount on margin, when there is an open position in the opposite direction with respect to the orders placed (the position acts as collateral for orders).

Margin on orders is calculated by the following formulas:

MarginBuyOrder  = Volume \* (InitialMarginBuy  + (Price - SettlementPrice) \* Tick value / Tick size \* (1 + 0.01 \* Margin currency rate))

MarginSellOrder = Volume \* (InitialMarginSell + (SettlementPrice - Price) \* Tick value / Tick size \* (1 + 0.01 \* Margin currency rate))

'Price' here depends on the order time and can be equal to:

-   The [Highest](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#prices) and the [Lowest price](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#prices) of the contract for the current session is used for not yet executed market or stop Buy and Sell orders, respectively. Since the price is not specified in market orders, the trader is charged the maximum possible margin. Once triggered, stop orders behave similar to market orders.
-   The order price is used for limit orders.
-   The Stop Limit price is used for stop limit orders.

Other parameters in the formulas:

-   InitialMarginBuy — the initial margin for the Buy operation.
-   InitialMarginSell — the initial margin for the Sell operation.
-   Currency margin rate is the rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble
-   SettlementPrice — [settlement price](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#prices) of an instrument for the current session.

All these parameters for calculation are provided by the Moscow Exchange.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">InitialMarginBuy is written to the "Initial margin" field, InitialMarginSell is written to the "Maintenance Margin" field in <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin" class="topiclink">symbol properties</a>.</span></p></td></tr></tbody></table>

Calculation example

The below example shows the calculation of margin requirements for the following trading account state:

-   Position Buy 3.00 Si-6.18 at 73640
-   Order Buy Limit 2.00 Si-6.18 at 73000
-   Order Sell Limit 10.00 Si-6.18 at 74500

Current session parameters

-   Clearing price = 73638
-   InitialMarginBuy = 7665.41
-   InitialMarginSell = 7739.59
-   Tick value = 1
-   Tick size = 1
-   Margin currency rate = 0

We substitute the values ​​in the formulas

MarginBuy  = 3 \* (7665.41 + (73640 - 73638) \* 1/1) + 2 \* (7665.41 + (73000-73638) \* 1/1) = 37057.05

MarginSell = -3 \* (7739.59 + (73638-73640) \* 1/1) +10.0 \* (7739.59 + (73638-74500) \* 1/1) = 45563.13

Margin = Max(37057.05, 45563.13) = 45563.13

The resulting margin for the Si-6.18 symbol is 45563.13.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The Exchange FORTS Futures mode must only be used together with the <a href="/en/docs/mt5/platform/components/gateways/moex_derivatives" class="topiclink">MOEX Derivatives Gateway</a>. Otherwise the margin requirements calculation results may be unpredictable.</span></p></td></tr></tbody></table>

## Collateral [#](margin_formula#collateral)

Non-tradable instruments of this type are used as trader's assets to provide the [required margin for open positions](/en/docs/mt5/platform/administration/admin_accounts/account_edit#collateral) of other instruments. For these instruments the margin is not calculated.

## Fixed Margin [#](margin_formula#fixed)

If a non-zero value is specified in the ["Initial margin"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin#initial) field, then no calculations by formulas specified in the "Calculation" field are performed (except for the calculation of [futures](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex), which is not affected). In this case, for all types of calculations (except for Forex and CFD Leverage), the margin is obtained as if "Futures" option is selected:

Volume in lots \* Initial margin

Volume in lots \* Maintenance margin

For Forex and CFD Leverage calculation types, the leverage is additionally considered:

Volume in lots \* Initial margin / Leverage

Volume in lots \* Maintenance margin / Leverage

The calculation is the same in all risk management modes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the amount of the maintenance margin is not specified, the initial margin value will be used instead.</span></p></td></tr></tbody></table>

## End-of-day margin conversion rate recalculation [#](margin_formula#recalculate_margin)

This option assists brokers in meeting regulatory requirements (in particular, NFA requirements), which limit the maximum allowed leverage for different symbol types.

In currency pair trading, the margin determined in the symbol's base currency is converted into the account deposit currency. For example, when trading EURUSD with a contract size of 100,000 and a leverage of 1:100, the margin will be EUR 1,000 per lot. If the trader's deposit currency is USD, the margin will be converted from EUR to USD at the current rate. The conversion rate is registered in the position's [Margin rate](/en/docs/mt5/platform/administration/admin_positions#margin_rate) field.

The EURUSD exchange rate will change over time, and the USD equivalent of EUR 1,000 will change accordingly. Thus, the trader's actual leverage may become greater or less than the original one.

To prevent this from happening, the trading platform provides a mechanism for updating margin conversions. It is activated by the "Recalculate margin exchange rate at the end of day" option in [common symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin#recalculate_margin) or in [group-specific symbol settings](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols/group_symbols_margin#recalculate_margin).

![End-of-day margin conversion rate recalculation](/en/docs/mt5/platform/img/margin_rate_recalculation.png "End-of-day margin conversion rate recalculation")

At the [end of the trading day](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server#end_of_day), the server will update the "Margin rate" field in all positions for the instruments with the recalculation enabled. The new value will be calculated using the current market prices for the relevant client groups (similar procedures performed during trade execution).

Please note the following features:

-   The margin rate is not recalculated on the days marked as non-working in the platform (according to the [Time section settings](/en/docs/mt5/platform/administration/admin_time))
-   The margin rate is recalculated after swaps calculations (if no swaps are charged, the rate is recalculated too)
-   If the required price is not available (zero) at the time of recalculation, no recalculation is performed

The recalculation process can be tracked in the trade server log. It will show the following records:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">margin&nbsp;rates&nbsp;update&nbsp;started</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">margin&nbsp;rates&nbsp;update&nbsp;finished&nbsp;</span></p></td></tr></tbody></table>

The recalculation is carried out only when a symbol margin currency is different from the account deposit currency. If the margin currency and the deposit currency are the same, then no recalculation is actually carried out. However, a record on updating the margin ratio value is still sent to the server journal. In this case, it will always be equal to 1.00000. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;margin&nbsp;rates&nbsp;for&nbsp;'EURUSD'&nbsp;positions&nbsp;updated&nbsp;-&nbsp;buy:&nbsp;1.00000000,&nbsp;sell:&nbsp;1.00000000</span></p></td></tr></tbody></table>

[Margin Calculation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation)

[Retail Forex, CFD, Futures — Netting](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex)