# Margin Calculation

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)[Symbols](/en/docs/mt4/administrator/administration/ug_symbols)Margin Calculation

# Margin Calculation

The margin is charged for securing traders' open positions. It is not charged for pending orders.

Generally, the margin for the client's account is calculated as the sum of the margin requirements for all open positions excluding covered ones. Covered positions are oppositely directed open positions for the same financial instrument.

Below are the margin calculation equations for trading symbols according to their type and settings. The final margin is calculated in three stages:

-   Basic calculation for a certain symbol;
-   [Conversion of the margin currency into the deposit one](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation#conversion);
-   [Multiplying by ratio](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation#rate);
-   [Considering hedged positions](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation#hedged).

## Basic Calculation for a Symbol [#](margin_calculation#main)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="height:19px;"><p class="p_tableatten"><span class="f_tableatten">If the <a href="/en/docs/mt4/administrator/administration/ug_symbols#initial_margin" class="topiclink">"Initial margin"</a> parameter value is set in the symbol settings, that value is used for calculation. The equations described in this section are not applied.</span></p></td></tr></tbody></table>

The trading platform provides several margin requirement calculation types depending on the financial instrument. You can select the calculation type in Calculation tab ([Margin calculation](/en/docs/mt4/administrator/administration/ug_symbols#margin_calculation) field):

### Forex

The margin for Forex market symbols is calculated using the following equation:

Volume in lots \* Contract size / Leverage

For example, let's calculate the margin requirements for buying one lot of EURUSD, while [the size of one contract](/en/docs/mt4/administrator/administration/ug_symbols#contract) is 100,000 and the leverage is 1:100. After placing the appropriate values to the equation, we will obtain the following result:

1 \* 100 000 / 100 = EUR 1,000

So, now we have the margin requirements value in [margin currency](/en/docs/mt4/administrator/administration/ug_symbols#margin_currency) of the symbol.

### CFD

The margin requirements for CFDs and stocks are calculated using the following equation:

Volume in lots \* Contract size \* Open market price

For example, let's calculate the margin requirements for buying one lot of oil, the size of the contract is 100 barrels, the current Ask price is USD 80. After placing the appropriate values to the equation, we will obtain the following result:

1 \* 100 \* 80 = USD 8,000

So, now we have the margin value in margin currency of the symbol.

### CFD Leverage

The leverage is also considered in this type of margin requirement calculation for CFDs:

Volume in lots \* Contract size \* Open market price / Leverage

### CFD Index [#](margin_calculation#cfd_index)

For index CFDs, the margin requirements are calculated according to the following equation:

Volume in lots \* Contract size \* Open market price \* Tick price / Tick size

In this equation, the ratio of [price](/en/docs/mt4/administrator/administration/ug_symbols#tick_price) and [one tick](/en/docs/mt4/administrator/administration/ug_symbols#tick_size) size is considered in addition to a common CFD calculation.

### Futures [#](margin_calculation#futures)

There are two types of the margin requirements for futures contracts:

-   Initial margin is the amount that must be available on the account at the moment of attempting to enter the market. Further maintenance of the same sum may not be obligatory.
-   Maintenance margin is the minimum amount that must be available on the account for maintaining an open position.

Both values are specified in [Calculation](/en/docs/mt4/administrator/administration/ug_symbols#setup_calculation) tab of the symbol settings. The final size of the margin depends on the volume:

Volume in lots \* Initial margin

Volume in lots \* Maintenance margin

### Fixed Margin [#](margin_calculation#fixed)

If a non-zero value is specified in the ["Initial margin"](/en/docs/mt4/administrator/administration/ug_symbols#initial_margin) field of Calculation tab, then no calculations by the above mentioned formulas are performed (except for the calculation of [futures](/en/docs/mt4/administrator/administration/ug_symbols/margin_calculation#futures)). In this case, for all types of calculations except for Forex and CFD Leverage, the margin is calculated as below:

Volume in lots \* Initial margin

For Forex and CFD Leverage calculation types, the leverage is additionally considered:

Volume in lots \* Initial margin / Leverage

## Margin Rate [#](margin_calculation#rate)

The "Percentage" parameter is provided in the [Calculation](/en/docs/mt4/administrator/administration/ug_symbols#margin_calculation) tab of the symbol settings. The previously calculated margin requirements value (converted into the deposit currency) is additionally multiplied by Percentage/100.

For example, the previously calculated margin for buying one lot of EURUSD is USD 1,279. This amount is additionally multiplied by Percentage/100. So, if Percentage is 115, the final margin is 1,279 \* 1.15 = USD 1,470.85.

## Converting into Deposit Currency [#](margin_calculation#conversion)

This stage is common for all calculation types. Conversion of the margin requirements calculated using one of the methods mentioned above is performed in case their currency is different from the [account deposit](/en/docs/mt4/administrator/administration/ug_groups#deposit_currency) one.

If conversion is performed for a Forex instrument (Margin calculation = Forex):

-   An ending is derived from a symbol name: the first six characters of the name are considered to be the symbol's main name, while the remaining part is considered to be an ending. For example, for EURUSDmicro pair, the main name is EURUSD, while an ending is micro.
-   A conversion currency pair is formed from margin and deposit currencies. An ending (if present) is added to the obtained pair.
-   If the obtained symbol coincides with the transaction currency pair, the position's open price is used for calculation.
-   Otherwise, the pair for direct conversion is sought. For example, if position is opened at EURJPYmicro, while USD is the deposit currency, the search for EURUSDmicro is conducted.
-   If such a pair is found, conversion is performed at an average pair's price at the time of conversion: (Bid + Ask)/2.
-   If such a symbol is not found, an attempt to convert using USD is made. Suppose that we have a position at EURJPY, while the deposit currency is TRY. If the server has no EURTRY symbol, two symbols (EURUSD and USDTRY) are used for conversion. Thus, the conversion is performed in two stages. At each stage, the average price of an appropriate pair at the time of conversion is used: (Bid + Ask)/2.
-   The presence of an ending is considered when searching for symbols. If a symbol with an open position has an ending, only the symbols with the same ending are used for conversion.

Conversion for other instrument types:

-   A conversion currency pair is formed from margin and deposit currencies.
-   The pair for direct conversion is sought. Only pairs in the form of XXXYYY without suffixes are used. For example, if position is opened at GOLD with USD margin currency, while EUR is the deposit currency, the search for EURUSD pair is conducted.
-   If such a pair is found, conversion is performed at an average pair's price at the time of conversion: (Bid + Ask)/2.
-   If such a symbol is not found, an attempt to convert using USD is made. Suppose that we have a position at #LKOH. The margin currency is RUR, while the deposit currency is EUR. If the server has no EURRUR, two symbols (EURUSD and USDRUR) are used for conversion. Thus, the conversion is performed in two stages. At each stage, the average price of an appropriate pair at the time of conversion is used: (Bid + Ask)/2.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Only symbols with the Forex calculation type can be used for conversion. For example, if you have the EURTRY symbol with the Futures calculation type, the platform will not be able to use its prices to convert EUR to TRY.</span></p></td></tr></tbody></table>

## Hedged margin [#](margin_calculation#hedged)

Hedged (covered) positions are the ones opened at the same instrument, but in different directions. The margin for such positions can be calculated in two ways. The calculation method is defined by ["Calculate hedged margin using larger leg"](/en/docs/mt4/administrator/administration/ug_groups#larger_leg) option.

### If the option is disabled (basic calculation)

For each covered lot of a position, the margin is charged according to the value specified in [Hedged](/en/docs/mt4/administrator/administration/ug_symbols#hedged) field of the symbol settings.

If the [initial margin](/en/docs/mt4/administrator/administration/ug_symbols#initial_margin) is set for the symbol, the hedged margin is displayed as an absolute value (in monetary value).

If the initial margin is not set (equal to 0), the contract size is specified in Hedged field. The margin is calculated by the formula corresponding to the instrument type using the specified contract size. For example, there are two positions – Buy EURUSD 1 lot and Sell EURUSD 1 lot, the contract size is 100,000. If 50,000 is set in Hedged field, the margin is charged for both positions as for 1 lot. If it is set to 0, no margin is charged for the covered volume.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If position open price is used in the margin calculation (for example, for CFD), the average open price is used for calculating the margin for covered positions: (Buy open price + Sell open price) / 2.</span></p></td></tr></tbody></table>

### If the option is enabled (using the larger leg)

If "Calculate hedged margin using larger leg" is enabled, the calculation is performed as follows:

-   The volume of all short and long positions for a symbol is calculated.
-   A weighted average open price and a weighted average price of conversion to the deposit currency are calculated for each leg.
-   Then, the margin for short and long legs is calculated using the formulas described above for each symbol type.
-   The biggest value is used as a total one.

Let's consider the following example. We have 3 positions on EURUSD:

-   Buy 2 lot EURUSD at 1.38905
-   Buy 2 lot EURUSD at 1.38605
-   Sell 2 lot EURUSD at 1.38986
-   Sell 1 lot EURUSD at 1.38995

The long leg volume is 4 lots. The short leg volume is 3 lots. The open price is not considered when calculating the margin for Forex symbols. Suppose that the contract size is 100,000, the leverage is 1:100. Now, let's calculate the margin:

-   Margin for the long leg = 4 \* 100,000 / 100 = 4,000
-   Margin for the short leg = 3 \* 100,000 / 100 = 3,000

The total margin value is 4,000.

## Checking Margin [#](margin_calculation#check)

The margin is checked in the following cases:

1.  When a trader places an order for opening a market position.
2.  Additionally, after an order is confirmed for brokers, in case ["Do not check free margin after dealer's answer"](/en/docs/mt4/administrator/administration/ug_groups#margin_dealer_answer) option is disabled for the group in the symbol settings. It is recommended that you enable this option if orders are sent to an external trading system.
3.  For pending orders, the margin is checked at the order's activation. If a trader has insufficient funds for opening a position at the moment the pending order is activated, and processing is performed automatically by a server or manager terminal, the pending order is removed. The relevant message is added to the order and the server journal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Check rules:</span></p><ol><li value="1" class="p_tableatten"><span class="f_tableatten">After an appropriate operation (order) is performed (executed), the trader's free margin considering the <a href="/en/docs/mt4/administrator/administration/ug_groups#credit" class="topiclink">virtual credit</a> should not be negative (it should exceed or be equal to 0).</span></li><li value="2" class="p_tableatten"><span class="f_tableatten">After executing an order, which is opposite to the present position (closing or reversal), the margin should not increase. In fact, it means that a trader can close his or her position or reverse it considering available funds under any circumstances. This rule is applied only if <a href="/en/docs/mt4/administrator/administration/ug_symbols#strong_hedged" class="topiclink">"Strong hedged margin mode"</a> option is disabled in the symbol settings.</span></li></ol><p class="p_tableatten"><span class="f_tableatten">If strong margin check is disabled, the system will allow placing an order if any of the rules is met. If the trader has enough free margin (1), it does not matter if the margin will increase or not (2) — the system will allow placing an order.</span></p><p class="p_tableatten"><span class="f_tableatten">If strong margin check is enabled, the only criterion for placing an order is the availability of the required free margin.</span></p></td></tr></tbody></table>

[Symbols Import](/en/docs/mt4/administrator/administration/ug_symbols/ug_symbols_import)

[Swap Calculation](/en/docs/mt4/administrator/administration/ug_symbols/swap_calculation)