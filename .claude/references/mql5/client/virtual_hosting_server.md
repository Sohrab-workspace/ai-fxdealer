# Register a Server

> Source: https://support.metaquotes.net/en/docs/mt5/client/virtual_hosting_server

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)Register a Server

# Register a Server

To receive a virtual platform, connect using the appropriate trading account, open the context window of the [Navigator](/en/docs/mt5/client/interface) and execute "![Register a virtual server](/en/docs/mt5/client/img/vh_icon.png "Register a virtual server") Register a Virtual Server" command.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/yd3ar2y0pCo/video.mp4" target="_blank" title="Watch video: How to rent a virtual platform"><img class="help" alt="Watch video: How to rent a virtual platform" title="Watch video: How to rent a virtual platform" width="142" height="80" src="/en/docs/mt5/client/img/video_hosting_rent.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: How to rent a virtual platform</span></p><p class="p_fortable"><span class="f_fortable">A detailed how-to description that will help you to rent a virtual hosting directly from a trading platform. It is easy: choose the nearest server and payment plan to let your robots and signals run 24 hours a day.</span></p></td></tr></tbody></table>

![Registering a virtual server](/en/docs/mt5/client/img/vh_allocate_start.png "Registering a virtual server")

This will open the VPS section, and the system will automatically select the server that is closest to your broker. The network connection improvements will be shown in the left part of the window: the system will provide the comparison of network delays between your terminal on the hosting server and the broker server, and between your local and the broker server. Lower network latency provides better condition for the execution of trading operations, such as reduced slippage and probability of getting re-quotes.

![Read the terms of hosting and select a subscription](/en/docs/mt5/client/img/vps_rent.png "Read the terms of hosting and select a subscription")

In order to rent a virtual platform, you need to have a valid MQL5.community account. If your MQL5 account is not specified in the [trading platform settings](/en/docs/mt5/client/settings#community), you will be prompted you to add one.

## Hosting Plans [#](virtual_hosting_server#tariff)

Select a suitable hosting plan: longer rental periods are more cost-efficient.

The following plans can also be available:

-   Free — free hosting rental for unused time. This option appears if you [cancel](/en/docs/mt5/client/virtual_hosting_terminal#cancel) a previously rented VPS. In this case, unused hosting time is credited to your MQL5 account. This time can be used to rent a new VPS.
-   Sponsored — free hosting; the rental is paid by your broker. The availability of this option depends on your broker. Please contact your broker to find out how you can rent a VPS for free.

You can change the selected service plan only after the rental period expires.

## Auto Renewal [#](virtual_hosting_server#renewal)

If you want the rental period to be renewed with the same payment plan after subscription expiration, enable the option "Automatically renew subscription with sufficient funds and terminal activity".

With this option, you can be sure that your Expert Advisors and signal subscriptions will not stop due to the end of the VPS period. You do not have to monitor the subscription period, while the system will automatically renew it.

If the VPS subscription expires, your hosting data will be completely deleted from the server. You can manually rent it again, but in this case you will have to configure the entire environment anew. The auto renewal option helps avoid this issue.

Auto renewal is performed using the same payment method which was used for the first subscription purchase. If you paid for the subscription with your card, the system will use this card. If payment with the same card cannot be made, the fee will be charged from your MQL5 account.

To protect you from unnecessary payments for inactive hosting subscriptions, the system checks the hosting state during auto renewal. If hosting was [stopped](/en/docs/mt5/client/virtual_hosting_terminal#stop), the subscription will not be renewed.

Attempts to auto-renew your hosting start early, in case something goes wrong. The day before the expiration date, the system will attempt to charge the corresponding payment. If the renewal fails, you will receive a notification to the email specified in your MQL5 account. The new rental period will start after the expiration of the current period, not when the renewal is actually charged.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">You can <a href="/en/docs/mt5/client/virtual_hosting_terminal#renewal" class="topiclink">enable or disable</a> the auto renewal option at any moment.</span></li><li class="p_tableatten"><span class="f_tableatten">A VPS subscription can only be renewed automatically — manual mode is not supported.</span></li></ul></td></tr></tbody></table>

## Payment [#](virtual_hosting_server#payment)

At the last step, select a payment system.

![Select a payment system](/en/docs/mt5/client/img/vps_pay.png "Select a payment system")

To pay for the hosting subscription from your MQL5.community account balance, select the MQL5 option. If you do not have enough money on your account, you do not necessarily need to go to the site and add money to your account. A payment for the hosting subscription can be transferred directly through one of the payment systems. Select any of the available options and follow the system instructions to complete the payment. To maintain a clear and unified history of rented virtual servers, the required amount is first transferred to your MQL5.community account, from which an appropriate payment is made.

![After the payment, the VPS is ready to use](/en/docs/mt5/client/img/vps_ready.png "After the payment, the VPS is ready to use")

After paying for the VPS subscription, you can migrate the platform environment to the virtual server immediately. Select the desired [migration type](/en/docs/mt5/client/virtual_hosting_migration#process) and click "Migrate". If the platform is not ready for migration, you can perform it later.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">By renting the Virtual Hosting service, you agree to <a href="https://www.mql5.com/en/hosting/rules" target="_blank" class="weblink" title="Rules of Using the Virtual Hosting Service">the service rules</a>. Read them carefully.</span></p></td></tr></tbody></table>

[Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)

[Migration](/en/docs/mt5/client/virtual_hosting_migration)