# Slack

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_messenger/slack

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)[Messengers](/en/docs/mt5/platform/administration/integration/integration_messenger)Slack

# Slack

To set up a Slack channel integration:

-   [Create a workspace](/en/docs/mt5/platform/administration/integration/integration_messenger/slack#workspace) in which messages will be posted
-   [Create an application](/en/docs/mt5/platform/administration/integration/integration_messenger/slack#app) which will post the messages
-   [Connect the application to the channel](/en/docs/mt5/platform/administration/integration/integration_messenger/slack#app_connect) in the workspace
-   [Create a messenger configuration](/en/docs/mt5/platform/administration/integration/integration_messenger/slack#configuration) in the platform

## Creating a channel in the workspace [#](slack#workspace)

Select a workspace and create there a channel to which the system will post messages. If you do not have a workspace yet, create it following the [Slack instructions](https://slack.com/help/articles/206845317-Create-a-Slack-workspace).

To create a channel, click "Add channel" on the left-hand side of the workspace. Next, specify the name of the channel.

![Create a channel in a Slack workspace](/en/docs/mt5/platform/img/messenger_slack_channel.png "Create a channel in a Slack workspace")

The channel name will be used to [configure the messenger](/en/docs/mt5/platform/administration/integration/integration_messenger/slack#configuration) on the platform side. It is specified without #. In this example, it is "automation".

## Creating an application in Slack [#](slack#app)

To create an application, follow the link [https://api.slack.com/apps?new\_app=1](https://api.slack.com/apps?new_app=1).

![Creating an application in Slack](/en/docs/mt5/platform/img/messenger_slack_create_app.png "Creating an application in Slack")

You can configure the created application manually or use the attached manifest — a ready-made settings template, in which you should only replace a few lines.

### Configuration using the manifest

To assist with the setup, we have prepared a manifest template. It sets all the necessary application parameters, and you only need to specify your name.

The manifest is available in two formats: YAML and JSON. You may use any of them at your discretion:

YAML

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">display_information:</span><br><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_CodeExample" style="background-color: #fffbe6;">name:&nbsp;MetaTrader&nbsp;App</span><br><span class="f_CodeExample">features:</span><br><span class="f_CodeExample">&nbsp;&nbsp;bot_user:</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="background-color: #fffbe6;">display_name:&nbsp;MetaTrader&nbsp;App</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;always_online:&nbsp;false</span><br><span class="f_CodeExample">oauth_config:</span><br><span class="f_CodeExample">&nbsp;&nbsp;scopes:</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;bot:</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;chat:write</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;channels:join</span><br><span class="f_CodeExample">settings:</span><br><span class="f_CodeExample">&nbsp;&nbsp;org_deploy_enabled:&nbsp;false</span><br><span class="f_CodeExample">&nbsp;&nbsp;socket_mode_enabled:&nbsp;false</span><br><span class="f_CodeExample">&nbsp;&nbsp;token_rotation_enabled:&nbsp;false</span></p></td></tr></tbody></table>

JSON

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"display_information":&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="background-color: #fffbe6;">"name":&nbsp;"MetaTrader&nbsp;App"</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;},</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"features":&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"bot_user":&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="background-color: #fffbe6;">"display_name":&nbsp;"MetaTrader&nbsp;App"</span><span class="f_CodeExample">,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"always_online":&nbsp;false</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;},</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"oauth_config":&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"scopes":&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"bot":&nbsp;[</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"chat:write",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"channels:join"</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;},</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"settings":&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"org_deploy_enabled":&nbsp;false,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"socket_mode_enabled":&nbsp;false,</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"token_rotation_enabled":&nbsp;false</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

You should change two parameters in these settings:

-   name — application name.
-   display name — the display name will be used for the messages published by the application in the workspace.

When creating an application, select "From an app manifest", then select a workspace and paste in the updated manifest text:

![Create an application from a manifest](/en/docs/mt5/platform/img/messenger_slack_app_manifest.png "Create an application from a manifest")

### Manual configuration

When creating an application, select "From scratch", then specify the application name and select a workspace:

![Creating an application manually](/en/docs/mt5/platform/img/messenger_slack_app_manual.png "Creating an application manually")

After creating the application, add "chat:write" and "channels:join" permissions for the app in the "OAuth & Permissions" section:

![Set application permissions](/en/docs/mt5/platform/img/messenger_slack_app_permissions.png "Set application permissions")

### Getting an OAuth token

In the "OAuth & Permissions" section, click "Install to Workspace". After you confirm access to the workspace, a token will be generated for you. Specify it in the platform-side [messenger settings](/en/docs/mt5/platform/administration/integration/integration_messenger/slack#configuration).

![Getting a token for an application](/en/docs/mt5/platform/img/messenger_slack_app_token.png "Getting a token for an application")

## Connecting an application to a workspace [#](slack#app_connect)

Go to Slack and add the application to the channel where you want to post messages. Click on the channel name and go to the "Integrations" section. Click "Add apps" in this section:

![Add an app to a channel](/en/docs/mt5/platform/img/messenger_slack_app_add.png "Add an app to a channel")

Next, select the previously created application.

![Select an app to add to the channel](/en/docs/mt5/platform/img/messenger_slack_app_add_choose.png "Select an app to add to the channel")

## Creating a configuration [#](slack#configuration)

When your workspace and application are ready, create a [messenger configuration](/en/docs/mt5/platform/administration/integration/integration_messenger) in the platform, fill in the common parameters, and then specify the following details:

-   Endpoint — the address of the Slack server to which requests are sent. The default endpoint is https://slack.com/api; this value should not be changed.
-   Channel — the name of the channel within the Slack workspace, to which the messages will be sent. The name is specified without the # prefix.
-   OAuth token — token for authorizing the application that will send messages to the channel.

![Creating a messenger configuration](/en/docs/mt5/platform/img/messenger_slack_configuration.png "Creating a messenger configuration")

[Telegram](/en/docs/mt5/platform/administration/integration/integration_messenger/telegram)

[KYC](/en/docs/mt5/platform/administration/integration/integration_kyc)