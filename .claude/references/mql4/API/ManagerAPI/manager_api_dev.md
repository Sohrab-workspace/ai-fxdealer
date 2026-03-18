# Application Development

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_dev

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
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
        -   [Development Features](/en/docs/mt4/api/features)
        -   [Structures](/en/docs/mt4/api/reference_structures)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
        -   [Manager API](/en/docs/mt4/api/manager_api)
            -   [Application Development](/en/docs/mt4/api/manager_api/manager_api_dev)
            -   [Exported Functions and Factory](/en/docs/mt4/api/manager_api/manager_api_exported_factory)
            -   [Common Functions](/en/docs/mt4/api/manager_api/manager_api_common)
            -   [Connecting to the Server](/en/docs/mt4/api/manager_api/manager_api_connect)
            -   [Configuration Databases](/en/docs/mt4/api/manager_api/manager_api_config)
            -   [Server Management](/en/docs/mt4/api/manager_api/manager_api_server)
            -   [Price Data](/en/docs/mt4/api/manager_api/manager_api_chart)
            -   [Data Feeds](/en/docs/mt4/api/manager_api/manager_api_feeder)
            -   [Backup](/en/docs/mt4/api/manager_api/manager_api_backup)
            -   [Trading](/en/docs/mt4/api/manager_api/manager_api_trade)
            -   [Dealings](/en/docs/mt4/api/manager_api/manager_api_dealer)
            -   [Users](/en/docs/mt4/api/manager_api/manager_api_user)
            -   [Online Connections](/en/docs/mt4/api/manager_api/manager_api_online)
            -   [Symbols](/en/docs/mt4/api/manager_api/manager_api_symbol)
            -   [Mail, News and Notifications](/en/docs/mt4/api/manager_api/manager_api_newsmail)
            -   [Reports](/en/docs/mt4/api/manager_api/manager_api_report)
            -   [Summary Positions](/en/docs/mt4/api/manager_api/manager_api_summary)
            -   [Exposure](/en/docs/mt4/api/manager_api/manager_api_exposure)
            -   [Protocol Extension](/en/docs/mt4/api/manager_api/manager_api_extension)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Application Development

# Application Development

MetaTrader 4 Manager API is a library in the form of a DLL file that contains the full set of administrator and manager commands for accessing MetaTrader 4 Server. With the Manager API, you can develop our own administrator and manager tools or even your own manager terminal.

The Manager API library and API use examples are distributed together with the MetaTrader Administrator terminal and are available in the \\api directory. New versions of the Manager API are added to the LiveUpdate system and are automatically downloaded together with other components. The Manager API is provided with a few examples and their source code: ManagerAPIAdmin - use of administrator functions; ManagerAPISample - use of manager functions, pumping, dealing; ManagerAPITrade - an example of a manager's trade transaction; DelphiSample - an example of API use in Delphi environment; DelphiPumping - use of pumping in Delphi environment.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The 64 bit version of the Manager API library (mtmanapi64.dll) is not supported and is provided "as is". The following functions are not available in the 64 bit version: MailsRequest, MailSend, NewsSend, NewsGet, NewsTopicGet and NewsBodyGet. For more reliable performance, use the 32 bit version (mtmanapi.dll).</span></p></td></tr></tbody></table>

## Exported Functions and Manager Interface

The entire API is described in one header file MT4ManagerAPI.h, ManagerAPI.pas file is used in examples for Delphi. The Manager API library exports two simple functions:

-   [MtManVersion](/en/docs/mt4/api/manager_api/manager_api_exported_factory/manager_api_mtmanversion) - returns the version and build of the API library, the higher word means API version, the lower one means its build. In order to select the version and build from the returned value, you may use HIWORD and LOWORD macros.
-   [MtManCreate](/en/docs/mt4/api/manager_api/manager_api_exported_factory/manager_api_mtmancreate) - creates and returns an instance of the manager interface; returns null if the interface creation fails, otherwise returns a non-zero value.

The MT4ManagerAPI.h file includes a manager interface factory [CManagerFactory](/en/docs/mt4/api/manager_api/manager_api_exported_factory), which automatically loads the mtmanapi.dll library, enables initialization of the WinSocks library, as well as provides wrappers for the exported functions MtManVersion and MtManCreate.

