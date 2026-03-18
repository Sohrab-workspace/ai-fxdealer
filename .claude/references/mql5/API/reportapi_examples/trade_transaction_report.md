# Trade Transactions Report

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_examples/trade_transaction_report

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
            -   [Purpose of the Report API](/en/docs/mt5/api/reportapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/reportapi_interaction)
            -   [Configuration of Reports](/en/docs/mt5/api/reportapi_configuration)
            -   [Request for Reports](/en/docs/mt5/api/reportapi_request)
            -   [Requirements for Modules](/en/docs/mt5/api/reportapi_requirements)
            -   [Creating a Simple Report](/en/docs/mt5/api/reportapi_simple_report)
            -   [Tabular Reports](/en/docs/mt5/api/reportapi_tables)
            -   [HTML Reports](/en/docs/mt5/api/reportapi_html)
            -   [Dashboards](/en/docs/mt5/api/reportapi_dashboards)
            -   [Templates](/en/docs/mt5/api/reportapi_html_template)
            -   [Charts](/en/docs/mt5/api/reportapi_html_charts)
            -   [Memory Management](/en/docs/mt5/api/reportapi_memory_management)
            -   [Multithreading](/en/docs/mt5/api/reportapi_multithreading)
            -   [Ready-made Examples](/en/docs/mt5/api/reportapi_examples)
                -   [Accounts Groups](/en/docs/mt5/api/reportapi_examples/accounts_groups_report)
                -   [Accounts Growth](/en/docs/mt5/api/reportapi_examples/accounts_growth_report)
                -   [Accounts Lifetime by Countries](/en/docs/mt5/api/reportapi_examples/accounts_lifetime_report)
                -   [Agents](/en/docs/mt5/api/reportapi_examples/agents_report)
                -   [Agents Detailed](/en/docs/mt5/api/reportapi_examples/agents_detailed_report)
                -   [Credit Facility](/en/docs/mt5/api/reportapi_examples/credit_facility_report)
                -   [Daily](/en/docs/mt5/api/reportapi_examples/daily_report)
                -   [Daily Detailed](/en/docs/mt5/api/reportapi_examples/daily_detailed_report)
                -   [Daily Server Logs](/en/docs/mt5/api/reportapi_examples/daily_server_report)
                -   [Daily Dealing](/en/docs/mt5/api/reportapi_examples/daily_dealing_report)
                -   [Daily Trades](/en/docs/mt5/api/reportapi_examples/daily_trade_report)
                -   [Daily Orders](/en/docs/mt5/api/reportapi_examples/daily_orders_report)
                -   [Daily Positions](/en/docs/mt5/api/reportapi_examples/daily_positions_report)
                -   [Daily Expert Advisors](/en/docs/mt5/api/reportapi_examples/daily_expert_report)
                -   [Deals History](/en/docs/mt5/api/reportapi_examples/deals_history_report)
                -   [Deals Profit](/en/docs/mt5/api/reportapi_examples/deals_profit_report)
                -   [Deals Initiators](/en/docs/mt5/api/reportapi_examples/deals_initiators_report)
                -   [Deals Geography](/en/docs/mt5/api/reportapi_examples/deals_geography_report)
                -   [Deals Weekly](/en/docs/mt5/api/reportapi_examples/deals_weekly_report)
                -   [Deposit and Withdrawal](/en/docs/mt5/api/reportapi_examples/deposit_withdrawal_report)
                -   [Equity](/en/docs/mt5/api/reportapi_examples/equity_report)
                -   [Margin Calls](/en/docs/mt5/api/reportapi_examples/margin_call_report)
                -   [Orders History](/en/docs/mt5/api/reportapi_examples/orders_history_report)
                -   [Positions History](/en/docs/mt5/api/reportapi_examples/positions_history_report)
                -   [Segregated](/en/docs/mt5/api/reportapi_examples/segregated_report)
                -   [Summary](/en/docs/mt5/api/reportapi_examples/summary_report)
                -   [Gateways Turnover](/en/docs/mt5/api/reportapi_examples/gateways_turnover_report)
                -   [Gateways Profit](/en/docs/mt5/api/reportapi_examples/gateways_profit_report)
                -   [Gateways White Label](/en/docs/mt5/api/reportapi_examples/gateways_wl_report)
                -   [Execution Types](/en/docs/mt5/api/reportapi_examples/execution_type_report)
                -   [Trade Accounts](/en/docs/mt5/api/reportapi_examples/trade_accounts_report)
                -   [Trade Transactions](/en/docs/mt5/api/reportapi_examples/trade_transaction_report)
                -   [Trade Modifications](/en/docs/mt5/api/reportapi_examples/trade_modification_report)
                -   [Trade Performance Summary](/en/docs/mt5/api/reportapi_examples/performance_summary_report)
                -   [Trade Group Statistics](/en/docs/mt5/api/reportapi_examples/group_statistics_report)
                -   [StopOut Compensations](/en/docs/mt5/api/reportapi_examples/stopouts_compensation_report)
                -   [Money Flow Daily](/en/docs/mt5/api/reportapi_examples/money_flow_daily_report)
                -   [Money Flow Weekly](/en/docs/mt5/api/reportapi_examples/money_flow_weekly_report)
                -   [Lifetime Value](/en/docs/mt5/api/reportapi_examples/lifetime_value_report)
                -   [First Time Deposit](/en/docs/mt5/api/reportapi_examples/first_time_deposit_report)
                -   [Retention of Trading Accounts](/en/docs/mt5/api/reportapi_examples/retention_of_trading_accounts_report)
                -   [Retention of Clients](/en/docs/mt5/api/reportapi_examples/retention_of_clients_report)
                -   [NFA](/en/docs/mt5/api/reportapi_examples/nfa_report)
                -   [EMIR](/en/docs/mt5/api/reportapi_examples/emir_report)
                -   [Fund Overview](/en/docs/mt5/api/reportapi_examples/fund_overview_report)
                -   [Risk Appetite](/en/docs/mt5/api/reportapi_examples/risk_appetite_report)
                -   [Fast Profit Deals](/en/docs/mt5/api/reportapi_examples/fast_profit_deals_report)
            -   [Entry Points](/en/docs/mt5/api/reportapi_entrypoints)
            -   [Report Plugin Interface](/en/docs/mt5/api/imtreportcontext)
            -   [Main Interface of Reports](/en/docs/mt5/api/imtreportapi)
            -   [Dashboard Interfaces](/en/docs/mt5/api/reportapi_dashboard)
            -   [Diagram Interfaces](/en/docs/mt5/api/reportapi_auxiliary)
            -   [Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)
            -   [Data Cache Interfaces](/en/docs/mt5/api/reportapi_cache)
        -   [Web API](/en/docs/mt5/api/webapi)
        -   [SQL Export](/en/docs/mt5/api/sql_export)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Ready-made Examples](/en/docs/mt5/api/reportapi_examples)Trade Transactions

