# Setup

> Source: https://support.metaquotes.net/en/docs/mt4/terminal/autotrading/tester/tester_parameters

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
            -   [Where to Get Trade Robots and Indicators](/en/docs/mt4/terminal/autotrading/charts_analysis_get_indicators)
            -   [MQL4](/en/docs/mt4/terminal/autotrading/mql4)
            -   [MetaEditor](/en/docs/mt4/terminal/autotrading/metaeditor)
            -   [Expert Advisors](/en/docs/mt4/terminal/autotrading/experts)
            -   [Strategy Testing](/en/docs/mt4/terminal/autotrading/tester)
                -   [Setup](/en/docs/mt4/terminal/autotrading/tester/tester_parameters)
                -   [Results](/en/docs/mt4/terminal/autotrading/tester/tester_results)
                -   [History Files in FXT Format](/en/docs/mt4/terminal/autotrading/tester/tester_fxt)
            -   [Indicator Testing](/en/docs/mt4/terminal/autotrading/tester_indicator)
            -   [Expert Optimization](/en/docs/mt4/terminal/autotrading/tester_optimization)
            -   [Custom Indicators](/en/docs/mt4/terminal/autotrading/custom_indicators)
            -   [Scripts](/en/docs/mt4/terminal/autotrading/scripts)
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

[MetaTrader 4](/en/docs/mt4)[Client terminal](/en/docs/mt4/terminal)[Auto Trading](/en/docs/mt4/terminal/autotrading)[Strategy Testing](/en/docs/mt4/terminal/autotrading/tester)Setup

# Setup

Before starting to test expert advisors, one has to perform the setup. This means that one has to:

-   [select an expert and set up its inputs](/en/docs/mt4/terminal/autotrading/tester/tester_parameters#expert)
-   [select a symbol and its period](/en/docs/mt4/terminal/autotrading/tester/tester_parameters#securities)
-   [select one of three modeling methods](/en/docs/mt4/terminal/autotrading/tester/tester_parameters#model)
-   [set the testing time range (optional)](/en/docs/mt4/terminal/autotrading/tester/tester_parameters#time_range)

To test and optimize experts, a special ["Tester" window](/en/docs/mt4/terminal/overview/strategy_tester) is used in the terminal. All above parameters are set in the "Settings" tab of this window.

## An Expert Advisor and Its Parameters [#](tester_parameters#expert)

One has to select an expert to be tested in the "Tester — Expert Advisor" field. One cannot select any expert file in this field. Only those experts that are available in the client terminal can be selected here. To be selected, they must be compiled and located in the /EXPERTS folder.

![strategy_tester](/en/docs/mt4/terminal/img/strategy_tester.png)

After an expert has been selected, one has to perform additional setting of testing parameters and inputs. This can be done by pressing of the "Expert properties" button.

![strategy_tester_settings_expert_properties](/en/docs/mt4/terminal/img/strategy_tester_settings_expert_properties.png)

A new window with three tabs will appear then:

-   Testing — general testing parameters are set in this tab. These are volume and currency of the initial deposit to be given in the corresponding fields. It is this deposit that will be operated by the expert during testing. Types of positions to be opened at testing are defined here, as well: Only Long — open only long positions; Only Short — open only short ones; Long and Short — open both long and short positions. Whatever expert algorithm is, it will open positions only in the defined directions. One can include an optimization genetic algorithm and select a parameter to be optimized (maximization by the balance value, the profit factor, expected payoff, or minimization by the maximal drawdown value or drawdown percent).
-   Inputs — the list of all inputs is given here as a table. Inputs are variables that influence the expert operation and can be changed directly from the client terminal. There is no need to change the expert code in order to change these parameters. The amount of input variables can change depending on the expert. At testing, the expert inputs are defined in the "Value" field. Data written in the fields of "Start", "Step", and "Stop" do not influence expert testing and are necessary just for [optimization of its parameters](/en/docs/mt4/terminal/autotrading/tester_optimization). How to work with these parameters is described in the ["Optimization Setup" section](/en/docs/mt4/terminal/autotrading/tester_optimization).
-   Optimization — settings in this tab allow to limit testing passes at optimization. Changing of parameters in this tab does not influence single testing passes of the expert.

## Symbol and Its Period [#](tester_parameters#securities)

To start testing, it is not enough just to select an expert and set it up. One has to select a symbol and a period (timeframe) for testing. These are data that will be used for testing. At testing, one can select an available in terminal symbol or use an external data file. History data files of \*.FXT format stored in the /TESTER directory are used in testing. These file are created automatically at testing if an available in the terminal symbol was selected.

The symbol is defined in the field of the same name, and timeframe is in the "Period" field. If no data file for this symbol, period and modeling method does not exist yet, it will be created automatically. If there are no history data for the symbol or period, the tester will download the last 512 history bars automatically.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If there are some data outside the latest 512 bars for the symbol, the history data will be downloaded automatically, up to the last available one. This can cause sharp increase of the incoming traffic.</span></p></td></tr></tbody></table>

## Methods of Modeling [#](tester_parameters#model)

Historical data are saved in the terminal only as bars and represent records appearing as [TOHLCV (HST format)](/en/docs/mt4/terminal/service/history_center). These data can be used for modeling of price changes at testing experts. In some cases, such information is not enough for testing. For example, for the daily timeframe, price changes within a bar can result in triggering of the expert. At the same time, no triggering can occur at testing. In other words, testing an expert based on only bars can be inaccurate and give a false idea about the expert efficiency.

The trading terminal allows to test experts by various methods of historical data modeling. Using historical data from smaller periods, it is possible to see price fluctuations within bars, i.e., price changes will be emulated more precisely. For example, when an expert is tested on one-hour data, price changes for a bar can be modeled on one-minute data. Thus, modeling brings historical data near the real price fluctuations and makes expert testing more authentic.

One of three methods of historical data modeling can be chosen for testing:

-   Open prices only (fastest method to analyze the bar just completed)  
    Some automated trading systems do not depend on properties of modeling within a bar, they trade on completed bars. The bar is completed if the next one has appeared. These are such experts for that this modeling method was developed.  
    In this mode, the bar opening is modeled first (Open = High = Low = Close, Volume=1) what allows the expert to identify the completion of the preceding bar precisely. It is this incipient bar that is used to start testing the expert. At the next step, the fully completed current bar will be given, but no testing is performed on it!
-   Control points (the nearest less timeframe is used)  
    The control points modeling method is intended for a crude estimate of experts efficiency that trade within the bar. The historical data of the nearest less timeframe must be available to apply this method. In some cases, the available data of the less timeframe do not completely cover the time range of the timeframe under test. If the data of the less timeframe are missing, the bar evolution is generated on the basis of predefined wave templates as it was in the preceding, third version of MetaTrader 3 Client Terminal.  
       
    As soon as historical data of the less timeframe appear, these new data will be interpolated. However, the really existing OHLC prices appear as control points. In the most cases, the results of testing experts by method of control points can also be considered as estimated ones, not as final ones. Such results are of intermediate, estimated nature.
-   Every tick (based on all available least timeframes)  
    This is the most accurate method of modeling prices within a bar. Unlike that of "control points", this method uses for generation not only data of the nearest less timeframe, but also those of all available nearest timeframes. At that, if there are data of more than one period for the same timeframe at the same time, the data of the least timeframe will be used for modeling. Like in the preceding method, control points are generated on the basis of OHLC data of the least available timeframe. To generate price movements between control points, interpolation based on predefined templates is also used, so one-minute data are highly desirable to be available that would cover the entire testing range. It is possible that several similar ticks are modeled one after another. In this case, the doubled quotes will be filtered out, and the volume of the last of them will be fixed.  
       
    One has to consider the possible large amount of tick data modeled. This can influence the consumed resources of the operation system and testing speed.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention:</span></p><ul><li><ul><li class="p_tableatten"><span class="f_tableatten">it is not recommended to launch testing on every tick if there are no available less timeframes that completely cover the period under test, otherwise, the results will not be accurate;</span></li><li class="p_tableatten"><span class="f_tableatten">modeling on control points is basically used at optimization of experts, and all ticks modeling is for a close testing.</span></li></ul></li></ul></td></tr></tbody></table>

The modeling quality can be checked in the "Report" window. The "Modeling quality" field and a colored band are intended for this. The band is a scheme of the modeling process. It can be of three colors:

1.  Gray — this part of available data did not participate in testing. Gray color can appear if the date range was specified for testing (described below);
2.  Red — modeling was not performed in this space because of missing data of a less timeframe. At that, only data of the timeframe selected for testing were used;
3.  Green — modeling was performed in this space. And the brighter is the color, the higher the modeling quality was. For example, at testing on H1 period, the deep-green band can mean that data of M30 period were used for testing, and the brightest one does that M1-period data are used.

The price history stored in the client terminal includes only Bid prices. On default, to model Ask prices, the strategy tester uses the current spread of a symbol at the beginning of testing. However a user can set a custom spread for testing in the "Spread" field.

## Time Range [#](tester_parameters#time_range)

The range of dates allows to test experts not on all available data, but within a certain time space only. This can be useful if there is a need to test a certain part of history data. Date range can be used not only for expert testing, but also for modeling of the testing succession of bars (file of data modeled to be used for testing). It is often no need to model data of the entire history, especially for every-tick modeling where the amount of unused data can be very large. That is why, if data range was allowed to be set at the initial modeling of testing succession, bars that are beyond this range will not be modeled, but just transcribed into the output succession. The data will not be excluded from the succession in order the correct calculation of indicators on the entire received history to be possible. It must be noted that the first 100 bars will not be modeled either. This limitation does not depend on the date range defined.

To enable date range limitation, one has to flag "Use date" and specify the necessary values in the fields of "From" and "To". After all settings have been made, one can press the "Start" button and start testing. After testing has started, the approximate time of completing of this process can be viewed in the lower part of the window.

## Testing Visualization [#](tester_parameters#visual)

If the ""Visualization"is flagged, after the "Start" button has been clicked, the chart will be opened automatically, on which the modeled tick sequence will be played. The playback speed can be regulated. The playback can be suspended by clicking the "||" button. The repeated click on this button resumes the income of the modeled ticks. Pressing of F12 causes immediate appearance of the next tick even in the suspension mode. Visualization can be skipped up to a certain date. After the desired date is set and the "Skip to" button is clicked, visualizing will stop and then resumed after the tester reaches the defined date.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Attention: If "Optimization" is enabled, <a href="/en/docs/mt4/terminal/autotrading/tester_optimization" class="topiclink">expert parameters will be optimized</a>, not tested, after the "Start" button has been pressed.</span></p></td></tr></tbody></table>

[Strategy Testing](/en/docs/mt4/terminal/autotrading/tester)

[Results](/en/docs/mt4/terminal/autotrading/tester/tester_results)