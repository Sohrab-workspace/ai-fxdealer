# Williams’ Percent Range

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/oscillators/wpr

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Oscillators](/en/docs/mt5/client/indicators/oscillators)Williams' Percent Range

# Williams’ Percent Range

Williams’ Percent Range Technical Indicator (%R) is a dynamic technical indicator, which determines whether the market is overbought/oversold. Williams’ %R is very similar to the [Stochastic Oscillator](/en/docs/mt5/client/indicators/oscillators/so). The only difference is that %R has an upside down scale and the Stochastic Oscillator has internal smoothing.

Indicator values ranging between -80% and -100% indicate that the market is oversold. Indicator values ranging between -0% and -20% indicate that the market is overbought. To show the indicator in this upside down fashion, one places a minus symbol before the Williams' Percent Range values (for example -30%). One should ignore the minus symbol when conducting the analysis.

As with all overbought/oversold indicators, it is best to wait for the symbol price to change direction before placing your trades. For example, if an overbought/oversold indicator is showing an overbought condition, it is wise to wait for the security’s price to turn down before selling the security.

An interesting phenomenon of the Williams' Percent Range indicator is its uncanny ability to anticipate a reversal in the underlying security’s price. The indicator almost always forms a peak and turns down a few days before the security’s price peaks and turns down. Likewise, Williams Percent Range usually creates a trough and turns up a few days before the security’s price turns up.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_wpr" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Williams' Percent Range](/en/docs/mt5/client/img/wpr.png "Williams' Percent Range")

## Calculation

Below is the formula of the %R indicator calculation, which is very similar to the [Stochastic Oscillator](/en/docs/mt5/client/indicators/oscillators/so) formula:

%R = -(MAX (HIGH (i - n)) - CLOSE (i)) / (MAX (HIGH (i - n)) - MIN (LOW (i - n))) \* 100

Where:

CLOSE (i) — today's closing price;  
MAX (HIGH (i - n)) — the highest maximum over a number (n) of previous periods;  
MIN (LOW (i - n)) — the lowest minimum over a number (n) of previous periods.

[Triple Exponential Average](/en/docs/mt5/client/indicators/oscillators/tea)

[Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)