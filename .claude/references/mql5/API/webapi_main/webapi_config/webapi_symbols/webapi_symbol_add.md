# Adding a Symbol

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_add

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
            -   [Getting Started](/en/docs/mt5/api/webapi_preparing)
            -   [Format of Commands](/en/docs/mt5/api/webapi_https)
            -   [Authentication](/en/docs/mt5/api/webapi_rest_authentication)
            -   [Escaping Special Characters](/en/docs/mt5/api/webapi_screening)
            -   [Maintaining Connections](/en/docs/mt5/api/webapi_pings)
            -   [Protocol Extension](/en/docs/mt5/api/webapi_protocol_extension)
            -   [Examples](/en/docs/mt5/api/webapi_examples)
            -   [Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)
                -   [Configuration Databases](/en/docs/mt5/api/webapi_main/webapi_config)
                    -   [Common](/en/docs/mt5/api/webapi_main/webapi_config/webapi_common)
                    -   [Network](/en/docs/mt5/api/webapi_main/webapi_config/webapi_network)
                    -   [Time](/en/docs/mt5/api/webapi_main/webapi_config/webapi_time)
                    -   [Groups](/en/docs/mt5/api/webapi_main/webapi_config/webapi_groups)
                    -   [Symbols](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols)
                        -   [Data Structure](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_data_structure)
                        -   [Add](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_add)
                        -   [Add Multiple](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_add_batch)
                        -   [Delete](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_delete)
                        -   [Delete Multiple](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_delete_batch)
                        -   [Shift](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_shift)
                        -   [Get Total](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_total)
                        -   [Get List](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_list)
                        -   [Get by Index](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_next)
                        -   [Get by Name or Mask](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_get)
                        -   [Get by Group](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_get_group)
                        -   [Add Subgroup](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_group_add)
                        -   [Delete Subgroup](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_group_delete)
                        -   [Shift Subgroup](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_group_shift)
                        -   [Get Subgroup Total](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_group_total)
                        -   [Get Subgroup by Index](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_group_next)
                        -   [Get Subgroup List](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_group_exist)
                    -   [Floating Margin](/en/docs/mt5/api/webapi_main/webapi_config/webapi_leverage)
                    -   [Firewall](/en/docs/mt5/api/webapi_main/webapi_config/webapi_firewall)
                    -   [Holidays](/en/docs/mt5/api/webapi_main/webapi_config/webapi_holiday)
                    -   [Managers](/en/docs/mt5/api/webapi_main/webapi_config/webapi_manager)
                    -   [Routing](/en/docs/mt5/api/webapi_main/webapi_config/webapi_route)
                    -   [History Synchronization](/en/docs/mt5/api/webapi_main/webapi_config/webapi_history_sync)
                    -   [Spreads](/en/docs/mt5/api/webapi_main/webapi_config/webapi_spread)
                    -   [Email](/en/docs/mt5/api/webapi_main/webapi_config/webapi_email)
                    -   [Messengers](/en/docs/mt5/api/webapi_main/webapi_config/webapi_messenger)
                    -   [Gateways](/en/docs/mt5/api/webapi_main/webapi_config/webapi_gateway)
                    -   [Data Feeds](/en/docs/mt5/api/webapi_main/webapi_config/webapi_feeder)
                    -   [Reports](/en/docs/mt5/api/webapi_main/webapi_config/webapi_report)
                    -   [Plugins](/en/docs/mt5/api/webapi_main/webapi_config/webapi_plugin)
                    -   [Subscriptions](/en/docs/mt5/api/webapi_main/webapi_config/webapi_subscription_cfg)
                -   [Trading](/en/docs/mt5/api/webapi_main/webapi_trading)
                -   [Users](/en/docs/mt5/api/webapi_main/webapi_users)
                -   [Clients](/en/docs/mt5/api/webapi_main/webapi_client)
                -   [Mail](/en/docs/mt5/api/webapi_main/webapi_mail)
                -   [News](/en/docs/mt5/api/webapi_main/webapi_news)
                -   [Prices](/en/docs/mt5/api/webapi_main/webapi_prices)
                -   [Daily Reports](/en/docs/mt5/api/webapi_main/webapi_daily)
                -   [Settings Files](/en/docs/mt5/api/webapi_main/webapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/webapi_main/webapi_subscription)
                -   [Common Requests](/en/docs/mt5/api/webapi_main/webapi_common_request)
                -   [Outdated version of Rest API](/en/docs/mt5/api/webapi_main/webapi_old)
                -   [PHP Implementation of Protocol](/en/docs/mt5/api/webapi_main/php)
                -   [.NET Implementation of Protocol](/en/docs/mt5/api/webapi_main/net)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)[Configuration Databases](/en/docs/mt5/api/webapi_main/webapi_config)[Symbols](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols)Add

