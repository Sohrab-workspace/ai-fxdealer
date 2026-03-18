# Fundamental Analysis

> Source: https://support.metaquotes.net/en/docs/mt5/client/fundamental

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
            -   [View and Configure Charts](/en/docs/mt5/client/charts)
            -   [Publish Online](/en/docs/mt5/client/mql5_charts)
            -   [Technical Indicators](/en/docs/mt5/client/indicators)
            -   [Analytical Objects](/en/docs/mt5/client/objects)
            -   [Fundamental Analysis](/en/docs/mt5/client/fundamental)
                -   [USA](/en/docs/mt5/client/fundamental/economic_indicators_usa)
                -   [European Union](/en/docs/mt5/client/fundamental/economic_indicators_euro)
                -   [United Kingdom](/en/docs/mt5/client/fundamental/economic_indicators_uk)
                -   [Japan](/en/docs/mt5/client/fundamental/economic_indicators_japan)
                -   [Germany](/en/docs/mt5/client/fundamental/economic_indicators_ger)
                -   [Switzerland](/en/docs/mt5/client/fundamental/economic_indicators_switzerland)
                -   [Australia](/en/docs/mt5/client/fundamental/economic_indicators_australia)
                -   [Canada](/en/docs/mt5/client/fundamental/economic_indicators_canada)
                -   [China](/en/docs/mt5/client/fundamental/economic_indicators_china)
                -   [New Zealand](/en/docs/mt5/client/fundamental/economic_indicators_newzealand)
            -   [Additional Technical Indicators](/en/docs/mt5/client/charts_analysis_get_indicators)
            -   [Additional Features](/en/docs/mt5/client/charts_advanced)
        -   [Algorithmic Trading, Trading Robots](/en/docs/mt5/client/algotrading)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)Fundamental Analysis

# Fundamental Analysis

The purpose of fundamental analysis is in the constant monitoring and studying of various economic and industrial indicators, which may affect the quotes of a financial instrument.

For example, annual report releases, news about a new contract or a regulatory law can seriously affect the price of company shares. To keep abreast, you need to constantly analyze this information.

## Where can I read the financial news [#](fundamental#news)

Straight in the platform you can receive financial news from international news agencies. This helps you stay updated and take appropriate trading decisions.

News items appear on the News tab of Toolbox window. To read the news, double click on its title.

![Financial News](/en/docs/mt5/client/img/fundamental_news.png "Financial News")

## Why do brokers provide different news? [#](fundamental#broker)

Any financial newsletters can be received in the trading platform. Every broker selects the news types and providers.

## How to configure the news language? [#](fundamental#lang_category)

