# Filtration of Quotes

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/datafeeds/unidde/unidde_filtration

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
                -   [Dow Jones Prime Tass News Feeder](/en/docs/mt5/platform/components/datafeeds/djprimetassnewsfeeder)
                -   [DJ News Feeder](/en/docs/mt5/platform/components/datafeeds/djnewsfeeder)
                -   [IQFeeder](/en/docs/mt5/platform/components/datafeeds/iqfeeder)
                -   [MetaTrader 4 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader4feeder)
                -   [MetaTrader 5 Feeder](/en/docs/mt5/platform/components/datafeeds/metatrader5feeder)
                -   [Trading Central News Feeder](/en/docs/mt5/platform/components/datafeeds/tcnewsfeeder)
                -   [MetaTrader 5 UniFeeder](/en/docs/mt5/platform/components/datafeeds/metatrader5unifeeder)
                -   [Thomson Reuters Feeder](/en/docs/mt5/platform/components/datafeeds/thomsonreutersfeeder)
                -   [RSS News Feeder](/en/docs/mt5/platform/components/datafeeds/rssnewsfeeder)
                -   [IBTimes News Feeder](/en/docs/mt5/platform/components/datafeeds/ibtnewsfeeder)
                -   [ForexPros Feeder](/en/docs/mt5/platform/components/datafeeds/forexprosfeeder)
                -   [KnowledgeView News Feeder](/en/docs/mt5/platform/components/datafeeds/knowledgeviewnewsfeeder)
                -   [FXstreet Feeder](/en/docs/mt5/platform/components/datafeeds/fxstreetfeeder)
                -   [Financial Source News Feeder](/en/docs/mt5/platform/components/datafeeds/financialsourcenewsfeeder)
                -   [Claws & Horns Feeder](/en/docs/mt5/platform/components/datafeeds/clawshornsfeeder)
                -   [UniNewsFeeder](/en/docs/mt5/platform/components/datafeeds/uninewsfeeder)
                -   [Alliance News Feeder](/en/docs/mt5/platform/components/datafeeds/alliancenewsfeeder)
                -   [Newsquawk](/en/docs/mt5/platform/components/datafeeds/newsquawk)
                -   [Remote Datafeed](/en/docs/mt5/platform/components/datafeeds/remote_datafeed)
                -   [Universal DDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde)
                    -   [Installation and Setup](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_setup)
                    -   [Setting Up Symbols](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols)
                    -   [Filtration of Quotes](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_filtration)
                    -   [UniFeeder Protocol](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_protocol)
            -   [Gateways](/en/docs/mt5/platform/components/gateways)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[Data Feeds](/en/docs/mt5/platform/components/datafeeds)[Universal DDE Connector](/en/docs/mt5/platform/components/datafeeds/unidde)Filtration of Quotes

# Filtration of Quotes

Universal DDE Connector has the built-in system of automatic filtration of received quotes before they are passed to the [history server](/en/docs/mt5/platform/components/history_server). The filtration system consists of several components:

## Selecting the Best Banks

One of the most effective ways of cleaning quotes is the automatic selection of the best [banks](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols#bank) based on statistic data on them. If you tick off "Auto" for the list of banks, UniDDE will start collecting statistics of symbol quotes from banks. Based on this statistics, once a day (except for holidays) several best banks are selected and automatically added to the ["List of banks"](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols#bank_list). Next day filtering of quotes will be performed according to this list. If the selected list of banks is satisfying, you can disable Auto.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The automatic selection of the list of banks according to the collected results is performed once a day. I.e. the list will be empty the first day.</span></p></td></tr></tbody></table>

## Cleaning from "White" Noise [#](unidde_filtration#white_noise)

For a milder cleaning of the quotes thread from the "white" noise, another new adaptive filtration mechanism is used — ["Automatic filter"](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols#automatic_filter). It analyzes the average deviation of received prices and sifts away questionable quotes that fit several template situations.

Very often the thread filtration requires analysis of the next quote for making a decision about the previous questionable price, which may slow down data delivery. But the automatic filter in UniDDE does not allow questionable prices stay longer than half a second. This condition can let some questionable quotes in, but there is one more filtration level described below.

## Rough Protection [#](unidde_filtration#auto_limit)

For a rough protection from erroneous price substitution from other symbols the ["Auto Limit"](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols#auto_limit) mode is used, which doesn't let in new prices if they differ from previous ones by more than the specified number of percents.

[Setting Up Symbols](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_symbols)

[UniFeeder Protocol](/en/docs/mt5/platform/components/datafeeds/unidde/unidde_protocol)