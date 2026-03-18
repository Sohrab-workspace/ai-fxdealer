# CMTFile

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtfile

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
            -   [SMTTime](/en/docs/mt5/api/smttime)
            -   [CMTFile](/en/docs/mt5/api/cmtfile)
                -   [Open](/en/docs/mt5/api/cmtfile/cmtfile_open)
                -   [OpenRead](/en/docs/mt5/api/cmtfile/cmtfile_openread)
                -   [OpenWrite](/en/docs/mt5/api/cmtfile/cmtfile_openwrite)
                -   [Close](/en/docs/mt5/api/cmtfile/cmtfile_close)
                -   [Handle](/en/docs/mt5/api/cmtfile/cmtfile_handle)
                -   [IsOpen](/en/docs/mt5/api/cmtfile/cmtfile_isopen)
                -   [Size](/en/docs/mt5/api/cmtfile/cmtfile_size)
                -   [TimeCreate](/en/docs/mt5/api/cmtfile/cmtfile_timecreate)
                -   [TimeLastAccess](/en/docs/mt5/api/cmtfile/cmtfile_timelastaccess)
                -   [TimeLastModify](/en/docs/mt5/api/cmtfile/cmtfile_timelastmodify)
                -   [CurrPos](/en/docs/mt5/api/cmtfile/cmtfile_currpos)
                -   [Read](/en/docs/mt5/api/cmtfile/cmtfile_read)
                -   [Write](/en/docs/mt5/api/cmtfile/cmtfile_write)
                -   [Seek](/en/docs/mt5/api/cmtfile/cmtfile_seek)
                -   [ChangeSize](/en/docs/mt5/api/cmtfile/cmtfile_changesize)
                -   [Flush](/en/docs/mt5/api/cmtfile/cmtfile_flush)
                -   [FilesCopy](/en/docs/mt5/api/cmtfile/cmtfile_filescopy)
                -   [DirectoryCreate](/en/docs/mt5/api/cmtfile/cmtfile_directorycreate)
                -   [DirectoryRemove](/en/docs/mt5/api/cmtfile/cmtfile_directoryremove)
                -   [DirectoryClean](/en/docs/mt5/api/cmtfile/cmtfile_directoryclean)
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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)CMTFile

# CMTFile

This class contains additional functions for working with files.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Method</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Purpose</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_open" class="topiclink">Open</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Open a file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_openread" class="topiclink">OpenRead</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Open the specified file for reading.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_openwrite" class="topiclink">OpenWrite</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Open the specified file for writing.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_close" class="topiclink">Close</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Close the previously opened file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_handle" class="topiclink">Handle</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the handle (Windows descriptor) of a file, with which you can work using the appropriate WinAPI methods.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_isopen" class="topiclink">IsOpen</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Check whether there is an open file (file handle).</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_size" class="topiclink">Size</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the file size.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_timecreate" class="topiclink">TimeCreate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the creation time of the currently open file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_timelastaccess" class="topiclink">TimeLastAccess</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the time of the last access to the currently open file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_timelastmodify" class="topiclink">TimeLastModify</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the time of the last modification of the currently open file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_currpos" class="topiclink">CurrPos</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Get the current position in the open file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_read" class="topiclink">Read</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Reading from a currently open file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_write" class="topiclink">Write</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Write to the currently open file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_seek" class="topiclink">Seek</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Move the pointer of the current position in a file.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_changesize" class="topiclink">ChangeSize</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Change the size of the current file to the specified size.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_flush" class="topiclink">Flush</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Forced writing of data from the file cache to disk.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_filescopy" class="topiclink">FilesCopy</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Copy files from one directory to another</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_directorycreate" class="topiclink">DirectoryCreate</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Create a directory.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_directoryremove" class="topiclink">DirectoryRemove</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Remove a directory and all its contents.</span></p></td></tr><tr class="table"><td class="table" style="width:119px;"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/api/cmtfile/cmtfile_directoryclean" class="topiclink">DirectoryClean</a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delete files from a specified directory based on the file mask.</span></p></td></tr></tbody></table>

## Constants [#](cmtfile#constants)

The following constants are used in the class:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:118px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Constant</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:118px;"><p class="p_fortable"><span class="f_FunctionRemark">INVALID_POSITION</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">_UI64_MAX</span></p></td></tr></tbody></table>

[Sec](/en/docs/mt5/api/smttime/smttime_sec)

[Open](/en/docs/mt5/api/cmtfile/cmtfile_open)