# Synchronization Features

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_synchronization/synchronization_features

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
                -   [Synchronization Features](/en/docs/mt5/platform/administration/admin_synchronization/synchronization_features)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)Synchronization Features

# Synchronization Features

There are some specific features of synchronization that should be taken into account before you start this process.

## Specifics of synchronization of MetaTrader 5 and MetaTrader 4 servers [#](synchronization_features#features)

![Synchronization diagram](/en/docs/mt5/platform/img/synchronization_scheme.png "Synchronization diagram")

There is a considerable difference between synchronization with MetaTrader 4 and MetaTrader 5 servers.

-   History data in MetaTrader 5 are stored only as 1 minute data and are converted to larger timeframes by request in the client terminal. In MetaTrader 4 different timeframes are stored.
-   During synchronization with MetaTrader 4 servers, the successive selection of the most complete data starting from 1 minute timeframe is performed. First all M1 data are taken. Then it tries to obtain the missing part from H1 data. The hour value of the MetaTrader 4 server is written for the first minute on the MetaTrader 5 server. Then an attempt is made to obtain missing data from D1 timeframe. The daily data of MetaTrader 4 (e.g. 01.03.2009) are written for the first minute of the day of MetaTrader 5 (e.g. 01.03.2009 00:00). Therefore, clients can get a complete chart for the history period only on the timeframe, from which the data were imported.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To synchronize data with the MetaTrader 4 server, at least one <a href="/en/docs/mt5/platform/administration/admin_groups/group_types#demo" class="topiclink">demo group</a> should be available on it. The group can be disabled.</span></p></td></tr></tbody></table>

## Time zone correction [#](synchronization_features#time_zone)

[Synchronization settings](/en/docs/mt5/platform/administration/admin_synchronization#time_zone) provide the special function of correcting time zones. It allows to easily synchronize history data by MetaTrader servers located in different time zones. There are two variants of operation of this function:

-   Auto detect  
    If this variant is selected, the time difference will be detected automatically. Besides, it will also be detected, whether the option of [Daylight saving time](/en/docs/mt5/platform/administration/admin_time#daylight_saving) is enabled on both servers. This parameter is taken into account only when small parts of history data are synchronized, because switch to DST may differ in different countries. At the synchronization of larger parts of data, the current time shift (+1 hour if it has been performed already) and is added to the time zone difference. History data are synchronized with the difference by the obtained time shift.
-   Setting a precise correction  
    When this variant is chosen, history data will be shifted strictly by this value, not taking into account the DST.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">To synchronize larger periods of history data we recommend using servers with disabled DST switch.</span></p></td></tr></tbody></table>

[Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)

[Subscriptions](/en/docs/mt5/platform/administration/subscriptions)