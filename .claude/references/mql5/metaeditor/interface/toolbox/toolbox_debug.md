# Debug

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/interface/toolbox/toolbox_debug

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

# Debug

The "Debug" tab is only displayed when this [process](/en/docs/mt5/metaeditor/development/debug) is running. The window is separated into two parts. The left part displays the [call stack](/en/docs/mt5/metaeditor/development/debug#stack) and the right one displays the [values of observed expressions](/en/docs/mt5/metaeditor/development/debug#watch):

![Debug](/en/docs/mt5/metaeditor/img/toolbox_debug.png "Debug")

## Call Stack

The call stack is displayed in the form of a table with the following fields:

-   File — the name and the path to the file the function was called from;
-   Function — the name of the function where the current stage of the program execution is performed;
-   Line — the number of line where the execution of program was stopped.

If no breakpoints are toggled and none of the commands of the [step-by-step debugging](/en/docs/mt5/metaeditor/development/debug#step) are executed, the left part of the window will be displayed empty. Using context menu commands one can show/hide the grid that separates fields and enable/disable automatic arrangement of columns.

## Watching Expressions

The right part of the "Debug" window is intended for [watching values of expressions](/en/docs/mt5/metaeditor/development/debug#watch) during the debugging process. The information is shown in the following fields:

-   Expression — the name of the watched expression;
-   Value — the value of the watched expression;
-   Type — the type of the expression.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:middle; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">If the value of an expression is not defined or not calculated at the moment, the "Unknown identifier" entry will be displayed in the corresponding field. Such expressions are marked by the <img class="help" alt="Unknown identifier" title="Unknown identifier" width="16" height="16" src="/en/docs/mt5/metaeditor/img/unknown_identifier_icon.png"> icon.</span></p></td></tr></tbody></table>

In order to add an expression to view in this window one should press the "![Add Watch](/en/docs/mt5/metaeditor/img/add_watch_icon.png "Add Watch") Add Watch" button in the [context menu](/en/docs/mt5/metaeditor/interface/source_code_windows#add_watch) of the window of working with the source code.

### Context Menu

The context menu of the right part of the window allows executing a number of commands:

-   Edit — edit the name of the watched expression. The same action can be performed by pressing "F2" key or by a double click on the name field of the expression;
-   ![Add](/en/docs/mt5/metaeditor/img/add_watch_icon.png "Add") Add — add an expression. The new line will appear in the table as soon as you press this button. In the "Expression" field one should enter the name of the watched expression. One can add an expression by pressing the "Insert" key as well;
-   ![Delete](/en/docs/mt5/metaeditor/img/delete_icon.png "Delete") Delete — delete the selected expression. The same action can be performed by pressing the "Delete" key;
-   ![Copy Value](/en/docs/mt5/metaeditor/img/copy_icon.png "Copy Value") Copy Value — copy the value of the expression to the clipboard;
-   Grid — show/hide grid to separate fields. The same action can be performed by pressing the "G" key;
-   Auto Arrange — enable/disable the automatic arrangement of the column size. The same action can be performed by pressing the "A" key.