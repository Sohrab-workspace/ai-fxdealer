# Configuration of Groups

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_group

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Groups

# Configuration of Groups

The MetaTrader 5 API allows managing groups in the trading platform — adding new groups, modifying and deleting existing ones.

The following interfaces of group settings are available:

-   [IMTConGroup](/en/docs/mt5/api/config_group#imtcongroup)
-   [IMTConGroupSymbol](/en/docs/mt5/api/config_group#imtcongroupsymbol)
-   [IMTConGroupArray](/en/docs/mt5/api/config_group/imtcongrouparray)
-   [IMTConGroupSink](/en/docs/mt5/api/config_group#imtgroupsink)
-   [IMTConCommTier](/en/docs/mt5/api/config_group#commission)
-   [IMTConCommission](/en/docs/mt5/api/config_group#commission)

The below figure shows different elements of group configuration in the MetaTrader 5 Administrator, to help you understand the purpose of the interfaces:

![Configuration of groups in MetaTrader 5 Administrator](/en/docs/mt5/api/img/groups.png "Configuration of groups in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [Group name](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_group).
2.  [The server to which the group is linked](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_server).
3.  [The type of authorization](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_authmode).
4.  The [Margin Call](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_margincall) and [Stop Out](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_marginstopout) levels.
5.  [The group deposit currency](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_currency).

Below is a detailed description of the correspondence of methods and group settings in the MetaTrader 5 Administrator.

## IMTConGroup [#](config_group#imtcongroup)

The [IMTConGroup](/en/docs/mt5/api/config_group/imtcongroup) interface provides access to the main group settings. In MetaTrader 5 Administrator, group settings are divided into several tabs:

-   [Common](/en/docs/mt5/api/config_group#common)
-   [Company](/en/docs/mt5/api/config_group#company)
-   [News&Mail](/en/docs/mt5/api/config_group#news_mail)
-   [Permissions](/en/docs/mt5/api/config_group#permissions)
-   [Margin](/en/docs/mt5/api/config_group#margin)
-   [Symbols](/en/docs/mt5/api/config_group#symbols)
-   [Commissions](/en/docs/mt5/api/config_group#commissions)
-   [Reports](/en/docs/mt5/api/config_group#reports)

### Common [#](config_group#common)

![The "Common" tab](/en/docs/mt5/api/img/groups_common.png "The "Common" tab")

The following elements are shown above:

1.  [Group name](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_group).
2.  [Deposit currency](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_currency).
3.  [A trade server to which the group is linked](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_server).
4.  [The type of authorization for the clients in the group](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_authmode).
5.  [Minimum length of account password](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_authpasswordmin).
6.  [Allow accounts from the group to connect to the server](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_permissionsflags).
7.  [Enable confirmation of certificates](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_permissionsflags).
8.  [Forced password change upon first connection](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_permissionsflags).

### Company [#](config_group#company)

![The "Company" tab](/en/docs/mt5/api/img/groups_company.png "The "Company" tab")

The following elements are shown above:

1.  [The name of the company that services the group](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_company).
2.  [The address of the company's website](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_companypage).
3.  [The email address of the company](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_companyemail).
4.  [The address of the company's technical support website](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_companysupportpage).
5.  [The e-mail address for technical support of the company](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_companysupportemail).
6.  [A folder of templates of the company](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_companycatalog).

### News&Mail [#](config_group#news_mail)

![The "News&Mail" tab](/en/docs/mt5/api/img/groups_news_mail.png "The "News&Mail" tab")

The following elements are shown above:

1.  [The mode of news sending to the clients from the group](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_newsmode).
2.  [News categories available to the group](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_newscategory).
3.  [News languages available to the group](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_newslangadd).
4.  [An option of enabling and disabling the internal mail system](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_mailmode).

### Permissions [#](config_group#permissions)

![The "Permissions" tab](/en/docs/mt5/api/img/groups_permissions.png "The "Permissions" tab")

The following elements are shown above:

1.  [Maximum number of symbols available to the group](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_limitsymbols).
2.  [Available trading history](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_limithistory).
3.  [A default deposit for demo accounts](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_demodeposit).
4.  [The option enables/disables trading using Expert Advisors](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_tradeflags).
5.  [An option for enabling/disabling swap charging](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_tradeflags).
6.  [The option enables/disables the use of trailing stop](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_tradeflags).
7.  [The maximum number of placed orders at a time](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_limitorders).
8.  [The annual interest rate](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_tradeinterestrate).
9.  [Default leverage for demo accounts](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_demoleverage).
10.  [The option enables/disables the use of the Signals service](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_tradeflags).

### Margin [#](config_group#margin)

![The "Margin" tab](/en/docs/mt5/api/img/groups_margin.png "The "Margin" tab")

The following elements are shown above:

1.  [The Margin Call level](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_margincall).
2.  [The Stop Out level](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_marginstopout).
3.  [The mode of Margin Call and Stop Out check](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_marginsomode).
4.  [Including floating profit/loss into free margin calculation](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_marginfreemode).
5.  [Including daily recorded profit into free margin calculation](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_marginfreeprofitmode).
6.  [The amount of virtual credit](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_tradevirtualcredit).

### Symbols [#](config_group#symbols)

![The "Symbols" tab](/en/docs/mt5/api/img/groups_symbols.png "The "Symbols" tab")

The following elements are shown above:

1.  [Add a symbol configuration](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_symboladd).
2.  [Modify a symbol configuration](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_symbolupdate).
3.  [Delete a symbol configuration](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_symboldelete).

### Commissions [#](config_group#commissions)

![The "Commissions" tab](/en/docs/mt5/api/img/groups_commissions.png "The "Commissions" tab")

The following elements are shown above:

1.  [Add commission configuration](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_commissionadd).
2.  [Modify commission configuration](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_commissionupdate).
3.  [Delete commission configuration](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_commissiondelete).

### Reports [#](config_group#reports)

![The "Reports" tab](/en/docs/mt5/api/img/groups_reports.png "The "Reports" tab")

The following elements are shown above:

1.  [An option of enabling/disabling generation of daily reports](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_reportsmode).
2.  [An option of enabling/disabling emailing of reports](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_reportsflags).
3.  [Address of SMTP server for sending reports](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_reportssmtp).
4.  [A login to authorize on the SMTP server](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_reportssmtplogin).
5.  [A password to authorize on the SMTP server](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_reportssmtppass).
6.  [An option of enabling/disabling sending copies of reports to the technical support mailbox](/en/docs/mt5/api/config_group/imtcongroup/imtcongroup_reportsflags).

## IMTConGroupSymbol [#](config_group#imtcongroupsymbol)

The IMTConGroupSymbol interface provides access to individual symbol settings for a group. Dialogs of symbol settings for a group are similar to the dialogs of [common symbol settings](/en/docs/mt5/api/config_symbol#imtconsymbol). Therefore, here only some of the group symbol settings from MetaTrader 5 Administrator:

![Configuration of symbols in MetaTrader 5 Administrator](/en/docs/mt5/api/img/groups_symbol_settings.png "Configuration of symbols in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [Symbols to which settings apply](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_path).
2.  [The option of using default spread settings](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_spreaddiffdefault).
3.  [Spread difference](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_spreaddiff).
4.  [Spread balance difference](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_spreaddiffbalance).
5.  [Option of using default volume settings](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_volumemindefault).
6.  [Minimal volume](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_volumemin).
7.  [Volume change step](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_volumestep).
8.  [Maximal volume](/en/docs/mt5/api/config_group/imtcongroupsymbol/imtcongroupsymbol_volumemax).

## IMTConGroupSink [#](config_group#imtgroupsink)

The [IMTConGroupSink](/en/docs/mt5/api/config_group/imtcongroupsink) interface contains handlers of the events of group configuration changes.

## IMTConCommTier and IMTConCommission [#](config_group#commission)

These interfaces provide access to group commission settings. The [IMTConCommission](/en/docs/mt5/api/config_group/imtconcommission) interface provides access to the main commission settings, and [IMTConCommTier](/en/docs/mt5/api/config_group/imtconcommtier) — to the settings of commission levels.

![Configuration of commission levels in MetaTrader 5 Administrator](/en/docs/mt5/api/img/groups_commission_settings.png "Configuration of commission levels in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [Commission name](/en/docs/mt5/api/config_group/imtconcommission/imtconcommission_name).
2.  [Description of the commission](/en/docs/mt5/api/config_group/imtconcommission/imtconcommission_description).
3.  [Symbols, for which the commission is charged](/en/docs/mt5/api/config_group/imtconcommission/imtconcommission_path).
4.  [Type of ranges for commission levels](/en/docs/mt5/api/config_group/imtconcommission/imtconcommission_rangemode).
5.  [Type of commission](/en/docs/mt5/api/config_group/imtconcommission/imtconcommission_mode).
6.  [Adding a commission level](/en/docs/mt5/api/config_group/imtconcommission/imtconcommission_tieradd).
7.  [Editing a commission level](/en/docs/mt5/api/config_group/imtconcommission/imtconcommission_tierupdate).
8.  [Deleting a commission level](/en/docs/mt5/api/config_group/imtconcommission/imtconcommission_tierdelete).
9.  [Start of a commission level](/en/docs/mt5/api/config_group/imtconcommtier/imtconcommtier_rangefrom).
10.  [End of a commission level](/en/docs/mt5/api/config_group/imtconcommtier/imtconcommtier_rangeto).
11.  [Commission amount](/en/docs/mt5/api/config_group/imtconcommtier/imtconcommtier_value).
12.  [Maximum commission amount](/en/docs/mt5/api/config_group/imtconcommtier/imtconcommtier_minimal).
13.  [Method of commission charging](/en/docs/mt5/api/config_group/imtconcommtier/imtconcommtier_mode).
14.  [Commission calculation currency](/en/docs/mt5/api/config_group/imtconcommtier/imtconcommtier_currency).
15.  [Type of commission charging](/en/docs/mt5/api/config_group/imtconcommtier/imtconcommtier_type).

[OnSpreadSync](/en/docs/mt5/api/config_spread/imtconspreadsink/imtconspreadsink_onspreadsync)

[IMTConGroup](/en/docs/mt5/api/config_group/imtcongroup)