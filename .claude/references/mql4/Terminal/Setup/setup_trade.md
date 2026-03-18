# Trade

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/setup/setup_trade

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Client Terminal Settings](/en/docs/mt4/terminal/setup)Trade

# Trade

Settings used for orders opening are grouped in this tab.

![Trade](/en/docs/mt4/terminal/img/options_trading.png "Trade")

Parameters input here facilitate opening of orders and cannot cause critical changes in the terminal operation.

-   Symbol by Default  
    The "Symbol by default" option allows to define the symbol value in the ["Order" window](/en/docs/mt4/terminal/positions/positions_control/positions_open) automatically when a trading operation is performed. The "Automatic" parameter means that the active chart symbol will be set in this field, the "Last used" — the symbol of the latest trade operation. For the same symbol to be set repeatedly, the "Default" parameter must be enabled, and the necessary symbol chosen from the list.
-   Lots by Default  
    In the similar way, the initial amount of lots can be defined ("Lots by default" option): "Last used" is a parameter used in the previous operation, and "by default" is a constant, manually set value.
-   Deviation  
    The symbol price can change within the ordering time. As a result, the price of the prepared order will not correspond with the market one, and position will not be opened. The "Deviation" option helps to avoid this. Maximum permissible deviation from the value given in the order can be specified in this field. If prices do not correspond, the program will modify the order by itself what allows to open a new position.
-   One click trading — [special terms and conditions](/en/docs/mt4/terminal/setup/setup_trade#agreement) should be accepted to use this option. The "One click trading" option allows performing trade operations with a single mouse click without additional confirmation from the trader (without showing the [trade dialog window](/en/docs/mt4/terminal/positions/positions_control/positions_open)). The one click trading feature is implemented in the following parts of the terminal:

-   the [quick trading pane on the chart](/en/docs/mt4/terminal/chart_management/chart_trading);
-   [trade levels](/en/docs/mt4/terminal/positions/trading_chart#pending_chart) on the chart;

-   [trade commands](/en/docs/mt4/terminal/positions/trading_chart#position_context) in the chart context menu;

-   the ["Trading"](/en/docs/mt4/terminal/overview/terminal/terminal_trade#one_click) tab in the "Terminal" window.

## Terms and Conditions for Using One-Click Trading Function [#](setup_trade#agreement)

When "One click trading" option is used for the first time, Terms and Conditions for using this function are displayed to users.

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">Disclaimer</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">You are about to activate One Click Trading mode. By clicking "I Accept these Terms and Conditions" below, you acknowledge that you have read and understood the following terms and conditions, and you agree to be bound hereby. Your current version of the terminal enables you to choose between the following modes for order submission. You agree that you will be bound by the procedures and conditions specified herein with respect to each such mode.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">1. The Default mode for order submission is a two-step process. Using the Default mode, you first invoke a new order window. Then you need to select an appropriate order type, its parameters and confirm your order submission by clicking either Buy, Sell, Place, Modify or Close buttons depending on particular order type selected and your trading intentions. Using the Default mode, your order will not be submitted until you have completed both of the aforementioned steps.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">2. The One Click Trading mode for order submission ("One-click trading") is a one-step process. Using the One Click Trading mode, your order will be submitted when you:</span></p><p class="p_fortable"><span class="f_fortable">- single-click either bid (SELL) or ask (BUY) rate buttons either:</span></p><p class="p_fortable"><span class="f_fortable">&nbsp; &nbsp;- on the Trading tab in the Market Watch window</span></p><p class="p_fortable"><span class="f_fortable">&nbsp; &nbsp;- on the One Click Trading panel of a chart</span></p><p class="p_fortable"><span class="f_fortable">- close pending orders or delete stop levels on the Trade tab of the Terminal window</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">THERE WILL BE NO SUBSEQUENT CONFIRMATION PROMPT FOR YOU TO CLICK. YOU WILL NOT BE ABLE TO WITHDRAW OR CHANGE YOUR ORDER ONCE YOU CLICK. UNDER NORMAL MARKET CONDITIONS AND SYSTEM PERFORMANCE, A MARKET ORDER WILL BE PROMPTLY FILLED AFTER SUBMISSION AND YOU WILL HAVE ENTERED INTO A BINDING TRANSACTION.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">You can activate or deactivate One Click Trading mode on the Trade tab of Options window of the terminal.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">By selecting the One Click Trading mode, you understand that your orders will be submitted by clicking the bid or ask rate button or in any other way described above, without any further order confirmation. You agree to accept all risks associated with the use of the order submission mode you have chosen, including, without limitation, the risk of errors, omissions or mistakes made in submitting any order.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">You agree to fully indemnify and hold harmless #company# from any and all losses, costs and expenses that it may incur as a result of any such errors, omissions or mistakes by you, your trading manager or any other person trading on your behalf.</span></p></td></tr></tbody></table>

If you accept the conditions, tick "I Accept these Terms and Conditions" option and click "ОК". If you do not accept the conditions, click "Cancel" and do not use "One Click Trading" function.

[Objects](/en/docs/mt4/terminal/setup/setup_objects)

[Expert Advisors](/en/docs/mt4/terminal/setup/setup_experts)