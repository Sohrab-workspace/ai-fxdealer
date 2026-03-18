# Basic Margin Calculation

> Source: https://support.metaquotes.net/en/docs/mt5/manager/trading_advanced/margin_formula

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
            -   [Basic Principles](/en/docs/mt5/manager/trade_principles)
            -   [Market Watch](/en/docs/mt5/manager/market_watch)
            -   [Market Depth](/en/docs/mt5/manager/depth_of_market)
            -   [Economic Calendar](/en/docs/mt5/manager/economic_calendar)
            -   [Trading Notifications](/en/docs/mt5/manager/trade_alerts)
            -   [Working with Trading Positions](/en/docs/mt5/manager/positions)
            -   [Working with Trading Orders](/en/docs/mt5/manager/orders)
            -   [Viewing and Editing Trading Operations](/en/docs/mt5/manager/edit_trades)
            -   [For Advanced Users](/en/docs/mt5/manager/trading_advanced)
                -   [Margin Calculation: Basic](/en/docs/mt5/manager/trading_advanced/margin_formula)
                -   [Margin Calculation: Retail Forex, CFD, Futures — Netting](/en/docs/mt5/manager/trading_advanced/margin_forex)
                -   [Margin Calculation: Retail Forex, CFD, Futures — Hedging](/en/docs/mt5/manager/trading_advanced/margin_forex_hedge)
                -   [Margin Calculation: Stock Exchange](/en/docs/mt5/manager/trading_advanced/margin_exchange)
                -   [Spreads](/en/docs/mt5/manager/trading_advanced/spreads)
                -   [Collateral Symbols](/en/docs/mt5/manager/trading_advanced/symbols_collateral)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Trading Operations](/en/docs/mt5/manager/trading)[For Advanced Users](/en/docs/mt5/manager/trading_advanced)Margin Calculation: Basic

# Basic Margin Calculation

