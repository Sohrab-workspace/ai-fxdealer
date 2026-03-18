# Alerts

> Source: https://support.metaquotes.net/en/docs/mt4/multiterminal/analytics/ug_alerts

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
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
        -   [Getting Started](/en/docs/mt4/multiterminal/getting_started)
        -   [Client Accounts](/en/docs/mt4/multiterminal/accounts)
        -   [Trading](/en/docs/mt4/multiterminal/trading)
        -   [Analytics](/en/docs/mt4/multiterminal/analytics)
            -   [News](/en/docs/mt4/multiterminal/analytics/ug_news)
            -   [Alerts](/en/docs/mt4/multiterminal/analytics/ug_alerts)
        -   [User Interface](/en/docs/mt4/multiterminal/user_interface)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MultiTerminal](/en/docs/mt4/multiterminal)[Analytics](/en/docs/mt4/multiterminal/analytics)Alerts

# Alerts

Alerts tab contains information about created alerts. The alerts are intended for signaling about events in the market. Having created alerts, one may leave the monitor as the multiterminal will automatically inform about the server events.

All alerts in this tab are represented as a table with the following fields:

-   Symbol — security, the data on which are used to check for the condition specified. If the "Time=" parameter (alert triggering at the pre-defined time) was selected as a condition, the symbol does not matter;
-   Condition — condition under which the alert will trigger. The following can be used as such a condition:

-   -   Bid> — the Bid price is higher than the specified value. If the current Bid price exceeds the given value, the alert will trigger;
    -   Bid< — the Bid price is lower than the specified value. If the current Bid price goes under the given value, the alert will trigger;
    -   Ask> — the Ask price is higher than the specified value. If the current Ask price exceeds the given value, the alert will trigger;
    -   Ask< — the Ask price is lower than the specified value. If the current Ask price goes under the given value, the alert will trigger;
    -   Time= — time is equal to the given value. As soon as this time comes, the alert will trigger.

-   Counter — the amount of alert triggerings;
-   Limit — maximum permissible amount of the alert triggerings. Having triggered this given amount of times, the alert will stop triggering;
-   Timeout — the period of time between alert triggerings;
-   Event — the action to be performed. This can be an audio signal, a file executable in operational environment, or a message sent by email.

## Alerts Management

The following context menu commands are intended for managing alerts:

-   Create — create a new alert. The same action can be performed by pressing the Insert key;
-   Modify — edit the alert. The same action can be performed by double-clicking on the alert name in the table or by pressing the Enter key;
-   Delete — delete the alert. This action can also be performed by pressing the Delete key;
-   Enable / Disable — enable/disable the alert. The alert will not be deleted when disabled, but it stops to trigger. It can be enabled later. The same action can be performed by pressing the Space key or enabling in the alert setup window (described below).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: To manage alerts with the keyboard, one should activate this window first. To do so, it is necessary to click with the left mouse button in the window.</span></p></td></tr></tbody></table>

One can start modifying an alert by double-clicking of the left mouse button in the alert information line. In this case, as well as at execution of the "Modify" and "Create" context menu commands, the alert editor window will appear:

-   Enable — alert on/off. When the alert is off, it is not deleted, but it will stop functioning. This option is similar to the "Enable On/Off" context menu command and pressing of the Space key;
-   Action — assign an action to be performed when an event happens: play a sound, run a file, or send an email.  
    When playing a sound or running a file, one should specify the corresponding files. At sending a message, one should specify the topic and text of the message;
-   Symbol — security, the values of which will be used to check the condition;
-   Condition — condition ("Time=", "Bid<", "Bid>", "Ask<", "Ask>") under which the alert will trigger;
-   Value — check the value of the condition. If the symbol price is equal to this value, the alert will trigger;
-   Source — the alert. When a sound is played or a file is run, one should specify the path to the corresponding file. When a message is sent by email, one should input the message. It must be noted that one should set up [email parameters](/en/docs/mt4/multiterminal/getting_started/ug_setup#email) for sending message;
-   Timeout — the time period between alert triggerings;
-   Maximum iterations — maximum amount of times the alert triggering repeats.

The "Test" button allows to check the usability of the selected alert. For changes to come into effect, one must press the "OK" button.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: To send messages about events happened, one has to set up mailbox parameters in the <a href="/en/docs/mt4/multiterminal/getting_started/ug_setup#email" class="topiclink">program settings</a>.</span></p></td></tr></tbody></table>

[News](/en/docs/mt4/multiterminal/analytics/ug_news)

[User Interface](/en/docs/mt4/multiterminal/user_interface)