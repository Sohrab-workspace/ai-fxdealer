# Futures

> Source: https://support.metaquotes.net/en/docs/mt5/client/trading_advanced/futures

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Trading Operations](/en/docs/mt5/client/trading)[For Advanced Users](/en/docs/mt5/client/trading_advanced)Futures

# Futures

Futures is a derivative product. It is a financial contract between two parties obligating one party to deliver a commodity or a financial instrument at a predetermined future date, and the other party to pay a predetermined price for it at a future point. Commodity or a financial asset that is the subject of the contract is called an underlying asset.

The futures contracts do not always aim at buying or selling an asset. In most cases, market participants make a consistent purchase and sale (or vice versa) of futures to profit from the price difference. In this case, the contracts are detached from the transaction subject becoming independent financial instruments.

The name of the underlying asset and delivery date are indicated in the futures name in the [trading symbol properties](/en/docs/mt5/client/market_watch#specification):

![Underlying asset and delivery date](/en/docs/mt5/client/img/futures_underlying.png "Underlying asset and delivery date")

Here you can see Gazprom equity futures contract with the delivery date set to March 2015.

Futures contracts' underlying asset delivery dates are standardized on the stock market. For example, contracts with delivery in the second, third and fourth quarters of the year may be offered during the first quarter, while contracts with delivery in the third and fourth quarters of the current year and the first quarter of the next year may be offered during the second quarter of the current year.

The exchange provides data on settlement prices of the contracts with different delivery dates, volumes of performed transactions and number of open positions on a daily basis. To review these data, select the required instrument in Market Watch and go to the [Details](/en/docs/mt5/client/market_watch#details) tab.

![Detailed contract data](/en/docs/mt5/client/img/futures_details.png "Detailed contract data")

## Contract Settlements

Unlike a spot market where assets are traded for immediate delivery and payment, on the futures market all final settlements are made only on the underlying asset delivery day. Until then, if the contract price goes up, a buyer may sell it and receive profit from the price difference (the same works for short positions).

In order to protect against a default on the contract, the exchange defines the amount of funds that should be present on the trader's account. These funds are called performance bond or margin. There are two types of margin:

-   Initial — the funds necessary to open a position (enter the market).
-   Maintenance — the funds that should be maintained on the account as long as the position is open.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For more information about margin calculations, please read the <a href="/en/docs/mt5/client/trading_advanced/margin_forex#futures" class="topiclink">appropriate description</a>.</span></p></td></tr></tbody></table>

Following the results of each trading day, the exchange determines the calculation (clearing) price during the clearing session. This price is then used to close all open positions. According to the difference between the position open price and close (clearing) price, profit/loss obtained in the last trading day is deposited to/withdrawn from the trader's balance. That process is called variation margin charging. Variation margin charge transactions are displayed in the History tab. They have "variation margin close" comment.

![Charging variation margin](/en/docs/mt5/client/img/futures_variation.png "Charging variation margin")

After variation margin is charged, positions are re-opened. Now, their open price corresponds to the clearing price of the previous session. Position re-open transactions have "variation margin open" comment.

[Spreads](/en/docs/mt5/client/trading_advanced/spreads)

[Trading Report](/en/docs/mt5/client/trading_advanced/history_report)