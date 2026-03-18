# IMTServerAPI::GroupAdd

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupadd

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
                        -   [GroupCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupcreate)
                        -   [GroupSymbolCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupsymbolcreate)
                        -   [GroupCommissionCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupcommissioncreate)
                        -   [GroupTierCreate](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_grouptiercreate)
                        -   [GroupSubscribe](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupsubscribe)
                        -   [GroupUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupunsubscribe)
                        -   [GroupAdd](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupadd)
                        -   [GroupDelete](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupdelete)
                        -   [GroupShift](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupshift)
                        -   [GroupTotal](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_grouptotal)
                        -   [GroupNext](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupnext)
                        -   [GroupGet](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupget)
                    -   [Managers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_manager)
                    -   [History Synchronization](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_historysync)
                    -   [Gateways](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_gateway)
                    -   [Routing](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_route)
                    -   [Reports](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_report)
                    -   [Mail Servers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_email)
                    -   [Messengers](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_messenger)
                    -   [Automation](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_automation)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)[Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)[Groups](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group)GroupAdd

# IMTServerAPI::GroupAdd

Adds or updates a group configuration.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTServerAPI::GroupAdd</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTConGroup*</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">group</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Group&nbsp;configuration&nbsp;object</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

group

\[in\]  An object of group configuration.

Return Value

An indication of successful completion is the [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) response code. Otherwise, a corresponding error code will be returned.

Note

When calling the method, a check is made whether the entry already exists. If the entry already exists, it is updated, otherwise a new entry is added. A key field for comparison is the name of the group [IMTConGroup::Group()](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_group). When you try to add a completely identical record, no changes are made, and therefore the [IMTConGroupSink::OnGroupUpdate](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_ongroupupdate) notification method is not called.

A configuration can be added or updated only from the plugins that run on the main server. For all other plugins the response code [MT\_RET\_ERR\_NOTMAIN](/en/docs/mt5/api/retcodes_api) will be returned.

Before adding, the correctness of the record is checked. If the record is incorrect, the error code [MT\_RET\_ERR\_PARAMS](/en/docs/mt5/api/retcodes_common) is returned.

After adding a group, wait approximately 1000 ms before adding new accounts to it. This time is required for the platform to apply the configuration.

[GroupUnsubscribe](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupunsubscribe)

[GroupDelete](/en/docs/mt5/api/imtserverapi/serverapi_configuration/serverapi_config_group/imtserverapi_groupdelete)