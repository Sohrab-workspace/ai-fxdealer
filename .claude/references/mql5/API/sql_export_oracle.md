# Installation and Setup of Oracle Database

> Source: https://support.metaquotes.net/en/docs/mt5/api/sql_export_oracle

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[SQL Export](/en/docs/mt5/api/sql_export)Installation and Setup of Oracle

# Installation and Setup of Oracle Database

Download the distribution kit from the Oracle's website ([http://www.oracle.com/technetwork/products/express-edition/downloads/index.html](https://www.oracle.com/technetwork/products/express-edition/downloads/index.html)) to install free version of Oracle Database Express Edition. Oracle allows the free use of only the 32-bit version of Express. Therefore, agree to the license terms and download Oracle Database Express Edition 11g Release 2 for Windows x32.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten"><a href="https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package" target="_blank" class="weblink">"Update for Visual C++ 2013 and Visual C++ Redistributable Package"</a> must be installed on the computer where the backup server is installer. Otherwise expert to Oracle databases will not be possible.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Oracle Database Express Edition is limited to 11 GB of user data. If the limit is exceeded, new data will not be added to the database.</span></li></ul></td></tr></tbody></table>

Distribution kit consists of a ZIP archive that should be unpacked into a temporary folder. Then launch DISK1\\setup.exe and follow the instructions:

-   accept the license terms at License Agreement stage;
-   specify administrator password at Specify Database Passwords stage:

![Oracle_4](/en/docs/mt5/api/img/oracle_4.png)

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

![oracle_setting_local](/en/docs/mt5/api/img/oracle_setting_local.png)

In case backup and Oracle servers are located on different computers:

![oracle_setting_remote](/en/docs/mt5/api/img/oracle_setting_remote.png)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Oracle Database Express Edition has only one database named XE. Therefore, that is the database that should be specified in Data Folder parameter.</span></li><li class="p_tableatten"><span class="f_tableatten">It is recommended to install Oracle and backup servers on the same computer for faster export. It should also be kept in mind that the backup server itself also consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backups will work close to necessary DBMS.</span></li></ul></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">successfully</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">connected</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">to</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">database</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'XE'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">at</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'localhost'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">as</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">user</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5user'</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">server</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">version</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Oracle</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Database</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">11g</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Express</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Edition</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Release</span><span class="f_CodeExample">&nbsp;11.2.0.2.0&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Production</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">creating</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">created</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">adding</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">added</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">creating</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">table</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">created</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">adding</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Oracle:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">primary</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">key</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold;">for</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">'mt5_symbols_sessions'</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">added</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Symbols:</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">symbols</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">and</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">sessions</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">loaded</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">in</span><span class="f_CodeExample">&nbsp;203&nbsp;</span><span class="f_CodeExample">msecs</span><br><span class="f_CodeExample">2012.10.18&nbsp;16</span><span class="f_CodeExample">:</span><span class="f_CodeExample">33</span><span class="f_CodeExample">:</span><span class="f_CodeExample">36&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">SQL</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">Export</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">Symbols:</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">synchronization</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">started</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

[Installation and Setup of MS SQL](/en/docs/mt5/api/sql_export_mssql)

[Installation and Setup of PostgreSQL](/en/docs/mt5/api/sql_export_postgre)