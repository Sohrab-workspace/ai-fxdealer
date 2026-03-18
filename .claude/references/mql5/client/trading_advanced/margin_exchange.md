# Exchange Risk Management Model

> Source: https://support.metaquotes.net/en/docs/mt5/client/trading_advanced/margin_exchange

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
            -   [Basic Principles](/en/docs/mt5/client/general_concept)
            -   [Depth of Market](/en/docs/mt5/client/depth_of_market)
            -   [Market Watch](/en/docs/mt5/client/market_watch)
            -   [Options Board](/en/docs/mt5/client/options_board)
            -   [Executing Trades](/en/docs/mt5/client/performing_deals)
            -   [One Click Trading](/en/docs/mt5/client/one_click_trading)
            -   [Trading Report](/en/docs/mt5/client/report)
            -   [For Advanced Users](/en/docs/mt5/client/trading_advanced)
                -   [Price Data](/en/docs/mt5/client/trading_advanced/price_data)
                -   [Margin Calculation: Retail Forex, Futures](/en/docs/mt5/client/trading_advanced/margin_forex)
                -   [Margin Calculation: Exchange Model](/en/docs/mt5/client/trading_advanced/margin_exchange)
                -   [Collateral Symbols](/en/docs/mt5/client/trading_advanced/collateral)
                -   [Custom Financial Instruments](/en/docs/mt5/client/trading_advanced/custom_instruments)
                -   [Spreads](/en/docs/mt5/client/trading_advanced/spreads)
                -   [Futures](/en/docs/mt5/client/trading_advanced/futures)
                -   [Trading Report](/en/docs/mt5/client/trading_advanced/history_report)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Trading Operations](/en/docs/mt5/client/trading)[For Advanced Users](/en/docs/mt5/client/trading_advanced)Margin Calculation: Exchange Model

# Exchange Risk Management Model

The trading platform provides different risk management models, which define the type of pre-trade control. At the moment, the following models are used:

-   [For Retail Forex, Futures](/en/docs/mt5/client/trading_advanced/margin_forex) — used for the OTC market. Margin calculation is based on the type of instrument.
-   [For Stock Exchange, based on margin discount rates](/en/docs/mt5/client/trading_advanced/margin_exchange) — used for the exchange market. Margin calculation is based on the discounts for instruments. Discounts are set by the broker, however they cannot be lower than the exchange set values.

## Basic Terminology

### Exposure [#](margin_exchange#assets)

Assets — the current value of purchased financial instruments (of long positions) defined in a trader's deposit currency. The value is determined dynamically based on the price of the latest deal of the financial instrument, taking into account the liquidity margin rate. In fact, the amount of assets is equivalent to the amount of money that the trader would receive in case of immediate closure of long positions.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Assets&nbsp;=&nbsp;Size1&nbsp;*&nbsp;Price1&nbsp;*&nbsp;L1&nbsp;&nbsp;+&nbsp;Size2&nbsp;*&nbsp;Price2&nbsp;*&nbsp;L2&nbsp;+&nbsp;...&nbsp;+SizeN&nbsp;*&nbsp;PriceN&nbsp;*&nbsp;LN</span></p></td></tr></tbody></table>

Where:

-   Size — the size of the Nth position calculated as the product of the volume in lots and the contract size.
-   Price — the current market price of the financial instrument.
-   L — the liquidity rate of the instrument.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Only liquid instruments can be used as collateral.</span></p></td></tr></tbody></table>

### Liabilities [#](margin_exchange#liabilities)

Liabilities are obligations on current short positions calculated as the value of these positions at the current market price. In fact, the amount of liabilities is equivalent to the amount of money that the trader would pay in case of immediate closure of short positions.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Liabilities&nbsp;=&nbsp;Size1&nbsp;*&nbsp;Price1&nbsp;&nbsp;+&nbsp;Size2&nbsp;*&nbsp;Price2&nbsp;+&nbsp;...&nbsp;+SizeN&nbsp;*&nbsp;PriceN</span></p></td></tr></tbody></table>

Where:

