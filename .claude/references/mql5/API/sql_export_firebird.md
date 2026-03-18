# Installation and Setup of FireBird

> Source: https://support.metaquotes.net/en/docs/mt5/api/sql_export_firebird

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
    -   [iPhone/iPad](/en/docs/mt5/iphone)
    -   [Android](/en/docs/mt5/android)
    -   [WebTerminal](/en/docs/mt5/platform/components/web_terminal)
    -   [API](/en/docs/mt5/api)
        -   [Getting Started](/en/docs/mt5/api/getting_started)
        -   [Server API](/en/docs/mt5/api/serverapi)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
            -   [Installation and Setup of MySQL](/en/docs/mt5/api/sql_export_mysql)
            -   [Installation and Setup of MariaDB](/en/docs/mt5/api/sql_export_maria)
            -   [Installation and Setup of FireBird](/en/docs/mt5/api/sql_export_firebird)
            -   [Installation and Setup of MS SQL](/en/docs/mt5/api/sql_export_mssql)
            -   [Installation and Setup of Oracle](/en/docs/mt5/api/sql_export_oracle)
            -   [Installation and Setup of PostgreSQL](/en/docs/mt5/api/sql_export_postgre)
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
        -   [Database Interfaces](/en/docs/mt5/api/reference_bases)
        -   [Tools](/en/docs/mt5/api/reference_tools)
        -   [Development Features](/en/docs/mt5/api/features)
        -   [List of Events](/en/docs/mt5/api/event_list)
        -   [List of Hooks](/en/docs/mt5/api/hook_list)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[SQL Export](/en/docs/mt5/api/sql_export)Installation and Setup of FireBird

# Installation and Setup of FireBird

