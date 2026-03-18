# Installation and Setup of MariaDB

> Source: https://support.metaquotes.net/en/docs/mt5/api/sql_export_maria

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[SQL Export](/en/docs/mt5/api/sql_export)Installation and Setup of MariaDB

# Installation and Setup of MariaDB

To install MariaDB, download the required version from the official product website [https://downloads.mariadb.org/](https://downloads.mariadb.org/). At the time, the platform supports all available MariaDB versions.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Choose between 32-bit and 64-bit versions based on the evaluated potential volume of data bases. The 64-bit server version is more preferable, as it makes possible to have data caches of more than 2 Gb and has better scalability due to increasing RAM on the server.</span></p></td></tr></tbody></table>

Run the installation file and follow the on-screen instructions. The below example shows the installation of MariaDB 10.2 (x64).

![MariaDB Installation](/en/docs/mt5/api/img/mariadb_install.gif "MariaDB Installation")

After selecting components for the installation (you can install with default settings), specify the password for the "root" administrator account. For security reasons, it is recommended that you do not allow the use of the "root" account during remote connections (leave the "Enable root access from remote machines" option disabled). Instead, after installing the MariaDB server and creating a scheme (database) for working with MetaTrader 5, create a separate account with access only to the desired schema, and allow remote connections to it.

It is also recommended to enable the "Use UTF8 as default server's character set" option.

Then, specify network settings (default settings can be used) and the parameter for sending anonymous reports on the DBMS operation (can be disabled). After that, start the installation process and wait for it to finish.

![MariaDB Installation](/en/docs/mt5/api/img/mariadb_install2.gif "MariaDB Installation")

Now create a schema (a database) to which data from MetaTrader 5 will be exported. To do this, launch the MySQL Client (MariaDB) program from the Start menu. In the window that appears, enter the password for the "root" account and press Enter. Then enter a command to create a data base, e.g. "create schema metatrader5;". Here "metatrader5" is the name of the schema. You can use any other name.

![Creating a schema for exporting data from MetaTrader 5](/en/docs/mt5/api/img/mariadb_create_db.png "Creating a schema for exporting data from MetaTrader 5")

Next, configure data export on the MetaTrader 5 side. If the backup server and the MariaDB server are installed on the same computer, the following settings will be used:

![Export settings when installing MariaDB on the same computer where the backup server is installed](/en/docs/mt5/api/img/mariadb_setting_local.png "Export settings when installing MariaDB on the same computer where the backup server is installed")

If the database is installed separately from the backup server, specify its address in the "Server" field. In the Login and Password fields, specify he details of the account that has access to the required schema and is allowed for use during remote connection.

![Export settings when installing MySQL on a separate computer](/en/docs/mt5/api/img/mariadb_setting_remote.png "Export settings when installing MySQL on a separate computer")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended to install MariaDB and the backup server on the same computer for faster export. However, it should also be kept in mind that the backup server consumes resources. Also, remember that it is possible to deploy several backups for a trade server. These backup servers will run close to necessary DBMS.</span></p></td></tr></tbody></table>

Additional export parameters can be selected at [SQL Options](https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_backup_server#sql_settings) tab.

[Installation and Setup of MySQL](/en/docs/mt5/api/sql_export_mysql)

[Installation and Setup of FireBird](/en/docs/mt5/api/sql_export_firebird)