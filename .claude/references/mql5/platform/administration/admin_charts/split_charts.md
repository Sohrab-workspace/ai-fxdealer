# Split Stocks

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_charts/split_charts

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
                -   [Import of History Data](/en/docs/mt5/platform/administration/admin_charts/admin_charts_import)
                -   [Split Stocks](/en/docs/mt5/platform/administration/admin_charts/split_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)Split Stocks

# Split Stocks

Split is an increase of the number of outstanding stocks by splitting them with a proportional decrease in their value. The opposite operation — consolidating (or reverse split) by decreasing a number of stocks with a proportional increase in their value — is possible as well.

The appropriate operations (stock splitting/consolidation) can be executed on the trading platform's side as well:

-   Transforming the minute and [tick symbol history](/en/docs/mt5/platform/administration/admin_ticks/split_ticks) means proportional increase or decrease in prices, spreads and volumes.
-   Transforming the current client's positions — assigning a new volume and price with the ability to remove stop loss and take profit levels. Transforming is performed using MetaTrader 5 Manager.

Click "Split Stock" in the context menu of the "1 Minute History Charts" section.

![Transforming minute data when splitting stocks](/en/docs/mt5/platform/img/split_charts.png "Transforming minute data when splitting stocks")

Select a trading instrument and a time interval, and click Request. Minute bars appear in the list.

Set the split settings:

-   Use "New Shares" and "Old Shares" to set stock split/consolidation ratio so that prices can be transformed similarly.
-   Set the rounding rule in case the number of digital places of a new price exceeds the value set in the symbol's [Digits parameter](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common#digits). For example, when transforming the price of 35.15 with the ratio of 2:1, we obtain 17.575. When rounded down, the final price is 17.57, when rounded up, it is 17.58. Also, the "Standard" rounding option (standard rounding to the nearest integer) is available as well. For example, if the Digits is 2, the rounding is performed as follows: 17.234 -> 17.23, 17.235 -> 17.24.
-   If necessary, you can specify the time interval in which the split will be performed, using the "Split from" and "To" fields. In this case the operation will only be performed for one-minute data in the specified range, while the remaining data will not be affected. Such an operation may be needed for performing a backdated split. If you want to split the entire available symbol history, leave these parameters unchanged.

After implementing all the settings, click Calculate to see the preliminary split results. New parameters for each bar are displayed in the table: new OHLC prices and spread. Click Process to execute a split.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Splitting can take quite a long time. Do not launch the process during trading hours.</span></li><li class="p_tableatten"><span class="f_tableatten">Split is performed both for 1-minute and tick data, regardless of the section from which the process is launched. Only preliminary split results can be viewed separately.</span></li></ul></td></tr></tbody></table>

The process can be tracked using the [history server journal](/en/docs/mt5/platform/administration/admin_network/network_journal).

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2017.04.18&nbsp;17:30:27.339&nbsp;&nbsp;&nbsp;&nbsp;HistoryBase&nbsp;&nbsp;&nbsp;&nbsp;#AA&nbsp;split&nbsp;2&nbsp;for&nbsp;1&nbsp;started,&nbsp;up&nbsp;rounding</span><br><span class="f_CodeExample">2017.04.18&nbsp;17:30:27.366&nbsp;&nbsp;&nbsp;&nbsp;HistoryBase&nbsp;&nbsp;&nbsp;&nbsp;#AA&nbsp;split&nbsp;for&nbsp;2014.04.26&nbsp;completed&nbsp;[1239&nbsp;bars&nbsp;updated,&nbsp;126977&nbsp;ticks&nbsp;updated]</span><br><span class="f_CodeExample">2017.04.18&nbsp;17:30:27.406&nbsp;&nbsp;&nbsp;&nbsp;HistoryBase&nbsp;&nbsp;&nbsp;&nbsp;#AA&nbsp;split&nbsp;for&nbsp;2014.04.27&nbsp;completed&nbsp;[1052&nbsp;bars&nbsp;updated,&nbsp;105122&nbsp;ticks&nbsp;updated]</span><br><span class="f_CodeExample">....</span><br><span class="f_CodeExample">2017.04.18&nbsp;17:34:28.429&nbsp;&nbsp;&nbsp;&nbsp;HistoryBase&nbsp;&nbsp;&nbsp;&nbsp;#AA&nbsp;split&nbsp;for&nbsp;2017.04.17&nbsp;completed&nbsp;[1438&nbsp;bars&nbsp;updated,&nbsp;134115&nbsp;ticks&nbsp;updated]</span><br><span class="f_CodeExample">2017.04.18&nbsp;17:34:28.888&nbsp;&nbsp;&nbsp;&nbsp;HistoryBase&nbsp;&nbsp;&nbsp;&nbsp;#AA&nbsp;split&nbsp;for&nbsp;2017.04.18&nbsp;completed&nbsp;[874&nbsp;bars&nbsp;updated,&nbsp;89779&nbsp;ticks&nbsp;updated]</span><br><span class="f_CodeExample">2017.04.18&nbsp;17:34:28.888&nbsp;&nbsp;&nbsp;&nbsp;HistoryBase&nbsp;&nbsp;&nbsp;&nbsp;#AA&nbsp;split&nbsp;2&nbsp;for&nbsp;1&nbsp;finished&nbsp;[3497656&nbsp;bars&nbsp;updated,&nbsp;26295115&nbsp;ticks&nbsp;updated]</span></p></td></tr></tbody></table>

## Split Scanner [#](split_charts#split_scanner)

Split scanner automatically analyzes the price history of trading instruments to identify possible stock splits. The scanner then adjusts the price history to generate a smooth chart corresponding to the instrument's current prices. During analysis, the system additionally checks an internal database of publicly known stock splits.

Go to the "1-Minute History Charts" section and select "![Split Scanner](/en/docs/mt5/platform/img/split_scanner_icon.png "Split Scanner")Split Scanner" in the context menu. Next, select a group of symbols and click "Scan". Check the received split points. The list will display:

-   Found split date
-   Price before and after split, their ratio
-   Number of stocks before and after split, their ratio (split ratio)
-   Overall conversion rate for prices and stocks, taking into account all splits found for the instrument

To customize the information displayed, use the context menu.

Records found in the internal list of known splits are highlighted in green.

![Splits search result](/en/docs/mt5/platform/img/split_scanner.png "Splits search result")

Check the "Recalculate Charts" box for the desired splits. Please note that there can be multiple splits for each instrument. Click "Process split", and the platform will automatically convert minute and tick data.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Splitting can take quite a long time. Do not launch the process during trading hours.</span></li><li class="p_tableatten"><span class="f_tableatten">Split is performed both for 1-minute and tick data, regardless of the section from which the process is launched. Only preliminary split results can be viewed separately.</span></li></ul></td></tr></tbody></table>

[Import of History Data](/en/docs/mt5/platform/administration/admin_charts/admin_charts_import)

[Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)