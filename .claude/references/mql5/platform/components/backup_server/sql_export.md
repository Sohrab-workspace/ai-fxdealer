# SQL Export

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/sql_export

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
                -   [Backup Features](/en/docs/mt5/platform/components/backup_server/backup_server_features)
                -   [Switching to Backup Server](/en/docs/mt5/platform/components/backup_server/backup_server_switch)
                -   [Restoring Server](/en/docs/mt5/platform/components/backup_server/backup_server_restore)
                -   [SQL Export](/en/docs/mt5/platform/components/backup_server/sql_export)
                    -   [Installation and Setup of MySQL](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_mysql)
                    -   [Installation and Setup of MariaDB](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_maria)
                    -   [Installation and Setup of MS SQL](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_mssql)
                    -   [Installation and Setup of Oracle](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_oracle)
                    -   [Installation and Setup of PostgreSQL](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_postgre)
                    -   [mt5\_accounts](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_accounts)
                    -   [mt5\_allocations](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_allocations)
                    -   [mt5\_allocations\_agreements](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_allocations_agreements)
                    -   [mt5\_antiddos\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_antiddos_servers)
                    -   [mt5\_antiddos\_sources](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_antiddos_sources)
                    -   [mt5\_automation\_actions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_automation_actions)
                    -   [mt5\_automation\_conditions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_automation_conditions)
                    -   [mt5\_automation\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_automation_params)
                    -   [mt5\_automations](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_automations)
                    -   [mt5\_clients](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_clients)
                    -   [mt5\_commissions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_commissions)
                    -   [mt5\_commissions\_tiers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_commissions_tiers)
                    -   [mt5\_corporate](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_corporate)
                    -   [mt5\_corporate\_links](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_corporate_links)
                    -   [mt5\_daily](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_daily)
                    -   [mt5\_daily\_orders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_daily_orders)
                    -   [mt5\_daily\_positions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_daily_positions)
                    -   [mt5\_deals](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_deals)
                    -   [mt5\_documents](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_documents)
                    -   [mt5\_email](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_email)
                    -   [mt5\_feeder\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_feeder_params)
                    -   [mt5\_feeder\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/mt5_feeder_symbols)
                    -   [mt5\_feeder\_translates](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_feeder_translates)
                    -   [mt5\_feeders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_feeders)
                    -   [mt5\_firewall](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_firewall)
                    -   [mt5\_gateway\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_gateway_params)
                    -   [mt5\_gateway\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/mt5_gateway_symbols)
                    -   [mt5\_gateway\_translates](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_gateway_translates)
                    -   [mt5\_gateways](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_gateways)
                    -   [mt5\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_groups)
                    -   [mt5\_groups\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_groups_symbols)
                    -   [mt5\_history\_sync](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_history_sync)
                    -   [mt5\_history\_sync\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_history_sync_symbols)
                    -   [mt5\_holidays](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_holidays)
                    -   [mt5\_leverage\_rules](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_leverage_rules)
                    -   [mt5\_leverage\_tiers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_leverage_tiers)
                    -   [mt5\_leverages](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_leverages)
                    -   [mt5\_managers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_managers)
                    -   [mt5\_messengers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_messengers)
                    -   [mt5\_messenger\_countries](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_messenger_countries)
                    -   [mt5\_messenger\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_messenger_groups)
                    -   [mt5\_network](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network)
                    -   [mt5\_network\_access\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_access_servers)
                    -   [mt5\_network\_antiddos](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_antiddos)
                    -   [mt5\_network\_backup\_folders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_backup_folders)
                    -   [mt5\_network\_backup\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_backup_servers)
                    -   [mt5\_network\_history\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_history_servers)
                    -   [mt5\_network\_trade\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_trade_servers)
                    -   [mt5\_orders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_orders)
                    -   [mt5\_orders\_history](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_history)
                    -   [mt5\_pay\_rules](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_rules)
                    -   [mt5\_pay\_rule\_conditions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_rule_conditions)
                    -   [mt5\_pay\_wallets](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallets)
                    -   [mt5\_pay\_wallet\_commissions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallet_commissions)
                    -   [mt5\_pay\_wallet\_countries](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallet_countries)
                    -   [mt5\_pay\_wallet\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallet_groups)
                    -   [mt5\_pay\_wallet\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallet_params)
                    -   [mt5\_payments](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_payments)
                    -   [mt5\_payment\_history](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_payment_history)
                    -   [mt5\_plugin\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_plugin_params)
                    -   [mt5\_plugins](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_plugins)
                    -   [mt5\_positions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_positions)
                    -   [mt5\_prices](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_prices)
                    -   [mt5\_report\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_report_params)
                    -   [mt5\_reports](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_reports)
                    -   [mt5\_routing](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_routing)
                    -   [mt5\_routing\_conds](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_routing_conds)
                    -   [mt5\_routing\_dealers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_routing_dealers)
                    -   [mt5\_spread\_legs](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_spread_legs)
                    -   [mt5\_spreads](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_spreads)
                    -   [mt5\_streamings](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streamings)
                    -   [mt5\_streaming\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streaming_groups)
                    -   [mt5\_streaming\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streaming_symbols)
                    -   [mt5\_streaming\_topics](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streaming_topics_enum)
                    -   [mt5\_streaming\_topic\_data](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streaming_topic_data)
                    -   [mt5\_subscriptions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscriptions)
                    -   [mt5\_subscription\_countries](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscription_countries)
                    -   [mt5\_subscription\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscription_groups)
                    -   [mt5\_subscription\_news](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscription_news)
                    -   [mt5\_subscription\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscription_symbols)
                    -   [mt5\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_symbols)
                    -   [mt5\_symbols\_sessions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_symbols_sessions)
                    -   [mt5\_time](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_time)
                    -   [mt5\_time\_weekdays](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_time_weekdays)
                    -   [mt5\_users](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_users)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
            -   [Old WebTerminal](/en/docs/mt5/platform/components/web_terminal_old)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Backup Server](/en/docs/mt5/platform/components/backup_server)SQL Export

