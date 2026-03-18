# MetaTrader 5 Gateway to FXCM PRO

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/gateways/fxcmpro

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
                -   [MOEXFX](/en/docs/mt5/platform/components/gateways/moex_fx)
                -   [MOEX Securities](/en/docs/mt5/platform/components/gateways/moex_securities)
                -   [MOEX Derivatives](/en/docs/mt5/platform/components/gateways/moex_derivatives)
                -   [DGCX](/en/docs/mt5/platform/components/gateways/dgcx)
                -   [MetaTrader 5](/en/docs/mt5/platform/components/gateways/metatrader5gateway)
                -   [MetaTrader 4](/en/docs/mt5/platform/components/gateways/metatrader4gateway)
                -   [Integral](/en/docs/mt5/platform/components/gateways/integral)
                -   [Currenex](/en/docs/mt5/platform/components/gateways/currenex)
                -   [Euronext FX](/en/docs/mt5/platform/components/gateways/euronextfx)
                -   [Cboe FX](/en/docs/mt5/platform/components/gateways/cboefx)
                -   [LMAX Global](/en/docs/mt5/platform/components/gateways/lmax)
                -   [FXCM PRO](/en/docs/mt5/platform/components/gateways/fxcmpro)
                -   [Borsa Istanbul](/en/docs/mt5/platform/components/gateways/borsa)
                -   [Interactive Brokers](/en/docs/mt5/platform/components/gateways/interactive_brokers)
            -   [Old WebTerminal](/en/docs/mt5/platform/components/web_terminal_old)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
        -   [Migration from MetaTrader 4](/en/docs/mt5/platform/migration)
        -   [App Store](/en/docs/mt5/platform/appstore)
        -   [Technical Support](/en/docs/mt5/platform/support)
        -   [Additional Features](/en/docs/mt5/platform/additional)
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
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Gateways](/en/docs/mt5/platform/components/gateways)FXCM PRO

# MetaTrader 5 Gateway to FXCM PRO

