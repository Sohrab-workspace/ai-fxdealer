# Price Calculation

> Source: https://support.metaquotes.net/en/docs/mt5/client/mql5cloud_calculation

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
            -   [How to Use](/en/docs/mt5/client/mql5cloud_use)
            -   [How to Participate](/en/docs/mt5/client/mql5cloud_install)
            -   [Price Calculation](/en/docs/mt5/client/mql5cloud_calculation)
        -   [Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)Price Calculation

# Price Calculation

This section describes the formula of price calculation for providing and using the agents of the [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud).

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">All the financial operations connected with the MQL5 Cloud Network are performed through the internal payment system of <a href="https://www.mql5.com/" target="_blank" class="weblink" title="MQL5.community">MQL5.community</a>. You can view all the financial operations on the MQl5.community website in the profile of the user account used for working in the MQL5 Cloud Network.</span></p></td></tr></tbody></table>

Tester agent productivity and the time it spent for a task execution are taken into account when calculating payment amounts. Each tester agent has its productivity index - PR. The higher the CPU productivity, the higher this index and the more calculations an agent can perform per unit time.

Calculation of funds for executed calculations is arranged as follows. Payment for a tester agent having PR=100 is 0.08 USD per hour. One work unit is equal to one quantum that is equivalent to the work of an agent having PR=1 in 1 ms (1 millisecond). Therefore, the cost of one quantum is calculated as follows:

   QuantPrice=0.08 USD/(100PR\*3,600,000ms)=2.22222E-10 USD

The table below shows the calculations for the work of a single-core agent having PR=100 within 1 hour and 1 month.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Time range</span></p></th><th class="table" style="width:207px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">QuantPrice, USD/(PR*ms)</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Agent PR</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Time, ms</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Amount, USD</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable">1 hour</span></p></td><td class="table" style="width:207px;"><p class="p_fortable"><span class="f_fortable">2.22222E-10</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">100</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">3,600,000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">0.08</span></p></td></tr><tr class="table"><td class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable">1 month</span></p></td><td class="table" style="width:207px;"><p class="p_fortable"><span class="f_fortable">2.22222E-10</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">100</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">2,592,000,000</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">57.60</span></p></td></tr></tbody></table>

In addition to the service cost, a fee is charged for the internet traffic transmitted to each agent for task execution. The transmitted data includes the file of the Expert Advisor being tested, its input parameters, environment settings, price data and other service information. The traffic cost is USD 0.00002 per megabyte.

[How to Participate](/en/docs/mt5/client/mql5cloud_install)

[Virtual Hosting for 24/7 Operation](/en/docs/mt5/client/virtual_hosting)