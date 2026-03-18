# MetaEditor settings

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/settings

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)Settings

# MetaEditor settings

MetaEditor provides multiple settings to help you conveniently customize your work in the development environment. To open the settings, click ![Options...](/en/docs/mt5/metaeditor/img/options_icon.png "Options...") Options... in the [Tools](/en/docs/mt5/metaeditor/main_menu_tools#settings) menu (Ctrl+O).

![MetaEditor settings](/en/docs/mt5/metaeditor/img/settings.png "MetaEditor settings")

All settings are grouped in several tabs based on what they do:

-   [General](/en/docs/mt5/metaeditor/settings#common) — general code editing settings: tab size, auto completion, auto list of names, etc.
-   [Colors](/en/docs/mt5/metaeditor/settings#color) — colors for highlighting MQL4/MQL5 language syntax.
-   [Font](/en/docs/mt5/metaeditor/settings#font) — settings of a text entered in MetaEditor.
-   [Styler](/en/docs/mt5/metaeditor/settings#styler) — settings for the automatic source code styling.
-   [Compiler](/en/docs/mt5/metaeditor/settings#compiler) — settings of external compiling for multilingual projects.
-   [AI Assistant](/en/docs/mt5/metaeditor/settings#ai_assistant) — AI coding assistant integration settings.
-   [Debug](/en/docs/mt5/metaeditor/settings#debug) — program [debugging](/en/docs/mt5/metaeditor/debug) settings.
-   [MQL5.community](/en/docs/mt5/metaeditor/settings#mql5community) — configuring connection to MQL5.community for accessing unique services, including [MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage).

## General [#](settings#common)

This tab features general code editing settings: tab size, auto completion, auto list of names, etc.

![General](/en/docs/mt5/metaeditor/img/settings_general.png "General")

The window contains the following parameters:

-   Tabulation — number of characters inserted when pressing Tab.
-   Insert spaces — enable/disable replacing tab characters with spaces.
-   String indices — enable/disable line numbering in the code editing window.
-   Auto indent — enable/disable auto indent when moving to the next line according to the indent of the previous one.
-   Auto parameters — enable/disable automatic opening of the [function signature](/en/docs/mt5/metaeditor/intelligent_management#info) hint when you enter it.
-   Auto list names — enable/disable auto opening of a scrollable [list of names](/en/docs/mt5/metaeditor/intelligent_management#substitute) of built-in and custom functions when entering the first characters of their names.
-   List names after "n" characters — set the number of characters followed by the auto list of names.
-   Insert () and closing } \] ) ' " — automatic insertion of parentheses after functions and closing parentheses and quotation marks when entering opening ones.
-   Highlight current line — when enabled, the current code line in the editing window is highlighted in gray.
-   Highlight matching brackets — when enabled, the background of matching parentheses is highlighted when the mouse cursor is placed between them.
-   Enable clipboard history — [clipboard history](/en/docs/mt5/metaeditor/intelligent_management#clipboard) enables faster work with the source code. You can disable this feature if you do not need it.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">It is recommended not to disable the "Insert spaces" option to save the code formatting when transferring to other editors.</span></p></td></tr></tbody></table>

## Colors [#](settings#color)

The Colors tab configures highlighting MQL4/MQL5 language syntax when working with a source code.

![Colors](/en/docs/mt5/metaeditor/img/settings_colors.png "Colors")

The Elements block allows you to select MQL4/MQL5 language syntax elements, while the right part manages their display: Foreground, Background. The block below the settings shows an example of how this element will be displayed in the code editing window. Click Reset All to reset the syntax highlighting settings to default values.

Using the options, you can select color scheme presets for the code editing window: light (default), dark and blue. You can customize the editor for a comfortable work at night, without having to configure the editor view manually. Simply choose a dark color scheme for such cases.

## Font [#](settings#font)

This tab configures the font type and size for displaying code in the editing window.

![Font](/en/docs/mt5/metaeditor/img/settings_font.png "Font")

The following setting blocks are available here:

-   Font — font type selected from the list of available ones.
-   Size — font size. The size can be selected from the list or entered manually. It is also possible to change the font size in the [code editing window](/en/docs/mt5/metaeditor/source_code_windows). This can be done by holding down Ctrl and scrolling the mouse wheel.
-   Script — font encoding selected from the list of available ones.
-   Preview window — here we can see the final text appearance after applying the settings.
-   Bold — enable/disable display of an element in bold.

## Styler [#](settings#styler)

[The styler](/en/docs/mt5/metaeditor/styler) quickly brings a source code design in line with the recommended standard. This makes the code look professional and easy to read.

![Styler Settings](/en/docs/mt5/metaeditor/img/settings_styler.png "Styler Settings")

In this section you can specify settings for the styler:

-   Style — the style that will be used to format the code. Multiple variants are available, including the recommended MetaQuotes style, Linux, Java, GNU and other styles.
-   Spaces per indentation — the number of spaces to be inserted at the beginning of a new line to align nested constructions.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(condition)</span><br><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;body</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

-   Convert tabs to spaces — if this option is enabled, the styler will replace each tab character with one space.
-   Delete empty lines — the styler can remove all lines having only space characters, tabs or line breaks.
-   Insert spaces after commas and semicolons — when this option is enabled, the styler will visually separate constructions with element enumerations:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//&nbsp;before&nbsp;styler</span><br><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">for</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">i=</span><span class="f_CodeExample" style="color: #008000;">0</span><span class="f_CodeExample">;i&lt;total;i++)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;body</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #808080;">//&nbsp;after&nbsp;styler</span><br><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">for</span><span class="f_CodeExample">(</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">i=</span><span class="f_CodeExample" style="color: #008000;">0</span><span class="f_CodeExample">;</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample">i&lt;total;</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample">i++)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample" style="color: #808080;">//&nbsp;body</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

-   Insert spaces around statement operators — when this option is enabled, the styler will insert spaces around the assignment, equality, comparison, and other operators. For example:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample" style="color: #808080;">//&nbsp;before&nbsp;styler</span><br><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(x==</span><span class="f_CodeExample" style="color: #008000;">1</span><span class="f_CodeExample">&amp;y!=</span><span class="f_CodeExample" style="color: #008000;">2</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">a=</span><span class="f_CodeExample" style="color: #008000;">0</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample">}</span><br><span class="f_CodeExample" style="color: #808080;">//&nbsp;after&nbsp;styler</span><br><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">if</span><span class="f_CodeExample">(x</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample">==</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">1</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample">&amp;</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample">y</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample">!=</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">2</span><span class="f_CodeExample">)</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">{</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;&nbsp;</span><span class="f_CodeExample" style="font-weight: bold; color: #0000ff;">int</span><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">a</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample">=</span><span class="f_CodeExample" style="color: #ffffff; background-color: #b8cde5;">&nbsp;</span><span class="f_CodeExample" style="color: #008000;">0</span><span class="f_CodeExample">;</span><br><span class="f_CodeExample" style="color: #ffffff;">&nbsp;</span><span class="f_CodeExample">}</span></p></td></tr></tbody></table>

## Compilers [#](settings#compiler)

You do not necessarily need to use an external editor for multilingual projects. C/C++ and Python projects can be managed straight from MetaEditor.

If appropriate compilers are installed on your PC, MetaEditor will detect them and add to settings. Optionally, you can specify paths to required components under the Compilers tab. From the same tab, you can download the components by clicking Install next to the appropriate field.

After that you can work with C/C++ and Python projects similarly to MQL5 programs.

![External Compiler Settings](/en/docs/mt5/metaeditor/img/settings_compilers.png "External Compiler Settings")

Also in this section you can set parameters for compiling MQL5 programs:

-   MQL5 — processor architecture for which the [applications will be compiled](/en/docs/mt5/metaeditor/compile#architecture).

-   Check floating point dividers — applications with the check disabled work a little faster, because the zero divide error is not checked during code execution. The parameter can be overridden for each [project](/en/docs/mt5/metaeditor/projects#properties) separately.

## AI Assistant [#](settings#ai_assistant)

MetaEditor features [AI Assistant](/en/docs/mt5/metaeditor/ai_assistant) — the advanced automatic code completion tool powered by the [OpenAI](https://openai.com/blog/openai-codex)\-based models. This section provides the relevant settings:

![AI Assistant settings](/en/docs/mt5/metaeditor/img/ai_assistant_settings.png "AI Assistant settings")

-   Use MQL5 account — this option is currently available for free. Later, you will be able to pay for the subscription directly from your [MQL5 account balance](/en/docs/mt5/metaeditor/settings#mql5community).
-   Use OpenAI API key — you can use it if you have already purchased the [subscription](https://openai.com/api/pricing/) and have the key.
-   Model — a neural network which will process your requests. GPT-3.5 Turbo, GPT-4 Turbo and GPT-4o are currently available.
-   Maximum tokens — the number of text units which the model can return in response to a prompt.
-   Variability — affects how strictly the neural network will follow the prompt. The higher the value, the greater the result randomness. This option corresponds to the [temperature](https://platform.openai.com/docs/api-reference/chat#classifications/create-temperature) parameter in OpenAI models.

## Debug [#](settings#debug)

This tab allows you to configure general [debugging](/en/docs/mt5/metaeditor/debug) and program [profiling](/en/docs/mt5/metaeditor/profiling) options.

![Debug](/en/docs/mt5/metaeditor/img/settings_debug.png "Debug")

The following settings are available here:

-   Enable optimizations in profiling — disable this option to access more details in the profiling report. However, please note that speed can drop significantly and code bottlenecks can be imprecise without optimization.
-   Enable inlining in profiling — during inlining, the function code is added directly to call its call site, which enables significant program acceleration in come cases. However, this procedure makes the [profiling of functions](/en/docs/mt5/metaeditor/profiling) difficult. In order to obtain a report on "pure" functions, you can disable inlining.
-   Use visual mode for debugging on history — debugging on history is performed in non-visual mode by default. This option can be used to enable the visual mode manually. Profiling on history always runs in the non-visual mode.  
    Profiling on history in the visual mode is practically useless, since resources are spent on rendering rather than on MQL program calculations. Normally, the real data mode is enough for testing graphics functions (panels, objects and others). Programs in this mode are simply launched on a regular chart.
-   Use specified settings — enable/disable the use of certain settings for debugging and profiling programs. When starting debugging or profiling, the program will be launched on a chart with a specified symbol and period. When debugging on history, these parameters are used for visual testing. If this option is disabled, all the fields below are not editable.
-   Symbol — symbol chart to be used for debugging/profiling of programs.
-   Period — chart period to be used when debugging/profiling programs.
-   Date — period used to check a program when [debugging in history](/en/docs/mt5/metaeditor/debug#history). A visual testing is launched in the strategy tester on this period.
-   Execution — strategy tester allows you to emulate network delays during an Expert Advisor operation in order to bring testing closer to real conditions. A certain time delay is inserted between placing a trade request and its execution in the strategy tester. From the moment of sending a request till its execution, the price can change. This allows you to evaluate how trade processing speed affects the trading results. Select a delay to be used when debugging on history: no delay, a fixed value (one of the predefined values or a custom one) or a random value. For more information, please read the trading platform user guide.
-   Tick generation mode — used for debugging on history. For more information, please read the trading platform user guide.

-   Every tick — most accurate but the slowest mode. It simulates all ticks.
-   1 minute OHLC — in this mode only 4 prices (Open, High, Low and Close) of each minute bar are emulated.
-   Open prices only — in this mode, OHLC prices are also simulated, however only the open price is used for testing/optimization.
-   Deposit — initial deposit currency and amount for debugging on history. Please note that cross rates for converting profit and margin to the specified deposit currency must be available on the account, to ensure proper debugging. Only symbols with the "Forex" or "Forex No Leverage" calculation type can be used as cross rates.
-   Leverage — leverage used for debugging on history data.
-   Profit in pips — if this option is enabled, profit during debugging and profiling in the tester will be calculated in pips instead of money. This mode accelerates testing while there is no need to recalculate profit to deposit currency using conversion rates (and thus there is no need to download the appropriate price history). Swap and commission calculations are eliminated in this mode. Please note that when calculating profit in pips, the deal volume does not matter. Only the number of won/lost pips is calculated for each deal. Also margin control is not performed in this mode.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If no symbol and chart period for debugging/profiling are specified on this tab, the first symbol of the Market Watch window on H1 timeframe is used by default.</span></p></td></tr></tbody></table>

## MQL5.community [#](settings#mql5community)

Trading platform and MetaEditor are tightly integrated with [MQL5.community](https://www.mql5.com/en "MQL5.community") — a community of MQL5 developers. The MQL5.community provides unique services for traders and developers:

-   Market — you can purchase any ready-made application [in the store of MQL4/MQL5 programs](https://www.mql5.com/en/market "Market on MQL5.community website"). Before purchasing, you can download a trial version and test it in the strategy tester.
-   MQL5 Cloud Network [is a powerful distributed computing network](https://cloud.mql5.com/ "MQL5 Distributed Cloud Network") available for testing and optimization of Expert Advisors in the Strategy Tester. Thousands of optimization sessions can now be performed in minutes. In addition to using the network, you can provide your own computing capacities and earn.
-   MQL5 Storage — personal storage of source codes integrated into the MetaEditor. Keep your code safe and access it from anywhere in the world. The MQL5 Storage features will be expanded soon to allow multiple users to remotely work on one project.
-   Freelance — if you cannot find the desired application in the Code Base or Market, order one from a professional developer in the [Freelance section](https://www.mql5.com/en/job "Freelance on MQL5.community") of MQL5.community website.
-   Code Base — [download](/en/docs/mt5/metaeditor/toolbox#codebase "Download an application at the Code Base tab") any code published in the [Code Base](https://www.mql5.com/en/code "Code Base at MQL5.community") of MQL5.community website. The code is automatically placed in the correct directory and compiled.
-   Articles — various useful MQL5.community articles about MQL5 programming language and the platform have been published on the MQL5.community website. [Find](/en/docs/mt5/metaeditor/toolbar_search) the necessary data by article headers and descriptions conveniently listed in a separate tab of the [Toolbox](/en/docs/mt5/metaeditor/toolbox#articles) window.
-   MQL5 Charts — a special service allowing to [post screenshots from the trading platform online](https://www.mql5.com/en/charts) and share them in popular social networks.
-   Signals — subscribe to [trading signals](https://www.mql5.com/en/signals) of professional traders and receive them straight in your platform.

![Configuring access to MQL5.community](/en/docs/mt5/metaeditor/img/settings_mql5community.png "Configuring access to MQL5.community")

Enter your account detail and get access to all the unique services of the MQL5.community:

-   Login — MQL5.community account.
-   Password — a password to the specified account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The password is stored on the hard drive in an encrypted form.</span></li><li class="p_tableatten"><span class="f_tableatten">Login and password are case sensitive. They should accurately match your login on MQL5.community website.</span></li><li class="p_tableatten"><span class="f_tableatten">If you do not have an MQL5.community account, please <a href="https://www.mql5.com/en/auth_register" target="_blank" class="weblink" title="Register at MQL5.community">register</a> and get access to unique opportunities.</span></li></ul></td></tr></tbody></table>

[Launch](/en/docs/mt4/metaeditor/open)

[Integration with other IDEs](/en/docs/mt4/metaeditor/integration_ide)