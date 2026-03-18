# Gann Tools

> Source: https://support.metaquotes.net/en/docs/mt5/client/objects/gann

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
                -   [Lines](/en/docs/mt5/client/objects/lines)
                -   [Channels](/en/docs/mt5/client/objects/channels)
                -   [Fibonacci Tools](/en/docs/mt5/client/objects/fibo)
                -   [Gann Tools](/en/docs/mt5/client/objects/gann)
                    -   [Gann Line](/en/docs/mt5/client/objects/gann/gann_line)
                    -   [Gann Fan](/en/docs/mt5/client/objects/gann/gann_fan)
                    -   [Gann Grid](/en/docs/mt5/client/objects/gann/gann_grid)
                -   [Elliott Tools](/en/docs/mt5/client/objects/elliott)
                -   [Shapes](/en/docs/mt5/client/objects/shapes)
                -   [Arrows](/en/docs/mt5/client/objects/arrows)
                -   [Graphical Objects](/en/docs/mt5/client/objects/graphical_objects)
            -   [Fundamental Analysis](/en/docs/mt5/client/fundamental)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)[Analytical Objects](/en/docs/mt5/client/objects)Gann Tools

# Gann Tools

Gann tools can be applied to a price or indicator chart using the "Objects — Gann" items of the ["Insert"](/en/docs/mt5/client/interface) menu or the ["Line Studies"](/en/docs/mt5/client/interface) toolbar. The following types of Gann tools are available in the platform:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="width:26px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></th><th class="table" style="width:109px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Type</span></p></th><th class="table"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Gann Line" title="Gann Line" width="14" height="16" src="/en/docs/mt5/client/img/gann_line_icon.png"></p></td><td class="table" style="width:109px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Gann Line</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gann Line represents a trendline drawn at an angle of 45 degrees. Two points must be set for this tool to be drawn. <a href="/en/docs/mt5/client/objects/gann/gann_line" class="topiclink">Read more...</a></span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Gann Fan" title="Gann Fan" width="16" height="16" src="/en/docs/mt5/client/img/gann_fan_icon.png"></p></td><td class="table" style="width:109px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Gann Fan</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Gann Fan represents a set of trendlines drawn from one point at different angles. Gann considered the trendline of 1x1 (45 degrees) as a very important one. If the price curve is located above this line, it is the indication of the bull market, if it is below this line it is that of the bear market. Gann thought that the ray of 1x1 is a powerful support line when the trend is ascending, and he considered the breaking this line as an important turn signal. One point must be set for Gann Fan to be drawn. <a href="/en/docs/mt5/client/objects/gann/gann_fan" class="topiclink">Read more...</a></span></p></td></tr><tr class="table"><td class="table" style="width:26px;"><p class="p_fortable"><img class="help" alt="Gann Grid" title="Gann Grid" width="16" height="16" src="/en/docs/mt5/client/img/gann_grid_icon.png"></p></td><td class="table" style="width:109px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Gann Grid</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Lines of the Gann Grid are drawn at an angle of 45 degrees. Two points must be set for this tool to be drawn. <a href="/en/docs/mt5/client/objects/gann/gann_grid" class="topiclink">Read more...</a></span></p></td></tr></tbody></table>

[Fibonacci Expansion](/en/docs/mt5/client/objects/fibo/fibo_expansion)

[Gann Line](/en/docs/mt5/client/objects/gann/gann_line)