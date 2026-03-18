# Installation and Setup of MySQL Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_mysql

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Backup Server](/en/docs/mt5/platform/components/backup_server)[SQL Export](/en/docs/mt5/platform/components/backup_server/sql_export)Installation and Setup of MySQL

# Installation and Setup of MySQL Server

Download one of the distribution kits from MySQL website ([http://dev.mysql.com/downloads/mysql](https://dev.mysql.com/downloads/mysql)) to start installation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Select 32 or 64-bit considering potential volumes of databases. 64-bit server version is more preferable, as it makes possible to have data caches of more than 2 Gb and has better scalability due to increasing RAM on the server.</span></p></td></tr></tbody></table>

Downloaded distribution kit should be installed in accordance with the instructions:

-   at the first step, agree to the terms of use and click "Next"
-   at the second step, select the installation type ("Server only" is recommended)
-   at the third step, click "Execute" and wait for the installation to complete
-   at the fourth and fifth steps, click "Next" to go to the MySQL configuration

![MySQL Installation](/en/docs/mt5/platform/img/mysql_install.gif "MySQL Installation")

During the first configuration step, select the installation type "Standalone MySQL Server /Classin MySQL Replication". Next, select the type of the computer on which MySQL is installed. Based on this information, the configuration Wizard sets efficient parameters for memory, hard drive and CPU consumption. Developer Machine should not be used in real work, therefore, select one of the following types:

-   Server Machine is used in case other services (for example, web server) are present on the computer. In this case, MySQL will consume a "moderate" amount of memory.
-   Dedicated MySQL Server Machine should be selected if the computer will be used exclusively for MySQL server. In this case, MySQL will consume "maximum available" amount of memory for faster performance.

In addition to the computer type, ports and communication channels can also be configured from here, although you can use default values ​​for these parameters.

![Database Configuration](/en/docs/mt5/platform/img/mysql_configure.gif "Database Configuration")

At the next step, specify the password for the root login (administrator account). Here you can also create additional accounts and configure permissions for them.

![Configuring MySQL Accounts](/en/docs/mt5/platform/img/mysql_configure_users.png "Configuring MySQL Accounts")

Further you will be asked to configure the integration of the MySQL server with the operating system, as well as the server extensions. You can use default settings for the above parameters. At the last step, click "Execute" and wait for the configuration to complete.

![MySQL configuration completion](/en/docs/mt5/platform/img/mysql_configure_finish.gif "MySQL configuration completion")

To increase MySQL server performance, edit the my.ini file located in the MySQL installation directory, i.e. C:\\Program Files\\MySQL\\MySQL Server 5.7\\my.ini for the 64-bit version and C:\\Program Files (x86)\\MySQL\\MySQL Server 5.7\\my.ini for the 64-bit version. The file can also be located in C:\\Program Data\\MySQL\\MySQL Server 5.7.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">#&nbsp;InnoDB,&nbsp;unlike&nbsp;MyISAM,&nbsp;uses&nbsp;a&nbsp;buffer&nbsp;pool&nbsp;to&nbsp;cache&nbsp;both&nbsp;indexes&nbsp;and</span><br><span class="f_CodeExample">#&nbsp;row&nbsp;data.&nbsp;The&nbsp;bigger&nbsp;you&nbsp;set&nbsp;this&nbsp;the&nbsp;less&nbsp;disk&nbsp;I/O&nbsp;is&nbsp;needed&nbsp;to</span><br><span class="f_CodeExample">#&nbsp;access&nbsp;data&nbsp;in&nbsp;tables.&nbsp;On&nbsp;a&nbsp;dedicated&nbsp;database&nbsp;server&nbsp;you&nbsp;may&nbsp;set&nbsp;this</span><br><span class="f_CodeExample">#&nbsp;parameter&nbsp;up&nbsp;to&nbsp;80%&nbsp;of&nbsp;the&nbsp;machine&nbsp;physical&nbsp;memory&nbsp;size.&nbsp;Do&nbsp;not&nbsp;set&nbsp;it</span><br><span class="f_CodeExample">#&nbsp;too&nbsp;large,&nbsp;though,&nbsp;because&nbsp;competition&nbsp;of&nbsp;the&nbsp;physical&nbsp;memory&nbsp;may</span><br><span class="f_CodeExample">#&nbsp;cause&nbsp;paging&nbsp;in&nbsp;the&nbsp;operating&nbsp;system.&nbsp;&nbsp;Note&nbsp;that&nbsp;on&nbsp;32bit&nbsp;systems&nbsp;you</span><br><span class="f_CodeExample">#&nbsp;might&nbsp;be&nbsp;limited&nbsp;to&nbsp;2-3.5G&nbsp;of&nbsp;user&nbsp;level&nbsp;memory&nbsp;per&nbsp;process,&nbsp;so&nbsp;do&nbsp;not</span><br><span class="f_CodeExample">#&nbsp;set&nbsp;it&nbsp;too&nbsp;high.</span><br><span class="f_CodeExample">innodb_buffer_pool_size=2046M</span></p></td></tr></tbody></table>

This parameter should be selected considering the server's bit count and available physical memory:

-   for a 32-bit server this value should not exceed 80 % of physical memory and it also should not exceed 2046;
-   for a 64-bit server this value should not exceed 80 % of physical memory.

When exporting data, the platform uses zero date if a date is not specified. Thus in my.ini you need to turn off the SQL modes that prohibit zero dates: NO\_ZERO\_IN\_DATE and NO\_ZERO\_DATE. Find the "sql\_mode" parameter and delete that modes from it:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">sql_mode&nbsp;=&nbsp;"STRICT_TRANS_TABLES,</span><span class="f_CodeExample" style="background-color: #ffff00;">NO_ZERO_IN_DATE,NO_ZERO_DATE</span><span class="f_CodeExample">,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"</span></p></td></tr></tbody></table>

The last step is creation of the schema, to which MySQL data is exported, and performing configuration on the side of MetaTrader 5.

To do this, launch MySQL 5.7 Command Line Client in Start - All Programs - MySQL - MySQL Server 5.7 and enter root password. The following script should be executed after that:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">create&nbsp;schema&nbsp;schema_name;</span></p></td></tr></tbody></table>

For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">create</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">schema</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">metatrader5;</span></p></td></tr></tbody></table>

## Configuration on MetaTrader 5 side

In case backup and MySQL servers are installed on the same computer, connection settings will be as follows:

![Export settings when installing MySQL on the same computer where the backup server is installed](/en/docs/mt5/platform/img/mysql_platform_local.png "Export settings when installing MySQL on the same computer where the backup server is installed")

In case backup and MySQL servers are located on different computers:

![Export settings when installing MySQL on a separate computer](/en/docs/mt5/platform/img/mysql_platform_remote.png "Export settings when installing MySQL on a separate computer")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended to install MySQL and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.</span></p></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

After all settings are specified, the backup server will immediately start export into the external DBMS. Request the [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) of the appropriate backup server using SQL keyword to track the export process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;successfully&nbsp;connect&nbsp;to&nbsp;'127.0.0.1:metatrader5'&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'root'</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;server&nbsp;version&nbsp;5.7.19</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;table&nbsp;'mt5_symbols'&nbsp;creating&nbsp;started</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;table&nbsp;'mt5_symbols'&nbsp;created</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;primary&nbsp;key&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'mt5_symbols'&nbsp;adding&nbsp;started</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;primary&nbsp;key&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'mt5_symbols'&nbsp;added</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;table&nbsp;'mt5_symbols_sessions'&nbsp;creating&nbsp;started</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;table&nbsp;'mt5_symbols_sessions'&nbsp;created</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;primary&nbsp;key&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'mt5_symbols_sessions'&nbsp;adding&nbsp;started</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;MySQL:&nbsp;primary&nbsp;key&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'mt5_symbols_sessions'&nbsp;added</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Symbols:&nbsp;0&nbsp;symbols&nbsp;and&nbsp;0&nbsp;sessions&nbsp;loaded&nbsp;in&nbsp;312&nbsp;msecs</span><br><span class="f_CodeExample">19:00:16&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Symbols:&nbsp;synchronization&nbsp;started</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

[SQL Export](/en/docs/mt5/platform/components/backup_server/sql_export)

[Installation and Setup of MariaDB](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_maria)