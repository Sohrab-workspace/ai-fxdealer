# Common Automation Settings

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_common

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
                -   [Common Settings](/en/docs/mt5/platform/administration/automation/automation_common)
                -   [Triggers](/en/docs/mt5/platform/administration/automation/automation_trigger)
                -   [Conditions](/en/docs/mt5/platform/administration/automation/automation_condition)
                -   [Actions](/en/docs/mt5/platform/administration/automation/automation_action)
                -   [Macros](/en/docs/mt5/platform/administration/automation/automation_macros)
                -   [Statistics](/en/docs/mt5/platform/administration/automation/automation_statistics)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Automations](/en/docs/mt5/platform/administration/automation)Common Settings

# Common Automation Settings

To create a task, open the "Automation" section and create a new configuration:

![Create a configuration and specify general parameters](/en/docs/mt5/platform/img/automation_create.png "Create a configuration and specify general parameters")

Set general parameters for the task:

-   Name — task name. Set descriptive names which reflect the idea of target actions. Appropriate naming will ensure efficient task managements when many tasks are accumulated in the system. While the maximum name length is 127 characters, we recommend keeping names short and concise. This will make it easier to search for automation events in [server logs](/en/docs/mt5/platform/administration/admin_network/network_journal), among other things. It is not recommended to use special characters in the name: %, !. " etc.
-   Trigger — [an event in the platform](/en/docs/mt5/platform/administration/automation/automation_trigger) upon the occurrence of which the automation task should be executed. When a trigger fires, the correspondence of the occurred event to the relevant [conditions](/en/docs/mt5/platform/administration/automation/automation_condition) is checked. If all the conditions are met, a [predefined action](/en/docs/mt5/platform/administration/automation/automation_action) is performed.
-   Started — the date and time on which the trigger check will be activated.
-   Expired — the date and time after which the trigger check will be disabled. If no value is specified in this field, the trigger check interval is considered unlimited.
-   Repetitions — the maximum number of event repetitions over the period specified in the next field. Every time a trigger fires, the system checks how many similar events have occurred during the specified period. If the threshold has been reached, no action is performed. For all triggers except for those of the "[Schedule](/en/docs/mt5/platform/administration/automation/automation_trigger#schedule)" type, a zero value means that the number of repetitions is not limited. If zero is set for a scheduled event, the trigger will fire once at the time specified in the "Started" field. For more setup details please view section "[Period and repetitions setup specifics](/en/docs/mt5/platform/administration/automation/automation_common#period_features)" below.
-   Period — the period of time for which the number of repetitions should be checked. If you are limiting the occurrence of an event, do not leave the period field set to zero. You should explicitly specify some value. Otherwise, the repetition limit will not work.
-   Days of week, Months, Days of month — days and months for which triggers are enabled. If an event does not meet the specified criteria, the event handling will be skipped.

If a task configuration is not ready or if you wish to suspend it, uncheck the "Enable" box.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">For convenience, tasks can be grouped in directories. Click "Add" in the context menu of the "Automation" section in the left-hand tree and specify the new directory name. Then drag and drop the desired tasks into this directory.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">To quickly create similar tasks, use the "<img class="help" alt="Add copy" title="Add copy" width="13" height="15" src="/en/docs/mt5/platform/img/add_copy_icon.png">Add copy" command of the context menu. Instead of creating each task from scratch, create a copy of the existing one and adjust the required parameters.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">When you cancel your subscription to the Automations service, only the three tasks that were activated first will continue to operate. All other tasks will stop running, even if their configurations are enabled. The number of active tasks and their names are displayed in the server log at startup:</span><br><span class="f_tableatten">Automation &nbsp; &nbsp; &nbsp;loading 130 tasks (91 disabled, 3 active)</span><br><span class="f_tableatten">Automation &nbsp; &nbsp; &nbsp;active tasks: High Process CPU usage Alert, Manager Order Modify, Geo Condition</span></li></ul></td></tr></tbody></table>

## Period and repetitions setup specifics [#](automation_common#period_features)

[Repetitions](/en/docs/mt5/platform/administration/automation/automation_common#repetitions) and [period](/en/docs/mt5/platform/administration/automation/automation_common#period) settings have different logic for the "[Schedule](/en/docs/mt5/platform/administration/automation/automation_trigger#schedule)" triggers and for all other triggers:

-   For schedule triggers, this setting indicates how many times and at which intervals the event generation shall be repeated. Therefore, the Repetitions and Period parameters cannot be zero for such events, otherwise they will never be triggered.
-   For all other triggers the setting indicates how many event repetitions in the specified period shall cause the trigger to fire.

Example: Started = 10:30, Repetitions = 3, Period = 3 minutes.

For the "Scheduled event" trigger, the event will be generated three times: at 10:30, at 10:33 and at 10:36. After that the generation will stop.

For all other triggers, the first 3 events over the last 3 minutes at the event occurrence time will be used. For example, if the "Login" trigger is used and connection events occur in the specified period, then:

-   Logging in at 10:30:01 will activate a trigger, as there have been no triggers in the last 3 minutes.
-   Logging in at 10:30:03 will activate a trigger, as there have been only 1 trigger, at 10:30:01.
-   Logging in at 10:31:00 will activate a trigger, as there have been only 2 triggers, at 10:30:01 and at 10:30:03.
-   Logging in at 10:31:01 will not activate a trigger, as there have already been 3 triggers in the last 3 minutes: at 10:30:01, at 10:30:03 and at 10:31:00.
-   Logging in at 10:33:01 will activate a trigger, as there have only been 2 triggers in the last 3 minutes: at 10:30:03 and at 10:31:00.
-   Logging in at 10:33:02 will not activate a trigger, as there have already been 3 triggers in the last 3 minutes: at 10:30:03, at 10:31:00 and at 10:33:01.
-   This logic will continue until the time specified in the "Expired" field.

Trigger activations are calculated in the context of the event source. For example, connections of users 1000 and 1001 are different and thus they will be counted separately. The following unique keys are used:

-   Login — for triggers form sections "Connections", "Finance" (except for first operation events, such as first deposit, first withdrawal, etc.) and "Trade".
-   Symbol — for triggers from the "Prices" section.
-   Absent (no key) — triggers for first operation events, such as first deposit, first credit, etc., "Scheduled event" triggers from the "Platform" section.

If only the period is specified and the number of repetitions is set to 0, the "Scheduled event" trigger will generate an event every specified interval, without any limitations, until the time specified in the "[Expired](/en/docs/mt5/platform/administration/automation/automation_common#expiration)" field. All other trigger types will activate a trigger for each event, without any limitation on the number of repetitions.

If only the number of repetitions is set and the period is equal to zero, the "Scheduled event" trigger will fire once, at the time specified in the "Started" field (the number of repetitions is ignored). All other trigger types shall fire only the first n times, where n is the number of specified repetitions.

[Automations](/en/docs/mt5/platform/administration/automation)

[Triggers](/en/docs/mt5/platform/administration/automation/automation_trigger)