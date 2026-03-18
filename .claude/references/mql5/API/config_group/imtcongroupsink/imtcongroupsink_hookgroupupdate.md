# IMTConGroupSink::HookGroupAdd

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_hookgroupupdate

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
        -   [Internal Data Types](/en/docs/mt5/api/reference_types)
        -   [Journal Constants](/en/docs/mt5/api/journal)
        -   [Return Codes](/en/docs/mt5/api/reference_retcodes)
        -   [Structures](/en/docs/mt5/api/reference_structures)
        -   [Configuration Interfaces](/en/docs/mt5/api/reference_configurations)
            -   [Common](/en/docs/mt5/api/config_common)
            -   [Network](/en/docs/mt5/api/config_network)
            -   [Plugins](/en/docs/mt5/api/config_plugins)
            -   [Data Feeds](/en/docs/mt5/api/config_datafeeds)
            -   [Time](/en/docs/mt5/api/config_time)
            -   [Holidays](/en/docs/mt5/api/config_holiday)
            -   [Firewall](/en/docs/mt5/api/config_firewall)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
                -   [IMTConGroup](/en/docs/mt5/api/config_group/imtcongroup)
                -   [IMTConGroupSymbol](/en/docs/mt5/api/config_group/imtcongroupsymbol)
                -   [IMTConGroupArray](/en/docs/mt5/api/config_group/imtcongrouparray)
                -   [IMTConGroupSink](/en/docs/mt5/api/config_group/imtcongroupsink)
                    -   [OnGroupAdd](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_ongroupadd)
                    -   [OnGroupUpdate](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_ongroupupdate)
                    -   [OnGroupDelete](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_ongroupdelete)
                    -   [OnGroupSync](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_ongroupsync)
                    -   [HookGroupAdd](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_hookgroupadd)
                    -   [HookGroupUpdate](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_hookgroupupdate)
                    -   [HookGroupDelete](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_hookgroupdelete)
                -   [IMTConCommission](/en/docs/mt5/api/config_group/imtconcommission)
                -   [IMTConCommTier](/en/docs/mt5/api/config_group/imtconcommtier)
            -   [Floating Margin](/en/docs/mt5/api/config_leverage)
            -   [Managers](/en/docs/mt5/api/config_manager)
            -   [History Synchronization](/en/docs/mt5/api/config_historysync)
            -   [Gateways](/en/docs/mt5/api/config_gateway)
            -   [Routing](/en/docs/mt5/api/config_route)
            -   [Reports](/en/docs/mt5/api/config_report)
            -   [Mail Servers](/en/docs/mt5/api/config_email)
            -   [Messengers](/en/docs/mt5/api/config_messenger)
            -   [Automations](/en/docs/mt5/api/config_automation)
            -   [VPS](/en/docs/mt5/api/config_vps)
            -   [KYC](/en/docs/mt5/api/config_kyc)
            -   [Subscriptions](/en/docs/mt5/api/config_subscription)
            -   [Funds and ETF](/en/docs/mt5/api/config_funds)
            -   [Additional Parameters](/en/docs/mt5/api/config_param)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)[Groups](/en/docs/mt5/api/config_group)[IMTConGroupSink](/en/docs/mt5/api/config_group/imtcongroupsink)HookGroupUpdate

# IMTConGroupSink::HookGroupAdd

Hook for the update of group settings.

C++

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTAPIRES&nbsp;&nbsp;</span><span class="f_Functions">IMTConGroupSink::HookGroupUpdate</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;UINT64</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Manager&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;IMTConGroup*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">cfg</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;current&nbsp;group</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">IMTConGroup*</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_cfg</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;A&nbsp;pointer&nbsp;to&nbsp;the&nbsp;updated&nbsp;group</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

.NET (Gateway/Manager API)

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">virtual&nbsp;MTRetCode&nbsp;&nbsp;</span><span class="f_Functions">CIMTConGroupSink.HookGroupUpdate</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">ulong</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">login</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Manager&nbsp;login</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTConGroup&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">cfg</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Current&nbsp;group</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">CIMTConGroup&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Param">new_cfg</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Updated&nbsp;group</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

login

\[in\] [The login of the manager](/en/docs/mt5/api/config_manager/imtconmanager/imtconmanager_login), who is going to update the group settings. If the group is to be updated by the plugin, 0 is specified in the parameter.

cfg

\[in\]  A pointer to the [current group object](/en/docs/mt5/api/config_group/imtcongroup).

new\_cfg

\[out\]  A pointer to the [group object](/en/docs/mt5/api/config_group/imtcongroup) after making change.

Return Value

In case there are no handlers if this event, [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful) is returned.

If the event handler returns a code different from [MT\_RET\_OK](/en/docs/mt5/api/retcodes_successful), then the group will not be updated and the hook will not be passed to other handlers (including other plugins).

Note

The hook is called right before making changes to the configuration database. The main purpose of this hook is to modify an entry that is being updated, and, if necessary, to prevent the unwanted change of records.

This method can only be used in the MetaTrader 5 Server API.

[HookGroupAdd](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_hookgroupadd)

[HookGroupDelete](/en/docs/mt5/api/config_group/imtcongroupsink/imtcongroupsink_hookgroupdelete)