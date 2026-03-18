# Intelligent management

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/intelligent_management

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
        -   [Launch](/en/docs/mt4/metaeditor/open)
        -   [Settings](/en/docs/mt4/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt4/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt4/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt4/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt4/metaeditor/workspace)
        -   [Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)
        -   [MQL4/MQL5 Wizard](/en/docs/mt4/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt4/metaeditor/development)
            -   [Intelligent management](/en/docs/mt4/metaeditor/intelligent_management)
            -   [Find and replace](/en/docs/mt4/metaeditor/source_code_find)
            -   [Styler](/en/docs/mt4/metaeditor/styler)
            -   [Compilation](/en/docs/mt4/metaeditor/compile)
            -   [MQL5 Cloud Protector: Advanced protection for programs](/en/docs/mt4/metaeditor/mql5_cloud_protector)
            -   [Code debugging](/en/docs/mt4/metaeditor/debug)
            -   [Code profiling](/en/docs/mt4/metaeditor/profiling)
            -   [AI Assistant](/en/docs/mt4/metaeditor/ai_assistant)
            -   [Generating included code](/en/docs/mt4/metaeditor/generate_mqh)
            -   [Working with C++ DLL (integration with MS Visual Studio)](/en/docs/mt4/metaeditor/c_dll)
            -   [Working with Python](/en/docs/mt4/metaeditor/python)
            -   [OpenCL support](/en/docs/mt4/metaeditor/opencl)
        -   [Working with SQL data bases](/en/docs/mt4/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt4/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt4/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt4/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt4/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt4/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt4/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt4/metaeditor/video_guides)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Developing programs](/en/docs/mt4/metaeditor/development)Intelligent management

# Intelligent management

For ease of programming, MetaEditor provides various tools from auto substitutions of names and tips to functions up to bookmarks and [hot keys](/en/docs/mt5/metaeditor/hotkeys). These tools allow you to speed up the process of code writing, make navigation easier and help prevent errors.

This section describes the following functions:

