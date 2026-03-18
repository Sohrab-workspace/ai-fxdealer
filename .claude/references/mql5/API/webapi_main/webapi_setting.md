# Settings Files

> Source: https://support.metaquotes.net/en/docs/mt5/api/webapi_main/webapi_setting

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
            -   [Getting Started](/en/docs/mt5/api/webapi_preparing)
            -   [Format of Commands](/en/docs/mt5/api/webapi_https)
            -   [Authentication](/en/docs/mt5/api/webapi_rest_authentication)
            -   [Escaping Special Characters](/en/docs/mt5/api/webapi_screening)
            -   [Maintaining Connections](/en/docs/mt5/api/webapi_pings)
            -   [Protocol Extension](/en/docs/mt5/api/webapi_protocol_extension)
            -   [Examples](/en/docs/mt5/api/webapi_examples)
            -   [Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)
                -   [Configuration Databases](/en/docs/mt5/api/webapi_main/webapi_config)
                -   [Trading](/en/docs/mt5/api/webapi_main/webapi_trading)
                -   [Users](/en/docs/mt5/api/webapi_main/webapi_users)
                -   [Clients](/en/docs/mt5/api/webapi_main/webapi_client)
                -   [Mail](/en/docs/mt5/api/webapi_main/webapi_mail)
                -   [News](/en/docs/mt5/api/webapi_main/webapi_news)
                -   [Prices](/en/docs/mt5/api/webapi_main/webapi_prices)
                -   [Daily Reports](/en/docs/mt5/api/webapi_main/webapi_daily)
                -   [Settings Files](/en/docs/mt5/api/webapi_main/webapi_setting)
                    -   [Get](/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_get)
                    -   [Update](/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_set)
                    -   [Delete](/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_delete)
                -   [Subscriptions](/en/docs/mt5/api/webapi_main/webapi_subscription)
                -   [Common Requests](/en/docs/mt5/api/webapi_main/webapi_common_request)
                -   [Outdated version of Rest API](/en/docs/mt5/api/webapi_main/webapi_old)
                -   [PHP Implementation of Protocol](/en/docs/mt5/api/webapi_main/php)
                -   [.NET Implementation of Protocol](/en/docs/mt5/api/webapi_main/net)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Web API](/en/docs/mt5/api/webapi)[Manager Interface (Rest API)](/en/docs/mt5/api/webapi_main)Settings Files

# Settings Files

The Web API allows saving application settings on a trade server and accessing them at any time. Settings are stored in a special directory separately for each manager account, which uses the API: \[trade server directory\]\\settings\\\[manager login\]\\.

This option enables quickly setup of the manager's workplace. For example, if the manager changes the computer, there will be no need to re-configure the web-application. Instead, you can easily apply settings, which were saved previously on the trade server. It is also possible to create several sets of manager settings for performing certain tasks.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Only one level of nesting and no more than 128 folders can be stored inside each manager directory. The maximum number of settings files is 1024. The size of each configuration file is no more than 16 MB.</span></li><li class="p_tableatten"><span class="f_tableatten">Settings are saved and accessed on the server, to which the Web API client is connected (on which the connected manager account is located). If you have multiple servers, you need to save the settings on each server.</span></li><li class="p_tableatten"><span class="f_tableatten">This function is secure for the trade server: the Web API does not allow sending potentially dangerous file types to the server (for example, *.exe). Only files with the following extensions are allowed: ini, cfg, dat, json, config, sqlite, xml, conf, settings, key, db, txt and log, as well as files without extensions. Furthermore, the content can only be represented as a JSON document.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The Web API allows you to receive configuration files which were set via the <a href="/en/docs/mt5/api/imtmanagerapi/imtmanagerapi_setting" class="topiclink">Manager API</a>, but only if the file contents are a JSON document.</span></li></ul></td></tr></tbody></table>

## The General Scheme of operations with the settings

Settings are stored in a special directory of the trade server: \[trade server directory\]\\settings\\\[manager login\]\\.

-   A web application can receive the settings file via the [/api/setting/get](/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_get) request. For example, during the application launch or when the user executes an appropriate command.
-   The settings are read from the file and applied.
-   If the user edits settings during the application operation, the application can update the settings file on the trade server via the [/api/setting/set](/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_set) method.

Please note that settings comprise one whole file. You cannot update an individual setting on the server. To update a setting, it is necessary to generate a whole file with all settings. For the Web API, file contents can only be a valid JSON document.

Settings should not be updated on the server too often, i.e. every time when settings are edited on the application side. After editing settings, the user can immediately change some other settings or revert changes. It is recommended to send updates not more than once in 5 minutes.

Several applications can work with the same settings files, including different types of APIs. The Web API does not track changes in files on the server side. Every call of [/api/setting/set](/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_set) rewrites the specified settings file, even if it has already been changed by another application. The server always stores the last submitted version.

## Requests for working with the settings files

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:130px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Request</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:130px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_get" class="topiclink">/api/setting/get</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Receive the settings file from the trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:130px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_set" class="topiclink">/api/setting/set</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Send the settings file to the trade server.</span></p></td></tr><tr class="table"><td class="table" style="width:130px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_delete" class="topiclink">/api/setting/delete</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete the settings file on the trade server.</span></p></td></tr></tbody></table>

[Get Light Paged](/en/docs/mt5/api/webapi_main/webapi_daily/webapi_daily_get_light_page)

[Get](/en/docs/mt5/api/webapi_main/webapi_setting/webapi_setting_get)