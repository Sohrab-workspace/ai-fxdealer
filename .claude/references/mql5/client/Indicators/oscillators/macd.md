# MACD

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/oscillators/macd

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
            -   [View and Configure Charts](/en/docs/mt5/client/charts)
            -   [Publish Online](/en/docs/mt5/client/mql5_charts)
            -   [Technical Indicators](/en/docs/mt5/client/indicators)
                -   [Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)
                -   [Oscillators](/en/docs/mt5/client/indicators/oscillators)
                    -   [Average True Range](/en/docs/mt5/client/indicators/oscillators/atr)
                    -   [Bears Power](/en/docs/mt5/client/indicators/oscillators/bears)
                    -   [Bulls Power](/en/docs/mt5/client/indicators/oscillators/bulls)
                    -   [Chaikin Oscillator](/en/docs/mt5/client/indicators/oscillators/chaikin)
                    -   [Commodity Channel Index](/en/docs/mt5/client/indicators/oscillators/cci)
                    -   [DeMarker](/en/docs/mt5/client/indicators/oscillators/demarker)
                    -   [Force Index](/en/docs/mt5/client/indicators/oscillators/fi)
                    -   [MACD](/en/docs/mt5/client/indicators/oscillators/macd)
                    -   [Momentum](/en/docs/mt5/client/indicators/oscillators/momentum)
                    -   [Moving Average of Oscillator](/en/docs/mt5/client/indicators/oscillators/mao)
                    -   [Relative Strength Index](/en/docs/mt5/client/indicators/oscillators/rsi)
                    -   [Relative Vigor Index](/en/docs/mt5/client/indicators/oscillators/rvi)
                    -   [Stochastic Oscillator](/en/docs/mt5/client/indicators/oscillators/so)
                    -   [Triple Exponential Average](/en/docs/mt5/client/indicators/oscillators/tea)
                    -   [Williams' Percent Range](/en/docs/mt5/client/indicators/oscillators/wpr)
                -   [Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)
                -   [Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)
            -   [Analytical Objects](/en/docs/mt5/client/objects)
            -   [Fundamental Analysis](/en/docs/mt5/client/fundamental)
            -   [Additional Technical Indicators](/en/docs/mt5/client/charts_analysis_get_indicators)
            -   [Additional Features](/en/docs/mt5/client/charts_advanced)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Oscillators](/en/docs/mt5/client/indicators/oscillators)MACD

# MACD

Moving Average Convergence/Divergence (MACD) is a trend-following dynamic indicator. It indicates the correlation between two [Moving Averages](/en/docs/mt5/client/indicators/trend_indicators/ma) of a price.

The Moving Average Convergence/Divergence (MACD) Technical Indicator is the difference between a 26-period and 12-period [Exponential moving averages (EMA)](/en/docs/mt5/client/indicators/trend_indicators/ma#ema). In order to clearly show buy/sell opportunities, a so-called signal line (9-period moving average of the indicator) is plotted on the MACD chart.

The MACD proves most effective in wide-swinging trading markets. There are three popular ways to use the Moving Average Convergence/Divergence: crossovers, overbought/oversold conditions, and divergences.

## Crossovers

The basic MACD trading rule is to sell when the MACD falls below its signal line. Similarly, a buy signal occurs when the Moving Average Convergence/Divergence rises above its signal line. It is also popular to buy/sell when the MACD goes above/below zero.

## Overbought/Oversold Conditions

The MACD is also useful as an overbought/oversold indicator. When the shorter moving average pulls away dramatically from the longer moving average (i.e., the MACD rises), it is likely that the symbol price is overextending and will soon return to more realistic levels.

## Divergence

An indication that an end to the current trend may be near occurs when the MACD diverges from the symbol. A bullish divergence occurs when the Moving Average Convergence/Divergence indicator is making new highs while prices fail to reach new highs. A bearish divergence occurs when the MACD is making new lows while prices fail to reach new lows. Both of these divergences are most significant when they occur at relatively overbought/oversold levels.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_macd" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Moving Average Convergence/Divergence](/en/docs/mt5/client/img/macd.png "Moving Average Convergence/Divergence")

## Calculation

The MACD is calculated by subtracting the value of a 26-period exponential moving average from a 12-period exponential moving average. A 9-period dotted simple moving average of the MACD (the signal line) is then plotted on top of the MACD.

MACD = EMA(CLOSE, 12) - EMA(CLOSE, 26)

SIGNAL = SMA(MACD, 9)

Where:

EMA — Exponential Moving Average;  
SMA — Simple Moving Average;  
SIGNAL — the signal line of the indicator.

[Force Index](/en/docs/mt5/client/indicators/oscillators/fi)

[Momentum](/en/docs/mt5/client/indicators/oscillators/momentum)