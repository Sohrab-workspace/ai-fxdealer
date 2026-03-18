# Start Page

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_start

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Start Page

# Start Page

The start page displays important information about the platform operation: license data, the number of groups, accounts and trading operations. In addition, here you can change live update settings, as well as find a lot of useful information related to platform administration.

To open the start page, select the desired platform on the left side of the terminal.

![Start Page](/en/docs/mt5/platform/img/start_page_platform.png "Start Page")

## Server Data

The following platform data is specified in the page header:

-   Name of the trading platform owner company.
-   Platform name displayed in client terminals. It consists of two parts:

-   Owner company's short name indicated in the license.
-   An additional part as define by you. Here you can specify additional data, such as the server type: demo or live. The short name is set in the "Server Name" field below. After editing the data, click "Apply" on the toolbar to save settings.  
    The additional data must not look like the domain name of the server. For example, do not specify "demo.com", "real.net", etc.

## License Information

The main license details are shown at the top of the page. Here, you will be warned of approaching expiration date or account limit. Separate warnings can be shown if your platform is [not activated](/en/docs/mt5/platform/platform_installation/activation).

-   License — the website of the company for which the trading platform license has been issued.
-   License valid till — license expiration date. For example, if 2021.12.31 is specified, the license is valid until 2021.12.30 23:59:59 trading platform time.  
    If payments are made in a timely manner and your platform is properly connected to the license server (updates.metaquotes.net), the license will be updated automatically. If the license update fails for any reason, the license field will become highlighted in red one month before the license expiration date. In this case please contact the [support team](/en/docs/mt5/platform/support) for renewal. Once the license expires, the platform operation will stop and you will not be able to provide further services to your clients.
-   Symbols — the total number of [symbols](/en/docs/mt5/platform/administration/admin_symbols) in the platform, as well as the limitation according to your license type (if there is any).
-   Groups — the total number of [groups](/en/docs/mt5/platform/administration/admin_groups) in the platform, as well as the limitation according to your license type (if there is any).
-   Real accounts — the total number of real clients in the entire platform, as well as the limitation on the number of clients according to the license (if any). Real accounts are client records that are not included into demo\*, manager\*, preliminary\* and contest\* [groups](/en/docs/mt5/platform/administration/admin_groups/group_types). Only [enabled accounts](/en/docs/mt5/platform/administration/admin_accounts/account_edit#enable) for which [trading is allowed](/en/docs/mt5/platform/administration/admin_accounts/account_edit#trading) are counted.
-   Deals — the number of [deals](/en/docs/mt5/platform/administration/admin_deals) executed in the platform.

## Live update [#](admin_start#update)

The [update](/en/docs/mt5/platform/administration/admin_update) of system components is set in this block:

-   Disabled — no updates to the platform components are performed, either automatically or manually.
-   Enabled — platform components are updated to latest release versions in the automatic mode.
-   Enabled with beta versions — when you launch live update, both release and beta versions of platform components will be installed. Beta versions precede the main release, allowing you to test the new features released in the update, as well as to test the operation of your plugins, gateways and other additional components. This option should only be enabled on test servers. Please make sure not to update your real servers with live accounts up to the beta version.

After editing the data, click "Apply" on the toolbar to save settings.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Make sure your platform is <a href="/en/docs/mt5/platform/platform_installation/activation" class="topiclink">activated</a>. Otherwise, some of its basic features will be limited. If a notification in the upper part of the page shows that the platform is not activated, launch activation using the Services menu.</span></p></td></tr></tbody></table>

## Alerts

Important alerts concerning the platform components are shown in this block:

-   No connection between the [gateway](/en/docs/mt5/platform/administration/admin_gateways) or [data feed](/en/docs/mt5/platform/administration/admin_feeds) and the source. If such an alert appears, please check the gateway or data feed [journal](/en/docs/mt5/platform/administration/admin_gateways/journal_gateway).
-   A [platform component](/en/docs/mt5/platform/components) is not connected. In this case please check if the appropriate service is running in the operating system and check the latest logs in the component's log in the disk.

Please do not ignore alerts.

## Administrator best practices [#](admin_start#best_practice)

This block features useful tips concerning platform operation, which will assist in using the platform to its full capabilities: what components need further setup or verification, how additional symbols can be added and other tips. A click on a tip will open an appropriate Administrator terminal section. After that the advice line will be hidden from the list.

[Import/Export Settings](/en/docs/mt5/platform/administration/common_info/import_export_config)

[Network cluster](/en/docs/mt5/platform/administration/admin_network)