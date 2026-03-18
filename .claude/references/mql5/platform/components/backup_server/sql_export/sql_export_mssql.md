# Installation and Setup of Microsoft SQL Server

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_mssql

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Backup Server](/en/docs/mt5/platform/components/backup_server)[SQL Export](/en/docs/mt5/platform/components/backup_server/sql_export)Installation and Setup of MS SQL

# Installation and Setup of Microsoft SQL Server

Download one of the distribution kits from Microsoft website ([http://www.microsoft.com/en-us/download/details.aspx?id=29062](https://www.microsoft.com/en-us/download/details.aspx?id=29062)) to install free version of Microsoft SQL Exress 2012.

You need to download ENU\\x86\\SQLEXPR\_x86\_ENU.exe or ENU\\x64\\SQLEXPR\_x64\_ENU.exe.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">MetaTrader 5 supports data export both to Microsoft SQL Server 2005/2008/2012/2014/2016/2017/2019/2022 and to their Express versions.</span></li><li class="p_tableatten"><span class="f_tableatten">Microsoft SQL Server Express 2005 has a limit of 4 GB on user data. Microsoft SQL Server Express 2008 R2 / 2012 has a limit of 10 GB. Therefore, it is recommended to use 2008 R2 or 2012 as Express version. If the limit is exceeded, new data will not be added to the database.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Operating system Windows 8 or higher is required for the <a href="https://www.microsoft.com/en-us/download/details.aspx?id=56840" target="_blank" class="weblink">Microsoft SQL 2016</a> installation.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Select 32 or 64-bit considering potential volumes of databases. 64-bit server version is more preferable, as it makes possible to have data caches of bigger volume and has better scalability due to increasing RAM on the server.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">By default, the backup server connects to the database using the Windows system driver MS OLE DB Provider for SQL Server (SQLOLEDB). This driver is pre-installed in all operating systems, however it is outdated and does not support the TLS 1.1 and TLS 1.2 protocols. If your company's policy does not allow using TLS protocols below 1.1. and they are disabled in the system, the SQLOLEDB driver will not be able to provide backup server connection to the database. In this case you should install an additional driver <a href="https://www.microsoft.com/en-us/download/details.aspx?id=56730" target="_blank" class="weblink">MSOLEDBSQLS</a>, which supports protocols TLS 1.1 and 1.2. After that the backup server will automatically start using the new driver for connecting to the database.</span></li></ul></td></tr></tbody></table>

Downloaded distribution kit should be installed in accordance with the instructions. First, select "New SQL Server stand-alone installation or add features to an existing installations" to install a new copy of Microsoft SQL Server. Check the "I accept the license terms" option at "License Terms" step. Leave default parameters at the following steps up to "Server Configuration". Set Automatic mode for "SQL Server Browser" at "Server Configuration" step:

![MSSQL_6_a](/en/docs/mt5/platform/img/mssql_6_a.png)

Select "Mixed Mode (SQL Server authentication and Windows authentication)" and specify the administrator password at "Database Engine Configuration" step:

![MSSQL_8_a](/en/docs/mt5/platform/img/mssql_8_a.png)

Leave default parameters at the following steps.

TCP/IP should also be enabled for access to SQL Server from the network. To do this, launch "SQL Server Configuration Manager" from the start menu:

![MSSQL_TCP](/en/docs/mt5/platform/img/mssql_tcp.png)

Restart SQL Server (SQLExpress) service in SQL Server Services section.

Launch SQLCMD.exe application ("C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\Binn\\OSQL.EXE" or "C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\Binn\\OSQL.EXE") with the following parameters after installation to create a database:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">SQLCMD.EXE</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-S</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">localhost\SQLEXPRESS</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-U</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">sa</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-P</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">password</span></p></td></tr></tbody></table>

The password is the same as at "Database Engine Configuration" step. Execute the following command in SQLCMD.exe console:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">CREATE</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">DATABASE</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">METATRADER5</span><br><span class="f_CodeExample">GO</span></p></td></tr></tbody></table>

The database will be generated.

In case backup and MS SQL servers are installed on the same computer, connection settings will be as follows:

![MSSQL_AA](/en/docs/mt5/platform/img/mssql_aa.png)

In case backup and MS SQL servers are located on different computers:

![MSSQL_BA](/en/docs/mt5/platform/img/mssql_ba.png)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended to install MS SQL and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.</span></p></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">successfully</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">connected</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">to</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">database</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">at</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'localhost\SQLEXPRESS'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">as</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">user</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'sa'</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">version</span><span class="f_CodeExample">&nbsp;11.0.2100.60&nbsp;</span><span class="f_CodeExample">RTM</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">(Express</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Edition)</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">creating</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">created</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">adding</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">added</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">creating</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">created</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">adding</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">added</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Symbols:</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">symbols</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">and</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">sessions</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">loaded</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">in</span><span class="f_CodeExample">&nbsp;344&nbsp;</span><span class="f_CodeExample">msecs</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Symbols:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">synchronization</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

[Installation and Setup of MariaDB](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_maria)

[Installation and Setup of Oracle](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_oracle)