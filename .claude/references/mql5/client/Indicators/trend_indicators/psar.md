# Parabolic SAR

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/psar

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
                    -   [Adaptive Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ama)
                    -   [Average Directional Movement Index](/en/docs/mt5/client/indicators/trend_indicators/admi)
                    -   [Average Directional Movement Index Wilder](/en/docs/mt5/client/indicators/trend_indicators/admiw)
                    -   [Bollinger Bands](/en/docs/mt5/client/indicators/trend_indicators/bb)
                    -   [Double Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/dema)
                    -   [Envelopes](/en/docs/mt5/client/indicators/trend_indicators/envelopes)
                    -   [Fractal Adaptive Moving Average](/en/docs/mt5/client/indicators/trend_indicators/fama)
                    -   [Ichimoku Kinko Hyo](/en/docs/mt5/client/indicators/trend_indicators/ikh)
                    -   [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma)
                    -   [Parabolic SAR](/en/docs/mt5/client/indicators/trend_indicators/psar)
                    -   [Standard Deviation](/en/docs/mt5/client/indicators/trend_indicators/sd)
                    -   [Triple Exponential Moving Average](/en/docs/mt5/client/indicators/trend_indicators/tema)
                    -   [Variable Index Dynamic Average](/en/docs/mt5/client/indicators/trend_indicators/vida)
                -   [Oscillators](/en/docs/mt5/client/indicators/oscillators)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Parabolic SAR

# Parabolic SAR

Parabolic SAR Technical Indicator was developed for analyzing the trending markets. The indicator is constructed on the price chart. This indicator is similar to [Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma) with the only difference that Parabolic SAR moves with higher acceleration and may change its position in terms of the price. The indicator is below the prices on the bull market (Up Trend), when the market is bearish (Down Trend), it is above the prices.

If the price crosses Parabolic SAR lines, the indicator turns, and its further values are situated on the other side of the price. When such an indicator turn does take place, the maximum or the minimum price for the previous period would serve as the starting point. When the indicator makes a turn, it gives a signal of the trend end (correction stage or flat), or of its turn.

The Parabolic SAR is an outstanding indicator for providing exit points. Long positions should be closed when the price sinks below the SAR line, short positions should be closed when the price rises above the SAR line. It means one should trace the movement of Parabolic SAR and hold open positions only in the direction of this movement. It is often the case that the indicator serves as a trailing stop line.

If the long position is open (i.e., the price is above the SAR line), the Parabolic SAR line will go up, regardless of what direction the prices take. The length of the SAR line movement depends on the scale of the price movement.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_sar" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Parabolic SAR](/en/docs/mt5/client/img/parabolic_sar.png "Parabolic SAR")

## Calculation

For long positions:

SAR (i) = SAR (i - 1) + ACCELERATION \* (HIGH (i - 1) - SAR (i - 1))

For short positions:

SAR (i) = SAR (i - 1) + ACCELERATION \* (LOW (i - 1) - SAR (i - 1))

Where:

SAR (i - 1) — value of Parabolic SAR on the previous bar;  
ACCELERATION — acceleration factor;  
HIGH (i - 1) — maximal price for the previous period;  
LOW (i - 1) — minimal price for the previous period.

The indicator value increases if the price of the current bar is higher than previous bullish and vice versa. The acceleration factor (ACCELERATION) will double at the same time, which would cause Parabolic SAR and the price to come together. In other words, the faster the price grows or sinks, the faster the indicator approaches the price.

[Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma)

[Standard Deviation](/en/docs/mt5/client/indicators/trend_indicators/sd)