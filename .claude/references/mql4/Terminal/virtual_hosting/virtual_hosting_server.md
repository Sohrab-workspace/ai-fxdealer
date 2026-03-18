# Registering Server

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_server

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)Registering Server

# Registering Server

To receive a virtual terminal, connect by the appropriate trading account, open the context window of the [Navigator](/en/docs/mt4/terminal/overview/navigator) and execute ![Register a Virtual Server](/en/docs/mt4/terminal/img/vh_icon.png "Register a Virtual Server") "Register a Virtual Server" command.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/yd3ar2y0pCo/video.mp4" target="_blank" title="Watch video: How to Rent A Virtual Platform"><img class="help" alt="Watch video: How to Rent A Virtual Platform" title="Watch video: How to Rent A Virtual Platform" width="142" height="80" src="/en/docs/mt4/terminal/img/video_hosting_rent.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: How to Rent A Virtual Platform</span></p><p class="p_fortable"><span class="f_fortable">Detailed how-to description that will help to rent a virtual hosting directly from a trading platform. Its simple: choose nearest server and payment plan in order to let your robots and signals work for 24 hours a day.</span></p></td></tr></tbody></table>

![Registering a virtual server](/en/docs/mt4/terminal/img/vh_allocate_start.png "Registering a virtual server")

The Virtual Hosting wizard will automatically select the server that is closest to your broker. In the wizard window, you will see how ping (network latency) will decree compared to your current connection. Lower network latency between your platform and the broker's server provides better condition for the execution of trading operations, such as reduced slippage and probability of getting re-quotes.

Select the appropriate plan and click "Next". Service plan conditions are defined by hosting companies.

![The Virtual Hosting wizard automatically selects the server that is closest to your broker.](/en/docs/mt4/terminal/img/vh_wizard.png "The Virtual Hosting wizard automatically selects the server that is closest to your broker.")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">You can change the selected service plan after the rental period expires.</span></p></td></tr></tbody></table>

If your MQL5 account is not specified in the [trading platform settings](/en/docs/mt4/terminal/setup/settings_mql5community), the Virtual Hosting wizard will prompt you to add one. In order to rent a virtual platform, you need to have a valid MQL5.community account. You can register account right away if you do not have any.

![Enter your MQL5 account or register](/en/docs/mt4/terminal/img/vh_mql5account.png "Enter your MQL5 account or register")

Click "Next" and check all the data: the trading account, for which you are going to rent a virtual hosting, as well as the cost of subscription.

![Checking data and hosting rental confirmation](/en/docs/mt4/terminal/img/vh_wizard_confirm.png "Checking data and hosting rental confirmation")

To continue, you should agree with the [Virtual Hosting service rules](https://www.mql5.com/en/hosting/rules "Rules of Using the Virtual Hosting Service"). Read them carefully.

If you want the rental period to be renewed after its expiration with the same service plan, enable the option "Automatically renew subscription with sufficient funds and terminal activity". The renewal can be performed only if there are enough funds on your MQL5.community account to pay for the rent and the [rented server is running](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_terminal).

After clicking Next, the server rent process is finished and the appropriate payment is deducted from your account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If the rent is canceled by a user, no refund is made.</span></p></td></tr></tbody></table>

![Completion of the server registration](/en/docs/mt4/terminal/img/vh_wizard_finish.png "Completion of the server registration")

You can move the terminal environment to the virtual server immediately. Select the necessary [migration type](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration#process) and click "Migrate now". If the terminal is not prepared yet, click Finish to perform migration later.

## Paying for Virtual Hosting straight from the Payment Systems [#](virtual_hosting_server#pay)

If you do not have enough money on your MQL5.community account to pay for the hosting, you do not need to go to the website and fund it. You can pay for the hosting straight from one of the payment systems. Just click "Next" after choosing the rent plan. Then choose a suitable payment system.

![Paying for virtual hosting straight from the payment systems](/en/docs/mt4/terminal/img/vh_direct_pay.png "Paying for virtual hosting straight from the payment systems")

To maintain a clear and unified history of rented virtual hosting platforms, the required amount will be transferred to your MQL5.community account first, from which a payment for the service will be made. You can easily access and review all your payments from your MQL5.community Profile.

After paying you will pass to the last step of renting where you can perform the migration right away.

[Virtual Hosting](/en/docs/mt4/terminal/virtual_hosting)

[Migration](/en/docs/mt4/terminal/virtual_hosting/virtual_hosting_migration)