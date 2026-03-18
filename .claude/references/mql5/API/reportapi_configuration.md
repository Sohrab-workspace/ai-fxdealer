# Report Configuration

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_configuration

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
            -   [Purpose of the Report API](/en/docs/mt5/api/reportapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/reportapi_interaction)
            -   [Configuration of Reports](/en/docs/mt5/api/reportapi_configuration)
            -   [Request for Reports](/en/docs/mt5/api/reportapi_request)
            -   [Requirements for Modules](/en/docs/mt5/api/reportapi_requirements)
            -   [Creating a Simple Report](/en/docs/mt5/api/reportapi_simple_report)
            -   [Tabular Reports](/en/docs/mt5/api/reportapi_tables)
            -   [HTML Reports](/en/docs/mt5/api/reportapi_html)
            -   [Dashboards](/en/docs/mt5/api/reportapi_dashboards)
            -   [Templates](/en/docs/mt5/api/reportapi_html_template)
            -   [Charts](/en/docs/mt5/api/reportapi_html_charts)
            -   [Memory Management](/en/docs/mt5/api/reportapi_memory_management)
            -   [Multithreading](/en/docs/mt5/api/reportapi_multithreading)
            -   [Ready-made Examples](/en/docs/mt5/api/reportapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reportapi_entrypoints)
            -   [Report Plugin Interface](/en/docs/mt5/api/imtreportcontext)
            -   [Main Interface of Reports](/en/docs/mt5/api/imtreportapi)
            -   [Dashboard Interfaces](/en/docs/mt5/api/reportapi_dashboard)
            -   [Diagram Interfaces](/en/docs/mt5/api/reportapi_auxiliary)
            -   [Dataset Interfaces](/en/docs/mt5/api/reportapi_dataset)
            -   [Data Cache Interfaces](/en/docs/mt5/api/reportapi_cache)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)Configuration of Reports

# Report Configuration

In order for the server to start using the reports module, add its configuration via the Administrator terminal:

![Reports section](/en/docs/mt5/api/img/admin_report_list.png "Reports section")

To add or change the configuration of the module, click ![Add](/en/docs/mt5/api/img/add_button.png "Add") Add or ![Edit](/en/docs/mt5/api/img/edit_button.png "Edit") Edit on the toolbar or in the context menu.

![Editing the report settings](/en/docs/mt5/api/img/report_edit.png "Editing the report settings")

Fill in the following fields in this window:

-   Enable — enable/disable the report. The module starts operating immediately after the option is enabled and the configuration is saved. To get started, server restart is not required.
-   Name — name of the report configuration. The same name is indicated in the report list of the Manager terminal.
-   Type — all reports available on the server are displayed here. The list is compiled based on the DLL report files which are located under the /report directory of the main trading server.
-   Trade server — to the right of the Name field, select a trade server the report is configured for. The report will be generated using the data on the specified server; and it will be available only when a manager connects to the specified server.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Each configuration of the report is bound to a specific server and thus generates reports concerning this server only.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Reports are generated for a manager in accordance with his or her access permissions. Reports are generated only for available groups of accounts.</span></li></ul></td></tr></tbody></table>

## Parameters

At the bottom of the window, there is a control block for managing the external parameters of reports. These parameters are provided for when writing modules and allow you to manage them from outside.

The following commands are available for managing the parameters:

-   Add — add a new parameter. After clicking, a new line will appear in the window. In the Parameter field, specify the name of the parameter, and in Value, assign a value to this parameter. String type parameters are created by default. To select another type (integer or fractional) click the arrow on the "Add" button.
-   Edit — change the selected parameter. The same operation can be done by a double-click on the required field.
-   Delete — delete the selected parameter.

[Interaction with Servers](/en/docs/mt5/api/reportapi_interaction)

[Request for Reports](/en/docs/mt5/api/reportapi_request)