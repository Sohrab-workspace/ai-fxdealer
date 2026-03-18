# Installation and Setup of PostgreSQL

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_postgre

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Backup Server](/en/docs/mt5/platform/components/backup_server)[SQL Export](/en/docs/mt5/platform/components/backup_server/sql_export)Installation and Setup of PostgreSQL

# Installation and Setup of PostgreSQL

Download the required version of PostgreSQL installer from the [official website](https://www.postgresql.org/download/).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten"><a href="https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package" target="_blank" class="weblink">"Update for Visual C++ 2013 and Visual C++ Redistributable Package"</a> must be installed on the computer where the backup server is installed. Otherwise export to PostgreSQL databases will not be possible.</span></p></td></tr></tbody></table>

Run the installation file and follow the on-screen instructions. Choose an installation directory an a set of components:

![Installation of PostgreSQL](/en/docs/mt5/platform/img/postgre1.gif "Installation of PostgreSQL")

Next, select the directory, in which the databases will be stored, set a password for the administrator account "postgres". Then specify the port at which the PostgreSQL server will listen to incoming connections.

![Installation of PostgreSQL](/en/docs/mt5/platform/img/postgre2.gif "Installation of PostgreSQL")

Next, set the [locale](https://postgrespro.com/docs/postgrespro/9.5/locale.html) to be used by by the database cluster. The locale is inherited from the operating system be default. Locale affects the operation of some SQL requests. In the next steps, click "Next", and wait for the installation to complete.

![Installation of PostgreSQL](/en/docs/mt5/platform/img/postgre3.gif "Installation of PostgreSQL")

After installation, run the pgAdmin utility from the Start menu. Connect to the server using the postgres login and the password specified during installation. Next, create a database to export information from MetaTrader 5.

![Creating a database in PostgreSQL](/en/docs/mt5/platform/img/postgre_db_create.png "Creating a database in PostgreSQL")

Then configure data export on the platform site. In case the backup server and PostgreSQL servers are installed on the same computer, connection parameters should be configured as follows:

![Export settings when installing PostgreSQL on the same computer where the backup server is installed](/en/docs/mt5/platform/img/postgres_settings_local.png "Export settings when installing PostgreSQL on the same computer where the backup server is installed")

In case the backup server and PostgreSQL servers are installed on different computers, connection parameters should be configured as follows:

![Export settings when installing PostgreSQL on a separate computer](/en/docs/mt5/platform/img/postgres_settings_remote.png "Export settings when installing PostgreSQL on a separate computer")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">It is recommended to install PostgreSQL and the backup server on the same computer for faster export. However, it should also be kept in mind that the backup server consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backup servers will run close to necessary DBMS.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">All authentication methods are supported for connecting to PostgreSQL, including scram-sha-256.</span></li></ul></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2017.12.21&nbsp;15:17:17.154 &nbsp; &nbsp; &nbsp; &nbsp;SQL&nbsp;Export &nbsp; &nbsp; &nbsp; &nbsp;PostgreSQL:&nbsp;server&nbsp;version&nbsp;10.1</span><br><span class="f_CodeExample">2017.12.21&nbsp;15:17:17.156 &nbsp; &nbsp; &nbsp; &nbsp;SQL&nbsp;Export &nbsp; &nbsp; &nbsp; &nbsp;PostgreSQL:&nbsp;successfully&nbsp;connected&nbsp;to&nbsp;database&nbsp;'metatrader5'&nbsp;at&nbsp;'localhost'&nbsp;as&nbsp;user&nbsp;'postgres'</span><br><span class="f_CodeExample">2017.12.21&nbsp;15:17:17.170 &nbsp; &nbsp; &nbsp; &nbsp;SQL&nbsp;Export &nbsp; &nbsp; &nbsp; &nbsp;PostgreSQL:&nbsp;table&nbsp;'mt5_symbols_sessions'&nbsp;creating&nbsp;started</span><br><span class="f_CodeExample">2017.12.21&nbsp;15:17:17.180 &nbsp; &nbsp; &nbsp; &nbsp;SQL&nbsp;Export &nbsp; &nbsp; &nbsp; &nbsp;PostgreSQL:&nbsp;table&nbsp;'mt5_symbols_sessions'&nbsp;created</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

[Installation and Setup of Oracle](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_oracle)

[mt5\_accounts](/en/docs/mt5/platform/components/backup_server/sql_export/sql_mt5_accounts)