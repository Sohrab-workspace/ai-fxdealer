# Installation and Setup of Microsoft SQL Server

> Source: https://support.metaquotes.net/en/docs/mt5/api/sql_export_mssql

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[SQL Export](/en/docs/mt5/api/sql_export)Installation and Setup of MS SQL

# Installation and Setup of Microsoft SQL Server

Download one of the distribution kits from Microsoft website ([http://www.microsoft.com/en-us/download/details.aspx?id=29062](https://www.microsoft.com/en-us/download/details.aspx?id=29062)) to install free version of Microsoft SQL Exress 2012.

You need to download ENU\\x86\\SQLEXPR\_x86\_ENU.exe or ENU\\x64\\SQLEXPR\_x64\_ENU.exe.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">MetaTrader 5 supports data export both to Microsoft SQL Server 2005/2008/2012/2014/2016 and to their Express versions.</span></li><li class="p_tableatten"><span class="f_tableatten">Microsoft SQL Server Express 2005 has a limit of 4 GB on user data. Microsoft SQL Server Express 2008 R2 / 2012 has a limit of 10 GB. Therefore, it is recommended to use 2008 R2 or 2012 as Express version. If the limit is exceeded, new data will not be added to the database.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Operating system Windows 8 or higher is required for the <a href="https://www.microsoft.com/en-us/download/details.aspx?id=54284" target="_blank" class="weblink">Microsoft SQL 2016</a> installation.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Select 32 or 64-bit considering potential volumes of databases. 64-bit server version is more preferable, as it makes possible to have data caches of bigger volume and has better scalability due to increasing RAM on the server.</span></li></ul></td></tr></tbody></table>

Downloaded distribution kit should be installed in accordance with the instructions. First, select "New SQL Server stand-alone installation or add features to an existing installations" to install a new copy of Microsoft SQL Server. Check the "I accept the license terms" option at "License Terms" step. Leave default parameters at the following steps up to "Server Configuration". Set Automatic mode for "SQL Server Browser" at "Server Configuration" step:

![MSSQL_6_a](/en/docs/mt5/api/img/mssql_6_a.png)

Select "Mixed Mode (SQL Server authentication and Windows authentication)" and specify the administrator password at "Database Engine Configuration" step:

![MSSQL_8_a](/en/docs/mt5/api/img/mssql_8_a.png)

Leave default parameters at the following steps.

TCP/IP should also be enabled for access to SQL Server from the network. To do this, launch "SQL Server Configuration Manager" from the start menu:

![MSSQL_TCP](/en/docs/mt5/api/img/mssql_tcp.png)

Restart SQL Server (SQLExpress) service in SQL Server Services section.

Launch SQLCMD.exe application ("C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\Binn\\OSQL.EXE" or "C:\\Program Files (x86)\\Microsoft SQL Server\\110\\Tools\\Binn\\OSQL.EXE") with the following parameters after installation to create a database:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">SQLCMD.EXE</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-S</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">localhost\SQLEXPRESS</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-U</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">sa</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">-P</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">password</span></p></td></tr></tbody></table>

The password is the same as at "Database Engine Configuration" step. Execute the following command in SQLCMD.exe console:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">CREATE</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">DATABASE</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">METATRADER5</span><br><span class="f_CodeExample">GO</span></p></td></tr></tbody></table>

The database will be generated.

In case backup and MS SQL servers are installed on the same computer, connection settings will be as follows:

![MSSQL_AA](/en/docs/mt5/api/img/mssql_aa.png)

In case backup and MS SQL servers are located on different computers:

![MSSQL_BA](/en/docs/mt5/api/img/mssql_ba.png)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended to install MS SQL and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.</span></p></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">successfully</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">connected</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">to</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">database</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">at</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'localhost\SQLEXPRESS'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">as</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">user</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'sa'</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">version</span><span class="f_CodeExample">&nbsp;11.0.2100.60&nbsp;</span><span class="f_CodeExample">RTM</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">(Express</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Edition)</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">creating</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">created</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">adding</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">added</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">creating</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">created</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">adding</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MSSQL:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">added</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Symbols:</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">symbols</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">and</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">sessions</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">loaded</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">in</span><span class="f_CodeExample">&nbsp;344&nbsp;</span><span class="f_CodeExample">msecs</span><br><span class="f_CodeExample">13</span><span class="f_CodeExample">:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">40&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Symbols:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">synchronization</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

[Installation and Setup of FireBird](/en/docs/mt5/api/sql_export_firebird)

[Installation and Setup of Oracle](/en/docs/mt5/api/sql_export_oracle)