# Trade Transactions Report

Trade Transaction Report provides detailed data on trading operations at MetaTrader 5 servers. This report is useful not only for a broker but also when providing data to regulatory bodies.

The report is implemented as TradesTransactionReports.dll file (TradesTransactionReports64.dll for 64-bit platform version) combining the report and the server plugin. The plugin collects data on report transactions and saves them in Reports\\Trades.Transaction.Reports directory in trading server's folder, while the report provides collected data in the appropriate format. The plugin should be enabled in the settings of the appropriate trading server. If the plugin is not enabled, report data will not be updated and the report will provide data only for the plugin's operation period.

TradesTransactionReports.dll file is included into the standard delivery and located in Reports directory of MetaTrader 5 trading server.

## Plugin Installation

The appropriate plugin should be installed to collect the data used in the report. To install the plugin, enter Plugins section in MetaTrader 5 Administrator. After the server to install the plugin has been selected, click "![Add](/en/docs/mt5/api/img/add_button.png "Add")Add" command.

![Configuring the Plugin](/en/docs/mt5/api/img/tradetrans_plugin_config.png "Configuring the Plugin")

The following settings are available:

-   Groups — group filter. Groups are separated with a comma. To specify groups, you may also use the mask "\*" and the negation sign "!". For example, the value "demoforex,democfd" means that the plugin will collect the transaction details for users in demoforex and democfd groups. The value "\*" is for all groups. The default value is "\*,!demo\*,!contest\*" which means all groups except those whose names start with demo and contest.
-   Base Directory — name of the directory where the database of transactions is saved for the report. The data is saved for each day. This directory is automatically created in Reports\\Trade.Transaction.Report. In most cases, this parameter should save a default value.
-   Symbol — symbol filter. Symbols are separated with a comma. To specify groups, you may also use the mask "\*" and the negation sign "!". For example, the value "EURUSD,GBPUSD" means that the plugin will collect the transaction details for EURUSD and GBPUSD symbols. The value "\*" is for all symbols. \*,!CFD\\\* value is for all symbols except those in the CFD group.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is not recommended to use the same Base Directory parameters for different plugins. In such case, correct operation of those plugins is not guaranteed.</span></p></td></tr></tbody></table>

