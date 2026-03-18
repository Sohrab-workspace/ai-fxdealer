# Common Functions

> Source: https://support.metaquotes.net/en/docs/mt4/api/manager_api/manager_api_common

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
            -   [Application Development](/en/docs/mt4/api/manager_api/manager_api_dev)
            -   [Exported Functions and Factory](/en/docs/mt4/api/manager_api/manager_api_exported_factory)
            -   [Common Functions](/en/docs/mt4/api/manager_api/manager_api_common)
                -   [QueryInterface](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_queryinterface)
                -   [AddRef](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_addref)
                -   [Release](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_release)
                -   [MemFree](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_memfree)
                -   [ErrorDescription](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_errordescription)
                -   [WorkingDirectory](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_workingdirectory)
                -   [PumpingSwitch](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_pumpingswitch)
                -   [PumpingSwitchEx](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_pumpingswitchex)
                -   [BytesSent](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_bytessent)
                -   [BytesReceived](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_bytesreceived)
                -   [LogsOut](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_logsout)
                -   [LogsMode](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_logsmode)
                -   [LicenseCheck](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_licensecheck)
            -   [Connecting to the Server](/en/docs/mt4/api/manager_api/manager_api_connect)
            -   [Configuration Databases](/en/docs/mt4/api/manager_api/manager_api_config)
            -   [Server Management](/en/docs/mt4/api/manager_api/manager_api_server)
            -   [Price Data](/en/docs/mt4/api/manager_api/manager_api_chart)
            -   [Data Feeds](/en/docs/mt4/api/manager_api/manager_api_feeder)
            -   [Backup](/en/docs/mt4/api/manager_api/manager_api_backup)
            -   [Trading](/en/docs/mt4/api/manager_api/manager_api_trade)
            -   [Dealings](/en/docs/mt4/api/manager_api/manager_api_dealer)
            -   [Users](/en/docs/mt4/api/manager_api/manager_api_user)
            -   [Online Connections](/en/docs/mt4/api/manager_api/manager_api_online)
            -   [Symbols](/en/docs/mt4/api/manager_api/manager_api_symbol)
            -   [Mail, News and Notifications](/en/docs/mt4/api/manager_api/manager_api_newsmail)
            -   [Reports](/en/docs/mt4/api/manager_api/manager_api_report)
            -   [Summary Positions](/en/docs/mt4/api/manager_api/manager_api_summary)
            -   [Exposure](/en/docs/mt4/api/manager_api/manager_api_exposure)
            -   [Protocol Extension](/en/docs/mt4/api/manager_api/manager_api_extension)
        -   [DataFeed API](/en/docs/mt4/api/datafeed_api)
        -   [Report API](/en/docs/mt4/api/report_api)
        -   [WebServices API](/en/docs/mt4/api/webservices_api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[API](/en/docs/mt4/api)[Manager API](/en/docs/mt4/api/manager_api)Common Functions

# Common Functions

Manager API provides various service functions that allow managing the operation of the application.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Function</span></p></th><th class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_queryinterface" class="topiclink">QueryInterface</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Returns a pointer to the interfaces of the Manager API object.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_addref" class="topiclink">AddRef</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Increases the counter of references to the Manager API object interface by one.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_release" class="topiclink">Release</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Deletes a previously created Manager interface.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_memfree" class="topiclink">MemFree</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Releases the specified memory block.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_errordescription" class="topiclink">ErrorDescription</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Returns a text description for the passed error code.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_workingdirectory" class="topiclink">WorkingDirectory</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Sets the working directory of the Manager API application.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_pumpingswitch" class="topiclink">PumpingSwitch</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Switching the Manager interface to the <a href="/en/docs/mt4/api/manager_api/manager_api_dev#pumping" class="topiclink">pumping mode</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_pumpingswitchex" class="topiclink">PumpingSwitchEx</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Switching the Manager interface to the <a href="/en/docs/mt4/api/manager_api/manager_api_dev#pumping_ext" class="topiclink">extended pumping</a> mode.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_bytessent" class="topiclink">BytesSent</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Gets the number of bytes sent over the network during the current operation session of the Manager API application.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_bytesreceived" class="topiclink">BytesReceived</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Gets the number of bytes received over the network during the current operation session of the Manager API application.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_logsout" class="topiclink">LogsOut</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">The functions for logging messages.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_logsmode" class="topiclink">LogsMode</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">Selects Manager API log operation mode.</span></p></td></tr><tr class="table"><td class="table" style="width:114px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_licensecheck" class="topiclink">LicenseCheck</a></span></p></td><td class="table" style="width:571px;"><p class="p_fortable"><span class="f_fortable">The function checks the application license.</span></p></td></tr></tbody></table>

[Create](/en/docs/mt4/api/manager_api/manager_api_exported_factory/manager_api_cmanagerfactory/manager_api_cmanagerfactory_create)

[QueryInterface](/en/docs/mt4/api/manager_api/manager_api_common/cmanagerinterface_queryinterface)