# Exchange Risk Management Model

> Source: https://support.metaquotes.net/en/docs/mt5/manager/trading_advanced/margin_exchange

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Trading Operations](/en/docs/mt5/manager/trading)[For Advanced Users](/en/docs/mt5/manager/trading_advanced)Margin Calculation: Stock Exchange

# Exchange Risk Management Model

Exchange risk management model is the calculation of collateral on positions on the basis of symbol discounts which the broker defines based on data provided by the exchange.

## Basic Terminology

### Assets [#](margin_exchange#assets)

Assets — the current value of purchased financial instruments (of long positions) defined in client's deposit currency. The value is determined dynamically based on the price of the latest deal of the financial instrument, taking into account the liquidity margin rate. In fact, the amount of assets is equivalent to the amount of money that the trader would receive in case of immediate closure of long positions.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Assets&nbsp;=&nbsp;Value1&nbsp;*&nbsp;L1&nbsp;&nbsp;+&nbsp;Value2&nbsp;*&nbsp;L2&nbsp;+&nbsp;...&nbsp;+&nbsp;ValueN&nbsp;*&nbsp;LN</span></p></td></tr></tbody></table>

Here:

-   Value is the [market value of the position](/en/docs/mt5/manager/trading_advanced/margin_exchange#value). It is determined depending on the financial instrument type.
-   L — the liquidity rate of the instrument.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Only liquid instruments, i.e. those with the liquidity rate &gt;0, can be used as collateral.</span></p></td></tr></tbody></table>

### Liabilities [#](margin_exchange#liabilities)

Liabilities — obligations on current short positions calculated as the value of these positions at the current market price. In fact, the amount of liabilities is equivalent to the amount of money that the client would pay in case of immediate closure of short positions.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Liabilities&nbsp;=&nbsp;Value1&nbsp;&nbsp;+&nbsp;Value2&nbsp;+&nbsp;...&nbsp;+&nbsp;ValueN</span></p></td></tr></tbody></table>

Here Value is the [market value of the position](/en/docs/mt5/manager/trading_advanced/margin_exchange#value). It is determined depending on the financial instrument type.

### Balance (own funds)

Balance — the client's own funds on the account.

### Equity (portfolio value)

Equity is calculated by the following formula:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Equity&nbsp;=&nbsp;Own&nbsp;Funds&nbsp;+&nbsp;Assets&nbsp;-&nbsp;Liabilities&nbsp;-&nbsp;Commission</span></p></td></tr></tbody></table>

### Margin

-   Initial margin is the minimum value of trader's own funds with which the trader is allowed to enter the market.
-   Adjusted initial margin is the minimum value of own funds with which a trader is allowed to enter the market, including client's current market positions and limit orders .
-   Maintenance margin is the minimum amount of funds that must be available on the account for maintaining an open position. If the equity level falls below the maintenance margin, the broker starts closing trader's positions. The position closing procedure is determined by the broker's regulations.

### Determining the market value of a position [#](margin_exchange#value)

For instruments with the Exchange Stocks [calculation type](/en/docs/mt5/manager/market_watch#specification), the market value is determined as follows:

Volume in lots \* Contract size \* Open market price

For Exchange Bonds instruments, the position value is calculated using the following formula:

Volume in lots \* Contract size \* Face value \* Market Open price / 100 + AI

Here AI is the accrued interest.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The market value is calculated in symbol's base currency. If necessary, the resulting value can be converted to the account deposit currency.</span></p></td></tr></tbody></table>

## Calculation Features

On the spot market, as opposed to the futures and forward markets (where there is only the movement of collateral), payment and receipt of assets (or liabilities in the event of repurchase) occur immediately at the moment of deal conclusion. Accordingly, the transaction value is immediately reflected on the trader's balance.

Since the payment for the instrument purchase or sale is always made in full, the margin is only used as an indication of the trading account state, which determines the possibility of opening new positions or necessity to close out existing positions.

## Margin calculation for Exchange Stocks, Exchange Bonds, Exchange MOEX Stocks and Exchange MOEX Bonds

The margin is the discounted assessment of client's positions:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;=&nbsp;Value1&nbsp;*&nbsp;MarginRate1&nbsp;&nbsp;+&nbsp;Value2&nbsp;*&nbsp;MarginRate2&nbsp;+&nbsp;...&nbsp;+&nbsp;ValueN&nbsp;*&nbsp;MarginRateN</span></p></td></tr></tbody></table>

Here:

-   Value is the [market value of the position](/en/docs/mt5/manager/trading_advanced/margin_exchange#value). It is determined depending on the financial instrument type.
-   MarginRate is the rate of margin or discount of the instrument, for which a position is opened. Individual margin rates can be used for the initial and maintenance margin, as well as for short and long positions.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If margin rates of an instrument are equal to 0, such an instrument is considered to be non-marginable. For long positions, the charged margin is equal the value of such positions; short positions on non-margin instruments are not allowed.</span></p></td></tr></tbody></table>

![Discounts](/en/docs/mt5/manager/img/margin_discounts.png "Discounts")

### Example of Opening a Long Position

Assume initially the trader's balance is 1,000,000 RUR. The initial and maintenance margin rates are equal to 0.1 and 0.05. For simplicity, we do not take into account the commission size.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trade operations and price fluctuations</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trader's account state</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Buying 1000 shares of LKOH 150 RUR each</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: 1,000,000 RUR - 1000 * 150 RUR = 850,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: 1000 * 150 = 150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li><li class="p_fortable"><span class="f_fortable">Equity: 850,000 RUR + 150,000 RUR = 1,000,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: 15,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: 7,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price drop to 50 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: 850,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable" style="font-weight: bold;">1000 * 50 = 50,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">850,000 RUR + 50,000 RUR = 900,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">5,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">2,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Buying 20,000 shares 50 RUR each</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable" style="font-weight: bold;">850 000 RUR - 20 000 * 50 RUR = -150 000 RUR </span><span class="f_fortable">(uses borrowed money)</span></li><li class="p_fortable"><span class="f_fortable">Assets: (</span><span class="f_fortable" style="font-weight: bold;">1,000 + 20,000) * 50 RUR = 1,050,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,050,000 RUR - 150,000 RUR = 900,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">105,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">52,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price drop to 10 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">-150 000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable" style="font-weight: bold;">21,000 * 10 RUR = 210,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">210,000 RUR - 150,000 RUR = 60,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">21,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">10,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price drop to 7.8 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">-150 000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable" style="font-weight: bold;">21,000 * 7.8 RUR = 163,800 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">163,800 RUR - 150,000 RUR = 13,800 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">16,380 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">8,190 RUR</span></li></ul><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Note:</span><span class="f_fortable"> equity below the initial margin. A trader cannot open new positions, only close existing ones.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price drop to 5 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">-150 000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable" style="font-weight: bold;">21,000 * 5 RUR = 110,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">110,000 RUR - 150,000 RUR = -40,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">11,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">5,500 RUR</span></li></ul><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Note:</span><span class="f_fortable"> equity below the maintenance margin. Broker forcibly closes the trader's position.</span></p></td></tr></tbody></table>

### Example of Opening a Short Position

Assume initially the trader's balance is 1,000,000 RUR. The initial and maintenance margin rates are equal to 0.1 and 0.05. For simplicity, we do not take into account the commission size.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trade operations and price fluctuations</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trader's account state</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Selling 1000 shares of LKOH 150 RUR each</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: 1,000,000 RUR + 1,000 * 150 RUR = 1,150,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: -1,000 * 150 RUR = </span><span class="f_fortable">-150,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: 1,150,000 RUR - </span><span class="f_fortable">150,000 RUR = </span><span class="f_fortable">1,000,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Initial margin: 15,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: 7,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price grows to 300 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">1,150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: </span><span class="f_fortable" style="font-weight: bold;">-1000 * 300 RUR = -300,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,150,000 RUR - 300,000 RUR = 850,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">30,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">15,000 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price grows to 1000 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">1,150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: </span><span class="f_fortable" style="font-weight: bold;">-1000 * 1000 RUR = -1,000,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,150,000 RUR - 1,000,000 RUR = 150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">100,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">50,000 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price grows to 1100 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">1,150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: </span><span class="f_fortable" style="font-weight: bold;">-1000 * 1100 RUR = -1,100,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,150,000 RUR - 1,100,000 RUR = 50,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">110,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">55,000 RUR</span></li></ul><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Note:</span><span class="f_fortable"> equity below the initial margin. A trader cannot open new positions, only close existing ones.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price grows to 1200 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">1,150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: </span><span class="f_fortable" style="font-weight: bold;">-1000 * 1200 RUR = -1,200,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,150,000 RUR - 1,200,000 RUR = -50,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">120,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">60,000 RUR</span></li></ul><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Note:</span><span class="f_fortable"> equity below the maintenance margin. Broker forcibly closes the trader's position.</span></p></td></tr></tbody></table>

### Adjusted Initial Margin Calculation for Exchange Stocks and Exchange Bonds [#](margin_exchange#corrected)

If a trader has limit orders, then the following formula is used for calculating the initial margin when opening a position.

The adjusted margin is always calculated on the larger side — the aggregate amount of Buy or Sell positions and orders.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Corrected&nbsp;Margin&nbsp;=&nbsp;Max(Margin&nbsp;Buy;Margin&nbsp;Sell)</span></p></td></tr></tbody></table>

Long side calculation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;Buy&nbsp;=&nbsp;PositionSize&nbsp;*&nbsp;(PriceMarket&nbsp;-&nbsp;PriceMin)&nbsp;+&nbsp;(PositionSize&nbsp;+&nbsp;OrdersBuySize)&nbsp;*&nbsp;PriceMin&nbsp;*&nbsp;MarginRate&nbsp;+&nbsp;(OrdersBuyValue&nbsp;-&nbsp;OrdersBuySize&nbsp;*&nbsp;PriceMin)</span></p></td></tr></tbody></table>

Here:

-   PositionSize — position size calculated as the product of the volume in lots and the contract size.
-   PriceMarket — the current market price of the financial instrument (last deal price).
-   PriceMin — the minimum price among all current buy limit orders of the trader.
-   OrdersBuySize — the size of the trader's buy limit orders calculated as the product of the total volume of orders in lots and the contract size.
-   OrdersBuyValue — the value of the buy limit orders if they were executed at the prices specified in them. It is calculated as the sum of the products of order sizes and their limit price.
-   MarginRate — the amount of the symbol discount.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the trader's current position is short, and its size is greater than or equal to OrdersBuySize, Margin Buy is not calculated and is considered to be 0.</span><span class="f_ol"> In fact, this is a situation where even after the execution of all limit Buy orders, the trader will have a short position or the position will be completely eliminated.</span></p></td></tr></tbody></table>

Short side calculation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;Sell&nbsp;=&nbsp;-PositionSize&nbsp;*&nbsp;(PriceMax&nbsp;-&nbsp;PriceMarket)&nbsp;-&nbsp;(PositionSize&nbsp;-&nbsp;OrdersSellSize)&nbsp;*&nbsp;PriceMax&nbsp;*&nbsp;MarginRate&nbsp;+&nbsp;(OrdersSellSize&nbsp;*&nbsp;PriceMax&nbsp;-&nbsp;OrdersSellValue)</span></p></td></tr></tbody></table>

Here:

-   PositionSize — position size calculated as the product of the volume in lots and the contract size.
-   PriceMarket — the current market price of the financial instrument (last deal price).
-   PriceMax — the maximum price among all current sell limit orders of the trader.
-   OrdersSellSize — the size of the trader's sell limit orders calculated as the product of the total volume of orders in lots and the contract size.
-   OrdersSellValue — the value of the sell limit orders if they were executed at the prices specified in them. It is calculated as the sum of the products of order sizes and their limit price.
-   MarginRate — the amount of the symbol discount.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the trader's current position is long, and its size is greater than or equal to OrdersSellSize, Margin Buy is not calculated and is considered to be 0.</span><span class="f_ol"> In fact, this is a situation where even after the execution of all limit Sell orders, the trader will still have a long position or the position will be completely eliminated.</span></p></td></tr></tbody></table>

Consider the following example. The trader has:

-   Position Buy 1 lot LKOH, contract size is 1000 shares, the current price is 100 RUR, initial margin rate is 0.1
-   Order Buy Limit 0.5 lot LKOH (500 shares), order price is 80 RUR
-   Order Buy Limit 0.3 lot LKOH (300 shares), order price is 60 RUR
-   Order Buy Limit 0.1 lot LKOH (100 shares), order price is 40 RUR

Calculations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">PriceMin&nbsp;=&nbsp;40</span><br><span class="f_CodeExample">Price&nbsp;Market&nbsp;=&nbsp;100</span><br><span class="f_CodeExample">OrdersBuySize&nbsp;=&nbsp;500&nbsp;+&nbsp;300&nbsp;+&nbsp;100&nbsp;=&nbsp;900</span><br><span class="f_CodeExample">OrdersBuyValue&nbsp;=&nbsp;500&nbsp;*&nbsp;80&nbsp;+&nbsp;300&nbsp;*&nbsp;60&nbsp;+&nbsp;100&nbsp;*&nbsp;40&nbsp;=&nbsp;62&nbsp;000</span><br><span class="f_CodeExample">Margin&nbsp;Buy&nbsp;=&nbsp;1000&nbsp;*&nbsp;(100&nbsp;-&nbsp;40)&nbsp;+&nbsp;(1000&nbsp;+&nbsp;900)&nbsp;*&nbsp;40&nbsp;*&nbsp;0.1&nbsp;+&nbsp;(62&nbsp;000&nbsp;&nbsp;-&nbsp;900&nbsp;*&nbsp;40)&nbsp;=&nbsp;87&nbsp;900</span></p></td></tr></tbody></table>

The total amount of the adjusted initial margin is equal to 87,900.

### Adjusted initial margin calculation for Exchange MOEX Stocks and Exchange MOEX Bonds [#](margin_exchange#corrected_moex)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The Exchange MOEX Stocks and Exchange MOEX Bonds calculation modes are only used for the financial instruments which are traded on Moscow Exchange. The adjusted margin calculation rules applied in these modes are valid on Moscow Exchange since 01.07.2019.</span></p></td></tr></tbody></table>

If a client has limit orders, then the below formulas are used for calculating the initial margin when opening a position.

The adjusted margin is always calculated on the larger side, i.e. the aggregate amount of Buy or Sell positions and orders.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Corrected&nbsp;Margin&nbsp;=&nbsp;Max(Margin&nbsp;Buy;Margin&nbsp;Sell)</span></p></td></tr></tbody></table>

Long side calculation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;Buy&nbsp;=&nbsp;(PositionSize&nbsp;+&nbsp;OrdersBuySize)&nbsp;*&nbsp;PriceMarket&nbsp;*&nbsp;MarginRate</span></p></td></tr></tbody></table>

Here:

-   PositionSize — position size calculated as the product of the volume in lots and the contract size.
-   PriceMarket — the current market price of the financial instrument (last deal price).
-   OrdersBuySize — the size of the client's buy limit orders calculated as the product of the total volume of orders in lots and the contract size.
-   MarginRate — the amount of the symbol discount.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the current position of a client is short and its size is greater than or equal to OrdersBuySize, then Margin Buy is not calculated and is considered 0.</span><span class="f_ol"> This is because even if all the client's limit buy orders were executed, a short position would still remain after that or the position would be completely eliminated.</span></p></td></tr></tbody></table>

Short side calculation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;Sell&nbsp;=&nbsp;(-PositionSize&nbsp;+&nbsp;OrdersSellSize)&nbsp;*&nbsp;PriceMarket&nbsp;*&nbsp;MarginRate</span></p></td></tr></tbody></table>

Here:

-   PositionSize — position size calculated as the product of the volume in lots and the contract size.
-   PriceMarket — the current market price of the financial instrument (last deal price).
-   OrdersSellSize — the size of the client's sell limit orders calculated as the product of the total volume of orders in lots and the contract size.
-   MarginRate — the amount of the symbol discount.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the current position of a client is long and its size is greater than or equal to OrdersSellSize, then Margin Sell is not calculated and is considered 0.</span><span class="f_ol"> This is because even if all the client's limit sell orders were executed, a long position would still remain after that or the position would be completely eliminated.</span></p></td></tr></tbody></table>

Consider the following example. The client has:

-   Position Buy 1 lot LKOH, contract size is 1000 shares, the current price is 100 RUR, initial margin rate is 0.1
-   Order Buy Limit 0.5 lot LKOH (500 shares), order price is 80 RUR
-   Order Buy Limit 0.3 lot LKOH (300 shares), order price is 60 RUR
-   Order Buy Limit 0.1 lot LKOH (100 shares), order price is 40 RUR

Calculations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Price&nbsp;Market&nbsp;=&nbsp;100</span><br><span class="f_CodeExample">OrdersBuySize&nbsp;=&nbsp;500&nbsp;+&nbsp;300&nbsp;+&nbsp;100&nbsp;=&nbsp;900</span><br><span class="f_CodeExample">Margin&nbsp;Buy&nbsp;=&nbsp;(1000&nbsp;+&nbsp;900)&nbsp;*&nbsp;100&nbsp;*&nbsp;0.1&nbsp;=&nbsp;19,000</span></p></td></tr></tbody></table>

The total amount of the adjusted initial margin is equal to 19,000.

### Adjusted margin calculation for non-marginal instruments [#](margin_exchange#unmargined)

A financial instrument is considered non-marginal if [zero margins](/en/docs/mt5/manager/margin#margin_rate) are specified for this instrument. Thus, no margin is charged for the positions of such instruments, while the trader pays full collateral when opening such positions. Accordingly, the calculation of initial margin when a position for a non-marginal instrument is opened is actually involves the check of whether the trader has enough money to buy the asset (short positions for non-marginal instruments are usually prohibited).

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;Buy&nbsp;=&nbsp;OrderBuySize&nbsp;*&nbsp;PriceAsk</span><br><span class="f_CodeExample">Margin&nbsp;Sell&nbsp;=&nbsp;(-&nbsp;PositionSize&nbsp;+&nbsp;OrderSellSize)&nbsp;*&nbsp;PriceMarket</span></p></td></tr></tbody></table>

Here:

-   PositionSize — position size calculated as the product of the volume in lots and the contract size.
-   OrdersBuySize — the size of the client's buy limit orders calculated as the product of the total volume of orders in lots and the contract size.
-   OrdersSellSize — the size of the client's sell limit orders calculated as the product of the total volume of orders in lots and the contract size.
-   PriceMarket — the current market price of the financial instrument (last deal price).
-   PriceAsk — the current Ask price of the instrument.

Note that the current Ask (not Last) price is used in the long position margin calculation formula. Non-marginal instruments are usually low-liquid. Accordingly, deals with such instruments are rare and thus the last deal price may differ significantly from the current market price. Therefore, the current Ask price is used for the correct estimation of the asset value.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">This calculation is used for non-marginal instruments with type Exchange Stocks, Exchange Bonds, Exchange MOEX Stocks and Exchange MOEX Bonds.</span></p></td></tr></tbody></table>

## Margin calculation for other types of instruments

For all financial instruments except Exchange Stocks and Exchange Bonds, margin is calculated similar to [Retail Forex, CFD, Futures for netting](/en/docs/mt5/manager/trading_advanced/margin_forex). However, this calculated margin value is not recorded in a separate field of the account state, but increases the client's liabilities. The margin amount is actually blocked in the trader's account as collateral. Floating profit from positions is included in the account equity (and thus it affects the free margin amount).

Unlike the Retail mode, the exchange system does not take into account whether positions are [in spread](/en/docs/mt5/manager/trading_advanced/margin_forex#spread).

For example, there is an open position: Buy EURUSD 1.00 lot at 1.16135. Forex calculation type is used for the instrument, and its contract size is 100,000. The account deposit is USD, the leverage is 1:200.

-   Calculate the margin using the [Forex formula](/en/docs/mt5/manager/trading_advanced/margin_formula): 1 \* 100 000 / 200 = 500 EUR
-   Convert the margin from EUR to USD at the price as of the deal time: 500 \* 1.16135 = 580.68 USD

The resulting value is not recorded to the Margin field, but is written to the Trading Account Liabilities field instead.

[Margin Calculation: Retail Forex, CFD, Futures — Hedging](/en/docs/mt5/manager/trading_advanced/margin_forex_hedge)

[Spreads](/en/docs/mt5/manager/trading_advanced/spreads)