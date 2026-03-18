# Signals

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/overview/terminal/toolbox_signals

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
            -   [Main Menu](/en/docs/mt4/terminal/overview/main_menu)
            -   [Toolbars](/en/docs/mt4/terminal/overview/toolbars)
            -   [Market Watch](/en/docs/mt4/terminal/overview/market_watch)
            -   [Depth of Market](/en/docs/mt4/terminal/overview/depth_of_market)
            -   [Data Window](/en/docs/mt4/terminal/overview/data_window)
            -   [Navigator](/en/docs/mt4/terminal/overview/navigator)
            -   [Chart Switching Bar](/en/docs/mt4/terminal/overview/charts_bar)
            -   [Client terminal](/en/docs/mt4/terminal/overview/terminal)
                -   [Trade](/en/docs/mt4/terminal/overview/terminal/terminal_trade)
                -   [Exposure](/en/docs/mt4/terminal/overview/terminal/toolbox_exposure)
                -   [Account History](/en/docs/mt4/terminal/overview/terminal/terminal_account_history)
                -   [News](/en/docs/mt4/terminal/overview/terminal/terminal_news)
                -   [Alerts](/en/docs/mt4/terminal/overview/terminal/terminal_alerts)
                -   [Mailbox](/en/docs/mt4/terminal/overview/terminal/terminal_mailbox)
                -   [Company](/en/docs/mt4/terminal/overview/terminal/toolbox_company)
                -   [Market](/en/docs/mt4/terminal/overview/terminal/toolbox_market)
                -   [Signals](/en/docs/mt4/terminal/overview/terminal/toolbox_signals)
                -   [Code Base](/en/docs/mt4/terminal/overview/terminal/toolbox_codebase)
                -   [Search](/en/docs/mt4/terminal/overview/terminal/toolbox_search)
                -   [Experts](/en/docs/mt4/terminal/overview/terminal/terminal_experts)
                -   [Journal](/en/docs/mt4/terminal/overview/terminal/terminal_journal)
            -   [Tester](/en/docs/mt4/terminal/overview/strategy_tester)
            -   [Search](/en/docs/mt4/terminal/overview/search)
            -   [Fast Navigation](/en/docs/mt4/terminal/overview/fast_nav)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[User Interface](/en/docs/mt4/terminal/overview)[Client terminal](/en/docs/mt4/terminal/overview/terminal)Signals

# Signals

Signals service allows anyone to become a provider and sell trading signals or subscribe to them and follow the strategy of an experienced trader.