Download one of the distribution kits from FireBird website ([http://www.firebirdsql.org/en/server-packages](https://www.firebirdsql.org/en/server-packages)).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Select 32 or 64-bit considering potential volumes of databases. 64-bit server version is more preferable, as it makes possible to have data caches of more than 2 GB and has better scalability due to increasing RAM on the server.</span></p></td></tr></tbody></table>

Run the installation file and follow the on-screen instructions. Agree to the terms of use and specify FireBird installation path (you may use the default path). Next, specify the list of components to install or use the default option.

![FireBird installation](/en/docs/mt5/api/img/firebird_install.gif "FireBird installation")

Then specify the name for the program group in the Start menu and configure the integration of the FireBird server with the operating system (these parameters can also be left by default). At the next step, specify the password for the SYSDBA login (administrator account). Start the installation process by pressing "Install" and wait for it to finish.

![FireBird installation](/en/docs/mt5/api/img/firebird_install2.gif "FireBird installation")

After installation, you need to create a schema (database) to which data will be exported. To do this, open "Start — All Programs — FireBird 3.0" and launch "Firebird ISQL Tool". Execute the following command in it:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">CREATE&nbsp;DATABASE&nbsp;'path_to_the_DB\DB-file_name.fdb'&nbsp;page_size&nbsp;16384&nbsp;user&nbsp;'user_name'&nbsp;password&nbsp;'password';</span></p></td></tr></tbody></table>

Example:

![Example of FireBird database creation](/en/docs/mt5/api/img/firebird_base_create.png "Example of FireBird database creation")

In this example, 'c:\\databases' directory should be created in advance.

Additional Firebird setup should be performed to increase efficiency. To do this, edit the firebird.conf configuration text file in the installation directory:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">#&nbsp;----------------------------</span><br><span class="f_CodeExample">#&nbsp;Number&nbsp;of&nbsp;cached&nbsp;database&nbsp;pages</span><br><span class="f_CodeExample">#</span><br><span class="f_CodeExample">#&nbsp;This&nbsp;sets&nbsp;the&nbsp;number&nbsp;of&nbsp;pages&nbsp;from&nbsp;any&nbsp;one&nbsp;database&nbsp;that&nbsp;can&nbsp;be&nbsp;held</span><br><span class="f_CodeExample">#&nbsp;in&nbsp;cache&nbsp;at&nbsp;once.&nbsp;If&nbsp;you&nbsp;increase&nbsp;this&nbsp;value,&nbsp;the&nbsp;engine&nbsp;will</span><br><span class="f_CodeExample">#&nbsp;allocate&nbsp;more&nbsp;pages&nbsp;to&nbsp;the&nbsp;cache&nbsp;for&nbsp;every&nbsp;database.&nbsp;By&nbsp;default,&nbsp;the</span><br><span class="f_CodeExample">#&nbsp;SuperServer&nbsp;allocates&nbsp;2048&nbsp;pages&nbsp;for&nbsp;each&nbsp;database&nbsp;and&nbsp;the&nbsp;classic</span><br><span class="f_CodeExample">#&nbsp;allocates&nbsp;75&nbsp;pages&nbsp;per&nbsp;client&nbsp;connection&nbsp;per&nbsp;database.</span><br><span class="f_CodeExample">#</span><br><span class="f_CodeExample">#&nbsp;Type:&nbsp;integer</span><br><span class="f_CodeExample">#</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="font-weight: bold;">DefaultDbCachePages&nbsp;=&nbsp;65536</span></p></td></tr></tbody></table>

It means that DefaultDbCachePages line should be uncommented and the value of 65536 should be set for it. This will make Firebird to use cache of 1 GB for the database. If necessary, you can set a lower value using the following equation:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">Cache&nbsp;size&nbsp;=&nbsp;Page&nbsp;size&nbsp;(16&nbsp;Kb)&nbsp;*&nbsp;DefaultDbCachePages</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The maximum value for DefaultDbCachePages is 65536 meaning that the maximum cache for 16 Kb pages will be approximately equal to 1 GB.</span></p></td></tr></tbody></table>

In case backup and FireBird servers are installed on the same computer, connection settings will be as follows:

![fb_setting_local](/en/docs/mt5/api/img/fb_setting_local.png)

In case backup and FireBird servers are located on different computers:

![fb_setting_remote](/en/docs/mt5/api/img/fb_setting_remote.png)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended to install FireBird and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.</span></p></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;successfully&nbsp;connected&nbsp;to&nbsp;database&nbsp;'c:\databases\metatrader5.fdb'&nbsp;at&nbsp;'127.0.0.1'&nbsp;as&nbsp;user&nbsp;'SYSDBA'</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;server&nbsp;version&nbsp;3.0.2</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;table&nbsp;'mt5_symbols'&nbsp;creating&nbsp;started</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;table&nbsp;'mt5_symbols'&nbsp;created</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;primary&nbsp;key&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'mt5_symbols'&nbsp;adding&nbsp;started</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;primary&nbsp;key&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'mt5_symbols'&nbsp;added</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;table&nbsp;'mt5_symbols_sessions'&nbsp;creating&nbsp;started</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;table&nbsp;'mt5_symbols_sessions'&nbsp;created</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;primary&nbsp;key&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'mt5_symbols_sessions'&nbsp;adding&nbsp;started</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Firebird:&nbsp;primary&nbsp;key&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;'mt5_symbols_sessions'&nbsp;added</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Symbols:&nbsp;0&nbsp;symbols&nbsp;and&nbsp;0&nbsp;sessions&nbsp;loaded&nbsp;in&nbsp;93&nbsp;msecs</span><br><span class="f_CodeExample">2012.10.17&nbsp;15:16:08&nbsp;&nbsp;&nbsp;&nbsp;SQL&nbsp;Export&nbsp;&nbsp;&nbsp;&nbsp;Symbols:&nbsp;synchronization&nbsp;started</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

[Installation and Setup of MariaDB](/en/docs/mt5/api/sql_export_maria)

[Installation and Setup of MS SQL](/en/docs/mt5/api/sql_export_mssql)