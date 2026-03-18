# CMTFile::Read

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtfile/cmtfile_read

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[CMTFile](/en/docs/mt5/api/cmtfile)Read

# CMTFile::Read

Reading from a currently open file.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">DWORD&nbsp;&nbsp;</span><span class="f_Functions">CMTFile::Read</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">void</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">*buffer</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Buffer&nbsp;for&nbsp;data</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;DWORD</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">length</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Data&nbsp;length</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

\*buffer

\[in\]  A pointer to the buffer, in which the read data will be placed.

length

\[in\]  The amount of data that you want to read. Data are read from the current position.

Return Value

Amount of data read in bytes.

[CurrPos](/en/docs/mt5/api/cmtfile/cmtfile_currpos)

[Write](/en/docs/mt5/api/cmtfile/cmtfile_write)