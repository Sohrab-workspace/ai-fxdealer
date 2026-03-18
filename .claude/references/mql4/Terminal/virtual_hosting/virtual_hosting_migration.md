# Migration

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration

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
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
            -   [Registering Server](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_server)
            -   [Migration](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration)
            -   [Working with Terminal](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)Migration

# Migration

Migration is transferring the current active environment from the client terminal to the virtual one. This is a simple and straightforward way to change the set of launched programs, open charts and subscription parameters in the virtual terminal.

## Preparing for Migration

Before launching the virtual terminal, you should prepare an active environment for it — charts, launched indicators and Expert Advisors, Signal copying parameters and the terminal settings.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/NGSHrX-QAOU/video.mp4" target="_blank" title="Watch video: Preparing to Migrate Robots and Signals "><img class="help" alt="Watch video: Preparing to Migrate Robots and Signals " title="Watch video: Preparing to Migrate Robots and Signals " width="142" height="80" src="/en/docs/mt4/terminal/img/video_hosting_migrate.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Preparing to Migrate Robots and Signals</span></p><p class="p_fortable"><span class="f_fortable">How to setup a trading environment, in order to execute your trading robots and signals on a virtual platform for 24 hours a day?</span></p></td></tr></tbody></table>

### Charts and Market Watch

In the [Market Watch](/en/docs/mt4/terminal/overview/market_watch) window, set up the list of symbols critical for your Expert Advisors' operation. We recommend that you remove all unnecessary symbols to decrease the tick traffic received by the terminal. There is no point in keeping hundreds of symbols in the Market Watch if only a couple of them are used for trading.

Open only the charts that you really need. Although there are no limitations on the number of open charts, there is no point in opening unnecessary ones. Color settings do not matter.

