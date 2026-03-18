# Contract Specification

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/service/symbol_spec

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
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
            -   [Configuration at Startup](/en/docs/mt4/terminal/service/start_conf_file)
            -   [History Center](/en/docs/mt4/terminal/service/history_center)
            -   [Export of Quotes](/en/docs/mt4/terminal/service/dde)
            -   [Global Variables](/en/docs/mt4/terminal/service/global_variables)
            -   [Contract Specification](/en/docs/mt4/terminal/service/symbol_spec)
            -   [Languages Support](/en/docs/mt4/terminal/service/languages_support)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Tools](/en/docs/mt4/terminal/service)Contract Specification

# Contract Specification

![contract_specification](/en/docs/mt4/terminal/img/contract_specification.png)

This message window allows to view securities contract specifications. The main parameters are grouped in table with following fields:

-   Spread — difference between Bid and Ask prices in points;
-   Digits — the amount of digits after decimal point in the price representation;
-   Stops level — minimum distance to the current price in points at which [Stop Loss and Take Profit orders](/en/docs/mt4/terminal/positions/orders#stop_loss) can be placed;
-   Pendings are good till cancel — forced closing of pending orders at the end of a session. "Yes" means that pending orders will not be closed forcedly;
-   Contract size — one-lot price in deposit currency;
-   Tick price — the size of minimal price change in quote currency;
-   Tick size — minimal symbol price change interval in points;
-   Profit calculation mode — accepted profit calculation technique (Forex, Contracts, Futures);
-   Swap type — rollover calculation type (in points, in deposit currency, or in per cents);
-   Swap long — rollover size for a long position;
-   Swap short — rollover size for a short position;
-   Margin calculation mode — accepted free margin calculation technique (Forex, Contracts, Futures)
-   Margin hedge — size of margin for hedged positions.

The symbol specification window can be called by pressing of "Properties" button in the [Market Watch window](/en/docs/mt4/terminal/overview/market_watch#symbols) or the "Symbol properties" of the ["Tester — Settings" window](/en/docs/mt4/terminal/overview/strategy_tester/strategy_tester_setup).

[Global Variables](/en/docs/mt4/terminal/service/global_variables)

[Languages Support](/en/docs/mt4/terminal/service/languages_support)