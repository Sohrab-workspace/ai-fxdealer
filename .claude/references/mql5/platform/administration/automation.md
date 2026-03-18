# Automations

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/automation

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Automations

# Automations

The Automations service enables the execution of various actions in the platform based on predefined scenarios. The service allows specifying a list of conditions and a list of actions that should trigger under these conditions. Automations allows companies to streamline numerous day-to-day operations and eventually reduce manual work. The service does not require from the administrator any extra programming skills, while all rules can be configured in a user-friendly visual mode.

![Automate your work in the MetaTrader 5 platform](/en/docs/mt5/platform/img/automation_intro.jpg "Automate your work in the MetaTrader 5 platform")

The following actions can be automated:

-   Communication with clients. Automatically notify clients when their balances drop below a certain value, send promotional emails to new clients and reminders to inactive customers.
-   Platform maintenance. Reboot servers and gateways if performance metrics degrade, launch history synchronization according to a pre-configured schedule.
-   Managing of configurations. Set dynamic time-based symbol and group parameters, rearrange routing rules after reaching threshold volumes.
-   Managing of deals. Close positions and cancel orders upon expiration of futures contracts.
-   Managing of accounts. Disable trading for malicious traders, conduct balance operations and add automated comments upon certain actions.
-   Sending events to external systems. Back-office integration options will be added soon. For example, you can send information on opened accounts to online trader rooms or to your CRM system via the REST API.

Reduce manual work and free up resources for important business tasks, as well as improve the quality of services by eliminating human errors. Save money on programmer services and paid plugins by replacing them with simple and easily controlled automation tasks.

## Test the service and purchase a subscription

You can create up to three Automation tasks for free. Any types of conditions and actions can be automated. Test the system and evaluate its efficiency for your business.

To remove trial restrictions and to add more automations, [purchase the service subscription from the App Store](https://support.metaquotes.net/en/market/product/547). The service costs USD 500 per month, but the savings and the additional earnings can certainly be much higher than the aforementioned cost.

[Order MetaTrader 5 Automations](https://support.metaquotes.net/en/market/product/547 "Order MetaTrader 5 Automations")

## Task configuration

To configure an automation task, specify:

-   [Time and repetition periodicity](/en/docs/mt5/platform/administration/automation/automation_common) for the task
-   [Triggers](/en/docs/mt5/platform/administration/automation/automation_trigger) — the events upon which the task should be performed
-   [Additional conditions](/en/docs/mt5/platform/administration/automation/automation_condition), under which the task should be performed
-   [Action](/en/docs/mt5/platform/administration/automation/automation_action) to be executed upon the specified conditions

The platform features a few ready-made service examples, which can help you in understanding the service operation and setup principles. Customize the settings and enable tasks to see how the service works.

[Detailed statistics](/en/docs/mt5/platform/administration/automation/automation_statistics) will show how effectively the Automations service assists you in solving everyday tasks.

[Authentication Protocols](/en/docs/mt5/platform/administration/security/authentication_protocol)

[Common Settings](/en/docs/mt5/platform/administration/automation/automation_common)