The CManagerInterface class is a manager interface - a set of administrator and manager functions for accessing the MetaTrader Server. Each manager interface can be in three states:

-   Direct connection to a server - can be used for configuring server through administrator commands, for working with backups, for a direct access to server databases, for changing symbol settings, as well as for sending emails, news, etc.
-   Pumping - connection in data pumping mode, the manager interface sparingly receives database updates from the server and sends notification about updated data to a custom program.
-   Dealing - connection in client request processing mode, the manager interface program sends notifications about new trade requests to a custom program and sends dealer responses to a server.

After the creation of a manager interface, a program can call the WorkingDirectory function for setting a working directory of API, in which symbol settings, received emails and API logs will be stored. If an error occurs, the ErrorDescription function returns a text description of the error. After completing operation with the manager interface, it is necessary to call the Release function in order to delete a previously created manager interface.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Many functions of the manager interface, such as <a href="/en/docs/mt4/api/manager_api/manager_api_config/manager_api_config_firewall/cmanagerinterface_cfgrequestaccess" class="topiclink">CfgRequestAccess</a> or <a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersrequest" class="topiclink">UsersRequest</a>, return a pointer to a data array, which should be released after use by using the <a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_memfree" class="topiclink">MemFree</a> function.</span></p></td></tr></tbody></table>

## Connection and Authentication [#](manager_api_dev#connect)

Connection to a server is performed using the [Connect](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_connect) function, which received the server address in the "server:port" format, or uses the default port 443 if the port number is not specified. The [Disconnect](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_disconnect) function is used for disconnecting from the server. The [IsConnected](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_isconnected) function is used for checking the connection state and returns a non-zero value if the manager interface is connected to a server; otherwise it returns null.

Authentication on the server is performed using the [Login](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_login) function. Only an account from the 'manager' group, for which permissions are specified in the MetaTrader Administrator in Managers section, can connect using the Manager API.

Aft authentication on the server, it is possible to change the password of the manager's account using the [PasswordChange](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_passwordchange) function, as well as to receive own permissions using [ManagerRights](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_managerrights), receive the server time using [ServerTime](/en/docs/mt4/api/manager_api/manager_api_server/cmanagerinterface_servertime) or check connection to a server using the [Ping](/en/docs/mt4/api/manager_api/manager_api_connect/cmanagerinterface_ping) function.

## Administrator Commands [#](manager_api_dev#admin)

Manager API provides a number of functions, for the successful implementation of which the manager account needs to have administrator rights.

The manager interface includes four functions that send [server operation control commands](/en/docs/mt4/api/manager_api/manager_api_server):

-   [SrvRestart](/en/docs/mt4/api/manager_api/manager_api_server/cmanagerinterface_srvrestart) - restarts the MetaTrader Server;
-   [SrvChartsSync](/en/docs/mt4/api/manager_api/manager_api_server/cmanagerinterface_srvchartssync) - synchronizes history data;
-   [SrvLiveUpdateStart](/en/docs/mt4/api/manager_api/manager_api_server/cmanagerinterface_srvliveupdatestart) - starts Live Update;
-   [SrvFeedsRestart](/en/docs/mt4/api/manager_api/manager_api_feeder/cmanagerinterface_srvfeedsrestart) - restarts data feeds.

It is possible to expand the functionality of the server by adding the commands that must be implemented by server-side plugins. During the call of the [ExternalCommand](/en/docs/mt4/api/manager_api/manager_api_extension/cmanagerinterface_externalcommand) function of the manager terminal, the server passes the received command to the plugins that export the [MtSrvManagerProtocol](/en/docs/mt4/api/server_api/server_api_hook/server_api_hook_extension/mtsrvmanagerprotocol) function.

The manager interface includes a set of [functions for editing server settings](/en/docs/mt4/api/manager_api/manager_api_config):

-   CfgRequest\* - requests server settings;
-   CfgUpdate\* - edits a record of the server configuration;
-   CfgDelete\* - deletes a record of the server configuration;
-   CfgShift\* - moves a record of the server configuration.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In order to use the Cfg* methods, the manager account needs to have the Administrator permission (<a href="/en/docs/mt4/api/reference_structures/structure_config/conmanager" class="topiclink">ConManager::admin</a>).</span></p></td></tr></tbody></table>