The trading platform provides several margin requirement calculation types depending on the financial instrument. Calculation type is displayed in the "Calculation" field of the [symbol specification](/en/docs/mt5/manager/market_watch#calculation): Margin calculation formula for each instrument depends on the risk management formulaused for the client group:

-   [for Retail Forex, Futures](/en/docs/mt5/manager/trading_advanced/margin_forex) — used for the OTC market. Margin calculation is based on the type of instrument.
-   [for Retail Forex, CFD, Futures with hedging](/en/docs/mt5/manager/trading_advanced/margin_forex) — used for OTC market. Margin calculation is based on the type of instrument, as well as group settings. The [hedging position accounting](/en/docs/mt5/manager/trade_principles#hedging) is used.
-   [for Stock Exchange, based on margin discount rates](/en/docs/mt5/manager/trading_advanced/margin_exchange) — used for the exchange market. Margin calculation is based on the discounts for instruments. Discounts are set by the broker, however they cannot be lower than the exchange set values.

The model is set for each client group on the trading server. To view the model you are using, open the [margin tab](/en/docs/mt5/manager/groups) in the group dialog:

![Margin settings](/en/docs/mt5/manager/img/group_position_system.png "Margin settings")

The basic calculation is only the first stage in the calculation of the final margin value. The value calculated by formulas is always converted to the deposit currency, after which the margin rate and other parameters are additionally applied. A detailed calculation scheme is provided in separate sections for each risk management system.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the <a href="/en/docs/mt5/manager/market_watch#specification" class="topiclink">Initial Margin</a> parameter value is specified in symbol settings, this value will be used. The formulas described in this section will not be applied.</span></p></td></tr></tbody></table>

## Forex

The margin for Forex market symbols is calculated using the following equation:

All modes: Volume in lots \* Contract size / Leverage

For example, let's calculate the margin requirements for buying one lot of EURUSD, while [the size of one contract](/en/docs/mt5/manager/market_watch#contract_size) is 100,000 and the leverage is 1:100.

![Margin calculation for Forex symbols](/en/docs/mt5/manager/img/margin_forex.png "Margin calculation for Forex symbols")

By substituting the appropriate values to the formula, we obtain the following result:

1 \* 100000 / 100 = EUR 1000

So, now we have the margin requirements value in base currency (or [margin currency](/en/docs/mt5/manager/market_watch#margin_currency)) of the symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Generally, margin requirements currency matches the symbol's base currency. If the margin currency is different, calculation results are displayed in the margin currency rather than the symbol's base currency.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">In this mode, a client leverage is taken into account even if a <a href="/en/docs/mt5/manager/trading_advanced/margin_formula#fixed" class="topiclink">fixed margin</a> is set.</span></li></ul></td></tr></tbody></table>

## Forex No Leverage [#](margin_formula#noleverage)

This type of calculation is also used for Forex symbols. However, it ignores the client's leverage, in contrast to the previous calculation type:

All modes: Volume in lots \* Contract size

For example, let's calculate the margin requirements for buying one lot of EURUSD, while [the size of one contract](/en/docs/mt5/manager/market_watch#contract_size) is 100,000 and the leverage is 1:100. After placing the appropriate values to the equation, we will obtain the following result:

1 \* 100,000 = EUR 100,000

So, now we have the margin requirements value in base currency (or margin currency) of the symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Generally, margin requirements currency matches the symbol's base currency. If the margin currency is different, calculation results are displayed in the margin currency rather than the symbol's base currency.</span></p></td></tr></tbody></table>

## CFDs [#](margin_formula#cfd)

Margin requirements for CFDs are calculated using the following formula:

All modes: Volume in lots \* Contract size \* Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell deals.

For example, let's calculate the margin requirements for buying one lot of oil, with the contract size being 100 barrels, and the current Ask price being USD 80.

![Margin calculation for CFD and Exchange Stocks](/en/docs/mt5/manager/img/margin_cfd.png "Margin calculation for CFD and Exchange Stocks")

By substituting the appropriate values to the formula, we obtain the following result:

1 \* 100 \* 80 = USD 8,000

So, now we have the margin value in the base currency (or margin currency) of the symbol.

## CFD Leverage

The leverage is also considered in this type of margin requirement calculation for CFDs:

All modes: Volume in lots \* Contract size \* Open market price / Leverage

## CFD Index [#](margin_formula#cfd_index)

For index CFDs, the margin requirements are calculated according to the following equation:

All modes: Volume in lots \* Contract size \* Open market price \* Tick price / Tick size

In addition to the usual calculation for CFDs, the formula takes into account the tick [price](/en/docs/mt5/manager/market_watch#tick_price) to tick [size](/en/docs/mt5/manager/market_watch#tick_size) ratio.

![Margin calculation for CFD Index](/en/docs/mt5/manager/img/margin_cfd_index.png "Margin calculation for CFD Index")

## Futures, Exchange Futures [#](margin_formula#futures)

There are two types of margin requirements for futures contracts:

-   Initial margin is the amount that must be available on the account at the moment of attempting to enter the market. Further maintenance of the same amount may not be obligatory.
-   Maintenance margin is the minimum amount that must be available on the account for holding a position open.

Both values are specified in the [symbol specification](/en/docs/mt5/manager/market_watch#initial_margin).

![Margin calculation for Futures and Exchange Futures](/en/docs/mt5/manager/img/margin_exchange.png "Margin calculation for Futures and Exchange Futures")

The final margin amount depends on the volume:

Volume in lots \* Initial margin

Volume in lots \* Maintenance margin

The same calculation method is applied for all risk management modes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the amount of the maintenance margin is not specified, the initial margin value will be used instead.</span></p></td></tr></tbody></table>

## Exchange Options [#](margin_formula#options)

There are two types of margin requirements for futures contracts:

-   Initial margin is the amount that must be available on the account at the moment of attempting to enter the market. Further maintenance of the same amount may not be obligatory.
-   Maintenance margin is the minimum amount that must be available on the account for holding a position open.

Both values are specified in the [symbol specification](/en/docs/mt5/manager/market_watch#initial_margin). The final size of the margin depends on the volume:

Volume in lots \* Initial margin

Volume in lots \* Maintenance margin

If the amount of the maintenance margin is not specified, the initial margin value will be used instead. If neither the initial nor the maintenance margin is specified, the appropriate value will be calculated according to the following formula:

Volume in lots \* Contract size \* Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell deals.

The same calculation method is applied for all risk management modes.

## Exchange Stocks, Exchange MOEX Stocks [#](margin_formula#stocks)

Margin requirements for stocks are calculated using the following formula:

Retail Forex, CFD, Futures: Volume in lots \* Contract size \* Open market price

Retail Forex, CFD, Futures with hedged position: Volume in lots \* Contract size \* Open market price

The current market Ask price is used for buy deals, while the current Bid price is used for sell deals.

For example, let's calculate the margin requirements for buying one lot of oil, with the contract size being 100 barrels, and the current Ask price being USD 80. By substituting the appropriate values to the formula, we obtain the following result:

1 \* 100 \* 80 = USD 8,000

So, now we have the margin value in the base currency (or margin currency) of the symbol.

In the "Stock Exchange, based on margin discount rates" mode, margin for stocks is calculated as an indicative value, for assessing the trading account state relative to available positions. In this case, the margin amount is not blocked on the account and therefore does not reduce available funds. For details, please see the [appropriate section](/en/docs/mt5/manager/trading_advanced/margin_exchange).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The only difference for the Exchange Stocks and Exchange MOEX Stocks modes is the <a href="/en/docs/mt5/manager/trading_advanced/margin_exchange#corrected" class="topiclink">calculation of the adjusted initial margin</a> when using the exchange model for risk management.</span></p></td></tr></tbody></table>

## Exchange Bonds, Exchange MOEX Bonds [#](margin_formula#bonds)

The bond margin is calculated as part of the position value. Bond prices are provided as a face value percentage, so the position value is calculated as follows:

Retail Forex, CFD, Futures: Volume in lots \* Contract size \* Face value \* Open price / 100

Retail Forex, CFD, Futures with hedged position: Volume in lots \* Contract size \* Face value \* Open price / 100

The part of the position value to be reserved for maintenance is determined by [margin ratios](/en/docs/mt5/manager/trading_advanced/margin_forex#rate).

In the "Stock Exchange, based on margin discount rates" mode, bond margin is calculated as an indicative value, for assessing the trading account state relative to available positions. In this case, the margin amount is not blocked on the account and therefore does not reduce available funds. For details, please see the [appropriate section](/en/docs/mt5/manager/trading_advanced/margin_exchange).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The position value is calculated in the symbol's base currency (not in the profit currency).</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The only difference for the Exchange Bonds and Exchange MOEX Bonds modes is the <a href="/en/docs/mt5/manager/trading_advanced/margin_exchange#corrected" class="topiclink">calculation of the adjusted initial margin</a> when using the exchange model for risk management.</span></li></ul></td></tr></tbody></table>

## Exchange FORTS Futures [#](margin_formula#forts)

The margin for the futures contracts of the Moscow Exchange derivative section is calculated separately for each symbol: First, the margin is calculated for the open position and all Buy orders. Then the margin for the same position and all Sell orders is calculated. The calculation is the same in all risk management modes.

MarginBuy  = MarginPos + Sum(MarginBuyOrder)

MarginSell = MarginPos + Sum(MarginSellOrder))

The largest one of the calculated values is used as the final margin value for the symbol.

Thus, the same position is used in the calculation of both values. In the first formula (which includes Buy orders), the position margin is calculated as follows:

MarginPos  = Volume \* (InitialMarginBuy  + (Open Price - SettlementPrice) \* Tick Price / Tick Size \* (1 + 0.01 \* Margin Currency Rate))

The volume is used with a positive sign for long positions and with a negative sign for short positions.

In the second formula (which includes Sell orders), the position margin is calculated as follows:

MarginPos = Volume \* (InitialMarginSell + (SettlementPrice - Open Price) \* Tick Price / Tick Size \* (1 + 0.01 \* Margin Currency Rate))

The volume is used with a positive sign for short positions and with a negative sign for long positions.

This approach provides the trader a discount on margin, when there is an open position in the opposite direction with respect to the orders placed (the position acts as collateral for orders).

Margin on orders is calculated by the following formulas:

MarginBuyOrder  = Volume \* (InitialMarginBuy  + (Price - SettlementPrice) \* Tick price / Tick size \* (1 + 0.01 \* Margin currency rate))

MarginSellOrder = Volume \* (InitialMarginSell + (SettlementPrice - Price) \* Tick price / Tick size \* (1 + 0.01 \* Margin currency rate))

'Price' here depends on the order time and can be equal to:

-   The highest and the lowest contract price of the current session are used for the market or Stop Buy and Sell orders, which have not yet been executed. Since the price is not specified in market orders, the trader is charged the maximum possible margin. Once triggered, stop orders behave similar to market orders.
-   The order price is used for limit orders.
-   The Stop Limit price is used for stop limit orders.

Other parameters in the formulas:

-   InitialMarginBuy — the initial margin for the Buy operation.
-   InitialMarginSell — the initial margin for the Sell operation.
-   Currency margin rate is the rate change radius of the currency, a futures contract is denominated in, relative to the Russian ruble
-   SettlementPrice — the symbol's settlement price for the current session.

All these parameters for calculation are provided by the Moscow Exchange.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">InitialMarginBuy is displayed in the "Initial margin" field, InitialMarginSell is shown in the "Maintenance Margin" field in <a href="/en/docs/mt5/manager/market_watch#specification" class="topiclink">contract specification</a>.</span></p></td></tr></tbody></table>

Calculation example

The below example shows the calculation of margin requirements for the following trading account state:

-   Position Buy 3.00 Si-6.18 at 73640
-   Order Buy Limit 2.00 Si-6.18 at 73000
-   Order Sell Limit 10.00 Si-6.18 at 74500

Current session parameters

-   Clearing price = 73638
-   InitialMarginBuy = 7665.41
-   InitialMarginSell = 7739.59
-   Tick price = 1
-   Tick size = 1
-   Margin currency rate = 0

We substitute the values ​​in the formulas

MarginBuy  = 3 \* (7665.41 + (73640 - 73638) \* 1/1) + 2 \* (7665.41 + (73000-73638) \* 1/1) = 37057.05

MarginSell = -3 \* (7739.59 + (73638-73640) \* 1/1) +10.0 \* (7739.59 + (73638-74500) \* 1/1) = 45563.13

Margin = Max(37057.05, 45563.13) = 45563.13

The resulting margin for the Si-6.18 symbol is 45563.13.

## Collateral [#](margin_formula#collateral)

Non-tradable instruments of this type are used as trader's assets to provide the [required margin for open positions](/en/docs/mt5/manager/account_overview#collateral) on other instruments. For these instruments the margin is not calculated.

## Fixed Margin [#](margin_formula#fixed)

If a non-zero value is specified in [symbol specification](/en/docs/mt5/manager/market_watch#initial_margin) in the "Initial margin" field, then no calculations by above formulas are performed (except for the calculation of [futures](/en/docs/mt5/manager/trading_advanced/margin_formula#futures), which is not affected). In this case, for all types of calculations (except for Forex and CFD Leverage), the margin is obtained as if "Futures" option is selected:

Volume in lots \* Initial margin

Volume in lots \* Maintenance margin

For Forex and CFD Leverage calculation types, the leverage is additionally considered:

Volume in lots \* Initial margin / Leverage

Volume in lots \* Maintenance margin / Leverage

The same calculation method is applied for all risk management modes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the amount of the maintenance margin is not specified, the initial margin value will be used instead.</span></p></td></tr></tbody></table>

## End-of-day margin conversion rate recalculation [#](margin_formula#recalculate_margin)

This option assists brokers in meeting regulatory requirements (in particular, NFA requirements), which limit the maximum allowed leverage for different symbol types.

In currency pair trading, the margin determined in the symbol's base currency is converted into the account deposit currency. For example, when trading EURUSD with a contract size of 100,000 and a leverage of 1:100, the margin will be EUR 1,000 per lot. If the trader's deposit currency is USD, the margin will be converted from EUR to USD at the current rate. The conversion rate is registered in the position's [Margin rate](/en/docs/mt5/manager/edit_trades#margin_rate) field.

The EURUSD exchange rate will change over time, and the USD equivalent of EUR 1,000 will change accordingly. Thus, the trader's actual leverage may become greater or less than the original one.

To prevent this from happening, the trading platform provides a mechanism for updating margin conversions. It is activated by the new "Recalculate margin exchange rate at the end of day" option in [symbol settings](/en/docs/mt5/manager/margin#recalculate_margin).

![End-of-day margin conversion rate recalculation](/en/docs/mt5/manager/img/margin_rate_recalculation.png "End-of-day margin conversion rate recalculation")

At the end of the trading day, the server will update the "Margin rate" field in all positions for the instruments with the recalculation enabled. The new value will be calculated using the current market prices for the relevant client groups (similar procedures performed during trade execution).

Please note the following features:

-   The margin rate is not recalculated on the days marked as non-working in the platform (according to the server settings)
-   The margin rate is recalculated after swaps calculations (if no swaps are charged, the rate is recalculated too)
-   If the required price is not available (zero) at the time of recalculation, no recalculation is performed

The recalculation process can be tracked in the trade server log. It will show the following records:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">margin&nbsp;rates&nbsp;update&nbsp;started</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">margin&nbsp;rates&nbsp;update&nbsp;finished&nbsp;</span></p></td></tr></tbody></table>

[For Advanced Users](/en/docs/mt5/manager/trading_advanced)

[Margin Calculation: Retail Forex, CFD, Futures — Netting](/en/docs/mt5/manager/trading_advanced/margin_forex)