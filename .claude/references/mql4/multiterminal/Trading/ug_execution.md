# Types of Execution

> Source: https://support.metaquotes.net/en/docs/mt4/multiterminal/trading/ug_execution

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
    -   [MetaEditor](/en/docs/mt4/metaeditor)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
        -   [Getting Started](/en/docs/mt4/multiterminal/getting_started)
        -   [Client Accounts](/en/docs/mt4/multiterminal/accounts)
        -   [Trading](/en/docs/mt4/multiterminal/trading)
            -   [Order Types](/en/docs/mt4/multiterminal/trading/ug_orders)
            -   [Types of Execution](/en/docs/mt4/multiterminal/trading/ug_execution)
            -   [Trade Orders](/en/docs/mt4/multiterminal/trading/trade_orders)
        -   [Analytics](/en/docs/mt4/multiterminal/analytics)
        -   [User Interface](/en/docs/mt4/multiterminal/user_interface)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MultiTerminal](/en/docs/mt4/multiterminal)[Trading](/en/docs/mt4/multiterminal/trading)Types of Execution

# Types of Execution

There are three order execution modes in the multiterminal:

-   Instant Execution  
    In this mode, the order is executed at the price offered to the broker. At sending the order to be executed, terminal sets the current prices in the order. If a broker accepts the prices, the order will be executed. If not, the so-called "Requote" will occur: broker returns prices at which the order can be executed.
-   Execution on Request  
    In this mode, the market order is executed at the price previously received from the broker. Prices for a certain market order are requested from the broker before the order is sent. After the prices are received, order execution at the given price can be either confirmed or rejected.
-   Execution by Market  
    In this order execution mode, a broker makes a decision about the order execution price without any additional discussion with the trader. Sending of the order in such a mode means advance consent to its execution at this price.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: Execution mode for each security is defined by the brokerage company.</span></p></td></tr></tbody></table>

[Order Types](/en/docs/mt4/multiterminal/trading/ug_orders)

[Trade Orders](/en/docs/mt4/multiterminal/trading/trade_orders)