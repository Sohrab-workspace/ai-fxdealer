# Signals

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/settings_signals

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)Signals

# Signals

Use this tab to configure ["Signals" service](https://www.mql5.com/en/signals "Signals Service") in the client terminal.

Signals service is the part of integration of the trading terminal and [MQL5.community website](https://www.mql5.com/en "MQL5.community"). It allows anyone to become a provider and sell trading signals or subscribe to them and follow the strategy of an experienced trader.

Any traders can subscribe to the signals of another experienced trader ([provider](/en/docs/mt4/terminal/signals/signal_provider)) to copy his or her trade operations.

Find more about the service in [Signals](/en/docs/mt4/terminal/signals) section.

![Signals](/en/docs/mt4/terminal/img/options_signals.png "Signals")

The name of the signal you are currently [subscribed](/en/docs/mt4/terminal/signals/signal_subscriber) to is displayed at the top of the tab. If there is no subscription, the settings below will be uneditable.

-   Agree to the terms of use of the Signals service — agree to the [terms to start using the service](https://www.mql5.com/en/signals/rules "Rules of Using the Signals Service"). Read the rules carefully. If you agree, check the box next to the option. If you do not agree with the rules, do not use the Signals service.

-   Enable realtime signal subscription — trading operations will be copied to your account only after this option is enabled. No operations will be copied to the account in case the option is disabled. The settings below will become editable only after enabling this option.
-   Copy Stop Loss and Take Profit levels — [Stop Loss](/en/docs/mt4/terminal/positions/orders#stop_loss) and [Take Profit](/en/docs/mt4/terminal/positions/orders#take_profit) placed at the provider's account will be also placed on your trading account if this option is enabled. These orders are executed at the broker's side. It means that they are executed regardless of whether the client terminal has been launched or not. Also, execution can be performed at completely different brokerage companies (if subscriber and provider have different brokers).  
    Therefore, it is guaranteed that a position will be closed when copying Stop orders in case a specified profit and loss levels have been reached.

-   Synchronize positions without confirmations — automatic synchronization without additional confirmation. When subscribing to a signal, trading states of the Subscriber's and Provider's accounts are [synchronized](/en/docs/mt4/terminal/signals/signal_subscriber#sync). This can be a primary synchronization when activating the subscription or [a re-synchronization](/en/docs/mt4/terminal/signals/signal_subscriber#resync) during copying.  
    If pending orders or non-signal positions (opened manually or by an Expert Advisor) are detected at the Subscriber's account during synchronization, the dialog offering to close the positions and remove the orders is displayed. If during the [initial synchronization](/en/docs/mt4/terminal/signals/signal_subscriber#sync), a provider account has floating (unfixed) profit, a user will see a dialog window offering to wait for better conditions to start copying. In both cases, synchronization is not performed and copying of signals is stopped until the user makes the decision by clicking the appropriate dialog button.  
    If the platform is working around the clock without constant external control (for example, runs on VPS), confirmation requests to perform synchronization are left unanswered and thus can prevent signals from being copied. When this option is enabled, synchronization is always performed automatically without the need for Subscriber's confirmation.

-   If there are custom positions/orders, they are left on the account, while the system starts/proceeds copying the Provider's trades.
-   If the Provider has a floating profit, the platform does not wait for better entry conditions and starts copying immediately.

-   Use no more than \[A\] % — percentage value of your deposit that can be used for following provider's signals. For example, if your balance is 10 000 USD and 90% is specified here, then 9 000 USD will be used for following the signals. This affects the calculation of volumes of the deals performed when following the signals. The volume is calculated proportionally. See ["Signal Subscribers"](/en/docs/mt4/terminal/signals/signal_subscriber#trade) section for more information. It is strongly not recommended to change the deposit load if you already have positions opened according to a signal. This will lead to correction of volume of the open positions (volume increase or partial close by reopening the positions at the current market price).
-   Stop if equity is less than \[B\] — this parameter allows you to limit losses when using trading signals. If equity drops below a specified level, copying of trade signals will be automatically terminated, all positions will be closed and all pending orders will be removed. 0 means no limitations.
-   Deviation/Slippage \[C\] spreads — this setting is similar to deviation set when [orders are placed](/en/docs/mt4/terminal/positions/positions_control/pending_orders_delete) from the terminal. This is the value of the permissible deviation of the executed order price from the price initially requested by the client terminal when copying a trading operation. This value is displayed as a part of the current spread on the symbol used in trading operation.  
    The order is executed if the deviation is less or equal to the specified parameter. If the deviation exceeds the specified value, the terminal will increase the acceptable deviation by 0,5 of the spread and make another attempt to perform the trade operation. If the requote is received again, the accounts of the subscriber and provider will become unsynchronized. Later the terminal will try to synchronize them again.

[Community](/en/docs/mt4/terminal/setup/settings_mql5community)

[User Interface](/en/docs/mt4/terminal/overview)