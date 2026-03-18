# Corporate links

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_accounts/corporate_links

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
                -   [Creating Account](/en/docs/mt5/platform/administration/admin_accounts/account_add)
                -   [Editing Account](/en/docs/mt5/platform/administration/admin_accounts/account_edit)
                -   [Preliminary Accounts](/en/docs/mt5/platform/administration/admin_accounts/preliminary_accounts)
                -   [Archive and Backup Bases](/en/docs/mt5/platform/administration/admin_accounts/accounts_archive)
                -   [Import of Accounts from File](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_export)
                -   [Import of Accounts from MetaTrader 5](/en/docs/mt5/platform/administration/admin_accounts/accounts_import_mt)
                -   [Checking and Fixing Balance](/en/docs/mt5/platform/administration/admin_accounts/account_balance_check)
                -   [Account Allocation Settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups)
                -   [Corporate Links](/en/docs/mt5/platform/administration/admin_accounts/corporate_links)
                -   [Links to Depositing and Withdrawing](/en/docs/mt5/platform/administration/admin_accounts/deposit_withdrawal)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Accounts](/en/docs/mt5/platform/administration/admin_accounts)Corporate Links

# Corporate links

Some regulators require brokers to show traders a certain set of agreements and regulatory documents. In particular, one of the NFA requirements is to display a document on providing information about transactions (Transactional Data Request). In order to enable brokers to bring client terminals into compliance with the requirements, the trading platform provides a mechanism for adding custom links.

Set a list of corporate links and they will automatically appear in the desktop, mobile and web client terminal menus.

![Corporate links in client terminals](/en/docs/mt5/platform/img/corporate_links_client.png "Corporate links in client terminals")

Go to "Clients & Accounts \\ Corporate links", add a new entry and specify the settings:

-   Company — name of a company (White Label) displaying the links.
-   Group — group of accounts the links are to be displayed for.
-   Description — description to be displayed in the list of settings.
-   Countries — list of countries the links are to be displayed for. A country is taken from the [account settings](/en/docs/mt5/platform/administration/admin_accounts/account_edit#personal).

Using these settings, you can create different sets of links. They will be displayed depending on what account the client is connected to in the terminal.

![Corporate links to be added to client terminals](/en/docs/mt5/platform/img/corporate_links.png "Corporate links to be added to client terminals")

Specify the agreements and links to them at the bottom. They will be displayed in client terminals.

Use the \[lang\] macro in the links to show to users the agreements in the desired language. The macro substitutes the language identifier into the link depending on the language of the client terminal interface. For example, you can specify the link as follows: https://broker.com/\[lang:en|es|de|zh\]/client\_agreement. If the client uses the English interface of the terminal, the following link will be generated for this user: https://broker.com/en/client\_agreement. For the Spanish interface, the link will be https://broker.com/es/client\_agreement, etc.

Languages are specified in the ISO 639-1 format. The following values are supported: en|ru|es|pt|zh|ar|cs|fr|it|de|el|id|jp|pl|tr. If the interface language does not match any of the values specified in the macro, the first language from the list will be used.

## Settings check order

Link settings are checked from top to bottom. The first suitable setting is applied to the account, while further settings will be ignored. For example, you have created the following sets of links:

1.  Groups: real\\\*; Countries: Spain, France, Portugal
2.  Groups: real\\\*; Countries: USA, Canada
3.  Groups: All; Countries: All

The second set of links will be shown to a real account from Canada. Any account created outside of the real\\\* groups will see the third set of links.

If you change the settings order as follows:

1.  Groups: All; Countries: All
2.  Groups: real\\\*; Countries: Spain, France, Portugal
3.  Groups: real\\\*; Countries: USA, Canada

The first set of links will be shown to all accounts. Sets 2 and 3 will not be used.

[Account Allocation Settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups)

[Links to Depositing and Withdrawing](/en/docs/mt5/platform/administration/admin_accounts/deposit_withdrawal)