# Custom Financial Instruments

> Source: https://support.metaquotes.net/en/docs/mt5/client/trading_advanced/custom_instruments

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Trading Operations](/en/docs/mt5/client/trading)[For Advanced Users](/en/docs/mt5/client/trading_advanced)Custom Financial Instruments

# Custom Financial Instruments

The trading platform allows creating custom financial symbols. You can view [charts](/en/docs/mt5/client/charts) of such symbols and perform [technical analysis](/en/docs/mt5/client/indicators), as well as use them for testing trading robots and indicators in the [Strategy Tester](/en/docs/mt5/client/testing).

If your broker does not provide the instrument, on which you want to test your strategy, or the provided history depth and the quality of price history is not enough, you can create a custom symbol and upload required data to it.

## How to Create and Configure a Custom Symbol

Open the symbol management window using the context menu of the ["Market Watch"](/en/docs/mt5/client/market_watch) window and click on "Create Custom Symbol":

![Creating a custom financial instrument](/en/docs/mt5/client/img/custom_symbol_create.png "Creating a custom financial instrument")

For a custom symbol, you can configure some parameters from the [specification of trading instruments](/en/docs/mt5/client/market_watch#specification), as well as some additional parameters:

-   Basis — the name of the underlying asset for the custom symbol. For example, gold is the underlying asset for futures contracts.
-   Page — the web page containing symbol information. It will be displayed as a link when viewing symbol properties in the Market Watch window.
-   Chart mode — the price used for creating the symbol chart, Bid or Last.
-   Background — the background color for the symbol in the Market Watch window.
-   Calculate hedged margin using larger leg — this mode is only used on [hedging](/en/docs/mt5/client/general_concept#hedging) accounts, where opposite positions of the same symbol can exist simultaneously. Symbol margin can be calculated using the margin of a short side (all sell positions and pending orders) and of a long side (all buy positions and sending orders). The largest one of the calculated values is used as the final margin value.
-   Time limits use — by setting "Yes", you can specify the first and the last day of the symbol trading period (circulation period).

In addition to the above parameters, you can configure trading and quoting sessions for the symbol. Sessions are configured separately for each day. Double-click on a day to edit it.

![Trading and Quoting Sessions of a Custom Symbol](/en/docs/mt5/client/img/custom_symbol_sessions.png "Trading and Quoting Sessions of a Custom Symbol")

Set the desired sessions using sliders. Expert Advisors will not be able to trade in the Strategy Tester in non-session hours.

Trading sessions are not specified by default, and coincide with quoting sessions. If you need to configure the time of quoting and trading sessions separately, enable the option "Enable separate trading sessions". Each trading session must be within a quoting session.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">You can quickly configure your custom symbol by copying parameters of any similar instrument and modifying them. Select an existing symbol in the "Copy from" field.</span></li><li class="p_tableatten"><span class="f_tableatten">The name of the custom symbol must not match the names of symbols provided by the brokers. If you connect to the server, on which a symbol with the same name exists, the custom symbol will be deleted.</span></li><li class="p_tableatten"><span class="f_tableatten">The symbol name may only contain Latin letters without punctuation, spaces or special characters (may only contain ".", "_", "&amp;" and "#"). It is not recommended to use characters &lt;, &gt;, :, ", /, |, ?, *.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The minute and tick history of the custom financial instrument is automatically deleted when the following parameters in the symbol <a href="/en/docs/mt5/client/market_watch#specification" class="topiclink">specifications</a> are changed: the formula (for <a href="/en/docs/mt5/client/trading_advanced/custom_instruments#synthetic" class="topiclink">synthetic symbols</a>), the tick size and value, the charting mode, the point value and accuracy. When the above parameters are changed from MQL5 programs, price data is also deleted. Be careful and properly configure all the symbol parameters before <a href="/en/docs/mt5/client/trading_advanced/custom_instruments#import_history" class="topiclink">importing history</a>.</span></li></ul></td></tr></tbody></table>

## Import and Export of Custom Symbols [#](custom_instruments#export)

You can easily share custom symbols or transfer symbols between your platforms. Parameters of a specific custom symbol can be exported or imported from its settings editing window shown above.

It is also possible to export and import entire groups of symbols:

![Exporting and Importing Settings of a Group of Custom Symbols](/en/docs/mt5/client/img/custom_symbol_group_export.png "Exporting and Importing Settings of a Group of Custom Symbols")

Settings are exported to JSON text files:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">{</span><br><span class="f_CodeExample">"ConfigSymbols"&nbsp;:&nbsp;[</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">"Symbol"&nbsp;:&nbsp;"EURUSD_cust",</span><br><span class="f_CodeExample">"Path"&nbsp;:&nbsp;"Custom\\Forex\\EURUSD_cust",</span><br><span class="f_CodeExample">"ISIN"&nbsp;:&nbsp;"",</span><br><span class="f_CodeExample">"Description"&nbsp;:&nbsp;"Euro&nbsp;vs&nbsp;US&nbsp;Dollar",</span><br><span class="f_CodeExample">....</span></p></td></tr></tbody></table>

## Managing Custom Symbols [#](custom_instruments#manage)

All symbols are displayed in a separate Custom group. If you need to modify or delete a symbol, use the context menu of the list:

![Creating, Editing and Deleting Custom Symbols](/en/docs/mt5/client/img/custom_symbol_manage.png "Creating, Editing and Deleting Custom Symbols")

## Importing the Price History [#](custom_instruments#import_history)

You can import price data to your custom symbol from any text file, as well as from MetaTrader history files (HST). Choose a symbol and go to the "Bars" or "Ticks" tab.

![Importing the Price History to a Custom Symbol](/en/docs/mt5/client/img/custom_symbol_import.gif "Importing the Price History to a Custom Symbol")

In the import dialog, specify the path to the file and set the required parameters:

-   Separator — separator of items in a text file.
-   Skip columns and rows — amount of columns (from left to right) and rows (from top to bottom) to be skipped during an import.
-   Shift — time shift by hours. The option is used when importing data saved in a different time zone.
-   Use selected only — import only rows highlighted in the row view area. You can highlight rows with your mouse while holding Ctrl or Shift.

A file with 1-minute bars should have the following format: Date Time Open High Low Close TickVolume Volume Spread. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;DATE&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;TIME&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;OPEN&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;HIGH&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;LOW&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;CLOSE&gt;&nbsp;&lt;TICKVOL&gt;&lt;VOL&gt;&nbsp;&nbsp;&nbsp;&nbsp;&lt;SPREAD&gt;</span><br><span class="f_CodeExample">2016.06.27&nbsp;&nbsp;&nbsp;&nbsp;00:01:00&nbsp;&nbsp;&nbsp;&nbsp;1.10024&nbsp;&nbsp;&nbsp;&nbsp;1.10136&nbsp;&nbsp;&nbsp;&nbsp;1.10024&nbsp;&nbsp;&nbsp;&nbsp;1.10070&nbsp;&nbsp;&nbsp;&nbsp;18&nbsp;&nbsp;&nbsp;&nbsp;54000000&nbsp;&nbsp;&nbsp;&nbsp;44</span><br><span class="f_CodeExample">2016.06.27&nbsp;&nbsp;&nbsp;&nbsp;00:02:00&nbsp;&nbsp;&nbsp;&nbsp;1.10070&nbsp;&nbsp;&nbsp;&nbsp;1.10165&nbsp;&nbsp;&nbsp;&nbsp;1.10070&nbsp;&nbsp;&nbsp;&nbsp;1.10165&nbsp;&nbsp;&nbsp;&nbsp;32&nbsp;&nbsp;&nbsp;&nbsp;55575000&nbsp;&nbsp;&nbsp;&nbsp;46</span><br><span class="f_CodeExample">2016.06.27&nbsp;&nbsp;&nbsp;&nbsp;00:03:00&nbsp;&nbsp;&nbsp;&nbsp;1.10166&nbsp;&nbsp;&nbsp;&nbsp;1.10166&nbsp;&nbsp;&nbsp;&nbsp;1.10136&nbsp;&nbsp;&nbsp;&nbsp;1.10163&nbsp;&nbsp;&nbsp;&nbsp;13&nbsp;&nbsp;&nbsp;&nbsp;13000000&nbsp;&nbsp;&nbsp;&nbsp;46</span><br><span class="f_CodeExample">2016.06.27&nbsp;&nbsp;&nbsp;&nbsp;00:04:00&nbsp;&nbsp;&nbsp;&nbsp;1.10163&nbsp;&nbsp;&nbsp;&nbsp;1.10204&nbsp;&nbsp;&nbsp;&nbsp;1.10155&nbsp;&nbsp;&nbsp;&nbsp;1.10160&nbsp;&nbsp;&nbsp;&nbsp;23&nbsp;&nbsp;&nbsp;&nbsp;51000000&nbsp;&nbsp;&nbsp;&nbsp;41</span></p></td></tr></tbody></table>

A file with ticks should have the following format: Date Time Bid Ask Last Volume. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&lt;DATE&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;TIME&gt;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;BID&gt;&nbsp;&nbsp;&nbsp;&lt;ASK&gt;&nbsp;&nbsp;&nbsp;&lt;LAST&gt;&nbsp;&nbsp;&lt;VOLUME&gt;</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:03:47.212&nbsp;&nbsp;&nbsp;&nbsp;1.14175&nbsp;1.14210&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:03:47.212&nbsp;&nbsp;&nbsp;&nbsp;1.14168&nbsp;1.14206&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:03:47.717&nbsp;&nbsp;&nbsp;&nbsp;1.14175&nbsp;1.14206&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:03:54.241&nbsp;&nbsp;&nbsp;&nbsp;1.14175&nbsp;1.14205&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:03:57.982&nbsp;&nbsp;&nbsp;&nbsp;1.14165&nbsp;1.14201&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:04:07.795&nbsp;&nbsp;&nbsp;&nbsp;1.14175&nbsp;1.14201&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:04:55.432&nbsp;&nbsp;&nbsp;&nbsp;1.14164&nbsp;1.14200&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:14:33.743&nbsp;&nbsp;&nbsp;&nbsp;1.14173&nbsp;1.14203&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:14:33.743&nbsp;&nbsp;&nbsp;&nbsp;1.14173&nbsp;1.14201&nbsp;0.00000&nbsp;0</span><br><span class="f_CodeExample">2017.07.03&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;00:16:44.901&nbsp;&nbsp;&nbsp;&nbsp;1.14174&nbsp;1.14195&nbsp;0.00000&nbsp;0</span></p></td></tr></tbody></table>

Do not pass [tick flags](/en/docs/mt5/client/market_watch#history), as the terminal calculates them during import.

You can use data from any existing instrument for your custom symbol. [Export](/en/docs/mt5/client/market_watch#history) data, modify it if necessary, and import the data back.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The price history is stored in the form of one-minute bars. All other timeframes are created based on these bars. You can also import data of higher timeframes, but charts on lower timeframes will have gaps in this case. For example, if you import one-hour data, one bar per hour will be shown on the M1 chart.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">During import, the time interval is completely replaced by data from the specified file. For example, if the file contains data from 2016.01.01 00:00:00 to 2016.06.01 00:00:00, and the custom symbol history already has some data in this interval, these data will be completely replaced with new ones (even if the amount of imported data is less than data in the history).</span></li><li class="p_tableatten"><span class="f_tableatten">When importing bars, the presence of duplicate entries in the imported file (bars with the same time) is considered to be an error. In the platform, only one bar can correspond to one minute. When importing ticks, several ticks can have fully identical parameters.</span></li><li class="p_tableatten"><span class="f_tableatten">Values set to less than or equal to zero are not imported.</span></li><li class="p_tableatten"><span class="f_tableatten">During import, the user must provide the correct order of ticks in the file, i.e. from earlier ticks to more recent ones.</span></li></ul></td></tr></tbody></table>

Price data of custom symbols are saved in a separate Custom directory (not in the directories where data of trade servers are stored):

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">C:\Users\[windows&nbsp;account]\AppData\Roaming\MetaQuotes\Terminal\[instance&nbsp;id]\bases\Custom</span></p></td></tr></tbody></table>

## Editing the Price History [#](custom_instruments#edit_history)

You can edit the history of bars and ticks of custom symbols manually. To do this, request the required data interval in the "Bars" or "Ticks" tab.

-   Double-tap to change the value.
-   Use the context menu to add or delete entries
-   If you need to delete multiple bars/ticks at once, select them with the mouse, holding down Shift or Ctrl+Shift.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When editing bars, it is highly recommended to request data of the M1 timeframe. The price history is stored in the form of one-minute bars in the platform. All other timeframes are created based on these bars. Even if you initially request bars of another timeframe, all changes will be applied to the corresponding 1-minute bars. For example, if you request data of the M5 timeframe and edit a bar, five 1-minute bars will be replaced by one 1-minute bar (corresponding to the beginning of the M5 bar). It means that the edited interval will be completely replaced.</span></p></td></tr></tbody></table>

![Manual editing of 1-minute bars and tick data](/en/docs/mt5/client/img/custom_symbol_edit_history.gif "Manual editing of 1-minute bars and tick data")

For convenience, modified entries are highlighted as follows:

-   Red background means that the entry is incorrect (for example, the high price is less than the low price)
-   Green background indicates a correct modified entry
-   Gray background means a deleted entry
-   Yellow background shows an added entry

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When adding a new bar, the first unoccupied date/time from the current data selection is automatically inserted in the "Date" column.</span></li><li class="p_tableatten"><span class="f_tableatten">The platform does not allow creating bars with the same date/time. Only one bar can correspond to one minute.</span></li></ul></td></tr></tbody></table>

To save the changes, click "Apply Changes" at the bottom of the window.

## Use of Custom Financial Instruments

Use of custom symbols is similar to the use of instruments provided by the broker. Custom symbols are displayed in the [Market Watch window](/en/docs/mt5/client/market_watch); you can open charts of such symbols and apply indicators and analytical objects on them.

![A custom symbol price chart with technical indicators](/en/docs/mt5/client/img/custom_symbol_chart.png "A custom symbol price chart with technical indicators")

## Testing Using Custom Financial Instruments

Real trades cannot be executed on custom symbols, but they can be used for testing trading robots and indicators in the [Strategy Tester](/en/docs/mt5/client/testing). Select a custom symbol and launch testing:

![Testing a Trading Robot on a Custom Symbol](/en/docs/mt5/client/img/custom_symbol_testing.png "Testing a Trading Robot on a Custom Symbol")

When calculating the margin and profit of trades executed during testing, the Strategy Tester can automatically use cross rates available on the account. For example, if the profit currency is EUR and the account currency is USD, the tester will convert it according to the corresponding EURUSD rates.

Most often, custom symbol names include various suffixes, such as EURUSD.1 or EURUSD.f. Therefore, the strategy tester uses a special mechanism to search for suitable cross rates for recalculation.

For example, we have created a custom symbol AUDCAD.custom with the margin calculation type [Forex](/en/docs/mt5/client/trading_advanced/margin_forex), and the currency of our account is USD. Based on the name of the Forex instrument, the tester searches for the required symbols in the following order:

1.  First, the tester searches for symbols such as AUDUSD.custom (for margin calculation) and USDCAD.custom (for profit calculation).
2.  If any of these symbols is not found, the tester searches for the first symbol, whose name corresponds to the required currency pairs, i.e. AUDUSD and USDCAD. If it finds for example AUDUSD.b and USDCAD.b, the rates of these symbols will be used for margin and profit calculation.

For financial instruments with other [margin calculation types](/en/docs/mt5/client/trading_advanced/margin_forex) (Futures, Stock Exchange), a currency pair is needed for converting the instrument currency into deposit currency. For example, we have created a custom symbol with the British pound (GBP) set for the profit and margin currency, and the Swiss franc (CHF) used as the deposit currency. In this case, symbols for testing are searched in the following order:

1.  The availability of a trading instrument corresponding to GBPCHF (GBP vs CHF) is checked.
2.  If this symbol is not available, the tester will search for the first trading instrument corresponding to the GBPCHF currency pair, such as GBPCHF.b or GBPCHF.def.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When testing applications using custom instruments, make sure that the account has all the necessary currency pairs. Otherwise, the calculation of financial results and margin requirements during testing will not be possible.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The use of <a href="/en/docs/mt5/client/strategy_optimization#cloud" class="topiclink">MQL5 Cloud Network</a> for optimization using custom symbols is not allowed. This is due to the fact that custom symbols with the same names, but different price histories can exist on computers of different traders. In addition to the discrepancy of test results between network agents, this may cause mass reloading and synchronization of history data, which leads to excessive internet usage. Using <a href="/en/docs/mt5/client/strategy_optimization#farm" class="topiclink">local network agents</a> and <a href="/en/docs/mt5/client/metatester" class="topiclink">remote agents</a> is allowed.</span></li></ul></td></tr></tbody></table>

## Synthetic Symbols with Real-Time Quotes [#](custom_instruments#synthetic)

The trading platform allows creating synthetic financial instruments, i.e. symbols based on one or more existing instruments. The user should set the formula for calculating quotes, after which the platform will generate ticks of the synthetic instrument in real time, and also will create its minute history.

### How It Works

-   You create a synthetic instrument and set formula for price calculation.
-   The platform calculates ticks at a frequency of 10 times per second, provided that the price of at least one of the instruments used in the formula has changed.
-   The platform also calculates the history of 1-minute bars based on 1-minute bars of instruments used in its formula. All new bars (current and subsequent ones) will be drawn in real time based on the generated ticks of the synthetic instrument.

For example, you can create an instrument showing the [dollar index (USDX)](https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D0%B4%D0%B5%D0%BA%D1%81_%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0). It uses the below formula:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_CodeExample"><span class="f_CodeExample">50.14348112*</span><span class="f_CodeExample" style="color: #0000ff;">pow</span><span class="f_CodeExample">(ask(EURUSD),-0.576)*</span><span class="f_CodeExample" style="color: #0000ff;">pow</span><span class="f_CodeExample">(USDJPY,0.136)*</span><span class="f_CodeExample" style="color: #0000ff;">pow</span><span class="f_CodeExample">(ask(GBPUSD),-0.119)*</span><span class="f_CodeExample" style="color: #0000ff;">pow</span><span class="f_CodeExample">(USDCAD,0.091)*</span><span class="f_CodeExample" style="color: #0000ff;">pow</span><span class="f_CodeExample">(USDSEK,0.042)*</span><span class="f_CodeExample" style="color: #0000ff;">pow</span><span class="f_CodeExample">(USDCHF,0.036)</span></p></th></tr></thead></table>

The platform will calculate in real time the price of the new instrument based on the quotes of the other six symbols provided by your broker. The price changes will be visualized in the Market Watch window and on the chart:

![A synthetic instrument in Market Watch and its chart](/en/docs/mt5/client/img/synthetic_chart.png "A synthetic instrument in Market Watch and its chart")

Create a new custom symbol, open [its specification](/en/docs/mt5/client/trading_advanced/custom_instruments) and specify the formula:

![Instrument specification with a formula](/en/docs/mt5/client/img/synthetic_instrument.png "Instrument specification with a formula")

Calculation of [ticks](/en/docs/mt5/client/trading_advanced/custom_instruments#synthetic_ticks) and [1-minute bars](/en/docs/mt5/client/trading_advanced/custom_instruments#synthetic_bars) of a synthetic instrument starts when this instrument is added to the Market Watch. Also, all symbols required for the synthetic price calculation are automatically added to the Market Watch. An entry about the calculation start will be added to the platform [log](/en/docs/mt5/client/start_advanced/journal): Synthetic Symbol USDX: processing started.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Calculation of a synthetic instrument is stopped after it is removed from the Market Watch.</span></li><li class="p_tableatten"><span class="f_tableatten">Symbols that are currently used for calculating synthetic symbol prices cannot be hidden from the Market Watch.</span></li></ul></td></tr></tbody></table>

### Real-Time Calculation of Quotes [#](custom_instruments#synthetic_ticks)

Every 100 ms (i.e. ten times per second) the prices of the symbols used in calculation are checked. If at least one of them has changed, the price of the synthetic symbol is calculated and a new tick is generated. Calculation is performed in parallel in three threads for Bid, Ask and Last prices. For example, if the calculation formula is EURUSD\*GBPUSD, the price of the synthetic symbol will be calculated as follows:

-   Bid = bid(EURUSD)\*bid(GBPUSD)
-   Ask = ask(EURUSD)\*ask(GBPUSD)
-   Last = last(EURUSD)\*last(GBPUSD)

The availability of changes is checked separately for each price. For example, if only the Bid price of a source instrument has changed, only the appropriate price of a synthetic instrument will be calculated.

### Creating a History of 1-Minute Bars [#](custom_instruments#synthetic_bars)

In addition to collecting ticks in real time, the platform creates a minute history of the synthetic instrument. It enables traders to view synthetic symbol charts similar to normal ones, as well as to conduct technical analysis using objects and indicators.

When a trader adds a synthetic instrument to the Market Watch, the platform checks whether its calculated minute history exists. If it does not exist, the history for the last 60 days will be created, which includes about 50,000 bars. If a lower value is specified in the [Max. bars in chart](/en/docs/mt5/client/settings#max_bars) parameter in platform settings, the appropriate limitation will apply. If some of bars within this period were created earlier, the platform will additionally generate new bars.

After creating bars for the last 60 days, the platform will continue to create a deeper history in the background mode. The price history of each symbol used in the synthetic formula can be of different depth. Therefore the calculation is performed for the shortest available period. For example, the formula uses three financial instruments:

-   EURUSD with the history down to 2009.01.01
-   USDJPY with the history down to 2012.06.01
-   EURJPY with the history down to 2014.06.01

In this case, the history of the synthetic symbol will be calculated for a period from 2014.06.01 to the present. 100 minutes will be additionally discarded from this date, to ensure the calculation integrity (if any minute bar is not available in history, a previous minute bar is used in the calculation).

The history of one-minute bars of a synthetic instrument is calculated based one one-minute bars (not ticks) of instruments used in its formula. For example, to calculate the Open price of a 1-minute bar of a synthetic symbol, the platform uses the Open prices of symbols used in its formula. High, Low and Close prices are calculated in a similar way.

If the required bar is not available for any of the instruments, the platform will use the Close price of the previous bar. For example, three instruments are used: EURUSD, USDJPY and GBPUSD. If in the calculation of a bar corresponding to 12:00 the required bar of USDJPY is not available, the following prices will be used for calculation:

-   Open: EURUSD Open 12:00, USDJPY Close 11:59, GBPUSD Open 12:00
-   High: EURUSD High 12:00, USDJPY Close 11:59, GBPUSD High 12:00
-   Low: EURUSD Low 12:00, USDJPY Close 11:59, GBPUSD Low 12:00
-   Close: EURUSD Close 12:00, USDJPY Close 11:59, GBPUSD Close 12:00

If the minute bar is not available for all instruments used in the formula, the appropriate minute bar of the synthetic instrument will not be calculated.

### Creating Minute Bars

All new bars (current and subsequent ones) of the synthetic instrument are created based on the generated ticks. The price used for building the bars depends on the "Chart mode" parameter in the [specification](/en/docs/mt5/client/trading_advanced/custom_instruments):

![Chart mode of a synthetic instrument](/en/docs/mt5/client/img/synthetic_chart_mode.png "Chart mode of a synthetic instrument")

### What Operations Are Allowed in the Symbol Formula?

Price data and some properties of existing symbols provided by the broker can be used for calculating synthetic prices. Specify the following:

-   Symbol name — depending on the synthetic price to be calculated, the Bid, Ask or Last of the specified instrument will be used. For example, if EURUSD\*GBPUSD is specified, Bid is calculated as bid(EURUSD)\*bid(GBPUSD), and Ask = ask(EURUSD)\*ask(GBPUSD).
-   bid(symbol name) — the bid price of the specified symbol will be forcedly used for calculating the Bid price of the synthetic instrument. This option is similar to the previous one (where the price type is not specified).
-   ask(symbol name) — the Ask price of the specified symbol will be used for calculating the Bid price of the synthetic instrument. Bid price of the specified instrument will be used for calculating Ask. The Last price of the specified symbol will be used for calculating Last. If ask(EURUSD)\*GBPUSD is specified, the following calculation will be used:

-   Bid = ask(EURUSD)\*bid(GBPUSD)
-   Ask = bid(EURUSD)\*ask(GBPUSD)
-   Last = last(EURUSD)\*last(GBPUSD)
-   last(symbol name) — the Last price of the specified symbol will be used in the calculation of all prices of the synthetic instrument (Bid, Ask and Last). If last(EURUSD)\*GBPUSD is specified, the following calculation will be used:
-   Bid = last(EURUSD)\*bid(GBPUSD)
-   Ask = last(EURUSD)\*ask(GBPUSD)
-   Last = last(EURUSD)\*last(GBPUSD)
-   volume(symbol name) — the tick volume of the specified instrument will be used in the formula. Make sure that volume information is provided by the broker for this symbol.
-   point(symbol name) — the minimum price change of the specified instrument will be used in calculations.
-   digits(symbol name) — the number of decimal places in the specified symbol price will be used in the formula.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If a symbol has a complex name (contains hyphens, dots, etc.), it must be written in quotation marks. Example: "RTS-6.17".</span></p></td></tr></tbody></table>

The following arithmetic operations can be used in the formula: addition (+), subtraction (-), multiplication (\*), division (/) and remainder of division (%). For example, EURUSD+GBPUSD means that the price is calculated as the sum of EURUSD and GBPUSD prices. Also you can use the unary minus to change the sign, for example: -10\*EURUSD.

Mind the calculation priority of arithmetic operations:

-   The operations of multiplication, division and remainder are performed first, then addition and subtraction operations are performed.
-   The operations are performed from left to right. If the formula uses several operations that have the same priority (for example, multiplication and division), the operation on the left will be performed first.
-   You can use brackets ( and ) to change the priority of operations. Operations in brackets have the highest priority in the calculation. The left-to-right principle also applies for them: operations in brackets on the left are calculated first.

You can use constants in the formula:

-   Numerical (integer and float). Example: EURUSD\*2+GBPUSD\*0.7.
-   Symbol properties \_Digits and \_Point. They add to the formula appropriate properties of the custom symbol from the [specification](/en/docs/mt5/client/trading_advanced/custom_instruments). \_Digits means the number of decimal places in the instrument price; \_Point means the smallest change in the symbol price.

You can also use in the formula all [mathematical functions](https://www.mql5.com/en/docs/math) supported in [MQL5](/en/docs/mt5/client/autotrading#mql5), except for MathSrand, MathRand and MathIsValidNuber:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">fabs(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns an absolute value (modulo value) of the number passed to the function.</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">acos(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the arc cosine of the number in radians</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">asin(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the arcsine of the number in radians</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">atan(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the arc tangent of the number in radians</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">ceil(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the nearest upper integer</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">cos(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the cosine of the number</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">exp(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the exponent of the number</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">floor(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the nearest lower integer</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">log(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the natural logarithm</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">log10(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the logarithm of a number by base 10</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">fmax(number1, number2)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the highest of two numeric values</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">fmin(number1, number2)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the lowest of two numeric values</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">fmod(dividend, divisor)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the real remainder of the division of two numbers</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">pow(base, power)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Raises the base to the specified power</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">round(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Rounds the number to the nearest integer</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">sin(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the sine of the number</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">sqrt(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the square root</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">tan(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the tangent of the number</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">expm1(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the value of the expression exp(number)-1</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">log1p(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the value of the expression log(1+number)</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">acosh(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the value of the hyperbolic arc cosine</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">asinh(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the value of the hyperbolic arcsine</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">atanh(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the value of the hyperbolic arc tangent</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">cosh(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the value of the hyperbolic cosine</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">sinh(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the value of the hyperbolic sine</span></p></td></tr><tr class="table"><td class="table" style="width:170px;"><p class="p_fortable"><span class="f_fortable">tanh(number)</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Returns the value of the hyperbolic tangent</span></p></td></tr></tbody></table>

[Collateral Symbols](/en/docs/mt5/client/trading_advanced/collateral)

[Spreads](/en/docs/mt5/client/trading_advanced/spreads)