The list of all data feeds available on the server can be requested using the [SrvFeeders](/en/docs/mt4/api/manager_api/manager_api_feeder/cmanagerinterface_srvfeeders) function. [SrvFeederLog](/en/docs/mt4/api/manager_api/manager_api_feeder/cmanagerinterface_srvfeederlog) allows to request the logs of a configured data feed based on its name.

The manager interface contains functions for managing history database of the server:

-   [ChartRequest](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartrequest) - requests history data of a symbol and period starting with a selected date;
-   [ChartAdd](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartadd) - adds bars to the history database;
-   [ChartUpdate](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartupdate) - updates bars in the history database;
-   [ChartDelete](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartdelete) - deletes bars from the history database.

The performance base of the server can be accessed using the [PerformanceRequest](/en/docs/mt4/api/manager_api/manager_api_server/cmanagerinterface_performancerequest) function. A custom program that uses the API Manager, after the first request of the server performance, must maintain its own local database of performance and only request missing data when necessary. Requesting the entire database of the server performance from time to time is not allowed.

The manager interface includes administrator functions for accessing the current server databases:

-   [AdmUsersRequest](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admusersrequest) - requests accounts of the current database; you can specify a comma separated list of groups or accounts in the request string;
-   [AdmTradesRequest](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_admtradesrequest) - requests orders from the current database; you can specify a comma separated list of groups, accounts or orders in the request string;
-   [AdmTradesDelete](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_admtradesdelete) - deletes orders from the current database;
-   [AdmTradeRecordModify](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_admtraderecordmodify) - modifies order in the current database;
-   [AdmBalanceCheck](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admbalancecheck) - checks balances of a list of accounts;
-   [AdmBalanceFix](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admbalancefix) - corrects balances of a list of accounts in accordance with the trading history.

The manager interface contains functions for working with the backups of accounts and orders:

-   [BackupInfoUsers](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backupinfousers) - requests a list of backup files of the database of users;
-   [BackupInfoOrders](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backupinfoorders) - requests a list of backup files of the database of orders;
-   [BackupRequestUsers](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprequestusers) - requests accounts from a certain backup file; you can specify a comma separated list of groups or accounts in the request string;
-   [BackupRequestOrders](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprequestorders) - requests orders from a certain backup file; you can specify a comma separated list of groups or accounts in the request string;
-   [BackupRestoreUsers](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprestoreusers) - recovers accounts from backup;
-   [BackupRestoreOrderss](/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprestoreorders) - recovers orders from backup.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">After recovering accounts or orders from backups, it is necessary to adjust balances of restored accounts by calling the AdmBalanceFix function.</span></li><li class="p_tableatten"><span class="f_tableatten">Many administrator functions, such as <a href="/en/docs/mt4/api/manager_api/manager_api_config/manager_api_config_firewall/cmanagerinterface_cfgrequestaccess" class="topiclink">CfgRequest*</a>, <a href="/en/docs/mt4/api/manager_api/manager_api_feeder/cmanagerinterface_srvfeeders" class="topiclink">SrvFeeders</a>, <a href="/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_chartrequest" class="topiclink">ChartRequest</a>, <a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backupinfoorders" class="topiclink">BackupInfo*</a>, <a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprequestusers" class="topiclink">BackupRequest*</a>, <a href="/en/docs/mt4/api/manager_api/manager_api_backup/cmanagerinterface_backuprestoreorders" class="topiclink">BackupRestoreOrders</a>, <a href="/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_admusersrequest" class="topiclink">AdmUsersRequest</a>, <a href="/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_admtradesrequest" class="topiclink">AdmTradesRequest</a>, return a pointer to a data array, which should be released after use by using the MemFree function.</span></li></ul></td></tr></tbody></table>

## Symbols [#](manager_api_dev#symbols)

The list of all available symbols can be requested from the server using the [SymbolsRefresh](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsrefresh) function. During the first call, the function downloads the full list of symbols from the server. The list is saved as 'symbols.raw' in the working directory of Manager API. During further calls, symbols are only downloaded when there are changes in symbol settings as compared with the saved list. Settings of requested symbols or a selected symbol can be obtained using the [SymbolsGetAll](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsgetall) and [SymbolGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolget) functions. Settings of symbol groups can be obtained using the [SymbolsGroupsGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsgroupsget) function.

