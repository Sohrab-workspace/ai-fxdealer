# Events

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administrator/settings/settings_events

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
        -   [Getting Started](/en/docs/mt5/platform/administrator/getting_started)
        -   [User Interface](/en/docs/mt5/platform/administrator/interface)
        -   [Terminal Settings](/en/docs/mt5/platform/administrator/settings)
            -   [Common](/en/docs/mt5/platform/administrator/settings/settings_common)
            -   [Support](/en/docs/mt5/platform/administrator/settings/settings_support)
            -   [Events](/en/docs/mt5/platform/administrator/settings/settings_events)
            -   [Confirmations](/en/docs/mt5/platform/administrator/settings/settings_confirmations)
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
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Administrator](/en/docs/mt5/platform/administrator)[Terminal Settings](/en/docs/mt5/platform/administrator/settings)Events

# Events

At the "Events" tab you can set up the sound notifications about different events occurring in the administrator terminal.

![Events](/en/docs/mt5/platform/img/settings_events.png "Events")

All the events are displayed in the form of a table that contains their names and the sound files (on default) that are played when they occur. The following types of events are represented here:

-   Connect — signal of successful connection to a server;
-   Disconnect — signal of loosing connections with a server;
-   Email Notify — signal of receiving a message via the [mail system](/en/docs/mt5/platform/administration/mail);
-   Timeout — a certain time range is predefined for performing different operations (for example, requesting data from a server or refreshing the settings). If this range has been exceeded for some reason, the operation will not be performed, and this signal will trigger;
-   Ok — signal of a successfully performed operation;
-   News — signal of received [news](/en/docs/mt5/platform/administrator/interface/toolbox/toolbox_news).

If there is a need to disable any of the signals, it is necessary to double-click on its icon ![Enabled Event](/en/docs/mt5/platform/img/event_enabled_icon.png "Enabled Event") or double-click on its name. After that the icon will change to ![Disabled Event](/en/docs/mt5/platform/img/event_disabled_icon.png "Disabled Event"). To enable a signal the same operation must be performed.

In order to change a file played at the signal activation, double-click on its name or select it and press the "Enter" key. After that click "Choose other..." in the pop-up list and indicate the necessary file in the appeared window.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">By default a file with *.wav extension is offered as a sound. However, another file can be indicated as a signal. If a *.wav file is selected, at the event triggering the file will be played. If another file is selected, it will be opened using application it is associated with in the operating system.</span></p></td></tr></tbody></table>

For changes to take effect the "OK" button should be pressed.

[Support](/en/docs/mt5/platform/administrator/settings/settings_support)

[Confirmations](/en/docs/mt5/platform/administrator/settings/settings_confirmations)