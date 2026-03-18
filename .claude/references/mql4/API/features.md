# Development Features

> Source: https://support.metaquotes.net/en/docs/mt4/api/features

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
-   [MetaTrader 4](/en/docs/mt4)
    -   [Administrator](/en/docs/mt4/administrator)
    -   [Manager](/en/docs/mt4/manager)
    -   [Client terminal](/en/docs/mt4/terminal)
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
        -   [Development Features](/en/docs/mt4/api/features)
        -   [Structures](/en/docs/mt4/api/reference_structures)
        -   [Return Codes](/en/docs/mt4/api/reference_retcodes)
        -   [Server API](/en/docs/mt4/api/server_api)
        -   [Manager API](/en/docs/mt4/api/manager_api)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)Development Features

# Development Features

A number of important features of MetaTrader 4 API should be taken into account when developing applications. This will help to avoid many common issues.

## 32-bit time\_t

MetaTrader 4 API uses 32-bit [time\_t](https://msdn.microsoft.com/en-us/library/vstudio/4wacf567.aspx) type, but in recent versions of Microsoft Visual Studio the default value of this type is 64 bits. Macro \_USE\_32BIT\_TIME\_T should be set in the compilation directives when working with projects.

![Add macros _USE_32BIT_TIME_T and _CRT_SECURO_NO_WARNINGS in the compilation directives](/en/docs/mt4/api/img/time_t.png "Add macros _USE_32BIT_TIME_T and _CRT_SECURO_NO_WARNINGS in the compilation directives")

## Specification of Lots

In all functions and structures, volume in lots is specified as a value multiplied by 100: 100 means 1 lot, 1 means 0.01 lots.

## Links to Detailed Descriptions in other References

Many sections of MetaTrader 4 API Reference contain links to documentation on other platform components, including MetaTrader 4 Administrator User Guide. The links provide the detailed descriptions of the platform functions. The API documentation only contains a brief description of their nature and focuses mainly on programming features.

## Reserved Fields in Structures

Many structures used in MetaTrader 4 API contain reserved fields. It is not recommended to use these fields for your own needs. The trading platform developer may at any time remove or replace these fields.

## Resetting Structures

Before using structures, it is recommended to initialize them to zero. Example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">UserInfo</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">uinf={0};</span></p></td></tr></tbody></table>

## Adding Descriptions of Exported Functions to a Project

When developing plug-ins ([Server API](/en/docs/mt4/api/server_api)) and data feeds ([DataFeed API](/en/docs/mt4/api/datafeed_api)), a DEF file with descriptions of all exported functions must be included into the project. Example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">LIBRARY</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">AdvancedDealerHelper</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample">EXPORTS</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvAbout</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvStartup</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvPluginCfgAdd</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvPluginCfgSet</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvPluginCfgGet</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvPluginCfgNext</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvPluginCfgDelete</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvPluginCfgTotal</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvTradeRequestApply</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">MtSrvHistoryTickApply</span></p></td></tr></tbody></table>

[API](/en/docs/mt4/api)

[Structures](/en/docs/mt4/api/reference_structures)