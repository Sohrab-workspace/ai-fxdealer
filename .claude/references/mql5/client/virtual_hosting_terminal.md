# Working with the Virtual Platform

> Source: https://support.metaquotes.net/en/docs/mt5/client/virtual_hosting_terminal

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
            -   [Register a Server](/en/docs/mt5/client/virtual_hosting_server)
            -   [Migration](/en/docs/mt5/client/virtual_hosting_migration)
            -   [Working with the Virtual Platform](/en/docs/mt5/client/virtual_hosting_terminal)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)Working with the Virtual Platform

# Working with the Virtual Platform

The rented virtual server status can also be easily monitored from the trading platform. Use the Toolbox \\ VPS section to:

-   View [the virtual server data](/en/docs/mt5/client/virtual_hosting_terminal#details)
-   Synchronize the environment by performing the immediate [migration](/en/docs/mt5/client/virtual_hosting_migration#process)
-   Request the platform and Expert Advisor operation [journal](/en/docs/mt5/client/virtual_hosting_terminal#log)
-   [Stop the server](/en/docs/mt5/client/virtual_hosting_terminal#stop)
-   [Cancel hosting](/en/docs/mt5/client/virtual_hosting_terminal#cancel)

![Use the Toolbox \ VPS section to manage hosting](/en/docs/mt5/client/img/vps_manage.png "Use the Toolbox \ VPS section to manage hosting")

Further hosting actions are available via the MQL5.community profile:

-   [Canceling Hosting](/en/docs/mt5/client/virtual_hosting_terminal#cancel)
-   [Moving hosting to another trading account](/en/docs/mt5/client/virtual_hosting_terminal#move)
-   [Moving a virtual platform to another hosting server](/en/docs/mt5/client/virtual_hosting_terminal#move_server)
-   [Managing automated renewal](/en/docs/mt5/client/virtual_hosting_terminal#renewal)

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/SlKUjRISEfk/video.mp4" target="_blank" title="Watch video: How to control resources and manage subscriptions"><img class="help" alt="Watch video: How to control resources and manage subscriptions" title="Watch video: How to control resources and manage subscriptions" width="142" height="80" src="/en/docs/mt5/client/img/video_hosting_control.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: How to control resources and manage subscriptions</span></p><p class="p_fortable"><span class="f_fortable">Watch the video to learn how to analyze the virtual hosting resources report and how to control your subscriptions.</span></p></td></tr></tbody></table>

## Details [#](virtual_hosting_terminal#details)

All information about your virtual platform is presented in the left part of the window:

-   Hosting server name.
-   Ping in milliseconds displaying the network delay between the virtual server and the trade server of your broker. Information on how much ping on the virtual platform is less than that on the local one is also shown here. Lower network latency provides better condition for the execution of trading operations, such as reduced slippage and probability of getting re-quotes.
-   Trading account number for which hosting is registered, and the account holder name.
-   Selected subscription plan.
-   [Subscription auto renewal](/en/docs/mt5/client/virtual_hosting_terminal#renewal) status. Click on it to enable or to disable the option.
-   Subscription ID Click on it to navigate to the "Hosting section" of your MQL5.community profile. Your hosting subscription can be managed from this section: stop and start the server, cancel the subscription, move subscription to another trading account, enable/disable automatic renewal, move hosting to another server.
-   Subscription date.
-   Virtual server status: started, stopped. Hover over the status to view additional information about the virtual platform: the broker's access point to which the platform is connected, the status of connection to the broker's server, the state of the [Allow Push notifications](/en/docs/mt5/client/settings#notifications) option and current state.
-   Start/Stop commands to stop and launch the virtual platform. These commands are similar to stopping and starting the application. They do not affect the subscription.

### Performance [#](virtual_hosting_terminal#cpu)

This block features the configuration of the server, on which the virtual platform is running, as well as CPU, memory and hard disk usage graphs. Make sure that your program does not consume too much resources.

![Virtual platform and trading environment state](/en/docs/mt5/client/img/vps_state.png "Virtual platform and trading environment state")

## Environment

This section features information about the trading environment on the virtual platform: the number of launched charts, Expert Advisors and indicators.

-   Each Expert Advisor working on the virtual server is provided with information on the chart symbol and timeframe.
-   If a signal is running on the hosting, you can view its status right from here: whether copying of deals is enabled and whether the service is currently connected. To do this, hover over the signal name.

## Last migration

Information about the last data [migration](/en/docs/mt5/client/virtual_hosting_migration) and its type is shown here. Here you can also perform immediate synchronization of the current platform environment.

## Virtual Platform Logs [#](virtual_hosting_terminal#log)

To control the virtual platform operation, use the VPS \\ Journal section:

![Requesting the Journal from the virtual platform](/en/docs/mt5/client/img/vps_logs.png "Requesting the Journal from the virtual platform")

Logs are automatically requested from the hosting server when you scroll through the journal.

To access additional journal tools, click "Journal Viewer". In the newly opened log window, you can set a piece of text the journal entries are to be filtered by and a desired interval. After that, click Request to download the found logs. Here you can also select the journal type:

-   Terminal — logs about all events taking place in the platform including trade operations.
-   Experts — information about the Expert Advisor and indicator operation.

![Viewing Journal logs](/en/docs/mt5/client/img/vps_log_view.png "Viewing Journal logs")

The virtual platform logs are updated during each request and saved to \[platform data folder\]\\logs\\hosting.\*.terminal\\.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If a user requests too many records, only part of the first logs for the specified period are downloaded. This prevents performance degradation resulting from large logs. If you want to download further logs, you do not need to change the request period. Simply select the last line in the log viewer window and press PgDn.</span></p></td></tr></tbody></table>

## Stopping the Server [#](virtual_hosting_terminal#stop)

Stopping the server means the temporary shutdown of the virtual platform. This action is similar to closing the platform on your computer. It is performed by "![Stop Server](/en/docs/mt5/client/img/vh_stop_server_icon.png "Stop Server") Stop Server" command in the server context menu in the Navigator window or the "Start" button in the hosting section.

To launch the platform, execute the "![Start Server](/en/docs/mt5/client/img/vh_start_server_icon.png "Start Server")Start Server" or "Start" respectively.

## Canceling Hosting [#](virtual_hosting_terminal#cancel)

Hosting cancellation means that the virtual server will no be longer provided and the virtual platform will be completely deleted. All data transferred to hosting during migration will be completely removed, without the possibility to recover.

Refunds are made only if you cancel hosting within the first 24 hours after purchase. No refund is made if you cancel the subscription later. However, the unused hosting time will be credited to your MQL5 account in the form of free minutes. You can [rent a new VPS for free](/en/docs/mt5/client/virtual_hosting_server#tariff) using these minutes.

To cancel hosting, click on the subscription ID.

![Click on the ID to open the subscription management page](/en/docs/mt5/client/img/vps_identifier.png "Click on the ID to open the subscription management page")

In your MQL5.community profile, call up the subscription menu and click "Cancel":

![Subscription can be canceled from the Hosting section of the MQL5.community profile](/en/docs/mt5/client/img/vps_cancel.png "Subscription can be canceled from the Hosting section of the MQL5.community profile")

## Moving Hosting to Another Trading Account [#](virtual_hosting_terminal#move)

Virtual hosting is rented for a specific trading account, but it can be moved at any time. Open the "Hosting" section in your profile at MQL5.community.

Find the required subscription, click on the gear button and select "Move". Then specify a new trading account (login) and a new server (broker) if necessary, then click "Move".

![Moving hosting to another trading account](/en/docs/mt5/client/img/vh_move.png "Moving hosting to another trading account")

Open the trading platform and connect to the account, to which the hosting has been moved. Open Toolbox \\ VPS and [migrate your trading environment](/en/docs/mt5/client/virtual_hosting_migration).

## Moving a virtual platform to another hosting server [#](virtual_hosting_terminal#move_server)

The system automatically selects a virtual server with the minimum delay to your broker's server. However, connection figures may change over time, for example due to a change on broker's network infrastructure. In this case you can move the virtual platform to a hosting server with a better network connection.

Open the "Hosting" section in your profile at MQL5.community. Find the required subscription, click on the gear button and select "Change Server". Select the server with the smallest ping from the list and click "Move".

![A server can be changed under the Hosting section of the MQL5.community profile](/en/docs/mt5/client/img/vps_change_server.png "A server can be changed under the Hosting section of the MQL5.community profile")

After moving, navigate to Toolbox \\ VPS and [migrate the trading environment](/en/docs/mt5/client/virtual_hosting_migration).

## Managing automated renewal [#](virtual_hosting_terminal#renewal)

The [auto renewal](/en/docs/mt5/client/virtual_hosting_server#renewal) option eliminates the need to monitor your subscription status. As soon as the current hosting period expires, the system will automatically renew it at the same rate and using the same payment system that you used earlier.

You can enable or disable the auto renewal option at any time. To do this, click on the option status on the VPS page:

![To enable/disable auto renewal, click on the option status on the hosting page](/en/docs/mt5/client/img/vps_autorenew_platform.png "To enable/disable auto renewal, click on the option status on the hosting page")

You can also manage the option in the "Hosting" section of your MQL5.community profile:

![Automated renewal can be managed from the Hosting section of the MQL5.community profile](/en/docs/mt5/client/img/vps_autorenew.png "Automated renewal can be managed from the Hosting section of the MQL5.community profile")

[Migration](/en/docs/mt5/client/virtual_hosting_migration)

[Mobile Trading](/en/docs/mt5/client/mobile_trading)