# SQL Export

The MetaTrader 5 trading platform provides standard options for the real-time data export to MySQL, Microsoft SQL Server, FireBird, Oracle, MariaDB and PostgreSQL databases. This option enables the quick and easy deployment of data export to an external DBMS for using the platform data in any popular programming language and third-party applications. Thus, it is possible to create an intermediate layer between a trade server and broker's program services that regularly access trading data. This reduces the load on the trade server when it receives the current trading data.

The export function is enabled by simple specification of [settings for connection to DBMS](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql) via MetaTrader 5 Administrator. After that, the backup server will immediately perform an initial synchronization of data from the DBMS. Further, new data will be exported to the DBMS in real time. The following data is exported:

-   Information about clients (general information and trading status)
-   Current active orders and positions
-   The history of orders and deals
-   Current prices
-   Virtually all settings of the trading platform (except for the working time, synchronization and spreads)

The description of installation and setup of popular databases is provided in appropriate subsections:

-   [MySQL Server 5.7](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_mysql) (supported versions: 5.6, 5.7, 8.0, 8.1)
-   [MariaDB 10.2](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_maria) (all version supported)
-   [Microsoft SQL Express 2012](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_mssql) (supported versions: 2005, 2008, 2008 R2, 2012, 2014, 2016, 2017, 2019, 2022)
-   [Oracle Database Express Edition 11g](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_oracle) (supported versions: 11g/11g Express Edition, 12c, 18c, 19c, 21c, 23ai)
-   [PostgreSQL](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_postgre) (supported versions: 8.4 — 17)

## Operation Principle

Export mechanism has been implemented on the side of backup servers replicating data from the trade servers.

Below are the general steps of synchronization in a backup server:

-   The backup server connects to the appropriate trade server and is synchronized with it.
-   After synchronization with the trade server is successfully complete, the backup server synchronizes an external DBMS.
-   The backup server applies changes to its databases and the external DBMS via transactions from the trade server.

The backup server performs initial synchronization based on time stamps (Timestamp field in the tables) during each connection to DBMS:

-   All logs with different time stamps in the external DBMS are replaced with backup server logs.
-   All entries that are absent at the backup server are removed from the external DBMS.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A time stamp is used for checking the identity of the backup and the external DBMS logs. If a time stamp on the backup is similar to the on at the external DBMS, a backup server considers that all other log fields are similar and the log update is not required.</span></p></td></tr></tbody></table>

After databases are synchronized, the backup server applies change transactions on the external DBMS. Besides, prices and profit values for active orders (mt5\_orders), positions (mt5\_positions) and related trading accounts (mt5\_accounts) are also periodically updated.

A detailed description of exported tables can be found in the following subsections:

-   [mt5\_accounts](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_accounts) — trade account state database.

-   [mt5\_allocations](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_allocations) — account allocation settings.
-   [mt5\_allocations\_agreements](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_allocations_agreements) — list of agreements used in the account allocation settings.
-   [mt5\_antiddos\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_antiddos_servers) —  list of trading servers connected via the Anti DDoS Proxy Server.
-   [mt5\_antiddos\_sources](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_antiddos_sources) — range of IP addresses belonging to the provider's Anti DDoS proxy servers.
-   [mt5\_automation\_actions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_automation_actions) — actions for automation tasks.
-   [mt5\_automation\_conditions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_automation_conditions) — conditions for automation tasks.
-   [mt5\_automation\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_automation_params) — action parameters for automation tasks
-   [mt5\_automations](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_automations) — [automation](/en/docs/mt5/platform/administration/automation) tasks.

