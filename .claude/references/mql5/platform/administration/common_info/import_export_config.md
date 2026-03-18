# Import and Export Settings

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/common_info/import_export_config

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
                -   [Trading System](/en/docs/mt5/platform/administration/common_info/general_concept)
                -   [Price Data](/en/docs/mt5/platform/administration/common_info/price_data)
                -   [Working with Instructions](/en/docs/mt5/platform/administration/common_info/common_instructions)
                -   [Specifying Symbols and Groups](/en/docs/mt5/platform/administration/common_info/common_mask)
                -   [Data Export](/en/docs/mt5/platform/administration/common_info/export)
                -   [Import/Export Settings](/en/docs/mt5/platform/administration/common_info/import_export_config)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[General Information](/en/docs/mt5/platform/administration/common_info)Import/Export Settings

# Import and Export Settings

The administrator terminal allows to quickly export and import almost all settings of the trade platform. This functionality can be useful, for example, if you need to set up a test platform with the settings similar to your work platform.

## Export [#](import_export_config#export)

The platform settings are exported in a text file in the JSON format. To start the export, open the context menu of the platform and click "![Export](/en/docs/mt5/platform/img/export_button.png "Export") Export":

![Exporting the platform settings](/en/docs/mt5/platform/img/export_config.png "Exporting the platform settings")

The dialog where you can select the settings to be exported appears:

![Selecting the settings to be exported](/en/docs/mt5/platform/img/export_config_select.png "Selecting the settings to be exported")

Select the necessary settings and click "Export". Then specify a folder to save the file with settings.

## Import [#](import_export_config#import)

To import the settings, open the platform context menu as described above and click "![Import](/en/docs/mt5/platform/img/import_button.png "Import") Import".

![Importing the settings](/en/docs/mt5/platform/img/import_config.png "Importing the settings")

Select settings that should be imported. All non-selected items are skipped, while the appropriate platform settings remain unchanged. Using the "View" button you can check any imported configuration and change it if needed:

![Viewing the report configuration](/en/docs/mt5/platform/img/import_config_view.png "Viewing the report configuration")

After changing the settings in the preview mode, click "OK" and then "Import".

If an imported configuration does not exist in the platform, it will be created. If an imported configuration matches an existing configuration in the trade platform, the existing configuration settings will be updated. Configurations are compared by their key parameters, for example, group name, manager login (account number), routing rule name, etc.

Configurations of reports, plugins and funds are bound to specific servers in the cluster. When you export their settings, server IDs are also saved in JSON files. During import, the system checks the ID specified in the file and binds the configuration to the appropriate server. If the platform with the specified ID does not have a server with the specified identifier, the configuration will be bound to the main trade server. If necessary, you can change binding in the preview mode.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Be careful when importing the settings. It can seriously affect the operation of the trade platform.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Settings files use the UTF-16 Little Endian encoding. Files in other encodings cannot be imported.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Starting with the platform build 1930, all volume settings are exported in two versions: with standard and extended accuracy. For example, <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#volumes" class="topiclink">the minimum symbol volume</a> is exported as "VolumeMin" : "100" and "VolumeMinExt" : "1000000" (lots are obtained by dividing the values by 10000 and 100000000, respectively). Extended volume accuracy has a higher priority during import. If it is not specified (for example, if settings are exported by an older terminal version), the value with standard accuracy will be used.</span></li></ul></td></tr></tbody></table>

## Export and Import via Command Line [#](import_export_config#command_line)

To automate the configuration process, as well as to automate the transfer of platform settings without having to develop additional plugins and applications in C++, you can use command line export and import.

Close the Administrator terminal before executing commands in console mode. Otherwise, the commands will not be executed because the second copy of the application cannot be run in parallel.

In order to start MetaTrader 5 Administrator in the console mode, use the /console key:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">/console</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/server:&lt;Trade</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Server</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Address:Port&gt;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/login:&lt;Login&gt;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/password:&lt;Password&gt;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">/action:&lt;Command&gt;</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">[Command</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">Arguments]</span></p></td></tr></tbody></table>

Specify platform connection details in the 'server', 'login' and 'password' parameters. Specify the type of performed action in the 'action' parameter:

### Server Restart

Command /action:restart \[/name:<server name>\]. Optionally specify the server name (History, Access...). If the name is specified, the appropriate sever will be searched for (case insensitive). If the name is not specified, the command will be performed for the current connected server.

### Export of a Configuration to JSON

Command /action:export /file:<path> \[/type:<type> /config:<mask>\]. If no optional arguments are specified, the entire configuration of the connected server will be exported.

Argument /file:<path> sets the destination file path. Argument /type:<type> is used for exporting a selected configuration branch, the argument may have the following values:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">common</span><br><span class="f_CodeExample">network</span><br><span class="f_CodeExample">firewall</span><br><span class="f_CodeExample">time</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><br><span class="f_CodeExample">holidays</span><br><span class="f_CodeExample">groups</span><br><span class="f_CodeExample">managers</span><br><span class="f_CodeExample">routing</span><br><span class="f_CodeExample">gateways</span><br><span class="f_CodeExample">plugins</span><br><span class="f_CodeExample">feeders</span><br><span class="f_CodeExample">reports</span><br><span class="f_CodeExample">symbols</span><br><span class="f_CodeExample">spreads</span><br><span class="f_CodeExample">historysync</span></p></td></tr></tbody></table>

Argument /config:<mask> sets a search criterion to search for a particular configuration structure by a string mask (can contain \*,!). Search by mask can be used for the configurations of servers, groups, managers, trade requests, gateways, plugins, data feeds, reports, and symbols. The following rule applies to the rest of configurations: if a mask is set, the configuration should be skipped, if no mask is specified, the configuration should be processed.

### Import of a Configuration

Command /action:import /file:<path> \[/type:<type> /config:<mask>\]. All arguments are similar to those applied to exports, except for the /type argument. Branch common (common platform settings) cannot be imported.

[Data Export](/en/docs/mt5/platform/administration/common_info/export)

[Start Page](/en/docs/mt5/platform/administration/admin_start)