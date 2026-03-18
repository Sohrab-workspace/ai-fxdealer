# Structure of Application Files

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/development/development_projects

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
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

# Structure of Application Files

The files should be arranged carefully when developing MQL4/MQL5 applications. It is recommended to place files related to a particular application into a separate directory. The subfolders that are created in the folders of Expert Advisors, indicators, etc. will be further recognized by the ["Navigator"](/en/docs/mt5/metaeditor/interface/navigator) windows of the MetaEditor and the client terminal.

<table class="table" cellspacing="0" cellpadding="0" border="0" style="border:none; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:middle; width:227px; background-color:#ffffff; padding:0px;"><p class="p_table_img"><img class="help" alt="Projects" title="Projects" width="227" height="498" src="/en/docs/mt5/metaeditor/img/projects.png"></p><p class="p_fortable"><span class="f_fortable" style="font-size: 8pt;">All files that refer to the "Tetris" project are stored in a separate folder.</span></p></td><td style="vertical-align:top; background-color:#ffffff; padding:0px;"><p class="p_H2"><span class="f_H2">Creation of Folders and Placement of Files</span></p><p class="p_H2"><span class="f_txt">Subfolders can be created both by using the standard functions of the operating system explorer or through the <a href="/en/docs/mt5/metaeditor/interface/navigator" class="topiclink">"Navigator"</a> window. In order to create a subfolder one should choose the catalog in which it is necessary to &nbsp;create a subfolder, and execute the "New Folder" command in the <a href="/en/docs/mt5/metaeditor/interface/navigator#context_menu" class="topiclink">context menu</a> or press the "Insert" key. After that it is necessary to specify the name of the folder and press the "Enter" key or click with the mouse anywhere outside the name field.</span></p><p class="p_H2"><span class="f_txt">Once the subfolder is created different files can be moved to it. This action can also be done both via the explorer and via the navigator. All you need is to select a necessary file and move it to the end folder using the Drag'n'Drop technology.</span></p><p class="p_H2"><span class="f_H2">Peculiarities of Files Placement</span></p><p class="p_H2"><span class="f_txt">Each executable file (*.EX4 or *.EX5) that is obtained as a result of <a href="/en/docs/mt5/metaeditor/development/compile" class="topiclink">compilation</a> is placed to the same folder where the <a href="/en/docs/mt5/metaeditor/development/development_projects#main_file" class="topiclink">main file</a> of the source code of the program (*.MQ4 or *.MQ5) is located.</span></p><p class="p_H2"><span class="f_txt">If different files (*.MQH) are included to the code of a program it is necessary to consider their location. If an included file is located in the same folder as the main one then the following construction must be used:</span></p><div><div class="parent-table"><table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; background-color:#ffffff; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#include</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"file_name.mqh"</span></p></td></tr></tbody></table></div></div><p class="p_H2"><span class="f_txt">If it is necessary to search the include file in the directory where the permanent files of the terminal (executable file, libraries, etc.) are stored, the construction must be the following:</span></p><div><div class="parent-table"><table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><thead><tr style="text-align:left;vertical-align:top;"><th style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#include</span><span class="f_CodeExample">&nbsp;&lt;file_name.mqh&gt;</span></p></th></tr></thead></table></div></div><p class="p_H2"><span class="f_txt">Also there is a possibility to specify a relative path to the file:</span></p><div><div class="parent-table"><table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><thead><tr style="text-align:left;vertical-align:top;"><th style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#include</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"../folder_name/file_name.mqh"</span></p></th></tr></thead></table></div></div></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">All the changes made to the structure of files and folders using the explorer of the operating system are automatically displayed in the "Navigator" window. If the changes are not displayed immediately for some reasons, one can execute the <a href="/en/docs/mt5/metaeditor/interface/navigator#refresh" class="topiclink">"Refresh"</a> command in the context menu of the navigator or press the "F5" key.</span></p></td></tr></tbody></table>

## Main File of an Application

The main file of an application is the MQ4 or MQ5 file that contains the so-called entry points, the set of predefined functions that initialize the working of application (for example, OnInit(), OnStart(), OnChartEvent(), etc.). Other MQ4, MQ5 and MQH files can also be included in the main file. In order to obtain an executable file (\*.EX4 or \*.EX5) one should [compile](/en/docs/mt5/metaeditor/development/compile) the main MQ4 or MQ5 file exactly.