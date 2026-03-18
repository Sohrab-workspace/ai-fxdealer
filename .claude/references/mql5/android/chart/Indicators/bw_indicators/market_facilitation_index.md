# Market Facilitation Index

> Source: https://support.metaquotes.net/en/docs/mt5/android/chart/indicators/bw_indicators/market_facilitation_index

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
        -   [Getting Started](/en/docs/mt5/android/getting_started)
        -   [Quotes](/en/docs/mt5/android/quotes)
        -   [Depth of Market](/en/docs/mt5/android/depth_of_market)
        -   [Charts](/en/docs/mt5/android/chart)
            -   [Indicators](/en/docs/mt5/android/chart/indicators)
                -   [Trend Indicators](/en/docs/mt5/android/chart/indicators/trend_indicators)
                -   [Oscillators](/en/docs/mt5/android/chart/indicators/oscillators)
                -   [Volume Indicators](/en/docs/mt5/android/chart/indicators/volume_indicators)
                -   [Bill Williams' Indicators](/en/docs/mt5/android/chart/indicators/bw_indicators)
                    -   [Accelerator Oscillator](/en/docs/mt5/android/chart/indicators/bw_indicators/accelerator_oscillator)
                    -   [Alligator](/en/docs/mt5/android/chart/indicators/bw_indicators/alligator)
                    -   [Awesome Oscillator](/en/docs/mt5/android/chart/indicators/bw_indicators/awesome_oscillator)
                    -   [Fractals](/en/docs/mt5/android/chart/indicators/bw_indicators/fractals)
                    -   [Gator Oscillator](/en/docs/mt5/android/chart/indicators/bw_indicators/gator_oscillator)
                    -   [Market Facilitation Index](/en/docs/mt5/android/chart/indicators/bw_indicators/market_facilitation_index)
            -   [Objects](/en/docs/mt5/android/chart/objects)
        -   [Trade](/en/docs/mt5/android/trade)
        -   [History](/en/docs/mt5/android/history)
        -   [Accounts](/en/docs/mt5/android/settings_accounts)
        -   [Mailbox](/en/docs/mt5/android/settings_mail)
        -   [News Event](/en/docs/mt5/android/settings_news)
        -   [Messages](/en/docs/mt5/android/messages)
        -   [Settings](/en/docs/mt5/android/settings)
        -   [Journal](/en/docs/mt5/android/settings_journal)
        -   [About](/en/docs/mt5/android/settings_about)
        -   [Push Notifications](/en/docs/mt5/android/push)
        -   [Tablet Version](/en/docs/mt5/android/tablet)
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

[MetaTrader 5](/en/docs/mt5)[Android](/en/docs/mt5/android)[Charts](/en/docs/mt5/android/chart)[Indicators](/en/docs/mt5/android/chart/indicators)[Bill Williams' Indicators](/en/docs/mt5/android/chart/indicators/bw_indicators)Market Facilitation Index

# Market Facilitation Index

Market Facilitation Index Technical Indicator (BW MFI) is the indicator which shows the change of price for one tick. Absolute values of the indicator do not mean anything as they are, only indicator changes have sense. Bill Williams emphasizes the interchanging of MFI and volume:

-   Market Facilitation Index increases and volume increases — this points out that: a) the number of players coming into the market increases (volume increases) b) the new coming players open positions in the direction of bar development, i.e., the movement has begun and picks up speed.
-   Market Facilitation Index falls and volume falls. It means the market participants are not interested anymore.
-   Market Facilitation Index increases, but the volume falls. It is most likely, that the market is not supported with the volume from traders, and the price is changing due to speculations of the floor traders (broker agents and dealers).
-   Market Facilitation Index falls, but the volume increases. There is a battle between bulls and bears, characterized by a large sell and buy volume, but the price is not changing significantly since the forces are equal. One of the contending parties (buyers vs. sellers) will eventually win the battle. Usually, the break of such a bar lets you know if this bar determines the continuation of the trend or annuls the trend. Bill Williams calls such bar "curtsying".

![Market Facilitation Index](/en/docs/mt5/android/img/market_facilitation_index.png "Market Facilitation Index")

## Calculation

To calculate Market Facilitation Index you need to subtract the low price of a bar from the its high price and divide it by the volume.

BW MFI = (HIGH - LOW) / VOLUME

Where:

HIGH — the high price of the current bar;  
LOW — the low price of the current bar;  
VOLUME — the volume of the current bar.

[Gator Oscillator](/en/docs/mt5/android/chart/indicators/bw_indicators/gator_oscillator)

[Objects](/en/docs/mt5/android/chart/objects)