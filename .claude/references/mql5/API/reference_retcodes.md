# Return Codes

> Source: https://support.metaquotes.net/en/docs/mt5/api/reference_retcodes

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
            -   [Successful completion](/en/docs/mt5/api/retcodes_successful)
            -   [Common errors](/en/docs/mt5/api/retcodes_common)
            -   [Authentication](/en/docs/mt5/api/retcodes_authentication)
            -   [Configuration Management](/en/docs/mt5/api/retcodes_configs)
            -   [User management](/en/docs/mt5/api/retcodes_clients)
            -   [Trade management](/en/docs/mt5/api/retcodes_trades)
            -   [Report Generation](/en/docs/mt5/api/retcodes_reports)
            -   [Price Data](/en/docs/mt5/api/retcodes_price_history)
            -   [Trade Requests](/en/docs/mt5/api/retcodes_trade_request)
            -   [Dealer](/en/docs/mt5/api/retcodes_dealer)
            -   [API](/en/docs/mt5/api/retcodes_api)
            -   [Messengers](/en/docs/mt5/api/retcodes_messenger)
            -   [Subscriptions](/en/docs/mt5/api/retcodes_subscription)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)Return Codes

# Return Codes

The vast majority of functions in the MetaTrader 5 API return a special code to notify of the results of their implementation To develop high-quality, stable applications, a programmer should check the return codes of functions of called API methods.

Return codes are contained in the EnMTAPIRetcode enumeration, in file MT5APIConstants.h and are divided into several groups:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Group of codes</span></p></th><th class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Range of values</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_successful" class="topiclink">Successful completion</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">0-1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes that are returned with the successful completion of an operation.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_common" class="topiclink">Common errors</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">2-999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes returned when common errors occur.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_authentication" class="topiclink">Authentication</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">1000-1999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes returned during the authentication of users.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_configs" class="topiclink">Configuration management</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">2000-2999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes that are returned when changing configurations.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_clients" class="topiclink">User management</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">3000-3999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The codes returned when working with the database of users.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_trades" class="topiclink">Trade management</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">4000-4999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The codes returned when working with the trading database.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_reports" class="topiclink">Report Generation</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">5000-5999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes that are returned when generating reports.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_price_history" class="topiclink">Price Data</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">6000-6999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes that are returned when working with price data.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_trade_request" class="topiclink">Trade Requests</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">10000-10999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes returned while processing trade requests.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_dealer" class="topiclink">Dealer</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">11000-11999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes returned during the work of a dealer.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_api" class="topiclink">API</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">12000-12999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes related to the operation of API.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_messenger" class="topiclink">Instant messengers</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">14000-14999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes related to message sending via instant messengers.</span></p></td></tr><tr class="table"><td class="table" style="width:188px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/retcodes_subscription" class="topiclink">Subscriptions</a></span></p></td><td class="table" style="width:142px;"><p class="p_fortable"><span class="f_fortable">15000-15999</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Codes related to the operation of the <a href="https://support.metaquotes.net/en/docs/mt5/platform/administration/subscriptions" target="_blank" class="weblink">Subscriptions</a> service.</span></p></td></tr></tbody></table>

[Journal Constants](/en/docs/mt5/api/journal)

[Successful completion](/en/docs/mt5/api/retcodes_successful)