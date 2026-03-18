# Operations with SQL databases

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/database

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
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
        -   [Launch](/en/docs/mt4/metaeditor/open)
        -   [Settings](/en/docs/mt4/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt4/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt4/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt4/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt4/metaeditor/workspace)
        -   [Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)
        -   [MQL4/MQL5 Wizard](/en/docs/mt4/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt4/metaeditor/development)
        -   [Working with SQL data bases](/en/docs/mt4/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt4/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt4/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt4/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt4/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt4/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt4/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt4/metaeditor/video_guides)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)Working with SQL data bases

# Operations with SQL databases

MetaEditor provides options for convenient operations with databases. These capabilities are implemented based on the popular [SQLite](https://www.sqlite.org/index.html) engine integration. The entire database is located in a single file on a user PC's hard disk.

The editor provides access to the main functions for working with databases, allowing you to:

-   Create and connect databases
-   View tables and perform quick data queries
-   Create and execute SQL queries, rollback changes

The development of trading strategies is associated with processing of large amounts of data, and that is why databases are widely used in algo trading. The usage of databases will enable you to:

-   Analyze trading history and quotes
-   Save and analyze optimization and testing results
-   Prepare and exchange data with other analysis packages
-   Store settings and MQL5 program states

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The MQL5 language supports <a href="https://www.mql5.com/ru/docs/database" target="_blank" class="weblink">functions for working with databases</a> directly from your programs. For details please read the article "<a href="https://www.mql5.com/ru/articles/7463" target="_blank" class="weblink">SQLite: Native handling of SQL databases in MQL5</a>".</span></p></td></tr></tbody></table>

## Creating a database [#](database#create_database)

The quick database creation functionality is available from the MQL5 Wizard. You can easily create your first table and define its fields.

![Creating a database via a wizard](/en/docs/mt5/metaeditor/img/database_wizard.png "Creating a database via a wizard")

The following field types are available:

-   integer — integer values
-   real — real values
-   text — string values
-   blob — arrays of binary data

Fields can also be marked with flags:

-   primary — a primary key which uniquely identifies each record in the table. Only one field in a table can be used as a primary key. Values in this field must be unique.
-   unique — a field with values, which cannot be repeated. An attempt to write an already existing value will cause an error. You can use this flag for the fields, which must have unique values. For example, it can be set for a field used for trade tickets.

You can also create databases by using the Navigator context menu:

-   Create database — creates an empty database file of the selected format. The .db extension is used by default.
-   Create from file — create a database based on an existing \*.SQL database.

Once the database is created, you will be redirected to the appropriate Navigator section. All data operations are performed from this section.

## Import tables [#](database#import_table)

You can create tables in a database based on ready-made CSV-files. Click "Import Table" in the database menu, select a file and set the following parameters:

-   Table name in the database.
-   Automatic or manual file encoding detection.
-   Data separator: comma, semicolon, tab, or space.
-   Skipping of the specified number of lines at the beginning.
-   Comment prefix.
-   Whether the file has column names. If you enable this option, values from the first line of the file will be imported as column names.
-   How line breaks will be determined: line feed only (LF, default) or carriage return and line feed (CRLF) characters.
-   Whether data should be added to a new table or to an existing one.
-   Which quotes are used for strings in the file: single or double. Quotes will be removed during import.

![Importing a ready table to a database](/en/docs/mt5/metaeditor/img/database_import_table.png "Importing a ready table to a database")

## Working with the database [#](database#working)

The Navigator provides a separate tab for working with databases. Click "Open" in its context menu or in the "File" menu, and select the database file. Appropriate tables will appear in the Navigator.

Double-click on the table name to quickly query the first 1,000 records.

![Working with the database](/en/docs/mt5/metaeditor/img/database.png "Working with the database")

To execute a database query, enter it in the right part of the editor and click "Execute". In case of a query error, the corresponding message will be added to the [log](/en/docs/mt5/metaeditor/toolbox#journal). An example of a simple query creating a table:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">CREATE&nbsp;TABLE&nbsp;COMPANY(ID&nbsp;INT&nbsp;PRIMARY&nbsp;KEY&nbsp;NOT&nbsp;NULL,&nbsp;NAME&nbsp;TEXT&nbsp;NOT&nbsp;NULL,&nbsp;AGE&nbsp;INT&nbsp;NOT&nbsp;NULL,&nbsp;ADDRESS&nbsp;CHAR(50),&nbsp;SALARY&nbsp;REAL);</span></p></td></tr></tbody></table>

The COMPANY table has 5 fields: Record ID, Name, Age, Address and Salary. The ID field serves as a key. The key enables unique identification of each record and it can be used in different tables to link them together. This is similar to how a position ID links all deals and orders related to a particular position.

If a table column contains time data specified in minutes (UNIX time), seconds or microseconds since 1970.01.01, left-click on it and select the required format. After that, the time will be displayed in the usual format, YYYY.MM.DD hh:mm:ss.

To save a table as a file, query all data from the table using a query "SELECT \* FROM \[table name\]", and then click "Export" in the context menu. The export operation provides the same table options as [import](/en/docs/mt5/metaeditor/database#import_table).

[OpenCL support](/en/docs/mt4/metaeditor/opencl)

[Working with machine learning models](/en/docs/mt4/metaeditor/machine_learning)