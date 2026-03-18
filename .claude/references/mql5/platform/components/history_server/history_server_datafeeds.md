# Interaction with Quote Providers

> Source: https://support.metaquotes.net/en/docs/mt5/platform/components/history_server/history_server_datafeeds

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
            -   [Trade Server](/en/docs/mt5/platform/components/trade_server)
            -   [Access Server](/en/docs/mt5/platform/components/access_server)
            -   [History Server](/en/docs/mt5/platform/components/history_server)
                -   [Structure of Directories and Files](/en/docs/mt5/platform/components/history_server/history_server_structure)
                -   [Interaction with Quote Providers](/en/docs/mt5/platform/components/history_server/history_server_datafeeds)
                -   [Quotes Filtration](/en/docs/mt5/platform/components/history_server/quotes_filtration)
                -   [Console Commands](/en/docs/mt5/platform/components/history_server/history_server_console)
            -   [Backup Server](/en/docs/mt5/platform/components/backup_server)
            -   [Data Feeds](/en/docs/mt5/platform/components/datafeeds)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Components](/en/docs/mt5/platform/components)[History Server](/en/docs/mt5/platform/components/history_server)Interaction with Quote Providers

# Interaction with Quote Providers

In MetaTrader 5, [gateways](/en/docs/mt5/platform/administration/admin_gateways) and [data feeds](/en/docs/mt5/platform/administration/admin_feeds) can be used as providers of quotes. Their interaction with the history server is identical. This interaction can be analyzed in terms of the physical connection and at the level of quotes streaming.

## Physical Connection

The physical connection must be established for each source of quotes enabled in the appropriate settings of the platform. The physical connection details can be configured on the "Timeouts" tab of [gateways](/en/docs/mt5/platform/administration/admin_gateways/gateways_config#timeouts) and [data feeds](/en/docs/mt5/platform/administration/admin_feeds/feed_setup#timeouts). Let's consider the following configuration example:

-   Interval between reconnections = 5 seconds.
-   Number of reconnection attempts = 10.
-   Interval between series of reconnections = 60 seconds.

If a gateway/data feed loses connection with an external server, a reconnection attempt is made in 5 seconds. If it fails, another one is made in 5 seconds. The total number of attempts is 10. If unable to reconnect, a series of attempts is repeated after a pause of 60 seconds.

## Stream of Quotes

A stream of prices for several symbols goes through each physical connection to a quote provider.

At each point of time, the history server accepts the stream of prices for a certain symbol only from one quote provider, while other price streams of the same symbol are ignored. The source selected for the stream of prices for a symbol is considered a current (active) source for this symbol.

During operation the active source for an instrument may change. It is changed in accordance with [priority](/en/docs/mt5/platform/administration/admin_feeds#switching) settings. The priority of data feeds and gateways is determined by their position in the list.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The priority of <a href="/en/docs/mt5/platform/administration/admin_gateways" class="topiclink">gateways</a>, if they are used as a source of quotes, is always higher than that of data feeds.</span></p></td></tr></tbody></table>

The stream of prices switches to the source with a [higher priority](/en/docs/mt5/platform/administration/admin_feeds#switching) as soon as the first quotes for a symbol is received from that source.

It switches to the source with a lower priority by a timeout. In case no quotes are received from the active quote source during a certain time period (it is specified in the "Datafeeds timeout" parameter in [history server settings](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server#timeout)), then the history server switches to a source with the lower priority that provides quotes for the same symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The time to wait for a quote for a symbol is defined in the "Datafeeds timeout" parameter in <a href="/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_history_server#timeout" class="topiclink">history server settings</a>.</span></p></td></tr></tbody></table>

After a new quotes source is selected, it is considered active. All cases of server switching to streams from other sources are reflected in the [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) in the form of the following entry:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_fortable"><span class="f_fortable">2011.03.10 10:11:05 &nbsp; &nbsp;Ticks &nbsp; &nbsp;datafeed 4: &nbsp;CHFJPY activation</span></p></td></tr></tbody></table>

Here the entry means that for CHFJPY, a stream of quotes from the fourth data feed (a position in the list of data feeds at the moment the entry is made) is selected.

[Structure of Directories and Files](/en/docs/mt5/platform/components/history_server/history_server_structure)

[Quotes Filtration](/en/docs/mt5/platform/components/history_server/quotes_filtration)