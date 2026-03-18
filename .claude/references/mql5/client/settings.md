# Platform Settings

> Source: https://support.metaquotes.net/en/docs/mt5/client/settings

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
            -   [User Interface](/en/docs/mt5/client/interface)
            -   [Open an Account](/en/docs/mt5/client/acc_open)
            -   [Connect to an Account](/en/docs/mt5/client/authorization)
            -   [Deposits and withdrawals](/en/docs/mt5/client/payments)
            -   [Platform Settings](/en/docs/mt5/client/settings)
            -   [For Advanced Users](/en/docs/mt5/client/start_advanced)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)Platform Settings

# Platform Settings

The trading platform provides multiple settings to help you conveniently customize it. Click "![Options](/en/docs/mt5/client/img/options_icon.png "Options") Options" in the [Tools](/en/docs/mt5/client/interface) menu or press "Ctrl+O".

![Customize the platform](/en/docs/mt5/client/img/settings.png "Customize the platform")

All settings are grouped in several tabs based on what they do:

-   [Server](/en/docs/mt5/client/settings#server) — setup of server connection, configuration of a proxy server, and other important settings;
-   [Charts](/en/docs/mt5/client/settings#charts) — common settings of price charts and parameters of objects management: object selection straight after creation, immediate object configuration, and docking parameters;
-   [Trade](/en/docs/mt5/client/settings#trade) — default parameters applied to the opening of new orders. They include: financial instrument, number of lots, deviation, and placing of stop orders;
-   [Expert Advisors](/en/docs/mt5/client/settings#ea) — common settings for all Expert Advisors. They include: disabling operation of Expert Advisors, enabling importing functions from external DLL libraries and Expert Advisors, as well as a number of other features;
-   [GPU](/en/docs/mt5/client/settings#gpu) — managing OpenCL devices used for calculations in trading robots.
-   [Events](/en/docs/mt5/client/settings#events) — configuration of alerts of system events. You receive important alerts about connection loss, arrival of newsletters and other events;
-   [Notifications](/en/docs/mt5/client/settings#notifications) — sending push notifications to mobile devices from the trading platform;
-   [Email](/en/docs/mt5/client/settings#mail) — email parameters for sending messages straight from the platform;
-   [FTP](/en/docs/mt5/client/settings#ftp) — settings for publishing reports on the Internet. The trading platform allows saving and automatically publishing reports about the account state in real time. This is done over ftp based connection, which can be configured in this tab;
-   [Community](/en/docs/mt5/client/settings#community) — details of your MQL5.community account;
-   [Signals](/en/docs/mt5/client/settings#signals) — settings for the [Signals service](https://www.mql5.com/en/signals "Signals Service") in the trading platform.

## Server [#](settings#server)

This tab contains the most important settings. The trading platform is initially configured to provide proper trouble-free operation. Thus, it is highly recommended not to change any parameters in this window unless there is a special necessity.

![The Server tab contains settings for connection to a trading account](/en/docs/mt5/client/img/options_server.png "The Server tab contains settings for connection to a trading account")

The window contains the following parameters:

-   Server — the name of the trade server the platform connects to. After the program installation, this field is already filled in. However, if you want to connect to another server, specify here the domain name (or IP address) of the server and connection port number separated by a colon. For example: 192.168.0.1:443. These data are saved on your computer and take effect only when you try to open a [new account](/en/docs/mt5/client/acc_open). The new server address is added to the list of servers and can be selected during [account registration](/en/docs/mt5/client/acc_open);
-   Certificate — click here to view the [details of the certificate](/en/docs/mt5/client/start_advanced/extended_authorization#certificate_view) that is used for authenticating on a trade server. The button only appears if the [extended authentication](/en/docs/mt5/client/start_advanced/extended_authorization) mode is used on the server;
-   Login — an account opened on the trade server and used to connect to it when you run the platform;
-   Password — account password for connecting to a trade server;
-   Change — [change the password](/en/docs/mt5/client/settings#password) to the account;
-   Enable proxy server — allow the use of a proxy server when connecting to the trade server. If you enable this option, button "Proxy ..." becomes active;
-   Proxy — setup of connection through a [proxy server](/en/docs/mt5/client/settings#proxy);
-   Keep personal settings and data at startup — save account details (number, main and investor passwords) on the hard disk after an account is created. During the next platform start, these data will be used for the automatic connection. If the option is disabled, you will need to enter the details manually each time you start the platform. This option only affects the current account specified in the "Login" field;
-   Enable news — this option allows to enable or disable [news](/en/docs/mt5/client/fundamental#news). If this option is disabled, news will not be received in the platform;
-   News languages — this option allows filtering news by their language. When you click "Edit", the [news language](/en/docs/mt5/client/settings#news_language) selection dialog appears. If it is set to "Auto Select", the news language is selected automatically in accordance with the trading platform UI language. News articles in English are displayed in case the platform language is not available for the news.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">It is strongly recommended that you do not change server connection settings unless there is a special necessity.</span></p></td></tr></tbody></table>

### Password Change [#](settings#password)

To change the account password, click "Edit". After that the following window opens:

![To change the password, enter the current master password](/en/docs/mt5/client/img/change_password.png "To change the password, enter the current master password")

The following details are to be indicated in the password changing dialog:

-   Login — account number, this field cannot be changed;
-   Current password — the field to enter the [master password](/en/docs/mt5/client/acc_open#main_password);
-   Change master password — select this option if you want to change the master password of your account;
-   Change investor password — select this option if you want to change the investor password of your account;
-   New password — field for entering a new password;
-   Confirm — field for confirming a new password.

The new password must meet the following requirements:

-   It must be no shorter than the length requirement displayed in the password change dialog.
-   It must contain four character types: lowercase letters, uppercase letters, numbers, and [special characters](https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/special-characters) (#, @, ! etc.). For example, 1Ar#pqkj.
-   It must not match the previous password.

After specifying all the data click "OK".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">A password cannot be changed if the current password is not specified.</span></p></td></tr></tbody></table>

### Proxy Server Setup [#](settings#proxy)

A proxy server is an intermediate between the trader's computer and the trade server. It is mostly used by internet providers or by local networks. If you have any connection problems, contact your system administrator or ISP. If you use a proxy server, configure the platform accordingly. Option "Enable proxy server" enables proxy server support and activates the "Proxy..." button.

![Specify proxy settings if it is used for connection to the Internet](/en/docs/mt5/client/img/proxy_server.png "Specify proxy settings if it is used for connection to the Internet")

-   Server — enter here the IP address and port number of the server separated by a colon. To the right of this field, select the type of proxy server: HTTP, SOCKS4 or SOCKS5. In HTTP mode, NTLM authentication is also supported;
-   Login — a login to access the proxy server. If no login is required, leave it blank;
-   Password — a password to access the proxy server. If no password is required, leave the field blank.
-   Test — use this button to check whether all the proxy settings are correct. If the settings are incorrect, then after clicking on this button you will receive an appropriate message.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Consult your system administrator or internet provider for proxy setup details.</span></p></td></tr></tbody></table>

### News Language Selection [#](settings#news_language)

To select language of incoming news, click "Edit" next to the appropriate field.

![Select the language of financial news](/en/docs/mt5/client/img/options_select_language.png "Select the language of financial news")

The left part of the window contains available languages, the right part — selected ones. To add a language, double-click on it in the left part, or select it and click "Add." To delete a language, use the "Remove" button. The "Reset" button sets the default values.

## Charts [#](settings#charts)

Charts show dynamics of security price changes. Chart settings and history data parameters are grouped in this tab. Changing the parameters in this tab does not cause any global changes in the platform operation.

This tab also contains settings for working with different objects applied to charts. They include [technical](/en/docs/mt5/client/indicators) and [custom](/en/docs/mt5/client/trade_robots_indicators) indicators, as well as various [graphical objects](/en/docs/mt5/client/objects). Parameters collected in this tab facilitate work with graphical objects and cannot cause critical changes in the platform operation.

![The Charts tab contains settings for working with analytical objects, trade levels, etc.](/en/docs/mt5/client/img/options_charts.png "The Charts tab contains settings for working with analytical objects, trade levels, etc.")

The following chart settings are available on this tab:

-   Color print — the platform allows printing not only black and white, but also colored charts. The latter ones are more appropriate for analysis than black-and-white ones. Enable this option to print color charts, if your printer supports colored printing.
-   Show trade history — show/hide on the chart entries and exits for the appropriate instrument. For more details, please visit section "[How to Analyze Your Entries on the Chart](/en/docs/mt5/client/performing_deals#position_showonchart)". The parameter is applied to all charts which the user opens in the platform. If the parameter is enabled, the display of trading history will be enabled on all charts by default. It can further be individually disabled [in appropriate chart settings](/en/docs/mt5/client/charts_advanced/charts_settings#trade_history).
-   Show trade levels — this option enables the display of price levels at which a position has been opened or a pending order has been placed, as well as Stop Loss and Take Profit levels. Display of trade levels can be enabled [separately](/en/docs/mt5/client/charts_advanced/charts_settings#trade_levels) for each chart.

-   Disable dragging of trade levels — this option disables the possibility to modify [pending](/en/docs/mt5/client/performing_deals#pending_modify_chart) and [stop orders](/en/docs/mt5/client/performing_deals#position_modify_chart) by dragging them on the chart.
-   Enable dragging of trade levels — this option allows modifying [pending](/en/docs/mt5/client/performing_deals#pending_modify_chart) and [stop orders](/en/docs/mt5/client/performing_deals#position_modify_chart) by dragging them on the chart.
-   Enable dragging of trade levels with "Alt" key — this option allows to conveniently control [pending orders](/en/docs/mt5/client/performing_deals#pending_modify_chart) and [stop levels on a chart](/en/docs/mt5/client/performing_deals#position_modify_chart). By default, without enabling this option, the orders and stop levels are moved using a mouse (drag'n'drop). If multiple [objects](/en/docs/mt5/client/objects) are applied on a chart, you can accidentally move one of them instead of the level. In this case, enable this option. You still can drag trade levels using your mouse, but need to additionally hold the "Alt" key.
-   Preload chart data for open positions and orders — in order to save traffic, the trading platform downloads symbol price history only when the relevant data is requested, for example when the [price chart is opened](/en/docs/mt5/client/charts) or when [testing](/en/docs/mt5/client/testing) is launched. However, this may not always be convenient for actively used symbols. If you enable this option, the charts of the symbols for which you have open positions or pending orders, will always be updated in the background mode. Thus, you will not have to wait for data to be downloaded after chart opening, and the relevant data will be immediately available for analysis.
-   Show object properties after creation — all objects have certain [properties](/en/docs/mt5/client/objects#manage). For example, thickness and color of the trend line, period of the indicator's signal line, etc. Most traders use standard settings of all graphical objects, but in some cases you may need to set them up individually. Option "Show object properties after creation" allows to automatically open the window of properties of [graphical objects](/en/docs/mt5/client/objects#manage) and [indicators](/en/docs/mt5/client/indicators#run) after they are applied to a chart.
-   Select objects by single mouse click — graphical objects in the platform can be selected by a single or double click. This option allows switching between the object selection methods. If it is enabled, all objects are selected by a single click. If this option is disabled, all objects are selected by a double click.
-   Precise time scale — if this option is disabled, objects are bound to bars along the horizontal scale of a chart. If you enable it, then it is possible to position an object at any point between bars.
-   Select objects after creation — objects are positioned in charts manually. After creating an object you may need to move it, for example to accurately position a trendline. To do that, it is necessary to select the object first. This option allows to do that automatically right after placing an object on a chart.
-   Magnet sensitivity — the platform allows to "dock" anchor points (except for the central moving points) of [graphical objects](/en/docs/mt5/client/objects) to different bar prices to locate them more precisely. In the "Magnet sensitivity" field, the sensitivity of this option in pixels can be defined. For example, if the value of 10 is specified, the object will automatically be docked to a bar if the object's anchor point is located within a distance of 10 pips from the nearest bar price (OHLC). That point should also be within the bar width. To disable this option, set the parameter to 0.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you apply an object on a chart with the <a href="/en/docs/mt5/client/charts#operations" class="topiclink">timeframe</a> other than M1, the following magnet features appear:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">When anchoring a point of an object to one of the extreme price (OHLC), the specific minute is determined, where the extremum was recorded. Point of the object is bound to that minute, and it is reflected in the <a href="/en/docs/mt5/client/objects#parameters" class="topiclink">object properties</a>. This kind of behavior allows keeping proper positioning of objects when switching between timeframes.</span></li><li class="p_tableatten"><span class="f_tableatten">If the "Precise time scale" option is additionally enabled, then you may observe an effect when the anchor point moves away from an extreme point. This behavior appears if the actual extreme point doesn't correspond to the extreme point of a bar.</span></li></ul></td></tr></tbody></table>

-   Max. bars in chart — there is a difference between the bars stored in history and those shown in charts. This difference is determined by the fact that any amount of bars can be kept in the hard disk provided that it has enough space. But the amount of bars shown in the chart is limited by the computer resources.  
       
    Bars displayed on the chart are used for drawing [technical](/en/docs/mt5/client/indicators) and [custom](/en/docs/mt5/client/trade_robots_indicators) indicators. When multiple indicators and large amount of data to be displayed are used simultaneously, computer free resources (CPU load and free RAM) can exhaust very soon.  
       
    To avoid such problems, you can set the amount of data displayed on the charts. This can be done by selecting a corresponding value from the pop-up list or by entering a value manually in this field (minimum value is 5000). For the changes of this parameter to take effect, restart the platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Indicators can access more bars than specified in "Max bars in chart" parameter for more efficient calculation. Older bars are not removed immediately from the data cache when the new ones appear. This allows not to recalculate an indicator at each new bar, but calculate its values for new bars instead.</span></p></td></tr></tbody></table>

Changes of the settings take effect after clicking the OK button except the "Max. bars in chart" option. Restart the platform after you change the parameter.

## Trading [#](settings#trade)

This tab features settings used for [opening orders](/en/docs/mt5/client/performing_deals#position_open). Parameters specified here facilitate opening of orders and cannot cause critical changes in the platform operation.

![On the Trade tab, you can set the default settings for placing orders, and enable one-click trading](/en/docs/mt5/client/img/options_trade.png "On the Trade tab, you can set the default settings for placing orders, and enable one-click trading")

Use these options to set default parameters applied when [opening orders](/en/docs/mt5/client/performing_deals#position_open):

-   Symbol — this option allows to define a symbol that will be automatically added to the position opening window. The "Automatic" parameter means that the active chart symbol will be set in this field, the "Last used" — the symbol of the latest trade operation. If "Default" parameter is selected, you can specify a certain financial instrument that will be automatically set for all positions.
-   Volume — this option adds a certain volume in the [position opening](/en/docs/mt5/client/performing_deals#position_open) window, [quick trading panel on the chart](/en/docs/mt5/client/one_click_trading#chart_deal) and [a trading panel in Market Watch](/en/docs/mt5/client/market_watch#trading). The "Last Used" parameter means that the volume of a previous operation will be selected. The "Default" parameter allows to specify a certain volume to be indicated automatically for all positions.
-   Deviation — symbol price may change during order creation. As a result, the price of a prepared order will differ from the market one, and the position will not be opened. The "Use Deviation" option helps to avoid this. When "Default" parameter is set, to the right of this field you can set the maximum acceptable price deviation from the value indicated in the order. If prices are not identical, the program modifies the order and a new position is opened. If "Last Used" is selected, the deviation value of the previous opened position will be automatically set in the order opening window.
-   Stop levels — settings for the Stop Loss and Take Profit [levels](/en/docs/mt5/client/general_concept#take_profit) that will be added when [placing](/en/docs/mt5/client/performing_deals#position_open) orders or [modifying positions](/en/docs/mt5/client/performing_deals#position_modify). If the "in points" variant is chosen, stop levels will be specified in the number of points from the price of order placing. If the "in prices" variant is chosen, it will be necessary to specify the certain price level for stop levels.
-   One click trading — to use this option, you need to accept [special terms and conditions](/en/docs/mt5/client/settings#agreement). The one-click trading option allows performing trade operations in one click without additional confirmation by trader ([trade dialog](/en/docs/mt5/client/performing_deals#position_open) is not displayed). The one-click trading feature is implemented in the following parts of the platform:

-   the [Trading](/en/docs/mt5/client/market_watch#trading) tab in Market Watch,
-   [the quick trading panel on the chart](/en/docs/mt5/client/one_click_trading#chart_deal),
-   the [Trade](/en/docs/mt5/client/performing_deals#position_list) tab in the Toolbox window,
-   [Depth of Market](/en/docs/mt5/client/depth_of_market#quick_trading).
-   Show realtime history of deals on chart — when this option is enabled, all the deals performed by a trader are automatically displayed on the chart of the corresponding symbols with the icons ![Buy](/en/docs/mt5/client/img/buy_icon.png "Buy") (a Buy deal) and ![Sell](/en/docs/mt5/client/img/sell_icon.png "Sell") (a Sell deal). When you point the mouse cursor to an icon, a tooltip appears containing information about the deal: ticket, deal type, volume, symbol, open price and current price coordinate of the cursor.

### Terms and Conditions for Using One-Click Trading [#](settings#agreement)

When "One click trading" option is used for the first time, Terms and Conditions for using this function are displayed to users.

![Carefully read Terms and Conditions for Using "One-Click Trading" Function](/en/docs/mt5/client/img/one_click_disclaimer.png "Carefully read Terms and Conditions for Using "One-Click Trading" Function")

If you accept the conditions, tick "I Accept these Terms and Conditions" option and click "OK". If you do not accept the conditions, click "Cancel" and do not use the "One Click Trading" function.

## Expert Advisors [#](settings#ea)

Settings of working with Expert Advisors are grouped in this tab. Expert Advisors in the platform are applications developed in the [MetaQuotes Language 5](/en/docs/mt5/client/autotrading#mql5) used for the automation of analytical and trading processes. The description of how to create and use experts is given in section [How can I create and Expert Advisor or an Indicator](/en/docs/mt5/client/autotrading).

![Automated trading settings are available in the Expert Advisors tab](/en/docs/mt5/client/img/options_ea.png "Automated trading settings are available in the Expert Advisors tab")

This section contains description of settings common for all Expert Advisors only:

-   Allow Auto Trading — this option allows or prohibits trading using [Expert Advisors](/en/docs/mt5/client/trade_robots_indicators) and [scripts](/en/docs/mt5/client/autotrading#type). If it is disabled, scripts and Expert Advisors can work, but are not able to trade. This limitation can be useful for testing the analytical capabilities of an Expert Advisor in the real-time mode (not to be confused with testing on history data).  
    The option enables/disables automated trading for the entire platform. If you disable it, no Expert Advisor will be allowed to trade, even if you enable automated trading individually in the [Expert Advisor settings](/en/docs/mt5/client/trade_robots_indicators#run). If you enable it, the Expert Advisors will be allowed to trade, unless automated trading is individually disabled in the Expert Advisor parameters.

-   Disable automated trading when switching accounts — this option represents a protective mechanism disabling trading by Expert Advisors and scripts when the account is changed. It is useful, for example, when switching from a demo account to a real one.
-   Disable automated trading when switching profiles — a large amount of information about the current settings of all charts in the workspace is stored in [profiles](/en/docs/mt5/client/charts_advanced/templates_profiles#profiles). Particularly, profiles contain information about Expert Advisors attached. [Expert Advisors](/en/docs/mt5/client/trade_robots_indicators) included into the profile will start working with the arrival of a new tick. Enable this option to prevent trading by Expert Advisors when changing the profile.
-   Disable automated trading when switching chart symbols or period — if this option is enabled, then when the period or symbol of a chart is changed, the Expert Advisor attached to it will be automatically prohibited from trading.

-   Disable automatic trading through the external Python API — [Python scripts](/en/docs/mt5/client/trade_robots_indicators#python) which use the module for integration with the trading platform, can perform trading operations. However, this possibility is disabled by default for security reasons. You should explicitly enable auto trading by ticking off this option.
-   Allow DLL imports (potentially dangerous, enable only for trusted applications) — to extend functionality, [mql5 applications](/en/docs/mt5/client/autotrading) can use DLLs. This option allows determining a default value for the "Allow DLL imports" parameter used during [start of applications](/en/docs/mt5/client/trade_robots_indicators#run). It is recommended to disable import when working with unknown Expert Advisors.
-   Allow WebRequest for listed URL — the WebRequest() function in MQL5 is used for receiving and sending information to websites using GET and POST requests. To allow an MQL5 application to send such requests, enable this option and manually explicitly specify the URLs of trusted websites. For security reasons, the option is disabled by default.  
    To delete an address from the trusted list, select it and press "Delete".

## GPU [#](settings#gpu)

Modern video cards contain hundreds of small specialized processors which can simultaneously perform simple mathematical operations on incoming data threads.

-   The [OpenCL](https://www.mql5.com/en/docs/opencl) language organizes parallel computations and thus enables much faster operations for certain tasks when creating trading robots. In particular, such acceleration can be useful when developing applications based on neural networks. [MQL5](/en/docs/mt5/client/autotrading#mql5) provides native functions for accessing the OpenCL API and thus you can easily utilize API capabilities in your trading applications.

-   The trading platform and the MQL5 language also support [ONNX](https://www.mql5.com/en/docs/onnx), an open-source library for machine learning models. ONNX supports [CUDA](https://en.wikipedia.org/wiki/CUDA), which can significantly improve model inference performance.

In platform settings, you can explicitly specify which devices will be used for calculations. Using the settings, you can also enable/disable the use of CUDA/OpenCL when working in the local platform, in the strategy tester or when executing computational tasks received from the [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud).

![Manage GPU settings](/en/docs/mt5/client/img/options_gpu.png "Manage GPU settings")

The following information is displayed for each device:

-   Supported OpenCL version
-   Available memory
-   Support for the double type in calculations
-   Performance rating

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">We strongly recommend that you update your graphics drivers promptly to enhance stability and performance.</span></p></td></tr></tbody></table>

## Events [#](settings#events)

Alerts of system events (like server connection, disconnection, email notification, etc.) can be set up here. It is a very convenient tool informing about changes in the platform status. To start setting up alerts, check the "Allow" option.

![Sound alerts are configured in the Events tab](/en/docs/mt5/client/img/options_events.png "Sound alerts are configured in the Events tab")

All events are represented in the form of a table containing their names and default audio files that are executed when the event occurs. The following types of events are available:

-   Connect — alert of a successful connection to a server;
-   Disconnect — alert of server connection loss;
-   Email Notify — email received;
-   Timeout — a certain time range is given for performing trade operations. If this range has been exceeded for some reason, the operation will not be performed, and the alert will trigger;
-   Ok — alert of a successful execution of a trade operation;
-   News — alert of a received [newsletter](/en/docs/mt5/client/fundamental#news);
-   Expert Advisor — alert of a trade operation performed by an [Expert Advisor](/en/docs/mt5/client/trade_robots_indicators);
-   Alert — Alert() function executed by an Expert Advisor;
-   Requote — alert of a price changed (requote) at the attempt to perform a trade operation;
-   Trailing Stop — alert of [trailing stop order](/en/docs/mt5/client/general_concept#trailing_stop) triggering.
-   Testing Finished — alert of the end of [testing or optimization](/en/docs/mt5/client/testing).

To disable any of the alerts, click once on its icon ![Event](/en/docs/mt5/client/img/event_icon.png "Event") or double-click on its name. After that the icon will look like this — ![Disabled event](/en/docs/mt5/client/img/event_disabled_icon.png "Disabled event"). To activate an alert, repeat the same operation.

To change a file played when the event occurs, double-click on its name or select it and press "Enter". Then select "Choose other" from the drop-down list and specify the necessary file.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">By default a file with *.wav extension is offered as a sound. However, another file can also be selected. If a *.wav file is selected, it will be played when the alert triggers. If another file is selected, it will be opened using application it is associated with in the operating system.</span></p></td></tr></tbody></table>

## Notifications [#](settings#notifications)

The trading platform supports push notifications. Push notifications are short text messages which can be sent to mobile devices from the desktop platform and from various MQL5.community services.

Unlike SMS, push notifications are sent over the Internet and thus they do not depend on mobile carriers. They can be delivered to different regions without any fees. The trader only needs to install a mobile platform for [iOS](https://download.terminal.free/cdn/mobile/mt5/ios?hl=en&utm_campaign=metaquotes.download&utm_source=www.metatrader5.com "iOS") or [Android](https://download.terminal.free/cdn/mobile/mt5/android?hl=en&utm_campaign=metaquotes.download&utm_source=www.metatrader5.com "Android"). Notifications are delivered via the mobile platform.

### Configuring Notifications in the Mobile Platform

The identifier of the push notification recipient is MetaQuotes ID. Each device has a unique ID. Open the mobile platform and go to the "Messages" section:

![Specify MetaQuotes ID in the trading platform setting to receive pushes](/en/docs/mt5/client/img/mq_id.png "Specify MetaQuotes ID in the trading platform setting to receive pushes")

For further details please view the documentation for mobile platforms: [iPhone/iPad](https://www.metatrader5.com/en/mobile-trading/iphone/help/settings_messages), [Android](https://www.metatrader5.com/en/mobile-trading/android/help/messages).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">To install a mobile platform, please use the following links:</span></p><ul><li class="p_tableatten"><span class="f_tableatten"><a href="https://download.terminal.free/cdn/mobile/mt5/ios?hl=en&amp;utm_campaign=metaquotes.download&amp;utm_source=www.metatrader5.com" target="_blank" class="weblink" title="Mobile Platform for iPhone">Mobile Platform for iPhone</a></span></li><li class="p_tableatten"><span class="f_tableatten"><a href="https://download.terminal.free/cdn/mobile/mt5/android?hl=en&amp;utm_campaign=metaquotes.download&amp;utm_source=www.metatrader5.com" target="_blank" class="weblink" title="Mobile Platform for Android">Mobile Platform for Android</a></span></li></ul></td></tr></tbody></table>

### Configuring Notifications in the Desktop Platform

Check the "Enable Push Notifications" box and specify the MetaQuotes ID from your mobile platform.

![Sending of push notifications to a mobile device can be configured in the Notifications tab](/en/docs/mt5/client/img/options_notifications.png "Sending of push notifications to a mobile device can be configured in the Notifications tab")

You can specify up to 4 MetaQuotes IDs separated by commas. Push notifications will be sent to all devices simultaneously.

Next, select the type of notifications about trading activity on your account:

-   Notifications from the local terminal — the platform will automatically send notifications about all successful trade operations to the specified MetaQuotes ID. The platform will also send notifications about any balance operations performed on the account as well as about the Margin Call state (in this case notifications are sent periodically, as long as the account is in the Margin Call state). The platform will not send notification about unsuccessful operations (for example, if the order was rejected due to incorrect parameters).
-   Notifications from the trade server — the advantage of this option over the previous one is that the trader does not need to keep the platform constantly running. Notifications are sent from the broker's server. For example, if a Take Profit triggers on the server while your computer is turned off, you will receive a relevant position closing notification on your mobile device.  
       
    When you enable this option, the platform subscribes the current account to notifications. If you want to enable notifications for a different account, connect using the relevant account and enable this option in setting.  
       
    The availability and details of notifications depend on the broker. Three notification types are supported: orders, deals and balance operations. When you enable the option, the available notification types will be displayed in the platform log:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">&nbsp;'1222':&nbsp;subscribed&nbsp;to&nbsp;deals,&nbsp;orders,&nbsp;balance&nbsp;notifications&nbsp;from&nbsp;trade&nbsp;server</span></p></td></tr></tbody></table>

Click on the "Test" button to test the delivery of push notifications. Upon successful sending, you will see a corresponding message, and a test notification will be delivered to your mobile device.

### Configuring Notifications from MQL5.community

In order to keep abreast of the latest MQL5.community events, you can set up notifications about the latest site events via the Settings — Notifications section of your profile.

-   private message notifications
-   notifications about comments on your blogs, forum posts, etc.
-   notifications about step confirmations in the "Freelance" service
-   notifications about completed product publication steps in the Market, notifications about article and Code Base publications
-   notifications about new Market products, articles, free codes and Freelance orders
-   and much more

Next, go to Settings — Security, and enter your MetaQuotes ID.

![Configure notifications about MQL5.community events](/en/docs/mt5/client/img/options_notifications_community.png "Configure notifications about MQL5.community events")

### Sending Notifications via an MQL5 Application

The MQL5 language provides a special function [SendNotification](https://www.mql5.com/en/docs/network/sendnotification) which enables MQL5 applications to send push notifications to MetaQuotes ID specified in the platform settings. You can include notifications about any events in your code. If you do not have the required skills, you can order a program from a professional developer via the [Freelance](https://www.mql5.com/en/job) service.

### Sending Messages via the Alert Function

The trading platform allows creating [alerts](/en/docs/mt5/client/performing_deals#alert) to notify the user about market events. This feature is available in the Alerts tab of the Toolbox window. One of the event notification types is push notifications.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">There is a limitation on the number of messages sent: no more than 1 message per 0.5 second and no more that 10 messages per minute.</span></p></td></tr></tbody></table>

## Email [#](settings#mail)

Mailbox is configured on this tab. These settings will be then used to send message by the [Expert Advisor](/en/docs/mt5/client/trade_robots_indicators) command or by a triggered [alert](/en/docs/mt5/client/performing_deals#alert).

![Configure email notifications on the Email tab](/en/docs/mt5/client/img/options_email.png "Configure email notifications on the Email tab")

Configure the following parameters on this tab:

-   Enable — enable/disable the mailbox. If this option is disabled, all other settings are not available;
-   SMTP server — address of the SMTP server and port used. This server is used to send emails. The record must be made in the following format "\[server web address\] : \[port number\]". For example, "smtp.mail.ru:25", "smtp.gmail.com:465" etc.
-   SMTP login — a login for authentication on the mail server, usually it is an email address, for example, "your\_name@mail.net";
-   SMTP password — a password for authentication on the mail server (your mailbox password);
-   From — the email address, from which the message will be sent. Enter the name and address of the email account on the same mail server, the SMTP-protocol of which will be used. The name may also be missing. Example of this field: "your\_name, your\_name@mail.ru";
-   To — the email address, to which the messages will be sent. Name and address are also specified here, but the name may be omitted, for example: "any\_name, any\_mail@mail.net".

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Only one email address may be specified for either of fields "From" and "To". Several emails given with or without separators will not be accepted.</span></li><li class="p_tableatten"><span class="f_tableatten">The email password is stored in encrypted form.</span></li></ul></td></tr></tbody></table>

Click "Test" to send a test message using the settings specified. If the test is successful, click "OK" to apply these settings. If the test fails, it is recommended to check all settings again, restart the platform and resend a test message.

## FTP [#](settings#ftp)

The trading platform allows you to automatically publish [reports](/en/docs/mt5/client/performing_deals#trade_history) on the account state and its history. To do this, configure internet connection parameters through FTP.

![Sending reports can be configured on the FTP tab](/en/docs/mt5/client/img/options_publisher.png "Sending reports can be configured on the FTP tab")

The following parameters are available in this window:

-   FTP server — address of the FTP server the report will be sent to. For example, ftp.company.com;
-   FTP path — path to a directory on the FTP server where the reports will be placed. Specify the path relative to the root directory, for example: /inetpub/statements;
-   FTP login — login for authorizing on the FTP server;
-   FTP password — password for authorizing on the FTP server;
-   Passive mode — switching between active and passive mode. In the active mode, the trading platform accepts connection from the FTP server, in the passive mode the server accepts connection from the platform;
-   Test — use it to send a test report on the active account using the specified parameters. The test result is shown in a separate window;
-   Enable automatic publishing of reports via FTP — enable/disable publishing of reports. If you do not select this option, the remaining fields are not available;
-   Account — the account number you want to publish reports for. To publish reports, you need to be connected with this account;
-   Refresh every — periodicity of sending reports to the web server (in minutes).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">Reports are published for the currently active account only. If the account number specified in this tab does not correspond to the current one, reports will not be published.</span></li><li class="p_tableatten"><span class="f_tableatten">In the active mode, a free port (from dynamic range of 1024 to 65535) is allocated on the platform. The server connects to this port in order to set connection for data transmission. The FTP server connects to the client's port with the given number using TCP port 20 from its part to transfer data. In the passive mode, the server informs the client about the TCP port number (from the dynamic range of 1024 to 65535) to which the client can connect to set up data transfer.</span></li><li class="p_tableatten"><span class="f_tableatten">Report templates are located in the <a href="/en/docs/mt5/client/start_advanced/structure#templates" class="topiclink">/Templates</a> folder of the platform.</span></li></ul></td></tr></tbody></table>

## Community [#](settings#community)

The trading platform is tightly integrated with [MQL5.community](https://www.mql5.com/en "MQL5.community") — a community of MQL5 developers. The MQL5.community provides unique services for traders and developers:

-   The Market — the platform allows [purchasing](/en/docs/mt5/client/market_buy "Purchase the product at the Market tab") any ready-made application from the [MQL5 application store](https://www.mql5.com/en/market "Market on MQL5.community website") website. Before purchasing, you can download a trial version and test it in the [strategy tester](/en/docs/mt5/client/testing).
-   Signals — subscribe to the [trading signals](/en/docs/mt5/client/signals) of professional traders and receive them straight in your platform.
-   VPS — rent a [virtual platform](/en/docs/mt5/client/virtual_hosting) for 24/7 operation of copied signals and trading robots. A VPS can be rented directly from the platform and it does not require any additional setup on your side. Furthermore, the location of virtual servers ensures minimum delays in the execution of trading operations on the broker's server.
-   MQL5 Cloud Network [is a powerful distributed computing network](https://cloud.mql5.com/ "MQL5 Distributed Cloud Network") available for testing and optimization of Expert Advisors in the [Strategy Tester](/en/docs/mt5/client/testing). Thousands of optimization sessions can now be performed in minutes. In addition to using the network, you can provide your own computing capacities and [earn](/en/docs/mt5/client/mql5cloud_install "Take part in MQL5 Cloud Network") profit.
-   MQL5 Storage — personal storage of source codes integrated into the MetaEditor. Keep your code safe and access it from anywhere in the world. The MQL5 Storage features will be expanded soon to allow multiple users to remotely work on one project.
-   Freelance — if you cannot find the desired application in the Code Base or Market, order one from a professional developer in the [Freelance section](https://www.mql5.com/en/job "Freelance on MQL5.community") of MQL5.community website.
-   Code Base — [download](/en/docs/mt5/client/algotrading_get_ea_indicator#codebase "Download an application at the Code Base tab") any code published in the [Code Base](https://www.mql5.com/en/code "Code Base on MQL5.Community") of MQL5.community website. The code is automatically placed in the correct directory and compiled. You only need to run the application from the [Navigator](/en/docs/mt5/client/interface) window.
-   Articles — the extensive library of [MQL4/MQL5 programming articles](/en/docs/mt5/client/autotrading#articles) will help you learn how to create trading robots and technical indicators.
-   MQL5 Charts — a special service allowing to [post screenshots from the trading platform online](/en/docs/mt5/client/mql5_charts) and share them in popular social networks.

![MQL5.community](/en/docs/mt5/client/img/options_community.png "MQL5.community")

Enter your account details and get access to all the unique services of the MQL5.community:

-   Login — MQL5.community account.
-   Password — a password to the specified account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The password is stored on the hard drive in an encrypted form.</span></li><li class="p_tableatten"><span class="f_tableatten">If you do not have an MQL5.community account, please <a href="https://www.mql5.com/en/auth_register" target="_blank" class="weblink" title="Register at MQL5.community">register</a> and get access to unique opportunities.</span></li></ul></td></tr></tbody></table>

Link "register" opens the window of quick registration on MQL5.community.

![Traders community at MQL5.community provides useful services: application store, copy trading, hosting and freelance](/en/docs/mt5/client/img/mql5community_registration.png "Traders community at MQL5.community provides useful services: application store, copy trading, hosting and freelance")

Here, specify the desired username for your account, and e-mail. Once you click "Register", an account is created for you and an email with the account password is sent to the specified address.

To save resources and to optimize the platform working area, you can disable the MQL5 services which you do not use. For example, if you are not interested in [MQL5 programming languages](/en/docs/mt5/client/autotrading#articles) or in copy trading via the [Signals](/en/docs/mt5/client/signals) service, uncheck the relevant options in the settings to hide these sections. If you disable [Python integration](/en/docs/mt5/client/trade_robots_indicators#python) the relevant scripts will not be launched on charts.

## Signals [#](settings#signals)

Use this tab to configure the [Signals service](https://www.mql5.com/en/signals "Signals Service") in the trading platform.

The Signals service allows anyone to become a provider and sell trading signals or subscribe to them and follow the strategy of an experienced trader. Any traders can subscribe to the signals of another experienced trader ([Provider](/en/docs/mt5/client/signal_provider)) to copy his or her trade operations.

Find more about the service in the [Signals](/en/docs/mt5/client/signals) section.

![The Signals tab allows configuring automatic copying of trades on the account](/en/docs/mt5/client/img/options_signals.png "The Signals tab allows configuring automatic copying of trades on the account")

The name of the signal you are currently [subscribed](/en/docs/mt5/client/signal_subscriber) to is displayed at the top of the tab. If there is no subscription, the settings below are uneditable.

-   Agree to the terms of use of the Signals service — to start using the Signals service, agree to its [rules of use](https://www.mql5.com/en/signals/rules "Rules of Using the Signals Service"). Read the rules carefully. If you agree, check the box next to the option. If you do not agree with the rules, do not use the Signals service.
-   Enable realtime signal subscription — trading operations can be copied to your account only if this option is enabled. No operations will be copied to the account in case the option is disabled. The settings below will become editable only after enabling this option.
-   Copy Stop Loss and Take Profit levels — [Stop Loss](/en/docs/mt5/client/general_concept#stop_loss) and [Take Profit](/en/docs/mt5/client/general_concept#take_profit) placed at the provider's account will be also placed on your trading account if this option is enabled. These orders are executed at the broker's side. It means that they are executed regardless of whether the platform is running or not. Also, execution can be different for different brokers (if subscriber and provider have different brokers).  
    Therefore, copying of stop orders guarantees that a position will be closed upon reaching the specified profit and loss levels.
-   Synchronize positions without confirmations — automatic synchronization without additional confirmation. When subscribing to a signal, trading state of the Subscriber's and Provider's accounts are [synchronized](/en/docs/mt5/client/signal_subscriber#sync). This can be a primary synchronization when activating the subscription or [a re-synchronization](/en/docs/mt5/client/signal_subscriber#resync) during copying.  
    If pending orders or non-signal positions (opened manually or by an Expert Advisor) are detected at the Subscriber's account during synchronization, the dialog offering to close the positions and remove the orders is displayed. If during the [initial synchronization](/en/docs/mt5/client/signal_subscriber#sync), a provider account has floating (unfixed) profit, a user will see a dialog window offering to wait for better conditions to start copying. In both cases, synchronization is not performed and copying of signals is stopped until the user makes the decision by clicking the appropriate dialog button.  
    If the platform is working around the clock without constant external control (for example, runs on VPS), confirmation requests to perform synchronization are left unanswered and thus can prevent signals from being copied. When this option is enabled, synchronization is always performed automatically without the need for Subscriber's confirmation.

-   If there are custom positions/orders, they are left on the account, while the system starts/proceeds copying the Provider's trades.
-   If the Provider has a floating profit, the platform does not wait for better entry conditions and starts copying immediately.
-   Use no more than \[A\] % — percentage value of your deposit that can be used for following provider's signals. For example, if your balance is 10,000 USD and 90% is specified here, then 9,000 USD will be used for following the signals. This affects the calculation of volumes of the deals performed when following the signals. The volume is calculated proportionally. See ["Signal Subscribers"](/en/docs/mt5/client/signal_subscriber#trade) section for more information. It is strongly not recommended to change the deposit load if you already have positions opened according to a signal. This will lead to correction of volume of the open positions (volume increase or partial close at the current market price).
-   Stop if equity is less than \[B\] — this parameter allows you to limit losses when using trading signals. If equity drops below a specified level, copying of trade signals is automatically terminated, and all positions are closed. 0 means no limitations.
-   Deviation/Slippage \[C\] spreads — this setting is similar to deviation set when [orders are placed](/en/docs/mt5/client/performing_deals#position_open) from the platform. This is the value of the permissible deviation of the executed order price from the price initially requested by the platform when copying a trading operation. This value is displayed as a part of the current spread on the symbol used in trading operation.  
    The order is executed if the deviation is less or equal to the specified parameter. If the price deviation is greater than the specified value, operation is canceled. The next attempt to perform a trading operation will be carried out after a while.

[Deposits and withdrawals](/en/docs/mt5/client/payments)

[For Advanced Users](/en/docs/mt5/client/start_advanced)