# Debug

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/main_menu_debug

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
            -   [File](/en/docs/mt4/metaeditor/main_menu_file)
            -   [Edit](/en/docs/mt4/metaeditor/main_menu_edit)
            -   [Search](/en/docs/mt4/metaeditor/main_menu_search)
            -   [View](/en/docs/mt4/metaeditor/main_menu_view)
            -   [Debug](/en/docs/mt4/metaeditor/main_menu_debug)
            -   [Build](/en/docs/mt4/metaeditor/main_menu_build)
            -   [Tools](/en/docs/mt4/metaeditor/main_menu_tools)
            -   [Window](/en/docs/mt4/metaeditor/main_menu_window)
            -   [Help](/en/docs/mt4/metaeditor/main_menu_help)
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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Main menu](/en/docs/mt4/metaeditor/main_menu)Debug

# Debug

The menu is intended for [debugging](/en/docs/mt5/metaeditor/debug) MQL4/MQL5 programs. It contains the following commands:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:26px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></th><th class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Command</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Start" title="Start" width="14" height="14" src="/en/docs/mt5/metaeditor/img/start_debug_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Start/Resume debugging on real data<a name="start" class="hmanchor"></a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Launch <a href="/en/docs/mt5/metaeditor/debug" class="topiclink">debugging</a> of the current code on a chart that is updated in real time.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Start on History Data" title="Start on History Data" width="16" height="16" src="/en/docs/mt5/metaeditor/img/debug_history_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Start on History Data</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Launch <a href="/en/docs/mt5/metaeditor/debug#history" class="topiclink">debugging on history</a>. A program check runs in the visual testing mode in the strategy tester. An application is executed on a chart with an emulated sequence of ticks in the tester.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Pause" title="Pause" width="14" height="14" src="/en/docs/mt5/metaeditor/img/break_debug_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Pause<a name="break" class="hmanchor"></a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Pause a program debugging. To continue debugging, click Resume.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Stop" title="Stop" width="14" height="14" src="/en/docs/mt5/metaeditor/img/stop_debug_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Stop<a name="stop" class="hmanchor"></a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Stop debugging.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Step Into" title="Step Into" width="12" height="15" src="/en/docs/mt5/metaeditor/img/step_into_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Step Into</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Move one step of program execution accessing the called functions.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Step Over" title="Step Over" width="14" height="15" src="/en/docs/mt5/metaeditor/img/step_over_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Step Over</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Move one step of program execution without accessing the called functions.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Step Out" title="Step Out" width="15" height="14" src="/en/docs/mt5/metaeditor/img/step_out_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Step Out</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Execute a single step of a program one level higher.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Enable a breakpoint" title="Enable a breakpoint" width="16" height="16" src="/en/docs/mt5/metaeditor/img/breakpoint_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Toggle Breakpoint<a name="breakpoint" class="hmanchor"></a></span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Enable/disable a <a href="/en/docs/mt5/metaeditor/debug#breakpoint" class="topiclink">breakpoint</a> on the current line depending on its current status.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Clear All Breakpoints" title="Clear All Breakpoints" width="16" height="16" src="/en/docs/mt5/metaeditor/img/clear_all_breakpoints_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Clear All Breakpoints</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Clear all breakpoints from the currently debugged program.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Start profiling on real data" title="Start profiling on real data" width="15" height="12" src="/en/docs/mt5/metaeditor/img/start_profiling_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Start profiling on real data</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Launch the <a href="/en/docs/mt5/metaeditor/profiling" class="topiclink">profiling</a> of the current code on a normal chart that is updated in real time.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Start profiling on history data" title="Start profiling on history data" width="15" height="12" src="/en/docs/mt5/metaeditor/img/start_profiling_history_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Start profiling on history data</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Launch the <a href="/en/docs/mt5/metaeditor/profiling" class="topiclink">profiling</a> of the current code in the Strategy Tester in the visual mode.</span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Stop Profiling" title="Stop Profiling" width="10" height="10" src="/en/docs/mt5/metaeditor/img/stop_profiling_icon.png"></p></td><td class="table" style="width:223px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Stop Profiling</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Stop profiling.</span></p></td></tr></tbody></table>

[View](/en/docs/mt4/metaeditor/main_menu_view)

[Build](/en/docs/mt4/metaeditor/main_menu_build)