A user should have an active [MQL5.community](https://www.mql5.com/en "MQL5.community") account to use the Signals service. If you do not have an account yet, please [register](https://www.mql5.com/en/auth_register "Register on MQL5.community"). The account should be specified in the [terminal settings](/en/docs/mt4/terminal/setup/settings_mql5community).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Find more about how to become a signals provider or to subscribe to signals in <a href="/en/docs/mt4/terminal/signals" class="topiclink">Signals</a> section.</span></p></td></tr></tbody></table>

Signals tab of Terminal window displays trading signals available for subscription.

![Trading signals displayed in the terminal](/en/docs/mt4/terminal/img/toolbox_signals.png "Trading signals displayed in the terminal")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When connecting to a real account, only signals based on real accounts are displayed in the list.</span></li><li class="p_tableatten"><span class="f_tableatten">Only the first one thousand signals sorted by their rating are displayed in the terminal's showcase. Other signals can be found via <a href="https://www.mql5.com/en/signals" target="_blank" class="weblink" title="Signals on MQL5.community">MQL5.community</a> website or by using <a href="/en/docs/mt4/terminal/overview/terminal/toolbox_search" class="topiclink">search</a>.</span></li></ul></td></tr></tbody></table>

Basic parameters are displayed in the signals list:

-   Growth graph.
-   Signal — signal name.
-   Equity — equity at the signal's account.

-   Growth — deposit growth in percentage value calculated on the basis of trade history without considering deposits and withdrawals;

-   Weeks — number of weeks that have passed since the first trade on the trading account was performed (the entire account lifetime instead of the period since its registration as a signal is considered);

-   Max DD — maximum balance drop from the local maximum in percentage value;
-   PF — profit factor, ratio between gross profit and gross loss. One means that these parameters are equal.
-   Price — signal price in USD. Also, "Add to Favorites" ![Add to Favorites](/en/docs/mt4/terminal/img/signal_favorite_icon.png "Add to Favorites") button can be found in this column allowing you to add a signal to [Favorites](/en/docs/mt4/terminal/overview/terminal/toolbox_signals#favorites).

The list can be sorted by any of the above parameters. The first mouse click on the column name sorts the signals by the first parameter, while the second click — by the second parameter. To reset the sorting, click the upper line of the growth graph column.

## Signal Monitoring [#](toolbox_signals#monitor)

Double-click the signal in the list to see a detailed information about it.

![Signal monitoring](/en/docs/mt4/terminal/img/toolbox_signals_view.png "Signal monitoring")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Detailed description of parameters tracked by the trading accounts monitoring system can be found in <a href="/en/docs/mt4/terminal/signals/signal_monitoring" class="topiclink">"Accounts Monitoring"</a> section.</span></p></td></tr></tbody></table>

The upper part of the tab contains the toolbar:

-   ![Add to Favorites](/en/docs/mt4/terminal/img/signal_favorite_icon.png "Add to Favorites") — add/remove the signal from [Favorites](/en/docs/mt4/terminal/overview/terminal/toolbox_signals#favorites).

-   ![Visualize](/en/docs/mt4/terminal/img/visualize_icon.png "Visualize") — this command allows viewing the trade history of the signal account on [charts](/en/docs/mt4/terminal/chart_management) in the terminal. If your click it, all the charts of symbols traded on the signal account will be opened. All deals performed on the signal account will be displayed on those chart with icons ![Buy](/en/docs/mt4/terminal/img/buy_icon.png "Buy") and ![Sell](/en/docs/mt4/terminal/img/sell_icon.png "Sell").
-   Subscribe — subscribe to the current signal;
-   Unsubscribe — unsubscribe from the trading signal;
-   Renew subscription — prolong your current subscription.

## Subscription to Signal [#](toolbox_signals#subscribe)

If you are satisfied with the signal (including its price), you can subscribe to it. Click "Subscribe" at the top of the toolbar. Subscription confirmation window will appear:

![Subscription confirmation](/en/docs/mt4/terminal/img/toolbox_signals_subscribe.png "Subscription confirmation")

Basic signal data is displayed here:

-   Signal — signal's name. When clicking on a name, you will move to a signal's description on MQL5.community.
-   Provider — signal provider's name. When clicking on it, you will move to the provider's MQL5.community profile.
-   Broker — name of a broker server used by the provider.
-   Growth — deposit growth on the provider's account from the moment of signal registration. The value is specified in percentage from the initial value.
-   Price — monthly subscription price.

You should also agree to the terms of use of the signals service by ticking the appropriate option.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">No deals will be copied to your account until you activate <a href="/en/docs/mt4/terminal/setup/settings_signals" class="topiclink">"Enable realtime signal subscription"</a> option in your trading terminal.</span></p></td></tr></tbody></table>

## Unsubscribe from Signal [#](toolbox_signals#unsubscribe)

To manage subscription in the client terminal, open a page of any signal. "You already subscribed to \[signal name\]" message is displayed in the upper panel.

![You are already subscribed to the signal](/en/docs/mt4/terminal/img/signal_subscription_exists.png "You are already subscribed to the signal")

The signal name is a link leading you to the signal's page. Click "Unsubscribe" in the signal's upper command panel.

## Favorites [#](toolbox_signals#favorites)

A huge number of signals is available for subscription. When searching for signals, you can add any of them to Favorites in order to select the best one. Add/remove a signal from Favorites by clicking ![Add to Favorites](/en/docs/mt4/terminal/img/signal_favorite_icon.png "Add to Favorites") button available in the signals list and a signal page.

All Favorite signals are displayed in a separate tab:

![Favorites](/en/docs/mt4/terminal/img/signal_favorites.png "Favorites")

## My Statistics [#](toolbox_signals#stats)

Statistics on signal copying is displayed in this tab. It contains data on all signals the current trading account has ever been subscribed to.

![My Statistics](/en/docs/mt4/terminal/img/signal_statistics.png "My Statistics")

All values in the list are only based on the trades copied to the trading account in accordance with the signal:

-   Growth graph.
-   Signal — signal name.

-   Growth — deposit growth in percentage value calculated on the basis of trade history without considering deposits and withdrawals;

-   Weeks — number of weeks, during which the signal was copied;

-   Max DD — maximum balance drop from the local maximum in percentage value;
-   PF — profit factor, ratio between gross profit and gross loss. One means that these parameters are equal.
-   End date — signal subscription end date.

The list can be sorted by any of the above parameters. The first mouse click on the column name sorts the signals by the first parameter, while the second click — by the second parameter. To reset the sorting, click the upper line of the growth graph column.

[Market](/en/docs/mt4/terminal/overview/terminal/toolbox_market)

[Code Base](/en/docs/mt4/terminal/overview/terminal/toolbox_codebase)