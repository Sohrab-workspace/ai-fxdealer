# SQL Export

> Source: https://support.metaquotes.net/en/docs/mt5/api/sql_export

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)SQL Export

# SQL Export

The MetaTrader 5 trading platform provides standard options for the real-time data export to MySQL, Microsoft SQL Server, FireBird, Oracle, MariaDB and PostgreSQL databases. This option enables the quick and easy deployment of data export to an external DBMS for using the platform data in any popular programming language and third-party applications. Thus, it is possible to create an intermediate layer between a trade server and broker's program services that regularly access trading data. This reduces the load on the trade server when it receives the current trading data.

The export function is enabled by simple specification of settings for connection to DBMS via MetaTrader 5 Administrator. After that, the backup server will immediately perform an initial synchronization of data from the DBMS. Further, new data will be exported to the DBMS in real time. The following data is exported:

-   Information about clients (general information and trading status)
-   Current active orders and positions
-   The history of orders and deals
-   Current prices
-   Virtually all settings of the trading platform (except for the working time, synchronization and spreads)

The description of installation and setup of popular databases is provided in appropriate subsections:

-   [MySQL Server 5.7](/en/docs/mt5/api/sql_export_mysql) (supported versions: 5.1, 5.5, 5.6, 5.7, 8.0, 8.1)
-   [MariaDB 10.2](/en/docs/mt5/api/sql_export_maria) (all version supported)
-   [Microsoft SQL Express 2012](/en/docs/mt5/api/sql_export_mssql) (supported versions: 2005, 2008, 2008 R2, 2012, 2014, 2016, 2017, 2019, 2022)
-   [Oracle Database Express Edition 11g](/en/docs/mt5/api/sql_export_oracle) (supported versions: 11g/11g Express Edition, 12c, 18c, 19c, 21c, 23ai)
-   [PostgreSQL](/en/docs/mt5/api/sql_export_postgre) (supported versions: 8.4 — 17)

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

A detailed description of exported tables can be found in the [MetaTrader 5 Administrator User Guide](https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/sql_export).

## Your own data in MetaTrader 5 tables

In the platform, you can create your own tables and databases, add your own fields in mt5\_\* tables, which are used for data export, as well as create stored procedures and triggers.

-   The backup server does not recreate data, but only adds or updates existing records. A table entry is only deleted if the appropriate entry is deleted on the platform side. For example, if a user is added to the mt5\_users tables, the appropriate user record will exist in the database until the user is deleted from MetaTrader 5.
-   The backup server only works with its own tables and fields.
-   The backup server does not create default indexes. Each index is an extra load on the database, which can slow down exports and information updates.
-   When you create your own fields in mt5\_\* tables, do not forget to set default values for them (or allow NULL). Otherwise, the backup server will not be able to add new entries to the tables.

[WebTrader](/en/docs/mt5/api/webapi_main/net/net_webtrader)

[Installation and Setup of MySQL](/en/docs/mt5/api/sql_export_mysql)