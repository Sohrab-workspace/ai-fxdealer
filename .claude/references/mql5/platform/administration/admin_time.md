# Time

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_time

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Time

# Time

This section is intended for configuring server time settings. At non-working time clients can connect to the server, watch charts and trade history, but cannot conduct trade operations.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">One can setup the trade and quotation sessions for each symbols separately at the <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions" class="topiclink">"Sessions"</a> tab.</span></p></td></tr></tbody></table>

![Time](/en/docs/mt5/platform/img/time.png "Time")

Time settings are divided into common and day settings:

## Common Settings [#](admin_time#common)

The following parameters are available in this block:

-   Time zone — the time zone of the trade server (e.g. GMT+1:00);
-   Daylight Saving Time correction — enable/disable DST correction;
-   Time synchronization with — a list of addresses of reference servers used for [time synchronization](/en/docs/mt5/platform/administration/admin_time#synchronization).

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Changes in "Time zone" and "Daylight Saving Time correction" become effective only after the server restart. It is strongly recommended not to change server time zone settings during a trade day, because this may cause failure of quotes. These settings should be changed on weekend or holidays or at night when the trading activity is minimal and the thread of quotes is slow.</span></p></td></tr></tbody></table>

## Time synchronization [#](admin_time#time_synchronization)

The MetaTrader 5 platform automatically synchronizes the operating system's time with the reference server. Accurate system time is extremely important for several reasons:

-   Accurate order sequencing. In trading, milliseconds (and even microseconds) matter. To correctly determine which trade or order was first, all system components must be precisely aligned in time. Proper synchronization ensures consistent event ordering across components, avoiding related processing errors.
-   Regulatory compliance. Many regulators require brokers to ensure timestamp accuracy to the millisecond. This is necessary for auditing and investigating controversial situations, for example, when there is suspicion of market manipulation.
-   Arbitrage distortion prevention. Time difference across systems can create opportunities for unfair trading advantages, such as execution time manipulations.
-   Consistent logs and monitoring. Synchronized timestamps are crucial for proper diagnostics and event tracking across system components.

Reference servers are specified in the "Time synchronization with" field. By default, two servers are used: time.cloudflare.com and pool.ntp.org. Additional servers can be added, separated by commas. The platform automatically selects the server with the lowest network latency based on DNS resolution. If the fastest server is unavailable, it will try the next one in the list. Synchronization uses the NTP and TIME protocols.

All MetaTrader 5 servers support time synchronization. However, only one server on a machine performs actual synchronization. For example, if the machine runs the main server, history server, and access server, all servers will attempt to synchronize, but the system time will only be updated by the component selected as primary among all MetaTrader 5 servers running on the machine. The status of the primary synchronization server may transition from one server to another.

Time synchronization occurs every 10 minutes. To check the status, request the server [logs](/en/docs/mt5/platform/administration/admin_network/network_journal) for entries containing "system time". Example log entries:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Time&nbsp;system&nbsp;time&nbsp;synchronized&nbsp;via&nbsp;78.46.53.2(0.19&nbsp;ms&nbsp;ping)&nbsp;for&nbsp;3&nbsp;ms</span><br><span class="f_CodeExample">Time&nbsp;system&nbsp;time&nbsp;synchronization&nbsp;via&nbsp;78.46.53.2(0.19&nbsp;ms&nbsp;ping)&nbsp;failed</span></p></td></tr></tbody></table>

Logs appear only on the server performing synchronization. If no entries are found, check logs of other servers on the same machine.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="width:100%;"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">When MetaTrader 5 servers (services) start, the <a href="/en/docs/mt5/platform/platform_installation/installation_preparations#time" class="topiclink">Windows Time Service is automatically disabled</a>. However, if the platform's "Time synchronization with" parameter is not specified, the service remains active.</span></p></td></tr></tbody></table>

When other platform servers connect to the main server, they align their time zones and daylight saving settings with it. Log entries appear as:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">timezone&nbsp;synchronized&nbsp;with&nbsp;main&nbsp;server</span></p></td></tr></tbody></table>

If the time zone or daylight saving changes, the connecting server updates its settings and restarts to apply them.

## Daylight Saving Considerations

In addition to time synchronization, the platform monitors daylight saving transitions. For this process, it relies on dates stored in the operating system's time zone. Therefore, in Windows, it is strongly recommended that the OS time zone and daylight saving settings match those configured in MetaTrader 5.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:324px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Platform and OS settings</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Performed actions</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:324px;"><p class="p_fortable"><span class="f_fortable">DST enabled in MetaTrader 5</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">After Windows switches to DST, the platform does the same within an hour (during the hourly synchronization). The platform uses time data stored in the OS time zone.</span></p></td></tr><tr class="table"><td class="table" style="width:324px;"><p class="p_fortable"><span class="f_fortable">DST disabled in MetaTrader 5</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">No switch is performed.</span></p></td></tr><tr class="table"><td class="table" style="width:324px;"><p class="p_fortable"><span class="f_fortable">DST enabled in MetaTrader 5 but there is no DST switch for the time zone set in OS.</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">No switch is performed, since the platform has no exact data on what date/time the shift is to be performed.</span></p></td></tr></tbody></table>

## Day Settings [#](admin_time#daily_settings)

In order to start editing working time, select one of days and press button "![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit" in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit#edit) menu, on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the context menu. The following window will be opened:

![Time Editing](/en/docs/mt5/platform/img/time_edit.png "Time Editing")

Working hours are colored blue. In order to change a working hour into non-working or vice versa, click it with t he left mouse button. To change working hours in bulk, click on the necessary hour and drag the cursor to another hour. Button "\*" at the end of the line allows switching all working into non-working and vice versa.

For changes to take effect, execute command "![Apply Changes](/en/docs/mt5/platform/img/apply_changes_button.png "Apply Changes") Apply Changes" in the [Edit](/en/docs/mt5/platform/administrator/interface/main_menu/menu_edit#apply) menu, or the same command on the [Standard](/en/docs/mt5/platform/administrator/interface/toolbar/toolbar_standard) toolbar or in the context menu.

## Context Menu [#](admin_time#context)

The context menu of the Time section contains the following commands:

-   ![Edit](/en/docs/mt5/platform/img/edit_button.png "Edit") Edit — edit the selected instruction;
-   ![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export to File — [export](/en/docs/mt5/platform/administration/common_info/import_export_config) work time settings to a file.
-   ![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import from File — [import](/en/docs/mt5/platform/administration/common_info/import_export_config#import) work time settings to a file.
-   ![Find](/en/docs/mt5/platform/img/find_button.png "Find") Find — open the [search](/en/docs/mt5/platform/administrator/interface/search) window;
-   Auto Arrange — if this option is enabled the size of columns is selected automatically;
-   Grid — this option shows/hides field separators.

[Statistics](/en/docs/mt5/platform/administration/automation/automation_statistics)

[Holidays](/en/docs/mt5/platform/administration/admin_holidays)