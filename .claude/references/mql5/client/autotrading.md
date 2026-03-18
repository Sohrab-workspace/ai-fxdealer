# How to Create an Expert Advisor or an Indicator

> Source: https://support.metaquotes.net/en/docs/mt5/client/autotrading

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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)How to Create an Expert Advisor or an Indicator

# How to Create an Expert Advisor or an Indicator

The trading platform contains a built in programming language MetaQuotes Language 5 ([MQL5](/en/docs/mt5/client/autotrading#mql5)), the [MetaEditor](/en/docs/mt5/client/autotrading#metaeditor) development environment and strategy testing tools.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Any information about the development of trading strategies in MQL5 can be found on the official <a href="https://www.mql5.com" target="_blank" class="weblink" title="MQL5.Community">MQL5.community</a> site. The website section <a href="https://www.mql5.com/en/code" target="_blank" class="weblink" title="Code Base">Code Base</a> contains examples of ready-to-use applications.</span></p></td></tr></tbody></table>

## The MQL5 Programming Language of Trading Strategies [#](autotrading#mql5)

The trading platform has its own built-in language for programming trading strategies [MetaQuotes Language 5](https://www.mql5.com/ "MQL5"). It is the fifth generation of MQL languages. It allows developing [Expert Advisors](/en/docs/mt5/client/autotrading#type) to automate trading processes, as well as implementing your own trading strategies. MQL5 also allows creating [custom indicators](/en/docs/mt5/client/autotrading#type), [scripts](/en/docs/mt5/client/autotrading#type) and function libraries.

MQL5 Features:

-   The language is object-oriented;
-   MQL5 syntax is similar to that of C++;
-   It contains a large number of functions necessary for analyzing quotes, managing positions, calling technical indicators, etc.;
-   It is a high-performance language;
-   High protection against decompilation: new complex encryption algorithms, file integrity checking, and the complexity of the language;
-   [OpenCL](https://www.mql5.com/en/articles/405 "OpenCL: The Bridge to Parallel Worlds article") support to enable use of video cards for calculations in MQL5 applications;
-   Integrated software development environment [MetaEditor](/en/docs/mt5/client/autotrading#metaeditor) including a debugger.

A detailed description of all language constructions and functions is provided in the MQL5 Reference. All the necessary information about MQL5 can also be found on the developer community website at [https://www.mql5.com](https://www.mql5.com).

## MetaEditor [#](autotrading#metaeditor)

MetaEditor is an integrated [MQL5](https://www.mql5.com) development environment. It is a component of the trading platform. MetaEditor allows you to create, edit, compile and debug source code written in [MQL5](/en/docs/mt5/client/autotrading#mql5).

-   MQL5 Wizard for creating templates and trading robots  
    MetaEditor includes the MQL5 Wizard that helps to quickly create MQL5 programs. With the MQL5 Wizard a trader without programming skills can easily create Expert Advisors. You only need to select trading signals for an Expert Advisor, as well as money management and trailing stop algorithms. The Expert Advisor code is generated automatically based on selected parameters.  
    In addition, the MQL5 Wizard allows creating MQL5 program templates to simplify the work of a programmer.
-   Helps with the source code  
    MetaEditor can recognize language structures: suggests tips on how to use functions and highlights various elements of the program source code. Thus, the editor enhances navigation in the source code of trading programs and speeds up the development process.
-   Debugging  
    MetaEditor allows you to debug programs to greatly facilitate troubleshooting. A step-by-step execution of a source code enables monitoring of the variable values.
-   Profiling for code optimization  
    The editor also provides tools for software profiling. You can identify the slowest functions in the source code and optimize your program.
-   Articles about programming and a source code library  
    Straight from the editor, you can find a plethora of MQL5 programming tutorials. You can additionally access a huge code base of free automated trading programs.
-   Online MQL5 Storage with versioning support  
    The storage provides safe storage of files and the possibility to restore lost files, as well as access your code from any computer using a MQL5.community account.

More details about MetaEditor can be found in its built-in help files. The description of MQL5 can be found in the built-in reference and the official [MQL5.community](https://www.mql5.com "MQL5.community") website.

## Algo Trading Books [#](autotrading#algobook)

To assist beginners, we have released two comprehensive books on MQL5 programming, designed for anyone who wish to master the creation of trading robots and applications for algorithmic trading. The books offer a systematic and structured presentation of the material to make the learning process easier. Detailed code examples, which explain the step-by-step creation of trading robots and applications, allow for a deeper understanding of algorithmic trading nuances.

"[MQL5 Programming for Traders](https://www.mql5.com/en/book "MQL5 Programming for Traders")" is the most complete and detailed tutorial on MQL5, suitable for programmers of all levels. Beginners will learn the basics: the book introduces development tools and basic programming concepts. Based on this material, you will create, compile and run your first application in the MetaTrader 5 trading platform. Users with experience in other programming languages can directly proceed to the applied sections: creating trading robots and analytical applications in MQL5.

"[Neural Networks in Algorithmic Trading with MQL5](https://www.mql5.com/en/neurobook "Book on Neural Networks, MQL5, OpenCL and Python")" is a guide to using machine learning methods in trading robots for the MetaTrader 5 platform. You will be progressively introduced to the fundamentals of neural networks and their application in algorithmic trading. As you advance, you will build and train your own AI solution, gradually adding new features. In addition to learning MQL5, you will gain Python and OpenCL programming skills and explore integrated matrix and vector methods, which enable the solution of complex mathematical problems with concise and efficient code.

## Articles on the development of trading applications [#](autotrading#articles)

[MQL5.community](https://www.mql5.com "MQL5.community") website features an extensive library [of articles on MQL4/MQL5 programming](https://www.mql5.com/en/articles). Articles are an excellent guide for creating applications, since they cover a lot of practical tasks involving algorithmic trading. New articles are published every week.

List of all available articles is displayed directly in MetaEditor. To find the necessary material, use the [online search](/en/docs/mt5/client/interface#search).

![Articles on MQL4/MQL5 programming](/en/docs/mt5/client/img/articles.png "Articles on MQL4/MQL5 programming")

## Types of MQL5 Applications [#](autotrading#type)

Three major types of trading applications are available.

### Expert Advisors

Expert Advisors are mechanical trading systems that allow complete automation of analytical and trading activities for the efficient operation in the financial markets. They allow to perform prompt technical analysis of price data and control trading activities on the basis of signals received. They also help to strictly follow a trading strategy eliminating emotions.

All Expert Advisors are stored in the [/MQL5/Experts](/en/docs/mt5/client/start_advanced/structure#ea) folder of the trading platform.

### Custom Indicators

Custom Indicators are custom developed technical indicators intended for analyzing price dynamics. Trading tactics and Expert Advisors are developed based on algorithms of indicators. Custom indicators are only used for analyzing symbol price dynamics. Indicators cannot trade and do not have access to charts.

All indicators are stored in the [/MQL5/Indicators](/en/docs/mt5/client/start_advanced/structure#indicators) folder of the trading platform.

### Scripts

A script is an application written in [MQL5](/en/docs/mt5/client/autotrading#mql5) designed for a single execution of an action. A script can perform both analytical and trading functions. Unlike [Advisors](/en/docs/mt5/client/autotrading#type), scripts are executed on request. In other words, if an Expert Advisor works almost continuously, a script executes its function and quits.

All scripts are stored in the [/MQL5/Scripts](/en/docs/mt5/client/start_advanced/structure#scripts) folder of the trading platform.

### Services

[Services](/en/docs/mt5/client/trade_robots_indicators#service) enable the use of custom price feeds for the platform and to implement price delivery from external systems in real time, just like it is implemented on brokers' trade servers. Services can also be used to perform other service tasks in the background.

Unlike Expert Advisors, indicators and scripts, services are not linked to a specific chart. Such applications run in the background and are launched automatically when the terminal is started (unless such an app was forcibly stopped).

All services are stored under the [/MQL5/Services](/en/docs/mt5/client/start_advanced/structure#scripts) folder of the trading platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_Normal"><span class="f_txt">Inside folders Experts, Indicators, Scripts and Services, applications can be sorted into subfolders. The structure of their location is displayed in the <a href="/en/docs/mt5/client/interface" class="topiclink">Navigator</a> window.</span></p></td></tr></tbody></table>

## How to Create and Run a Trading Application [#](autotrading#create)

Click "![Create in MetaEditor](/en/docs/mt5/client/img/create_icon.png "Create in MetaEditor") Create in MetaEditor" in the context menu of the [Navigator](/en/docs/mt5/client/interface) window in section Expert Advisors, Indicators or Scripts. MetaEditor can also be launched by pressing F4.

![Start creating a trading application](/en/docs/mt5/client/img/ea_create.png "Start creating a trading application")

This launches [MetaEditor](/en/docs/mt5/client/autotrading#metaeditor) with an automatically opened MQL5 Wizard. Use it to generate the necessary program template to quickly start software development. Let's create a simple script writing a message "Hello world" into the [journal](/en/docs/mt5/client/start_advanced/journal).

![The MQL5 Wizard generates a template of the application](/en/docs/mt5/client/img/example_wizard_script.png "The MQL5 Wizard generates a template of the application")

In the resulting template, we add the code Print("Hello World"); and compile it by pressing F7 to receive an executable file. The executable file has an extension EX5 and can be run in the trading platform.

![Compiling and its results](/en/docs/mt5/client/img/example_compile.png "Compiling and its results")

Compilation results are added to the editor log.

In accordance with the application type, the source code is saved to the folder MQL5\\Scripts\\. The executable file is created in the same folder. You can now return to the trading platform and run the generated script.

![Running a script in the trading platform](/en/docs/mt5/client/img/example_run_script.png "Running a script in the trading platform")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Specifics of use of automated trading programs are described in section <a href="/en/docs/mt5/client/trade_robots_indicators" class="topiclink">"Expert Advisors and custom indicators"</a>.</span></p></td></tr></tbody></table>

## How to Edit a Trading Application [#](autotrading#modify)

To edit a trading robot or a custom indicator, click "![Modify](/en/docs/mt5/client/img/modify_icon.png "Modify") Modify" in its context menu in the [Navigator](/en/docs/mt5/client/interface) window or select it and press Enter. This opens [MetaEditor](/en/docs/mt5/client/autotrading#metaeditor) with the source code of the selected indicator. After you have modified the indicator, re-compile it (F7). Otherwise its previous unchanged version will be used in the platform.

## How to Shut Down a Trading Application [#](autotrading#quit)

There are many ways to shut down a trading application in the platform.

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Trading robot</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Custom technical indicator</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Script</span></p></th></tr></thead><tbody><tr class="table"><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Click "Remove" in the <a href="/en/docs/mt5/client/charts_advanced/charts_objects_list#ea" class="topiclink">Expert List</a> window;</span></li><li class="p_fortable"><span class="f_fortable">Change the chart <a href="/en/docs/mt5/client/charts_advanced/templates_profiles" class="topiclink">template</a>;</span></li><li class="p_fortable"><span class="f_fortable">Change the <a href="/en/docs/mt5/client/charts_advanced/templates_profiles#profiles" class="topiclink">profile</a>, provided that the <a href="/en/docs/mt5/client/settings#profile" class="topiclink">appropriate option is enabled in the platform settings</a>;</span></li><li class="p_fortable"><span class="f_fortable">Turn off the trading platform;</span></li><li class="p_fortable"><span class="f_fortable">Close the chart the Expert Advisor is running on;</span></li><li class="p_fortable"><span class="f_fortable">Run another Expert Advisor on the same chart;</span></li><li class="p_fortable"><span class="f_fortable">Click "<img class="help" alt="Remove Expert Advisor" title="Remove Expert Advisor" width="16" height="16" src="/en/docs/mt5/client/img/ea_remove_icon.png"> Remove" in the context menu of the Expert Advisor icon on the chart.</span></li></ul></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Click&nbsp;"<img class="help" alt="Remove indicator" title="Remove indicator" width="16" height="16" src="/en/docs/mt5/client/img/delete_indicator_icon.png"> Delete" or "<img class="help" alt="Delete indicator window" title="Delete indicator window" width="16" height="16" src="/en/docs/mt5/client/img/delete_indicator_window.png"> Delete Indicator Window" in the context menu of the indicator;</span></li><li class="p_fortable"><span class="f_fortable">Click "Delete" in the <a href="/en/docs/mt5/client/charts_advanced/charts_objects_list#indicators" class="topiclink">Indicator List</a> window;</span></li><li class="p_fortable"><span class="f_fortable">Change the chart <a href="/en/docs/mt5/client/charts_advanced/templates_profiles" class="topiclink">template</a>;</span></li><li class="p_fortable"><span class="f_fortable">Re-open the chart.</span></li></ul></td><td class="table"><ul><li class="p_fortable"><span class="f_fortable">Click "Remove" in the <a href="/en/docs/mt5/client/charts_advanced/charts_objects_list#ea" class="topiclink">Expert List</a> window. This window also contains a list of running scripts;</span></li><li class="p_fortable"><span class="f_fortable">Change the chart <a href="/en/docs/mt5/client/charts_advanced/templates_profiles" class="topiclink">template</a>;</span></li><li class="p_fortable"><span class="f_fortable">Change the <a href="/en/docs/mt5/client/charts_advanced/templates_profiles#profiles" class="topiclink">profile</a>, provided that the <a href="/en/docs/mt5/client/settings#profile" class="topiclink">appropriate option is enabled in the platform settings</a>;</span></li><li class="p_fortable"><span class="f_fortable">Change the <a href="/en/docs/mt5/client/charts" class="topiclink">chart</a> symbol;</span></li><li class="p_fortable"><span class="f_fortable">Change the chart <a href="/en/docs/mt5/client/charts#operations" class="topiclink">timeframe</a>;</span></li><li class="p_fortable"><span class="f_fortable">Turn off the trading platform;</span></li><li class="p_fortable"><span class="f_fortable">Close the chart the script is running on;</span></li><li class="p_fortable"><span class="f_fortable">Run another script on the same chart;</span></li><li class="p_fortable"><span class="f_fortable">Click "<img class="help" alt="Remove Script" title="Remove Script" width="16" height="16" src="/en/docs/mt5/client/img/script_remove_icon.png"> Remove" in the context menu of the script icon on the chart.</span></li></ul></td></tr></tbody></table>

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If a trading application is running on a chart, it will not be shut down if you delete the appropriate executable file from the <a href="/en/docs/mt5/client/interface" class="topiclink">Navigator</a> window.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Disabling Expert Advisors <a href="/en/docs/mt5/client/settings#enable_ea" class="topiclink">in the trading platform settings</a> does not disable them completely. This operation only prohibits Expert Advisors from trading.</span></li></ul></td></tr></tbody></table>

## How to Run a Downloaded File of the MQ5 Source Code [#](autotrading#mq5)

If you only have a source code file (\*.MQ5), save it in a folder corresponding to the application type:

-   For Expert Advisors — /MQL5/Experts
-   For indicators — /MQL5/Indicators
-   For scripts —/MQL5/Scripts

To quickly navigate to the trading platform data folder, click "![Open data folder](/en/docs/mt5/client/img/terminal_data_icon.png "Open data folder") Open data folder" in the [File](/en/docs/mt5/client/interface) menu.

To run a file in the trading platform, compile it in the [MetaEditor](/en/docs/mt5/client/autotrading#metaeditor):

-   Open MetaEditor by pressing F4.
-   In MetaEditor, open the source code file in the Navigator window by a double left-click on the file name.
-   Press F7 to compile it.

This creates an executable \*.EX5 file that can be run in the trading platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Source files (*.MQ5) are not displayed in the <a href="/en/docs/mt5/client/interface" class="topiclink">Navigator</a> window of the trading platform.</span></p></td></tr></tbody></table>

[Where to Find Trading Robots and Indicators](/en/docs/mt5/client/algotrading_get_ea_indicator)

[Strategy Testing](/en/docs/mt5/client/testing)