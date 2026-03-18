# Intellectual Control

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/development/source_code/intelligent_management

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

# Intellectual Control

Different tools, from the auto substitution of names and tips of functions to bookmarks and hotkeys, are implemented in MetaEditor for the convenient development of programs. These means allow to quicken up the process of the source code writing, conveniently navigate through it and avoid mistakes.

The following functions are described in this section:

-   [Auto Substitution of Function Names](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#substitute)
-   [Information about Parameters](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#info)
-   [Go To Definition](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#definition)
-   [List of Functions](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#list)
-   [Comments Inserting](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#comments)
-   [Additional Functions for Code Editing](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#additional)
-   [Working with Bookmarks](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#bookmarks)
-   [Go To Line](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#goto_line)
-   [Snippets](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#snippet)
-   [Inserting Resources](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#resource)
-   [Text Conversion](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#convert)

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">Any changes made to the source code can be rolled back using the "<img class="help" alt="Undo" title="Undo" width="13" height="9" src="/en/docs/mt5/metaeditor/img/undo_icon.png"> Undo" command in the <a href="/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit#undo" class="topiclink">"Edit"</a> menu, in the <a href="/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#undo" class="topiclink">"Standard"</a> toolbar or using the "Ctrl+Z" key combination.</span></p></td></tr></tbody></table>

## Auto Substitution of Function Names

It is the possibility of viewing the list of variants of names of built in and user functions, constants, variables, members of classes, keywords, etc. The variants of substitution are determined by the first typed symbols. Opening of this list is performed automatically when writing the source code. In order to manually open this list one should use the "![List Names](/en/docs/mt5/metaeditor/img/list_names_icon.png "List Names") List Names" command in the ["Edit"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit#list_names) menu, in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#list_names) toolbar or use the "Ctrl+Space" key combination after the first symbols of the name are typed:

![List of Names](/en/docs/mt5/metaeditor/img/list_names.png "List of Names")

Further it is only left to choose the necessary variant using the "Arrow Up" and "Arrow Down" keys and then press the "Enter" key. The choice can be made using the mouse as well. If one continues to type the letters of the function name, the list of possible variants of substitution will get shorter.

## Information about Parameters

This feature allows viewing parameters of a chosen function and their types. In order to open this information one should execute the "![Parameter Info](/en/docs/mt5/metaeditor/img/parameter_info_icon.png "Parameter Info") Parameter Info" command in the ["Edit"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit#parameter_info) menu, in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#parameter_info) toolbar or use the "Ctrl+Shift+Space" key combination. The commands must be executed when the mouse cursor is within the brackets where the parameters are specified. The pop-up help line containing the parameters will appear below the function as soon as you do it:

![Information about Parameters](/en/docs/mt5/metaeditor/img/parameter_info.png "Information about Parameters")

Let's consider the displayed information in the example shown in the screenshot above:

-   \[1 of 2\] — it means that there are two variants of parameters specification for the function. In order to switch between them one should use the "Arrow Up" and "Arrow Down" keys or click with the left mouse button on the tip line;
-   bool — it indicates the type of the values returned by the function;
-   ObjectSetInteger — the name of the function;
-   (long chart\_id, ... ) — the enumeration of possible parameters of the function, the type of the parameter is specified before each of them ("long" in this case). The parameter where the mouse cursor currently is displayed bold.

## Go To Definition

This function allows to automatically move to the declaration or definition of the selected function or variable. If the definition or declaration is in another file, then this file will be opened and the mouse cursor will be moved to the corresponding position. This function also allows to move to the include files (#include).

In order to go to definition one should place the cursor at a parameter and execute the "![Go To Definition](/en/docs/mt5/metaeditor/img/go_to_definition_icon.png "Go To Definition") Go To Definition" command in the ["Edit"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit#goto) menu, in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#goto) toolbar or use the"Alt+G" key combination. In order to go to an include file one should place the cursor at the line where it is declared and execute one of the commands mentioned above.

## List of Functions

This feature allows to open the list of all declared functions in the current file. In order to open the list one should execute the "![List Functions](/en/docs/mt5/metaeditor/img/list_funtions_icon.png "List Functions") List Functions" command in the ["Edit"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit#list_functions) menu, in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#list_functions) toolbar or use the "Alt+M" key combination.

![List of Functions](/en/docs/mt5/metaeditor/img/list_functions.png "List of Functions")

The parameters that were specified for the functions are shown in brackets. By clicking with the left mouse button or using the "Enter" key one can go to the definition of the selected function in the file. Each type of the function has its own icon in the list:

-   ![Function](/en/docs/mt5/metaeditor/img/function_icon.png "Function") — function;
-   ![Fucntion of Events Handling](/en/docs/mt5/metaeditor/img/function_event_icon.png "Fucntion of Events Handling") — function of events handling (On\*);
-   ![Public Method of Class](/en/docs/mt5/metaeditor/img/class_public_method_icon.png "Public Method of Class") — public method of a class;
-   ![Protected Method of Class](/en/docs/mt5/metaeditor/img/class_method_protected_icon.png "Protected Method of Class") — protected method of a class;
-   ![Private Method of Class](/en/docs/mt5/metaeditor/img/class_method_private_icon.png "Private Method of Class") — private method of a class;

## Comments Inserting

Different commands for working with comments in the source code are implemented in the ["Edit"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit#comments) menu and in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar:

-   ![Function Header](/en/docs/mt5/metaeditor/img/function_header_icon.png "Function Header") Function Header — insert a ready field for a comment to a function;
-   ![Block Comment](/en/docs/mt5/metaeditor/img/block_comment_icon.png "Block Comment") Block Header — insert symbols of a single-line comment;
-   ![Comment Lines](/en/docs/mt5/metaeditor/img/comment_lines_icon.png "Comment Lines") Comment Lines — insert the "//" comments in the beginning of each selected line;
-   ![Uncomment Lines](/en/docs/mt5/metaeditor/img/uncomment_lines_icon.png "Uncomment Lines") Uncomment Lines — remove the "//" comments from the beginning of each selected line.

The execution of the "![Block Comment](/en/docs/mt5/metaeditor/img/block_comment_icon.png "Block Comment") Block Comment" or the usage of the "Ctrl+/" key combination inserts the symbols of a single-line comment at the indicated position:

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; background-color:#ffffff; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//---</span></p></td></tr></tbody></table>

If the "![Function Header](/en/docs/mt5/metaeditor/img/function_header_icon.png "Function Header") Function Header" or the "Ctrl+." key combination is used then the workpiece for a comment to the function will be inserted at the indicated position:

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; background-color:#ffffff; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #808080;">//|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span></p></td></tr></tbody></table>

## Additional Functions for Code Editing

The ["Additional"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit#comments) submenu of the "Edit" menu contains several commands for easier editing a source code:

-   ![Increase Line Indent](/en/docs/mt5/metaeditor/img/increase_indent_icon.png "Increase Line Indent") Increase Line Indent — this command allows inserting three spaces (or a tab character) at the beginning of selected lines. To insert spaces in a single line, put the mouse cursor at the beginning of the line and execute this command (or press the "Tab" hotkey). To insert spaces in several lines, select the whole lines.
-   ![Decrease Line Indent](/en/docs/mt5/metaeditor/img/decrease_indent_icon.png "Decrease Line Indent") Decrease Line Indent — this command allows removing three spaces (or a tab character) from the beginning of selected lines. The same action can be performed using the Tab+Shift key combination.
-   ![Make Uppercase](/en/docs/mt5/metaeditor/img/make_uppercase_icon.png "Make Uppercase") Make Uppercase — this command makes all the letters of a selected phrase uppercase. The same action can be performed using the Ctrl+Shift+U key combination.
-   ![Make Lowercase](/en/docs/mt5/metaeditor/img/make_lowercase_icon.png "Make Lowercase") Make Lowercase — this command makes all the letters of a selected phrase lowercase. The same action can be performed using the Ctrl+U key

## Working with Bookmarks

Bookmarks are intended for denoting necessary lines in the source code for further convenient navigation through them. The commands for working with bookmarks are located in the "Bookmarks" submenu of the ["Edit"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit#bookmarks) menu, in the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard#bookmarks) toolbar and in the context menu of the text. There are the following commands for working with them in MetaEditor:

-   ![Toggle Bookmark](/en/docs/mt5/metaeditor/img/toggle_bookmark_icon.png "Toggle Bookmark") Toggle Bookmark — toggle or untoggle a [bookmark](/en/docs/mt5/metaeditor/development/source_code/intelligent_management#bookmarks) on the current line of the edited file depending on its current state. The same action can be performed using the "Ctrl+F2" key combination;
-   ![Next Bookmark](/en/docs/mt5/metaeditor/img/next_bookmark_icon.png "Next Bookmark") Next Bookmark — move to the next bookmark in the current source code. The same action can be performed using the "F2" key;
-   ![Previous Bookmark](/en/docs/mt5/metaeditor/img/previous_bookmark_icon.png "Previous Bookmark") Previous Bookmark — move to the previous bookmark in the source code. The same action can be performed using the "Shift+F2" key combination;
-   ![Clear All Bookmarks](/en/docs/mt5/metaeditor/img/clear_all_bookmarks_icon.png "Clear All Bookmarks") Clear All Bookmarks — clear all bookmarks from the current file. The same action can be performed using the "Ctrl+Shift+F2" key combination.

MetaEditor includes the feature of working with named bookmarks - bookmarks that have a one-digit identifier assigned. To set such a bookmark press a 0-9 digit key holding the "Ctrl" key. To go to a previously set key, press the corresponding digit key while holding the "Alt" key. Name bookmarks make the navigation through a source code much easier.

## Go To Line

To quickly go to a line in the code of the current file, one can use the "![Go To Line](/en/docs/mt5/metaeditor/img/go_to_line_icon.png "Go To Line") Go To Line" command of the ["Edit"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit) menu or the ["Standard"](/en/docs/mt5/metaeditor/interface/toolbar/toolbar_standard) toolbar. The following window is opened as soon as this button is pressed:

![Go To Line](/en/docs/mt5/metaeditor/img/goto_line.png "Go To Line")

The range of lines containing code in the file is specified in the window. To go to a line, one should indicate its number and press the "OK" button.

## Snippets

To make writing of a code easier, MetaEditor includes a possibility of inserting snippets — small template fragments of code that describes a structure element of the MQL4/MQL5 language. To insert a snippet you should type a special keyword. As soon as you do it, the cursor will change to ![A snippet can be inserted](/en/docs/mt5/metaeditor/img/snippet_cursor.png "A snippet can be inserted"), what means that a snippet can be inserted. The next step is to press the "Tab" key.

For example, to insert a class declaration, type the keyword "class" and press the "Tab" key:

![Example of snippet](/en/docs/mt5/metaeditor/img/snippet_example.png "Example of snippet")

As soon as you do it, the keyword will be replaced with a class declaration. To switch between the active fields of a snippet (in this case? they are the name, constructor and destructor of a class), use the "Tab" and "Shift+Tab" keys.

If you change an active field, the other fields of the snippet will be changed automatically. For example, if you change the class name, the names of the constructor and destructor will be changed automatically; if you change a variable name in one of the expressions of a "for" operator, the names of variables in its other expressions will also be changed.

The system of working with snippets recognizes structures, classes, enumerations, methods and functions if your press the "Ctrl+Enter" key combination. At that the cursor must be within description of the corresponding structural element. As soon as that combination is pressed, the user will be able to move between members (for classes, structures and enumerations) and arguments (for methods and functions) using the "Tab" and "Shift+Tab" keys as well as to edit them together as described above.

At this moment, the following snippets are supported:

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><thead><tr style="text-align:left;vertical-align:top;"><th style="vertical-align:top; width:128px; background-color:#dbe9f9; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Keyword</span></p></th><th style="vertical-align:top; width:685px; background-color:#dbe9f9; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th></tr></thead><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">#import</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of an import.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnBookEvent</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnBookEvent.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnCalculate</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnCalculate.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">case</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">The "case" selector.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnChartEvent</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnChartEvent.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">class</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of a class.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnDeinit</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnDeinit.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">do</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of the "do while" loop.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">enum</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of an enumeration.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">for</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of the "for" loop.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">if</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of the "if" condition.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">else</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of the "else" condition.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnInit</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnInit.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnStart</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnStart.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">struct</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of a structure.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">switch</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">The "switch" selector.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnTester</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnTester.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnTesterInit</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnTesterInit.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnTesterPass</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnTesterPass.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnTesterDeinit</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnTesterDeinit.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnTick</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnTick.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnTimer</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnTimer.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnTrade</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnTrade.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">OnTradeTransation</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Event handler OnTradeTransation.</span></p></td></tr><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; width:128px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">while</span></p></td><td style="vertical-align:top; width:685px; padding:5px; border:solid thin #b1c2d6;"><p class="p_fortable"><span class="f_fortable">Declaration of the "while" loop.</span></p></td></tr></tbody></table>

## Inserting Resources

Commands from the ["Edit—Insert"](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit) menu allow to quickly insert resource files and thus can facilitate application development.

### Options as #property

Inserts in the current position the #property directive and immediately opens the list of all [program properties](https://www.mql5.com/en/docs/basis/preprosessor/compilation) available in the language.

### BMP/WAV as #resource

To add an image or a sound file to the program resources, run this command and select a BMP or WAV file (the appropriate file must be located in the \\MQL5 directory). The #resource directive with the proper path to the selected file will be inserted at the current position of the program.

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#resource</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"\\Images\\image.bmp"</span></p></td></tr></tbody></table>

### DLL/EX5 as #import

You can import functions from an external library or an EX5/EX4 file by executing this command and selecting the appropriate file (the file must be located in the \\MQL5 directory). A pair of #import directives with the proper path to the selected file will be inserted at the current position of the program.

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#import</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"..\Experts\SendNotification.ex5"</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="color: #0000ff;">#import</span></p></td></tr></tbody></table>

Add a description of the imported functions between the directives.

### MQH as #include

To insert an include file to the program code, run this command and select an MQH file (the appropriate file must be located in the \\MQL5 directory). The #include directive with the proper path to the selected file will be inserted at the current position of the program.

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#include</span><span class="f_CodeExample">&nbsp;&lt;Arrays\Array.mqh&gt;</span></p></td></tr></tbody></table>

### A set of parameters as #property

To insert to a program code a set of parameters for Expert Advisor testing, run this command and select a SET file (the appropriate file must be stored in the \\MQL5 directory). The #property directive with the proper path to the selected file will be inserted at the current position of the program.

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#property</span><span class="f_CodeExample">&nbsp;tester_set&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"\\Profiles\\Tester\\Moving&nbsp;Average.set"</span></p></td></tr></tbody></table>

### File as Binary Array

This command allows you to add to the program text any file in the form of a binary array. Run the command and select the desired file (the appropriate file must be located in the \\MQL5 directory). A char array will be inserted at the current position of the program.

Among others, this function allows you to transfer chart templates with Expert Advisors or indicators: insert your template in the program code as an array, and save it to disk then using the FileSave function. After that the template can be applied on the desired chart using the ChartApplyTemplate function.

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #808080;">//|&nbsp;Script&nbsp;program&nbsp;start&nbsp;function&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">OnStart</span><span class="f_CodeExample">()</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample" style="color: #808080;">//---&nbsp;A&nbsp;template&nbsp;file&nbsp;as&nbsp;a&nbsp;binary&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;unsigned&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">char</span><span class="f_CodeExample">&nbsp;my_template[]=</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0xFF,0xFE,0x3C,&nbsp;...&nbsp;,0x00&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;the&nbsp;data&nbsp;array&nbsp;in&nbsp;this&nbsp;example&nbsp;is&nbsp;shortened</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;};</span><br><span class="f_CodeExample" style="color: #808080;">//---&nbsp;Saving&nbsp;and&nbsp;applying&nbsp;the&nbsp;template</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(FileSave(</span><span class="f_CodeExample" style="color: #008080;">"my_template.tpl"</span><span class="f_CodeExample">,my_template))</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Print</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #008080;">"Custom&nbsp;template&nbsp;saved&nbsp;in&nbsp;\\MQL5\\Files"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #0000ff;">ChartApplyTemplate</span><span class="f_CodeExample">(0,</span><span class="f_CodeExample" style="color: #008080;">"\\Files\\my_template.tpl"</span><span class="f_CodeExample">))</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Print</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #008080;">"Custom&nbsp;template&nbsp;applied&nbsp;to&nbsp;the&nbsp;current&nbsp;chart"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Print</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #008080;">"Failed&nbsp;to&nbsp;apply&nbsp;custom&nbsp;template"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Print</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #008080;">"Failed&nbsp;to&nbsp;save&nbsp;custom&nbsp;template"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span></p></td></tr></tbody></table>

### CSV as a text array

To add data from a text file to the program code, run this command and select a TXT or CSV file (the appropriate file must be located in the \\MQL5 directory). A string array of the required dimension containing data from the file will be inserted at the current program position:

<table class="table" cellspacing="0" cellpadding="5" border="1" style="border:solid 2px #b1c2d6; border-spacing:0px; border-collapse:collapse;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:5px; border:solid thin #b1c2d6;"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">string</span><span class="f_CodeExample">&nbsp;data[][3]=</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;{</span><span class="f_CodeExample" style="color: #008080;">"name1"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008080;">"value1"</span><span class="f_CodeExample">},</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;{</span><span class="f_CodeExample" style="color: #008080;">"name2"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008080;">"value2"</span><span class="f_CodeExample">},</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;{</span><span class="f_CodeExample" style="color: #008080;">"name3"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008080;">"value3"</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample">&nbsp;&nbsp;};</span></p></td></tr></tbody></table>

## Text Conversion

The MetaEditor allows you to easily convert the format of source data. Open the desired file, select text in it and execute one of the commands from the [Edit—Convert](/en/docs/mt5/metaeditor/interface/main_menu/main_menu_edit) menu:

-   ASCII to HEX
-   ASCII to Base64
-   ASCII to Binary Array
-   HEX to ASCII
-   Base64 to ASCII