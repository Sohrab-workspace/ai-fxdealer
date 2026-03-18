# Telegram

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_messenger/telegram

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)[Messengers](/en/docs/mt5/platform/administration/integration/integration_messenger)Telegram

# Telegram

To set up a Telegram channel integration:

-   [Create a channel](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram#channel) to which messages will be posted
-   [Register a bot](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram#bot) which will post messages
-   [Add the bot to the channel](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram#add_bot) and set the relevant permissions
-   [Create a messenger configuration](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram#configuration) in the platform

## Creating a Telegram channel [#](telegram#channel)

Create a channel to which messages will be posted. To do this, open the Telegram app, tap the new dialog button next to the search bar and select "Create Channel". If you already have a channel, go to the next step.

Specify the channel name and privacy settings.

![Creating a Telegram channel](/en/docs/mt5/platform/img/messenger_telegram_channel_create.png "Creating a Telegram channel")

To set up the integration, you will need the name or ID of the created channel:

If the channel is public, the name is available on its properties page. Open the channel and tap on the title. In the properties window, the name is shown in the link: https://t.me/\[channel name\]. Specify it in the platform-side [messenger settings](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram#configuration), along with the @ character. For example, @monitoring\_platform.

The public name is not available for private channels. You will need to use the Channel ID instead. To receive it, forward any message from the channel to the bot at [https://t.me/username\_to\_id\_bot](https://t.me/username_to_id_bot). Specify the ID in the platform-side messenger settings. For example, "-1001760596130" (always specify "-" before the ID number).

Optionally, you can use the following method to obtain the channel ID. It works for both public and private channels, but it can only be used after you have [created your bot](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram#bot).

-   Prepare a bot and a channel for integration by following the instructions from this section
-   Send any message from the channel to your bot
-   When setting up the [configuration](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram#configuration) on the platform side, leave the Channel field empty
-   The system will check the incoming message in the bot, will receive the channel ID and will add it to the configuration

![Get channel name or id](/en/docs/mt5/platform/img/messenger_telegram_channel.png "Get channel name or id")

## Create a Telegram bot [#](telegram#bot)

Create a Telegram bot which will post messages to the channel. To do this, open a chat with the BotFather user at [https://t.me/botfather](https://t.me/botfather). Send the /newbot command to the chat. Then set the login and the name of the bot.

![Create a Telegram bot](/en/docs/mt5/platform/img/messenger_telegram_bot.png "Create a Telegram bot")

You will receive a message with the bot authorization token. The token is used when [configuring the messenger](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram#configuration) in the platform.

## Adding the bot to a channel [#](telegram#add_bot)

Next, add the bot to the channel to which you want to publish messages. Open the channel and tap on the title. Select "Administrators" and tap "Add Admin". After that, enter the bot name in the search bar.

![Adding the bot to a channel](/en/docs/mt5/platform/img/messenger_telegram_bot_channel.png "Adding the bot to a channel")

Optionally, you can open the bot profile using the link obtained in the previous step and then select "Add to Group or Channel". After that, specify permissions for the bot.

![Adding a Telegram bot to a channel](/en/docs/mt5/platform/img/messenger_telegram_bot_add.png "Adding a Telegram bot to a channel")

The bot only needs a permission to post messages, but it must be added to the channel as Admin.

Similarly, in the "Subscribers" section of the channel properties, you can add employee accounts to the channel.

## Creating a configuration [#](telegram#configuration)

When the channel and bot are ready, create a [messenger configuration](/en/docs/mt5/platform/administration/integration/integration_messenger) in the platform, fill in the common parameters, and then specify the following details:

-   Endpoint — the address of the Telegram server to which requests are sent. The default endpoint is https://api.telegram.org, this value should not be changed.
-   Channel — the name of the channel to which the messages will be sent (begins with @). Optional a channel identifier, such as "-1001760596130", can be specified here.
-   Authorization token — Telegram bot authorization token.

![Creating a messenger configuration](/en/docs/mt5/platform/img/messenger_telegram_configuration.png "Creating a messenger configuration")

[Messengers](/en/docs/mt5/platform/administration/integration/integration_messenger)

[Slack](/en/docs/mt5/platform/administration/integration/integration_messenger/slack)