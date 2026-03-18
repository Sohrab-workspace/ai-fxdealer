# Calculation of Profit

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_symbols/profit_calculation

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Symbols](/en/docs/mt4/administrator/administration/ug_symbols)Profit Calculation

# Calculation of Profit

For various types of trading instruments, the profit is calculated differently. The final profit is calculated in two stages:

-   Basic calculation for a symbol;
-   Conversion of the profit currency into the deposit one.

## Basic Calculation for a Symbol [#](profit_calculation#main)

The trading platform provides five types of profit calculation depending on the financial instrument. You can select the calculation type in Calculation tab (["Profit calculation"](/en/docs/mt4/administrator/administration/ug_symbols#profit_calculation) field).

When calculating the profit, mathematical rounding by the number of decimal places in client's deposit currency is applied. Rounding is designated by Normalize() function in the formulas described below.

### Forex

Profit from Buy deals (when performing the opposite operations) at Forex symbols is calculated using the following formula:

Normalize(Close price  \* Contract size \* Volume in lots) — Normalize(Open price \* Contract size \* Volume in lots)

For Sell deals, Open and Close prices switch places in the formula:

Normalize(Open price  \* Contract size \* Volume in lots) — Normalize(Close price \* Contract size \* Volume in lots)

Let's consider closing a Buy position for 1 lot of EURUSD. The position was opened at 1.2000. The price at the closing moment is 1.2050. The contract size is 100 000. After placing these values to the formula, we obtain the following result:

Normalize(1.2050 \* 100 000 \* 1) — Normalize(1.2000 \* 100 000 \* 1) = 500 USD

So, now we have the profit value in profit currency of the symbol.

### CFD

Profit from Buy deals (when performing the opposite operations) at Forex, CFD and Stocks symbols is calculated using the following formula:

Normalize((Close price — Open price) \* Contract size \* Volume in lots \* Rate for conversion to deposit currency)

For Sell deals, Open and Close prices switch places in the formula:

Normalize((Open price — Close price) \* Contract size \* Volume in lots \* Rate for conversion to deposit currency)

Let's consider closing a Buy position for 1 lot of EURUSD. Deposit currency is USD. The position was opened at 1.2000. The price at the closing moment is 1.2050. The contract size is 100 000. After placing these values to the formula, we obtain the following result:

Normalize(1.2050 \* 100 000 \* 1) — Normalize(1.2000 \* 100 000 \* 1) = 500 USD

So, now we have the profit value in profit currency of the symbol. Since it matches the deposit currency, no conversion is needed.

### Futures [#](profit_calculation#futures)

Buy deals profit for futures is calculated using the following formula:

Normalize((Close price — Open price) \* Volume in lots \* Tick price / Tick size)

For Sell deals, Open and Close prices also switch places in the formula:

Normalize((Open price — Close price) \* Volume in lots \* Tick price / Tick size)

Correlation between the [price](/en/docs/mt4/administrator/administration/ug_symbols#tick_price) and one tick [size](/en/docs/mt4/administrator/administration/ug_symbols#tick_size) is considered when calculating profit for futures deals.

## Converting into Deposit Currency [#](profit_calculation#conversion)

Calculated profit conversion is performed if a profit currency is different from the account's [deposit currency](/en/docs/mt4/administrator/administration/ug_groups#deposit_currency).

### Forex

-   First, it is checked if the deal's symbol can be used for conversion. If yes, the current price is used for conversion: Bid — for Buy positions, Ask — for Sell ones.

-   Otherwise, an ending is derived from a position symbol name: the first six characters of the name are considered to be the symbol's main name, while the remaining part is considered to be an ending. For example, for EURUSDmicro pair, the main name is EURUSD, while an ending is micro.

-   A conversion currency pair is formed from profit and deposit currencies. An ending (if present) is added to the obtained pair.
-   The pair for direct conversion is sought. For example, if a profit is calculated for USDJPYmicro deal, while EUR is the deposit currency, the search for EURJPYmicro is conducted.
-   If the pair is found, conversion is performed by Bid price for Buy positions or Ask price - for Sell ones.
-   If such a symbol is not found, an attempt to convert using USD is made. Suppose that profit is calculated in RUR, while the deposit currency - in EUR. If the server has no EURRUR, two symbols (EURUSD and USDRUR) are used for conversion. Thus, the conversion is performed in two stages. Either Bid (if profit is calculated for Buy positions), or Ask price (for Sell positions) is used for both stages.

-   The presence of an ending is considered when searching for symbols. If a symbol with an open position has an ending, only the symbols with the same ending are used for conversion.

### CFD and Futures

-   At the start of the conversion, the search for a Forex symbol (symbol of Forex calculation type) with the base and quoted currency coinciding with the profit and deposit one is performed. Only pairs in the form of XXXYYY without suffixes are used. For example, USDCHF symbol is used to convert USD to CHF.
-   If such a symbol is found, its current Bid price is used.

-   If there is no such a symbol, the attempt is made to convert via USD. Suppose that the profit currency is XYZ, while the deposit one is ABC. If the server has no XYZABC or ABCXYZ symbol, two symbols (XYZUSD and ABCUSD) are used for conversion. Thus, the conversion is performed in two stages. Either Bid (if profit is calculated for Buy positions), or Ask price (for Sell positions) is used for both stages.
-   If conversion using USD is also impossible (no symbols), the profit is equal to zero.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Only symbols with the Forex calculation type can be used for conversion. For example, if you have the EURTRY symbol with the Futures calculation type, the platform will not be able to use its prices to convert EUR to TRY.</span></p></td></tr></tbody></table>

[Swap Calculation](/en/docs/mt4/administrator/administration/ug_symbols/swap_calculation)

[Securities](/en/docs/mt4/administrator/administration/ug_securities)