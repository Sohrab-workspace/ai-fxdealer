# MetaEditor environment folders

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/structure

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
        -   [Launch](/en/docs/mt5/metaeditor/open)
        -   [Settings](/en/docs/mt5/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt5/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt5/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt5/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt5/metaeditor/workspace)
        -   [Projects and MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage)
        -   [MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt5/metaeditor/development)
        -   [Working with SQL data bases](/en/docs/mt5/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt5/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt5/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt5/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt5/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt5/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt5/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt5/metaeditor/video_guides)
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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)MetaEditor environment folders

# MetaEditor environment folders

Before developing trading applications, users need to understand the data storage principles in the trading platform and MetaEditor.

All files for algorithmic trading (ready-made programs) and application development in MetaEditor environment are located in the /MQL5 (/MQL4) directory of the trading platform. To quickly jump to it, click ![Open Data Folder](/en/docs/mt5/metaeditor/img/open_data_folder_icon.png "Open Data Folder") Open Data Folder in the [File](/en/docs/mt5/metaeditor/main_menu_file#data_folder) menu. The directory location relative to the platform installation folder depends on the [MetaEditor launch mode](/en/docs/mt5/metaeditor/open).

Files in the /MQL5 (/MQL4) directory are located depending on their purpose and application type:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Folders and files</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Experts</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder for storing compiled (*.ex5, *.ex4) and source files of EAs (*.mq5, *.mqh, *.mq4).</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Files</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder for storing various files used by EAs and scripts.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Images</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder for storing *.bmp images used in programs.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Include</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder for storing common *.mqh files included in various programs.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Indicators</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder for storing compiled and source files of custom indicators.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Libraries</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder for storing MQL5/MQL4 libraries.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Logs</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Contains Expert Advisor log files (yyyymmdd.log). These files are created separately for each day of the EA operation, their names correspond to their creation date: yyyy </span><span class="f_txt">stands for the</span><span class="f_fortable"> year, mm </span><span class="f_txt">—</span><span class="f_fortable"> month, dd </span><span class="f_txt">—</span><span class="f_fortable"> date.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Presets</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">This folder stores the sets of parameters for launching EAs (Input parameters).</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Scripts</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder for storing compiled and source files of scripts.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">/Shared Projects</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Folder for working with <a href="/en/docs/mt5/metaeditor/projects#shared" class="topiclink">shared projects</a>.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">experts.dat</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Contains the EA database.</span></p></td></tr><tr class="table"><td class="table" style="width:116px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">mql5.storage</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable"><a href="/en/docs/mt5/metaeditor/mql5storage" class="topiclink">MQL5 Storage</a> service data.</span></p></td></tr></tbody></table>

## MQL4/MQL5 application file structure

The files should be arranged carefully when developing MQL4/MQL5 applications. The correct arrangement of files greatly simplifies working with large projects.

If you develop a trading robot, create a separate folder for it in the Experts directory. For indicators — in the Indicators directory, for scripts — in Scripts, etc. Place all files used for an application development in its folder except for common files (standard library, shared include files).

The [Navigator](/en/docs/mt5/metaeditor/navigator) window is used for managing the application structure.

<table class="table" cellspacing="0" cellpadding="0" border="0" style="border:none; border-spacing:0;"><tbody><tr class="table"><td class="table" style="vertical-align:middle; width:227px; padding:0;"><p class="p_table_img"><img class="help" alt="File structure in the Navigator window" title="File structure in the Navigator window" width="227" height="476" src="/en/docs/mt5/metaeditor/img/navigator_structure.png"></p></td><td class="table" style="padding:0;"><p class="p_H2"><span class="f_H2">Creating folders and placing files</span></p><p class="p_txt"><span class="f_txt">To create folders, use an OS explorer or the <a href="/en/docs/mt5/metaeditor/navigator" class="topiclink">Navigator</a> window. To create a sub-directory via the Navigator, select the necessary folder and click "New folder" in the context menu. Next, set the folder name and press Enter. To move a file to the created folder, simply drag it there (Drag'n'Drop).</span></p><p class="p_H2"><span class="f_H2">File arrangement</span></p><p class="p_txt"><span class="f_txt">During a <a href="/en/docs/mt5/metaeditor/compile" class="topiclink">compilation</a>, executable program files (*.EX4 or *.EX5) are created in the same folder as the main source code file of a program (*.MQ4 or *.MQ5) or a <a href="/en/docs/mt5/metaeditor/projects" class="topiclink">project</a> file (MQPROJ).</span></p><p class="p_txt"><span class="f_txt">The main file is an MQ4 or MQ5 file containing so-called entry points </span><span class="f_ol">— predefined functions initializing the application operation (for example: OnInit, OnStart, OnChartEvent, etc.). The main file may include other MQ4, MQ5 and MQH files, although it is the main file that should be compiled to create an executable program file.</span></p><p class="p_txt"><span class="f_txt">Consider the location of files when including them (*.MQH) to your program's code. If an include file is located in the same folder as the main one, use the following statement:</span></p><div><div class="parent-table"><table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#include</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"file_name.mqh"</span></p></td></tr></tbody></table></div></div><p class="p_txt"><span class="f_txt">If the file is located in the standard Include directory:</span></p><div><div class="parent-table"><table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#include</span><span class="f_CodeExample">&nbsp;&lt;file_name.mqh&gt;</span></p></th></tr></thead></table></div></div><p class="p_txt"><span class="f_txt">You can also specify a relative path to the file:</span></p><div><div class="parent-table"><table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#include</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"../folder_name/file_name.mqh"</span></p></th></tr></thead></table></div></div></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">All changes made to the directory and file structure via an OS explorer are automatically displayed in the Navigator window. If for some reason, these changes are not immediately displayed, run the <a href="/en/docs/mt5/metaeditor/navigator#refresh" class="topiclink">Refresh</a> command in the context menu of the Navigator or press F5.</span></li><li class="p_tableatten"><a name="main_file" class="hmanchor"></a><span class="f_tableatten">To create an executable program file, compile its main source file. This is a file containing the entry points — predefined functions initializing the application operation (for example: OnInit, OnStart, OnChartEvent, and so on).</span></li></ul></td></tr></tbody></table>

[Example of developing a program](/en/docs/mt5/metaeditor/project_example)

[MQL5.community: Community of Traders](/en/docs/mt5/metaeditor/mql5community)