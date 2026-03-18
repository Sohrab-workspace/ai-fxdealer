# Journal Constants

> Source: https://support.metaquotes.net/en/docs/mt5/api/journal

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)Journal Constants

# Journal Constants

The MetaTrader 5 API provides access to server logs. A number of the constants described in the MT5APILogger.h file are available for working with the logs. The constants are described in the following enumerations:

-   [EnMTLogCode](/en/docs/mt5/api/journal#enmtlogcode) — types of log messages.
-   [EnMTLogRequestMode](/en/docs/mt5/api/journal#enmtlogrequestmode) — types of events recorded in the log.
-   [EnMTLogType](/en/docs/mt5/api/journal#enmtlogtype) — types of log requests.
-   [EnMTLogFlags](/en/docs/mt5/api/journal#enmtlogflags) — flags of log entries.

## Message Types [#](journal#enmtlogcode)

Types of log messages are listed in the EnMTLogCode enumeration:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable">MTLogFolder</span></p></td><td class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable">-1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable">MTLogOK</span></p></td><td class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable">0</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Information message.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable">MTLogWarn</span></p></td><td class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable">1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Warning.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable">MTLogErr</span></p></td><td class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable">2</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Error message.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable">MTLogAtt</span></p></td><td class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable">3</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Critical error message.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable">MTLogLogin</span></p></td><td class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable">4</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">System login message.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable">MTLogFirst</span></p></td><td class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Beginning of enumeration. It corresponds to MTLogFolder.</span></p></td></tr><tr class="table"><td class="table" style="width:133px;"><p class="p_fortable"><span class="f_fortable">MTLogLast</span></p></td><td class="table" style="width:85px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">End of the enumeration. It corresponds to MTLogLogin.</span></p></td></tr></tbody></table>

This enumeration is used in the following methods:

-   [IMTAdminAPI::LoggerOut](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggerout)
-   [IMTManagerAPI::LoggerOut](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerout)
-   [IMTGatewayAPI::LoggerOut](/en/docs/mt5/api/imtgatewayapi/imtgatewayapi_common/imtgatewayapi_loggerout)
-   [IMTSerserAPI::LoggerOut](/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_loggerout)

## Request Types [#](journal#enmtlogrequestmode)

The types of request of the server journal are listed in the EnMTLogRequestMode enumeration:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">MTLogModeStd</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">0</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A standard request mode. All messages except for user connection notifications are requested.</span></p></td></tr><tr class="table"><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">MTLogModeErr</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">In this mode, only error messages (<a href="/en/docs/mt5/api/journal#enmtlogcode" class="topiclink">MTLogErr</a>) are requested.</span></p></td></tr><tr class="table"><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">MTLogModeFull</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">2</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">All types of log entries are requested when this mode is selected.</span></p></td></tr><tr class="table"><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">MTLogModeFirst</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Beginning of enumeration. It corresponds to MTLogModeStd.</span></p></td></tr><tr class="table"><td class="table" style="width:138px;"><p class="p_fortable"><span class="f_fortable">MTLogModeLast</span></p></td><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">End of enumeration. It corresponds to MTLogModeFull.</span></p></td></tr></tbody></table>

This enumeration is used in the following methods:

-   [IMTAdminAPI::LoggerServerRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggerserverrequest)
-   [IMTManagerAPI::LoggerServerRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerserverrequest)
-   [IMTServerAPI::LoggerRequest](/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_loggerrequest)

## Event Types [#](journal#enmtlogtype)

Types of events that are reflected in the journal logs are listed in the enumeration EnMTLogType:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeAll</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">0</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">All types of events.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeCfg</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Events of <a href="/en/docs/mt5/api/imtadminapi/imtadminapi_config" class="topiclink">configuration</a> changes.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeSys</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">2</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">System events.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeNet</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">3</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Events related to the network activity.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeHst</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">4</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Events associated with <a href="/en/docs/mt5/api/reference_ticks" class="topiclink">price data</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeUser</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">5</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Events associated with <a href="/en/docs/mt5/api/reference_user" class="topiclink">users</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeTrade</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">6</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtadminapi/imtadminapi_trading" class="topiclink">Trade</a> events.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeAPI</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">7</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Events associated with the Server API.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeNotify</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">8</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Various notifications. For example, messages related to <a href="https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_managers#control" target="_blank" class="weblink">monitoring operations of managers</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeLiveUpdate</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">16</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Events associated with the Live Update service.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeSendMail</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">17</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Events associated with email.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeFailover</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">18</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/backup_server_switch" target="_blank" class="weblink">Failover</a> process log (mt5failover.log).</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeSwitch</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">19</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">A copy of the backup server log for the last day (<a href="https://support.metaquotes.net/en/docs/mt5/platform/components/backup_server/backup_server_features#journal" target="_blank" class="weblink">*.log.failover</a>).</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeFirst</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Beginning of enumeration. It corresponds to MTLogTypeAll.</span></p></td></tr><tr class="table"><td class="table" style="width:157px;"><p class="p_fortable"><span class="f_fortable">MTLogTypeLast</span></p></td><td class="table" style="width:98px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">End of enumeration. It corresponds to MTLogTypeSendMail.</span></p></td></tr></tbody></table>

The events of update (MTLogTypeLiveUpdate) and email (MTLogTypeSendMail) are generated not at the server side, but by separate applications — mt5srvupdater.exe and mt5sendmail.exe.

This enumeration is used in the following methods:

-   [IMTAdminAPI::LoggerServerRequest](/en/docs/mt5/api/imtadminapi/imtadminapi_common/imtadminapi_loggerserverrequest)
-   [IMTManagerAPI::LoggerServerRequest](/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_common/imtmanagerapi_loggerserverrequest)
-   [IMTServerAPI::LoggerRequest](/en/docs/mt5/api/imtserverapi/serverapi_common/imtserverapi_loggerrequest)

## Log Flags [#](journal#enmtlogflags)

Flags that journal entries may have are listed in EnMTLogFlags:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:164px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:164px;"><p class="p_fortable"><span class="f_fortable">LOG_FLAGS_NONE</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">0</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The log does not have flags.</span></p></td></tr><tr class="table"><td class="table" style="width:164px;"><p class="p_fortable"><span class="f_fortable">LOG_FLAGS_CORRUPTED</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">The log has an invalid checksum (damaged or changed from outside).</span></p></td></tr><tr class="table"><td class="table" style="width:164px;"><p class="p_fortable"><span class="f_fortable">LOG_FLAGS_FIRST</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Beginning of enumeration. It corresponds to LOG_FLAGS_NONE.</span></p></td></tr><tr class="table"><td class="table" style="width:164px;"><p class="p_fortable"><span class="f_fortable">LOG_FLAGS_ALL</span></p></td><td class="table" style="width:78px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">End of enumeration. It corresponds to LOG_FLAGS_CORRUPTED.</span></p></td></tr></tbody></table>

[Internal Data Types](/en/docs/mt5/api/reference_types)

[Return Codes](/en/docs/mt5/api/reference_retcodes)