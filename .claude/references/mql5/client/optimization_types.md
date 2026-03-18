# Optimization Types

> Source: https://support.metaquotes.net/en/docs/mt5/client/optimization_types

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
            -   [Expert Advisors and Custom Indicators](/en/docs/mt5/client/trade_robots_indicators)
            -   [Where to Find Trading Robots and Indicators](/en/docs/mt5/client/algotrading_get_ea_indicator)
            -   [How to Create an Expert Advisor or an Indicator](/en/docs/mt5/client/autotrading)
            -   [Strategy Testing](/en/docs/mt5/client/testing)
            -   [How the Tester Downloads Historical Data](/en/docs/mt5/client/test_preparation)
            -   [Strategy Optimization](/en/docs/mt5/client/strategy_optimization)
            -   [Testing Features](/en/docs/mt5/client/testing_features)
            -   [Testing Report](/en/docs/mt5/client/testing_report)
            -   [Testing Visualization](/en/docs/mt5/client/visualization)
            -   [Journal of Testing](/en/docs/mt5/client/tester_journal)
            -   [Optimization Types](/en/docs/mt5/client/optimization_types)
            -   [Real and Generated Ticks](/en/docs/mt5/client/tick_generation)
            -   [MetaTester and Remote Agents](/en/docs/mt5/client/metatester)
            -   [Global Variables](/en/docs/mt5/client/service_global)
        -   [Trading Signals and Copy Trading](/en/docs/mt5/client/signals)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)Optimization Types

# Optimization Types

