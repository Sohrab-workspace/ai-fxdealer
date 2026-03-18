# Installation and Setup of PostgreSQL

> Source: https://support.metaquotes.net/en/docs/mt5/api/sql_export_postgre

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[SQL Export](/en/docs/mt5/api/sql_export)Installation and Setup of PostgreSQL

# Installation and Setup of PostgreSQL

Download the required version of PostgreSQL installer from the [official website](https://www.postgresql.org/download/).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten"><a href="https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package" target="_blank" class="weblink">"Update for Visual C++ 2013 and Visual C++ Redistributable Package"</a> must be installed on the computer where the backup server is installer. Otherwise expert to Oracle databases will not be possible.</span></p></td></tr></tbody></table>

Run the installation file and follow the on-screen instructions. Choose an installation directory an a set of components:

![Installation of PostgreSQL](/en/docs/mt5/api/img/postgre1.gif "Installation of PostgreSQL")

Next, select the directory, in which the databases will be stored, set a password for the administrator account "postgres". Then specify the port at which the PostgreSQL server will listen to incoming connections.

![Installation of PostgreSQL](/en/docs/mt5/api/img/postgre2.gif "Installation of PostgreSQL")

Next, set the [locale](https://postgrespro.com/docs/postgrespro/9.5/locale.html) to be used by by the database cluster. The locale is inherited from the operating system be default. Locale affects the operation of some SQL requests. In the next steps, click "Next", and wait for the installation to complete.

![Installation of PostgreSQL](/en/docs/mt5/api/img/postgre3.gif "Installation of PostgreSQL")

After installation, run the pgAdmin utility from the Start menu. Connect to the server using the postgres login and the password specified during installation. Next, create a database to export information from MetaTrader 5.

![Creating a database in PostgreSQL](/en/docs/mt5/api/img/postgre_db_create.png "Creating a database in PostgreSQL")

Then configure data export on the platform site. In case the backup server and PostgreSQL servers are installed on the same computer, connection parameters should be configured as follows:

![Export settings when installing PostgreSQL on the same computer where the backup server is installed](/en/docs/mt5/api/img/postgres_settings_local.png "Export settings when installing PostgreSQL on the same computer where the backup server is installed")

In case the backup server and PostgreSQL servers are installed on different computers, connection parameters should be configured as follows:

![Export settings when installing PostgreSQL on a separate computer](/en/docs/mt5/api/img/postgres_settings_remote.png "Export settings when installing PostgreSQL on a separate computer")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended to install PostgreSQL and the backup server on the same computer for faster export. However, it should also be kept in mind that the backup server consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backup servers will run close to necessary DBMS.</span></p></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

The backup server will immediately start export into the external DBMS after all settings are specified. Request the log of the appropriate backup server using SQL keyword to track the export process:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2017.12.21&nbsp;15:17:17.154 &nbsp; &nbsp; &nbsp; &nbsp;SQL&nbsp;Export &nbsp; &nbsp; &nbsp; &nbsp;PostgreSQL:&nbsp;server&nbsp;version&nbsp;10.1</span><br><span class="f_CodeExample">2017.12.21&nbsp;15:17:17.156 &nbsp; &nbsp; &nbsp; &nbsp;SQL&nbsp;Export &nbsp; &nbsp; &nbsp; &nbsp;PostgreSQL:&nbsp;successfully&nbsp;connected&nbsp;to&nbsp;database&nbsp;'metatrader5'&nbsp;at&nbsp;'localhost'&nbsp;as&nbsp;user&nbsp;'postgres'</span><br><span class="f_CodeExample">2017.12.21&nbsp;15:17:17.170 &nbsp; &nbsp; &nbsp; &nbsp;SQL&nbsp;Export &nbsp; &nbsp; &nbsp; &nbsp;PostgreSQL:&nbsp;table&nbsp;'mt5_symbols_sessions'&nbsp;creating&nbsp;started</span><br><span class="f_CodeExample">2017.12.21&nbsp;15:17:17.180 &nbsp; &nbsp; &nbsp; &nbsp;SQL&nbsp;Export &nbsp; &nbsp; &nbsp; &nbsp;PostgreSQL:&nbsp;table&nbsp;'mt5_symbols_sessions'&nbsp;created</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

[Installation and Setup of Oracle](/en/docs/mt5/api/sql_export_oracle)

[Internal Data Types](/en/docs/mt5/api/reference_types)