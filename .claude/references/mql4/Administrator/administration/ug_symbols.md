# Symbols

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_symbols

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Symbols

# Symbols

In this section, the list of financial instruments (symbols) and their settings are kept:

![Symbols](/en/docs/mt4/administrator/img/br_symbols.png "Symbols")

-   Symbol — name of the instrument;
-   Type — [instruments group](/en/docs/mt4/administrator/administration/ug_securities) (forex, cfd, futures, indexes);
-   Execution is the way of execution of the trading operations (Request, Instant, Market). In the "Instant" mode, the client makes a transaction at once according to the prices in the "Market Watch" window without advance requesting of prices as in the "Request" mode. The "Market" mode is intended for opening an "at-the-market" position (used for futures only);
-   Filter shows the level in points at which the filtering of quotes will start operating;
-   Spread — spread in points;
-   Stops — shows the price range (in points) from the current market price within which one may not apply Stop Loss or Take Profit;
-   Long / Short — rollover for transferring a position;
-   Digits — amount of digits after the point in the instrument price;
-   Trade — possibility to deal in the instrument.

Up to 1023 symbols can be created. For creating a new instrument, it is necessary to execute the "Edit — Add" menu command or the same command of the context menu. "Edit — Edit" allows to change settings of the symbols selected, and the "Delete" — command allows to delete them. When adding or adjusting anything, the window with detailed settings of the instrument will appear:

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: We highly recommend to perform changing list of financial instruments only on holidays, when markets are closed.</span></p></td></tr></tbody></table>

## Financial Instruments Detailed Setting, Symbol Tab [#](ug_symbols#setup_symbol)

![Symbol Tab](/en/docs/mt4/administrator/img/win_symbols_symbol.png "Symbol Tab")

-   Symbol — short name (symbol) of the instrument, Latin characters only, no punctuation marks, spaces or special characters (".","\_","&","#" are allowed). This name of the instrument will be used inside the whole system.One should not use only special characters as a symbol suffix, for example: EURUSD. or EURUSD.. . The suffix should include also letters, for example: EURUSD.pro;
-   Source is the synonym of the basic symbol the quotes of which should be used for the current instrument. The name of a real instrument of the system must be given. Note that the quotes will be taken directly from the corresponding symbols in the [data feed](/en/docs/mt4/administrator/administration/ug_data_feeds) (without any transformation according to the settings of the corresponding symbol in the trading platform). After having changed parameter in this field, you should restart server;

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If there are no history data for a symbol, but the "Source" field is filled out, these data will be created after the server restart by automatic copying history data of the symbol specified in the "Source" field.</span></p></td></tr></tbody></table>

-   Digits — the amount of digits after the point in the instrument's quotes;
-   Description — description of the instrument;
-   Type — a group type the instrument to be included in (the values are taken from the [Securities](/en/docs/mt4/administrator/administration/ug_securities) section);
-   Execution is the way of execution of the trading operations (Request, Instant, Market). In the "Instant" mode, the client makes a transaction at once according to the prices in the "Market Watch" window without advance requesting of prices as in the "Request" mode. The "Market" mode is intended for opening an "at-the-market" position (used for futures only);
-   Currency is calculation currency of the instrument. For the instruments with [Forex profit calculation](/en/docs/mt4/administrator/administration/ug_symbols/profit_calculation), the currency field denotes the underlying asset. It is always set as the first currency in the pair, and it cannot be changed. The second currency in the pair is used as the profit currency. For the instruments with CFD and Futures profit calculation, the currency field denotes the underlying assets and the profit currency. For this type of instruments the currency field is editable;
-   Trade — permission to deal in this instrument: "Full access" allows to close and open positions; "Close only" allows only closing; "No" — full prohibit to trade;
-   Background — background color of the instrument. This instrument will have the same background color in the "Market Watch" window of the client terminal and the manager terminal;
-   Margin currency is currency of margin calculation. This field is used when it is necessary to calculate margin requirements for a currency, other than the standard one of a symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">Examples of Margin Calculation:</span></p><p class="p_tableatten"><span class="f_tableatten">1. On EURUSD for <a href="/en/docs/mt4/administrator/administration/ug_symbols#setup_calculation" class="topiclink">Contract size</a> equal to EUR100,000 the margin requirements for a client having the deposit currency USD under standard conditions ("Margin currency" field is filled out with "EUR") will be calculated as:</span></p><p class="p_formula_table"><span class="f_formula_table">margin = contract_size * price * volume / leverage</span></p><p class="p_tableatten"><span class="f_tableatten">I.e. margin = 100000 * 1.2228 * 1 / 100 = USD1222.8, where contract_size = 100000, price = 1.2228 (EURUSD price), volume = 1, leverage = 100, respectively.</span></p><p class="p_tableatten"><span class="f_tableatten">2. For using margin requirements having <a href="/en/docs/mt4/administrator/administration/ug_symbols#setup_calculation" class="topiclink">Contract size</a> equal to USD100,000 it is enough to specify USD as a value for the "Margin currency" field. At this, margin requirements will be calculated as:</span></p><p class="p_formula_table"><span class="f_formula_table">margin = contract_size * volume / leverage.</span></p><p class="p_tableatten"><span class="f_tableatten">I.e. margin = 100000 * 1 / 100 = USD1000, where contract size = 100000, volume = 1, leverage = 100, respectively.</span></p><p class="p_tableatten"><span class="f_tableatten">"Margin currency" field value does not influence the profit calculations for a position. In both shown examples the profits are calculated for the contract size equal to EUR100,000.</span></p></td></tr></tbody></table>