## Report Installation

To install the plugin, enter Reports section in MetaTrader 5 Administrator. After the server to install the report has been selected, click "![Add](/en/docs/mt5/api/img/add_button.png "Add")Add" command.

![Setup of the Report](/en/docs/mt5/api/img/tradetrans_report_config.png "Setup of the Report")

The following specific settings are available for the report:

-   Base Directory — the directory where transaction databases are searched for. This parameter should be similar to the same-name parameter of the corresponding plugin. If the plugin with a similar Base Directory parameter does not exist, the report will be empty. Several reports may refer to the similar transaction databases.
-   Show group owner — the flag of Group Owner column display in the report. On default, the column is displayed (Yes). When set to No, Group Owner is not displayed in the report.
-   Show daily transactions — whether to show the state of orders and positions as of the end of the trading day (the "daily order" and "daily deal" fields) in the report.
-   Show reason — whether to show reasons for the execution of trading operations (the "reason" field) in the report.
-   Show retcode — whether to show codes of operation execution results (the "retcode" field) in the report.
-   Show rejected — showing rejected operation in the report.
-   Daily Report Path, Daily Report Time — once a day, the report plugin unloads data on all transactions for the past day to a CSV file.

-   In the "Daily Report Path" parameter, set the name of the folder in the trade server installation directory, in which files with transactions will be saved. The "confirms" folder is used by default. In this case, files are saved at the following path: \[trade server directory\]\\confirms\\\\YYYY.MM.DD.trans\\\\"Base Directory".csv, where "Base Directory" is the value of plugin's "Base Directory" parameter.
-   Specify the time, when the file with transactions should be generated, in the "Daily Report Time" parameter. The time is not set by default, so the file is generated at the [end of the trading day](/en/docs/mt5/api/config_network/imtconservertrade/imtconservertrade_overnighttime) (after completion of all day closing procedures).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The standard parameters are described in the <a href="/en/docs/mt5/api/reportapi_configuration" class="topiclink">"Report Configuration"</a> section.</span></p></td></tr></tbody></table>

## Using the Report

MetaTrader 5 Manager is used for requesting the report. The requested data can be filtered by group, logins, period and symbol mask. The report is generated in real time and the data can be updated by new transactions at each new request.

Find out more about working with the reports in the appropriate section of MetaTrader 5 Manager documentation.

![Requesting the report via MetaTrader 5 Manager](/en/docs/mt5/api/img/tradetrans_manager_request.png "Requesting the report via MetaTrader 5 Manager")

The request is resulted in the table which can be saved in HTML, CSV or Open XML (MS Office Excel 2007) formats:

![Request result](/en/docs/mt5/api/img/tradetrans_report_result.png "Request result")

The report includes the following information:

-   Login — user account's number;

-   Group — group the account belongs to;

-   Country — client's country of residence;
-   Account comment — comment to the trading account;

