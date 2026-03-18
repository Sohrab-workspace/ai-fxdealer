# Configuration of Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_symbol

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
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
            -   [Common](/en/docs/mt5/api/config_common)
            -   [Network](/en/docs/mt5/api/config_network)
            -   [Plugins](/en/docs/mt5/api/config_plugins)
            -   [Data Feeds](/en/docs/mt5/api/config_datafeeds)
            -   [Time](/en/docs/mt5/api/config_time)
            -   [Holidays](/en/docs/mt5/api/config_holiday)
            -   [Firewall](/en/docs/mt5/api/config_firewall)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
                -   [IMTConSymbol](/en/docs/mt5/api/config_symbol/imtconsymbol)
                -   [IMTConSymbolSession](/en/docs/mt5/api/config_symbol/imtconsymbolsession)
                -   [IMTConSymbolArray](/en/docs/mt5/api/config_symbol/imtconsymbolarray)
                -   [IMTConSymbolSink](/en/docs/mt5/api/config_symbol/imtconsymbolsink)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
            -   [Floating Margin](/en/docs/mt5/api/config_leverage)
            -   [Managers](/en/docs/mt5/api/config_manager)
            -   [History Synchronization](/en/docs/mt5/api/config_historysync)
            -   [Gateways](/en/docs/mt5/api/config_gateway)
            -   [Routing](/en/docs/mt5/api/config_route)
            -   [Reports](/en/docs/mt5/api/config_report)
            -   [Mail Servers](/en/docs/mt5/api/config_email)
            -   [Messengers](/en/docs/mt5/api/config_messenger)
            -   [Automations](/en/docs/mt5/api/config_automation)
            -   [VPS](/en/docs/mt5/api/config_vps)
            -   [KYC](/en/docs/mt5/api/config_kyc)
            -   [Subscriptions](/en/docs/mt5/api/config_subscription)
            -   [Funds and ETF](/en/docs/mt5/api/config_funds)
            -   [Additional Parameters](/en/docs/mt5/api/config_param)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Symbols

# Configuration of Symbols

The MetaTrader 5 API allows to manage Symbols in the trading platform — add new groups, modify and delete existing ones.

The following symbol interfaces are available:

