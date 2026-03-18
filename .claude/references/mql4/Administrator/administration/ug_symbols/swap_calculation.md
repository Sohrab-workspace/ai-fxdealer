# Swap Calculation

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_symbols/swap_calculation

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
            -   [Common](/en/docs/mt4/administrator/administration/ug_options)
            -   [Gateway](/en/docs/mt4/administrator/administration/gateway)
            -   [IP Access List](/en/docs/mt4/administrator/administration/ug_access)
            -   [Data Centers](/en/docs/mt4/administrator/administration/ug_data_server)
            -   [Time](/en/docs/mt4/administrator/administration/ug_time)
            -   [Holidays](/en/docs/mt4/administrator/administration/ug_holiday)
            -   [Symbols](/en/docs/mt4/administrator/administration/ug_symbols)
                -   [Symbols Import](/en/docs/mt4/administrator/administration/ug_symbols/ug_symbols_import)
                -   [Margin Calculation](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation)
                -   [Swap Calculation](/en/docs/mt4/administrator/administration/ug_symbols/swap_calculation)
                -   [Profit Calculation](/en/docs/mt4/administrator/administration/ug_symbols/profit_calculation)
            -   [Securities](/en/docs/mt4/administrator/administration/ug_securities)
            -   [Groups](/en/docs/mt4/administrator/administration/ug_groups)
            -   [Managers](/en/docs/mt4/administrator/administration/ug_managers)
            -   [Data Feeds](/en/docs/mt4/administrator/administration/ug_data_feeds)
            -   [Backup](/en/docs/mt4/administrator/administration/ug_backup)
            -   [Live Update](/en/docs/mt4/administrator/administration/ug_live_update)
            -   [Synchronization](/en/docs/mt4/administrator/administration/ug_synchronization)
            -   [Plugins](/en/docs/mt4/administrator/administration/ug_plugins)
            -   [Accounts](/en/docs/mt4/administrator/administration/ug_accounts)
            -   [Orders](/en/docs/mt4/administrator/administration/ug_orders)
            -   [Charts](/en/docs/mt4/administrator/administration/ug_charts)
            -   [Ticks](/en/docs/mt4/administrator/administration/ug_ticks)
            -   [Server Journal](/en/docs/mt4/administrator/administration/ug_logs)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Symbols](/en/docs/mt4/administrator/administration/ug_symbols)Swap Calculation

# Swap Calculation

