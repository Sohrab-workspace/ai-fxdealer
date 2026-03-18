# Migration

> Source: https://support.metaquotes.net/en/docs/mt5/client/virtual_hosting_migration

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
            -   [Register a Server](/en/docs/mt5/client/virtual_hosting_server)
            -   [Migration](/en/docs/mt5/client/virtual_hosting_migration)
            -   [Working with the Virtual Platform](/en/docs/mt5/client/virtual_hosting_terminal)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)Migration

# Migration

Migration is transferring the current active environment from the trading platform to the virtual one. This is a simple and straightforward way to change the set of launched programs, open charts and subscription parameters in the virtual platform.

## Preparing for Migration

Before you launch a virtual platform, prepare an active environment for it — charts, running indicators and Expert Advisors, Signal copying parameters and platform settings.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/NGSHrX-QAOU/video.mp4" target="_blank" title="Watch video: Preparing to migrate robots and signals"><img class="help" alt="Watch video: Preparing to migrate robots and signals" title="Watch video: Preparing to migrate robots and signals" width="142" height="80" src="/en/docs/mt5/client/img/video_hosting_migrate.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Preparing migration of robots and signals</span></p><p class="p_fortable"><span class="f_fortable">How to setup a trading environment, in order to execute your trading robots and signals on a virtual platform for 24 hours a day?</span></p></td></tr></tbody></table>

### Charts and Market Watch

In the [Market Watch](/en/docs/mt5/client/market_watch) window, set up the list of symbols critical for your Expert Advisors' operation. We recommend that you remove all unnecessary symbols to decrease the tick traffic received by the platform. There is no point in keeping hundreds of symbols in the Market Watch if only a couple of them are used for trading.

Open only the charts that you really need. Although there are no limitations on the number of open charts, there is no point in opening unnecessary ones. Color settings do not matter.

