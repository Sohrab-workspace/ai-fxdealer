# CMTFile::Open

> Source: https://support.metaquotes.net/en/docs/mt5/api/cmtfile/cmtfile_open

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

[MetaTrader 5](/en/docs/mt5)[API](/en/docs/mt5/api)[Tools](/en/docs/mt5/api/reference_tools)[CMTFile](/en/docs/mt5/api/cmtfile)Open

# CMTFile::Open

Open a file.

<table class="help" cellspacing="0" cellpadding="3" border="0" style="border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:3px; border:none"><p class="p_CodeExample"><span class="f_Keywords">bool&nbsp;&nbsp;</span><span class="f_Functions">CMTFile::Open</span><span class="f_CodeExample">(</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">LPCWSTR</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Param">lpFileName</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;File&nbsp;name</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;DWORD</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">dwAccess</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Access&nbsp;flags</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;DWORD</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">dwShare</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Share&nbsp;mode</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;DWORD</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">dwCreationFlags</span><span class="f_CodeExample">,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Types&nbsp;of&nbsp;actions</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_Keywords">const&nbsp;DWORD</span><span class="f_CodeExample">&nbsp;&nbsp;</span><span class="f_Param">dwAttributes=FILE_ATTRIBUTE_NORMAL</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_Comments">//&nbsp;Flags&nbsp;and&nbsp;attributes</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;)</span></p></td></tr></tbody></table>

Parameters

lpFileName

\[in\]  The name of the file to open.

dwAccess

\[in\]  File access flags: GENERIC\_READ (reading), GENERIC\_WRITE (writing) or both flags (GENERIC\_READ| GENERIC\_WRITE).

A more detailed description is available in MSDN - the dwDesiredAccess parameter of the [CreateFile function](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363858%28v=vs.85%29.aspx "MSDN, CreateFile").

dwShare

\[in\]  The sharing mode:

-   0 - prohibits opening of a file when other processes try to delete, read or write the file.
-   FILE\_SHARE\_DELETE - allows further opening of the file to delete it.
-   FILE\_SHARE\_READ - allows further opening of the file to read it.
-   FILE\_SHARE\_WRITE - allows further opening of the file to write it.

A more detailed description is available in MSDN - the dwShareMode parameter of the [CreateFile function](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363858%28v=vs.85%29.aspx "MSDN, CreateFile").

dwCreationFlags

\[in\] Types of action in case the file exists or does not exist:

-   CREATE\_ALWAYS - always create a new file. If the file that you open exists and it is possible to change it, it will be re-created.
-   CREATE\_NEW - create a new file only if the file to open does not exist.
-   OPEN\_ALWAYS - always open the file. If the file does not exist, the function will create it at a specified location if possible.
-   OPEN\_EXISTING - open the file only if it exists.
-   TRUNCATE\_EXISITING - opens a file and truncates it to zero byte size, but only of the file exists.

A more detailed description is available in MSDN - the dwCreationDisposition parameter of the [CreateFile function](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363858%28v=vs.85%29.aspx "MSDN, CreateFile").

dwAttributes=FILE\_ATTRIBUTE\_NORMAL

\[in\]  Flags and attributes of the file to open. Normally, files are opened with the attribute FILE\_ATTRIBUTE\_NORMAL, which means that the file has no special attributes.

The full list of flags and attributes, as well as additional information are available in MSDN - the dwFlagsAndAttributes parameter of the [CreateFile function](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363858%28v=vs.85%29.aspx "MSDN, CreateFile").

Return Value

True if successful, otherwise false.

[CMTFile](/en/docs/mt5/api/cmtfile)

[OpenRead](/en/docs/mt5/api/cmtfile/cmtfile_openread)