-   [Auto substitution of function names](/en/docs/mt5/metaeditor/intelligent_management#substitute)
-   [Information on parameters](/en/docs/mt5/metaeditor/intelligent_management#info)
-   [Moving to definition](/en/docs/mt5/metaeditor/intelligent_management#definition)
-   [List of functions](/en/docs/mt5/metaeditor/intelligent_management#list)
-   [Inserting comments](/en/docs/mt5/metaeditor/intelligent_management#comments)
-   [Additional code editing features](/en/docs/mt5/metaeditor/intelligent_management#additional)
-   [Working with bookmarks](/en/docs/mt5/metaeditor/intelligent_management#bookmarks)
-   [Go to Line](/en/docs/mt5/metaeditor/intelligent_management#goto_line)
-   [Snippets](/en/docs/mt5/metaeditor/intelligent_management#snippet)
-   [Inserting resources](/en/docs/mt5/metaeditor/intelligent_management#resource)
-   [Text conversion](/en/docs/mt5/metaeditor/intelligent_management#convert)
-   [Clipboard tracking](/en/docs/mt5/metaeditor/intelligent_management#clipboard)

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any changes can be undone by executing <img class="help" alt="Undo" title="Undo" width="13" height="9" src="/en/docs/mt5/metaeditor/img/undo_icon.png"> Undo command in the <a href="/en/docs/mt5/metaeditor/main_menu_edit#undo" class="topiclink">Edit</a> menu or on the <a href="/en/docs/mt5/metaeditor/toolbar_standard#undo" class="topiclink">Standard</a> toolbar, or by pressing Ctrl+Z.</span></p></td></tr></tbody></table>

## Auto substitution of function names [#](intelligent_management#substitute)

When you write the program code, MetaEditor automatically offers possible substitution options for built-in and custom functions, constants, variables, class members, keywords, etc. This speeds up the code writing. For example, as soon as you enter the first letters of the function name, a list of functions with suitable names immediately opens. Select the appropriate option with keyboard arrows and press Enter:

![Name list](/en/docs/mt5/metaeditor/img/list_names.png "Name list")

If an option list is too large, type a few more letters of the function name. To call the list manually, click ![List Names](/en/docs/mt5/metaeditor/img/list_names_icon.png "List Names") List Names in the [Edit](/en/docs/mt5/metaeditor/main_menu_edit#list_names) menu or Ctrl+Space after entering the first characters of the name.

## Information on parameters [#](intelligent_management#info)

You can see the function signature right when writing the code without opening the language help. To do this, place the cursor after the opening parenthesis which starts the description of the function parameters, and then click ![Parameter Info](/en/docs/mt5/metaeditor/img/parameter_info_icon.png "Parameter Info") Parameter Info in the [Edit](/en/docs/mt5/metaeditor/main_menu_edit#parameter_info) menu or Ctrl+Shift+Space. Info on parameters and type of a function return value is displayed in tooltips:

![Information on parameters](/en/docs/mt5/metaeditor/img/parameter_info.png "Information on parameters")

The following info is displayed for the function in the image above:

-   \[1 of 2\] means that the function has call options with different parameters. To switch between them, use the arrows on the keyboard or left-click on the prompt line.
-   bool specifies the value type returned by a function.
-   ObjectSetInteger — function name.
-   (long chart\_id, ... ) — enumeration of possible function parameters, a type is specified before each parameters (here it is long). The parameter the cursor is currently located on is displayed in bold.

## Jump to definition [#](intelligent_management#definition)

This tool enables a quick navigation to the definition (implementation) of the selected class type or element. Place the cursor over its name and select ![Go to Definition](/en/docs/mt5/metaeditor/img/go_to_definition_icon.png "Go to Definition") "Go to Definition" in the context menu or press Alt+G. If the definition is located in another file, it will be opened and the cursor will be placed in its corresponding position.

The function also enables the navigation to include files. To do this, place the cursor anywhere on the line where the include is declared (the #include directive) and execute the above command.

## Jump to declaration [#](intelligent_management#declaration)

This tool enables quick navigation to a variable or class member declaration. Place the cursor over the element name and select "Go to Declaration" in the context menu. If the declaration is located in another file, it will be opened and the cursor will be placed in its corresponding position.

## List of functions [#](intelligent_management#list)

This tool allows you to see a list of all declared functions in the current file. To open the list, click ![List Functions](/en/docs/mt5/metaeditor/img/list_funtions_icon.png "List Functions") List Functions in the [Edit](/en/docs/mt5/metaeditor/main_menu_edit#list_functions) menu or Alt+M.

![List of functions](/en/docs/mt5/metaeditor/img/list_functions.png "List of functions")

The function parameters are indicated in parentheses to the right of its name. To go to the function, click on its name in the list. Each type of functions in the list is marked by its icon:

-   ![Function](/en/docs/mt5/metaeditor/img/function_icon.png "Function") — function.
-   ![Event handling function](/en/docs/mt5/metaeditor/img/function_event_icon.png "Event handling function") — event handling function (On\*).
-   ![Public class method](/en/docs/mt5/metaeditor/img/class_public_method_icon.png "Public class method") — public class method (public).
-   ![Protected class method](/en/docs/mt5/metaeditor/img/class_method_protected_icon.png "Protected class method") — protected class method (protected).
-   ![Private class method](/en/docs/mt5/metaeditor/img/class_method_private_icon.png "Private class method") — private class method (private).

## Inserting comments [#](intelligent_management#comments)

To simplify working with comments in the program code, use a number of functions in the [Edit](/en/docs/mt5/metaeditor/main_menu_edit#comments) menu and [Standard](/en/docs/mt5/metaeditor/toolbar_standard) toolbar:

-   ![Function Header](/en/docs/mt5/metaeditor/img/function_header_icon.png "Function Header") Function Header — insert a comment blank for a function;
-   ![Block Comment](/en/docs/mt5/metaeditor/img/block_comment_icon.png "Block Comment") Block Comment — insert symbols of a single-line comment;
-   ![Comment Lines](/en/docs/mt5/metaeditor/img/comment_lines_icon.png "Comment Lines") Comment Lines — insert "//" comments at the beginning of each selected line;
-   ![Uncomment Lines](/en/docs/mt5/metaeditor/img/uncomment_lines_icon.png "Uncomment Lines") Uncomment Lines — remove "//" comments from the beginning of each selected line.

The ![Block Comment](/en/docs/mt5/metaeditor/img/block_comment_icon.png "Block Comment") Block Comment command (Ctrl+/) inserts single-line comment characters in the current position:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//---</span></p></td></tr></tbody></table>

The ![Function Header](/en/docs/mt5/metaeditor/img/function_header_icon.png "Function Header") Function Header (Ctrl+.) inserts a comment blank for a function in the current cursor position:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #808080;">//|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span></p></td></tr></tbody></table>

## Additional code editing features [#](intelligent_management#additional)

You can easily move code fragments from one part of the program to another. To do this, highlight the fragment and drag it to the necessary position (Drag'n'drop).

The [Advanced](/en/docs/mt5/metaeditor/main_menu_edit#comments) sub-menu of the Edit menu features a series of commands simplifying the source code editing:

-   ![Increase Line Indent](/en/docs/mt5/metaeditor/img/increase_indent_icon.png "Increase Line Indent") Increase Line Indent — insert three spaces (tab symbol) at the beginning of the selected lines. To insert spaces in a single line, position the cursor at its beginning. To insert spaces in several lines, select them in full.
-   ![Decrease Line Indent](/en/docs/mt5/metaeditor/img/decrease_indent_icon.png "Decrease Line Indent") Decrease Line Indent — remove three spaces (tab symbol) at the beginning of the selected lines. A similar action is performed by the Tab+Shift hot key.
-   ![Make Uppercase](/en/docs/mt5/metaeditor/img/make_uppercase_icon.png "Make Uppercase") Make Uppercase — change all characters of a selected phrase to uppercase. A similar action is performed by the Ctrl+Shift+U hot key.
-   ![Make Lowercase](/en/docs/mt5/metaeditor/img/make_lowercase_icon.png "Make Lowercase") Make Lowercase — change all characters of a selected phrase to lowercase. A similar action is performed by the Ctrl+U hot key.

## Working with bookmarks [#](intelligent_management#bookmarks)

Bookmarks allow you to quickly jump to different parts of a code. Mark the required lines with bookmarks and navigate between them using the [Edit — Bookmarks](/en/docs/mt5/metaeditor/main_menu_edit#bookmarks) menu commands and the context menu of a source code:

-   ![Toggle Bookmark](/en/docs/mt5/metaeditor/img/toggle_bookmark_icon.png "Toggle Bookmark") Toggle Bookmark — enable/disable a bookmark on the current line depending on its current status. The same can be done using the Ctrl+F2 hot key;
-   ![Next Bookmark](/en/docs/mt5/metaeditor/img/next_bookmark_icon.png "Next Bookmark") Next Bookmark — move to the next bookmark in the current code. The same can be done by F2 key;
-   ![Previous Bookmark](/en/docs/mt5/metaeditor/img/previous_bookmark_icon.png "Previous Bookmark") Previous Bookmark — move to the previous bookmark in the current code. The same action can be performed by pressing Shift+F2 hot key;
-   ![Clear All Bookmarks](/en/docs/mt5/metaeditor/img/clear_all_bookmarks_icon.png "Clear All Bookmarks") Clear All Bookmarks — remove all bookmarks from the current code. The same can be done by the Ctrl+Shift+F2 hot key.

MetaEditor also features named bookmarks — the ones having a digital ID assigned to them. To set such a bookmark, click 0-9 while holding Ctrl. To go to the previously set tab, press the corresponding number while holding Alt.

## Go to Line [#](intelligent_management#goto_line)

To quickly jump to any line of code in the current file, click ![Go to Line](/en/docs/mt5/metaeditor/img/go_to_line_icon.png "Go to Line") Go to Line in the [Search](/en/docs/mt5/metaeditor/main_menu_search) menu or press Ctrl+G. The following window is opened:

![Go to Line](/en/docs/mt5/metaeditor/img/goto_line.png "Go to Line")

The window displays the range of lines with a code in the current file. To go to the line, enter its number and click OK.

## Snippets [#](intelligent_management#snippet)

Snippets are small template fragments of a source code that describe a certain MQL4/MQL5 language construction. They make it easier and faster to write a source code. For example, they allow you to quickly add a workpiece to a program code to describe a class or a loop. To do this, simply enter a key word — 'class' or 'for'. The cursor changes to ![Snippet can be added](/en/docs/mt5/metaeditor/img/snippet_cursor.png "Snippet can be added") meaning that it is now possible to insert a snippet. Press Tab and a blank for class or 'for' loop is inserted to a program code according.

![Sample snippet](/en/docs/mt5/metaeditor/img/snippet_example.png "Sample snippet")

In order to switch between active snippet fields (here, these are name, class constructor and destructor), use Tab and Shift+Tab.

Changing one active field automatically changes the rest. For example, when changing the class name, constructor and destructor names are changed automatically as well. When changing a variable name in one of the 'for' loop expressions, the variables in its other expressions are changed as well.

The system of working with snippets also recognizes already described structures, classes, enumerations, methods and functions. Place the cursor within the description of the corresponding structure and press Ctrl+Enter. After that, you can navigate between members (classes, structures and enumerations) and arguments (methods and functions) using Tab and Shift+Tab keys and edit them together as described above.

The following snippets are supported at the moment:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Keyword</span></p></th><th class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Value</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">#import</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Import declaration.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnBookEvent</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnBookEvent handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnCalculate</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnCalculate handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">case</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">'case' selector.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnChartEvent</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnChartEvent handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">class</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Class declarations.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnDeinit</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnDeinit handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">do</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Declaration of the 'do while' loop.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">enum</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Declaration of enumeration.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">for</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Declaration of the 'for' loop.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">if</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Declaration of the 'if' condition.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">else</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Declaration of the 'else' condition.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnInit</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnInit handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnStart</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnStart handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">struct</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Structure declaration.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">switch</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">'switch' selector.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnTester</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnTester handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnTesterInit</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnTesterInit handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnTesterPass</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnTesterPass handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnTesterDeinit</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnTesterDeinit handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnTick</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnTick handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnTimer</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnTimer handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnTrade</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnTrade handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">OnTradeTransation</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">OnTradeTransation handler.</span></p></td></tr><tr class="table"><td class="table" style="width:128px;"><p class="p_fortable"><span class="f_fortable">while</span></p></td><td class="table" style="width:685px;"><p class="p_fortable"><span class="f_fortable">Declaration of the 'while' loop.</span></p></td></tr></tbody></table>

## Inserting resources [#](intelligent_management#resource)

Commands from the [Edit — Insert](/en/docs/mt5/metaeditor/main_menu_edit) menu allow to quickly insert resource files and thus can facilitate application development.

### Options as #property

Inserts in the current position the #property directive and immediately opens the list of all [program properties](https://www.mql5.com/en/docs/basis/preprosessor/compilation) available in the language.

### BMP/WAV as #resource

To add an image or a sound file to the program resources, run this command and select a BMP or WAV file (the appropriate file must be located in the\\ MQL5 directory). The #resource directive with the proper path to the selected file will be inserted at the current position of the program.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#resource</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"\\Images\\image.bmp"</span></p></td></tr></tbody></table>

### DLL/EX5 as #import

You can import functions from an external library or an EX5/EX4 file by executing this command and selecting the appropriate file (the file must be located in the\\ MQL5 directory). A pair of #import directives with the proper path to the selected file will be inserted at the current position of the program.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#import</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"..\Experts\SendNotification.ex5"</span><br><span class="f_CodeExample">&nbsp;</span><br><span class="f_CodeExample" style="color: #0000ff;">#import</span></p></td></tr></tbody></table>

Add a description of the imported functions between the directives.

### MQH as #include

To insert an include file to the program code, run this command and select an MQH file (the appropriate file must be located in the \\MQL5 directory). The #include directive with the proper path to the selected file will be inserted at the current position of the program.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#include</span><span class="f_CodeExample">&nbsp;&lt;Arrays\Array.mqh&gt;</span></p></td></tr></tbody></table>

### A set of parameters as #property

To insert to a program code a set of parameters for Expert Advisor testing, run this command and select a SET file (the appropriate file must be stored in the\\ MQL5 directory). The #property directive with the proper path to the selected file will be inserted at the current position of the program.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">#property</span><span class="f_CodeExample">&nbsp;tester_set&nbsp;</span><span class="f_CodeExample" style="color: #008080;">"\\Profiles\\Tester\\Moving&nbsp;Average.set"</span></p></td></tr></tbody></table>

### Data and time as YYYY.MM.DD hh:mm:ss / UNIX time

Use this command to insert the date and time in the required format, into your code. The command selection opens an interactive calendar. Select the date and time in the calendar, and it will be inserted into the current program position in the selected format.

![Inserting date and time into code](/en/docs/mt5/metaeditor/img/insert_datetime.png "Inserting date and time into code")

### Color as clrColor

Use this command to easily insert the color in the required format, into your code. A click on the command opens an interactive palette. Select a color from the palette, and it will be inserted into the current position in the CLRColor format used in MQL5 functions.

![Inserting color into code](/en/docs/mt5/metaeditor/img/insert_color.png "Inserting color into code")

### File as Binary Array

This command allows you to add to the program text any file in the form of a binary array. Run the command and select the desired file (the appropriate file must be located in the\\ MQL5 directory). A char array will be inserted at the current position of the program.

Among others, this function allows you to transfer chart templates with Expert Advisors or indicators: insert your template in the program code as an array, and save it to disk then using the FileSave function. After that the template can be applied on the desired chart using the ChartApplyTemplate function.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #808080;">//|&nbsp;Script&nbsp;program&nbsp;start&nbsp;function&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</span><br><span class="f_CodeExample" style="color: #808080;">//+------------------------------------------------------------------+</span><br><span class="f_CodeExample" style="color: #0000ff;">void</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">OnStart</span><span class="f_CodeExample">()</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample" style="color: #808080;">//---&nbsp;a&nbsp;template&nbsp;file&nbsp;as&nbsp;a&nbsp;binary&nbsp;array</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;unsigned&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">char</span><span class="f_CodeExample">&nbsp;my_template[]=</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0xFF,0xFE,0x3C,&nbsp;...&nbsp;,0x00&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;the&nbsp;data&nbsp;array&nbsp;in&nbsp;this&nbsp;example&nbsp;is&nbsp;shortened</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;};</span><br><span class="f_CodeExample" style="color: #808080;">//---&nbsp;saving&nbsp;and&nbsp;applying&nbsp;the&nbsp;template</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(FileSave(</span><span class="f_CodeExample" style="color: #008080;">my_template.tpl</span><span class="f_CodeExample">,my_template))</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Print</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #008080;">"Custom&nbsp;template&nbsp;saved&nbsp;in&nbsp;\\MQL5\\Files"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">if</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #0000ff;">ChartApplyTemplate</span><span class="f_CodeExample">(0,</span><span class="f_CodeExample" style="color: #008080;">"\\Files\\my_template.tpl"</span><span class="f_CodeExample">))</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Print</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #008080;">"Custom&nbsp;template&nbsp;applied&nbsp;to&nbsp;the&nbsp;current&nbsp;chart"</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Print</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #008080;">Failed&nbsp;to&nbsp;apply&nbsp;custom&nbsp;template</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">else</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #0000ff;">Print</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="color: #008080;">Failed&nbsp;to&nbsp;save&nbsp;custom&nbsp;template</span><span class="f_CodeExample">);</span><br><span class="f_CodeExample">&nbsp;&nbsp;}</span></p></td></tr></tbody></table>

### CSV as a text array

To add data from a text file to the program code, run this command and select a TXT or CSV file (the appropriate file must be located in the\\ MQL5 directory). A string array of the required dimension containing data from the file will be inserted at the current program position:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #0000ff;">string</span><span class="f_CodeExample">&nbsp;data[][3]=</span><br><span class="f_CodeExample">&nbsp;&nbsp;{</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;{</span><span class="f_CodeExample" style="color: #008080;">"name1"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008080;">"value1"</span><span class="f_CodeExample">},</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;{</span><span class="f_CodeExample" style="color: #008080;">"name2"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008080;">"value2"</span><span class="f_CodeExample">},</span><br><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;{</span><span class="f_CodeExample" style="color: #008080;">"name3"</span><span class="f_CodeExample">,</span><span class="f_CodeExample" style="color: #008080;">"value3"</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample">&nbsp;&nbsp;};</span></p></td></tr></tbody></table>

## Text conversion [#](intelligent_management#convert)

The MetaEditor allows you to easily convert the format of source data. Open the desired file, select text in it and execute one of the commands from the [Edit — Convert](/en/docs/mt5/metaeditor/main_menu_edit) menu:

-   ASCII to HEX
-   ASCII to Base64
-   ASCII to Binary Array
-   HEX to ASCII
-   Base64 to ASCII

## Clipboard tracking [#](intelligent_management#clipboard)

The clipboard tracking manager improvements the source code convenience by enabling quick access to the last used data. Press Alt+V anywhere in the source code, select any of the previously copied lines from the menu, and it will be pasted in place.

![To paste lines from the clipboard history, press ALT+V or use the toolbar](/en/docs/mt5/metaeditor/img/clipboard.png "To paste lines from the clipboard history, press ALT+V or use the toolbar")

You can enable/disable tracking by using the corresponding toolbar command or via [editor settings](/en/docs/mt5/metaeditor/settings#common).

[Developing programs](/en/docs/mt4/metaeditor/development)

[Find and replace](/en/docs/mt4/metaeditor/source_code_find)