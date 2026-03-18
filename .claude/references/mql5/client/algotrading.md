# Algorithmic Trading, Trading Robots

> Source: https://support.metaquotes.net/en/docs/mt5/client/algotrading

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)Algorithmic Trading, Trading Robots

# Algorithmic Trading, Trading Robots

Algorithmic or automated trading is making buy and sell operations in the financial markets using special [trading robots](/en/docs/mt5/client/trade_robots_indicators). In the trading platform, these programs are also called Expert Advisors or EAs.

![Algorithmic trading](/en/docs/mt5/client/img/algotrading.png "Algorithmic trading")

Trading robots undertake price analysis based on preset algorithms, decision-making and, as a result, execution of trading operations in the market.

Trading robots are widely used in financial trading, and the share of automated operations relative to manual trading is constantly growing. A computer program has a variety of advantages:

-   It never gets tired
-   It is not susceptible to stress
-   It strictly follows a preselected algorithm
-   It rapidly responds to market changes.

### How to Start Creating Trading Robots

We have released two free books on MQL5 programming to help you master the creation of trading robots and applications for algorithmic trading.

These books offer a systematic and structured presentation of the material to make the learning process significantly easier. Detailed code examples, which explain the step-by-step creation of trading robots and applications, allow for a deeper understanding of algorithmic trading nuances. The books include numerous practical exercises to help reinforce the acquired knowledge and develop programming skills in real trading environments.

"[MQL5 Programming for Traders](https://www.mql5.com/en/book "MQL5 Programming Book")" is the most complete and detailed tutorial on MQL5, suitable for programmers of all levels. Beginners will learn the basics: the book introduces development tools and basic programming concepts. Based on this material, you will create, compile and run your first application in the MetaTrader 5 trading platform. Users with experience in other programming languages can directly proceed to the applied sections: creating trading robots and analytical applications in MQL5.

"[Neural Networks in Algorithmic Trading with MQL5](https://www.mql5.com/en/neurobook "Book on Neural Networks with MQL5, OpenCL and Python")" is a guide to using machine learning methods in trading robots for the MetaTrader 5 platform. You will be progressively introduced to the fundamentals of neural networks and their application in algorithmic trading. As you advance, you will build and train your own AI solution, gradually adding new features. In addition to learning MQL5, you will gain Python and OpenCL programming skills and explore integrated matrix and vector methods, which enable the solution of complex mathematical problems with concise and efficient code.

### Explore articles on developing trading strategies

[MQL5 Articles](https://www.mql5.com/en/articles "Articles on algorithmic/automated trading in MetaTrader and MQL4 and MQL5 programming") are an excellent resource for exploring the full potential of the language, covering a wide range of practical algorithmic trading tasks. For easy navigation, all articles are categorized into sections such as [Examples](https://www.mql5.com/en/articles/examples), [Expert Advisors](https://www.mql5.com/en/articles/expert_advisors), [Machine Learning](https://www.mql5.com/en/articles/machine_learning), and more. Every month, dozens of new articles are published on the [MQL5 Algotrading community](https://www.mql5.com/) website, written by traders for other traders. Read and discuss these articles to master modern algorithmic trading. For beginners, we have compiled a list of [16 recommended articles](https://www.metatrader5.com/en/metaeditor/help/articles) for a quick immersion into MQL5.

A special branch of algorithmic trading includes high frequency trading (HFT). As the name implies, trade operations are carried out at a high speed and frequency. The trading platform provides all the necessary tools for that:

-   Fast and efficient trading robots programming language [MQL5](/en/docs/mt5/client/autotrading#mql5)
-   Orders are sent from the platform and processed on the trade server with a minimum delay
-   Renting a [virtual platform](/en/docs/mt5/client/virtual_hosting) close to a broker to minimize network delays

Read this section to find out everything about the automated trading:

-   [Expert Advisors and Custom Indicators](/en/docs/mt5/client/trade_robots_indicators)
-   [Where to get trading robots and indicators](/en/docs/mt5/client/algotrading_get_ea_indicator)
-   [How to create an Expert Advisor or an indicator](/en/docs/mt5/client/autotrading)
-   [Strategy Testing](/en/docs/mt5/client/testing)
-   [Strategy Optimization](/en/docs/mt5/client/strategy_optimization)

[Templates and Profiles](/en/docs/mt5/client/charts_advanced/templates_profiles)

[Expert Advisors and Custom Indicators](/en/docs/mt5/client/trade_robots_indicators)