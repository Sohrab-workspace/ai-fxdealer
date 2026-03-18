# Accelerator Oscillator

> Source: https://support.metaquotes.net/en/docs/mt5/client/indicators/bw_indicators/ao

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
                -   [Volume Indicators](/en/docs/mt5/client/indicators/volume_indicators)
                -   [Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)
                    -   [Accelerator Oscillator](/en/docs/mt5/client/indicators/bw_indicators/ao)
                    -   [Alligator](/en/docs/mt5/client/indicators/bw_indicators/alligator)
                    -   [Awesome Oscillator](/en/docs/mt5/client/indicators/bw_indicators/awesome)
                    -   [Fractals](/en/docs/mt5/client/indicators/bw_indicators/fractals)
                    -   [Gator Oscillator](/en/docs/mt5/client/indicators/bw_indicators/go)
                    -   [Market Facilitation Index](/en/docs/mt5/client/indicators/bw_indicators/market_facilitation)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Technical Indicators](/en/docs/mt5/client/indicators)[Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)Accelerator Oscillator

# Accelerator Oscillator

Price is the latest element to change. Prior to price changes, the market driving force changes its direction, the driving force acceleration must slow down and reach nought. After that it starts accelerating in the opposite direction until price starts changing its direction.

Acceleration/Deceleration Technical Indicator (AC) measures acceleration and deceleration of the current driving force. This indicator will change direction before any changes in the driving force, which, it its turn, will change its direction before the price. If you realize that Acceleration/Deceleration is a signal of an earlier warning, it gives you evident advantages.

The nought line is basically the spot where the driving force is at balance with the acceleration. If Acceleration/Deceleration is higher than nought, then it is usually easier for the acceleration to continue the upward movement (and vice versa in cases when it is below nought). Unlike in case with [Awesome Oscillator](/en/docs/mt5/client/indicators/bw_indicators/awesome), it is not regarded as a signal when the nought line is crossed. The only thing that needs to be done to control the market and make decisions is to watch for changes in color. To save yourself serious reflections, you must remember: you can not buy with the help of Acceleration/Deceleration, when the current column is colored red, and you can not sell, when the current column is colored green.

If you enter the market in the direction of the driving force (the indicator is higher than nought, when buying, or it is lower than nought, when selling), then you need only two green columns to buy (two red columns to sell). If the driving force is directed against the position to be opened (indicator below nought for buying, or higher than nought for selling), a confirmation is needed, hence, an additional column is required. In this case the indicator is to show three red columns over the nought line for a short position and three green columns below the nought line for a long position.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><thead><tr class="attentable"><th class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can test the <a href="https://www.mql5.com/en/docs/standardlibrary/ExpertClasses/CSignal/signal_ac" target="_blank" class="weblink">trade signals</a> of this indicator by creating an Expert Advisor in <a href="https://www.metatrader5.com/en/automated-trading/mql5wizard" target="_blank" class="weblink">MQL5 Wizard</a>.</span></p></th></tr></thead></table>

![Accelerator Oscillator](/en/docs/mt5/client/img/ac.png "Accelerator Oscillator")

## Calculation

AC bar chart is the difference between the value of 5/34 of the driving force bar chart and 5-period simple moving average, taken from that bar chart.

MEDIAN PRICE = (HIGH + LOW) / 2

AO = SMA (MEDIAN PRICE, 5) - SMA (MEDIAN PRICE, 34)

AC = AO - SMA (AO, 5)

Where:

MEDIAN PRICE — median price;  
HIGH — the highest price of the bar;  
LOW — the lowest price of the bar;  
SMA — Simple Moving Average;  
AO — [Awesome Oscillator](/en/docs/mt5/client/indicators/bw_indicators/awesome).

[Bill Williams' Indicators](/en/docs/mt5/client/indicators/bw_indicators)

[Alligator](/en/docs/mt5/client/indicators/bw_indicators/alligator)