-   Size — the size of the Nth position calculated as the product of the volume in lots and the contract size.
-   Price — the current price of the instrument of the trader's open Nth position.

### Balance (own funds)

Balance — the trader's own funds on the account.

### Equity (portfolio value)

Equity is calculated by the following formula:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Equity&nbsp;=&nbsp;Own&nbsp;Funds&nbsp;+&nbsp;Assets&nbsp;-&nbsp;Liabilities&nbsp;-&nbsp;Commission</span></p></td></tr></tbody></table>

### Margin

-   Initial margin is the minimum value of trader's own funds with which the trader is allowed to enter the market.
-   Adjusted initial margin is the minimum value of trader's own funds with which the trader is allowed to enter the market, including current market positions and limit orders.
-   Maintenance margin is the minimum amount of funds that must be available on the account for maintaining an open position. If the equity level falls below the maintenance margin, the broker starts closing trader's positions. The position closing procedure is determined by the broker's regulations.

## Calculation Features

On the spot market, as opposed to the futures and forward markets (characterized by margin movement), payment and receipt of assets (or liabilities in the event of repurchase) occur immediately at the moment of deal conclusion. Accordingly, the transaction value is immediately reflected on the trader's balance.

Since the payment for the instrument purchase or sale is always made in full, the margin is only used as an indication of the trading account state, which determines the possibility of opening new positions or necessity to close out existing positions.

## Margin Calculation

The margin is the capitalized assessment of trader's positions:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;=&nbsp;Size1&nbsp;*&nbsp;Price1&nbsp;*&nbsp;MarginRate1&nbsp;&nbsp;+&nbsp;Size2&nbsp;*&nbsp;Price2&nbsp;*&nbsp;MarginRate2&nbsp;+&nbsp;...&nbsp;+&nbsp;SizeN&nbsp;*&nbsp;PriceN&nbsp;*&nbsp;MarginRateN</span></p></td></tr></tbody></table>

Where:

-   Size — the size of the Nth position calculated as the product of the volume in lots and the contract size.
-   Price — the current price of the instrument of the trader's open Nth position.
-   MarginRate — the rate of margin or discount of the instrument, for which a position is opened. Individual margin rates can be used for the initial and maintenance margin, as well as for short and long positions.

![Discounts](/en/docs/mt5/client/img/margin_discounts.png "Discounts")

### Example of Opening a Long Position

For example, the trader's initial balance is 1,000,000 RUR. The initial and maintenance margin rates are equal to 0.1 and 0.05. For simplicity, we do not take into account the commission size.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trade operations and price fluctuations</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trader's account state</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Buying 1000 shares of LKOH 150 RUR each</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: 1,000,000 RUR - 1000 * 150 RUR = 850,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: 1000 * 150 = 150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li><li class="p_fortable"><span class="f_fortable">Equity: 850,000 RUR + 150,000 RUR = 1,000,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: 15,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: 7,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price drop to 50 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: 850,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable" style="font-weight: bold;">1000 * 50 = 50,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">850,000 RUR + 50,000 RUR = 900,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">5,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">2,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Buying 20,000 shares 50 RUR each</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable" style="font-weight: bold;">850 000 RUR - 20 000 * 50 RUR = -150 000 RUR </span><span class="f_fortable">(uses borrowed money)</span></li><li class="p_fortable"><span class="f_fortable">Assets: (</span><span class="f_fortable" style="font-weight: bold;">1,000 + 20,000) * 50 RUR = 1,050,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,050,000 RUR - 150,000 RUR = 900,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">105,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">52,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price drop to 10 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">-150 000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable" style="font-weight: bold;">21,000 * 10 RUR = 210,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">210,000 RUR - 150,000 RUR = 60,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">21,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">10,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price drop to 7.8 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">-150 000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable" style="font-weight: bold;">21,000 * 7.8 RUR = 163,800 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">163,800 RUR - 150,000 RUR = 13,800 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">16,380 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">8,190 RUR</span></li></ul><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Note:</span><span class="f_fortable"> equity below the initial margin. A trader cannot open new positions, only close existing ones.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price drop to 5 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">-150 000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable" style="font-weight: bold;">21,000 * 5 RUR = 110,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: 0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">110,000 RUR - 150,000 RUR = -40,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">11 000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">5 500 RUR</span></li></ul><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Note:</span><span class="f_fortable"> equity below the maintenance margin. Broker forcibly closes the trader's position.</span></p></td></tr></tbody></table>

