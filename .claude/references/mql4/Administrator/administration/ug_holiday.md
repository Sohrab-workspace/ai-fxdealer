# Holidays

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/administration/ug_holiday

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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Administration](/en/docs/mt4/administrator/administration)Holidays

# Holidays

This section allows to introduce holidays to the working schedule both for each group of instruments (forex, cfd, futures, stocks), and for each individual instrument (EURUSD, USDCHF, #GOLD, etc.). These instructions allow to configure holidays during the workweek easily. On holidays, clients can connect to the system, watch charts and bid histories, but they cannot perform any trade operations.

![Holidays](/en/docs/mt4/administrator/img/br_holiday.png "Holidays")

When adding a holiday or changing the rules of work on that day (the "Add" è "Edit" commands respectively) you will see the setting window:

![Holidays](/en/docs/mt4/administrator/img/win_holiday.png "Holidays")

To enable/disable the holiday check/unchek the "Enable" box. Tick the "Every Year" field if the holiday repeats every year. You should indicate the year for other holidays. If market works for several hours on a holiday, you should indicate the working hours in the "Work time" additionally. The name of a financial instrument or that of a group of instruments will be stored in the "Symbol" field ("All" means all financial instruments), and holiday — will be described in the "Description" field.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Quotes transmission and trading continues until the last minute of the work time range inclusive. For example, if the work time is from 00:00 to 18:00, then the actual work time is 00:00:00 — 18:00:59.</span></p></td></tr></tbody></table>

## Holidays Check

Holiday rules are checked from top downward. The check is stopped at the first permissive rule for the specified symbol-time pack. Let's consider the following example:

![Example of Holidays setup](/en/docs/mt4/administrator/img/holidays_example.png "Example of Holidays setup")

The following rules are set:

-   The first rule prohibits trading all symbols on January 1, 2014
-   The second one allows trading Forex group symbols from 10:00 to 12:00 on that day
-   The third one allows trading the same symbols from 13:00 to 22:00
-   The fourth one prohibits trading all symbols on January 1, 2014

As a result, trading Forex group symbols will be allowed from 10:00 to 12:00 and from 13:00 to 22:00 on January 1, 2014. The fourth rule is ignored, as the check stops at the first one that permits trading. Thus, in order to set several trading intervals inside one time interval, you should first set a prohibitive rule followed by permissive ones.

[Time](/en/docs/mt4/administrator/administration/ug_time)

[Symbols](/en/docs/mt4/administrator/administration/ug_symbols)