-   Leverage — user account's leverage;
-   Dealer — login of the dealer that placed the order. Indicated only if the request is placed by a dealer;
-   IP — user's IP address;
-   Currency — account deposit's currency;
-   Order — order number (ticket);
-   Order ID — order identifier in a external trading system. The identifier is changed in case the order is updated in the external trading system by canceling or placing a new order;
-   Deal — deal number (ticket);
-   Deal ID — deal identifier in an external trading system;
-   Position — the ticket of a deal;
-   Position ID — the ID of a position in an external trading system;
-   Action — action type (see below);
-   Type — trading operation type (see below);
-   Entry — direction of the operation: in (market entry), out (market exit), in/out (position reversal);
-   Symbol — trading symbol;
-   Position By — the ticket of the opposite position. It is shown if the source position (Position) was closed by an opposite one;
-   Lots — volume in lots;
-   Amount — volume;
-   Time — transaction time;
-   Price — transaction price;
-   Bid — bid market price at the moment of transaction;
-   Ask — ask market price at the moment of transaction;
-   Position Price — position price for position closing transactions;
-   SL — Stop Loss price;
-   TL — Take Profit price;
-   Margin Rate — margin rate at the moment of transaction;
-   Margin Amount — margin volume at the moment of transaction without considering the leverage;
-   Commission — deal commission;
-   Swap — swap size;
-   Profit — profit/loss size;
-   Profit Currency — profit currency;
-   Profit Rate — conversion rate of the profit currency to deposit currency;
-   Raw Profit — the size of profit/loss obtained as a result of the operation. Indicated in the profit currency of the operation symbol;
-   Amount Closed — closed volume in amounts;
-   Gateway Price — price in external trade system;
-   Reason — [reason](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal/imtdeal_enum#endealreason) of the operation execution;
-   Retcode — [result ot execution](/en/docs/mt5/api/retcodes_trade_request);
-   Group Owner — name of the company the client is serviced by. It corresponds to Company field in client group configuration.

Action field reflects the transaction type. It may contain the following values:

-   market — market operation (entering, exiting, reversal);
-   position modify — position's Stop Loss and Take Profit modification;
-   pending — placing a pending order;
-   pending modify — modifying a pending order;
-   pending cancel — canceling a pending order;
-   pending expiration — pending order expiration;
-   pending activation — pending order activation;
-   stop loss — closing position by Stop Loss;
-   take profit — closing position by Take Profit;
-   deposit — balance operation;
-   order stopout — canceling order by Stop Out;
-   position stopout — closing position by Stop Out;
-   stoplimit — Stop Limit order activation;
-   daily order — the state of the order as of the end of the trading day;
-   daily position — the state of the position as of the end of the trading day;
-   close by — closing of a position by an opposite one;
-   rollover — transferring of a position on the next trading day;
-   market by dealer — a market operation performed by a dealer;
-   position modify by dealer — modification of the Stop Loss or Take Profit levels of a position performed by a dealer;
-   pending modify by dealer — modification of a pending order by a dealer;
-   pending cancel by dealer — canceling of a pending order by a dealer;
-   pending activation by dealer — activation of a pending order by a dealer;
-   dealer close by — the operation of closing of a position by an opposite one performed by a dealer;
-   variation margin — variation margin calculation.

Type field displays order or transaction type:

-   buy — order for buying at the current market price;
-   sell — order for selling at the current market price;
-   buy limit — buy limit order;
-   sell limit — sell limit order;
-   buy stop — buy stop order;
-   sell stop — sell stop order;
-   buy stop limit — buy stop limit order;
-   sell stop limit — sell stop limit order;
-   deposit — deposit or withdrawal operation;
-   credit — credit operation;
-   charge — charging commissions;
-   correction — correction operations;
-   bonus — adding bonuses;
-   commission — commission;
-   commission daily — commission per day;
-   commission monthly — commission per month;
-   agent daily — charging a daily agent commission;
-   agent monthly — charging a monthly agent commission;
-   interest rate — accrual of annual interest;
-   buy canceled — a canceled buy deal;
-   sell canceled — a canceled sell deal;
-   dividend —  payment of taxable dividend;
-   dividend franked — payment of nontaxable dividend;
-   tax — charging a tax;
-   agent — accrual of instant agent commission.

[Trade Accounts](/en/docs/mt5/api/reportapi_examples/trade_accounts_report)

[Trade Modifications](/en/docs/mt5/api/reportapi_examples/trade_modification_report)