In addition to the full list of symbols, the manager interface supports the list of selected symbols; in the pumping mode, the manager interface receives updates of quotes only for the symbols that are in the list of selected symbols. You can add a symbol to the list by using the [SymbolAdd](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symboladd) function, while the [SymbolHide](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolhide) function deletes a symbol from the list of selected ones. Short description of a selected symbol can be accessed using the [SymbolInfoGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolinfoget) function.

If a manager's account has the 'market watch' permission, the [SymbolChange](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolchange) function can be used fir editing spread, execution mode, limit & stop levels and the background color of a selected symbol. Using the [SymbolSendTick](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsendtick) function, it is possible to add a quote into the stream of quotes provided by a data feed.

## Direct Access to Server Databases [#](manager_api_dev#database)

The manager interface includes a number of functions for a a direct request and editing of server databases.

The [GroupsRequest](/en/docs/mt4/api/manager_api/manager_api_config/manager_api_config_group/cmanagerinterface_groupsrequest) function of the manager interface allows requesting a list of available account groups. The list of all accounts can be requested using the [UsersRequest](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersrequest) function, the list of selected accounts can be requested using [UserRecordsRequest](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordsrequest), the list of connected clients can be requested using OnlineRequest. The [UserRecordNew](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordnew) function allows allocating a new account, [UserRecordUpate](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordupdate) allows changing account data. [UsersGroupOp](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersgroupop) is used for group operations with a list of accounts: deleting accounts, enabling accounts, blocking accounts, editing leverage of the group of a list of accounts. [UserPasswordCheck](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userpasswordcheck) is used for checking an account password. The [UserPasswordSet](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userpasswordset) function changes the master or investor password of an account, as well as allows to reset a public key on the server if extended authentication is used - in this case the server will request a new key from the client during the next connection.

The list of all orders can be requested using [TradesRequest](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradesrequest), the list of selected orders can be requested using [TradeRecordsRequest](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_traderecordsrequest), [TradesUserHistory](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradesuserhistory) requests a trading history of a selected account.

The manager interface allows you to open an order, to close an order or to modify an open order by using the [TradeTransaction](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradetransaction) function. After opening a new order or performing a balance operation, the ticket of the new order will be returned in a field of the [TradeTransInfo::order](/en/docs/mt4/api/reference_structures/structure_trade/tradetransinfo) parameter. When necessary, the [TradeCheckStops](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_service/cmanagerinterface_tradecheckstops) function allows you to check the stoploss/takeprofit levels and the pending order opening price passed in TradeTransInfo, as well as 'price' passed as the second parameter, compliance with the Limit & Stop level, which is set in the Administrator for each symbol ([ConSymbol::stops\_level](/en/docs/mt4/api/reference_structures/structure_config/consymbol)). The expiration of a pending order is also checked (should not be closer than 10 minutes from the current time).

Through the manager interface, you can request the list of closed positions, based on which you can form a report for a set of accounts using the [ReportsRequest](/en/docs/mt4/api/manager_api/manager_api_report/cmanagerinterface_reportsrequest) function. Daily requests formed on the server for a list of accounts can be requested using the [DailyReportsRequest](/en/docs/mt4/api/manager_api/manager_api_report/cmanagerinterface_dailyreportsrequest) function. When requesting reports, the request period (field from and to of the structures [ReportGroupRequest](/en/docs/mt4/api/reference_structures/structure_report/reportgrouprequest) and [DailyGroupRequest](/en/docs/mt4/api/reference_structures/structure_report/dailygrouprequest)) should be set to the beginning and end of a trading day on the server ([ConCommon::endhour](/en/docs/mt4/api/reference_structures/structure_config/concommon), [ConCommon::endminute](/en/docs/mt4/api/reference_structures/structure_config/concommon)). For example, when you request reports for the current trading day from the server, on which the time of the trading day end is 23:59, you can use the following code:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">ReportGroupRequest</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">req={"some_group"};</span><br><span class="f_CodeExample">req.from=(time(NULL)/86400)*86400;</span><br><span class="f_CodeExample">req.to</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">=req.from+86400;</span><br><span class="f_CodeExample">...</span></p></td></tr></tbody></table>