Set "Max bars in chart" parameter in [Charts](/en/docs/mt4/terminal/setup/setup_charts#bars_count) tab of the terminal settings. Some custom indicators are developed in a wasteful way and perform calculations on all history available on the chart. In that case, the lesser the specified value, the better. However, make sure that the indicator works correctly with these settings by restarting the terminal after changing this parameter.

The virtual terminal has been designed so that it automatically downloads all available history from a trade server, but not more than 500 000 bars are available on a chart.

### Indicators and Expert Advisors

Apply to the charts all indicators and Expert Advisors that are necessary for the terminal's autonomous operation. Most trading robots do not refer to indicators on the charts, so check out and decide what you really need.

Products purchased on the [Market](/en/docs/mt4/terminal/overview/terminal/toolbox_market) and launched on the chart are also moved during migration. They remain completely functional, and the number of available activations is not decreased. Automatic licensing of purchased products without spending available activations is provided only for the virtual terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">DLL calls are completely forbidden in the virtual terminal. During the first attempt to call a function from DLL, the launched program is stopped with the critical error.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">During platform synchronization with the virtual server, charts without Expert Advisors are ignored, even if custom indicators are running on these charts. If you need to migrate a custom indicator, run it on the chart of an "empty" Expert Advisor that does not perform operations. Such an Expert Advisor can be easily generated using the MQL5 Wizard in <a href="/en/docs/mt4/terminal/autotrading/metaeditor" class="topiclink">MetaEditor</a> by selecting "Expert Advisor: template". This is to ensure that indicators are migrated on purpose.</span></li></ul></td></tr></tbody></table>

All external parameters of indicators and Expert Advisors should be set correctly. Check them once again before launching synchronization.

Scripts cannot be moved during migration even if they have been launched in an endless loop on the chart at the time of synchronization.

### Configuring Email, FTP and Signals

If an Expert Advisor is to send emails, upload data via [FTP](/en/docs/mt4/terminal/setup/setup_publisher) or [copy Signal trades](/en/docs/mt4/terminal/setup/settings_signals), make sure to specify all necessary settings. Set correct login and password of your MQL5.community account in [Community](/en/docs/mt4/terminal/setup/settings_mql5community) tab. This is necessary for Signal copying.

### Permission to Trade and Signal Copying

The automated trading is always allowed in the virtual terminal. Therefore, any Expert Advisor with trading functions launched during synchronization can trade on the virtual terminal after the migration. Do not launch the Expert Advisors you are not sure about.

When migrating Expert Advisors, autotrading function is automatically disabled in the local terminal. This is done is order to prevent the situation when two terminals connected with the same account trade with the same Expert Advisor.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Regardless of whether autotrading is allowed or forbidden in your client terminal or in the properties of a launched Expert Advisor, any trading robot is allowed to trade after being moved to the virtual terminal.</span></p></td></tr></tbody></table>

Set necessary trade copying parameters in [Signals](/en/docs/mt4/terminal/setup/settings_signals) tab. If a trading account has an active subscription and trade copying is allowed, permission to copy signals is disabled in the client terminal during migration. This is done in order to prevent the situation when two terminals connected to the same account copy the same trades simultaneously. It is not necessary to turn on signal copying on the local terminal when migrating to a virtual terminal where the signal is already running.

The ["Synchronize positions without confirmations"](/en/docs/mt4/terminal/setup/settings_signals) setting is always enabled in the virtual platform. The virtual platform has no user interface, the operations are copied only automatically, and it is impossible to confirm them manually.

Trade copying is automatically enabled on the virtual terminal when migration is complete. Message about copy cancelation in the client terminal is also repeated in the journal.

### Setting WebRequest

If a program that is to operate in the virtual terminal uses [WebRequest](https://www.mql5.com/en/docs/network/webrequest "WebRequest function") function for sending HTTP requests, you should set permission and list all trusted URLs in [Expert Advisors](/en/docs/mt4/terminal/setup/setup_experts) tab.

## Migration [#](virtual_hosting_migration#process)

Migration is performed during each synchronization of the client terminal. Synchronization is always a one-direction process — the client terminal's environment is moved to the virtual terminal but never vice versa. The virtual terminal status can be monitored via requesting the terminal's and Expert Advisors' logs as well as virtual server's monitoring data.

To perform synchronization, open the context menu and select migration type. There are several types of migration that should be used depending on the objective:

-   All — complete migration is necessary if you want to simultaneously launch [Expert Advisors/indicators](/en/docs/mt4/terminal/overview/terminal/toolbox_market) and [trade copying](/en/docs/mt4/terminal/signals). In this mode, account connection data, as well as all open charts, signal copying parameters, launched Expert Advisors and indicators, FTP and email settings are moved to the virtual server.
-   Experts — only Expert Advisors and indicators are moved, if subscription to Signals is not required. Unlike the complete migration, signal subscription parameters are not transferred in this mode.
-   Signal — only Signal copying settings (no charts or programs) are moved. In this mode, account connection data, signal copying parameters, FTP and email settings are moved to the virtual server.

![Starting migration](/en/docs/mt4/terminal/img/vh_migrate.png "Starting migration")

Thus, you always can change the number of charts and the list of symbols in the Data Window, the set of launched programs and their input parameters, the terminal settings and Signal subscription.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">All available history concerning the open charts is automatically uploaded during the first synchronization. Uploading history from a trade server can take some time, and all programs launched on the charts should process the updated data correctly during the synchronization.</span></p></td></tr></tbody></table>

When performing migration, all data is recorded in the client terminal's log.

![Logging migration process](/en/docs/mt4/terminal/img/vh_migrate_log.png "Logging migration process")

After the synchronization, open the virtual terminal's main journal to examine the actions performed on it.

![Requesting the Journal from the Virtual Terminal](/en/docs/mt4/terminal/img/vh_log_request.png "Requesting the Journal from the Virtual Terminal")

In the newly opened log window, you can set a piece of text the journal entries are to be filtered by and a desired interval. After that, click Request to download the found logs.

![Viewing Journal logs](/en/docs/mt4/terminal/img/vh_log_view.png "Viewing Journal logs")

The virtual terminal's logs are updated during each request and saved to \[terminal data folder\]\\logs\\hosting.\*.terminal\\.

## Migration Features

The migration process has a number of features:

-   Automated trading is always allowed in the Virtual terminal even if it has been forbidden by the terminal settings or in the launched Expert Advisor's parameters.
-   Scripts are not moved during migration even if they have been launched in an endless loop on the chart at the time of synchronization.
-   Charts with non-standard timeframes and symbols are not moved.

[Registering Server](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_server)

[Working with Terminal](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal)