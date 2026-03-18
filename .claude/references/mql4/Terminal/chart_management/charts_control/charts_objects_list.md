# Lists of Objects Applied

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/chart_management/charts_control/charts_objects_list

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
                -   [Lists of Objects Applied](/en/docs/mt4/terminal/chart_management/charts_control/charts_objects_list)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Working with Charts](/en/docs/mt4/terminal/chart_management)[Chart Management](/en/docs/mt4/terminal/chart_management/charts_control)Lists of Objects Applied

# Lists of Objects Applied

The ["Charts"](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) menu and the context menu of the chart displaying window allow calling lists of applied graphical object, indicators and Expert Advisors. Thus object properties can be modified or objects can be deleted from the chart.

## List of Indicators [#](charts_objects_list#indicators)

This window can be opened using the "![Indicators List](/en/docs/mt4/terminal/img/indicators_list_icon.png "Indicators List") Indicators List" command of the ["Charts"](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) menu or the context menu of the chart window, or using the "Ctrl+I" hotkeys. This window allows managing indicators applied to the chart.

![Indicators List](/en/docs/mt4/terminal/img/indicators_list.png "Indicators List")

The window contains the list of indicators that are currently applied to the chart. Indicators are divided into two groups: those plotted in the main chart window and those plotted in a separate window. When one of indicators is selected, the "Properties" and "Delete" buttons become active. The "Properties" button opens the window of [indicator parameters](/en/docs/mt4/terminal/analytics/tech_indicators). The "Delete" button deletes an indicator from the chart.

## List of Objects [#](charts_objects_list#objects)

This window can be opened using the "![Objects List](/en/docs/mt4/terminal/img/objects_list_icon.png "Objects List") Objects List" command in the "Objects" sub-menu of the ["Charts"](/en/docs/mt4/terminal/overview/main_menu/main_menu_charts) menu or the context menu, or by pressing the "Ctrl+B" hotkeys. The window allows managing various graphical objects imposed to the chart.

![Objects List](/en/docs/mt4/terminal/img/objects_list.png "Objects List")

This window shows the list of all [objects](/en/docs/mt4/terminal/analytics/objects_control) currently imposed to the chart. These objects are represented in a table with the following fields:

-   Object — type of object. If a check is placed in the "Object" field, this object will be selected in the chart;
-   Name — object name. This name is formed out of the period of a chart the object is imposed to, object type and the unique identifies that is automatically assigned to each object. This name can be changed in the [object properties](/en/docs/mt4/terminal/analytics/objects_control);
-   Description — object description. It can also be changed in the [object properties](/en/docs/mt4/terminal/analytics/objects_control);
-   Window — number of the window, in which the object is applied. 0 denotes the main chart window, further figures denote order numbers of indicator sub-windows from upside down.

The "Objects" window contains the following commands:

-   Show — move the chart to the selected object;
-   Properties — [edit](/en/docs/mt4/terminal/analytics/objects_control) properties of a selected object;
-   Delete — delete a selected object;
-   List all — any object can be set as hidden (OBJPROP\_HIDDEN property) from an [MQL4](/en/docs/mt4/terminal/autotrading/mql4) application. Such objects are displayed on a chart and not displayed in the object list on default. If you click the "List all" button, hidden objects will be displayed in the list.

Use Ctrl+A hotkeys to select all objects.

[Chart Management](/en/docs/mt4/terminal/chart_management/charts_control)

[Publishing Charts Online](/en/docs/mt4/terminal/chart_management/mql5_charts)