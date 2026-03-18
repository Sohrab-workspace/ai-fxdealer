# Charts

> Source: https://support.metaquotes.net/en/docs/mt5/iphone/settings/settings_charts

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
        -   [Getting Started](/en/docs/mt5/iphone/getting_started)
        -   [Quotes](/en/docs/mt5/iphone/quotes)
        -   [Depth of Market](/en/docs/mt5/iphone/depth_of_market)
        -   [Chart](/en/docs/mt5/iphone/chart)
        -   [Trade](/en/docs/mt5/iphone/trade)
        -   [History](/en/docs/mt5/iphone/history)
        -   [Accounts](/en/docs/mt5/iphone/settings_accounts)
        -   [Mailbox](/en/docs/mt5/iphone/settings_mail)
        -   [News](/en/docs/mt5/iphone/settings_news)
        -   [Messages](/en/docs/mt5/iphone/settings_messages)
        -   [Push Notifications](/en/docs/mt5/iphone/push)
        -   [Settings](/en/docs/mt5/iphone/settings)
            -   [Charts](/en/docs/mt5/iphone/settings/settings_charts)
            -   [Journal](/en/docs/mt5/iphone/settings/settings_journal)
            -   [Settings](/en/docs/mt5/iphone/settings/settings_about)
            -   [Certificates](/en/docs/mt5/iphone/settings/settings_certificates)
        -   [iPad Version](/en/docs/mt5/iphone/ipad)
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

[MetaTrader 5](/en/docs/mt5)[iPhone/iPad](/en/docs/mt5/iphone)[Settings](/en/docs/mt5/iphone/settings)Charts

# Charts

In this section you can control [chart](/en/docs/mt5/iphone/chart) settings. To go to this section, run the "![Charts](/en/docs/mt5/iphone/img/charts_icon.png "Charts") Charts" command in the [platform settings](/en/docs/mt5/iphone/settings).

![Chart Settings](/en/docs/mt5/iphone/img/chart_settings.png "Chart Settings")

The following parameters are available:

-   Bar Chart — show the chart as a sequence of bars.
-   Candlesticks — show the chart as a sequence of candlesticks.
-   Line Chart — show the chart as a line.
-   Volume — show/hide real volumes on the chart. The availability of this information varies by broker. Typically, data on real volumes is only provided for exchange instruments or on ECN accounts.
-   Tick Volumes — show/hide tick volumes on the chart.
-   Ask Price Line — show/hide the Ask price level of the latest quote. Bars in the platform are formed based on Bid prices (or Last prices if the [depth of market](/en/docs/mt5/iphone/depth_of_market) is available for the instrument). However, at opening of long positions and closing of the short ones, the Ask price is always used. The Ask price is not displayed on the chart, so it cannot be seen. To have a more precise control over trading, enable the "Ask price line" parameter. An additional horizontal line corresponding to the Ask price of the latest quote appears on the chart.
-   Period Separators — date and time of each bar are displayed on the horizontal axis of the chart. And this horizontal scale interval is the selected timeframe. The "Period Separators" option draws additional vertical lines corresponding to the larger period (timeframe) borders. Daily separators are drawn for M1 to H1 charts, weekly separators are shown for H4, monthly appear for D1 and year separators are used for W1 and MN1 charts.

-   Countdown to bar close — [countdown timer](/en/docs/mt5/iphone/chart#countdown) that displays the remaining time until the current bar closes.

-   Trade positions — show current symbol's open [positions](/en/docs/mt5/iphone/trade#position) on the [chart](/en/docs/mt5/iphone/chart). Operations are displayed as lines with captions at the level of the price, at which they were executed.

-   Trade orders — show current symbol's [pending orders](/en/docs/mt5/iphone/trade#orders) on the chart. Works similarly to the previous option.
-   SL/TP levels — show Stop Loss and Take profit levels for the current symbol's positions and pending orders on the chart. Works similarly to the previous option.
-   Trade History — show/hide on the chart entries and exits for the appropriate instrument. Deals are marked on charts with icons ![Buy Setup](/en/docs/mt5/iphone/img/buy_icon.png "Buy Setup") (a Buy deal) and ![Sell Setup](/en/docs/mt5/iphone/img/sell_icon.png "Sell Setup") (a Sell deal). In trading it is important to evaluate the correctness of market entry and exit moments. This can be conveniently done through the graphical representation of executed deals on the symbol's price chart.

-   Preload Chart Data — in order to save traffic, the trading platform downloads symbol price history only when the relevant data is requested, for example when a [price chart is opened](/en/docs/mt5/iphone/chart). However, this may not always be convenient for actively used symbols. If you enable this option, the charts of the symbols for which you have open positions or pending orders, will always be updated in the background mode. Thus, you will not have to wait for data to be downloaded after chart opening, and the relevant data will be immediately available for analysis. Chart data can only be preloaded if there is a Wi-Fi connections.
-   OHLC — when this option is enabled, current Open, High, Low and Close prices are displayed at the top of the chart. Therefore, the exact value of the last bar can always be seen.
-   Data Window — when this option is enabled in ["Crosshair" mode](/en/docs/mt5/iphone/chart#crosshair) [the data window](/en/docs/mt5/iphone/chart#data_window) will additionally be displayed on a chart. The Data Window displays the values of all active indicators in a specified point of a chart.
-   One-Click Trading — the trading platform allows performing trade operations in one click without additional confirmation by trader (trading dialog is not displayed). The function is available for the [depth of market](/en/docs/mt5/iphone/depth_of_market) and the [special chart panel](/en/docs/mt5/iphone/chart#one_click). Special terms and conditions should be accepted to use this option.
-   Trading Panel at the Bottom — the [One Click trading panel](/en/docs/mt5/iphone/chart#one_click) appears at the chart top by default. This option positions the panel at the bottom.
-   Colors — select the color display of the chart and its various elements:

-   Scheme — select a pre-defined color scheme of the chart. There are two color schemes: "Green on Black" and "Black on White".
-   Foreground — color of the axes, scale and OHLC line.
-   Grid — grid color.
-   Bar up — color of an up bar, its shadow and border of a bullish candlestick's body.
-   Bar down — color of down bar, its shadow and border of bearish candlestick's body.
-   Bull candle — color of bullish candlestick's body.
-   Bear candle — color of bearish candlestick's body.
-   Line chart — color of the chart line and Doji candlesticks.
-   Volumes — color of volumes and position opening levels.
-   Bid price line — color of the Bid price line.
-   Ask price line — color of the Ask price line.
-   Trade levels — color of levels displaying current positions and pending orders.
-   Stop levels — color of [stop order](/en/docs/mt5/iphone/trade/general_concept/order_types) (Stop Loss and Take Profit) levels.

[Settings](/en/docs/mt5/iphone/settings)

[Journal](/en/docs/mt5/iphone/settings/settings_journal)