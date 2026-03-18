# Payments in Client Terminals

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/payments/payments_clients

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
                -   [Payment Gateways](/en/docs/mt5/platform/administration/payments/payments_wallets)
                -   [Payment Processing Rules](/en/docs/mt5/platform/administration/payments/payments_rules)
                -   [Controlling Payments](/en/docs/mt5/platform/administration/payments/payments_operations)
                -   [Processing Payments](/en/docs/mt5/platform/administration/payments/payments_processing)
                -   [Payments in Client Terminals](/en/docs/mt5/platform/administration/payments/payments_clients)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Payments](/en/docs/mt5/platform/administration/payments)Payments in Client Terminals

# Payments in Client Terminals

After you configure payments on the trading server side, a special section will appear in the client terminals, from where your traders will be able to make deposits and withdrawals.

![Payments in the client terminal](/en/docs/mt5/platform/img/payments_terminal.png "Payments in the client terminal")

In addition to deposit and withdrawal options, the section displays the history of all transactions completed through the payment system. Pending [invoices for depositing via a bank transfer](/en/docs/mt5/platform/administration/payments/payments_wallets/payments_bank_transfer#deposit) can be downloaded as a PDF file.

Transaction specifics:

-   Transactions are always associated with the currently connected account. To deposit or withdraw funds from another account, the user must first connect to it.
-   The payments section is only available for real accounts and is not shown for other account types.
-   The list of available payment methods is determined by the gateway settings. You can configure access based on [groups](/en/docs/mt5/platform/administration/payments/payments_wallets#groups) and [countries](/en/docs/mt5/platform/administration/payments/payments_wallets#countries).
-   Payment settings take precedence over [settings of links to deposit and withdrawal pages](/en/docs/mt5/platform/administration/admin_accounts/deposit_withdrawal). If payments are configured in the platform, all deposit and withdrawal commands will open the payments section rather than external pages.

Find detailed info on using the payment system on the client terminal side in the appropriate manuals:

-   [MetaTrader 5 for desktops](https://www.metatrader5.com/en/terminal/help/startworking/payments)
-   [MetaTrader 5 for iPhone/iPad](https://www.metatrader5.com/en/mobile-trading/iphone/help/settings_accounts/payments)
-   [MetaTrader 5 for Android](https://www.metatrader5.com/en/mobile-trading/android/help/settings_accounts/payments)

[Processing Payments](/en/docs/mt5/platform/administration/payments/payments_processing)

[Managers](/en/docs/mt5/platform/administration/admin_managers)