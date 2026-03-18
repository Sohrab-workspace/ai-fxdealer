# IMTAdminAPI::GroupUpdate

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupupdate

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
            -   [Purpose of Manager API](/en/docs/mt5/api/managerapi_purpose)
            -   [Recommendations for Developers](/en/docs/mt5/api/managerapi_best_practice)
            -   [Getting Started](/en/docs/mt5/api/managerapi_preparing)
            -   [Ready-made Examples](/en/docs/mt5/api/managerapi_examples)
            -   [.NET Implementation](/en/docs/mt5/api/managerapi_net)
            -   [Python Implementation](/en/docs/mt5/api/managerapi_python)
            -   [Exported Functions](/en/docs/mt5/api/managerapi_exported)
            -   [CMTManagerAPIFactory](/en/docs/mt5/api/cmtmanagerapifactory)
            -   [Administrator Interface](/en/docs/mt5/api/imtadminapi)
                -   [Common Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_common)
                -   [Connection to the Server](/en/docs/mt5/api/imtadminapi/imtadminapi_connection)
                -   [Operations with Connection](/en/docs/mt5/api/imtadminapi/imtadminapi_network)
                -   [Server Management](/en/docs/mt5/api/imtadminapi/imtadminapi_server_manage)
                -   [Configuration Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_config)
                    -   [Common](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_common)
                    -   [Network](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_network)
                    -   [Plugins](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_plugin)
                    -   [Data Feeds](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_datafeed)
                    -   [Time](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_time)
                    -   [Holidays](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_holiday)
                    -   [Firewall](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_firewall)
                    -   [Symbols](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_symbol)
                    -   [Spreads](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_spread)
                    -   [Groups](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group)
                        -   [GroupCreate](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupcreate)
                        -   [GroupSymbolCreate](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupsymbolcreate)
                        -   [GroupCommissionCreate](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupcommissioncreate)
                        -   [GroupTierCreate](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_grouptiercreate)
                        -   [GroupSubscribe](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupsubscribe)
                        -   [GroupUnsubscribe](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupunsubscribe)
                        -   [GroupUpdate](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupupdate)
                        -   [GroupUpdateBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupupdatebatch)
                        -   [GroupDelete](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupdelete)
                        -   [GroupDeleteBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupdeletebatch)
                        -   [GroupShift](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupshift)
                        -   [GroupTotal](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_grouptotal)
                        -   [GroupNext](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupnext)
                        -   [GroupGet](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupget)
                    -   [Floating Margin](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_leverage)
                    -   [Managers](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_manager)
                    -   [History Synchronization](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_historysync)
                    -   [Gateways](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_gateway)
                    -   [Routing](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_route)
                    -   [Reports](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_report)
                    -   [Mail Servers](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_email)
                    -   [Messengers](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_messenger)
                    -   [Automation](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_automation)
                    -   [VPS](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_vps)
                    -   [KYC](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_kyc)
                    -   [Subscriptions](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_subscription)
                -   [Clients](/en/docs/mt5/api/imtadminapi/imtadminapi_clients)
                -   [Users](/en/docs/mt5/api/imtadminapi/imtadminapi_user)
                -   [Trade Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_trading)
                -   [Mail Database](/en/docs/mt5/api/imtadminapi/imtadminapi_mail)
                -   [News Database](/en/docs/mt5/api/imtadminapi/imtadminapi_news)
                -   [History Data](/en/docs/mt5/api/imtadminapi/imtadminapi_charts)
                -   [Tick Data](/en/docs/mt5/api/imtadminapi/imtadminapi_tick)
                -   [Settings Files](/en/docs/mt5/api/imtadminapi/imtadminapi_setting)
                -   [Subscriptions](/en/docs/mt5/api/imtadminapi/imtadminapi_subscription)
                -   [Custom Functions](/en/docs/mt5/api/imtadminapi/imtadminapi_custom)
                -   [ECN](/en/docs/mt5/api/imtadminapi/imtadminapi_ecn)
                -   [Geo Services](/en/docs/mt5/api/imtadminapi/imtadminapi_geo)
            -   [Manager Interface](/en/docs/mt5/api/imtmanagerapi)
            -   [Dealer Interface](/en/docs/mt5/api/imtdealersink)
            -   [Interface of Manager API Events](/en/docs/mt5/api/imtmanagersink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Manager API](/en/docs/mt5/api/managerapi)[Administrator Interface](/en/docs/mt5/api/imtadminapi)[Configuration Databases](/en/docs/mt5/api/imtadminapi/imtadminapi_config)[Groups](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group)GroupUpdate

# IMTAdminAPI::GroupUpdate

Adds or updates a group configuration.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTAdminAPI::GroupUpdate</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTConGroup*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Group&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTAdminAPI.GroupUpdate</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTConGroup</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Group&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Python

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Functions">AdminAPI.GroupUpdate</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">#&nbsp;Group&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

group

\[in\]  An object of group configuration.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, a corresponding error code will be returned.

Note

A configuration can be added or updated only from the applications that run on the main server. For all other applications the response code [MT\_RET\_ERR\_NOTMAIN](/en/docs/mt5/api/retcodes_api) will be returned.

Before adding, the correctness of the record is checked. If the record is incorrect, the error code [MT\_RET\_ERR\_PARAMS](/en/docs/mt5/api/retcodes_common) is returned.

After adding a group, wait approximately 1000 ms before adding new accounts to it. This time is required for the platform to apply the configuration.

[GroupUnsubscribe](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupunsubscribe)

[GroupUpdateBatch](/en/docs/mt5/api/imtadminapi/imtadminapi_config/imtadminapi_config_group/imtadminapi_groupupdatebatch)