# CMTThread::Priority

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtthread/cmtthread_priority

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
            -   [SMTFormat](/en/docs/mt5/api/smtformat)
            -   [SMTMath](/en/docs/mt5/api/smtmath)
            -   [SMTSearch](/en/docs/mt5/api/smtsearch)
            -   [CMTArrayBase](/en/docs/mt5/api/cmtarraybase)
            -   [CMTStr](/en/docs/mt5/api/cmtstr)
            -   [CMTSync](/en/docs/mt5/api/cmtsync)
            -   [CMTThread](/en/docs/mt5/api/cmtthread)
                -   [Start](/en/docs/mt5/api/cmtthread/cmtthread_start)
                -   [Shutdown](/en/docs/mt5/api/cmtthread/cmtthread_shutdown)
                -   [Terminate](/en/docs/mt5/api/cmtthread/cmtthread_terminate)
                -   [IsBusy](/en/docs/mt5/api/cmtthread/cmtthread_isbusy)
                -   [Handle](/en/docs/mt5/api/cmtthread/cmtthread_handle)
                -   [Priority](/en/docs/mt5/api/cmtthread/cmtthread_priority)
            -   [SMTTime](/en/docs/mt5/api/smttime)
            -   [CMTFile](/en/docs/mt5/api/cmtfile)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[CMTThread](/en/docs/mt5/api/cmtthread)Priority

# CMTThread::Priority

Set a thread priority.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">bool&nbsp;&nbsp;</span><span class="f_Functions">CMTThread::Priority</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">int</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">priority</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Priority</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

priority

\[in\]  Thread priority. The following values can be used to specify priority:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">ID</span></p></th><th class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_MODE_BACKGROUND_BEGIN</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">0x00010000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Start processing in the background mode.</span></p></td></tr><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_MODE_BACKGROUND_END</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">0x00020000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Finish processing in the background.</span></p></td></tr><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_PRIORITY_ABOVE_NORMAL</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a priority a point above the priority class of the process.</span></p></td></tr><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_PRIORITY_BELOW_NORMAL</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">-1</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a priority a point lower than the priority class of the process.</span></p></td></tr><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_PRIORITY_HIGHEST</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">2</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a priority two points above the priority class of the process.</span></p></td></tr><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_PRIORITY_IDLE</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">-15</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a base priority equal to 1 to the processes IDLE_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, ABOVE_NORMAL_PRIORITY_CLASS and HIGH_PRIORITY_CLASS or equal to 16 to the REALTIME_PRIORITY_CLASS processes.</span></p></td></tr><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_PRIORITY_LOWEST</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">-2</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a priority two points lower than the priority class of the process.</span></p></td></tr><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_PRIORITY_NORMAL</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">0</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a normal priority for the priority class of the process.</span></p></td></tr><tr class="table"><td class="table" style="width:233px;"><p class="p_fortable"><span class="f_fortable">THREAD_PRIORITY_TIME_CRITICAL</span></p></td><td class="table" style="width:89px;"><p class="p_fortable"><span class="f_fortable">15</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Assign a base priority equal to 15 to the processes IDLE_PRIORITY_CLASS, BELOW_NORMAL_PRIORITY_CLASS, NORMAL_PRIORITY_CLASS, ABOVE_NORMAL_PRIORITY_CLASS and HIGH_PRIORITY_CLASS or equal to 31 to the REALTIME_PRIORITY_CLASS processes.</span></p></td></tr></tbody></table>

A detailed description of priorities is available in [MSDN](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686277%28v=vs.85%29.aspx "Description of priorities in MSDN").

Return Value

If successful, returns true, otherwise returns false.

[Handle](/en/docs/mt5/api/cmtthread/cmtthread_handle)

[SMTTime](/en/docs/mt5/api/smttime)