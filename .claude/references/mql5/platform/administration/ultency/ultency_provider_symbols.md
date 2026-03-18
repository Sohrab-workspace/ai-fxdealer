# Provider Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols

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
                -   [Connection](/en/docs/mt5/platform/administration/ultency/ultency_connect)
                -   [Provider Symbols](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols)
                -   [Aggregated Symbols](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols)
                -   [Translations of Symbols and Quotes](/en/docs/mt5/platform/administration/ultency/ultency_translations)
                -   [Routing](/en/docs/mt5/platform/administration/ultency/ultency_routing)
                -   [Order Execution](/en/docs/mt5/platform/administration/ultency/ultency_execution)
                -   [Matching Orders](/en/docs/mt5/platform/administration/ultency/ultency_matching_orders)
                -   [Liquidity Orders](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_orders)
                -   [Deals](/en/docs/mt5/platform/administration/ultency/ultency_deals)
                -   [Ticks](/en/docs/mt5/platform/administration/ultency/ultency_ticks)
                -   [Execution Books](/en/docs/mt5/platform/administration/ultency/ultency_execution_books)
                -   [Control and Reporting](/en/docs/mt5/platform/administration/ultency/ultency_reporting)
                -   [Service Desk](/en/docs/mt5/platform/administration/ultency/ultency_service_desk)
                -   [Become a Provider](/en/docs/mt5/platform/administration/ultency/ultency_liquidity_offers)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Ultency](/en/docs/mt5/platform/administration/ultency)Provider Symbols

# Provider Symbols

Ultency imports financial instrument settings from liquidity providers and subsequently uses them for price data aggregation and order execution routed to the provider.

## Common [#](ultency_provider_symbols#common)

![Common settings of the aggregate symbol](/en/docs/mt5/platform/img/ultency_provider_symbols.png "Common settings of the aggregate symbol")

The following settings are available in the "Common" section:

-   Basis symbol — the name of the instrument associated with the symbol received from a provider. It is used to link the provider's instrument to an aggregated symbol.  
       
    Each aggregated symbol must have a designated [basis symbol](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#basis), which defines the instrument for which data is collected, as well as the list of providers whose data should be aggregated. Ultency scans all selected providers and aggregates data from instruments with the specified basis symbol. The basis symbol is also used for [routing the requests](/en/docs/mt5/platform/administration/ultency/ultency_routing).  
       
    A single provider cannot have multiple symbols with the same basis symbol.  
       
    To bulk modify or remove a basis symbol, select the desired records, click "Edit" in the menu, and then specify or delete the postfix in the corresponding field. The postfix must begin with a period (.). For example, if you select records with the basis symbols EURUSD, USDJPY, and GBPUSD and add a postfix .x (EURUSD.x) in the bulk editing window, all three base symbols will be changed to EURUSD.x, USDJPY.x, and GBPUSD.x, respectively.  
     
-   Source symbol — the name of the instrument on the provider side. This field is populated automatically when the provider is connected.
-   Coverage symbol — a symbol used to duplicate all trades executed through this provider.
-   Description — a brief description of the symbol.
-   Digits — the number of decimal places in the symbol prices. This is used for indication only on the provider's side. Prices are rounded only when [transmitted to MetaTrader 5](/en/docs/mt5/platform/administration/ultency/ultency_translations), while Ultency works with prices according to the original number of digits from the liquidity provider.
-   Market depth — the number of price levels (on each side) to be transmitted for this symbol. Other levels will be excluded from the aggregated book. If Market depth is disabled on Ultency or provider side, ticks for this symbol will be processed with the maximum execution volume specified in the [settings](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols#volume_max) and participate in order matching and B-Book book formation by [levels](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols#bands).

-   Market depth volume — units in which the liquidity provider delivers volume for the order book.  
       
    A data provider can send volumes as the number of lots (contracts) or as monetary amounts. In this field, you can explicitly specify how Ultency will interpret volume data.  
       
    By default, these values are interpreted in accordance with the [profit and margin calculation types](/en/docs/mt5/platform/administration/ultency/ultency_provider_symbols#calculation) used for the symbol.  
     
    -   For the Forex type, the volume is interpreted as the number of units of the symbol's base currency.
    -   For all other types — as the number of contracts (lots).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A liquidity provider must not have multiple instruments with the same basis symbol. For example, a regular EURUSD symbol and a similar symbol with different settings and an additional suffix in the name (EURUSD.x, etc.). This may cause errors or undefined behavior in Ultency. If duplicate symbols are available for the account used for <a href="/en/docs/mt5/platform/administration/ultency/ultency_connect#connect" class="topiclink">connecting to the provider</a>, contact the provider to ensure only one set is available.</span></p></td></tr></tbody></table>

## Currency [#](ultency_provider_symbols#currency)

The parameters in this section are informational and should not be modified. They reflect how the liquidity provider handles transactions and which settings they use.

-   Base currency — the base currency of the instrument.
-   Profit currency — the currency in which profits from trades on this symbol will be [calculated](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/profit_calculation).
-   Margin currency — the currency used to [calculate margin requirements](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation) for the symbol.

![Instrument currency settings](/en/docs/mt5/platform/img/ultency_provider_symbols_currency.png "Instrument currency settings")

## Quotes [#](ultency_provider_symbols#quotes)

This section defines settings for receiving quotes from the provider:

![Settings for receiving quotes from the provider](/en/docs/mt5/platform/img/ultency_provider_symbols_quotes.png "Settings for receiving quotes from the provider")

Specify the following parameters:

-   Enable — enables reception of quotes and depth of market for the symbol.
-   Bid markup — the number of points to adjust the Bid price received from the provider before passing it to the aggregated symbol. Positive values increase the prices, while negative values decrease them. The value is in points of the source symbol's price.
-   Ask markup — the number of points to adjust the Ask price received from the provider before passing it to the aggregated symbol. Positive values increase the prices, while negative values decrease them. The value is in points of the source symbol's price.

### Price Filtering

Filters are used to control the correctness of quotes from the liquidity provider:

-   Deviation — maximum allowed difference (in points) between the received price and the previous or average price (if "Moving average" is non-zero). Prices exceeding this deviation are discarded.
-   Moving average — number of previous prices used to calculate the average. If the current price deviates from this average by more than the "Deviation" value, it is discarded. A zero value means the current price is compared to the last price.
-   Liquidity providers — a list of liquidity providers whose prices are used to cross-check quotes from the current provider. When receiving a quote, the system will compare it with the latest price for the same basis symbol from the specified providers. If the price differs by more than the "Deviation" value, it is automatically discarded.

## Trading [#](ultency_provider_symbols#trading)

The parameters in this section are informational and should not be modified. They reflect how the liquidity provider handles transactions and which settings they use.

If necessary, you can only narrow the settings within the limits allowed by the provider. For example, you can disable one of the supported execution modes (but not enable the unsupported one) or increase the minimum volume.

![Symbol trading settings](/en/docs/mt5/platform/img/ultency_provider_symbols_trade.png "Symbol trading settings")

The following settings are available:

-   Contract size — the amount of the base asset per lot/contract (for currency pairs it is actually the value of one lot in the base currency of the instrument).
-   Calculation — symbol [margin requirements](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/margin_calculation/margin_forex) and [profit](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade/profit_calculation) calculation type. This parameter also affects the calculation of [swaps](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps).
-   Filling — additional [order filling rules](/en/docs/mt5/platform/administration/common_info/general_concept#fill_policy) that can be specified in Ultency. To allow a particular fill type, check the relevant box:
    -   Fill or Kill — order can only be executed in the specified volume.
    -   Immediate or Cancel — order can be executed in the maximum volume available in the market within the requested volume. If the request cannot be filled in full, an order with the available volume will be executed, and the remaining volume will be canceled.
    -   Passive — order is only placed in the market depth. If the order can be filled immediately when placed, this order is canceled.
    -   Return — this mode is not available in the list. It is always allowed for market orders (Buy and Sell) in the "Exchange execution" mode and for [limit and stop-limit orders](/en/docs/mt5/platform/administration/common_info/general_concept#pending_order) in the "Market Execution" and "Exchange Execution" modes.
-   Expiration — order expiration conditions. To allow an expiration type, check the relevant box:
    -   Good Till Canceled — the order will remain in the queue until it is canceled manually.
    -   Day — the order will be valid only during the current trading day. When processed on the MetaTrader 5 platform side, day orders are removed at the end of the calendar day (24 hours) taking into account [trading server time](/en/docs/mt5/platform/administration/admin_time) and symbol [trading sessions](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions). For example, if trading ends at 21:00, untriggered day orders will be canceled at the same time. When orders are processed in external systems via [gateways](/en/docs/mt5/platform/administration/admin_gateways), the expiration rules can be different and depend on the specific system.
    -   Specified time — the order will be valid until the specified date.
    -   Specified day — the order will be valid until 00:00 of the specified day. If outside a trading session, it will expire at the next available session.
-   Orders — allowed order types: Market, Limit, Stop, Stop Limit, Stop Loss, Take Profit, Close By. Enabling Close By orders does not affect [netting accounts](/en/docs/mt5/platform/administration/admin_groups/group_position#netting), as Close By orders can only be used on [hedging accounts](/en/docs/mt5/platform/administration/admin_groups/group_position#hedging).
-   Minimum volume — minimum order size for the symbol. The parameter is ignored when closing positions.
-   Maximum volume — maximum order size for the symbol. Applied when placing orders and when closing positions by [Stop Out](/en/docs/mt5/platform/administration/admin_groups/groups_settings#stopout).
-   Volume step — volume change step.
-   Volume limit — maximum total volume of an open position and pending orders in one direction (buy or sell) per one symbol. For example, a limit of 5 lots allows you to have an open 5-lot position and place a 5-lot Sell Limit order. But in this case, placing a pending Buy Limit order is not allowed, since the total volume in one direction would exceed the limit. Also, if there is a 5-lot Buy position, Ultency cannot place a Sell Limit order with a volume exceeding 5 lots: if the pending order triggered after the closing of the initial position, the system would have a short position exceeding the specified limit.

## Execution [#](ultency_provider_symbols#execution)

![Execution settings for the symbol](/en/docs/mt5/platform/img/ultency_provider_symbols_execution.png "Execution settings for the symbol")

The section defines additional execution parameters for orders routed to the liquidity provider.

### Maximum deviation [#](ultency_provider_symbols#maximum_deviation)

This parameter is only used when operations are sent as Instant Execution and Request Execution orders.

In case of an instant execution, an acceptable deviation is specified in the request sent to the external provider.

When a requote from an external provider is received, Ultency checks if the new price is within the specified deviation. If so, Ultency sends a new request to the provider with the prices from the requote. If the provider accepts the prices, the request is executed. In case of a repeated requote, the deviation will be checked according to the first request (i.e. the price of the original order).

If deviation is exceeded, execution is stopped, and the order is rejected.

### Execution Type

[Execution type](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_execution) for the symbol on the liquidity provider side. The parameter is displayed for information purposes only and cannot be modified.

## Margin [#](ultency_provider_symbols#margin)

The parameters in this section are informational and should not be modified. They reflect how the liquidity provider handles transactions and which settings they use. These settings are also used to calculate the coverage account margin to align conditions with the liquidity provider's terms.

When trading on the MetaTrader 5 side, your clients will use the same [margin settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin) in your platform. Align them with the providers' settings to avoid increased risks.

![Symbol margin settings](/en/docs/mt5/platform/img/ultency_provider_symbols_margin.png "Symbol margin settings")

## Margin Rates [#](ultency_provider_symbols#margin_rates)

The parameters in this section are informational and should not be modified. They reflect how the liquidity provider handles transactions and which settings they use. These settings are also used to calculate the coverage account margin to align conditions with the liquidity provider's terms.

When trading on the MetaTrader 5 side, your clients will use the same [margin settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin_rates) in your platform. Align them with the providers' settings to avoid increased risks.

![Margin Rates settings](/en/docs/mt5/platform/img/ultency_provider_symbols_margin_rates.png "Margin Rates settings")

## Swaps [#](ultency_provider_symbols#swaps)

The parameters in this section are informational and cannot be modified. They reflect how the liquidity provider handles transactions and which settings they use. These settings are also used to calculate the [coverage account](/en/docs/mt5/platform/administration/ultency/ultency_reporting#coverage) swaps to align conditions with the liquidity provider's terms.

![Swap settings](/en/docs/mt5/platform/img/ultency_provider_symbols_swaps.png "Swap settings")

The following settings are available:

-   Type — swap charging type.
-   Long positions — swap for Buy positions.
-   Short positions — swap for Sell positions.
-   Days in year — the number of days in a year to be used for [swap percent calculation](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps#percentage). Depending on the country and market in which the broker operates, as well as on the financial instrument type, different [number of days in a year](https://en.wikipedia.org/wiki/Day_count_convention) can be used when calculating annual percent. This parameter operates with such calculation specifics. The most common option of 360 days is used by default. You can change the value to 365 or 366, as well as specify a different value manually.
-   Swap multipliers — swap multiplier for each day of the week. This multiplier will be applied to the calculated swap value before charging. Specify 1 to charge the regular amount, 3 for triple swap or 0 to cancel swap.

Detailed information is available in the "[Symbols \\ Swaps](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_swaps)" section.

## Sessions [#](ultency_provider_symbols#sessions)

This section contains the provider's default quoting and trading sessions. You may narrow (but not expand) these sessions to restrict quoting and order routing.

![Configuring symbol sessions](/en/docs/mt5/platform/img/ultency_provider_symbols_sessions.png "Configuring symbol sessions")

Click on a day to adjust its session settings:

![Intraday session settings](/en/docs/mt5/platform/img/ultency_provider_symbols_sessions_edit.png "Intraday session settings")

To configure the time of quote and trading sessions separately, enable the corresponding option. Next, set up the sessions. The sliders that control session beginning and end times can be moved with the mouse and with the arrow keys. You can hold down the Shift key to slow down the slider speed. This enables precision of up to minutes when configuring sessions.

If the symbol should only be available for a specific time, set From and To parameters. Outside this range, trading will be [disabled](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#trade_disabled) for this symbol. Clients will receive a "Trading disabled" message upon attempting to place orders.

[Connection](/en/docs/mt5/platform/administration/ultency/ultency_connect)

[Aggregated Symbols](/en/docs/mt5/platform/administration/ultency/ultency_aggregated_symbols)