-   [IMTConSymbol](/en/docs/mt5/api/config_symbol#imtconsymbol)
-   [IMTConSymbolSession](/en/docs/mt5/api/config_symbol#imtconsymbolsession)
-   [IMTConSymbolArray](/en/docs/mt5/api/config_symbol/imtconsymbolarray)
-   [IMTConSymbolSink](/en/docs/mt5/api/config_symbol#imtsymbolsink)

The below figure shows different elements of symbol configuration in the MetaTrader 5 Administrator, to help you understand the purpose of the interfaces:

![Configuration of symbols in MetaTrader 5 Administrator](/en/docs/mt5/api/img/symbols.png "Configuration of symbols in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [Symbol name](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_symbol).
2.  [Symbol description](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_description).
3.  [Symbol type](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_calcmode) (type of profit and margin calculation).
4.  [Symbol execution type](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_execmode).
5.  [Number of decimal places in the symbol price](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_digits).

Below is a detailed description of the correspondence of methods and symbol settings in the MetaTrader 5 Administrator.

## IMTConSymbol [#](config_symbol#imtconsymbol)

The [IMTConSymbol](/en/docs/mt5/api/config_symbol/imtconsymbol) interface provides access to configuration of all the symbol parameters. In MetaTrader 5 Administrator, symbol settings are divided into several tabs:

-   [Common](/en/docs/mt5/api/config_symbol#common)
-   [Quotes](/en/docs/mt5/api/config_symbol#quotes)
-   [Trade](/en/docs/mt5/api/config_symbol#trade)
-   [Execution](/en/docs/mt5/api/config_symbol#execution)
-   [Margin](/en/docs/mt5/api/config_symbol#margin)
-   [Swaps](/en/docs/mt5/api/config_symbol#swaps)
-   [Sessions](/en/docs/mt5/api/config_symbol#sessions)

### Common [#](config_symbol#common)

![The "Common" tab](/en/docs/mt5/api/img/symbols_common.png "The "Common" tab")

The following elements are shown above:

1.  [Symbol name](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_symbol).
2.  International Securities Identification Number ([ISIN](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_isin)).
3.  [Underlying asset](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_basis).
4.  [The source of quotes for the symbol](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_source).
5.  [The background color of the symbol](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_colorbackground).
6.  [The amount of spread](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_spread).
7.  [Spread balance](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_spreadbalance).
8.  [Symbol description](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_description).
9.  [International Securities Identification Number](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_international).
10.  [The address of the symbol web page](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_page).
11.  [Number of decimal places in the symbol price](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_digits).
12.  [The range of the Depth of Market](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_tickbookdepth).
13.  [Base currency](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_currencybase).
14.  [Profit currency](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_currencyprofit).
15.  [Margin currency](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_currencymargin).

### Quotes [#](config_symbol#quotes)

![The "Quotes" tab](/en/docs/mt5/api/img/symbols_filtration.png "The "Quotes" tab")

The following elements are shown above:

1.  [Allow real time quotes from data feeds](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_tickflags).
2.  [Keep original prices](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_tickflags).
3.  [Receive market statistics from data feeds](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_tickflags).
4.  [Soft filtration level](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filtersoft).
5.  [The number of quotes to set a new level](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filtersoftticks).
6.  [Hard filtration level](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filterhard).
7.  [The number of quotes to set a new level](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filterhardticks).
8.  [Discard filtration level](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filterdiscard).
9.  [Minimum spread](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filterspreadmin).
10.  [Maximum spread](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_filterspreadmax).

### Trade [#](config_symbol#trade)

![The "Trade" tab](/en/docs/mt5/api/img/symbols_trade.png "The "Trade" tab")

The following elements are shown above:

1.  [Contract size](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_contractsize).
2.  [Method of profit and margin calculation](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_calcmode).
3.  [Trade settings](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_trademode).
4.  [Mode of keeping orders at a trade day change](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_gtcmode).
5.  [Filling types](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_fillflags).
6.  [Expiration types](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_expirflags).
7.  [Allowed types of order](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_orderflags).
8.  [Stop and Limit levels](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_stopslevel).
9.  [Freeze level](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_freezelevel).
10.  [Maximum delay of quotes](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_quotestimeout).
11.  [Mode of profit conversion for Forex symbols](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_enum#entradeflags).
12.  [Minimal volume](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_volumemin).
13.  [Volume change step](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_volumestep).
14.  [Maximal volume](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_volumemax).

### Execution [#](config_symbol#execution)

![The "Execution" tab](/en/docs/mt5/api/img/symbols_execution.png "The "Execution" tab")

The following elements are shown above:

1.  [Execution type](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_execmode).
2.  [Maximum time deviation](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_ietimeout).
3.  [Maximum price deviation in the profitable direction](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_ieslipprofit).
4.  [Maximum price deviation in the losing direction](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_iesliplosing).
5.  [Maximal volume](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_ievolumemax).

### Margin [#](config_symbol#margin)

![The "Margin" tab](/en/docs/mt5/api/img/symbols_margin.png "The "Margin" tab")

The following elements are shown above:

1.  [The size of the initial margin](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_margininitial).
2.  [The size of the maintenance margin](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginmaintenance).
3.  [The mode of checking margin](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginflags).
4.  [The initial margin rate](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginrateinitial).
5.  [The maintenance margin rate](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_marginratemaintenance).

### Swaps [#](config_symbol#swaps)

![The "Swaps" tab](/en/docs/mt5/api/img/symbols_swaps.png "The "Swaps" tab")

The following elements are shown above:

1.  [An option for enabling/disabling swap charging](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_swapmode).
2.  [Type of swap charging](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_swapmode).
3.  [The swap size for long positions](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_swaplong).
4.  [The swap size for short positions](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_swapshort).
5.  [The day to charge triple swap](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_swap3day).

### Sessions [#](config_symbol#sessions)

![The "Sessions" tab](/en/docs/mt5/api/img/symbols_sessions.png "The "Sessions" tab")

The following elements are shown above:

1.  [Quoting sessions](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_sessionquoteadd).
2.  [Trading sessions](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_sessiontradeadd).
3.  [The start date of a symbol's validity period](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_timestart).
4.  [The end date of a symbol's validity period](/en/docs/mt5/api/config_symbol/imtconsymbol/imtconsymbol_timeexpiration).

## IMTConSymbolSession [#](config_symbol#imtconsymbolsession)

The [IMTConSymbolSession](/en/docs/mt5/api/config_symbol/imtconsymbolsession) interface provides access to the parameters of trading and quoting sessions of a symbol.

![Symbol Sessions](/en/docs/mt5/api/img/symbol_sessions.png "Symbol Sessions")

The figure shows the sessions configuration dialog in MetaTrader 5 Administrator:

1.  [Session beginning](/en/docs/mt5/api/config_symbol/imtconsymbolsession/imtconsymbolsession_open).
2.  [Session end](/en/docs/mt5/api/config_symbol/imtconsymbolsession/imtconsymbolsession_close).

## IMTConSymbolSink [#](config_symbol#imtsymbolsink)

The [IMTConSymbolSink](/en/docs/mt5/api/config_symbol/imtconsymbolsink) interface contains the handlers of he events of symbol configuration changes.

[OnFirewallSync](/en/docs/mt5/api/config_firewall/imtconfirewallsink/imtconfirewallsink_onfirewallsync)

[IMTConSymbol](/en/docs/mt5/api/config_symbol/imtconsymbol)