Three main swap calculation types are implemented in the trading platform. You can select one of the calculation types in ["Rollover mode"](/en/docs/mt4/administrator/administration/ug_options#swap) field of the common settings section:

-   Normal
-   Reopen by close price
-   Reopen by bid

In Normal mode, client positions remain unchanged, while swap is charged in the special position field and displayed on the balance after the position is closed. In case of partial closing, the swap is proportionally charged for the balance.

In the modes with reopening at [the end of a trading day](/en/docs/mt4/administrator/administration/ug_symbols/swap_calculation#swap_time), the current positions are closed and the news ones are opened at the closing price or at the current Bid price at the moment of rollover. The open price is additionally corrected by the value specified in the [symbol swap settings](/en/docs/mt4/administrator/administration/ug_symbols#setup_swaps).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When using the reopen rollover mode, charging of swaps in points must be selected in the symbol settings.</span></li><li class="p_tableatten"><span class="f_tableatten">During the configuration, the swap size is specified for 1 lot position.</span></li><li class="p_tableatten"><span class="f_tableatten">Charging of swaps may be disabled for client groups using <a href="/en/docs/mt4/administrator/administration/ug_groups#enable_swaps" class="topiclink">"Enable charge of swaps"</a> option.</span></li></ul></td></tr></tbody></table>

## Swap Charging Time [#](swap_calculation#swap_time)

Swaps are charged at the end of a trading day. Trading day end time is defined in ["End of day time"](/en/docs/mt4/administrator/administration/ug_options#eod) field of the common settings section:

-   End of the day — daily reports for the previous day are first generated, swaps are charged afterwards.
-   Beginning of the day — swaps are charged first, reports are generated afterwards.

This option also affects the time of newly opened positions when charging swaps by reopening:

-   End of the day — trading day end time is set as a position opening time.
-   Beginning of the day — beginning of the next trading session is set as a position opening time. Suppose that the end of a trading day is set to 23:59, while trading sessions continue from 00:00 to 24:00 on weekdays. When a trading day is closed on Thursday, positions are reopened in 00:00 on Friday. When a trading day is closed on Friday, positions are reopened in 00:00 on Saturday, though 00:00 of Monday is specified as the opening time for such positions.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Swaps are not charged on Saturdays and Sundays (if the end of day time falls on one of these days).</span></p></td></tr></tbody></table>

## Redefining Swap Settings for Groups

Symbol swap settings can be re-defined for separate client groups. To do that, add the swap configuration on [group's Symbols](/en/docs/mt4/administrator/administration/ug_groups#group_symbols) tab and set new values for the margin by short and long positions.

## Swap with Reopening

At the moment of the rollover, positions are closed at the current price and the new ones are opened at the closing price or at the current Bid price. The open price is additionally corrected by the value specified in the symbol swap settings. Suppose that value of 2 is set for long positions. If a position was closed at 1.39805 during the rollover, it is reopened at 1.39807.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the swap value is fractional, the number of decimal places in the price, at which the position is reopened, is increased accordingly. For example, the value of 0.33 is set for long positions. If the position was closed at 1.39805, the reopening price is 1.3980533.</span></p></td></tr></tbody></table>

## Swap in Points

Swap in points is calculated using the following formula:

Volume in lots \* Swap size \* Point price

Depending on the position direction, the swap size is taken from "Long positions" or "Short positions" field. The price of a single point is defined as the profit received when a price changes by one point. Calculation (including conversion to the deposit currency) is performed according to [profit calculation types by symbol](/en/docs/mt4/administrator/administration/ug_symbols/profit_calculation). Calculation is performed the same way as for 1 point of a long position with the volume of 1 lot.

## Swap in Base Currency and Margin Calculation Currency

When "by money" option is selected, absolute swap values for positions having appropriate direction are specified in "Long positions" and "Short positions" fields. The values are specified in the symbol's [base currency](/en/docs/mt4/administrator/administration/ug_symbols#currency).

When "by money in margin currency" option is selected, absolute swap values for positions having appropriate direction are also specified in "Long positions" and "Short positions" fields. In that case, the values are specified in the [symbol margin currency](/en/docs/mt4/administrator/administration/ug_symbols#currency).

If the swap currency is different from the client's [deposit currency](/en/docs/mt4/administrator/administration/ug_groups#deposit_currency), it is converted according to the following rules:

-   An ending is derived from a symbol name: the first six characters of the name are considered to be the symbol's main name, while the remaining part is considered to be an ending. For example, for EURUSDmicro pair, the main name is EURUSD, while an ending is micro.

-   A conversion currency pair is formed from swap and deposit currencies. An ending (if present) is added to the obtained pair.
-   The pair for direct conversion is sought. For example, if a swap is calculated for USDJPYmicro deal, while EUR is the deposit currency, the search for EURJPYmicro is conducted.
-   If such a pair is found, conversion is performed at an average pair's price at the time of conversion: (Bid + Ask)/2.
-   If such a symbol is not found, an attempt to convert using USD is made. Suppose that swap is calculated in RUR, while the deposit currency - in EUR. If the server has no EURRUR, two symbols (EURUSD and USDRUR) are used for conversion. Thus, the conversion is performed in two stages. At each stage, the average price of an appropriate pair at the time of conversion is used: (Bid + Ask)/2.

-   The presence of an ending is considered when searching for symbols. If a symbol with an open position has an ending, only the symbols with the same ending are used for conversion.

## Swap as Annual Interest Rate

If the swap is charged as a percentage value per annum, percentage share of the position price is specified in "Long positions" and "Short positions" fields. The calculation is performed the following way:

-   The price of position's single lot in base currency is defined.
-   If a base currency is different from the deposit one, 1 lot price is converted according to the rules described [above](/en/docs/mt4/administrator/administration/ug_symbols/swap_calculation#conversion).
-   The value is multiplied by the position volume
-   The percentage defined in "Long positions" or "Short positions" field is taken from the obtained value.
-   The obtained value is divided by 360 (number of days in a banking year), since the swap is charged daily.

The price of 1 lot of a Forex symbol is defined by the contract size specified in the base currency. For example, price of 1 lot of EURUSD with the contract size 100 000 is 100 000 EUR.

The method of defining the price of 1 lot of the symbols belonging to other types depends on ["Use open price for position value calculation"](/en/docs/mt4/administrator/administration/ug_symbols#swap_open_price) option in the symbol swap settings:

-   If the option is disabled: Contract size \* Current price
-   If the option is enabled: Contract size \* Open price

For Futures symbols, the obtained value is additionally multiplied by [Tick price](/en/docs/mt4/administrator/administration/ug_symbols#tick_price) / [Tick size](/en/docs/mt4/administrator/administration/ug_symbols#tick_size).

## Three-Days Swap

The [3-days swap](/en/docs/mt4/administrator/administration/ug_symbols#3day) , i.e. the weekday to calculate the threefold swap, is set in the symbol swap settings. The 3-days swap is used for deals, the payments for which fall on weekends. For example, Wednesday is the threefold swap day for spot Forex deals (settled at the second business day after the transaction). On this day, the swap for Thursday, Saturday and Sunday is charged (the market is closed on the latter two days).

## Charging Variation Margin

["Charge variation margin on rollover"](/en/docs/mt4/administrator/administration/ug_symbols) option is available in the symbol swap settings. When enabled, the financial result (floating profit + swap) of client positions is calculated at the end of a trading day, as if they were closed at the current market price. The calculated amount is deposited to the client accounts as a separate balance operation. The current market price is specified as the open price of these positions.

In fact, this operation allows you to forcibly fix the current profits/losses of client positions every day.

[Margin Calculation](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation)

[Profit Calculation](/en/docs/mt4/administrator/administration/ug_symbols/profit_calculation)