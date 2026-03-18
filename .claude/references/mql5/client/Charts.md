# View and Configure Charts

> Source: https://support.metaquotes.net/en/docs/mt5/client/charts

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)View and Configure Charts

# View and Configure Charts

Charts in the trading platform visualize changes of financial symbol quotes over time. Charts are used for technical analysis and operation of Expert Advisors. They allow traders to visually monitor the prices of currencies and shares in real time and instantly respond to any changes in the market situation.

In the trading platform, you can open up to 100 charts at a time, customize their appearance and displayed information, apply and remove various [objects](/en/docs/mt5/client/objects) and [indicators](/en/docs/mt5/client/indicators), and much more.

## Chart: How to Open, View, Set Timeframe and Scale [#](charts#operations)

![Chart: how to open, view, set timeframe and scale](/en/docs/mt5/client/img/chart_operations.png)

### Chart opening

You can quickly open a chart by selecting a financial symbol in the Market Watch window and clicking on the "Chart Window" item of the context menu. You can also open a chart by dragging a symbol from the Market Watch window to any area of the trading platform.

Another way is to execute the "New Chart" command from the File menu or click the appropriate button on the toolbar.

### Chart types: broken line, bars and candlesticks

Price charts can be presented as a sequence of bars, Japanese candlesticks, and as a broken line. You can switch between presentation types using commands on the toolbar.

The figure shows the three price types.

The chart type can be changed using the Charts menu, the context menu of the chart or from the [chart properties](/en/docs/mt5/client/charts_advanced/charts_settings).

### Changing the chart timeframe

A timeframe is a time interval of quotes on the chart of a financial instrument. This is the time of one bar or candlestick. There are 21 chart timeframes from one minute to one month available in the trading platform.

The timeframe is selected depending on the trends studied. As a rule, the timeframes from M1 to M15 are used for short-term scalping. Mid-term timeframes are from M30 to H4, they are usually used for intraday trading. Higher timeframes allow you to analyze longer-term trends.

You can switch between the timeframes using a special toolbar "Timeframes".

A timeframe can also be changed using the "Charts" menu and the context menu of a chart.

### Chart zoom

To zoom the chart in or out, use buttons on the toolbar.

Chart scale can be changed by rolling the mouse wheel while holding down Ctrl.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">A chart can be opened by dragging an instrument from the Market Watch window. If the instrument is dragged to the window of an open chart, the new symbol is opened in the same window while the previous one is deleted from it. In this case all settings of the previous chart are applied to the new one. If you hold down Ctrl while dragging a financial instrument, the new chart is opened in a separate window using the DEFAULT.TPL <a href="/en/docs/mt5/client/charts#template" class="topiclink">template</a>, which is created during platform installation process. This template cannot be deleted, but it can be changed.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">To quickly find a desired chart among multiple open charts, select the appropriate symbol in the Market Watch, an order or position in the Trade or History section, or an alert. The chart frame of the appropriate symbol will blink three times.</span></li></ul></td></tr></tbody></table>

## How to Change the Color of the Chart [#](charts#color)

The chart appearance is highly customizable: you can hide or show any element, as well as change its color. For convenience, three color schemes of charts are available in the platform. In the [chart properties](/en/docs/mt5/client/charts_advanced/charts_settings), you can select a color scheme or set up colors of individual elements of the chart:

![Changing the chart color](/en/docs/mt5/client/img/char_color.png "Changing the chart color")

To open chart properties, click "![Properties](/en/docs/mt5/client/img/chart_properties_icon.png "Properties") Properties" in the context menu or the [Charts](/en/docs/mt5/client/interface) menu.

## How to Arrange Charts [#](charts#arrange)

If multiple charts are open in your trading platform, you can easily organize them. Use the [Window](/en/docs/mt5/client/interface) menu and select one of the available chart arrangement types:

![Arrangement of charts](/en/docs/mt5/client/img/chart_arrange.png "Arrangement of charts")

## What are the Templates and Profiles [#](charts#template)

Templates and profiles allow saving settings of charts and easily apply them when necessary. For example, to analyze a currency pair you have added horizontal lines to mark up the levels. Save a separate chart template in order to preserve the levels. In this case, you can always restore the levels on a new chart by applying the template.

Templates are used for saving parameters of an individual chart: chart type and color, color scheme, scale, running Expert Advisors, applied indicators and analytical objects, as well as other settings.

In profiles you can save the settings and arrangement of all open charts, that is of the entire workspace for technical analysis.

You can conveniently work with profiles and templates using the toolbar:

![Chart templates and profiles](/en/docs/mt5/client/img/chart_template.png "Chart templates and profiles")

They can also be accessed using the [Charts](/en/docs/mt5/client/interface) menu, the context menu of the chart and the [status bar](/en/docs/mt5/client/interface) of the platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">See <a href="/en/docs/mt5/client/charts_advanced/templates_profiles" class="topiclink">Templates and Profiles</a> for further details.</span></p></td></tr></tbody></table>

## How to View Precise Values on the Chart [#](charts#datawindow)

You can view the precise price, time or [indicator](/en/docs/mt5/client/indicators) values using the Crosshair and the Data Window.

Turn on the crosshair on the "Line Studies" toolbar, and the exact values of a chart point will be shown on the price and time scales. More details about the current cursor position on the chart are available in the Data Window: date and time, bar parameters, volumes, spread (minimum value on a selected bar), as well as indicator values.

![Viewing precise values on the chart](/en/docs/mt5/client/img/chart_precise_values.png "Viewing precise values on the chart")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any indicator can be configured (<a href="/en/docs/mt5/client/indicators#visualization" class="topiclink">Visualization</a> tab in the indicator properties window) so that its values are displayed in this window.</span></p></td></tr></tbody></table>

## Working with Charts on Multiple Monitors [#](charts#docked)

The trading platform allows detaching financial symbol charts from the main terminal working area. This feature is convenient when using multiple monitors. Thus, you may set the main platform window on one monitor to control your account state, and move your charts to the second screen to observe the market situation. To detach a chart from the terminal, disable the "![Docked](/en/docs/mt5/client/img/docked_icon.png "Docked")Docked" option in its context menu. After that move the chart to the desired monitor.

![Undocking a chart from the main platform window](/en/docs/mt5/client/img/chart_docked.png "Undocking a chart from the main platform window")

A separate toolbar on detached charts allows applying [analytical objects](/en/docs/mt5/client/objects) and [indicators](/en/docs/mt5/client/indicators) without having to switch between monitors. Use the toolbar context menu to manage the set of available commands or to hide it.

## Chart Construction Features [#](charts#notes)

The history data, based on which charts are constructed, are stored on the hard disk. When you open a chart, the data are loaded from the disk, and the last missing data are downloaded from the trading server. If there are no history data for the symbol on the hard disk, the latest 512 bars of history are downloaded.

To download earlier data, move the chart to the desired area. Once a chart is opened, the platform starts receiving information about the current quotes. Thus, further price changes are shown in the real-time mode. This information is automatically saved in the history file and used later when you reopen this chart.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">In the <a href="/en/docs/mt5/client/settings#max_bars" class="topiclink">platform settings</a>, you can set up the "Max. bars on chart" parameter. This parameter allows you to control the amount of history data displayed on the chart.</span></li><li class="p_tableatten"><span class="f_tableatten">Bid prices are used for constructing charts. If the <a href="/en/docs/mt5/client/depth_of_market" class="topiclink">depth of market</a> is available for a symbol, its chart is based on the Last prices (the price of the last executed trade).</span></li></ul></td></tr></tbody></table>

[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)

[Publish Online](/en/docs/mt5/client/mql5_charts)