-   Maximum Lots for IE indicates the size of the maximum permissible lot of the order in the "Instant" mode. All clients' orders having lots exceeding the indicated value will automatically be switched to the request execution mode;
-   Orders — types of allowed orders:

-   "Good Till Today including SL/TP" — intraday orders, all pending orders, as well as SL and TP levels of orders are removed when the next trading day starts;
-   "Good Till Canceled" — hold pending orders at the trading day change;
-   "Good Till Today excluding SL/TP" — daily orders, at the trading day change, the SL and TP levels are kept, only pending orders are deleted;

-   Spread by default — the spread of the instrument by default. Spread of instrument groups can be changed in the ["Groups"](/en/docs/mt4/administrator/administration/ug_groups#group_securities) section;
-   Long only — only long orders are allowed;
-   Limit & Stop Level — the price range (in points) from the current market price within which it is not allowed to set Stop Loss, Take Profit, or pending orders. When setting orders within that range, the server will return the "Invalid Stops" message and will not accept the order;
-   Spread Balance — the balance of spread;
-   Freeze Level — level for freezing orders that are close to the current price. When an order price is as close to the market price as the value specified here or less than that, its modification or deletion is prohibited. This limitation is also applied to positions. When current market price is close to a Stop Loss of Take Profit level of a position, modification of these levels is prohibited as well as modification of the position volume and closing of the position.

## Financial Instrument Detailed Setting, Filter Tab [#](ug_symbols#setup_filter)

![Filter Tab](/en/docs/mt4/administrator/img/win_symbols_filter.png "Filter Tab")

-   Allow Realtime Quotes from Datafeeds — allowing/prohibiting taking realtime quotes for this symbol from datafeeds. If this option is disabled a dealer may throw in the quotes for this symbol manually;
-   Save all incoming prices in a file — enabling/disabling to save tick prices into the \*.dat file.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention! This option must be disabled! This option can only be enabled when addition quotes control is needed.</span></p></td></tr></tbody></table>

-   Filtration Level is the level of filtration of incoming quotes in points. You can disable filtration putting 0. Filtering conditions:

-   |Ask — Bid| > filter
-   |Askcurrent — Askprevious| > filter
-   |Bidcurrent — Bidprevious| > filter

-   Automatic Limit forms the price range. If a new quote exceeds this range, it will be cut out. The "No" option will disable automatic filtration;
-   Filter — the amount of quotes needed to confirm a new level (disabling filtering).
-   Ignore quotes — period in seconds to ignore quotes after session start.
-   Smoothing — is the parameter of price smoothing in ticks. If this parameter is set, after general filtration incoming prices are smoothed by a weighted moving average.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten" style="font-weight: bold;">Example of a smoothing algorithm operation:</span></p><p class="p_tableatten"><span class="f_tableatten">1. For EURUSD the smoothing parameter 4 is set.</span></p><p class="p_tableatten"><span class="f_tableatten">2. Last incoming prices for this symbol (before smoothing) are: 1.4536 / 1.4538, 1.4539 / 1.4541, 1.4540 / 1.4542</span></p><p class="p_tableatten"><span class="f_tableatten">3. New price after filtration and spread value changing: 1.4544 / 1.4546.</span></p><p class="p_tableatten"><span class="f_tableatten">4. Calculate the average weighted price, the maximal weight being that of the last quote:</span></p><p class="p_formula_table"><span class="f_formula_table">SmoothedPrice = (1.4536*1 + 1.4539*2 + 1.4540*3 + 1.4544*4)/(1+2+3+4) = 1.4541</span></p><p class="p_tableatten"><span class="f_tableatten">5. Calculate a new pair of prices using spread value: 1.4541 / 1.4543.</span></p><p class="p_tableatten"><span class="f_tableatten">Attention! Quote smoothing should be used with maximal caution! Use of a large smoothing parameter will result in the delay of prices as compared to a quotes source!</span></p></td></tr></tbody></table>

## Financial Instrument Detailed Setting, Calculation Tab [#](ug_symbols#setup_calculation)

![Calculation Tab](/en/docs/mt4/administrator/img/win_symbols_calculation.png "Calculation Tab")

-   Contract size — the size of the contract;
-   Initial margin — the initial margin (for futures);
-   Maintenance — the "maintaining" margin (for futures);
-   Hedged — the "hedged" margin;
-   Tick size — the tick size (for futures);
-   Tick Price — the price of a tick (for futures);
-   Percentage — margin calculation factor, in percentage;
-   Profit calculation — the formula of profit calculation;
-   Margin calculation — the formula of margin calculation.
-   Strong hedged margin mode — strict check of margin requirements when opening a hedge position; when the option is disabled a hedge position can only be opened if free margin remains as non-negative after that or if margin requirements are reduced after the hedge position has been opened; when the option is enabled opening ot a hedge position is only permitted if free margin remains non-negative after that.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For the new value of the Percentage parameter to take effect, you must restart the trading server. To update the account status in the client terminal after the margin settings have been changed, you must reconnect to the account.</span></p></td></tr></tbody></table>

## Financial Instrument Detailed Setting, Swaps Tab [#](ug_symbols#setup_swaps)

![Swaps Tab](/en/docs/mt4/administrator/img/win_symbols_swaps.png "Swaps Tab")

-   Enable — enabling/disabling swap calculation for the instrument;
-   Type — the type of rollover calculation:

-   by points — swaps are charged in points in the volume specified below for short and long positions. The specified number of points is charged for each lot of a position. Swap size is converted from points to money (deposit currency). To do it, the point price of the corresponding buy position is calculated (regardless of the actual direction of the position).
-   by money — in [calculation currency](/en/docs/mt4/administrator/administration/ug_symbols#currency). The swap size is converted from the base currency into the deposit currency using the average price at the moment of swap charging: (Bid+Ask)/2.
-   by interest — as annual interest rate.  Since swaps are calculated and charged every day at the end of day time, the calculated amount of the annual interest rate is divided by 360. When charging swaps, first the cost of one symbol lot is calculated (the symbol of the opened position), and then the specified percent is calculated, the obtained amount is multiplied by the position volume (in lots) and the result is divided by 360. If the base currency of the symbol is different from the deposit currency, the swap is converted into the deposit currency. The conversion is performed using the average price at the moment of swap charging: (Bid+Ask)/2.
-   by money in margin currency — in [currency of margin calculation](/en/docs/mt4/administrator/administration/ug_symbols#margin_currency). The swap size is converted from the margin currency into the deposit currency using the average price at the moment of swap charging: (Bid+Ask)/2.

-   Long & Short positions — rollover values for calculation of long and short positions. The values can be redefined.
-   3-days swaps — the day of triple swap charge.
-   Use open price for position value calculation — if this option is enabled the calculation of the position value when charging the swaps in annual interest rates will be performed by the open price of the position (instead of the price at the end of day). This option does not affect the calculation of swaps for Forex symbols ([calculation type is "Forex")](/en/docs/mt4/administrator/administration/ug_symbols#setup_calculation).
-   Charge variation margin on rollover — if this option is enabled then during swap charging of swaps profit of all trade positions for a symbol is recalculated using the current prices, after which the financial result of a position (floating profit + swap) is added or deducted from a client's account in a separate balance operation. After that the position profit and swap are cleared, and the position open price is set equal to the current market price.

## Financial Instrument Operating Time Adjustment, Sessions Tab [#](ug_symbols#setup_sessions)

![Sessions Tab](/en/docs/mt4/administrator/img/win_symbols_sessions.png "Sessions Tab")

The Sessions tab is used for controlling the operating time of a financial instrument on certain days of the week.

To set the allowed trading time for the symbol, enable the "Use time limits" option. Then set the start and end of the period in the "From" and "To" fields. The "Use time limits" option does not affect the ability to transmit quotes for the symbol.

Double-clicking the desired day to adjust the quotes and trade sessions.

![Session Adjustment](/en/docs/mt4/administrator/img/win_symbols_sessions_details.png "Session Adjustment")

In the "Quotes" and "Trade" fields, you can separately adjust time for quotes translation or for the opportunity to trade using the desired instrument. If you need to adjust the different time for quotes translation and trading opportunity you should check the "Enable separate trading sessions" box. You can specify up to three quote and trading sessions for each day. Each trading session must be within the range of quotes session.

Moving the levers that set session start and closing time can be performed both using a mouse and keyboard arrows. If you hold the "Shift" button, their moving will be slowed down. Thus you can adjust the time of sessions within the accuracy of a minute.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: It is highly recommended to perform operations of changing the list of financial instruments on holidays only, when markets are closed.</span></p></td></tr></tbody></table>

[Holidays](/en/docs/mt4/administrator/administration/ug_holiday)

[Symbols Import](/en/docs/mt4/administrator/administration/ug_symbols/ug_symbols_import)