Two optimization types are available in the tester. You can select the appropriate one on the [Settings](/en/docs/mt5/client/strategy_optimization#settings) tab of the Strategy Tester.

## Slow Complete Algorithm

In this mode, optimization runs are performed for all possible combinations of values of input variables selected on the [appropriate tab](/en/docs/mt5/client/strategy_optimization#inputs).

This method is the most precise one. However, running the Expert Advisor with all possible combinations takes much time.

## Fast Genetic Algorithm

This type of optimization is based on the genetic algorithm of search for the best values of input parameters. This type is much faster than the first one and is almost of the same quality. The slow complete optimization that would take several years can be performed within several hours using the genetic algorithm.

Each individual has a specific set of genes which corresponds to the set of their parameters. Genetic optimization is based on the constant selection of the most "adapted" parameters (values that give the best result). In the general form, the algorithm can be represented the following way:

-   From the total number of all possible combinations of parameters, two populations (sets) are selected by a random sample;
-   Both sets are tested and the one with the best results (according to the [optimization criterion](/en/docs/mt5/client/optimization_types#criterion)) is left;
-   The set members are randomly crossed with one another, undergoing random mutations and inversions of parameters;
-   The descendants are sorted out by the best results, and crossing repeats;
-   Sorting and crossing operations are repeated as long as there is improvement of results (the best result among descendants is better than the best one among the parents). If the [optimization criterion](/en/docs/mt5/client/optimization_types#criterion) values are not improved during several crossings (generations), the optimization process is completed.

### Number of Test Runs

During the genetic optimization, the number of test runs is much lower, which provides quickness of optimization. After the start of the genetic optimization, an estimated number of test runs is displayed on the [Settings](/en/docs/mt5/client/testing#settings) tab. It is calculated by the following formula:

Population size \* (Unconditional number of generations + Number of generations for convergence estimation)

where:

-   Population size is calculated based on the number of possible combinations of optimization parameters, may range from 64 to 256;
-   Unconditional number of generations may range from 15 to 31. It is defined by the presence of optimization criterion improvement. 15 generations are tested in all optimizations. If a generation within the range between 15 and 31 does not have any improvement of the optimization criterion, an additional test of the next generations is started for convergence estimation.
-   Number of generations for convergence estimation is calculated as one third of the unconditional number of generations. If the unconditional number of generation is 18 (the 17-th generation has shown the best result and there are no improvements shown by the 18-th generation) then another 5 generations are tested: the 18-th generation has not shown any improvement, and for the estimation of convergence we need 18/3 = 6 generations without improvements of the optimization criterion. If there are no improvements shown by the specified number of generations, optimization is stopped.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If the total number of optimization steps exceeds 1,000,000 in a 32-bit system or 100,000,000 in a 64-bit system, the genetic optimization mode starts automatically.</span></li><li class="p_tableatten"><span class="f_tableatten">During the <a href="/en/docs/mt5/client/optimization_types" class="topiclink">genetic optimization</a>, intermediate results are saved in cache after the calculation of each generation (in a file platform_data_folder/tester/cache/*.gen). Thus the optimization process can be interrupted at any time. Even if the process of genetic optimization is interrupted as a result of an external factor (for example, power failure), the optimization will be automatically continued from the last calculated generation at the next start. The genetic optimization cache is stored until the <a href="/en/docs/mt5/client/strategy_optimization#settings" class="topiclink">optimization settings</a> are changed or the optimization process is completed.</span></li><li class="p_tableatten"><span class="f_tableatten">At a regular optimization stop (when you press the <a href="/en/docs/mt5/client/strategy_optimization#settings" class="topiclink">Stop button</a>) all the previously calculated runs are saved. When the optimization process is resumed, it continues from the last calculated run.</span></li></ul></td></tr></tbody></table>

### Optimization Criterion [#](optimization_types#criterion)

An optimization criterion is a certain factor, which value defines the quality of a tested set of parameters. The higher the value of the optimization criterion, the better the testing result with the given set of parameters. Such a factor can be selected in a field to the right of "Optimization" on the [Settings](/en/docs/mt5/client/strategy_optimization#settings) tab.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The optimization criterion is required only for the genetic algorithm.</span></p></td></tr></tbody></table>

The following optimization criteria are available:

-   Balance max — the highest value of the balance.
-   Profit Factor max —  the highest value of the [profit factor](/en/docs/mt5/client/testing_report#profit_factor).
-   Expected Payoff max — the highest value of the [expected payoff](/en/docs/mt5/client/testing_report#expected_payoff).
-   Drawdown min — in this case, the [relative drawdown of balance](/en/docs/mt5/client/testing_report#drawdown) in percentage terms is taken into account.
-   Recovery Factor max — the highest value of the [recovery factor](/en/docs/mt5/client/testing_report#recovery_factor).
-   Sharpe Ratio max — the highest value of the [Sharpe ratio](/en/docs/mt5/client/testing_report#sharpe_ratio).
-   Custom max — the optimization criterion here is the value of the OnTester() function in the Expert Advisor. This parameter allows using any custom value for the optimization of Expert Advisors.

Another option is to use "Complex Criterion max". This is an integral and complex measure of a test pass quality. It measures multiple parameters:

-   Number of Deals
-   Drawdown
-   Recovery Factor
-   Expected Payoff
-   Sharpe Ratio

By using this criterion, you can see that the highest value of one parameter (for example the profit) is not always the best option in terms of the complex analysis. The complex criterion gradually selects the best passes: firstly, by the number of deals, then by the Expected Payoff, Recovery Factor, and so on. The new option allows reception of the best optimization passes according to all parameters. Furthermore, you can select the optimal pass based on the desired parameter, such as the highest profit.

## All Symbols Selected in Market Watch

Unlike the above described optimization types, this one allows to test an Expert Advisor with the same [input parameters](/en/docs/mt5/client/strategy_optimization#inputs), but with different symbols. Only the [main symbol of testing](/en/docs/mt5/client/strategy_optimization#settings) is changed in each pass, i.e. the symbol of chart the EA would be attached to.

Optimization is performed only for symbols that are currently chosen in the [Market Watch](/en/docs/mt5/client/market_watch). So you can manage optimization by adjusting the set of selected symbols.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Please note that downloading of necessary price data from the server may take a long time. However, the slowdown of optimization as a result of data downloading occurs only during the first launch for a symbol, next time only the missing data is downloaded.</span></li><li class="p_tableatten"><span class="f_tableatten">The current values of <a href="/en/docs/mt5/client/strategy_optimization#inputs" class="topiclink">input parameters</a> specified in the "Value" field are used for the optimization by symbols.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/client/strategy_optimization#cloud" class="topiclink">MQL5 Cloud Network</a> is not supported for this type of optimization.</span></li></ul></td></tr></tbody></table>

[Journal of Testing](/en/docs/mt5/client/tester_journal)

[Real and Generated Ticks](/en/docs/mt5/client/tick_generation)