# Adding a Symbol

Using this request you can create or change a symbol on a server.

Request format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">POST&nbsp;/api/symbol/add</span><br><span class="f_CodeExample">{&nbsp;Description&nbsp;of&nbsp;a&nbsp;symbol&nbsp;being&nbsp;created&nbsp;in&nbsp;JSON&nbsp;format&nbsp;}</span></p></td></tr></tbody></table>

Response format

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;"retcode"&nbsp;:&nbsp;"code&nbsp;description",</span><br><span class="f_CodeExample">&nbsp;"answer"&nbsp;:&nbsp;{&nbsp;Description&nbsp;of&nbsp;the&nbsp;created&nbsp;symbol&nbsp;in&nbsp;JSON&nbsp;format&nbsp;}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

Example

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">//---&nbsp;request&nbsp;to&nbsp;the&nbsp;server</span><br><span class="f_CodeExample">POST&nbsp;/api/symbol/add</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;&nbsp;"Symbol"&nbsp;:&nbsp;"EURUSD",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"Path"&nbsp;:&nbsp;"Forex\\Major\\EURUSD",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"ISIN"&nbsp;:&nbsp;"",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"Description"&nbsp;:&nbsp;"Euro&nbsp;vs&nbsp;US&nbsp;Dollar",</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">}</span><br><span class="f_CodeExample">//---&nbsp;server&nbsp;response</span><br><span class="f_CodeExample">{</span><br><span class="f_CodeExample">&nbsp;&nbsp;"retcode"&nbsp;:&nbsp;"0&nbsp;Done",</span><br><span class="f_CodeExample">&nbsp;&nbsp;"answer"&nbsp;:&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"Symbol"&nbsp;:&nbsp;"EURUSD",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"Path"&nbsp;:&nbsp;"Forex\\Major\\EURUSD",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"ISIN"&nbsp;:&nbsp;"",</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;"Description"&nbsp;:&nbsp;"Euro&nbsp;vs&nbsp;US&nbsp;Dollar",</span><br><span class="f_CodeExample">...</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span><br><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

## Request Parameters

This command has no parameters. Description of the symbol is passed in the JSON format as an additional command body. When adding a symbols, all its [parameters](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_data_structure#symbol) must be described.

The JSON description of the symbol passed when creating is the same as the description returned by the server.

## Response Parameters

-   retcode — if successful, the command returns [a response code](/en/docs/mt5/api/retcodes_successful) 0. Otherwise, it will return an error code.
-   answer — parameters of the created symbol in JSON format. A complete description of the passed parameters of symbols is given in the ["Data structure"](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_data_structure#symbol) section.

## Notes

-   This command works only when connected to the main trade server. Otherwise error [12001](/en/docs/mt5/api/retcodes_api) is returned.
-   When the command is run the presence of the symbol you are adding is checked. A key field for comparison is the name of the symbol. If such a symbol already exists, its settings are updated.
-   When you update the configuration, only those parameters that are explicitly specified in the JSON description are changed. Other parameters stay unchanged.
-   Before adding, the correctness of the record is checked. If the entry is incorrect, it returns the error code [3](/en/docs/mt5/api/retcodes_common).
-   To run the command, [the manager account](/en/docs/mt5/api/webapi_rest_authentication#client_start) must have rights to connect as an administrator ([IMTConManager::RIGHT\_ADMIN](/en/docs/mt5/api/config_manager/imtconmanager/imtconmanager_enum#enmanagerrights)) and edit symbol configurations ([IMTConManager::RIGHT\_CFG\_SYMBOLS](/en/docs/mt5/api/config_manager/imtconmanager/imtconmanager_enum#enmanagerrights)). Otherwise, it returns the error code [8](/en/docs/mt5/api/retcodes_common).

[Data Structure](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_data_structure)

[Add Multiple](/en/docs/mt5/api/webapi_main/webapi_config/webapi_symbols/webapi_symbol_add_batch)