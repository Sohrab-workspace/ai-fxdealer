# Terminal Settings

> Source: https://support.metaquotes.net/en/docs/mt5/manager/settings

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)Terminal Settings

# Terminal Settings

The Manager terminal provides multiple settings to help you conveniently customize your work in the development environment. To open the settings, select "![Options](/en/docs/mt5/manager/img/options_icon.png "Options") Options" in the [Tools](/en/docs/mt5/manager/main_menu#tools) menu (Ctrl+O).

![MetaTrader 5 Manager settings](/en/docs/mt5/manager/img/settings.png "MetaTrader 5 Manager settings")

All settings are grouped in several tabs based on what they do:

-   [Server](/en/docs/mt5/manager/settings#server) — general settings of the Manager terminal.
-   [Dealer](/en/docs/mt5/manager/settings#dealer) — dealer activity settings.
-   [Automation](/en/docs/mt5/manager/settings#automation) — setting up automatic processing of trade requests.
-   [Support](/en/docs/mt5/manager/settings#support) — authorization data for accessing [technical support](/en/docs/mt5/manager/tech_support) section.
-   [Events](/en/docs/mt5/manager/settings#events) — setting up notifications on various events in the terminal.

## Server [#](settings#server)

The Server tab contains the main settings of the terminal: parameters of connection, received news, etc.

![Server](/en/docs/mt5/manager/img/options_server.png "Server")

The following settings are available here:

-   Server — name of the trade server the Manager terminal connects to. You can specify the IP address and port number of the server, separated by a colon, instead of its name. For example: 192.168.0.1:443. Added servers become available for selection during [authorization](/en/docs/mt5/manager/connect).
-   Login — manager's account created on the server.
-   Password — password for connection to the server.
-   Change — [change](/en/docs/mt5/manager/settings#password) the account password.
-   Enable proxy server — allow using a proxy server when connecting to the server. If you enable this option, the Proxy... button becomes active.
-   Proxy — setup of connection through a [proxy server](/en/docs/mt5/manager/settings#proxy).
-   Keep personal settings and data at startup — save data of the account (login and password) to a hard drive after they are specified during authorization. When you restart the terminal, these data will be used to automatically connect to the server. If this option is disabled, then every time you start the terminal, you will need to enter these data manually. This option affects only the current account specified in the Login field.
-   Hide online users — when enabled, the [Online Users](/en/docs/mt5/manager/online_accounts) tab that displays currently connected accounts is hidden. The changes take effect only after the terminal is restarted.
-   Enable news — enable/disable [news](/en/docs/mt5/manager/toolbox#news). If this option is disabled, news are not received in the terminal.
-   News languages — sort news by their language. When you click Edit, the [news language](/en/docs/mt5/manager/settings#news_language) selection dialog appears. If "Any language" is set here, then all news will be received in the terminal, regardless of their language.
-   Save files to — directory files are sent to via the [internal email system](/en/docs/mt5/manager/communication#mail). When you open an attached file, the terminal checks its extension and the correspondence of file contents to this extension. If the file type is allowed and its contents is checked, the terminal will open the file and save it to the specified directory. Otherwise, a warning is displayed, notifying that the file may harm the computer, and the file is not saved. The following file types are allowed: PNG, JPG/JPEG, BMP, ZIP, 7Z, GIF, DOC, XLS, DOCX, XSLX, ODT, RTF, CSV, TXT and LOG.  
    If a file with the same name and a different content exists in the directory, the manager's login and email arrival date/time up to a second will be added to the saved file name: \[login\]-\[file name\]-\[date and time\].\[extension\]. For example, the log file 20170501.log will be saved as 1001-20170501-20170502-170038.log.  
    By default, files are saved to C:\\Users\\\[Windows username\]\\Downloads\\MetaTrader. You can change the directory by clicking Browse.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">It is strongly recommended not to change the settings of server connection without any special need.</span></p></td></tr></tbody></table>

### Changing a password [#](settings#password)

To change the account password, click Edit on the Server tab.

![Changing the password](/en/docs/mt5/manager/img/change_password.png "Changing the password")

The following details are to be indicated in the password changing dialog:

-   Current password — field for entering the current master password;
-   New password — field for entering a new password;
-   Confirm — field for a repeated entering of the new password, to avoid errors.

The login cannot be changed. The password can only be changed for the currently connected account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><ul><li class="p_tableatten"><span class="f_tableatten">A password cannot be changed if the current password is not specified.</span></li><li class="p_tableatten"><span class="f_tableatten">A password should be complex enough: at least two of the three types of representation (lowercase letters, capital letters or digits) and not shorter than required in the password change dialog. The minimum number of characters in the password is determined on the trade server.</span></li></ul></td></tr></tbody></table>

### Proxy server setup [#](settings#proxy)

A proxy server is an intermediate link between the manager's computer and the trade server. It is mostly used by internet providers or by local networks. If you have any [connection](/en/docs/mt5/manager/connect) problems, contact your system administrator or ISP. If you use a proxy server, configure the terminal accordingly. Activate "Enable proxy server" option on the Server tab and click Proxy...

![Proxy server](/en/docs/mt5/manager/img/proxy_server.png "Proxy server")

Specify the following parameters:

-   Server — IP address and port separated by a colon. Select the proxy server type to the right of the field: HTTP, SOCKS4 or SOCKS5. In HTTP mode, NTLM authentication is also supported.
-   Login — login to access a proxy server. If no login is required, leave it blank.
-   Password — password to access a proxy server. If no password is required, leave it blank.

Click Test.. to verify proxy server settings. If the settings are correct, you will see a corresponding message.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable" style="vertical-align:middle;"><p class="p_tableatten"><span class="f_tableatten">Consult your system administrator or internet provider for proxy setup details.</span></p></td></tr></tbody></table>

### News language selection [#](settings#news_language)

You can use the languages of [news](/en/docs/mt5/manager/toolbox#news) in the terminal. To do this, click Change in front of the "News languages" on the Server tab.

![News language selection](/en/docs/mt5/manager/img/news_language.png "News language selection")

The left part of the window contains available languages, the right part — selected ones. To add a language, double-click on it in the left part, or select it and click Add. To delete a language, use the Remove button. To reset to initial settings, click Reset.

If "Any language" is set in the "News language" field, then all the news will be received in the terminal, regardless of their language.

## Support [#](settings#support)

On this tab, enter information about your account on the MetaQuotes Software Corp. technical support website. This is necessary to access the [technical support](/en/docs/mt5/manager/tech_support) section: news, articles, documentation, Service Desk, etc.

![Support](/en/docs/mt5/manager/img/options_support.png "Support")

These data will be used for contacting technical support directly from the Manager terminal.

## Dealer [#](settings#dealer)

This tab contains settings of the manager terminal that refer to [dealing](/en/docs/mt5/manager/dealing).

![Dealer](/en/docs/mt5/manager/img/options_dealer.png "Dealer")

The following settings are available here:

-   Automatic dealer connections — connect a dealer automatically after [authorization](/en/docs/mt5/manager/connect) on the server. To be able to [process](/en/docs/mt5/manager/dealing) incoming trade requests of clients, a manager should execute the "![Start Dealing](/en/docs/mt5/manager/img/start_dealing_icon.png "Start Dealing") Start Dealing" command. If you enable this option, this operation will be executed automatically when connecting to the server.
-   Throw in prices at request answer — when enabled: if the dealer confirms a trade request, the price, at which a dealer has confirmed it, will be automatically thrown in to the price flow before that. The same option can be enabled/disabled by command ![Throw in prices at request answer](/en/docs/mt5/manager/img/correct_prices_button.png "Throw in prices at request answer") on the [toolbar](/en/docs/mt5/manager/toolbar).
-   Force switch to dealer window on new request — when enabled: switch to the [dealer window](/en/docs/mt5/manager/dealing) when a new trade request is received.
-   Answer timeout — number of seconds a dealer has to answer to client's trade request. If the dealer does not answer within the specified time, the request is rejected automatically. The remaining time is displayed in the quoting field of the [Dealer](/en/docs/mt5/manager/dealing) section. The default value is 150 seconds. The valid range of values: 20-180 seconds.
-   Disconnect dealer after \[x\] automatic rejects — if a dealer does not process a client's trade request during the time specified in "Answer timeout", the request is automatically rejected. The parameter sets how many requests should be automatically rejected in a row before the manager account is disconnected from processing trade requests (disconnected as a dealer). If 0 value is set, the dealer is not disconnected.

## Automations [#](settings#automation)

The Manager terminal allows automatically process certain types of trade requests received from clients. On this tab, you can set up the types of requests processed automatically, and enable or disable automation.

![Automations](/en/docs/mt5/manager/img/options_automation.png "Automations")

Using Enable option, you can enable or disable automatic processing of requests. The same action can be performed by selecting "![Automations](/en/docs/mt5/manager/img/automation_button.png "Automations") Automation" on the toolbar.

To enable the processing of a request, it should be ticked ![Enabled](/en/docs/mt5/manager/img/enabled_icon.png "Enabled"). Requests that will not be processed, are marked with a cross ![Disabled](/en/docs/mt5/manager/img/disabled_icon.png "Disabled").

In the "Maximal volume" column, specify the maximal request volume that can be processed automatically. Requests with a larger volume should be processed manually. Zero means unlimited volume.

Automatic processing of the following types of requests is available:

-   Request Quotes — request of quotes in the Request [execution mode](/en/docs/mt5/manager/trade_principles#execution_type).
-   Confirm Requests — confirm execution of an [order](/en/docs/mt5/manager/trade_principles#market_order) at the price that a trader has received from a dealer in the Request execution mode.
-   Instant Order — confirmation of an order in the instant execution mode.
-   Market Order — confirmation of an order in the market execution mode.
-   Exchange Order — confirmation of an order in the exchange execution mode.
-   Close By Order — confirmation of an order to close a position using an opposite one.
-   Place Pending Order — placing a [pending order](/en/docs/mt5/manager/trade_principles#pending_order).
-   Modify Position (S/L, T/P) — request to change levels of [stop loss](/en/docs/mt5/manager/trade_principles#stop_loss) or [take profit](/en/docs/mt5/manager/trade_principles#take_profit).
-   Modify Pending Order — request to [modify](/en/docs/mt5/manager/orders#modify_delete) a pending order.
-   Delete Pending Order — request to [delete](/en/docs/mt5/manager/orders#modify_delete) a pending order.
-   Activate Pending Order — [activation](/en/docs/mt5/manager/orders#activate) of a pending order upon the occurrence of conditions specified in the order.
-   Activate Stop Loss — activation of an order to close a position when reaching a stop loss level.
-   Activate Take Profit — activation of an order to close a position when reaching the take profit level.
-   Activate Stop Limit Order — activation of Buy Stop Limit or Sell Stop Limit;
-   Delete Stopout Pending Order — delete a pending order when a client reaches the [stop out](/en/docs/mt5/manager/margin_calls#stopout_processing) level. Only orders with margin requirements (margin is reserved when placing an order) are to be deleted;
-   Close Stopout Position — close a position when a client reaches the [stop out](/en/docs/mt5/manager/margin_calls#stopout_processing) level.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Automatic processing is carried out only if the current account is <a href="/en/docs/mt5/manager/dealing" class="topiclink">connected as a dealer</a>.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">To prevent uncontrolled execution of requests, automation is set to disabled each time the terminal is restarted.</span></li></ul></td></tr></tbody></table>

## Events [#](settings#events)

On the Events tab, you can configure audio alerts about various events appearing in the Manager terminal.

![Events](/en/docs/mt5/manager/img/options_events.png "Events")

All events are accompanied by a sound file played when the event occurs. Notifications of the following events are available:

-   Connect — successful connection to the server.
-   Disconnect — loss of connection with the server.
-   Email Notify — incoming [email](/en/docs/mt5/manager/communication#mail).
-   Timeout — time is out. Certain time is given for the performance of certain operations (for example, data request from the server or update of settings). If during this period for whatever reason, the operation had not been made, the alert will trigger.
-   Ok — operation successful.
-   News — incoming [news](/en/docs/mt5/manager/toolbox#news).
-   Request — notification about a new request received from a client (request for prices, buy and sell trade requests, placing pending orders, 'close by' requests).
-   Modify Order — modification of [stop loss](/en/docs/mt5/manager/trade_principles#stop_loss)/[take profit](/en/docs/mt5/manager/trade_principles#take_profit) levels of a position, modification or deletion of a pending order.
-   SL / TP — activation of stop loss/take profit levels.
-   Pending Order — [activation of a pending order](/en/docs/mt5/manager/orders#activate).
-   Stopout — [closing of a position](/en/docs/mt5/manager/positions#close) or deletion of an order by stop out.

To disable an alert, left-click on its icon ![Enabled Alert](/en/docs/mt5/manager/img/event_enabled_icon.png "Enabled Alert") or double-click its name. After that, the icon changes to ![Disabled Alert](/en/docs/mt5/manager/img/event_disabled_icon.png "Disabled Alert"). To activate an alert, repeat the same operation.

To change a file played when the alert arrives, double-click its name or select it and press Enter. Then select "Choose other" from the drop-down list and specify the necessary file.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">By default, you are offered to choose a sound file with the *.wav extension, but you can specify any file type for the alert. If a *.wav file is selected, it is played when the alert triggers. If you select any other file, it is opened using the application it is associated with in the operating system.</span></p></td></tr></tbody></table>

## Confirmations [#](settings#confirmations)

From this section, you can enable or disable additional confirmation requests for dangerous actions executed via the Manager terminal.

The dangerous actions include:

-   Moving configurations via drag'n'drop (to protect against accidental actions)
-   Deleting records from databases

When performing any of these actions, the terminal requests additional confirmation. Confirmations can be disabled for experienced administrators, or when performing a large platform reconfiguration.

![Configuring confirmation of dangerous actions](/en/docs/mt5/manager/img/options_confirmations.png "Configuring confirmation of dangerous actions")

The confirmation is always requested for actions applied to 10 or more entries.

[Connecting to the Server](/en/docs/mt5/manager/connect)

[For Advanced Users](/en/docs/mt5/manager/beginning_advanced)