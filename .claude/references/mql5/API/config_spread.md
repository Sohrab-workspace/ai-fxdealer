# Configuration of Spreads

> Source: https://support.metaquotes.net/en/docs/mt5/api/config_spread

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
                -   [IMTConSpread](/en/docs/mt5/api/config_spread/imtconspread)
                -   [IMTConSpreadLeg](/en/docs/mt5/api/config_spread/imtconspreadleg)
                -   [IMTConSpreadSink](/en/docs/mt5/api/config_spread/imtconspreadsink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Configuration Interfaces](/en/docs/mt5/api/reference_configurations)Spreads

# Configuration of Spreads

MetaTrader 5 API allows users to configure the charging of the margin in case client's trading positions are in a spread to one another. The spread is defined as the presence of the oppositely directed positions at related symbols. Reduced margin requirements provide more trading opportunities for traders.

The following symbol interfaces are available:

-   [IMTConSpreadLeg](/en/docs/mt5/api/config_spread#imtconspreadleg)
-   [IMTConSpread](/en/docs/mt5/api/config_spread#imtconspread)
-   [IMTConSpreadSink](/en/docs/mt5/api/config_spread#imtconspreadsink)

For better understanding the purpose of the interfaces, the figure below shows different elements of spread configuration in MetaTrader 5 Administrator:

![Configuring spreads in MetaTrader 5 Administrator](/en/docs/mt5/api/img/spreads.png "Configuring spreads in MetaTrader 5 Administrator")

The following elements are shown above:

1.  [Spread A leg](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_alegadd)
2.  [Spread B leg](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_blegadd)
3.  [Charged margin](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_margintype)

Below is a detailed description of the correspondence of methods and spread settings in the MetaTrader 5 Administrator.

## IMTConSpreadLeg [#](config_spread#imtconspreadleg)

[IMTConSpreadLeg](/en/docs/mt5/api/config_spread/imtconspreadleg) interface provides access to configuration of spread legs.

![Spread leg](/en/docs/mt5/api/img/spread_leg.png "Spread leg")

The figure shows the sessions configuration dialog in MetaTrader 5 Administrator:

1.  [Weight](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_ratio)
2.  [Leg specification mode](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_mode)
3.  [Symbol or basic asset](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_symbol)
4.  [Beginning of the period (for a basic asset)](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_timefrom)
5.  [End of the period (for a basic asset)](/en/docs/mt5/api/config_spread/imtconspreadleg/imtconspreadleg_timeto)

## IMTConSpread [#](config_spread#imtconspread)

[IMTConSpread](/en/docs/mt5/api/config_spread/imtconspread) interface provides access to configuration of spread settings.

![Configuring spread](/en/docs/mt5/api/img/spread_config.png "Configuring spread")

The figure shows the spread configuration dialog in MetaTrader 5 Administrator:

1.  [Margin charging type](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_margintype)
2.  [Initial margin](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_margininitial)
3.  [Maintenance margin](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_marginmaintenance)
4.  [Adding a spread leg](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_alegadd)
5.  [Changing a spread leg](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_alegupdate)
6.  [Deleting a spread leg](/en/docs/mt5/api/config_spread/imtconspread/imtconspread_alegdelete)

## IMTConSpreadSink [#](config_spread#imtconspreadsink)

[IMTConSpreadSink](/en/docs/mt5/api/config_spread/imtconspreadsink) interface contains the handlers of the events of spread configuration changes.

[HookSymbolDelete](/en/docs/mt5/api/config_symbol/imtconsymbolsink/imtconsymbolsink_hooksymboldelete)

[IMTConSpread](/en/docs/mt5/api/config_spread/imtconspread)