The manager interface allows you to request the last emails of internal email system using MailsRequest functions, send an email via the internal mailing system using the MailSend function, add a newsletter into the news stream using NewsSend function, as well as change the configuration of the server using the PluginUpdate function. The JournalRequest function allows requesting server logs of a selected period.

## Pumping [#](manager_api_dev#pumping)

Pumping is a resource saving operational mode for data pumping from a server. When switched to pumping, the manager interface requests settings of symbols, groups, account database, orders and trade requests from the server, and then the server only sends data updates to the connected manager. After connection to the server, the manager interface can be switched to the pumping mode using the [PumpingSwitch](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_pumpingswitch) function. As a parameter to the function, you should pass a pointer to the callback function, which will be called by the manager interface for notifying about data update, or the handle of the window and custom message ID, to which notifications about data updates will be sent. Only the functions described below can be called for the manager interface in the pumping mode.

After calling PumpingSwitch, the Manager interface will send the following codes as a parameter to the callback function or as WPARAM parameter of a user message:

-   PUMP\_START\_PUMPING - the Manager interface has successfully switched to the pumping mode;
-   PUMP\_UPDATE\_SYMBOLS - symbol settings have been updated, the updated settings can be obtained using the functions [SymbolsGetAll](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolsgetall), [SymbolGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolget) or [SymbolInfoGet](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolinfoget);
-   PUMP\_UPDATE\_GROUPS - group settings have been updated, the updated settings can be obtained using the functions [GroupsGet](/en/docs/mt4/api/manager_api/manager_api_config/manager_api_config_group/cmanagerinterface_groupsget) or [GroupRecordGet](/en/docs/mt4/api/manager_api/manager_api_config/manager_api_config_group/cmanagerinterface_grouprecordget);
-   PUMP\_UPDATE\_USERS - the list of accounts has been updated, the updated list can be obtained using the functions [UsersGet](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_usersget) or [UserRecordGet](/en/docs/mt4/api/manager_api/manager_api_user/cmanagerinterface_userrecordget);
-   PUMP\_UPDATE\_ONLINE - the list of online clients has been updated, the updated list of online clients can be obtained using the functions [OnlineGet](/en/docs/mt4/api/manager_api/manager_api_online/cmanagerinterface_onlineget) or [OnlineRecordGet](/en/docs/mt4/api/reference_structures/structure_user/onlinerecord);
-   PUMP\_UPDATE\_BIDASK - a new quote has been received, the received quotes can be obtained using the [TickInfoLast](/en/docs/mt4/api/manager_api/manager_api_chart/cmanagerinterface_tickinfolast) function, the last prices can be obtained using one or more calls of the [SymbolInfoUpdated](/en/docs/mt4/api/manager_api/manager_api_symbol/cmanagerinterface_symbolinfoupdated) function;
-   PUMP\_UPDATE\_NEWS - a newsletter has been received, the headers of the received newsletters can be obtained using the functions [NewsGet](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsget), [NewsTotal](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newstotal) and [NewsTopicGet](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newstopicget); the body of a received newsletter can be requested using the [NewsBodyRequest](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsbodyrequest) function;
-   PUMP\_UPDATE\_NEWS\_BODY - a news body has been received, the news body can be obtained using the [NewsBodyGet](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_newsbodyget) function;
-   PUMP\_UPDATE\_MAIL - a new email has been received, it has been saved to a disk in the 'mailbox\\' folder of the Manager API working directory; the name of the file and the size of the email can be obtained using the [MailLast](/en/docs/mt4/api/manager_api/manager_api_newsmail/cmanagerinterface_maillast) function;
-   PUMP\_UPDATE\_TRADES - the list of orders has been updated, the updated list of orders can be obtained using the functions [TradesGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradesget) (all orders), [TradesGetBySymbol](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradesgetbysymbol) (orders of one symbol), [TradesGetByLogin](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradesgetbylogin) (orders of one account), [TradesGetByMarket](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradesgetbymarket) (all orders sorted by distance from the market) and [TradeRecordGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_traderecordget) (a specific order with the specified ticket). Trade results on symbols and groups of symbols can be obtained using the functions [SummaryGetAll](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetall), [SummaryGet](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summaryget), [SummaryGetByCount](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetbycount) and [SummaryGetByType](/en/docs/mt4/api/manager_api/manager_api_summary/cmanagerinterface_summarygetbytype). Company's exposure on currencies can be obtained using the functions [ExposureGet](/en/docs/mt4/api/manager_api/manager_api_exposure/cmanagerinterface_exposureget) and [ExposureValueGet](/en/docs/mt4/api/manager_api/manager_api_exposure/cmanagerinterface_exposurevalueget);
-   PUMP\_UPDATE\_REQUESTS - the list of trade requests has been updated, the updated list of trade requests can be obtained using the functions [RequestsGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_request/cmanagerinterface_requestsget) and [RequestInfoGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_request/cmanagerinterface_requestinfoget);
-   PUMP\_UPDATE\_PLUGINS - the list of server plugins has been updated, the updated list of plugins can be obtained using the functions [PluginsGet](/en/docs/mt4/api/manager_api/manager_api_config/manager_api_config_plugin/cmanagerinterface_pluginsget) and [PluginParamGet](/en/docs/mt4/api/manager_api/manager_api_config/manager_api_config_plugin/cmanagerinterface_pluginparamget);
-   PUMP\_UPDATE\_ACTIVATION - the list of orders with triggered Stop Loss or Take Profit levels, pending orders, and the most unprofitable orders for accounts in the stop out state has been updated;
-   PUMP\_UPDATE\_MARGINCALL - the list of accounts with the margin call state has been updated, the updated list of account margin requirements can be obtained using [MarginsGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_margin/cmanagerinterface_marginsget) and [MarginLevelGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_margin/cmanagerinterface_marginlevelget);
-   PUMP\_STOP\_PUMPING - the pumping mode has been stopped.
-   PUMP\_UPDATE\_NEWS\_NEW - a newsletter of the new [NewsTopicNew](/en/docs/mt4/api/reference_structures/structure_news_mail/newstopicnew) format has been received.

