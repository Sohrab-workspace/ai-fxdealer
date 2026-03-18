# Signal Providers

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/signals/signal_provider

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
            -   [Signal Providers](/en/docs/mt4/terminal/signals/signal_provider)
            -   [Signal Subscribers](/en/docs/mt4/terminal/signals/signal_subscriber)
            -   [Account Monitoring](/en/docs/mt4/terminal/signals/signal_monitoring)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Signals](/en/docs/mt4/terminal/signals)Signal Providers

# Signal Providers

Signal Provider is a trader who grants access to the data on his or her trading operations allowing other traders to copy them on their own trading accounts. To become a Signal Provider, a user should have an active MQL5.community account. If you do not have an account yet, please [register](https://www.mql5.com/en/auth_register "Register on MQL5.community").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Make sure to read the <a href="https://www.mql5.com/en/signals/rules" target="_blank" class="weblink" title="Rules of Using the Signals Service">rules before using the Signals service</a>.</span></p></td></tr></tbody></table>

Important information for Signal Providers:

-   [How to register as a Signal Provider](/en/docs/mt4/terminal/signals/signal_provider#seller)
-   [How to add a signal](/en/docs/mt4/terminal/signals/signal_provider#add)
-   [How to manage your signals](/en/docs/mt4/terminal/signals/signal_provider#manage)

## Registration as a Seller [#](signal_provider#seller)

To be able to register your trading account as a provider of paid signals, you should register as a seller. Move to the "Seller" section of your profile at [MQL5.community](https://www.mql5.com/en/signals "Signals section on MQL5.community").

![Start registration as a Signals Provider](/en/docs/mt4/terminal/img/register_seller.png "Start registration as a Signals Provider")

Prior to registration, you should confirm your consent to the processing of your personal data and agree to Service Rules. During the registration process, you will need to provide your personal data as well as to attach photographs of your ID documents. Every registration step is provided with detailed instructions. Please read them carefully and strictly follow the requirements.

Information about the approval or refusal of your registration will appear on the same page in due course.

## Adding a Signal [#](signal_provider#add)

After you have registered as a Signals Provider, you will see "Add signal" button instead of "Register" on the "Signals" tab.

![Adding a Signal](/en/docs/mt4/terminal/img/signal_add.png "Adding a Signal")

After clicking it, you will move to the account registration form where you should specify the account that will be used for sending trading signals.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_fortable"><span class="f_fortable">To quickly create a signal, select a required account in the <a href="/en/docs/mt4/terminal/overview/navigator" class="topiclink">"Navigator"</a> in the terminal, and execute the "Register as Signal" command in its context menu. Then you'll go the signal registration page at MQL5.community. The selected account and the right broker server will be automatically specified in the registration form.</span></p></td></tr></tbody></table>

![Signal registration form](/en/docs/mt4/terminal/img/signal_add_form.png "Signal registration form")

Enter the following data to add the signal:

-   Monitoring is enabled, real-time gathering of data — your signal will not be available to other users as long as this option is not ticked.
-   Name — trading signal name.
-   Terminal — the fourth version of the trading terminal should be selected in this field.
-   Login — account number, from which trading signals will be transmitted.
-   Password — specify your investor password here. This password provides access to the account in read-only mode without the possibility to perform trading operations. Master password is not specified and the Provider's account remains perfectly secure.
-   Broker — broker server name. When you start typing the first characters, the list of possible names will be shown to you.

-   Subscription price — if the signal is based on a real account, set subscription price in this field. The price is set in USD per month. Signals based on demo accounts are always free.

-   Notifications — you can receive notifications on various changes on MQL5.community website (new personal messages, correspondence with the moderator in seller's profile or Articles section, etc.) via your mobile phone. Notifications coming to your mobile number can be replaced with more up-to-date and reliable [push notifications](/en/docs/mt4/terminal/setup/settings_notifications). Specify your unique MetaQuotes ID (that can be found in the mobile trading terminals for [iPhone](https://download.terminal.free/cdn/mobile/mt4/ios?hl=en&utm_campaign=metaquotes.download&utm_source=www.metatrader4.com "iPhone") and [Android](https://download.terminal.free/cdn/mobile/mt4/android?hl=en&utm_campaign=metaquotes.download&utm_source=www.metatrader4.com "Android")) and receive instant and free notifications on all important MQL5.community events.

Click "Add" after specifying all the parameters.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">An account with a leverage exceeding 1:500 will not be available for <a href="/en/docs/mt4/terminal/signals/signal_subscriber" class="topiclink">subscription</a>. This limitation is implemented to protect subscribers from signals produced on accounts with too risky trading process.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">A provider doesn't need to stay always connected in the client terminal with the account used for providing signals. Trade operations are read by the signal server using the investor password provided during the registration and then delivered to subscribers.</span></li></ul></td></tr></tbody></table>

## Managing Signals [#](signal_provider#manage)

Move to "My Signals" section to manage your signals.

![My Signals](/en/docs/mt4/terminal/img/my_signals.png "My Signals")

Basic information about your signal is displayed here:

-   Name — signal name.

-   Growth — growth of signal provider's funds in percentage terms.

-   Subscribers — number of users currently subscribed to the signal.
-   Weeks — number of weeks that have passed since the first trade on the trading account was performed (the entire account lifetime instead of the period since its registration as a signal is considered);
-   Trades — number of trades used for fixing profit/loss.
-   Win — percentage of profitable trades out of their total amount.

Signals can be viewed by categories by clicking the appropriate tabs:

-   Public — signals that can be viewed by other users.
-   Disabled — signals with monitoring disabled.
-   All Signals — list of all signals.

Click the signal to edit it.

![Editing the signal](/en/docs/mt4/terminal/img/signal_edit.png "Editing the signal")

Move to the signal monitoring and click "Edit" in the upper right corner. The form filled out when [adding](/en/docs/mt4/terminal/signals/signal_provider#add) the signal will be displayed. Only the following parameters can be changed:

-   enable/disable signal;
-   signal name;
-   account password;
-   subscription price.

[Signals](/en/docs/mt4/terminal/signals)

[Signal Subscribers](/en/docs/mt4/terminal/signals/signal_subscriber)