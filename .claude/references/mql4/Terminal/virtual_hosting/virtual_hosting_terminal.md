# Working with the Virtual Terminal

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal

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
        -   [Analytics](/en/docs/mt4/terminal/analytics)
        -   [Trading](/en/docs/mt4/terminal/positions)
        -   [Auto Trading](/en/docs/mt4/terminal/autotrading)
        -   [Tools](/en/docs/mt4/terminal/service)
        -   [Articles](/en/docs/mt4/terminal/articles)
        -   [Signals](/en/docs/mt4/terminal/signals)
        -   [Market](/en/docs/mt4/terminal/market)
        -   [Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)
            -   [Registering Server](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_server)
            -   [Migration](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration)
            -   [Working with Terminal](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)Working with Terminal

# Working with the Virtual Terminal

The rented virtual server status can also be easily monitored from the client terminal. The server's context menu in Navigator window allows you to:

-   View [the virtual server data](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal#details).
-   Synchronize the environment by performing the immediate [migration](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration#process).
-   Request terminal and Expert Advisor operation [journal](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal#log).
-   [Stop the server](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal#stop).
-   [Cancel the hosting](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal#cancel).

![Viewing the virtual server data](/en/docs/mt4/terminal/img/vh_details.png "Viewing the virtual server data")

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/SlKUjRISEfk/video.mp4" target="_blank" title="Watch video: How to Control Resources and Manage Subscriptions"><img class="help" alt="Watch video: How to Control Resources and Manage Subscriptions" title="Watch video: How to Control Resources and Manage Subscriptions" width="142" height="80" src="/en/docs/mt4/terminal/img/video_hosting_control.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: How to Control Resources and Manage Subscriptions</span></p><p class="p_fortable"><span class="f_fortable">How to analyze the virtual hosting resources report and how to control your subscriptions - we show you in this video.</span></p></td></tr></tbody></table>

## Details [#](virtual_hosting_terminal#details)

To view the virtual server data, click ![Details](/en/docs/mt4/terminal/img/vh_details_icon.png "Details") Details in its context menu. The information is presented in several tabs.

### Details

![Details](/en/docs/mt4/terminal/img/vh_details_details.png "Details")

The following information is displayed here:

-   Hosting server name and your virtual terminal ID.
-   Ping in milliseconds displaying the network delay between the virtual server and a trade server of your broker.
-   Virtual server status: started, stopped. Here you can also enable/disable the virtual server and cancel the rent.
-   The service plan selected when [registering the server](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_server#tariff).
-   Registration date, MQL5.community account registration is performed to and the account's current balance.
-   Last synchronization date and its [type](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration#process). Here you can also perform immediate synchronization of the current terminal environment.

### CPU Usage [#](virtual_hosting_terminal#cpu)

![CPU usage graph](/en/docs/mt4/terminal/img/vh_details_cpu.png "CPU usage graph")

CPU usage graph is displayed here in percentage terms.

### Memory Usage [#](virtual_hosting_terminal#ram)

![Memory usage graph](/en/docs/mt4/terminal/img/vh_details_memory.png "Memory usage graph")

Memory usage graph is displayed here.

### Hard Disk Usage [#](virtual_hosting_terminal#hdd)

![Hard disk space usage graph](/en/docs/mt4/terminal/img/vh_details_hdd.png "Hard disk space usage graph")

Hard disk space usage is displayed here.

## Virtual Terminal Journal [#](virtual_hosting_terminal#log)

You can view the virtual terminal's journal to control its operation.

![Requesting the Journal from the Virtual Terminal](/en/docs/mt4/terminal/img/vh_log_request.png "Requesting the Journal from the Virtual Terminal")

In the newly opened log window, you can set a piece of text the journal entries are to be filtered by and a desired interval. After that, click Request to download the found logs. Here you can also select the journal type:

-   Terminal — logs about all events taking place in the terminal including trade operations.
-   Experts — data on Expert Advisor and indicator operation.

![Viewing Journal logs](/en/docs/mt4/terminal/img/vh_log_view.png "Viewing Journal logs")

The virtual terminal's logs are updated during each request and saved to \[terminal data folder\]\\logs\\hosting.\*.terminal\\.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If a user requests too many records, then only part of the first logs for the specified period will be downloaded. This prevents performance degradation resulting from large logs. If you want to download further logs, you don't need to change the request period. Simply select the last line in the log viewer window and press PgDn.</span></p></td></tr></tbody></table>

## Stopping the Server [#](virtual_hosting_terminal#stop)

Stopping the server means the temporary shutdown of the virtual terminal. This action is similar to closing the terminal on PC. It is performed by ![Stop Server](/en/docs/mt4/terminal/img/vh_stop_server_icon.png "Stop Server") "Stop Server" command in the server context menu of the Navigator window.

To launch the terminal, execute ![Start Server](/en/docs/mt4/terminal/img/vh_start_server_icon.png "Start Server") "Start Server" command.

## Canceling the Hosting [#](virtual_hosting_terminal#cancel)

Hosting cancelation means the virtual server is no longer provided and the virtual terminal is completely deleted with all data moved to it during the migration

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">No refund is made. The rental pay can be returned only within 24 hours after the virtual server has been registered.</span></p></td></tr></tbody></table>

To cancel the hosting, execute ![Cancel Hosting](/en/docs/mt4/terminal/img/vh_cancel_hosting_icon.png "Cancel Hosting") "Cancel Hosting" command in the server context menu of the Navigator window.

## Moving Hosting to Another Trading Account [#](virtual_hosting_terminal#move)

Virtual hosting is rented for a specific trading account, but it can be moved at any time. Open the "Hosting" section in your profile at MQL5.community.

Find the required subscription, click on the gear button and select "Move". Then specify a new trading account (login) and a new server (broker) if necessary, then click "Move".

![Moving hosting to another trading account](/en/docs/mt4/terminal/img/vh_move.png "Moving hosting to another trading account")

Open the trading platform and connect to the account, to which the hosting has been moved. Using the account context menu in the Navigator window, start the server and [migrate your trading environment](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration).

[Migration](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration)

[MetaEditor](/en/docs/mt4/metaeditor)