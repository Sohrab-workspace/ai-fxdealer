# Segregated Report

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_examples/segregated_report

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)[Ready-made Examples](/en/docs/mt5/api/reportapi_examples)Segregated

# Segregated Report

Segregated Report is a report on the change of financial state of the requested accounts for the specified period. The report is generated on the basis of daily reports. Thus each rate is calculated as the difference between its value in the daily report for the last date and the value in the daily report for the first date specified when requesting the report. Summarized data of the accounts (for example, balance, equity and floating p/l) is taken from the daily reports generated for the last date within the time range the report is requested for. If there is no report generated for that date, zero values will be displayed.

## Setup

The following parameters must be set in the manager terminal before requesting the report:

-   Groups — the groups containing the accounts, on which the report must be created. You can specify one or several accounts separating them by commas;
-   Period — starting and ending date of the period, for which the report will be generated.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Daily reports generation must be enabled on the server for the appropriate account groups to generate this type of reports.</span></p></td></tr></tbody></table>

The report contains the following data:

-   Login — account number.
-   Name — account holder name.

-   Group — group the account belongs to.

-   Country — client's country of residence.
-   Account comment — comment to the trading account.

-   Deposit — total funds deposited/withdrawn from the account per day.
-   Credit — final amount of credit funds submitted for the selected period (the difference between provided and withdrawn funds).
-   Commission — commission in the account for the specified period. Both blocked commission (in case they are accumulated within a day/a month and then withdrawn in a single balance deal), and commission charged immediately during a transaction are considered here.
-   Swap — total amount of swaps accumulated during the selected period. The amount is calculated based on swap values in deals.
-   Profit — net profit (profit - loss) obtained for the selected period.
-   Interest — annual interest accrued for the selected period.
-   Balance — balance at the moment of generation of the daily report for the last date within the time range the report is requested for.
-   Floating P/L — floating profit/loss in the account at the moment of generation of the daily report for the last date within the time range the report is requested for.
-   Equity — amount of funds in the account at the moment of generation of the daily report for the last date within the time range the report is requested for.
-   Currency — account deposit currency.

[Positions History](/en/docs/mt5/api/reportapi_examples/positions_history_report)

[Summary](/en/docs/mt5/api/reportapi_examples/summary_report)