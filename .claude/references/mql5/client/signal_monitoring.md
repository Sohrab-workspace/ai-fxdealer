# How to Choose a Signal

> Source: https://support.metaquotes.net/en/docs/mt5/client/signal_monitoring

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
            -   [How to Choose a Signal](/en/docs/mt5/client/signal_monitoring)
            -   [How to Subscribe to a Signal](/en/docs/mt5/client/signal_subscriber)
            -   [How to Become a Signal Provider](/en/docs/mt5/client/signal_provider)
        -   [Market App Store](/en/docs/mt5/client/market)
        -   [MQL5 Cloud Network](/en/docs/mt5/client/mql5cloud)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Trading Signals and Copy Trading](/en/docs/mt5/client/signals)How to Choose a Signal

# How to Choose a Signal

Every signal is provided with a detailed performance report: growth, balance and equity charts, multiple statistical values, full trading history and more.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/ntu6pZRopq4/video.mp4" target="_blank" title="Watch video: Trading signals showcase"><img class="help" alt="Watch video: Trading signals showcase" title="Watch video: Trading signals showcase" width="142" height="80" src="/en/docs/mt5/client/img/video_signals_showcase.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Trading signals showcase</span></p><p class="p_fortable"><span class="f_fortable">How to choose a trading signal and subscribe to it in a couple of clicks It is easy! Watch the video to find out everything about trading signals.</span></p></td></tr></tbody></table>

To open the showcase, go to the "Navigator \\ Signals" section. It features signal widgets with basic information:

![Signals showcase](/en/docs/mt5/client/img/toolbox_signals.png)

### Growth chart

This chart enables the visual evaluation of the signal performance.

### Rating

Sort signals by rating which is calculated based on a set of performance metrics, such as growth, drwadown, lifetime and others.

### Signal/Equity

Switch between signal sorting by name and by account equity.

### Growth/Weeks

Switch between signal sorting by growth rate and by the number of weeks since the first trade on the account.

### Subscribers/Funds

Switch between signal sorting by the number of subscribers and by the amount of subscribers' funds managed by this signal (only the funds on real accounts within the set risks).

### Trades/Profitable

Switch between signal sorting by the number of trades on the account and by the percentage of winning deals. A small number of trades cannot characterize trading, while the obtained profit can be random.

### Max DD/PF

Switch between signal sorting by the maximum drawdown and by the profit factor.

### Price

Sort signals by subscription cost.

### Growth

Deposit growth in percentage value calculated based on trading operation results, excluding withdrawals and top-up operations. Growth is one of the main characteristics, based on which you can evaluate the signal performance.

### Weeks

Account lifetime which starts on the first performed trade (this refers to the entire account lifetime rather than the period since its registration as a signal). The older the signal, the more trading information is available. Be careful subscribing to too young signals.

### Reliability

Reliability evaluates in % the risks of this signal relative to others. The higher the variable, the more reliable the signal.

### Algo trading

The share of deals performed by trading robots or scripts.

### Subscribers

The current number of signal subscribers.

### Price

Monthly subscription fee in USD.

By default, all signals are sorted by rating, that is by a complex metric based on profits, drawdowns, risks and many other criteria. Use the upper panel to search signals by a specific metric, such as the number of subscribers or price. The first click sorts the showcase by the first parameter and the second click switches to the second parameter.

For convenience, the signals showcase adapts depending on your account type:

