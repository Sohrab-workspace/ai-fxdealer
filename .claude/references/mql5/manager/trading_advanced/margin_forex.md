# Retail Forex, CFD, Futures

> Source: https://support.metaquotes.net/en/docs/mt5/manager/trading_advanced/margin_forex

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Trading Operations](/en/docs/mt5/manager/trading)[For Advanced Users](/en/docs/mt5/manager/trading_advanced)Margin Calculation: Retail Forex, CFD, Futures — Netting

# Retail Forex, CFD, Futures

This margin calculation model is used for Retail Forex, CFD and Futures with the [netting position accounting system](/en/docs/mt5/manager/trade_principles#netting). Unlike to the same model for hedging accounts, [spreads](/en/docs/mt5/manager/trading_advanced/margin_forex#spread) are additionally taken into account in this calculation method.

The first stage in margin calculation is defining if an account has positions or pending orders for the symbol the deal is performed for.

-   If that account has no positions and orders for the symbol, the margin is calculated using the [formulas](/en/docs/mt5/manager/trading_advanced/margin_formula).
-   If the account has an open position, and a new order of any type with the volume being less or equal to the current position is placed in the opposite direction, the total margin is equal to the current position's one. Example: we have a 1 lot EURUSD Buy position and place an order to Sell 1 lot EURUSD (similarly for Sell Limit, Sell Stop and Sell Stop Limit).
-   If the account has an open position and an order of any type is placed in the same direction, the total margin is equal to the sum of the current position's and placed order's margins.
-   If the account has an open position, and an order of any type with the volume exceeding the current position is placed in the opposite direction, two margin values are calculated - for the current position and for the placed order. The final margin is taken according to the highest of the two calculated values.
-   If the account has two or more oppositely directed market and limit orders, the margin is calculated for each direction (Buy and Sell). The final margin is taken according to the highest of the two calculated values. For all other order types (Stop and Stop Limit), the margin is summed up (charged for each order).

The margin amount is calculated in several stages:

-   Basic calculation for a certain symbol
-   [Conversion of margin currency into deposit currency](/en/docs/mt5/manager/trading_advanced/margin_forex#conversion)
-   [Multiplication by ratio](/en/docs/mt5/manager/trading_advanced/margin_forex#rate)
-   [Calculations for trading symbols in spread](/en/docs/mt5/manager/trading_advanced/margin_forex#spread)

## Basic Calculation for a Symbol [#](margin_forex#main)

[The basic margin value](/en/docs/mt5/manager/trading_advanced/margin_formula) in accordance with the symbol type is calculated first. The type is specified in the symbol specification as the ["Calculation"](/en/docs/mt5/manager/market_watch#specification) field value.

## Converting into Deposit Currency [#](margin_forex#conversion)

This stage is common for all calculation types. Conversion of the margin requirements calculated using one of the methods mentioned above is performed in case their currency is different from the account deposit one.

The current exchange rate of margin currency to deposit currency is used for conversion. The Ask price is used for buy deals, and the Bid price is used for sell deals.

Suppose that the basic size of the margin previously calculated for buying one lot of EURUSD is 1000 EUR. If the account deposit currency is USD, the current Ask price of EURUSD pair is used for conversion. For example, if the current rate is 1.2790, the total margin size is 1279 USD.

The margin to deposit currency conversion rate is shown in the "Margin rate" field in [orders](/en/docs/mt5/manager/edit_trades#order) and [positions](/en/docs/mt5/manager/edit_trades#position).

## Margin rate [#](margin_forex#rate)

The symbol specification allows setting additional multipliers (rates) for the margin requirements depending on the position/order type. A manager having appropriate permissions can manage these rates in [group settings](/en/docs/mt5/manager/margin#margin).

![Margin rate](/en/docs/mt5/manager/img/margin_rates.png "Margin rate")

The final size of the margin requirements previously calculated regarding conversion into the deposit currency is additionally multiplied by the appropriate rate. In addition, the rates allow complete disabling of margin for selected types of trading operations. To do this, set the zero margin ratio.

For example, the previously calculated margin for buying one lot of EURUSD is 1279 USD. This sum is additionally multiplied by long margin rate. For example, if it is equal to 1.15, the final margin is 1279 \* 1.15 = 1470.85 USD.

## Calculations for Spread Trading [#](margin_forex#spread)

The margin can be charged on preferential basis in case trading positions are in spread relative to each other. The spread is defined as the presence of the oppositely directed positions on related symbols. Reduced margin requirements provide traders with wider trading opportunities. Configuration of spreads is described in a [separate section](/en/docs/mt5/manager/trading_advanced/spreads).

## Application of floating margin rules [#](margin_forex#floating_margin)

Additional rates may be applied to the calculated margin value in accordance with the rules configured in the the [Leverages](/en/docs/mt5/manager/margin#leverage) section.

[Margin Calculation: Basic](/en/docs/mt5/manager/trading_advanced/margin_formula)

[Margin Calculation: Retail Forex, CFD, Futures — Hedging](/en/docs/mt5/manager/trading_advanced/margin_forex_hedge)