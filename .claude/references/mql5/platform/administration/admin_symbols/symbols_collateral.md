# Collateral Symbols

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/symbols_collateral

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
                -   [Symbol Settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings)
                -   [Splicing Futures](/en/docs/mt5/platform/administration/admin_symbols/symbols_splice)
                -   [Import of Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_import)
                -   [Collateral Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_collateral)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Symbols](/en/docs/mt5/platform/administration/admin_symbols)Collateral Symbols

# Collateral Symbols

The trading platform supports a special type of non-tradable assets, which can be used as client's assets to provide the required margin for open positions of other instruments. For example, a certain amount of gold in physical form can be available on a trader's account, which can be used as a margin (collateral) for open positions.

Such instruments have [calculation type "Collateral"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#calculation). Features of such symbols:

-   Clients can't perform any operations with these symbols, except for closing. A position can be opened only by a manager.
-   No profit can be accrued for the positions of these symbols, they have no stop loss or take profit.
-   The value of such a position, and thus the amount of money that a client can use as collateral, is calculated by the below formula:

Such assets are displayed as open positions. Their value is calculated by the formula: Contract size \* Lots \* Market Price \* Liquidity Rate.

Liquidity Rate is the share of the asset that a broker allows to use for the margin, it is set in the [symbol properties](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_margin).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For groups with the risk management mode <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk" class="topiclink">"for Stock Exchange, based on margin discount rates"</a>, the current Last price is used for Market Price, instead of Bid and Ask.</span></p></td></tr></tbody></table>

The Assets are added to the client's Equity and increase Free Margin, thus increasing the volumes of allowable trade operations on the account.

![Trader's assets in the client terminal](/en/docs/mt5/platform/img/assets.png "Trader's assets in the client terminal")

In the example above, a trader has 1 ounce of gold having the current market value of 1 210.56 USD. This value is added to the equity and the free margin.

[Symbol settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#trade_disabled) may allow clients and managers close such positions (Trade = Close only). In this case a trader will be able to convert the asset in the deposit currency at the current market rate and use that money for trading. A position can be closed only if the conversion rate of the assets currency into the deposit currency is available.

## Charging a client account

An asset can be added to a client account via the manager terminal or gateways. For example, [MetaTrader 5 Gateway to MOEX Securities](/en/docs/mt5/platform/components/gateways/moex_securities) supports importing the clients' money limits in currencies other than the ruble as Collateral positions.

## Configuring collateral symbols

Create a separate symbol group via the Administrator terminal and then create a currency symbol in it. Select "Collateral symbol currency" — "Client deposit currency" pair as a quote source for it.

![Configuring collateral symbols](/en/docs/mt5/platform/img/collateral_setup_1.png "Configuring collateral symbols")

Next:

-   Set Collateral for the symbol type
-   Disable trading for the symbol
-   Set contract size 1 to let the price be displayed down to the last cent
-   Specify zero size and tick value
-   Specify the liquidity margin rate - amount of the current value of an asset, which will be taken into account as collateral
-   Remove all margin ratios (set zero values)

![Configuring collateral symbols](/en/docs/mt5/platform/img/collateral_setup_2.png "Configuring collateral symbols")

[Import of Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_import)

[Spreads](/en/docs/mt5/platform/administration/spreads)