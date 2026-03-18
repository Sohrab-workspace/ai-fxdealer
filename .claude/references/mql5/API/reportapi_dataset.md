# Dataset interfaces

> Source: https://support.metaquotes.net/en/docs/mt5/api/reportapi_dataset

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
                -   [IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset)
                -   [IMTDatasetField](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield)
                -   [IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest)
                -   [IMTDatasetColumn](/en/docs/mt5/api/reportapi_dataset/imtdatasetcolumn)
                -   [IMTDatasetSummary](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Report API](/en/docs/mt5/api/reportapi)Dataset Interfaces

# Dataset interfaces

The interfaces described in this section are used for preparing source data for creating [dashboards](/en/docs/mt5/api/reportapi_dashboards) and [tabular reports](/en/docs/mt5/api/reportapi_tables). Data in a set is stored as a table with a set of columns and rows and a special summary row.

The following interfaces are provided for managing data sets:

-   [IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset) — description of a data set which consists of rows and columns.
-   [IMTDatasetColumn](/en/docs/mt5/api/reportapi_dataset/imtdatasetcolumn) — description of a column in a data set.
-   [IMTDatasetSummary](/en/docs/mt5/api/reportapi_dataset/imtdatasetsummary) — description of a summary row in a data set.

## Highly efficient requests for information from databases [#](reportapi_dataset#request)

The Report API enables highly efficient queries to the trading platform databases, with the flexible description of selection conditions (similar to SQL queries). Two interfaces are provided for operations with data requests: [IMTDatasetField](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield) for describing conditions, [IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest) for describing a request as a set of conditions.

To request data perform the following steps:

1.  Use the [IMTReprotAPI::DatasetRequestCreate](/en/docs/mt5/api/imtreportapi/imtreportapi_dataset/imtreportapi_datasetrequestcreate) method to create a data request object ([IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest)).
2.  Use [IMTReportAPI::DatasetAppend](/en/docs/mt5/api/imtreportapi/imtreportapi_dataset/imtreportapi_datasetappend) to create an object of a data set to which the query results will be added ([IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset))
3.  Use [IMTDatasetRequest::FieldCreate](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest/imtdatasetrequest_fieldcreate) to create the object of a field data for which will be requested ([IMTDatasetField](/en/docs/mt5/api/reportapi_dataset)).
4.  Describe the request condition using [IMTDatasetField](/en/docs/mt5/api/reportapi_dataset) methods and add it to the request object using the [IMTDatasetRequest::FieldAdd](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest/imtdatasetrequest_fieldadd) method.
5.  If you need to specify multiple conditions, repeat steps 3 and 4.
6.  Depending on the database from which you want to request data, call [IMTReportAPI::UserSelect](/en/docs/mt5/api/imtreportapi/imtreportapi_user/imtreportapi_userselect), [IMTReportAPI::ClientSelect](/en/docs/mt5/api/imtreportapi/imtreportapi_user/imtreportapi_clientselect) or [IMTReportAPI::DealSelect](/en/docs/mt5/api/imtreportapi/imtreportapi_trade/imtreportapi_deal/imtreportapi_dealselect), while passing to it the prepared request object ([IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest)).
7.  The request result will be added to the previously created data set object ([IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset)). Note that only fields marked as selected ([IMTDatasetField::FLAG\_SELECT](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield/imtdatasetfield_enum#enfieldflags)) are added to the resulting data set.

Data request examples are provided in the source code of the Capital report, which is available in "\[Report API installation directory\]\\Report\\Examples\\Capital.Standard.Reports".

[SeriesNext](/en/docs/mt5/api/reportapi_auxiliary/imtreportchart/imtreportchart_seriesnext)

[IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset)