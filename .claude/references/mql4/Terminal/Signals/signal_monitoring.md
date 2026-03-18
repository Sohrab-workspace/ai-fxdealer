# Account Monitoring

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/signals/signal_monitoring

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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Signals](/en/docs/mt4/terminal/signals)Account Monitoring

# Account Monitoring

The system of trade account monitoring is a part of "Signals" service. A detailed report can be received on any available signal.

A trade account can be monitored both via MQL5.community website and directly via the client terminal. Move to ["Signals" section](https://www.mql5.com/en/signals "MQL5.community Signals") on the website and select any signal to view its parameters:

![Account monitoring](/en/docs/mt4/terminal/img/signal_monitor.png "Account monitoring")

If you want to find data on a signal via the client terminal, open it in Signals tab of the [Terminal](/en/docs/mt4/terminal/overview/terminal/toolbox_signals) window.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/c4E1YpjKwKo/video.mp4" target="_blank" title="Watch video: Visualize a signal on a chart "><img class="help" alt="Watch video: Visualize a signal on a chart " title="Watch video: Visualize a signal on a chart " width="142" height="80" src="/en/docs/mt4/terminal/img/video_signals_chart.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Visualize a signal on a chart</span></p><p class="p_fortable"><span class="f_fortable">The effectiveness of the entry points and the unrealized profit can be easily assessed with the visualized chart of provider's deals.</span></p></td></tr></tbody></table>

![Signal monitoring](/en/docs/mt4/terminal/img/toolbox_signals_view.png "Signal monitoring")

Data on a trading account is divided into several blocks.

## Basic Data

Basic data is located on the left side of the page.

-   Growth — growth of the deposit in percentage terms calculated on the basis of trade operation only without taking into the account the deposits and withdrawals.
-   Initial Deposit — amount of money deposited to the account when opening it.
-   Deposits — funds deposited on the account during its life time. This parameter should always be considered when evaluating the signal's profitability. The balance curve may be supported by regularly deposited funds.
-   Withdrawals — funds withdrawn from the account during its life time.
-   Balance — money on the account, not accounting the floating profit of currently open orders.
-   Equity — deposit funds accounting for the results of the currently open positions (floating profit/loss).
-   Profit — profit/loss gained during the life time of the account.

-   Subscribers — current amount of the signal subscribers.
-   Subscribers' funds — total funds used by the signal subscribers (deposit load selected in the copying settings is considered). Only funds on real accounts are considered.

-   Max drawdown — maximal balance drop relative to the local maximum in deposit currency.

-   Weeks — number of weeks that have passed since the first trade on the trading account was performed (the entire account lifetime instead of the period since its registration as a signal is considered).

-   Last trade — amount of time passed since the last trade operation on the account of the signal provider.

-   Trades per week — average number of trades per week.

-   Avg holding time — average time of holding an open position.

-   Broker — name of a broker server where the account is registered.
-   Leverage — leverage value.
-   Type — trading type: Demo, Contest (for example, the account for participation in the Automated Trading Championship) or Real. Please note that demo accounts allow traders to afford the risks that may be unacceptable for real accounts.
-   Author — author (MQL5.community account) name.

-   Expected slippage — slippage based on statistics concerning copying of trades between subscriber's and provider's servers. This parameter is available only in the trading terminal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/cjcaKKLf6aY/video.mp4" target="_blank" title="Watch video: Trade statistics, growth, equity &amp; balance graphs"><img class="help" alt="Watch video: Trade statistics, growth, equity &amp; balance graphs" title="Watch video: Trade statistics, growth, equity &amp; balance graphs" width="142" height="80" src="/en/docs/mt4/terminal/img/video_signals_stat.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Trade statistics, growth, equity &amp; balance graphs</span></p><p class="p_fortable"><span class="f_fortable">Trade statistics is a detailed information on a signal, that will help you to make a wise decision. Growth, equity &amp; balance graphs allow you to visually estimate a successful provider.</span></p></td></tr></tbody></table>

## Graphs

The following graphs are available in the monitoring system:

### Balance Growth

![Balance growth graph](/en/docs/mt4/terminal/img/signal_monitoring_graph.png "Balance growth graph")

The vertical line in the graph indicates the moment when the trade account was connected to the monitoring system. Triangles ![Withdrawal](/en/docs/mt4/terminal/img/signal_withdrawal_icon.png "Withdrawal") and ![Deposit](/en/docs/mt4/terminal/img/signal_deposit_icon.png "Deposit") displayed on horizontal axes indicate balance operations on the account - withdrawals and deposits. If you put the mouse cursor over it, the operation amount will be displayed.

Below the graph, you can find a table containing monthly and annual returns. To view the growth for a specific month on the chart, click the corresponding return value.

### Equity graph

![Equity graph](/en/docs/mt4/terminal/img/signal_monitoring_equity.png "Equity graph")

For higher informativeness the graph also includes the balance curve.

The vertical line in the graph indicates the moment when the trade account was connected to the monitoring system.

Triangles ![Withdrawal](/en/docs/mt4/terminal/img/signal_withdrawal_icon.png "Withdrawal") and ![Deposit](/en/docs/mt4/terminal/img/signal_deposit_icon.png "Deposit") displayed on horizontal axes indicate balance operations on the account - withdrawals and deposits. If you put the mouse cursor over it, the operation amount will be displayed.

### Balance Graph

![Balance graph](/en/docs/mt4/terminal/img/signal_monitoring_balance.png "Balance graph")

The vertical line in the graph indicates the moment when the trade account was connected to the monitoring system. Triangles ![Withdrawal](/en/docs/mt4/terminal/img/signal_withdrawal_icon.png "Withdrawal") and ![Deposit](/en/docs/mt4/terminal/img/signal_deposit_icon.png "Deposit") displayed on horizontal axes indicate balance operations on the account - withdrawals and deposits. If you put the mouse cursor over it, the operation amount will be displayed. Balance changes occurred as a result of withdrawals and deposits are additionally highlighted with red and green color respectively.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#f6f8fd;"><tbody><tr class="attentable"><td class="attentable" style="width:142px;"><p class="p_fortable"><a href="https://www.metatrader5.com/video/1/KqDhr1kumRM/video.mp4" target="_blank" title="Watch video: Risks, distribution, news and reviews of trading signals "><img class="help" alt="Watch video: Risks, distribution, news and reviews of trading signals " title="Watch video: Risks, distribution, news and reviews of trading signals " width="142" height="80" src="/en/docs/mt4/terminal/img/video_signals_risk.png"></a></p></td><td class="attentable"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Watch video: Risks, distribution, news and reviews of trading signals</span></p><p class="p_fortable"><span class="f_fortable">How risky your provider trades and what other subscriber think of that? Watch this video and we will answer your questions.</span></p></td></tr></tbody></table>

### Risks

This section displays MFE and MAE distribution point graphs.

![Risks](/en/docs/mt4/terminal/img/signal_monitoring_risk.png "Risks")

Maximum profit (MFE) and maximum loss (MAE) values are recorded for each open order during its lifetime. These parameters additionally characterize each closed order using the values of the maximum unrealized potential and maximum permitted risk. MFE/Profit and MAE/Profit distribution graphs display each order as a point with received profit/loss value plotted along the X-axis, while maximum displayed values of potential profit (MFE) and potential loss (MAE) are plotted along the Y-axis.

If you place cursor over a position point on a graph, the same position point will be highlighted on the other graph. Thus you can analyze both potential profit and loss of every position.

The following statistical rates are displayed below the graphs:

-   Best trade — trade having the highest profit among all profitable ones;
-   Worst trade — trade having the worst loss among all loss-making ones;
-   Maximum consecutive wins — the amount of trades in the longest profitable sequence and its total profit;
-   Maximum consecutive losses — the amount of trades in the longest losing sequence and its total loss;
-   Maximal consecutive profit — the largest profit in a continuous profitable sequence and the amount of appropriate profitable trades;
-   Maximal consecutive loss — the largest loss in a continuous losing sequence and the amount of the appropriate losing trades;

If you place cursor over a rate, the corresponding trades will be highlighted on the graphs.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">This tab is available at <a href="https://www.mql5.com/en/signals" target="_blank" class="weblink" title="MQL5.community">MQL5.community</a> only.</span></li><li class="p_tableatten"><span class="f_tableatten">You can find out more information about MAE and MFE distributions in the article <a href="https://www.mql5.com/en/articles/1492" target="_blank" class="weblink" title="Article: Mathematics in Trading: How to Estimate Trade Results">Mathematics in Trading: How to Estimate Trade Results</a>.</span></li></ul></td></tr></tbody></table>

### Distribution

On the "Distribution" tab you can find the number of trade operations displayed by symbols and by type (Buy and Sell):

![Distribution of trade operations by symbols and by type](/en/docs/mt4/terminal/img/signal_monitoring_distribution.png "Distribution of trade operations by symbols and by type")

### Slippage

Slippage tab displays average slippage when executing trade operations on the servers of various brokers.

![Slippage](/en/docs/mt4/terminal/img/signal_monitoring_slippage.png "Slippage")

The average slippage is calculated based on statistics of trading signals execution at different brokers. Statistics is gathered for all signals at the provider's server. The difference between the order price placed by the signal provider and the order execution price at the subscriber's server is defined. The average value is calculated based on these data.

Number of slippage points is displayed according to the price accuracy (number of decimal places) at the signal provider's side.

Slippage can be caused by differences in quotes on the servers or trade execution delays. The lower the slippage, the higher the accuracy of the signal copying.

### Reviews

On the "Reviews" tabs, MQL5.community members can express their opinion on the signal.

![Reviews](/en/docs/mt4/terminal/img/signal_monitoring_review.png "Reviews")

### News

Using this tab, the signal provider can inform subscribers about any changes in the signal operations as well as provide any other useful information. If no news are published, this tab is not displayed.

## Trade Statistics

Detailed account trading statistics can be found below the chart.

-   Trades — total number of trades (orders that fix profit or loss);
-   Profit Trades — number of profitable trades and their share in the total number of trades in percentage value;
-   Loss Trades — number of losing trades and their share in the total number of trades in percentage value;
-   Long Trades — number of buy orders fixing profit and amount of profitable long orders in percentage value;
-   Short Trades — number of sell orders fixing profit and amount of profitable short orders in percentage value;
-   Best trade — trade having the highest profit among all profitable ones;
-   Worst trade — trade having the worst loss among all loss-making ones;
-   Profit Factor — ratio between gross profit and gross loss. One means that these parameters are equal;
-   Gross Profit — sum of all profitable orders in monetary units;
-   Gross Loss — sum of all loss-making orders in monetary units;
-   Average Profit — average profit for all profitable orders;
-   Average Loss — average loss for all loss-making orders;
-   Recovery Factor — this parameter displays the risk level of the strategy (the funds that are put to risk to earn the obtained profit). It is calculated as the ratio of gained profit to the maximum drawdown;
-   Sharpe Ratio — this parameter shows strategy efficiency and reliability. It displays the ratio of the arithmetic mean profit during the time the position was open and the standard deviation from that profit. The risk-free rate, which is the profit gained from the appropriate bank deposit funds is also considered here;
-   Expected Payoff is a statistically calculated parameter displaying average profitability/unprofitableness of one trade. Also, it is considered to display the expected profitability/unprofitableness of the next trade;
-   Maximum consecutive wins — the amount of trades in the longest profitable sequence and its total profit;
-   Maximum consecutive losses — the amount of trades in the longest losing sequence and its total loss;
-   Maximal consecutive profit — the largest profit in a continuous profitable sequence and the amount of appropriate profitable trades;
-   Maximal consecutive loss — the largest loss in a continuous losing sequence and the amount of the appropriate losing trades;
-   Annual Forecast — deposit growth forecast for a year according to the monitoring period results;
-   Monthly growth — deposit growth for the last month in percentage values.

## Trading Operations

The lower part of the monitoring page displays a detailed data on trading operations on the account.

### Positions

Current open positions are shown in a table with the following fields:

-   Order — ticket number (a unique identifier) of the order;
-   Time — time when the position was opened. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Type — position type: "Buy" — long, "Sell" — short;
-   Volume — volume of a trade operation (in lots). The minimal volume and its change step are limited by a brokerage company, the maximal one — by the deposit size;
-   Symbol — a financial instrument of the open position;
-   Price — the open price of the position;
-   S/L — [Stop Loss level](/en/docs/mt4/terminal/positions/orders#stop_loss) for the current position. If this order was not placed, a zero value is shown in the field;
-   T/P — [Take Profit level](/en/docs/mt4/terminal/positions/orders#take_profit) for the current position. If this order was not placed, a zero value is shown in the field;
-   Price — the current price of the financial symbol. Bid price is displayed for short positions, while Ask price is used for long ones;
-   Commission — broker commission charged for the trade operation;
-   Swap — amount of swaps charged;
-   Profit — the financial result of the deal with the account for the current price is written in this field. A positive result indicates the profitability of the deal, negative one indicates the loss.

Placed pending orders are shown below:

-   Order — ticket number (a unique identifier) of the pending order;
-   Time — time when the pending order was placed. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Type — [type of the pending order](/en/docs/mt4/terminal/positions/orders): "Sell Stop", "Sell Limit", "Buy Stop" or "Buy Limit";
-   Volume — volume requested in the pending order (in lots);
-   Symbol — a financial instrument of the pending order;
-   Price — price of the pending order activation;
-   S/L — level of the placed [Stop Loss order](/en/docs/mt4/terminal/positions/orders). If this order was not placed, a zero value is shown in the field;
-   T/P — level of the set [Take Profit](/en/docs/mt4/terminal/positions/orders#take_profit) order. If this order was not placed, a zero value is shown in the field;
-   Price — the current price of the financial symbol. Bid price is displayed for short orders, while Ask price is used for long ones. The price of the last performed deal (Last) is displayed for the orders involving exchange symbols (both directions).

### History

This tab displays the history of orders on the trading account. The history of orders is also displayed in a table with the following fields:

-   Order — ticket number (a unique identifier) of an order;
-   Time — time of an order. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Type — type of a trade operation: "Buy" — a buy deal, "Sell" — a sell deal;
-   Volume — volume of an executed order (in lots);
-   Symbol — financial instrument of an order;
-   Price — price an order was executed at;
-   S/L — level of the placed [Stop Loss order](/en/docs/mt4/terminal/positions/orders). If this order was not placed, a zero value is shown in the field;

-   T/P — level of the set [Take Profit](/en/docs/mt4/terminal/positions/orders#take_profit) order. If this order was not placed, a zero value is shown in the field;
-   Time — time of closing a position. The record is represented as YYYY.MM.DD HH:MM (year.month.day hour:minute);
-   Commission — broker commission charged for the trade operation;

-   Swap — amount of swaps charged;

-   Profit — the financial result of the order closing;
-   Comment — comment to a trade operation.

[Signal Subscribers](/en/docs/mt4/terminal/signals/signal_subscriber)

[Market](/en/docs/mt4/terminal/market)