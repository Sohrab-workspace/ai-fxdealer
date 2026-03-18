# Dataset

> Source: https://support.metaquotes.net/en/docs/mt5/api/imtserverapi/serverapi_dataset

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
            -   [Purpose of the Server API](/en/docs/mt5/api/serverapi_purpose)
            -   [Interaction with Servers](/en/docs/mt5/api/serverapi_interaction)
            -   [Configuration of Plugins](/en/docs/mt5/api/serverapi_configure_plugin)
            -   [Requirements for Plugins](/en/docs/mt5/api/serverapi_requirements)
            -   [Creating a Simple Plugin](/en/docs/mt5/api/serverapi_simpleplugin)
            -   [Hooks](/en/docs/mt5/api/serverapi_hooks)
            -   [Request Processing on the Server](/en/docs/mt5/api/hook_scheme)
            -   [Recommendations for Developers](/en/docs/mt5/api/serverapi_best_practice)
            -   [Debugging](/en/docs/mt5/api/serverapi_debug)
            -   [Ready-made Examples](/en/docs/mt5/api/serverapi_examples)
            -   [Entry Points](/en/docs/mt5/api/reference_entrypoints)
            -   [Plugin Interface](/en/docs/mt5/api/imtserverplugin)
            -   [Main API Interface](/en/docs/mt5/api/imtserverapi)
                -   [Common Functions](/en/docs/mt5/api/imtserverapi/serverapi_common)
                -   [Configuration Databases](/en/docs/mt5/api/imtserverapi/serverapi_configuration)
                -   [Clients](/en/docs/mt5/api/imtserverapi/serverapi_clients)
                -   [Users](/en/docs/mt5/api/imtserverapi/serverapi_users)
                -   [Online Connections](/en/docs/mt5/api/imtserverapi/serverapi_online)
                -   [Certificates](/en/docs/mt5/api/imtserverapi/serverapi_certificate)
                -   [Trade](/en/docs/mt5/api/imtserverapi/serverapi_trading)
                -   [History Data](/en/docs/mt5/api/imtserverapi/serverapi_chart)
                -   [Tick Data](/en/docs/mt5/api/imtserverapi/serverapi_ticks)
                -   [Depth of Market](/en/docs/mt5/api/imtserverapi/serverapi_book)
                -   [Mail Database](/en/docs/mt5/api/imtserverapi/serverapi_mail)
                -   [News Database](/en/docs/mt5/api/imtserverapi/serverapi_news)
                -   [Daily Reports](/en/docs/mt5/api/imtserverapi/serverapi_trading_daily)
                -   [Subscriptions](/en/docs/mt5/api/imtserverapi/serverapi_subscription)
                -   [Server Services](/en/docs/mt5/api/imtserverapi/serverapi_server_services)
                -   [Geo Services](/en/docs/mt5/api/imtserverapi/serverapi_geo)
                -   [Dataset](/en/docs/mt5/api/imtserverapi/serverapi_dataset)
                    -   [DatasetCreate](/en/docs/mt5/api/imtserverapi/serverapi_dataset/imtserverapi_datasetcreate)
                    -   [DatasetRequestCreate](/en/docs/mt5/api/imtserverapi/serverapi_dataset/imtserverapi_datasetrequestcreate)
                -   [Custom Functions](/en/docs/mt5/api/imtserverapi/serverapi_custom)
            -   [Interface of Server Events](/en/docs/mt5/api/imtserversink)
            -   [Interface of Custom Events](/en/docs/mt5/api/imtcustomsink)
            -   [Interface of Trade Events](/en/docs/mt5/api/imttradesink)
            -   [Interface of End-of-Day Events](/en/docs/mt5/api/imtendofdaysink)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Server API](/en/docs/mt5/api/serverapi)[Main API Interface](/en/docs/mt5/api/imtserverapi)Dataset

# Dataset

The Server API enables highly efficient queries to the trading platform databases, with the flexible description of selection conditions (similar to SQL queries). The following two interfaces are provided for working with requests: [IMTDatasetField](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield) is used for describing conditions; [IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest) is used for describing a request as a set of conditions.

To request data perform the following steps:

1.  Use the [IMTServerAPI::DatasetRequestCreate](/en/docs/mt5/api/imtserverapi/serverapi_dataset/imtserverapi_datasetrequestcreate) method to create a data request object ([IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest)).
2.  Use the [IMTServerAPI::DatasetCreate](/en/docs/mt5/api/imtserverapi/serverapi_dataset/imtserverapi_datasetcreate) method to create a dataset object to which the request results will be placed ([IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset))
3.  Use the [IMTDatasetRequest::FieldCreate](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest/imtdatasetrequest_fieldcreate) method to create the object of the field for which you wish to request data ([IMTDatasetField](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield)).
4.  Describe a request condition using [IMTDatasetField](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield) methods and add it to the request object using the [IMTDatasetRequest::FieldAdd](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest/imtdatasetrequest_fieldadd) method.
5.  If you need to specify multiple conditions, repeat steps 3 and 4.
6.  Depending on the database from which you wish to query data, call [IMTServerAPI::OrderSelect\*](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_orderselectbygroup), [IMTServerAPI::HistorySelect\*](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_order/imtserverapi_historyselectbygroup), [IMTServerAPI::DealSelect\*](/en/docs/mt5/api/imtserverapi/serverapi_trading/serverapi_trading_deal/imtserverapi_dealselectbygroup) or [IMTServerAPI::DailySelect\*](/en/docs/mt5/api/imtserverapi/serverapi_trading_daily/imtserverapi_dailyselectbygroup), by passing the prepared request object to it ([IMTDatasetRequest](/en/docs/mt5/api/reportapi_dataset/imtdatasetrequest)).
7.  The request result will be added to the earlier created dataset object ([IMTDataset](/en/docs/mt5/api/reportapi_dataset/imtdataset)). Note that only fields marked as selected ([IMTDatasetField::FLAG\_SELECT](/en/docs/mt5/api/reportapi_dataset/imtdatasetfield/imtdatasetfield_enum#enfieldflags)) are added to the resulting dataset.

The following methods are provided for operations with datasets in Server API:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:745px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtserverapi/serverapi_dataset/imtserverapi_datasetcreate" class="topiclink">DatasetCreate</a></span></p></td><td class="table" style="width:745px;"><p class="p_fortable"><span class="f_fortable">Create a dataset object.</span></p></td></tr><tr class="table"><td class="table" style="width:80px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/imtreportapi/imtreportapi_dataset/imtreportapi_datasetrequestcreate" class="topiclink">DatasetRequestCreate</a></span></p></td><td class="table" style="width:745px;"><p class="p_fortable"><span class="f_fortable">Create a data request object.</span></p></td></tr></tbody></table>

[GeoResolveIPv6Bulk](/en/docs/mt5/api/imtserverapi/serverapi_geo/imtserverapi_georesolveipv6bulk)

[DatasetCreate](/en/docs/mt5/api/imtserverapi/serverapi_dataset/imtserverapi_datasetcreate)