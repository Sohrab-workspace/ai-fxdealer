# IMTConAccountAgreement

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_common/imtconaccountagreement

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
                -   [IMTConCommon](/en/docs/mt5/api/config_common/imtconcommon)
                -   [IMTConAccountAllocation](/en/docs/mt5/api/config_common/imtconaccountallocation)
                -   [IMTConAccountAgreement](/en/docs/mt5/api/config_common/imtconaccountagreement)
                    -   [Enumerations](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_enum)
                    -   [Release](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_release)
                    -   [Assign](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_assign)
                    -   [Clear](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_clear)
                    -   [CaptionType](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_captiontype)
                    -   [CaptionCustomText](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_captioncustomtext)
                    -   [URL](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_url)
                    -   [Flags](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_flags)
                -   [IMTConCommonSink](/en/docs/mt5/api/config_common/imtconcommonsink)
            -   [Network](/en/docs/mt5/api/config_network)
            -   [Plugins](/en/docs/mt5/api/config_plugins)
            -   [Data Feeds](/en/docs/mt5/api/config_datafeeds)
            -   [Time](/en/docs/mt5/api/config_time)
            -   [Holidays](/en/docs/mt5/api/config_holiday)
            -   [Firewall](/en/docs/mt5/api/config_firewall)
            -   [Symbols](/en/docs/mt5/api/config_symbol)
            -   [Spreads](/en/docs/mt5/api/config_spread)
            -   [Groups](/en/docs/mt5/api/config_group)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)[Common](/en/docs/mt5/api/config_common)IMTConAccountAgreement

# IMTConAccountAgreement

The IMTConAccountAgreement class contains methods for working with the [agreements](https://support.metaquotes.net/ru/docs/mt5/platform/administration/admin_accounts/account_allocation_groups#agreement) which are shown to clients when opening accounts through terminals.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_release" class="topiclink">Release</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the current object.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_assign" class="topiclink">Assign</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign the passed object to the current one.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_clear" class="topiclink">Clear</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear an object.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_captiontype" class="topiclink">CaptionType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the agreement type.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_captioncustomtext" class="topiclink">CaptionCustomText</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the name of the user agreement.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_url" class="topiclink">URL</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the agreement link.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_flags" class="topiclink">Flags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get additional agreement settings.</span></p></td></tr></tbody></table>

The IMTConAccountAgreement class contains the following enumerations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Enumeration</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_enum#encaptiontype" class="topiclink">EnCaptionType</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Agreement types.</span></p></td></tr><tr class="table"><td class="table" style="width:150px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_enum#enflags" class="topiclink">EnFlags</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Additional agreement settings.</span></p></td></tr></tbody></table>

[AccountAgreementNext](/en/docs/mt5/api/config_common/imtconaccountallocation/imtconaccountallocation_accountagreementnext)

[Enumerations](/en/docs/mt5/api/config_common/imtconaccountagreement/imtconaccountagreement_enum)