### Example of Opening a Short Position

For example, the trader's initial balance is 1,000,000 RUR. The initial and maintenance margin rates are equal to 0.1 and 0.05. For simplicity, we do not take into account the commission size.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trade operations and price fluctuations</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trader's account state</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Selling 1000 shares of LKOH 150 RUR each</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: 1,000,000 RUR + 1,000 * 150 RUR = 1,150,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: -1,000 * 150 RUR = </span><span class="f_fortable">-150,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: 1,150,000 RUR - </span><span class="f_fortable">150,000 RUR = </span><span class="f_fortable">1,000,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Initial margin: 15,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: 7,500 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price grows to 300 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">1,150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: </span><span class="f_fortable" style="font-weight: bold;">-1000 * 300 RUR = -300,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,150,000 RUR - 300,000 RUR = 850,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">30,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">15,000 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price grows to 1000 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">1,150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: </span><span class="f_fortable" style="font-weight: bold;">-1000 * 1000 RUR = -1,000,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,150,000 RUR - 1,000,000 RUR = 150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">100,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">50,000 RUR</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price grows to 1100 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">1,150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: </span><span class="f_fortable" style="font-weight: bold;">-1000 * 1100 RUR = -1,100,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,150,000 RUR - 1,100,000 RUR = 50,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">110,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">55,000 RUR</span></li></ul><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Note:</span><span class="f_fortable"> equity below the initial margin. A trader cannot open new positions, only close existing ones.</span></p></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Price grows to 1200 RUR per share</span></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Balance: </span><span class="f_fortable">1,150,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Assets: </span><span class="f_fortable">0 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Liabilities: </span><span class="f_fortable" style="font-weight: bold;">-1000 * 1200 RUR = -1,200,000 RUR</span></li></ul><ul><li class="p_fortable"><span class="f_fortable">Equity: </span><span class="f_fortable" style="font-weight: bold;">1,150,000 RUR - 1,200,000 RUR = -50,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Initial margin: </span><span class="f_fortable" style="font-weight: bold;">120,000 RUR</span></li><li class="p_fortable"><span class="f_fortable">Maintenance margin: </span><span class="f_fortable" style="font-weight: bold;">60,000 RUR</span></li></ul><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Note:</span><span class="f_fortable"> equity below the maintenance margin. Broker forcibly closes the trader's position.</span></p></td></tr></tbody></table>

### Adjusted Initial Margin Calculation

If a trader has limit orders, then the following formula is used for calculating the initial margin when opening a position.

The adjusted margin is always calculated on the larger side — the aggregate amount of Buy or Sell positions and orders.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Corrected&nbsp;Margin&nbsp;=&nbsp;Max(Margin&nbsp;Buy;Margin&nbsp;Sell)</span></p></td></tr></tbody></table>

Long side calculation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;Buy&nbsp;=&nbsp;PositionSize&nbsp;*&nbsp;(PriceMarket&nbsp;-&nbsp;PriceMin)&nbsp;+&nbsp;(PositionSize&nbsp;+&nbsp;OrdersBuySize)&nbsp;*&nbsp;PriceMin&nbsp;*&nbsp;MarginRate&nbsp;+&nbsp;(OrdersBuyValue&nbsp;-&nbsp;OrdersBuySize&nbsp;*&nbsp;PriceMin)</span></p></td></tr></tbody></table>

Where:

