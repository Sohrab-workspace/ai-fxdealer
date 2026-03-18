# Installation and Setup of Oracle Database

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_oracle

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Backup Server](/en/docs/mt5/platform/components/backup_server)[SQL Export](/en/docs/mt5/platform/components/backup_server/sql_export)Installation and Setup of Oracle

# Installation and Setup of Oracle Database

Download the distribution kit from the Oracle's website ([http://www.oracle.com/technetwork/products/express-edition/downloads/index.html](https://www.oracle.com/technetwork/products/express-edition/downloads/index.html)) to install free version of Oracle Database Express Edition. Oracle allows the free use of only the 32-bit version of Express. Therefore, agree to the license terms and download Oracle Database Express Edition 11g Release 2 for Windows x32.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten"><a href="https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package" target="_blank" class="weblink">"Update for Visual C++ 2013 and Visual C++ Redistributable Package"</a> must be installed on the computer where the backup server is installer. Otherwise expert to Oracle databases will not be possible.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Oracle Database Express Edition is limited to 11 GB of user data. If the limit is exceeded, new data will not be added to the database.</span></li></ul></td></tr></tbody></table>

Distribution kit consists of a ZIP archive that should be unpacked into a temporary folder. Then launch DISK1\\setup.exe and follow the instructions:

-   accept the license terms at License Agreement stage;
-   specify administrator password at Specify Database Passwords stage:

![Oracle_4](/en/docs/mt5/platform/img/oracle_4.png)

Then click Next at the following stages and Install at the last one.

Create the client that will be used for connection. To do that, launch sqlplus.exe:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">sqlplus.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">system/password</span></p></td></tr></tbody></table>

Use the same password that was specified at Specify Database Passwords stage during installation. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">sqlplus.exe</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">system/MyAdminPassword</span></p></td></tr></tbody></table>

Then execute the following command to create the user:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">create</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">user</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">user_name</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">identified</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">by</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">password</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">default</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">tablespace</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">users</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">temporary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">tablespace</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">temp;</span></p></td></tr></tbody></table>

And allow connection for it:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">grant</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">connect,resource</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">to</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">user_name;</span></p></td></tr></tbody></table>

For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">create</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">user</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">mt5user</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">identified</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">by</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">mt5password</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">default</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">tablespace</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">users</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">temporary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">tablespace</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">temp;</span><br><span class="f_CodeExample">grant</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">connect,resource</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">to</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">mt5user;</span></p></td></tr></tbody></table>

In case backup and Oracle servers are installed on the same computer, connection settings will be as follows:

![oracle_setting_local](/en/docs/mt5/platform/img/oracle_setting_local.png)

In case backup and Oracle servers are located on different computers:

![oracle_setting_remote](/en/docs/mt5/platform/img/oracle_setting_remote.png)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Oracle Database Express Edition has only one database named XE. Therefore, that is the database that should be specified in Data Folder parameter.</span></li><li class="p_tableatten"><span class="f_tableatten">It is recommended to install Oracle and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.</span></li></ul></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">successfully</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">connected</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">to</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">database</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'XE'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">at</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'localhost'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">as</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">user</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5user'</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">version</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Oracle</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Database</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">11g</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Express</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Edition</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Release</span><span class="f_CodeExample">&nbsp;11.2.0.2.0&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Production</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">creating</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">created</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">adding</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">added</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">creating</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">created</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">adding</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">added</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Symbols:</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">symbols</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">and</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">sessions</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">loaded</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">in</span><span class="f_CodeExample">&nbsp;203&nbsp;</span><span class="f_CodeExample">msecs</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Symbols:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">synchronization</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

[Installation and Setup of MS SQL](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_mssql)

[Installation and Setup of PostgreSQL](/en/docs/mt5/platform/components/backup_server/sql_export/sql_export_postgre)