## Extended Pumping [#](manager_api_dev#pumping_ext)

In addition to the standard pumping mode, in which only notifications about data changes are received, a special mode is available, in which the received transactions are played. In this mode there is possible to obtain information about the changed client and order records, as well as about changes in group and symbol settings.

In order to switch to the extended pumping mode, you may use the [PumpingSwitchEx](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_pumpingswitchex) function. After switching to the expanded pumping mode, the callback function will be called:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">__stdcall</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">NotifyCallBack(</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">code,</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">type,</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">void</span><span class="f_CodeExample">*</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">data,</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">*param)</span></p></td></tr></tbody></table>

The callback function receives the following data as a parameter:

-   code - the type of change.
-   type - transaction type:
    -   TRANS\_ADD - add.
    -   TRANS\_DELETE - delete.
    -   TRANS\_UPDATE - update.
    -   TRANS\_CHANGE\_GRP - change group. It is sent to all managers to notify them that the client account has become available or, conversely, unavailable to them after the client group has changed.
-   data - a pointer to the updated data: the pointer type depends on the type of change.
-   param - the pointer that was passed as a parameter to the PumpingSwitchEx function.

Below is the correspondence between 'code' and the type of 'data' pointer:

-   PUMP\_UPDATE\_USERS - the [UserRecord](/en/docs/mt4/api/reference_structures/structure_user/userrecord) structure
-   PUMP\_UPDATE\_ONLINE - client's login as int
-   PUMP\_UPDATE\_TRADES - the [TradeRecord](/en/docs/mt4/api/reference_structures/structure_trade/traderecord) structure
-   PUMP\_UPDATE\_NEWS - the [NewsTopic](/en/docs/mt4/api/reference_structures/structure_news_mail/newstopic) or [NewsTopicNew](/en/docs/mt4/api/reference_structures/structure_news_mail/newstopicnew) structure
-   PUMP\_UPDATE\_MAIL - the [MailBox](/en/docs/mt4/api/reference_structures/structure_news_mail/mailboxheader) structure
-   PUMP\_UPDATE\_SYMBOLS - the [ConSymbol](/en/docs/mt4/api/reference_structures/structure_config/consymbol) structure
-   PUMP\_UPDATE\_GROUPS - the [ConGroup](/en/docs/mt4/api/reference_structures/structure_config/congroup) structure
-   PUMP\_UPDATE\_REQUESTS - the [RequestInfo](/en/docs/mt4/api/reference_structures/structure_trade/requestinfo) structure

Below is an example of receiving notification about changes in trade records:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(manager-&gt;PumpingSwitchEx(PumpingNotify,0,NULL)!=RET_OK)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">printf("pumping&nbsp;switch&nbsp;error");</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">__stdcall</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">PumpingNotify(</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">code,</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">type,</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">*data,</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">void</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">*param)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #339966;">//---&nbsp;checks</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(code==PUMP_UPDATE_TRADES</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">&amp;&amp;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">data!=NULL)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">TradeRecord</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">*trade=(TradeRecord*)data;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #339966;">//---</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">switch</span><span class="f_CodeExample">(type)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">case</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">TRANS_ADD:</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">printf("#%d&nbsp;added",trade-&gt;order);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">break</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">case</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">TRANS_DELETE:</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">printf("#%d&nbsp;closed",trade-&gt;order);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">break</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">case</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">TRANS_UPDATE:</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(trade-&gt;login==0)</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">printf("#%d&nbsp;deleted",trade-&gt;order);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">else</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">printf("#%d&nbsp;updated",trade-&gt;order);</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">break</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

