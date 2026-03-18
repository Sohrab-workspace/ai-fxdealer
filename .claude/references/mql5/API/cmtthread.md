# CMTThread

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtthread

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)CMTThread

# CMTThread

This class is a wrapper of WinAPI thread. It allows running parallel computing in a separate thread.

The class contains the following methods:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtthread/cmtthread_start" class="topiclink">Start</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Start the thread. After calling this method, the function thread_func starts.</span></p></td></tr><tr class="table"><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtthread/cmtthread_shutdown" class="topiclink">Shutdown</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Wait for the completion of thread operation during the specified time period.</span></p></td></tr><tr class="table"><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtthread/cmtthread_terminate" class="topiclink">Terminate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Forced completion of a thread.</span></p></td></tr><tr class="table"><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtthread/cmtthread_isbusy" class="topiclink">IsBusy</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Check the thread activity.</span></p></td></tr><tr class="table"><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtthread/cmtthread_handle" class="topiclink">Handle</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get a thread handle (WinAPI-descriptor).</span></p></td></tr><tr class="table"><td class="table" style="width:87px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtthread/cmtthread_priority" class="topiclink">Priority</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Set a thread priority.</span></p></td></tr></tbody></table>

[TryLock](/en/docs/mt5/api/cmtsync/cmtsync_trylock)

[Start](/en/docs/mt5/api/cmtthread/cmtthread_start)