-   [mt5\_clients](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_clients) — [client](/en/docs/mt5/platform/administration/clients) database.
-   [mt5\_commissions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_commissions) — [commission](/en/docs/mt5/platform/administration/admin_groups/groups_comissions) settings for groups.
-   [mt5\_commissions\_tiers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_commissions_tiers) — [commission level](/en/docs/mt5/platform/administration/admin_groups/groups_comissions#level) settings.

-   [mt5\_corporate](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_corporate) — corporate link settings.
-   [mt5\_corporate\_links](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_corporate_links) — list of configured corporate links.

-   [mt5\_daily](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_daily) — database of daily reports.

-   [mt5\_daily\_orders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_daily_orders) — data on the status of open orders at the end of the trading day.
-   [mt5\_daily\_positions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_daily_positions) — data on the status of position at the end of the trading day.

-   [mt5\_deals](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_deals) — [deal](/en/docs/mt5/platform/administration/admin_deals) database.
-   [mt5\_documents](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_documents) — database of [client documents](/en/docs/mt5/platform/administration/clients#documents).

-   [mt5\_email](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_email) — mail server settings.

-   [mt5\_feeder\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_feeder_params) — [additional settings](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#parameters) of data feeds.

-   [mt5\_feeder\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/mt5_feeder_symbols) — [symbol settings](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#symbols) for data feeds.

-   [mt5\_feeder\_translates](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_feeder_translates) — [conversion settings](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#translation) on data feeds.
-   [mt5\_feeders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_feeders) — settings of [data feeds](/en/docs/mt5/platform/administration/admin_feeds).
-   [mt5\_firewall](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_firewall) — [firewall](/en/docs/mt5/platform/administration/security/admin_access) settings.
-   [mt5\_gateway\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_gateway_params) — additional gateway settings.

-   [mt5\_gateway\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/mt5_gateway_symbols) — [symbol settings](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#symbols) for gateways.

-   [mt5\_gateway\_translates](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_gateway_translates) — translation settings in gateways.
-   [mt5\_gateways](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_gateways) — gateway settings.
-   [mt5\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_groups) — [groups'](/en/docs/mt5/platform/administration/admin_groups) configurations.
-   [mt5\_groups\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_groups_symbols) — individual [symbol settings for groups](/en/docs/mt5/platform/administration/admin_groups/admin_groups_symbols).

-   [mt5\_history\_sync](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_history_sync) — price history synchronization settings.
-   [mt5\_history\_sync\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_history_sync_symbols) — list of symbols specified in the price history synchronization settings.

-   [mt5\_holidays](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_holidays) — [holiday](/en/docs/mt5/platform/administration/admin_holidays) configurations.

-   [mt5\_leverage\_rules](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_leverage_rules) — rule settings in floating leverage configurations.
-   [mt5\_leverage\_tiers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_leverage_tiers) — level settings in floating leverage configurations.
-   [mt5\_leverages](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_leverages) — [floating leverage](/en/docs/mt5/platform/administration/leverages) configurations.

-   [mt5\_managers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_managers) — [manager](/en/docs/mt5/platform/administration/admin_managers) accounts.

-   [mt5\_messengers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_messengers) — [messenger](/en/docs/mt5/platform/administration/integration/integration_messenger) and [SMS provider](/en/docs/mt5/platform/administration/integration/integration_sms) configurations.
-   [mt5\_messenger\_countries](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_messenger_countries) — country settings for messengers and SMS providers.
-   [mt5\_messenger\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_messenger_groups) — group settings for messengers and SMS providers.

-   [mt5\_network](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network) — general [settings of servers](/en/docs/mt5/platform/administration/admin_network/network_add_edit).
-   [mt5\_network\_access\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_access_servers) — access servers settings.

-   [mt5\_network\_antiddos](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_antiddos) — Anti DDoS server settings.

-   [mt5\_network\_backup\_folders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_backup_folders) — backed up custom folders.

-   [mt5\_network\_backup\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_backup_servers) — backup servers settings.

-   [mt5\_network\_history\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_history_servers) — history server settings.
-   [mt5\_network\_trade\_servers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_network_trade_servers) — trade servers settings.
-   [mt5\_orders](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_orders) — open [order](/en/docs/mt5/platform/administration/admin_orders) database.
-   [mt5\_orders\_history](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_history) — closed [order](/en/docs/mt5/platform/administration/admin_orders) database.

-   [mt5\_pay\_rules](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_rules) — [payment routing rules](/en/docs/mt5/platform/administration/payments/payments_rules).
-   [mt5\_pay\_rule\_conditions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_rule_conditions) — conditions for payment routing rules.
-   [mt5\_pay\_wallets](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallets) — [payment wallet](/en/docs/mt5/platform/administration/payments) settings.
-   [mt5\_pay\_wallet\_commissions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallet_commissions) — commission settings in payment wallets.
-   [mt5\_pay\_wallet\_countries](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallet_countries) — country settings in payment wallets.
-   [mt5\_pay\_wallet\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallet_groups) — group settings in payment wallets.
-   [mt5\_pay\_wallet\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_pay_wallet_params) — additional parameters of payment wallets
-   [mt5\_payments](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_payments) — active payments database.
-   [mt5\_payments\_history](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_payment_history) — payment history database.

-   [mt5\_plugin\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_plugin_params) — [additional settings](/en/docs/mt5/platform/administration/admin_plugins#module) of plugins.
-   [mt5\_plugins](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_plugins) — [plugin](/en/docs/mt5/platform/administration/admin_plugins) settings.
-   [mt5\_positions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_positions) — [position](/en/docs/mt5/platform/administration/admin_positions) database.
-   [mt5\_prices](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_prices) — database of prices.
-   [mt5\_report\_params](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_report_params) — [additional settings](/en/docs/mt5/platform/administration/admin_reports#module) of reports.
-   [mt5\_reports](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_reports) — [report](/en/docs/mt5/platform/administration/admin_reports) settings.
-   [mt5\_routing](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_routing) — settings of [routing rules](/en/docs/mt5/platform/administration/requests_routing).
-   [mt5\_routing\_conds](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_routing_conds) — [additional conditions](/en/docs/mt5/platform/administration/requests_routing/routing_rules#condition) in routing rules
-   [mt5\_routing\_dealers](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_routing_dealers) — settings of [dealers/gateways](/en/docs/mt5/platform/administration/requests_routing#dealers) in routing rules.

-   [mt5\_spread\_legs](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_spread_legs) — spread legs.
-   [mt5\_spreads](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_spreads) — spread settings.

-   [mt5\_streamings](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streamings) — [data streaming](/en/docs/mt5/platform/administration/integration/integration_streaming) configurations.
-   [mt5\_streaming\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streaming_groups) — data steaming group settings.
-   [mt5\_streaming\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streaming_symbols) — data steaming symbol settings.
-   [mt5\_streaming\_topics](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streaming_topics_enum) — data steaming topic settings.
-   [mt5\_streaming\_topic\_data](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_streaming_topic_data) — additional data steaming settings.
-   [mt5\_subscriptions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscriptions) — [subscription](/en/docs/mt5/platform/administration/subscriptions) settings.
-   [mt5\_subscription\_countries](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscription_countries) — country settings for subscriptions.
-   [mt5\_subscription\_groups](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscription_groups) — group settings for subscriptions.
-   [mt5\_subscription\_news](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscription_news) — news settings for subscriptions.
-   [mt5\_subscription\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_subscription_symbols) — symbol settings for subscriptions.

-   [mt5\_symbols](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_symbols) — [symbol](/en/docs/mt5/platform/administration/admin_symbols) configurations.
-   [mt5\_symbols\_sessions](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_symbols_sessions) — symbol [trading and quotation sessions](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions).
-   [mt5\_time](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_time) — platform [trading time settings](/en/docs/mt5/platform/administration/admin_time).
-   [mt5\_time\_weekdays](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_time_weekdays) — platform's [working time schedule](/en/docs/mt5/platform/administration/admin_time#daily_settings), days.
-   [mt5\_users](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_users) — [account](/en/docs/mt5/platform/administration/admin_accounts) database.

## Custom Data in MetaTrader 5 Tables

In the platform, you can create custom tables and databases, add your own fields in mt5\_\* tables, which are used for data export, as well as create stored procedures and triggers.

-   The backup server does not recreate data, but only adds or updates existing records. A table entry is only deleted if the appropriate entry is deleted on the platform side. For example, if a user is added to the mt5\_users tables, the appropriate user record will exist in the database until the user is deleted from MetaTrader 5.
-   The backup server only works with its own tables and fields.
-   The backup server does not create default indexes. Each index is an extra load on the database, which can slow down exports and information updates.
-   When you create your own fields in mt5\_\* tables, do not forget to set default values for them (or allow NULL). Otherwise, the backup server will not be able to add new entries to the tables.

## Additional information

Find additional recommendations on handling SQL databases in the articles:

-   [Export to SQL database takes too much time](https://support.metaquotes.net/en/articles/1598)
-   [How to present account permissions in MySQL](https://support.metaquotes.net/en/articles/1576)

[Restoring Server](/en/docs/mt5/platform/components/backup_server/backup_server_restore)

[Installation and Setup of MySQL](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_mysql)