-   PositionSize — position size calculated as the product of the volume in lots and the contract size.
-   PriceMarket — the current market price of the financial instrument (last deal price).
-   PriceMin — the minimum price among all current buy limit orders of the trader.
-   OrdersBuySize — the size of the trader's buy limit orders calculated as the product of the total volume of orders in lots and the contract size.
-   OrdersBuyValue — the value of the buy limit orders if they were executed at the prices specified in them. It is calculated as the sum of the products of order sizes and their limit price.
-   MarginRate — the amount of the symbol discount.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the trader's current position is short, and its size is greater than or equal to OrdersBuySize, then Margin Buy is not calculated and is assumed to be 0.</span><span class="f_ol"> In fact, this is a situation where, even if all the trader's buy limit orders are filled, the trader will still have a short position or the position will be completely eliminated.</span></p></td></tr></tbody></table>

Short side calculation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Margin&nbsp;Sell&nbsp;=&nbsp;-PositionSize&nbsp;*&nbsp;(PriceMax&nbsp;-&nbsp;PriceMarket)&nbsp;-&nbsp;(PositionSize&nbsp;-&nbsp;OrdersSellSize)&nbsp;*&nbsp;PriceMax&nbsp;*&nbsp;MarginRate&nbsp;+&nbsp;(OrdersSellSize&nbsp;*&nbsp;PriceMax&nbsp;-&nbsp;OrdersSellValue)</span></p></td></tr></tbody></table>

Where:

-   PositionSize — position size calculated as the product of the volume in lots and the contract size.
-   PriceMarket — the current market price of the financial instrument (last deal price).
-   PriceMax — the maximum price among all current sell limit orders of the trader.
-   OrdersSellSize — the size of the trader's sell limit orders calculated as the product of the total volume of orders in lots and the contract size.
-   OrdersSellValue — the value of the sell limit orders if they were executed at the prices specified in them. It is calculated as the sum of the products of order sizes and their limit price.
-   MarginRate — the amount of the symbol discount.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the trader's current position is long, and its size is greater than or equal to OrdersSellSize, then Margin Sell is not calculated and is assumed to be 0.</span><span class="f_ol"> In fact, this is a situation where, even if all the trader's sell limit orders are filled, the trader will still have a long position or the position will be completely eliminated.</span></p></td></tr></tbody></table>

Let's consider the following example. The trader has:

-   Position Buy 1 lot LKOH, contract size is 1000 shares, the current price is 100 RUR, initial margin rate is 0.1
-   Order Buy Limit 0.5 lot LKOH (500 shares), order price is 80 RUR
-   Order Buy Limit 0.3 lot LKOH (300 shares), order price is 60 RUR
-   Order Buy Limit 0.1 lot LKOH (100 shares), order price is 40 RUR

Calculation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">PriceMin&nbsp;=&nbsp;40</span><br><span class="f_CodeExample">Price&nbsp;Market&nbsp;=&nbsp;100</span><br><span class="f_CodeExample">OrdersBuySize&nbsp;=&nbsp;500&nbsp;+&nbsp;300&nbsp;+&nbsp;100&nbsp;=&nbsp;900</span><br><span class="f_CodeExample">OrdersBuyValue&nbsp;=&nbsp;500&nbsp;*&nbsp;80&nbsp;+&nbsp;300&nbsp;*&nbsp;60&nbsp;+&nbsp;100&nbsp;*&nbsp;40&nbsp;=&nbsp;62&nbsp;000</span><br><span class="f_CodeExample">Margin&nbsp;Buy&nbsp;=&nbsp;1000&nbsp;*&nbsp;(100&nbsp;-&nbsp;40)&nbsp;+&nbsp;(1000&nbsp;+&nbsp;900)&nbsp;*&nbsp;40&nbsp;*&nbsp;0.1&nbsp;+&nbsp;(62&nbsp;000&nbsp;&nbsp;-&nbsp;900&nbsp;*&nbsp;40)&nbsp;=&nbsp;87&nbsp;900</span></p></td></tr></tbody></table>

The total amount of the adjusted initial margin is equal to 87,900.

[Margin Calculation: Retail Forex, Futures](/en/docs/mt5/client/trading_advanced/margin_forex)

[Collateral Symbols](/en/docs/mt5/client/trading_advanced/collateral)