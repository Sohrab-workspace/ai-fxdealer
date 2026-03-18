# Templates and Profiles

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/chart_management/templates

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
        -   [New trading features](/en/docs/mt4/terminal/new_terminal)
        -   [Getting Started](/en/docs/mt4/terminal/userguide)
        -   [Client Terminal Settings](/en/docs/mt4/terminal/setup)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
            -   [Chart Opening](/en/docs/mt4/terminal/chart_management/charts_open)
            -   [Setup](/en/docs/mt4/terminal/chart_management/charts_setup)
            -   [Chart Management](/en/docs/mt4/terminal/chart_management/charts_control)
            -   [Publishing Charts Online](/en/docs/mt4/terminal/chart_management/mql5_charts)
            -   [Quick Trading](/en/docs/mt4/terminal/chart_management/chart_trading)
            -   [Charts Print](/en/docs/mt4/terminal/chart_management/charts_print)
            -   [Deleted Charts](/en/docs/mt4/terminal/chart_management/charts_deleted)
            -   [Templates and Profiles](/en/docs/mt4/terminal/chart_management/templates)
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Working with Charts](/en/docs/mt4/terminal/chart_management)Templates and Profiles

# Templates and Profiles

A template is a set of chart window parameters that can be applied to other charts. The following can be stored in a template:

-   chart type and color;
-   color diagram;
-   chart scale;
-   OHLC line shown or hidden;
-   the attached expert advisor and its parameters;
-   the imposed custom and technical indicators with their settings;
-   line studies;
-   separators of days.

When a template is imposed into a chart, the stored settings, as they are, will be attached to the security and period. For example, one can create a template that includes indicators of MACD, RSI, and Moving Average, and then use it for other charts. In this case, charts windows will have the same view for different symbols and periods.

Templates are stored in the /TEMPLATES directory as TPL files. A template created once can be used unlimited amount of times. A basic template (DEFAULT.TPL) is created during installation of the terminal. It will be applied automatically for creation a new chart window. In future, it can be changed by using of the active chart window properties.

To create a new template, one has to execute the ["Charts — Template — Save Template..." menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command, the chart context menu command of the same name, or by pressing of the ![Templates](/en/docs/mt4/terminal/img/tb_charts_template.png "Templates") button of the ["Charts" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_charts). As a result, a new template will be created on basis of the data of active chart window. The same actions must be performed to modify a template, but an existing template should be selected instead of entering of a new filename. To impose a template into the chart window, one has to select the desired file in the templates managing menu or in any available folder in the "Open" window that can be called by the ["Charts — Template — Load Template..." menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command. The ["Charts — Template — Remove Template" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) command and the chart context menu command of the same name allow to delete templates.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The "DEFAULT.TPL" cannot be removed.</span></p></td></tr></tbody></table>

## Profiles [#](templates#profiles)

Profiles offer a convenient way of working with groups of charts. When a profile opens, each chart with its settings is placed exactly in the same location where it was before, at the profile saving. All changes in all chart windows of the given list are automatically saved in the current profile. The list of all chart windows of the current profile can be found in the ["Window" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_window). The name of the current profile is displayed in one of the status bar windows and checked in the profile managing menu. When the terminal is installed, the profile by default (DEFAULT) is created. Initially, four basic currency pairs are stored in it: "EUR/USD", "USD/CHF", "GBP/USD", and "USD/JPY".

Profiles are managed from a single menu that can be called by the ["File — Profiles" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_file) commands, by pressing of the ![Profiles](/en/docs/mt4/terminal/img/tb_standard_profile.png "Profiles") button of the ["Standard" toolbar](/en/docs/mt4/terminal/overview/toolbars/toolbars_standard), or by clicking with the mouse button on the current profile name in the status bar window. To use another profile, one has to select the desired name from the list in this menu. At that, the new profile will be opened and become the current. The "Save Profile" command saves the current profile in its state by the moment of the beginning of the command execution under a new name. The new profile is a copy of the previous one and becomes the current. One can delete profiles using the "Remove Profile" command.

The "Next Profile" command and Ctrl + F5 open all available profiles one by one, and the "Previous Profile" and accelerating keys of Shift + F5 allow to search profiles in the reverse direction.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: The current profile and that by default (DEFAULT) cannot be deleted.</span></p></td></tr></tbody></table>

A pre-defined profile can be assigned to a trade account in the client terminal. This profile must have a name that coincides with the number of the trade account. If there is a corresponding profile when switching to the given trade account, it will be opened automatically. If there is no pre-defined profile, the current profile will remain active.

[Deleted Charts](/en/docs/mt4/terminal/chart_management/charts_deleted)

[Analytics](/en/docs/mt4/terminal/analytics)