[FXCM PRO](https://www.fxcmpro.com/) is the institutional arm of FXCM, the largest broker in the United States. FXCM Pro trading system serves 200 000 traders all over the world conducting over 500 000 trades per day with the average daily volume of $14 billion.

FXCM Pro offers brokers the transparent service system based on agency commission with fully anonymous trading. The system provides access to [40 trading symbols](https://www.fxcm.com/uk/markets/) including currency pairs, indices, metals, energy and Treasury bonds. FXCM Pro offers customized pricing for each instrument and account. Based on customer mandate, FXCMs liquidity management team can source the most efficient liquidity providers and partnering venues to match your needs, be it single tickets on large orders, stickier pricing intraday on metals, and much more.

FXCM Pro trading systems (matching engine) are located in New York (Equinix NY7 data center) and Tokyo (Equinix TY3 data center). The system can be accessed both via the Internet and cross connect in FXCM data center.

## Two Operation Modes: Wholesale and Liquidity Solutions

You can select one of the two operation modes depending on your needs.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Wholesale</span></p></th><th class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Liquidity Solutions</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Wholesale is optimal for retail brokers looking to leverage FXCMs scale. Brokers are able to trade in FXCM Pro using large volumes, thus increasing the acceptable volume of non-hedged positions of their traders.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Cross Collateralization of FX and CFD Trading</span></p><p class="p_fortable"><span class="f_fortable">All customer positions are netted into one account, allowing for more efficient use of corporate cash.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Credit line</span></p><p class="p_fortable"><span class="f_fortable">Through a formal review process FXCM can extend credit in the form of NOP (Net Open Position) in a traditional bank Prime Brokerage manner with flexible settlement terms.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">No fees on small tickets</span></p><p class="p_fortable"><span class="f_fortable">FXCM provides all currency pairs on offer at 1K ticket sizes with no additional fees.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution suitable for automated trading</span></p><p class="p_fortable"><span class="f_fortable">FXCMs FX NDD model, and enhanced index and commodity CFD model is ideal for automated traders seeking a better execution experience.</span></p></td><td class="table" style="width:50%;"><p class="p_fortable"><span class="f_fortable">Liquidity Solutions mode provides liquidity for your traders and ability to send their trading operations to FXCM Pro. There are two distinctly different liquidity solutions — trading via a single account in FXCM Core system and trading in FXCM Pro ECN where an individual account is allocated to each trader.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">FXCM Core</span></p><p class="p_fortable"><span class="f_fortable">This technology suite supports nearly 200 000 traders globally, with over 500 000 trades done daily as well as over $14 billion in daily volumes.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><ul><li class="p_fortable"><span class="f_fortable">NDD execution model is agency based and truly anonymous. Banks and financial institutions comprising FXCMs matching engine have no information about their counterparty. Pending orders are stored on FCXM servers and sent to the matching system only if their execution conditions are fulfilled.</span></li><li class="p_fortable"><span class="f_fortable">Small ticket advantage — FXCM provides all currency pairs on offer at 1K ticket sizes with no additional fees.</span></li><li class="p_fortable"><span class="f_fortable">Multi asset clearing — all assets are traded on one trading account via a single API.</span></li></ul><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">FXCM Pro ECN </span><span class="f_fortable">—</span><span class="f_fortable" style="font-weight: bold;"> institutional API service</span></p><p class="p_fortable"><span class="f_fortable">This technology offers professional and institutional users the ability to tailor pricing on a per instrument, per account basis.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Based on customer mandate, FXCMs liquidity management team can source the most efficient liquidity providers and partnering venues to match your needs, be it single tickets on large orders, stickier pricing intraday on metals, and much more.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">FXCM also provides cross collateralization capabilities for all trading accounts.</span></p></td></tr></tbody></table>

## Getting Started with FXCM Pro

First, connect FXCM Pro to find out the details and conclude an agreement.

<table class="table" cellspacing="0" cellpadding="5" border="0" style="border:none; border-spacing:0;"><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Brandon Mulvihill</span><span class="f_fortable"> &nbsp;— &nbsp;Global Head, FXCM Pro</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Direct: +1 646 432 2521</span></p><p class="p_fortable"><span class="f_fortable">Mobile: +1 917 587 1339</span></p><p class="p_fortable"><span class="f_fortable">Email: bmulvihill@fxcmpro.com</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Chris Hossain</span><span class="f_fortable"> &nbsp;— &nbsp;Head of EMEA, FXCM Pro</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Direct: +44 207 903 6261</span></p><p class="p_fortable"><span class="f_fortable">Mobile: +44 7 540 789 656</span></p><p class="p_fortable"><span class="f_fortable">Email: chossain@fxcmpro.com</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Siju Daniel</span><span class="f_fortable"> — CEO, FXCM Asia</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Email: sdaniel@fxcm.com</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Claudio Flores</span><span class="f_fortable"> </span><span class="f_txt">—</span><span class="f_fortable"> &nbsp;VP, API &amp; Systems Trading</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Email: cflores@fxcm.com</span></p></td></tr></tbody></table>

After concluding an agreement, you will receive all necessary data for connecting to FXCM Pro trading system.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten"><a href="https://support.metaquotes.net/en/market/product/269" class="weblink">Order MetaTrader 5 Gateway to FXCM Pro</a></span></p><p class="p_tableatten"><span class="f_tableatten">&nbsp;</span></p><p class="p_tableatten"><span class="f_tableatten">You can order the MetaTrader 5 FXCM Pro Gateway through the <a href="https://support.metaquotes.net/en/market/product/269" target="_blank" class="weblink">"Buy"</a> section of the technical support site. After you make the payment, the MetaTrader 5 platform license will be automatically updated via the LiveUpdate system and you will be able to use MetaTrader 5 Gateway to FXCM Pro without limitations. The executable module of the gateway is included into the platform package and can run in a demo mode, allowing you to perform 100 operations for a work session (until restart).</span></p></td></tr></tbody></table>

## How the Gateway Works

MetaTrader 5 Gateway to FXCM Pro is a separate FXCMProGateway64.exe module that uses the MetaTrader 5 Gateway API for operation. The gateway works via two FIX channels: the first one is for trading, while the second one is for market data.

All orders entered in FCXM Pro are transferred to the unified requests database. The system selects appropriate orders automatically executing opposite orders with matching parameters (symbol, price etc.)

![Gateway operation](/en/docs/mt5/platform/img/fxcm_scheme.png "Gateway operation")

### Market Data

MetaTrader 5 Gateway to FXCM Pro automatically imports all the necessary symbols and processes their properties. The administrator only needs to perform a primary [setup](/en/docs/mt5/platform/components/gateways/fxcmpro#symbols).

Price data is transmitted in real time. The gateway is capable of narrowing or expanding prices on the go: quotes can be converted according to the settings when passing them to the platform and then re-converted back to their original state when passing trade operations to FXCM Pro. Detailed information on [prices conversion](/en/docs/mt5/platform/components/gateways/fxcmpro#markup) is available below.

### Trading Operations

Orders are sent to MetaTrader 5 Gateway to FXCM Pro for processing in accordance with the set [routing rules](/en/docs/mt5/platform/components/gateways/fxcmpro#routing). Processing of requests depends on the type of the order, as well as the gateway configuration.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Order type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Execution</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">Market order</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Delivered directly to FXCM Pro as a market order.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">Take Profit</span></p><p class="p_fortable"><span class="f_fortable">Buy Limit</span></p><p class="p_fortable"><span class="f_fortable">Sell Limit</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Depends on <a href="/en/docs/mt5/platform/components/gateways/fxcmpro#parameters" class="topiclink">Limit Orders Coverage Mode</a>:</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Limit Orders Coverage Mode=Gateway (default)</span></p><p class="p_fortable"><span class="f_fortable">Limit orders are processed on FXCM Pro side. Once a limit order has been placed by a client, an appropriate order is sent to FXCM Pro. There it is placed to the general queue awaiting for an opposite request with the same price to appear.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">Take Profit orders are processed the same way as in the Limit mode.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">The FXCM Pro system checks the availability of the required amount of funds to cover any type of order placed via the gateway. However, the check is performed on the broker's general account, on behalf of which the work is carried out. <a href="/en/docs/mt5/platform/components/gateways/fxcmpro#margin" class="topiclink">Margin reservation</a> of the clients should be configured for the appropriate order types in case Limit orders are directly delivered to an external system.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">By default, the margin is charged on the side of MetaTrader 5 only when market orders are placed. When placing pending orders in an external system, the client's available funds should be controlled on the side of MetaTrader 5 before the orders are transferred to avoid using all broker's funds by the client.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Limit Orders Coverage Mode=Limit</span></p><p class="p_fortable"><span class="f_fortable">Limit Orders and Take Profit orders are processed on the side of the MetaTrader 5. Once a limit order is triggered, an equivalent limit order is sent to FXCM Pro. That order has a short action time specified in Limit Orders Coverage Timeout parameter. Since the price specified in the order is already present in the market, the order will be executed with that price — a market deal will be performed. If the necessary volume of the financial instrument is not available in the market at the specified price, the order will be executed partially. Thanks to a short expiration time, a limit order with a residual volume will be removed from FXCM Pro. Thus, a client will have a market position as well as a limit order with a residual volume, which will be further processed in a similar way on the side of MetaTrader 5.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable">A limit order with the price equal to a Take Profit level is sent to FXCM Pro at the moment a Take Profit order has been activated. Since the price specified in the order is already present in the market, the order will be executed with that price — a market deal will be performed. If the necessary volume of the financial instrument is not available in the market at the specified price, the order will be executed partially. Thanks to a short expiration time, a limit order with a residual volume will be removed from FXCM Pro. Therefore, a client's position will be closed partially. Control over the Take Profit position level with the remaining volume will then be carried out on MetaTrader 5 side.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span><br><span class="f_fortable">Limit mode allows to protect against slippage, as a limit order is sent to FXCM Pro system with a specified price rather than a market order for execution by the current price.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Limit Orders Coverage Mode=Market</span></p><p class="p_fortable"><span class="f_fortable">Limit orders and Take Profit orders are processed on the MetaTrader 5 platform side. Once they trigger, an appropriate market order is sent to FXCM Pro.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">Buy Stop</span></p><p class="p_fortable"><span class="f_fortable">Sell Stop</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Depends on <a href="/en/docs/mt5/platform/components/gateways/fxcmpro#parameters" class="topiclink">Stop Orders Coverage</a>:</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Stop Orders Coverage=Y</span></p><p class="p_fortable"><span class="f_fortable">Delivered directly to FXCM Pro. Similarly to limit orders, margin reservation of the clients should be configured for the appropriate order types on MetaTrader 5 side in case of direct delivery of stop orders to FXCM Pro.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Stop Orders Coverage=N</span></p><p class="p_fortable"><span class="f_fortable">Processed on the MetaTrader 5 platform side until their stop price is reached. After a stop order is activated, an appropriate market order will be sent to the FXCM Pro system.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">Buy Stop Limit</span></p><p class="p_fortable"><span class="f_fortable">Sell Stop Limit</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Depends on Stop Orders Coverage:</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Stop Orders Coverage=Y</span></p><p class="p_fortable"><span class="f_fortable">Delivered directly to FXCM Pro. Similarly to limit orders, margin reservation of the clients should be configured for the appropriate order types on MetaTrader 5 side in case of direct delivery of stop limit orders to FXCM Pro.</span></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Stop Orders Coverage=N</span></p><p class="p_fortable"><span class="f_fortable">Processed on the MetaTrader 5 side. Upon order activation, an appropriate limit order is created in MetaTrader 5, and this order is then processed in accordance with the value of the Limit Orders Coverage Mode parameter.</span></p></td></tr><tr class="table"><td class="table" style="width:120px;"><p class="p_fortable"><span class="f_fortable">Stop Loss</span></p><p class="p_fortable"><span class="f_fortable">Stop Out</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Processed on the MetaTrader 5 side. Once they trigger, an appropriate market order is sent to FXCM Pro.</span></p></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">In case connection to </span><span class="f_fortable">FXCM Pro</span><span class="f_tableatten"> server is lost, the application will try to restore it repeatedly. If pending orders were executed during the disconnection period, they will be updated in the MetaTrader 5 platform after successful reconnection.</span></p></td></tr></tbody></table>

## Gateway Setup [#](fxcmpro#settings)

To start working, add [the new gateway configuration](/en/docs/mt5/platform/administration/admin_gateways):

![Gateway settings](/en/docs/mt5/platform/img/fxcm_common.png "Gateway settings")

Set the following parameters on the "Common" tab:

-   ID — unique dealer identifier, on whose behalf the trade requests will be processed. Requests are routed to the gateway according to this identifier.
-   Module — specify FXCMProGateway64 and accept the default settings after the module selection.
-   Trading server — FXCM Pro server IP-address and the port, where trade requests are processed. This information is provided by FXCM Pro as the SocketConnectHost and SocketConnectPort parameters. An encrypted SSL connection to a server is established by default. If you need to establish an unencryprted connection, additionally specify the /nossl key in the address bar. For example: 10.123.100.17:10219/nossl.
-   Trading login — login for connecting the trade flow corresponding to UserName tag (553) in FIX protocol. Provided by FXCM Pro.
-   Password — password for connecting the trade and quote flow corresponding to Password tag (554) in FIX protocol. Provided by FXCM Pro.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">ID value must be unique in the field of manager logins and gateway identifiers.</span></li><li class="p_tableatten"><span class="f_tableatten">The details for connection to the FXCM Pro server where trade requests are processed will be provided during the agreement conclusion.</span></li></ul></td></tr></tbody></table>

Now, go to the "Parameters" tab.

![Gateway parameters setup](/en/docs/mt5/platform/img/fxcm_param.png "Gateway parameters setup")

Specify the following parameters values here:

-   FIX Trade SenderCompID — standard parameter of the FIX messages heading used for a data sender identification. This parameter is provided by FXCM Pro as the value of SenderCompID (49).
-   FIX Trade TargetCompID — standard parameter of the FIX messages heading used for trading messages recipient identification. This parameter is provided by FXCM Pro as the value of TargetCompID (56).
-   FIX Trade TargetSubID — standard parameter of the FIX messages heading used for trading messages recipient identification. This parameter is provided by FXCM Pro as the value of TargetSubID (57).
-   FIX Market Data Address — IP address and port of the FXCM Pro server, from which market (price) data is transmitted. This information is provided by FXCM Pro as the SocketConnectHost and SocketConnectPort parameters. An encrypted SSL connection to a server is established by default. If you need to establish an unencryprted connection, additionally specify the /nossl key in the address bar. For example: 10.123.100.17:10219/nossl.
-   FIX Market Data SenderCompID — standard parameter of the FIX messages heading used for a market data sender identification. This parameter is provided by FXCM Pro as the value of SenderCompID (49).
-   FIX Market Data TargetCompID — standard parameter of the FIX messages heading used for market messages recipient identification. This parameter is provided by FXCM Pro as the value of TargetCompID (56).
-   FIX Market Data TargetSubID — standard parameter of the FIX messages heading used for market messages recipient identification. This parameter is provided by FXCM Pro as the value of TargetSubID (57).
-   FIX Market Data Log Enabled — if Yes, the gateway saves FIX connection (market flow) logs. Enable the parameter only in case of the gateway operation issues. The default value is No.
-   Limit Orders Coverage Mode — mode of processing Limit and Take Profit orders by the gateway. This parameter simplifies configuration of trade requests routing to the gateway, since there is no need to create a separate rule for routing the appropriate order types. Three processing modes are available:

-   -   Market — Limit and Take Profit orders are processed on the MetaTrader 5 platform side. If an order is activated, an appropriate market order is sent to FXCM Pro.
    -   Limit — Limit and Take Profit orders are processed on the MetaTrader 5 side.  
        Once a Limit order is triggered, an equivalent Limit order is sent to FXCM Pro. That order has a short action time specified in Limit Orders Coverage Timeout parameter. Since the price specified in the order is already present in the market, the order will be executed with that price — a market deal will be performed. If the necessary volume of the financial instrument is not available in the market at the specified price, the order will be executed partially. Thanks to a short expiration time, a Limit order with a residual volume will be removed from FXCM Pro. Thus, a client will have a market position as well as a Limit order with a residual volume, which will be further processed in a similar way on the side of MetaTrader 5.  
        A Limit order with the price equal to a Take Profit level is sent to FXCM Pro at the moment a Take Profit order has been activated. Since the price specified in the order is already present in the market, the order will be executed with that price — a market deal will be performed. If the necessary volume of the financial instrument is not available in the market at the specified price, the order will be executed partially. Thanks to a short expiration time, a Limit order with a residual volume will be removed from FXCM Pro. Therefore, a client's position will be closed partially. Control over the Take Profit position level with the remaining volume will then be carried out on the MetaTrader 5 side.  
        Limit mode allows to protect against slippage, as a Limit order is sent to FXCM Pro system with a specified price rather than a market order for execution by the current price. In addition, this mode allows you not to reserve margin on a client's account before sending an order to FXCM Pro.
    -   Gateway — Limit orders are processed on FXCM Pro side. Once a Limit order has been placed by a client, an appropriate order is sent to FXCM Pro. Take Profit orders are processed the same way as in the Limit mode.
-   Limit Orders Coverage Timeout — duration of Limit orders sent to FXCM Pro in Limit mode. Specified in seconds. The default value is 5.
-   Stop Orders Coverage — mode of handling Stop and Stop Limit orders. In case of 'Y' value, these order types will be transferred to FXCM Pro directly. In case of 'N' value, the orders will be processed inside MetaTrader 5 platform until their stop price is reached. After a Stop order is activated, an appropriate market order will be sent to the FXCM Pro system. After a Stop Limit order has been activated, a Limit order is created, which will be processed according to Limit Orders Coverage Mode parameter value.
-   Account Mapping Mode — the gateway supports several [modes of trade operation transferring](/en/docs/mt5/platform/components/gateways/fxcmpro#multiaccount) to FXCM PRO: on behalf of the broker's general account and on behalf of the individual accounts used for trading in the MetaTrader 5 platform. Three modes of trades operations transfer are available:
    -   omnibus — all orders will be sent to FXCM PRO on behalf of the broker's main account specified in the "Account Mapping" parameter.
    -   one-to-one — all orders will be sent to FXCM PRO on behalf of individual accounts on which the orders are placed in MetaTrader 5 (an external system account is specified in the settings of each account).
    -   conversion — combination of the previous two modes: orders of the accounts that have specified external system account will be sent on their own behalf, while all other orders will be transferred on behalf of the broker's general account.
-   Account Mapping — the number of the single account in the FXCM PRO system, on behalf of which clients' orders will be sent if the "Account Mapping Mode" parameter is set to "omnibus" or "conversion".
-   Quotes Delay — delay of transmitted quotes in seconds. The maximum duration of quotes delay is 20 minutes (1200 seconds). The flow of delayed quotes is neither thinned out, nor changed. A quote is passed to MetaTrader 5 History Server only after the expiration of delay period since the quote has arrived to Gateway API. If the temporary delay parameter is not defined, the quote delay is not used. Changes in depth of market and price statistics are delayed together with the quotes flow.
-   Quotes Tickstats Sample — the minimum frequency of sending price statistics in milliseconds. This parameter allows thinning out updates of price statistics reducing the traffic.
-   Quotes Ticks Sample — the minimum frequency of sending quotes in milliseconds. This parameter allows thinning out updates of quotes reducing the traffic. It is recommended for use on demo servers only.
-   Quotes Books Sample — the minimum frequency of depth of market updates in milliseconds. This parameter allows thinning out updates of the depth of market reducing the traffic. It is recommended for use on demo servers only.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">In no circumstances it is allowed to change operations transfer mode while in operation. Changing the mode is allowed only after all client positions are closed.</span></li><li class="p_tableatten"><span class="f_tableatten">Margin reservation of the clients should be configured for the appropriate order types <a href="/en/docs/mt5/platform/components/gateways/fxcmpro#margin" class="topiclink">in case Limit, Stop and/or Stop Limit orders</a> are directly transferred to an external system.</span></li></ul></td></tr></tbody></table>

The next stage is to specify the groups of the clients, whose requests will be processed via the MetaTrader 5 Gateway to FXCM Pro, as well as symbols, by which the gateway processes trading operations and broadcasts quotes.

![Configuring groups and symbols](/en/docs/mt5/platform/img/fxcm_groups_symbols.png "Configuring groups and symbols")

Make sure to enable "Allow importing symbol settings" option. The gateway imports symbols from FXCM Pro to Symbols/Preliminary/FXCM directory of the MetaTrader 5 and manages their parameters.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Initially, all imported symbols have trading ability disabled. System administrator must relocate imported symbols to the proper subgroup and allow trading for them.</span></li><li class="p_tableatten"><span class="f_tableatten">After symbols are relocated and trading abilities are enabled, the main trading server must be restarted.</span></li><li class="p_tableatten"><span class="f_tableatten">In case the gateway transmits configuration for the symbol that is already present in the platform, the configuration is updated. In this case, the symbol is not transferred and its trading ability is not turned off.</span></li><li class="p_tableatten"><span class="f_tableatten">The gateway supports conversion of symbols and quotes. For details, please view the <a href="/en/docs/mt5/platform/administration/admin_gateways/gateway_translation" class="topiclink">Symbol and Price Translation</a> section.</span></li></ul></td></tr></tbody></table>

## Margin Setup [#](fxcmpro#margin)

Margin reservation of the clients should be configured for the appropriate order types in case Limit, Stop and/or Stop Limit orders are directly transferred to an external system.

The external system checks the funds that are necessary to provide any type of order placed via the gateway. However, the check is performed on the broker's general account, on behalf of which the work is carried out.

By default, the margin is charged on the side of MetaTrader 5 only when market orders are placed. When placing pending orders in an external system, the client's available funds should be controlled on the side of MetaTrader 5 before the orders are transferred to avoid using all broker's funds by the client.

After an order has been transferred to the external system, MetaTrader 5 platform is not able to check the client's margin sufficiency any more. After the order has been executed in the external system, the gateway cannot ignore that fact. Therefore, the appropriate trading operation is performed in the platform.

Set non-zero coefficients for the orders directly transferred to the external trading system in symbol settings for the appropriate symbols:

![Margin setup](/en/docs/mt5/platform/img/integral_margin_allorders.png "Margin setup")

## Configuring Trade Requests Routing [#](fxcmpro#routing)

Configure the routing to let the clients requests to be transmitted to the FXCM Pro gateway. To do this, add a routing rule to the relevant [MetaTrader 5 Administrator](/en/docs/mt5/platform/administration/requests_routing) section.

Select "Process to dealers" as an action in common settings. Assign this routing rule for all requests and orders. In additional conditions, indicate groups of clients, whose requests will be passed to the gateway.

In the screenshots below all orders created by users in the real\\fxcm\\\* groups by symbols from the FXCM\\\* section will be sent to the gateway for processing.

![Configuring trade requests routing](/en/docs/mt5/platform/img/fxcm_routing.png "Configuring trade requests routing")

After the correct execution of the steps described above, the gateway will be ready for work.

## Configuring Trading Accounts [#](fxcmpro#multiaccount)

MetaTrader 5 GateWay to FXCM PRO allows transferring trading operations to an external system in different modes. The trading orders that are placed by clients in the MetaTrader 5 platform, can be sent to FXCM PRO on behalf of the broker's general account (specified in the [Account Mapping"](/en/docs/mt5/platform/components/gateways/fxcmpro#account_mapping) parameter of the gateway settings) or on behalf of the clients' individual accounts. In the latter case, the gateway connects to FXCM PRO via the broker's general account, but clients' trading operations are sent to FXCM PRO using individual accounts.

-   Order transferring mode is controlled by the [Account Mapping Mode](/en/docs/mt5/platform/components/gateways/fxcmpro#account_mapping) parameter in the gateway configuration.
-   Trading operations transfer conditions are determined when concluding an agreement between a brokerage company and FXCM PRO.
-   In no case should you change the operation transfer mode during operation. Changing the mode is allowed only when all client positions have been closed.

If you send trading operations using individual client accounts, the appropriate FXCM PRO account number must be specified in each account's settings. This can be done via the [administrator](/en/docs/mt5/platform/administration/admin_accounts/account_edit#trade_accounts) or [manager](https://support.metaquotes.net/en/docs/mt5/manager/management/management_accounts/account_view/account_view_account) terminal:

![Client's account in the external trading system](/en/docs/mt5/platform/img/fxcm_account.png "Client's account in the external trading system")

In "Trade accounts" section, select FXCM PRO gateway configuration and specify the client's account in the external system. That is the account, from which client trade operations will be transferred to FXCM PRO.

Client account numbers are provided by FXCM PRO.

## Changing Symbols Names and Markups [#](fxcmpro#markup)

The gateway receives the prices from FXCM PRO and transmits them to clients considering markups. Thus, a brokerage company receives its profit share from each deal performed at FXCM Pro. Markup values are set separately for Bid and Ask prices by each symbol:

![Changing symbol names and price correction](/en/docs/mt5/platform/img/fxcm_translation.png "Changing symbol names and price correction")

Besides, you can configure matching of symbol names used in FXCM Pro with the names used in your MetaTrader 5 platform. For example, if the symbol name in FXCM Pro is EURGBPFXCM, and it is called EURGBP in MetaTrader 5, enter EURGBP in the "Symbol" field and EURGBPFXCM in the "Source" field.

The above screenshot shows price conversion: at every tick, the Bid price will be reduced by 3 points, and the Ask price will be increased by 2 points. Below is a schematic example of the conversion:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">FXCM Pro</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">ask price</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">ask price</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">FXCM Pro</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">FXCM Pro</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit execution</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83004</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td></tr><tr class="table"><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">MetaTrader 5 server</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">buy limit execution</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">EURGBP 0.83006</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">&gt;&gt;&gt;</span></p></td><td class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable">Client terminal</span></p></td></tr></tbody></table>

A broker gains 2 pips of profit in this example. The price is sent to the client terminal only after the correction, so the clients work only with the corrected prices. If no correction is set for a symbol, the client will work with the original prices submitted by FXCM Pro.

## Prices Round Off

During the gateway's operation, accuracy of quotes (decimal places) passed for some symbol may change in the external trading system. Decrease in price accuracy at the external trading system's side does not affect the gateway's operation. It still transmits prices with less accuracy. However, if the number of decimal places at the external system's side increases, the gateway starts rounding off the passed prices.

Suppose that the accuracy of quotes has changed from 4 to 5 digits. Obtained five-digit quotes are rounded up in a broker's favor. Thus, buy requests of 1.23447, 1.23441 are rounded up to 1.2345, while sell ones of 1.23447, 1.23441 are rounded down to 1.23440.

Changes in symbol price accuracy are recorded in the gateway journal.

## Fill Policy and Order Expiration

When sending an order from the MetaTrader 5 client terminal, traders can set the order [execution policy](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#fill_policy) (FOK, IOC or Return) and [expiration time](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#expiration) (Good Till Canceled, Today, Date and Time, Date). In FXCM Pro trading system, the fill policy and expiration are set in a single parameter - Time in Force. Therefore, the gateway performs the following changes when passing the orders:

-   If FOK or IOC fill policy is set for an order, the same policy is applied in FXCM Pro system.
-   If a market order with Return fill policy is placed, it will be passed to FXCM Pro system in Good Till Canceled (GTC) mode.
-   If a limit order with Return fill policy is placed, expiration time from MetaTrader 5 (Good Till Canceled, Today, Specified, Specified Day) is inserted into the appropriate order parameter in FXCM Pro system.
-   If a limit order is activated in MetaTrader 5 platform and the gateway works in the mode of passing limit orders (Limit Orders Coverage Mode = Limit), a limit order with Good Till Date fill time policy is passed to FXCM Pro system. Limit Orders Coverage Timeout parameter also affects the order's lifetime. The gateway removes the placed order upon expiration of the specified time.
-   If a take profit position is activated in MetaTrader 5 platform and the gateway works in the mode of passing limit orders (Limit Orders Coverage Mode = Limit or Limit Orders Coverage Mode = Gateway), a limit order with Good Till Date fill time policy is passed to FXCM Pro system. Limit Orders Coverage Timeout parameter also affects the order's lifetime. The gateway removes the placed order upon expiration of the specified time.

[LMAX Global](/en/docs/mt5/platform/components/gateways/lmax)

[Borsa Istanbul](/en/docs/mt5/platform/components/gateways/borsa)