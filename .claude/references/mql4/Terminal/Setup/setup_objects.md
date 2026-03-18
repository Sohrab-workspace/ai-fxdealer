# Objects

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/setup_objects

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
            -   [Server](/en/docs/mt4/terminal/setup/setup_server)
            -   [Charts](/en/docs/mt4/terminal/setup/setup_charts)
            -   [Objects](/en/docs/mt4/terminal/setup/setup_objects)
            -   [Trade](/en/docs/mt4/terminal/setup/setup_trade)
            -   [Expert Advisors](/en/docs/mt4/terminal/setup/setup_experts)
            -   [Notifications](/en/docs/mt4/terminal/setup/settings_notifications)
            -   [Email](/en/docs/mt4/terminal/setup/setup_email)
            -   [FTP](/en/docs/mt4/terminal/setup/setup_publisher)
            -   [Events](/en/docs/mt4/terminal/setup/setup_events)
            -   [Community](/en/docs/mt4/terminal/setup/settings_mql5community)
            -   [Signals](/en/docs/mt4/terminal/setup/settings_signals)
        -   [User Interface](/en/docs/mt4/terminal/overview)
        -   [Working with Charts](/en/docs/mt4/terminal/chart_management)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)Objects

# Objects

Settings for working with graphical objects are grouped in this tab. Graphical objects are all line studies placed in the [toolbar having the same name](/en/docs/mt4/terminal/overview/toolbars/toolbars_line_studies) and in the ["Insert" menu](/en/docs/mt4/terminal/overview/main_menu/main_menu_insert). They consist of: [technical indicators](/en/docs/mt4/terminal/analytics/tech_indicators) (including [custom indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)), [line studies](/en/docs/mt4/terminal/analytics/objects_control/line_studies), geometrical figures, texts, and icons. Parameters collected in this tab facilitate the work with graphical objects and cannot cause critical changes in the terminal operation.

![options_objects](/en/docs/mt4/terminal/img/options_objects.png)

-   Show Properties after Creation  
    All graphical objects possess certain properties. For example, it can be thickness and color of the trend line, period of the indicator signal line, etc. The most traders use standard settings of all graphical objects, but it is sometimes necessary to set them up individually. The "Show properties after creation" option allows to set up objects immediately after they have been imposed. It is suitable when there are many objects having individual settings on the chart.
-   Select Object after Creation  
    Unlike [indicators](/en/docs/mt4/terminal/analytics/tech_indicators), such objects as line studies, text, icons, and geometrical figures are positioned in charts manually. After an object has been imposed, there can a need occur to move it, for example, to precise the position of the trend line. To do so, the necessary object must be selected first. The "Select object after creation" option allows to do it immediately after the object has been imposed in the chart.
-   Select Object by Single Mouse Click  
    Graphical objects in the terminal can be selected by single or double clicking of the left mouse button. This option allows to switch between methods of objects selection. If it is enabled, all objects will be selected by a single click. At that, the double click calls the window of the object properties. If this option is disabled, all objects will be selected by a double click.
-   Magnet Sensitivity  
    The terminal allows to "magnet" (anchor) checkpoints of objects to different bar prices to locate them more precisely. In the "Magnet sensitivity" field, the sensitivity of this option in pixels can be defined. For example, if the value of 10 is specified, the object will automatically be anchored to the bar if a checkpoint of the object is located within a radius of 10 pixels from the nearest bar price (OHLC). To disable this option, it is necessary to input parameter 0.

[Charts](/en/docs/mt4/terminal/setup/setup_charts)

[Trade](/en/docs/mt4/terminal/setup/setup_trade)