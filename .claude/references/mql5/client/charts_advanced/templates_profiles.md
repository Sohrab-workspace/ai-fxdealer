# Templates and Profiles

> Source: https://support.metaquotes.net/en/docs/mt5/client/charts_advanced/templates_profiles

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
            -   [View and Configure Charts](/en/docs/mt5/client/charts)
            -   [Publish Online](/en/docs/mt5/client/mql5_charts)
            -   [Technical Indicators](/en/docs/mt5/client/indicators)
            -   [Analytical Objects](/en/docs/mt5/client/objects)
            -   [Fundamental Analysis](/en/docs/mt5/client/fundamental)
            -   [Additional Technical Indicators](/en/docs/mt5/client/charts_analysis_get_indicators)
            -   [Additional Features](/en/docs/mt5/client/charts_advanced)
                -   [Chart Settings](/en/docs/mt5/client/charts_advanced/charts_settings)
                -   [Chart Print](/en/docs/mt5/client/charts_advanced/charts_print)
                -   [Chart Management](/en/docs/mt5/client/charts_advanced/charts_manage)
                -   [Lists of Objects Applied](/en/docs/mt5/client/charts_advanced/charts_objects_list)
                -   [Deleted Charts](/en/docs/mt5/client/charts_advanced/charts_deleted)
                -   [Templates and Profiles](/en/docs/mt5/client/charts_advanced/templates_profiles)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
        -   [Mobile Trading](/en/docs/mt5/client/mobile_trading)
        -   [MQL5 Algotrading community](/en/docs/mt5/client/mql5community)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Additional Features](/en/docs/mt5/client/charts_advanced)Templates and Profiles

# Templates and Profiles

A template is a set of chart window parameters that can be applied to other charts. The following data can be stored in a template:

-   chart type and color;
-   color scheme;
-   chart scale;
-   OHLC line shown or hidden;
-   running Expert Advisor and its parameters;
-   applied custom and technical indicators and their settings;
-   graphical objects;
-   separators of days.

When you apply a template to a chart, settings stored in it are applied to the instrument and timeframe. For example, you can create a template that includes indicators MACD, RSI, and Moving Average, and then use it for other charts. In this case, the chart windows look the same for different symbols and periods.