-   Only the first one thousand of signals sorted by rating are featured on the platform showcase. Other signals can be found via [MQL5.community](https://www.mql5.com/en/signals "Signals on MQL5.community") or by using [search](/en/docs/mt5/client/interface#search).
-   Signals that are incompatible with the current account are also hidden from the showcase.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/2Dk7UdpnWZg/video.mp4" target="_blank" title="Watch video: Detailed statistics of a trading signal"><img class="help" alt="Watch video: Detailed statistics of a trading signal" title="Watch video: Detailed statistics of a trading signal" width="142" height="80" src="/en/docs/mt5/client/img/video_signals_param.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Detailed statistics of a trading signal</span></p><p class="p_fortable"><span class="f_fortable">For your convenience, the most valuable parameters of trading signals are placed in a separate block. From this video you will find out where to find them and what to pay attention to.</span></p></td></tr></tbody></table>

Click on a signal to view its details.

![Detailed information about the signal](/en/docs/mt5/client/img/toolbox_signals_view.png)

### General information about the signal

-   Signal name.
-   Signal author's avatar and country.
-   Signal author's name. Click on the name to view the author's profile at MQL5.community. From the profile, you can also write a message to the author.
-   Monthly subscription fee in USD.

### Main signal characteristics

-   Growth — deposit growth in percentage value calculated on the basis of the account trading history, excluding deposits and withdrawals.
-   Balance — funds on the account, not including the floating profit of currently open orders.
-   Profit — profit/loss gained during the account lifetime.
-   Reliability — evaluates in % the risks of this signal compared to others. The higher the value, the more reliable the signal.
-   Weeks — the number of weeks since the first trade performed on the trading account (this parameter considers the entire account lifetime rather than the period since its registration as a signal).
-   Subscribers — the current number of signal subscribers.

### Visualize on chart

[View the signal trading history](/en/docs/mt5/client/signal_monitoring#show_on_chart) on charts in the trading platform. This command opens charts of the symbols that have ever been traded on the signal account. All performed deals will be displayed with the relevant icons.

### View on MQL5

Go to the signal page at MQL5.community.

### To Favorites

If you like a signal, add it to [favorites](/en/docs/mt5/client/signal_subscriber#favorites) to get back to it later.

### Extended signal statistics

-   Subscribers — the current number of signal subscribers.
-   Subscribers' funds — the total amount of subscribers' funds managed by this signal. The value only reflects funds on real accounts, within the used risks.
-   Maximal Drawdown — the largest balance or equity drop from the local maximum, as a percentage. The parameter shows either balance or equity drawdown, depending on which value is higher (worse).
-   Weeks — the number of weeks since the first trade performed on the trading account (this parameter considers the entire account lifetime rather than the period since its registration as a signal).

### Trading data

-   Latest trade — time since the last trading operation on the signal provider's account.
-   Trades per week — the average number of trades per week.
-   Avg holding time — average position holding time.

### Provider account details

-   Broker — the name of the broker's server on which the account is registered.
-   Leverage — account leverage amount.
-   Trading mode — account trading mode: demo or real. Please note that a provider can afford much greater risks on a demo account than they would on a real one.
-   Expected slippage — slippage calculated based on trade copying statistics between the subscriber's and the provider's servers. The parameter is only available in the trading platform.

The radar chart provides a quick assessment of the main signal parameters:

-   Algo trading — the share of deals performed using trading robots or scripts.
-   Maximal Drawdown — the largest balance or equity drop from the local maximum, as a percentage. The parameter shows either balance or equity drawdown, depending on which value is higher (worse).
-   Max deposit load — the share of funds on the provider's account used for opening positions. The value is calculated as Margin/Equity\*100. It characterizes risks in trading. The larger the traded volume, the higher the potential profit but also the larger the potential loss.
-   Profit trades — the number of profitable trades and their share in the total number of trades, as a percentage.
-   Loss trades — the number of losing trades and their share in the total number of trades, as a percentage.
-   Trading activity shows the time when the account had open positions, as a percentage of the total monitoring monitoring time. Low activity indicates low-frequency trading or low position holding time (scalping).

### Provider account details

-   Equity — funds on the account including the results of currently open positions (floating profit/loss). The current account balance and the floating profit of open positions are additionally shown on hover.
-   Profit — amount of profit/loss gained during the account lifetime. The number of trades on the account is shown on hover.
-   Initial deposit — funds deposited at account opening.
-   Withdrawals — funds withdrawn from the account for its entire lifetime. The number of withdrawal operations is additionally shown on hover.

### Signal graphical data

The tabs present signal performance [charts and diagrams](/en/docs/mt5/client/signal_monitoring#graphs): growth charts, equity and balance graphs, distribution of deals by symbols, risk data and reviews from signal subscribers.

## How to View the Signal Trading History on a Chart [#](signal_monitoring#show_on_chart)

To visually evaluate the effectiveness of how the provider enters and exits the market, you can display all of the trades on charts in the trading platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/c4E1YpjKwKo/video.mp4" target="_blank" title="Watch video: Visualize a signal on a chart"><img class="help" alt="Watch video: Visualize a signal on a chart" title="Watch video: Visualize a signal on a chart" width="142" height="80" src="/en/docs/mt5/client/img/video_signals_chart.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Visualize a signal on a chart</span></p><p class="p_fortable"><span class="f_fortable">The effectiveness of entry points and the unrealized profit can be easily assessed with the visualized chart of provider's deals.</span></p></td></tr></tbody></table>

Select![Visualize](/en/docs/mt5/client/img/visualize_icon.png "Visualize"). All the charts of symbols traded on the signal account are opened. The icons ![Buy](/en/docs/mt5/client/img/buy_icon.png "Buy") and ![Sell](/en/docs/mt5/client/img/sell_icon.png "Sell") on these charts show all trades performed on the signal account.

![View the signal trading history on a chart](/en/docs/mt5/client/img/signals_show_on_chart.png "View the signal trading history on a chart")

## Growth, Equity and Balance Graphs [#](signal_monitoring#graphs)

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/cjcaKKLf6aY/video.mp4" target="_blank" title="Watch video: Trade statistics, growth, equity &amp; balance graphs"><img class="help" alt="Watch video: Trade statistics, growth, equity &amp; balance graphs" title="Watch video: Trade statistics, growth, equity &amp; balance graphs" width="142" height="80" src="/en/docs/mt5/client/img/video_signals_stat.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Trade statistics, growth, equity &amp; balance graphs</span></p><p class="p_fortable"><span class="f_fortable">Trade statistics provide detailed information about a signal, to help you make a wise decision. Growth, equity &amp; balance graphs allow you to visually evaluate a successful provider.</span></p></td></tr></tbody></table>

These charts mainly show the profitability of the signal.

![Growth, Equity and Balance Graphs](/en/docs/mt5/client/img/signal_graph.png "Growth, Equity and Balance Graphs")

-   Growth — shows the growth of balance on the signal provider's account in percentage terms.
-   Equity — the chart shows both the equity curve and the balance curve. You should pay attention to the strong fall of equity relative to the balance. This indicates that the provider outstays the losses, which means an additional risk for the subscribers. Triangles ![Withdrawal](/en/docs/mt5/client/img/signal_withdrawal_icon.png "Withdrawal") and ![Deposit](/en/docs/mt5/client/img/signal_deposit_icon.png "Deposit") on the horizontal axes of the graph mark balance operations on the account — withdrawal and deposit. If you point the mouse cursor over it, the operation amount is displayed.
-   Balance — shows the growth of balance on the signal provider's account in money terms.

## Evaluating the Riskiness of the Signal

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/KqDhr1kumRM/video.mp4" target="_blank" title="Watch video: Risks, distribution, news and reviews of trading signals"><img class="help" alt="Watch video: Risks, distribution, news and reviews of trading signals" title="Watch video: Risks, distribution, news and reviews of trading signals" width="142" height="80" src="/en/docs/mt5/client/img/video_signals_risk.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Risks, distribution, news and reviews of trading signals</span></p><p class="p_fortable"><span class="f_fortable">How risky does your provider trade and what do other subscribers think of that? Watch this video to find the answers to these questions.</span></p></td></tr></tbody></table>

All risk evaluation metrics are available under the Risks section.

The first two graphs are the following:

-   Drawdown by equity — the largest equity drop from the local maximum, as a percentage. The larger the drawdown, the more risks the provider allows.
-   Deposit load — the share of funds on the provider's account used for opening positions. The value is calculated as Margin/Equity\*100. It characterizes risks in trading. The larger the traded volume, the higher the potential profit, but also the larger the potential loss.

These two charts only reflect data for the monitoring period; they are not calculated for the entire account history.

![Deposit load and equity drawdown graphs](/en/docs/mt5/client/img/signal_load_drawdown.png "Deposit load and equity drawdown graphs")

The following statistical rates are displayed below the graphs:

-   Best trade — trade having the highest profit among all profitable ones;
-   Worst trade— trade having the worst loss among all loss-making ones;
-   Max. consecutive wins — the amount of trades in the longest profitable sequence and its total profit;
-   Max. consecutive losses — the amount of trades in the longest losing sequence and its total loss;
-   Max. consecutive profit — the largest profit in a continuous profitable sequence and the amount of appropriate profitable trades;
-   Max. consecutive loss — the largest loss in a continuous losing sequence and the amount of the appropriate losing trades.

Below are MFE and MAE distribution point graphs.

![MFE and MAE distribution graphs](/en/docs/mt5/client/img/signal_monitoring_risk.png "MFE and MAE distribution graphs")

Maximum profit (MFE) and maximum loss (MAE) values are recorded for each open order during its lifetime. These parameters additionally characterize each closed order using the values of the maximum unrealized potential and maximum permitted risk. MFE/Profit and MAE/Profit distribution graphs display each order as a point with received profit/loss value plotted along the X-axis, while maximum displayed values of potential profit (MFE) and potential loss (MAE) are plotted along the Y-axis.

If you place cursor over a position point on a graph, the same position point will be highlighted on the other graph. Thus you can analyze both potential profit and loss of every position.

The following statistical rates are displayed below the graphs:

-   Best trade — trade having the highest profit among all profitable ones;
-   Worst trade— trade having the worst loss among all loss-making ones;
-   Max. consecutive wins — the amount of trades in the longest profitable sequence and its total profit;
-   Max. consecutive losses — the amount of trades in the longest losing sequence and its total loss;
-   Max. consecutive profit — the largest profit in a continuous profitable sequence and the amount of appropriate profitable trades;
-   Max. consecutive loss — the largest loss in a continuous losing sequence and the amount of the appropriate losing trades.

If you place cursor over a rate, the corresponding trades will be highlighted on the graphs.

When you hover over the statistics above, the relevant trades are highlighted on the MFE and MAE graphs.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Deposit load, drawdown, MAE and MFE graphs are only available on <a href="https://www.mql5.com/en/signals" target="_blank" class="weblink" title="MQL5.community">MQL5.community</a>. The trading platform only contains risk statistics.</span></li><li class="p_tableatten"><span class="f_tableatten">Find out more about MAE and MFE distributions in the article <a href="https://www.mql5.com/en/articles/1492" target="_blank" class="weblink" title="Article: Mathematics in Trading. How to Estimate Trade Results">Mathematics in Trading. How to Estimate Trade Results</a>.</span></li></ul></td></tr></tbody></table>

## Financial Instruments and Trading Direction in a Signal

The "Distribution" tab shows the number of trade operations displayed by symbols. It also contains the distribution of trades based on direction (Buy and Sell):

![Distribution of trade operations by symbols and by type](/en/docs/mt5/client/img/signal_monitoring_distribution.png "Distribution of trade operations by symbols and by type")

## Slippage during copy trading

The Slippage tab displays average slippage when executing trade operations on the servers of various brokers.

![Slippage](/en/docs/mt5/client/img/signal_monitoring_slippage.png "Slippage")

The average slippage is calculated based on statistics of trading signals execution at different brokers. Statistics is gathered for all signals at the provider's server. The difference between the order price placed by the signal provider and the order execution price at the subscriber's server is defined. The average value is calculated based on these data.

Number of slippage points is displayed according to the price accuracy (number of decimal places) at the signal provider's side.

Slippage can be caused by differences in quotes on the servers or trade execution delays. The lower the slippage, the higher the accuracy of the signal copying.

A separate tab provides statistics on the slippage for subscribers who copy signals on a [VPS](/en/docs/mt5/client/virtual_hosting). By choosing a VPS located close to the broker's servers, subscribers can significantly reduce slippage. You can evaluate connection improvement by checking out real statistics.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The access statistics is only available on <a href="https://www.mql5.com/en/signals" target="_blank" class="weblink" title="MQL5.community">MQL5.community</a>. Click "View on MQL5" to open the signal page.</span></p></td></tr></tbody></table>

## User Reviews about the Signal

On the "Reviews" tabs, MQL5.community members can express their opinion on the signal. Before you subscribe to a signal, check out the comments of other subscribers.

![Reviews](/en/docs/mt5/client/img/signal_monitoring_review.png "Reviews")

You can also leave your feedback after subscribing to the signal. Assist other community members in making the right choice. Select "Add a review" to go to the signal page at MQL5.community, where you can add your review.

## Signal News

Using tab "News", the signal provider can inform subscribers about any changes in the signal operations as well as provide any other useful information. If no news is published, this tab is not displayed.

## Trading and Statistics

Detailed account trading statistics, as well as currently open positions and the history of trades are displayed below the chart.

![Signal trading statistics](/en/docs/mt5/client/img/signal_trade_stat.png)

### Trade Statistics

-   Total Trades — the total number of trades (deals that lock profit or loss).
-   Profit Trades — the number of profitable trades and their share in the total number of trades in percentage value.
-   Loss Trades — the number of losing trades and their share in the total number of trades in percentage value.
-   Best trade — trade with the highest profit among all profitable trades.
-   Worst trade — trade with the largest loss among all loss-making trades.
-   Gross Profit — the sum of all profitable trades in monetary units.
-   Gross Loss — the sum of all loss-making trades in monetary units.
-   Max consecutive wins — the number of trades in the longest profitable sequence and its total profit.
-   Max consecutive profit — the largest profit in a continuous profitable sequence and the amount of appropriate profitable trades.
-   Sharpe Ratio — this parameter shows strategy efficiency and reliability. The value reflects the ratio of the arithmetical mean profit for the position holding time to the standard deviation from it. The risk-free rate, which is the profit gained from the appropriate bank deposit funds is also taken into account here.

### Trade Statistics

-   Recovery Factor — this parameter displays the risk level of the strategy (the funds that are put to risk to earn the obtained profit). It is calculated as the ratio of gained profit to the maximum drawdown.
-   Long Trades — the number of trades fixing profit from long deals and the number of profitable long trades in percentage value.
-   Short Trades — the number of trades fixing profit from short deals and the number of profitable short trades in percentage value.
-   Average Profit — the average profit from all profitable trades.
-   Average Loss — the average loss from all loss-making trades.
-   Profit Factor — ratio between gross profit and gross loss. One means that these parameters are equal.
-   Expected Payoff is a statistically calculated parameter displaying average profitability/unprofitableness of one trade. Also, it is considered to display the expected return of the next trade.
-   Max consecutive losses — the number of trades in the longest losing sequence and its total loss.
-   Max consecutive loss — the largest loss in a continuous losing sequence and the amount of the appropriate losing trades.
-   Monthly growth — the average deposit growth for a month in percentage values. The value is calculated as the total growth divided by the number of months traded.
-   Annual Forecast — deposit growth forecast for a year according to the monitoring period results.

### Open Positions

-   Symbol — the financial instrument of the open position.
-   Time — position opening time. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute).
-   Type — position type: "Buy" — long, "Sell" — short.
-   Volume — trade operation volume (in lots). The minimum volume and its change step are limited by a brokerage company, the maximum amount — by the deposit size.
-   Price — the price of a deal, as a result of which the position was opened. If the opened position is a result of execution of several deals, then this field displays their weighted average price: (price of deal 1 \* volume of deal 1 + ... + price of deal N \* volume of deal N) / (volume of deal 1 + ... + volume of deal N). The accuracy of rounding of the weighted average price is equal to the number of decimal places in the symbol price plus three additional characters.
-   S/L — [the Stop Loss level](/en/docs/mt5/client/general_concept#stop_loss) of the current position. If this order has not been placed, a zero value is displayed in this field.
-   T/P — [the Take Profit level](/en/docs/mt5/client/general_concept#take_profit) of the current position. If this order has not been placed, a zero value is displayed in this field.
-   Price — the current price of the financial symbol. Bid price is displayed for short positions, while Ask price is used for long ones. The price of the last performed deal (Last) is displayed for the positions of exchange symbols (both directions).
-   Swap — amount of swaps charged.
-   Profit — the financial result of the trade taking into account the current price is written in this field. The positive result tells that the trade is profitable, negative shows that it's losing.

### Pending Orders

-   Symbol — the financial instrument of the pending order.
-   Time — pending order placing time. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute).
-   Type — [pending order type](/en/docs/mt5/client/general_concept#pending_order): "Sell Stop", "Sell Limit", "Buy Stop", "Buy Limit", "Buy Stop Limit" or "Sell Stop Limit".
-   Volume — volume requested in the pending order, and volume covered by the deal (in lots).
-   Price — price reaching which the pending order will trigger.
-   S/L — the level of the [Stop Loss](/en/docs/mt5/client/general_concept#stop_loss) order. If this order has not been placed, a zero value is displayed in this field.
-   T/P — the level of the [Take Profit](/en/docs/mt5/client/general_concept#take_profit) order. If this order has not been placed, a zero value is displayed in this field.
-   Price — the current price of the financial symbol. Bid price is displayed for short orders, while Ask price is used for long ones. The price of the last performed deal (Last) is displayed for the orders involving exchange symbols (both directions).

### The history of trades on the signal

-   Time — the time of a trade. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute).
-   Symbol — a financial instrument of the deal.
-   Type — trading operation type: "Buy" — a buy deal, "Sell" — a sell deal. It is possible that previously performed deal can be canceled. In this case, the type of the previously performed deal is changed to Canceled buy or Canceled sell, and its profit/loss is reset to zero. Previously gained profit/loss is deposited/withdrawn from an account in a separate balance operation.
-   Direction — direction of the deal relative to the current position of a particular symbol: "in", "out" or "in/out".
-   Volume — the volume of an executed deal (in lots).
-   Price — price the deal was executed at.
-   Swap — amount of swaps charged.
-   Profit — the financial result of the position exiting. For entry trades the zero profit is shown.

## How to Add a Signal to Favorites [#](signal_monitoring#favorites)

A huge number of signals are available for subscription. When searching for signals, you can add any of them to Favorites in order to select the best one. To add a signal to or to remove it from Favorites, select![Add to Favorites](/en/docs/mt5/client/img/signal_favorite_icon.png "Add to Favorites")on the signal page.

All favorite signals are displayed under a separate section:

![Favorites](/en/docs/mt5/client/img/signal_favorites.png "Favorites")

[Trading Signals and Copy Trading](/en/docs/mt5/client/signals)

[How to Subscribe to a Signal](/en/docs/mt5/client/signal_subscriber)