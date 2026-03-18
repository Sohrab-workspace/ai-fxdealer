# Mail Servers

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_mail

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Integrations](/en/docs/mt5/platform/administration/integration)Mail Servers

# Mail Servers

The MetaTrader 5 platform is provided with the built-in email service. The service is used to send [trading reports](/en/docs/mt5/platform/administration/admin_groups/groups_settings#reports) to traders, for the [confirmation of email addresses](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups#confirmation) specified during account opening via client terminals, and for the [manual email sending](/en/docs/mt5/platform/administration/mail#create).

Reports and confirmation emails can be sent from different mailboxes, while a separate mailbox can be used for each client group. Thus your White Label partners can send emails to their clients from their own addresses.

Mail server configurations can be efficiently managed in the "Mail servers" section. Configure required parameters once and then you will be able to select the desired server configuration in the [client group](/en/docs/mt5/platform/administration/admin_groups/groups_settings#reports) or [account allocation settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups).

![Mail Server Setup](/en/docs/mt5/platform/img/mail_servers.png "Mail Server Setup")

Create a new configuration and set the mail server parameters:

-   Enable — enable/disable the mail server configuration. If the configuration is disabled, emails will not be sent via this server.
-   Name — configuration name.
-   Sender email — email address from which emails will be sent.
-   Sender name — sender name will be indicated in emails.
-   SMTP server — email server address for sending reports and port number, separated by a colon. Example: smtp.mailserver.com:80.
-   SMTP login — account login on the mail server.
-   Password — account password on the mail server. Some services, such as Gmail, Yahoo, mail.com, and others, require the use of a separate password to access the mailbox through third-party applications. It is usually called App Password. If you are using such a service for mailing, specify the App Password instead of the main password for accessing the mailbox. Additional information is usually provided on the service's website. For example, you can find information for Gmail [here](https://support.google.com/accounts/answer/185833?hl=en) and [here](https://www.hostpapa.com/knowledgebase/how-to-create-and-use-google-app-passwords/).
-   Default server — the "Default" option can be selected for the used mail server in [group settings](/en/docs/mt5/platform/administration/admin_groups/groups_settings#reports) and [account allocation settings](/en/docs/mt5/platform/administration/admin_accounts/account_allocation_groups). In this case the platform will check the list of all servers and will use the first available server with the "Default server" option enabled.

Sent email statistics is shown for each configuration in the list:

-   Total Sent / Errors — number of sent emails and number of unsent emails due to errors.
-   Queue — number of emails on the queue to be sent.
-   Time Min / Max / Avg — minimum, maximum and average time in milliseconds spent to send one email.

[Sponsored VPS](/en/docs/mt5/platform/administration/integration/integration_vps)

[SMS Gateways](/en/docs/mt5/platform/administration/integration/integration_sms)