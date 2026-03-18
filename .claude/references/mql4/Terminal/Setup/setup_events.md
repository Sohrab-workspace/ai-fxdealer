# Events

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/setup_events

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)Events

# Events

Signals of system events can be set up in the terminal (not to be mixed up with [alerts](/en/docs/mt4/terminal/overview/terminal/terminal_alerts)). It is a very convenient tool informing about changes in the terminal status. Signals can be set up in this tab. For this to be done, the "Enable" option must be enabled first. At that, a table containing the list of system events and corresponding actions will become active.

![options_events](/en/docs/mt4/terminal/img/options_events.png)

System events are:

-   Connect — connection to the server. Signal of successful connection to the server;
-   Disconnect — no connection to the server. Signal of interrupted connection to the server;
-   Email Notify — notifying by email. If this signal has triggered, it is recommended to check the ["Terminal — Mailbox" window](/en/docs/mt4/terminal/overview/terminal/terminal_mailbox);
-   Timeout — a certain time range is predefined for performing trade operations. If this range has been exceeded for some reason, the operation will not be performed, and this signal will trigger;
-   OK — trade operation has been successfully performed. No errors occurred when performing this operation;
-   News — receiving of news. If this signal has triggered, it is recommended to check the ["Terminal — News" window](/en/docs/mt4/terminal/overview/terminal/terminal_news);
-   Expert Advisor — this signal triggers when an [expert advisor](/en/docs/mt4/terminal/autotrading/experts) is performing a trade operation;
-   Alert — performing the Alert() function by an expert advisor;
-   Requote — price changed during preparation of a trade operation;
-   Trailing Stop — triggering of the [order of the same name](/en/docs/mt4/terminal/positions/trailing).

If there is a need to disable any of the signals, it is necessary to double-click on its name or icon with the left mouse button. Another double click will activate it again. After the signal has been triggered, the file specified in the "Action" field of the corresponding event will run. A double click on the file name allows to change the file. After double-clicking a pop-up list of available files to be assigned for the event will appear. You can also choose any other file by using the "Choose other..." item in the list. Selection of any file from this list and further Enter button pressing means that it is assigned to the corresponding event. To confirm all changes made, one has to press the "OK" button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Any file executable in the operation system can be assigned to the event.</span></p></td></tr></tbody></table>

[FTP](/en/docs/mt4/terminal/setup/setup_publisher)

[Community](/en/docs/mt4/terminal/setup/settings_mql5community)