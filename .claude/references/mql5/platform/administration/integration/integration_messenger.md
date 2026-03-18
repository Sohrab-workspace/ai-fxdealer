# Messengers

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_messenger

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
                -   [Finteza Analytics](/en/docs/mt5/platform/administration/integration/integration_finteza)
                -   [Sponsored VPS](/en/docs/mt5/platform/administration/integration/integration_vps)
                -   [Mail Servers](/en/docs/mt5/platform/administration/integration/integration_mail)
                -   [SMS Gateways](/en/docs/mt5/platform/administration/integration/integration_sms)
                -   [Messengers](/en/docs/mt5/platform/administration/integration/integration_messenger)
                    -   [Telegram](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram)
                    -   [Slack](/en/docs/mt5/platform/administration/integration/integration_messenger/slack)
                -   [KYC](/en/docs/mt5/platform/administration/integration/integration_kyc)
                -   [Event Streaming](/en/docs/mt5/platform/administration/integration/integration_streaming)
                -   [Web Services](/en/docs/mt5/platform/administration/integration/integration_web_services)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)Messengers

# Messengers

The trading platform features built-in integration with popular instant messengers. Using it along with the [Automations service](/en/docs/mt5/platform/administration/automation/automation_action#messenger_channel), you can configure the platform to send notifications about various system events to Telegram, Slack and other messenger channels. For example, you can promptly receive monitoring data, notifications about large financial transactions, manager connections in the platform, and other information directly on your phone.

## Configuring the Provider

![Messenger integration configuration](/en/docs/mt5/platform/img/messenger_channel.png "Messenger integration configuration")

Create a new configuration and specify the following parameters for connecting to the messenger:

-   Enable — enable/disable messenger configuration. If the configuration is disabled, the service will not be used to send messages.
-   Name — configuration name.
-   Type — used messenger. Currently supported messengers integrations include Telegram and Slack. The list will be further expanded.
-   Template — the basic [template](/en/docs/mt5/platform/administration/integration/integration_messenger#template) for sending messages via this messenger.

Further settings depend on the messenger:

-   [Telegram](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram)
-   [Slack](/en/docs/mt5/platform/administration/integration/integration_messenger/slack)

## How to use messengers after setup [#](integration_messenger#use)

To send messages to the configured channels use the "[Post in messenger channel](/en/docs/mt5/platform/administration/automation/automation_action#messenger_channel)" action. Enter the text to send and select one of the available messenger configurations.

## Templates [#](integration_messenger#template)

You can use message templates, while the text can be changed depending on the used message messenger or channel. For example, you can unify platform state notifications sent through the [Automations](/en/docs/mt5/platform/administration/automation/automation_action#messenger_channel) service. Specify the relevant text in the "Template" field, and it will be added to all messages:

![Use templates for easy message setup](/en/docs/mt5/platform/img/messenger_template.png "Use templates for easy message setup")

The field contains the default #MESSAGE# macro which substitutes the source text. In our example, the "Platform Monitoring" text is added to it, and the resulting message will be generated as "Platform Monitoring: \[text from automation action\]".

# Statistics

During operation, the system collects statistics on sent messages. It is available in the corresponding section of each messenger, as well as in the general list of configurations.

-   Status — the availability of the server (endpoint), via which the messages are sent.
-   Message sent — the number of successfully sent messages.
-   Errors — the number of messages that could not be sent.

![Message sending statistics](/en/docs/mt5/platform/img/messenger_statistics.png "Message sending statistics")

To reset the statistics and to start collecting it anew, select "Reset".

[Voiso](/en/docs/mt5/platform/administration/integration/integration_sms/voiso)

[Telegram](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram)