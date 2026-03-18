# Average Directional Movement Index Wilder

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/trend_indicators/admiw

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Trend Indicators](/en/docs/mt5/client/indicators/trend_indicators)Average Directional Movement Index Wilder

# Average Directional Movement Index Wilder

Average Directional Movement Index Wilder (ADX Wilder) helps to determine if there is a price trend. This technical indicator is constructed as a strict correspondence with the algorithm described by Welles Wilder in his book "New concepts in technical trading systems".

Trading rules of this indicator are described in the section ["Average Directional Movement Index"](/en/docs/mt5/client/indicators/trend_indicators/admi).

![Average Directional Movement Index Wilder](/en/docs/mt5/client/img/admiw.png "Average Directional Movement Index Wilder")

## Calculation

First positive (dm\_plus) and negative (dm\_minus) changes at each bar are calculated, as well as the true range tr:

If High(i) - High(i-1) > 0  dm\_plus(i) = High\[(i) - High(i-1), otherwise dm\_plus(i) = 0.  
If Low(i-1) - Low(i) > 0  dm\_minus(i) = Low(i-1) - Low(i), otherwise dm\_minus(i) = 0.

tr(i) = Max(ABS(High(i) - High(i-1)), ABS(High(i) - Close(i-1)), ABS(Low(i) - Close(i-1)))

Where:

High(i) — maximal price of the current bar;  
Low(i) — minimal price of the current bar;  
High(i-1) — maximal price of the previous bar;  
Low(i-1) — minimal price of the previous bar;  
Close(i-1)  — close price of the previous bar;  
Max (a, b , c) — maximal value out of three numbers: a, b and c;  
ABS(X)  — value of the number X absolute in its module.

After that smoothed values are calculated: Plus\_D(i), Minus\_D(i) and ATR():

ATR(i) = SMMA(tr, Period\_ADX,i)

Plus\_D(i) = SMMA(dm\_plus, Period\_ADX,i)/ATR(i)\*100

Minus\_D(i) = SMMA(dm\_minus, Period\_ADX,i)/ATR(i)\*100

Where:

SMMA(X, N, i) — [Smoothed Moving Average](/en/docs/mt5/client/indicators/trend_indicators/ma#smma) by values of X series on the current bar;  
Period\_ADX — number of periods used for calculation.

Now Directional Movement Index - DX(i) - is calculated:

DX(i) = ABS(Plus\_D(i) - Minus\_D(i))/(Plus\_D(i) + Minus\_D(i)) \* 100

After preliminary calculations we obtain the value of the ADX(i) indicator on the current bar by smoothing DX index values:

ADX(i) = SMMA(DX, Period\_ADX, i)

[Average Directional Movement Index](/en/docs/mt5/client/indicators/trend_indicators/admi)

[Bollinger Bands](/en/docs/mt5/client/indicators/trend_indicators/bb)