# Queue, Dealing, Margin Calls Windows

> Source: https://support.metaquotes.net/en/docs/mt4/manager/request_processing/ug_win_queue

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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Request Processing](/en/docs/mt4/manager/request_processing)Queue, Dealing, Margin Calls Windows

# Queue, Dealing, Margin Calls Windows

The "Queue" window is intended for displaying the client's list of requests belonging to groups for manual request execution. It can be called by pressing the ![Queue](/en/docs/mt4/manager/img/ic_queue.png "Queue") button in the "View" menu or on the "Standard" toolbar.

![Queue window](/en/docs/mt4/manager/img/win_queue.png "Queue window")

Requests of all clients queueing for being processed are displayed in the "Requests" tab. The current request being processed by the dealer is highlighted in red. In the "History" tab, the request history of the client is displayed whose request is under processing by the current dealer. This list allows to follow the client's trading activity. The rejected requests of the client are highlighted in pink.

![Queue Window, History Tab](/en/docs/mt4/manager/img/win_queue_hist.png "Queue Window, History Tab")

It is possible to switch to the "History" tab automatically as soon as a new client's request incomes. To do so, it is necessary to enable "Track Requests" mode in the context menu of general queue of requests. The "Details" command of the context menu opens the account management window.

## Dealing Tab [#](ug_win_queue#dealing)

The "Dealing" tab of the "Toolbox" window displays the journal of the dealer's answers to the client requests. This journal is stored on the disk in "operations.log" file in the "logs" subdirectory of the manager terminal.

![Dealing Window](/en/docs/mt4/manager/img/tb_dealing.png "Dealing Window")

The "Details" command of the context menu opens the window of account management. The "Copy" command of the context menu copies the selected lines of the journal to the clipboard.

## Margin Calls Window [#](ug_win_queue#margin_call)

The "Margin Calls" window allows to track clients having not enough money on their accounts to meet margin requirements. This window displays the clients' account list, free margin level (pawn requirements) of which is equal to or less than Margin-Call level. To call this window you should press the ![Margin Calls](/en/docs/mt4/manager/img/ic_margin_call.png "Margin Calls") button in the "View" menu or on the "Standard" toolbar.

![Margin Calls Window](/en/docs/mt4/manager/img/margincalls.png "Margin Calls Window")

Clients having the free margin level less than that of Stop Out are highlighted in pink. For such clients, the most unprofitable open order is automatically searched for to be listed among triggered orders of the [Dealer Window](/en/docs/mt4/manager/request_processing/ug_dealing). The profit field of such an order is highlighted in red. When Stop-Out [automation](/en/docs/mt4/manager/request_processing/ug_automation) is enabled, the most unprofitable order will be closed automatically.

The "Details" command of the context menu opens the account management window. The "Email" command of the context menu allows to send a message (warning or requirement to add deposit on account) to the client via internal mailbox.

[Automation](/en/docs/mt4/manager/request_processing/ug_automation)

[Reports and Journal](/en/docs/mt4/manager/reports_journal)