Newsletters in various languages can be received in the trading platform. To configure the list of languages, open the [platform settings](/en/docs/mt5/client/settings#server) by clicking "![Options](/en/docs/mt5/client/img/options_icon.png "Options") Options" in the [Tools](/en/docs/mt5/client/interface) menu.

![Setting the language of news](/en/docs/mt5/client/img/news_language.png "Setting the language of news")

Click "Edit" in the "News Language" field and select the desired languages. The default is automatic selection, i.e. newsletters are filtered by the platform interface language. If you do not want to receive newsletters, uncheck "Enable news".

For your convenience, the newsletters are divided into categories. Open the context menu in the news tab. Click "Customize" in the submenu of news categories to open their setup window:

![News categories](/en/docs/mt5/client/img/news_categories.png "News categories")

In the tree-like list, select the news categories you want to display in the trading platform.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The types of available categories are defined by the data provider chosen by your broker.</span></p></td></tr></tbody></table>

## How to follow macroeconomic indicators? [#](fundamental#macro)

In addition to the news, the platform contains the [Economic Calendar](https://www.mql5.com/en/economic-calendar). The calendar features publications of over 600 [macroeconomic indicators](/en/docs/mt5/client/fundamental) concerning 15 largest global economies, including USA, European Union, Japan, UK, Canada, Australia, China, etc. Relevant data is collected from open sources in real time.  

Macroeconomic indicators are parameters describing the state of the country they are calculated for. They characterize the level of economic development and may indicate either economic growth or a decline. By analyzing the macroeconomic indicators, it is possible to forecast future price movements.

The indicators and events can be viewed on the "Calendar" tab of the "Toolbox" window.

![Economic Calendar](/en/docs/mt5/client/img/fundamental_calendar.png "Economic Calendar")

By default, the calendar displays current week events, including past and upcoming events. Use the context menu to switch to another period. You can access events for the previous, current and next week, as well as appropriate months. A deeper history is available in the [web version](https://www.mql5.com/en/economic-calendar).

Every indicator is provided with the release time, priority, as well as its current, forecast and previous values. The current value appears as soon as the indicator is released. If this value is less than the predicted one, the indicator is highlighted in red. If the current value is larger, the indicator is shown in blue.

To view a detailed event description or the history of its values as a graph or table, double click on its name.

For easier search, filter events in the list using the context menu:

-   by priority
-   by the currency of the country for which the indicator is published
-   by country for which the indicator is published

<table class="help" cellspacing="0" cellpadding="0" border="0" style="width:100%; border:none; border-spacing:0;"><thead><tr><th style="vertical-align:top; width:50%; padding:0; border:none"><h3>Install the Calendar on your site</h3></th><th style="vertical-align:top; width:50%; padding:0; border:none"><h3>Download the mobile calendar version</h3></th></tr></thead><tbody><tr><td style="vertical-align:top; width:50%; padding:0; border:none"><p class="p_table_text"><span class="f_table_text">You can add the Economic Calendar in your site free of charge. This can be done by pasting <a href="https://www.mql5.com/en/economic-calendar/widgets" target="_blank" class="weblink">the ready widget code</a> in the desired web page.</span></p><p class="p_table_text"><span class="f_table_text">You do not have to worry about licensing risks. The Calendar is based on data collected from public sources.</span></p><p class="p_table_text"><span class="f_table_text">The advantages of the Calendar:</span></p><ul><li class="p_table_text"><span class="f_table_text">Useful content on your site: offer your visitors a powerful service for tracking global economic events.</span></li><li class="p_table_text"><span class="f_table_text">Flexible customization for your website: set the desired widget width and height, the amount of data displayed, the language and date format.</span></li><li class="p_table_text"><span class="f_table_text">Multilingual interface: all events and descriptions are fully translated into 9 languages, including English, Chinese, Japanese, Russian, Spanish, Portuguese, German, Turkish and Arabic.</span></li><li class="p_table_text"><span class="f_table_text">Full representation: every event is provided with a detailed description and notes related to the release influence on individual currencies, as well as the source link, release date and charts.</span></li><li class="p_table_text"><span class="f_table_text">No ads: you will not have to pay for the service by showing third-party ads.</span></li><li class="p_table_text"><span class="f_table_text">Automatic time zone selection: event tracking is maintained via local time adaptation. Manual adaptation of time zones is also possible.</span></li><li class="p_table_text"><span class="f_table_text">Automatic update: the calendar is automatically updated as soon as a new event appears in a source.</span></li><li class="p_table_text"><span class="f_table_text">Continuous development: when a country is added, all economic indices which have a significant impact on the national currency are included in the calendar.</span></li></ul><p class="p_table_text"><a style="background-color:#17a21d;color:#fff;display:inline-block;padding:15px 30px;text-decoration:none;" href="https://www.mql5.com/en/economic-calendar/widgets?utm_campaign=www.metatrader5.com">Install the Calendar in your site &gt;&gt;</a></p><p class="p_table_text"><span class="f_table_text">&nbsp;</span></p></td><td style="vertical-align:top; width:50%; padding:0; border:none"><p class="p_table_text"><span class="f_table_text">The Economic Calendar is available as a separate <a href="https://www.tradays.com" target="_blank" class="weblink">Tradays</a> application for mobile devices powered by iOS and Android.</span></p><p class="p_table_text"><span class="f_table_text">The mobile version features a complete set of functions for the full-fledged operation and a number of additional features:</span></p><ul><li class="p_table_text"><span class="f_table_text">More than 600 events related to the world's largest economies, including US, UK, European Union, japan, Canada, Australia, China, among others.</span></li><li class="p_table_text"><span class="f_table_text">Detailed event descriptions.</span></li><li class="p_table_text"><span class="f_table_text">Access to historic indicator values in the form of tables and charts.</span></li><li class="p_table_text"><span class="f_table_text">Filters by priority and countries, to which the indicators are related.</span></li><li class="p_table_text"><span class="f_table_text">Ability to create event reminders in a couple of clicks.</span></li></ul><p class="p_table_text"></p><div><div><p></p><div><div class="parent-table"><table class="help" cellspacing="0" cellpadding="10" border="0" style="width:100%; border:none; border-spacing:0;"><tbody><tr><td style="vertical-align:top; padding:10px; border:none"><p class="p_fortable"><a href="https://download.terminal.free/cdn/mobile/tradays/ios?utm_campaign=www.metatrader5.com" target="_blank" title="The Tradays Economic Calendar mobile app for iPhone/iPad"><img class="help" alt="The Tradays Economic Calendar mobile app for iPhone/iPad" title="The Tradays Economic Calendar mobile app for iPhone/iPad" width="193" height="66" src="/en/docs/mt5/client/img/app-store.png"></a></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><img class="help" alt="The Tradays Economic Calendar mobile app for iPhone/iPad" title="The Tradays Economic Calendar mobile app for iPhone/iPad" width="277" height="556" src="/en/docs/mt5/client/img/tradays-iphone.png"></p></td><td style="vertical-align:top; padding:10px; border:none"><p class="p_fortable"><a href="https://download.terminal.free/cdn/mobile/tradays/android?utm_campaign=www.metatrader5.com" target="_blank" title="The Tradays Economic Calendar mobile app for Android"><img class="help" alt="The Tradays Economic Calendar mobile app for Android" title="The Tradays Economic Calendar mobile app for Android" width="193" height="59" src="/en/docs/mt5/client/img/google-play.png"></a></p><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p><p class="p_fortable"><img class="help" alt="The Tradays Economic Calendar mobile app for Android" title="The Tradays Economic Calendar mobile app for Android" width="277" height="556" src="/en/docs/mt5/client/img/tradays-android.png"></p></td></tr></tbody></table></div></div></div></div></td></tr></tbody></table>

## Types of Macroeconomic Indicators [#](fundamental#macro_type)

Macroeconomic indicators are categorized based on the countries for which they are published. Read the detailed description of the most popular indicators in further topics:

-   [US macroeconomic indicators](/en/docs/mt5/client/fundamental/economic_indicators_usa)
-   [EU macroeconomic indicators](/en/docs/mt5/client/fundamental/economic_indicators_euro)
-   [UK macroeconomic indicators](/en/docs/mt5/client/fundamental/economic_indicators_uk)
-   [Macroeconomic indicators of Japan](/en/docs/mt5/client/fundamental/economic_indicators_japan)
-   [Macroeconomic indicators of Germany](/en/docs/mt5/client/fundamental/economic_indicators_ger)
-   [Macroeconomic indicators of Switzerland](/en/docs/mt5/client/fundamental/economic_indicators_switzerland)
-   [Macroeconomic indicators of Australia](/en/docs/mt5/client/fundamental/economic_indicators_australia)
-   [Macroeconomic indicators of Canada](/en/docs/mt5/client/fundamental/economic_indicators_canada)
-   [Macroeconomic indicators of China](/en/docs/mt5/client/fundamental/economic_indicators_china)
-   [Macroeconomic indicators of New Zealand](/en/docs/mt5/client/fundamental/economic_indicators_newzealand)

## How to display the macroeconomic indicators on a chart? [#](fundamental#chart)

Information about macroeconomic events can be displayed on the charts of corresponds currency pairs. You can visually assess the impact of various events on the currencies.

![Add macroeconomic indicators to the chart](/en/docs/mt5/client/img/fundamental_calendar_event.png "Add macroeconomic indicators to the chart")

To add the indicators to the chart, click on "![Add All Events](/en/docs/mt5/client/img/add_all_events_icon.png "Add All Events") Add All Events" in the context menu of the calendar.

[Rectangle Label](/en/docs/mt5/client/objects/graphical_objects/obj_rect_label)

[USA](/en/docs/mt5/client/fundamental/economic_indicators_usa)