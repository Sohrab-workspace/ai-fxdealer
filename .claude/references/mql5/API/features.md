# Development Features

> Source: https://support.metaquotes.net/en/docs/mt5/api/features

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)Development Features

# Development Features

A number of important features of MetaTrader 5 API should be taken into account when developing applications. This will help to avoid many common issues.

## Operations with Volumes [#](features#volume)

MetaTrader 5 API supports two volume operation modes, implying standard and extended accuracy: 4 and 8 decimal places respectively. For that purpose, each structure and interface implying volumes provides pairs of members/methods. For example:

-   [IMTConfirm::Volume](/en/docs/mt5/api/reference_trading/trading_request/imtconfirm/imtconfirm_volume), [IMTExecution::DealVolume](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolume) — standard volume accuracy is used
-   [IMTConfirm::VolumeExt](/en/docs/mt5/api/reference_trading/trading_request/imtconfirm/imtconfirm_volumeext), [IMTExecution::DealVolumeExt](/en/docs/mt5/api/reference_trading/trading_request/imtexecution/imtexecution_dealvolumeext) — extended volume accuracy is used

All increased volume accuracy methods have names with the "Ext" addition. The standard mode is suitable for the most trading symbols. The extended accuracy mode is intended for cryptocurrencies.

In all methods which use standard accuracy, the volume is indicated as multiplied by 10,000. For example, 100 means 0.01 lots. In all extended accuracy methods, the volume is indicated as multiplied by 100,000,000. For example, 10,000,000 means 0.1 lot.

On the platform side, volume storage is not divided into two entities (normal and increased accuracy), the value is always stored in the INT64 format, with the fixed 8-digit accuracy. For example, IMTConfirm::Volume and IMTConfirm::VolumeExt methods read and set the same value on the platform side. If you set 1-lot volume using the IMTConfirm::Volume(10000) set-method, the same 1-lot volume will be obtained via the IMTConfirm::VolumeExt get-method, but it will be represented as a value of 100,000,000.

In structures (such as [MTTick](/en/docs/mt5/api/mttick)), the extended volume accuracy always has higher priority. When passing a structure in which both volume types are filled, the server will use the extended accuracy value. When returning volume values, the server fills both fields: with standard and extended accuracy.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">We strongly recommend not to mix methods utilizing different accuracy volumes within one project. If you switch to extended volume accuracy, make sure to convert the entire project to the extended accuracy rather than separate methods.</span></p></td></tr></tbody></table>

## Correspondence of software interfaces to the terminal GUI

The descriptions of the interfaces of configuration bases and database provide illustrations showing the correspondence of their methods to elements of the MetaTrader 5 Administrator and MetaTrader 5 Manager interface. The detailed descriptions of the platform functions are available in the References of appropriate terminals. The API documentation only provides a brief description of their nature and focuses mainly on programming features.

## Reserved Fields in Structures

Many structures used in MetaTrader 5 API contain reserved fields. It is not recommended to use these fields for your own needs. The trading platform developer may at any time remove or replace these fields.

## Resetting Structures

Before using structures, it is recommended to initialize them to zero. An example:

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_CodeExample">MTTick&nbsp;tick={0};</span></p></td></tr></tbody></table>

[DirectoryClean](/en/docs/mt5/api/cmtfile/cmtfile_directoryclean)

[List of Events](/en/docs/mt5/api/event_list)