Templates are saved as TPL-files in folder [\\MQL5\\Profiles\\Templates](/en/docs/mt5/client/start_advanced/structure#templates). The platform provides several predefined names of templates:

-   default.tpl — the basic template that us automatically applied when you create a new chart;
-   tester.tpl — the template of the chart on which [testing](/en/docs/mt5/client/testing) results are displayed;
-   debug.tpl — the template of the chart created when you start MQL5 application debugging from [MetaEditor](/en/docs/mt5/client/autotrading#metaeditor).

To create a template with the desired parameters (or modify an existing one), configure the chart and click "![Save Template...](/en/docs/mt5/client/img/save_template_button.png "Save Template...") Save Template..." in its context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To share and synchronize templates and profiles between your platforms, use the <a href="https://www.metatrader5.com/en/metaeditor/help/mql5storage" class="weblink">MQL5 Storage</a>, which is integrated into MetaEditor. You will be able to access them from any computer using your <a href="/en/docs/mt5/client/mql5community" class="topiclink">MQL5.community</a> account.</span></p></td></tr></tbody></table>

## Actions with Templates

Click "Templates" in the [Chart](/en/docs/mt5/client/interface) menu or in the context menu of a chart or click on ![Templates menu](/en/docs/mt5/client/img/templates_button.png "Templates menu") on the toolbar.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:189px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Templates menu</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Actions with templates</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:189px;"><p class="p_fortable"><img class="help" alt="Templates menu" title="Templates menu" width="185" height="169" src="/en/docs/mt5/client/img/templates_menu.png"></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Creation</span><br><span class="f_fortable">To create a new template click "<img class="help" alt="Save Template..." title="Save Template..." width="16" height="16" src="/en/docs/mt5/client/img/save_template_button.png"> Save Template...". A new template is created based on the information of the active chart window.</span></li><li class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Modification</span><br><span class="f_fortable">To edit a template, follow the same steps, but instead of a new file name select an existing template.</span></li><li class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Applying</span><br><span class="f_fortable">To apply a template to a chart, select the required file at the bottom of the menu or click "Load Template" to open a template from any other folder.</span></li><li class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Deletion</span><br><span class="f_fortable">To remove a template, click "Remove Template" in the <a href="/en/docs/mt5/client/interface" class="topiclink">Charts menu</a> or the context menu of the chart.</span></li></ul></td></tr></tbody></table>

## Profiles [#](templates_profiles#profiles)

Profiles provide a convenient way of working with groups of charts. The following data can be stored in a profile:

-   charts that are open at the moment when you save the profile
-   the location and size of these charts;
-   [templates](/en/docs/mt5/client/charts_advanced/templates_profiles) applied to the charts.

When a profile is opened, each chart with all its settings is located exactly in the same position where it was during profile saving. All changes in open chart windows are automatically saved in the current profile. The list of all charts of the current profile is available in the [Window](/en/docs/mt5/client/interface) menu. The name of the current profile is displayed in the [status bar](/en/docs/mt5/client/interface) and is marked with a tick in the profile control menu.

A default profile is created during platform installation. Initially, it stores four chart windows of basic currency pairs: EURUSD, USDCHF, GBPUSD and USDJPY. All profiles are stored in a folder [\\MQL5\\Profiles\\Charts](/en/docs/mt5/client/start_advanced/structure#profiles).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Chart templates with running Expert Advisors are also saved in profiles, therefore the <a href="/en/docs/mt5/client/settings#profile" class="topiclink">platform settings</a> provide an option for automatic disabling of Expert Advisors when changing the profile.</span></p></td></tr></tbody></table>

## Managing Profiles [#](templates_profiles#profiles_manage)

Click "Profiles" in the [File menu](/en/docs/mt5/client/interface), button ![Profiles menu](/en/docs/mt5/client/img/profiles_button.png "Profiles menu") on the toolbar or click on the name of the current profile in the [status bar](/en/docs/mt5/client/interface).

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:189px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Profiles menu</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Commands</span></p></th></tr></thead><tbody><tr class="table"><td class="table" rowspan="2" style="width:189px;"><p class="p_fortable"><img class="help" alt="Profiles menu" title="Profiles menu" width="166" height="170" src="/en/docs/mt5/client/img/profiles_menu.png"></p></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Next</span><span class="f_fortable"> — switch to the next profile in the list. The same action can be performed using hotkeys "Ctrl+F5";</span></li><li class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Previous</span><span class="f_fortable"> — switch to the previous profile in the list. The same action can be performed using "Shift+F5";</span></li><li class="p_fortable"><img class="help" alt="Save As..." title="Save As..." width="16" height="16" src="/en/docs/mt5/client/img/profile_save_button.png"><span class="f_fortable"> </span><span class="f_fortable" style="font-weight: bold;">Save as</span><span class="f_fortable"> — save the current profile with a new name. The new profile is a copy of the current one and becomes active after saving;</span></li><li class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Remove</span><span class="f_fortable"> — delete a profile. Clicking on this command opens the menu of existing profiles. Select one of them to delete it.</span></li></ul></td></tr><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">The lower part of this menu contains the list of existing profiles. To apply one of them click on it.</span></p></td></tr></tbody></table>

A predefined profile can be assigned to a trade account. Create a profile with the same name as the account number. The predefined profile is applied automatically when you switch to this account. If there is no predefined profile, the current profile remains active.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">The current profile and the default profile (marked as DEFAULT) cannot be deleted.</span></p></td></tr></tbody></table>

[Deleted Charts](/en/docs/mt5/client/charts_advanced/charts_deleted)

[Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)