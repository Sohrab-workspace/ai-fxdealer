# IMTServerAPI::AutomationTrigger

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationtrigger

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
            -   [Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)
            -   [Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)
            -   [Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)
            -   [Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)
            -   [Hooks](/en/docs/mt5/api/serverapi_hooks)
            -   [Request Processing on the Server](/en/docs/mt5/api/hook_scheme)
            -   [Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)
            -   [Debugging](/en/docs/mt5/api/serverapi_debug)
            -   [Ready-made Examples](/en/docs/mt5/api/serverapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reference_entrypoints)
            -   [Plugin Interface](/en/docs/mt5/api/imtserverplugin)
            -   [Main API Interface](/en/docs/mt5/api/imtserverapi)
                -   [Common Functions](/en/docs/mt5/api/imtserverapi/serverapi_common)
                -   [Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)
                    -   [Common](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_common)
                    -   [Network](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_network)
                    -   [Plugins](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_plugins)
                    -   [Data Feeds](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_datafeeds)
                    -   [Time](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_time)
                    -   [Holidays](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_holiday)
                    -   [Firewall](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_firewall)
                    -   [Symbols](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_symbol)
                    -   [Spreads](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_spread)
                    -   [Groups](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group)
                    -   [Managers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_manager)
                    -   [History Synchronization](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_historysync)
                    -   [Gateways](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_gateway)
                    -   [Routing](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_route)
                    -   [Reports](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_report)
                    -   [Mail Servers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_email)
                    -   [Messengers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_messenger)
                    -   [Automation](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation)
                        -   [AutomationCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationcreate)
                        -   [AutomationConditionCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationconditioncreate)
                        -   [AutomationActionCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationactioncreate)
                        -   [AutomationParamCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationparamcreate)
                        -   [AutomationSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationsubscribe)
                        -   [AutomationUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationunsubscribe)
                        -   [AutomationAdd](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationadd)
                        -   [AutomationDelete](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationdelete)
                        -   [AutomationShift](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationshift)
                        -   [AutomationTotal](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationtotal)
                        -   [AutomationNext](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationnext)
                        -   [AutomationGet](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationget)
                        -   [AutomationTrigger](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationtrigger)
                    -   [VPS](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_vps)
                    -   [KYC](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_kyc)
                    -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_subscription)
                    -   [Floating Margin](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_leverage)
                -   [Clients](/en/docs/mt5/api/imtserverapi/serverapi_clients)
                -   [Users](/en/docs/mt5/api/imtserverapi/serverapi_users)
                -   [Online Connections](/en/docs/mt5/api/imtserverapi/serverapi_online)
                -   [Certificates](/en/docs/mt5/api/imtserverapi/serverapi_certificate)
                -   [Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)
                -   [History Data](/en/docs/mt5/api/imtserverapi/serverapi_chart)
                -   [Tick Data](/en/docs/mt5/api/imtserverapi/serverapi_ticks)
                -   [Depth of Market](/en/docs/mt5/api/imtserverapi/serverapi_book)
                -   [Mail Database](/en/docs/mt5/api/imtserverapi/serverapi_mail)
                -   [News Database](/en/docs/mt5/api/imtserverapi/serverapi_news)
                -   [Daily Reports](/en/docs/mt5/api/imtserverapi/serverapi_trading_daily)
                -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_subscription)
                -   [Server Services](/en/docs/mt5/api/imtserverapi/serverapi_server_services)
                -   [Geo Services](/en/docs/mt5/api/imtserverapi/serverapi_geo)
                -   [Dataset](/en/docs/mt5/api/imtserverapi/serverapi_dataset)
                -   [Custom Functions](/en/docs/mt5/api/imtserverapi/serverapi_custom)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
            -   [Interface of End-of-Day Events](/en/docs/mt5/api/imtendofdaysink)
        -   [Manager API](/en/docs/mt5/api/managerapi)
        -   [Gateway API](/en/docs/mt5/api/gatewayapi)
        -   [Report API](/en/docs/mt5/api/reportapi)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)[Automation](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation)AutomationTrigger

# IMTServerAPI::AutomationTrigger

Send an event to trigger an automation rule with the specified name.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::AutomationTrigger</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">name</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Configuration&nbsp;name</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTUser*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">user</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;User&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTAccount*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">account</span><span class="f_CodeExample">,&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;An&nbsp;object&nbsp;of&nbsp;the&nbsp;account&nbsp;trading&nbsp;state</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTDeal*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">deal</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Deal&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTOrder*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">order</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Order&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTPosition*</span><span class="f_CodeExample">&nbsp;</span><span class="f_Param">position</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Position&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

name

\[in\]  The name of the automation configuration for which the event is sent. The [IMTConAutomation::Name](/en/docs/mt5/api/config_automation/imtconautomation/imtconautomation_name) fields is used for the name.

user

\[in\]  The [IMTUser](/en/docs/mt5/api/reference_user/imtuser) user object. Optional parameter.

account

\[in\]  The [IMTAccount](/en/docs/mt5/api/reference_trading/user_account/imtaccount) object of the account trading state. Optional parameter.

deal

\[in\]  The [IMTDeal](/en/docs/mt5/api/reference_trading/trading_deal/imtdeal) deal object. Optional parameter.

order

\[in\]  The [IMTOrder](/en/docs/mt5/api/reference_trading/trading_order/imtorder) order object. Optional parameter.

position

\[in\]  The [IMTPosition](/en/docs/mt5/api/reference_trading/trading_position/imtposition) position object. Optional parameter.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, an error code will be returned.

Note

Use this function to run automation tasks based on your own events. During the function call, a special event is generated for the task specified in the 'name' parameter. The event causes the task to trigger.

When the event is received on the server side, the trigger type set for the automation task is checked. If it is different from [IMTConAutomationTrigger::TRIGGER\_EXTERNAL\_API](/en/docs/mt5/api/config_automation/imtconautomation/imtconautomation_enum#entriggers), the task will not trigger.

Parameters 'user', 'account', 'deal', 'order' and 'position' should be filled depending on your tasks and on what the event being generated is associated with. If it concerns changes in the user database, pass 'user'; if it implies execution of a deal on the account, pass 'deal', and so on.

Information from these parameters is passed as an execution context for the automation task. You can use it for checks in [additional parameters](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_condition) and in [macros](https://support.metaquotes.net/en/docs/mt5/platform/administration/automation/automation_macros). For example, login from 'user' can be checked in [IMTConAutoCondition::CONDITION\_ACCOUNT\_LOGIN](/en/docs/mt5/api/config_automation/imtconautocondition/imtconautocondition_enum#enconditions), and ticket from 'deal' can be used in [IMTConAutoCondition::CONDITION\_DEAL\_TICKET](/en/docs/mt5/api/config_automation/imtconautocondition/imtconautocondition_enum#enconditions).

[AutomationGet](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation/imtserverapi_automationget)

[VPS](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_vps)