Set "Max bars in chart" parameter in [Charts](/en/docs/mt5/client/settings#charts) tab of the platform settings. Some custom indicators are developed in a wasteful way and perform calculations on all history available on the chart. In that case, the lesser the specified value, the better. However, make sure that the indicator works correctly with these settings by restarting the platform after changing the parameter.

The virtual platform is designed so that it automatically downloads all available history from a trade server, but not more than 500 000 bars are available on a chart.

### Indicators and Expert Advisors

Apply to the charts all indicators and Expert Advisors that are necessary for the autonomous operation of the platform. Most trading robots do not access data of indicators on the charts, so check out and decide what you really need.

Products purchased from the [Market](/en/docs/mt5/client/market) and launched on the chart are also moved during migration. They remain completely functional, and the number of available activations is not decreased. Automatic licensing of purchased products without spending available activations is provided only for the virtual platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">DLL calls are completely forbidden in the virtual platform.</span></li><li class="p_tableatten"><span class="f_tableatten">During platform synchronization with the virtual server, charts without Expert Advisors are ignored, even if custom indicators are running on these charts. If you need to migrate a custom indicator, run it on the chart of an "empty" Expert Advisor that does not perform operations. Such an Expert Advisor can be easily generated using the MQL5 Wizard in <a href="/en/docs/mt5/client/autotrading#metaeditor" class="topiclink">MetaEditor</a> by selecting "Expert Advisor: template". This is to ensure that indicators are migrated on purpose.</span></li></ul></td></tr></tbody></table>

All external parameters of indicators and Expert Advisors should be set correctly. Check them once again before you start synchronization.

Scripts cannot be moved during migration even if they are running in an endless loop on the chart at the time of synchronization.

### Configuring Email, FTP and Signals

If an Expert Advisor is to send emails, upload data via [FTP](/en/docs/mt5/client/settings#ftp) or [copy Signal trades](/en/docs/mt5/client/settings#signals), make sure to specify all the necessary settings. Specify the login and password of your MQL5.community account on the [Community](/en/docs/mt5/client/settings#community) tab. This is required for Signal copying.

### Permission to Trade and Copy Signals

The automated trading is always allowed in the virtual platform. Therefore, any Expert Advisor with trading functions running during synchronization can trade on the virtual platform after the migration. Do not launch the Expert Advisors you are not sure about.

When you transfer Expert Advisors, the automated trading function is automatically disabled in the local platform. This is done to prevent the situation when two platforms connected with the same account trade through the same Expert Advisor.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Regardless of whether auto trading is allowed or forbidden in your platform or in the properties of a running Expert Advisor, any trading robot is allowed to trade after being moved to a virtual platform.</span></p></td></tr></tbody></table>

Set the desired trade copying parameters on the [Signals](/en/docs/mt5/client/settings#signals) tab. If a trading account has an active subscription and trade copying is allowed, permission to copy signals is disabled in the trading platform during migration. This is done to prevent the situation when two platforms connected to the same account copy the same trades simultaneously. It is not necessary to turn on signal copying on the local platform when migrating to a virtual platform where the signal is already running.

The ["Synchronize positions without confirmations"](/en/docs/mt5/client/settings#signals) setting is always enabled in the virtual platform. The virtual platform has no user interface, the operations are copied only automatically, and it is impossible to confirm them manually.

Trade copying is automatically enabled on the virtual platform once the migration is complete. Message about copy cancellation on the local platform is also repeated in the journal.

### Setting WebRequest

If a program that is to operate on the virtual platform uses the [WebRequest](https://www.mql5.com/en/docs/network/webrequest "WebRequest function") function for sending HTTP requests, set permission and list all trusted URLs on the [Expert Advisors](/en/docs/mt5/client/settings#ea) tab.

## Migration [#](virtual_hosting_migration#process)

Migration is performed every time you synchronize the trading platform. Synchronization is always a one-direction process — the local platform environment is moved to the virtual platform, but never vice versa. The virtual platform status can be monitored via requesting the platform and Expert Advisor logs, as well as virtual server monitoring data.

To perform synchronization, navigate to VPS and select the migration type. There are several types of migration that should be used depending on the objective:

-   All — a complete migration is necessary if you want to simultaneously launch [Expert Advisors/indicators](/en/docs/mt5/client/market) and [trade copying](/en/docs/mt5/client/signals). In this mode, account connection data, as well as all open charts, signal copying parameters, running Expert Advisors and indicators, FTP and email settings are copied to the virtual server.
-   Experts — only Expert Advisors and indicators are transferred, if subscription to Signals is not required. Unlike the complete migration, signal subscription parameters are not transferred in this mode.
-   Signal — only Signal copying settings (no charts or programs) are transferred. In this mode, account connection data, signal copying parameters, FTP and email settings are transferred to the virtual server.

![Select migration type](/en/docs/mt5/client/img/vps_migration.png "Select migration type")

Thus, you can anytime change the number of charts and the list of symbols in the Data Window, the set of running programs and their input parameters, platform settings and Signal subscription.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">All available history data of open charts is automatically uploaded during the first synchronization. Uploading history from a trade server can take some time, and all programs running on the charts should process the updated data correctly during the synchronization.</span></p></td></tr></tbody></table>

During migration, all the information is recorded in the platform log.

![Logging migration process](/en/docs/mt5/client/img/vps_migration_log.png "Logging migration process")

After the synchronization, open the main journal of the virtual platform to examine the actions performed on it. To do this, navigate to VPS \\ Journal:

![Virtual platform logs](/en/docs/mt5/client/img/vps_logs.png "Virtual platform logs")

To view further details, click "Journal Viewer". In the newly opened log window, specify the desired search text to filter the journal entries, and the desired time frame. After that, click Request to download the found logs.

![Viewing Journal logs](/en/docs/mt5/client/img/vps_log_view.png "Viewing Journal logs")

The virtual platform logs are updated during each request and saved to \[platform data folder\]\\logs\\hosting.\*.terminal\\.

## Migration Features

The migration process has a number of features:

-   Automated trading is always allowed in the virtual platform even if it is disabled in the local platform settings or in the running Expert Advisor's parameters.
-   Scripts are not transferred during migration even if they have been launched in an endless loop on the chart at the time of synchronization.
-   Charts with non-standard timeframes and symbols are not transferred.
-   Accounts with [one-time password](/en/docs/mt5/client/start_advanced/otp) authentication cannot be used on a VPS. Virtual hosting is designed for a completely autonomous platform operation, which would not be possible if manual one-time password specification were required for each connection to the account.

[Register a Server](/en/docs/mt5/client/virtual_hosting_server)

[Working with the Virtual Platform](/en/docs/mt5/client/virtual_hosting_terminal)