## Processing Stop and Pending Orders [#](manager_api_dev#stops_pendings)

In pimping mode, upon trigger of Stop Loss or Take Profit, the manager interface sends the PUMP\_UPDATE\_ACTIVATION notification to the client program. After the call of [TradesGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradesget), appropriate activation flags will be added to the TradeRecord::activation fields of the updated records: ACTIVATION\_SL, ACTIVATION\_TP or ACTIVATION\_PENDING. If the price has rolled back from the order activation level, flags ACTIVATION\_SL\_ROLLBACK, ACTIVATION\_TP\_ROLLBACK or ACTIVATION\_PENDING\_ROLLBACK will be added. Processing of a triggered Stop Loss or Take Profit, as well as opening of a pending order can be performed using TradeTransaction. If for some reason there is no need to execute an order after the rollback of a price, the [TradeClearRollback](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradeclearrollback) function allows to remove activation flags ACTIVATION\_SL\_ROLLBACK, ACTIVATION\_TP\_ROLLBACK and ACTIVATION\_PENDING\_ROLLBACK from the order database of the manager interface.

# Margin Requirements and Stop-Out Processing

When switched to pumping, the manager interface can also requests settings of groups and full databases of accounts and orders, and then the databases are efficiently updated when the updates are received from the server. Based on the requested data, the manager interface calculates the margin requirements of accounts. In order to save resources, the margin requirements are only calculated for the accounts that have open positions. For the accounts that didn't have any open positions during the connection session, [MarginLevelGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_margin/cmanagerinterface_marginlevelget) returns RET\_ERROR, while margin=0, equity=margin\_free=UserRecord::balance+UserRecord::credit. Each time one or more accounts enter or exit the Margin Call state, the manager interface in the pumping mode sends the PUMP\_UPDATE\_MARGINCALL notification to the client program.

Since margin requirements (MarginLevel::margin) are only changed when a position is opened or closed, [MarginsGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_margin/cmanagerinterface_marginsget) should be called upon receiving the PUMP\_UPDATE\_TRADES notification. Usually it is necessary to only monitor accounts in the Margin Call or Stop Out mode. Here MarginsGet can be called even more rarely - upon receipt of the PUMP\_UPDATE\_MARGINCALL notification, then delete normal margin levels from the returned array (levels for which MarginLevel::level\_type==MARGINLEVEL\_OK). Upon receipt of PUMP\_UPDATE\_TRADES, only update the remaining margin requirements of logins by calling [MarginLevelGet](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_margin/cmanagerinterface_marginlevelget). The database of margin requirements is indexed by logins, therefore few calls of MarginLevelGet is better than calls of MarginsGet, which copies a large data array for all accounts. If you need to monitor free margin (MarginLevel::margin\_free) and the margin level (MarginLevel::margin\_level), you can also call MarginLevelGet on each tick (PUMP\_UPDATE\_BIDASK).

