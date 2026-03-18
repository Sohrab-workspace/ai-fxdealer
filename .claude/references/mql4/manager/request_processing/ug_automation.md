# Automation

> Source: https://support.metaquotes.net/en/docs/mt4/manager/request_processing/ug_automation

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
        -   [Getting Started](/en/docs/mt4/manager/getting_started)
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
            -   [Dealer](/en/docs/mt4/manager/request_processing/ug_dealing)
            -   [Automation](/en/docs/mt4/manager/request_processing/ug_automation)
            -   [Queue, Dealing, Margin Calls Windows](/en/docs/mt4/manager/request_processing/ug_win_queue)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
        -   [Articles](/en/docs/mt4/manager/articles)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Request Processing](/en/docs/mt4/manager/request_processing)Automation

# Automation

MetaTrader Manager 4 allows a connected dealer to confirm trade operations of certain types automatically. To get a permission for automatic confirmation of requests, it is necessary to enable "Automation" mode on the dealer's toolbar or in the context menu of the dealer's à window.

The request types to be processed automatically are set up using "Automation" tab of the "Options" window ("Tools -> Options..." menu). It is possible to indicate a trade operation volume to be processed automatically for each request type. When receiving a request having a volume above the maximum volume, the dealer will have to answer this request manually.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention! A request with the volume above the specified value will not be processed until a dealer answers it manually.</span></p></td></tr></tbody></table>

![Automation](/en/docs/mt4/manager/img/opt_automation.png "Automation")

-   Enable — enable automatic confirmation of requests;
-   Profile — automatic confirmation settings profile;
-   Save As — save automatic confirmation settings as profile;
-   Delete — delete selected automatic confirmation settings profile.

It is possible to enable automatic execution and setting maximum lot volume for the following request types:

-   Request Quotes — request prices;
-   Modify Orders (S/L, T/P, Open Price) — modify orders (Stop Loss, Take Profit, open price for a pending order);
-   Confirmations — confirmation of operations in the request mode and in the instant execution mode;
-   Buy/Sell Market — buy or sell at market;
-   Close Market — close at market;
-   Close By Orders — "Close by" orders;
-   Close All Orders — "Close by Symbol" orders;
-   Stop Out — Stop Out orders;
-   Place Pending Orders — place pending orders;
-   Delete Pending Orders — delete pending orders;
-   Activate Pending Order — activate pending orders;
-   Activate Stop Loss — activate Stop-Loss orders;
-   Activate Take Profit — activate Take-Profit orders.

[Dealer](/en/docs/mt4/manager/request_processing/ug_dealing)

[Queue, Dealing, Margin Calls Windows](/en/docs/mt4/manager/request_processing/ug_win_queue)