When one or more accounts enter or exit the Stop Out state, the manager interface automatically finds the most losing orders of such accounts and adds the ACTIVATION\_STOPOUT or ACTIVATION\_STOPOUT\_ROLLBACK flag to the TradeRecord::activation field. After that the manager interface sends the PUMP\_UPDATE\_ACTIVATION notification to the client program. After receiving this notification, the client program can request all orders using the TradesGet function and then find orders with the ACTIVATION\_STOPOUT or ACTIVATION\_STOPOUT\_ROLLBACK flag from the list and close them. If for some reason there is no need to close the order, the TradeClearRollback function allows you to remove order activation flags ACTIVATION\_STOPOUT\_ROLLBACK from the database of orders of the manager interface.[TradeClearRollback](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_order/cmanagerinterface_tradeclearrollback)

If you want to handle Stop Out using a method other than closing the most unprofitable position, then, after receiving PUMP\_UPDATE\_MARGINCALL, you should request a list of margin levels, find levels in the MARGINLEVEL\_STOPOUT state from the received list, then request a list of positions of the found logins using TradesGetByLogin and then find and close the desired position in accordance with the Stop Out processing rules.

## Profit Calculation [#](manager_api_dev#profit)

In the pumping mode, it is possible to calculate the profits of an order. This can be done by using the [TradeCalcProfit](/en/docs/mt4/api/manager_api/manager_api_trade/manager_api_trade_service/cmanagerinterface_tradecalcprofit) method. Here is an example of profit calculation for an order BUY 1.00 EURUSD with the open price of 1.0000 and the close price of 1.2000 for the client 5555:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">TradeRecord</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">trade={0};</span><br><span class="f_CodeExample">COPY_STR(trade.symbol,"EURUSD");</span><br><span class="f_CodeExample">trade.login</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">=5555;</span><br><span class="f_CodeExample">trade.volume</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">=100;</span><br><span class="f_CodeExample">trade.cmd</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">=OP_BUY;</span><br><span class="f_CodeExample">trade.open_price</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">=1.0000;</span><br><span class="f_CodeExample">trade.close_price=1.2000;</span><br><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(manager-&gt;TradeCalcProfit()!=FALSE)</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">printf("%.2lf\n",trade.profit);</span></p></td></tr></tbody></table>

## Dealings [#](manager_api_dev#dealing)

Dealing is the manager interface operation mode, in which it receives clients trade requests from the server and sends the dealer replies to the server. After connection to the server, the manager interface can be switched to the dealing mode using the [DealerSwitch](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerswitch) function. As a parameter to the function, you should pass a pointer to the callback function, which will be called by the manager interface for notifying about new trade requests from the server, or the handle of the window and custom message ID, to which notifications about new trade requests will be sent.

After calling DealerSwitch, the Manager interface will send the following codes as a parameter to the callback function or as WPARAM parameter of a user message:

-   DEAL\_START\_DEALING - the Manager interface has successfully switched to the dealing mode;
-   DEAL\_REQUEST\_NEW - a new trade request has arrived from the server;
-   DEAL\_STOP\_DEALING - dealing mode stopped.

After receiving the DEAL\_REQUEST\_NEW notification, a custom program should call the [DealerRequestGet](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerrequestget) function in order to receive a new trade request. After that a dealer can confirm (or requote) the request - [DealerSend](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealersend), reject the request - [DealerReject](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerreject), or return the request to the queue on the server - [DealerReset](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealerreset), so that another dealer could process the request. In order to requote using DealerSend, enter new requote prices in field [RequestInfo::prices](/en/docs/mt4/api/reference_structures/structure_trade/requestinfo) and pass TRUE as a 'requote' parameter. Flag [DealerSend](/en/docs/mt4/api/manager_api/manager_api_dealer/cmanagerinterface_dealersend) determines whether quotes should be added to a stream during response, it corresponds to the 'Throw in Prices' option in the Manager terminal.

[Manager API](/en/docs/mt4/api/manager_api)

[Exported Functions and Factory](/en/docs/mt4/api/manager_api/manager_api_exported_factory)