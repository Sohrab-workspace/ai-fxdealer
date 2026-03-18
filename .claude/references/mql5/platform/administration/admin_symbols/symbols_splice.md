# Splicing Futures

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/admin_symbols/symbols_splice

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
        -   [Platform Installation](/en/docs/mt5/platform/platform_installation)
        -   [Platform Components](/en/docs/mt5/platform/components)
        -   [Platform Setup](/en/docs/mt5/platform/administration)
            -   [General Information](/en/docs/mt5/platform/administration/common_info)
            -   [Start Page](/en/docs/mt5/platform/administration/admin_start)
            -   [Network cluster](/en/docs/mt5/platform/administration/admin_network)
            -   [Integrations](/en/docs/mt5/platform/administration/integration)
            -   [Security](/en/docs/mt5/platform/administration/security)
            -   [Automations](/en/docs/mt5/platform/administration/automation)
            -   [Time](/en/docs/mt5/platform/administration/admin_time)
            -   [Holidays](/en/docs/mt5/platform/administration/admin_holidays)
            -   [Leverages](/en/docs/mt5/platform/administration/leverages)
            -   [Groups](/en/docs/mt5/platform/administration/admin_groups)
            -   [Clients](/en/docs/mt5/platform/administration/clients)
            -   [Accounts](/en/docs/mt5/platform/administration/admin_accounts)
            -   [Payments](/en/docs/mt5/platform/administration/payments)
            -   [Managers](/en/docs/mt5/platform/administration/admin_managers)
            -   [Orders](/en/docs/mt5/platform/administration/admin_orders)
            -   [Deals](/en/docs/mt5/platform/administration/admin_deals)
            -   [Positions](/en/docs/mt5/platform/administration/admin_positions)
            -   [Gateways](/en/docs/mt5/platform/administration/admin_gateways)
            -   [Data Feeds](/en/docs/mt5/platform/administration/admin_feeds)
            -   [Plugins](/en/docs/mt5/platform/administration/admin_plugins)
            -   [Reports](/en/docs/mt5/platform/administration/admin_reports)
            -   [Ultency](/en/docs/mt5/platform/administration/ultency)
            -   [ECN](/en/docs/mt5/platform/administration/ecn)
            -   [Routing](/en/docs/mt5/platform/administration/requests_routing)
            -   [Funds & ETF](/en/docs/mt5/platform/administration/fund_etf)
            -   [Symbols](/en/docs/mt5/platform/administration/admin_symbols)
                -   [Symbol Settings](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings)
                -   [Splicing Futures](/en/docs/mt5/platform/administration/admin_symbols/symbols_splice)
                -   [Import of Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_import)
                -   [Collateral Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_collateral)
            -   [Spreads](/en/docs/mt5/platform/administration/spreads)
            -   [1 Minute History Charts](/en/docs/mt5/platform/administration/admin_charts)
            -   [Bid/Ask/Last Ticks](/en/docs/mt5/platform/administration/admin_ticks)
            -   [Synchronization](/en/docs/mt5/platform/administration/admin_synchronization)
            -   [Subscriptions](/en/docs/mt5/platform/administration/subscriptions)
            -   [Mailbox](/en/docs/mt5/platform/administration/mail)
            -   [Live Update](/en/docs/mt5/platform/administration/admin_update)
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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)[Symbols](/en/docs/mt5/platform/administration/admin_symbols)Splicing Futures

# Splicing Futures

MetaTrader 5 trading platform allows users to splice the quotes of the symbols having a single underlying but different validity periods. Futures can serve as examples of such symbols. Spliced symbol charts allow performing technical analysis of prices for an underlying asset.

It is possible to splice not only bars but tick data as well. Please note that tick data take much more disk space compared to minute history. After splicing, same ticks are stored separately for source symbols and a spliced one.

To splice the futures, a new symbol should be created. The history of quotes of this symbol will represent splicing of several futures with one underlying asset. Also, quotes of the front futures will be broadcast in real time at this symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The front futures is a futures with the closest expiration date.</span></p></td></tr></tbody></table>

![Splicing Futures](/en/docs/mt5/platform/img/splice_symbol.png "Splicing Futures")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Since the splicing symbol is created solely for analytical purposes, the ability to trade it should be disabled at <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#trade_disabled" class="topiclink">"Trade"</a> tab.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Splicing symbols are not influenced by <a href="/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions" class="topiclink">session settings</a>, because the sessions of original symbols may differ.</span></li></ul></td></tr></tbody></table>

["Exchange Futures" calculation type](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_trade#trade_disabled) should be set on the symbol's "Trade" tab. Also, the following parameters should be set for the symbol:

-   name should be specified in "Symbol" field of ["Common"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common) tab ;
-   additional information can be specified in "Description" field (optional);
-   a link to the web page can be specified in "Page" field (optional);
-   market depth should be enabled;
-   spread, spread balance, prices, etc. settings on the "Common" tab should be disabled;
-   quote sessions from 00:00 to 24:00 on all days should be set on ["Sessions"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions) tab (session borders are often defined by an exchange shortly before the sessions themselves; these settings are set to ensure getting into the exchange's quote sessions);
-   set underlying asset and splicing settings according to the instruction below.

All other symbol parameters are of no importance.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The following settings of the splicing symbol must match the settings of the symbols used for splicing:</span></p><ul><li class="p_tableatten"><span class="f_tableatten">Tick size</span></li><li class="p_tableatten"><span class="f_tableatten">Digits</span></li><li class="p_tableatten"><span class="f_tableatten">Market depth (size)</span></li></ul></td></tr></tbody></table>

## Setting an Underlying Asset

The underlying asset, according to which the splicing will be performed, should be specified in "Basis" field of ["Common"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_common) tab. The quotes of all symbols with the specified underlying asset will participate in splicing.

## Configuring Splicing

As a rule, several futures having different expiration dates are simultaneously traded for the same underlying asset. A point, at which the quotes of one futures are replaced with the quotes of another, is called a splicing point.

The splicing type is set first. Despite a single underlying asset, the level of price for futures having different expiration dates may differ. Thus, considerable drops may form in their splicing points. The trading platform allows splicing the prices both with and without reducing the price to a single level.

-   Unadjusted — splicing of quotes is performed without reducing the price level of the previous (expiring) contract to the prices of the next one (or a frontal one — futures with the closest expiration date). In this case, real quotes will be available in history.
-   Adjusted — the difference between the last quote of the previous (expiring) contract and the first quote of the new front contract is calculated during splicing. The calculated difference is added/deducted from all previous quotes leading to the adjustment of the price level. This method allows forming a smooth final chart convenient for full-scaled technical analysis. However, the history will contain reduced quotes instead of actual ones.

The main step in setting up splicing is defining a splicing point. The trading platform has the ability to define a splicing point relative to a symbol's expiration date. Each symbol has its expiration date shown in "To" field of ["Sessions"](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions) tab.

Futures splicing can be performed either at the moment of a current (front) contract's expiration or with a shift from that moment by the specified number of days. The point of switching to the quotes of the next contract depends on the "Splice shift" parameter. If it is set to 0, the quotes switch at the moment of the current contract's expiration, otherwise — the specified number of days earlier than its expiration.

After saving the symbol, the platform will start splicing and its chart will become available for viewing. Also, quotes of the front futures will be broadcast in real time at this symbol. And depending on the "Splice shift" parameter the symbol will switch to the quotes of the next contract at the moment of the current contract's expiration or the specified number of days earlier than its expiration.

Detailed information about splicing points and transformation prices can be found in the [journal](/en/docs/mt5/platform/administration/admin_network/network_journal) of the history server.

## Example of splicing

Let's consider the example of splicing of three symbols:

-   RTS-9.12 futures for RTS underlying with the expiration date of 2012.09.15 15:45
-   RTS-12.12 futures for RTS underlying asset with the expiration date of 2012.12.15 15:45
-   RTS-3.13 futures for RTS underlying asset with the expiration date of 2013.03.15 15:45.

Let's specify the following settings for the splicing symbol:

-   Symbol — @RTS;
-   Basis — RTS;
-   Splice — Adjusted;
-   Date — Expiration;
-   Shift — 1.

After saving the symbol, check the splicing by the history server's journal:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">2013.02.15&nbsp;</span><span class="f_CodeExample">09:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">35&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">HistoryBase</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">@RTS</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">continuous</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">build</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">from</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">RTS-</span><span class="f_CodeExample">3.13&nbsp;</span><span class="f_CodeExample">[</span><span class="f_CodeExample">2012.12.14</span><span class="f_CodeExample">-</span><span class="f_CodeExample">2013.03.14</span><span class="f_CodeExample">][</span><span class="f_CodeExample">45638&nbsp;</span><span class="f_CodeExample">bars</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">updated][adjustment</span><span class="f_CodeExample">&nbsp;0&nbsp;</span><span class="f_CodeExample">pips]</span><br><span class="f_CodeExample">2013.02.15&nbsp;</span><span class="f_CodeExample">09:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">37&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">HistoryBase</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">@RTS</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">continuous</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">build</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">from</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">RTS-</span><span class="f_CodeExample">12.12&nbsp;</span><span class="f_CodeExample">[</span><span class="f_CodeExample">2012.09.14</span><span class="f_CodeExample">-</span><span class="f_CodeExample">2012.12.14</span><span class="f_CodeExample">][</span><span class="f_CodeExample">72600&nbsp;</span><span class="f_CodeExample">bars</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">updated][adjustment</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample">40&nbsp;</span><span class="f_CodeExample">pips]</span><br><span class="f_CodeExample">2013.02.15&nbsp;</span><span class="f_CodeExample">09:</span><span class="f_CodeExample">24</span><span class="f_CodeExample">:</span><span class="f_CodeExample">39&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">HistoryBase</span><span class="f_CodeExample">&nbsp;&nbsp;&nbsp;</span><span class="f_CodeExample">@RTS</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">continuous</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">build</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">from</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">RTS-</span><span class="f_CodeExample">9.12&nbsp;</span><span class="f_CodeExample">[</span><span class="f_CodeExample">2011.06.06</span><span class="f_CodeExample">-</span><span class="f_CodeExample">2012.09.14</span><span class="f_CodeExample">][</span><span class="f_CodeExample">70532&nbsp;</span><span class="f_CodeExample">bars</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">updated][adjustment</span><span class="f_CodeExample">&nbsp;</span><span class="f_CodeExample">-</span><span class="f_CodeExample">220&nbsp;</span><span class="f_CodeExample">pips]</span></p></td></tr></tbody></table>

The example above shows the splicing of three symbols. The splicing is performed the day before the symbol's expiration.

The quotes' period that has got into the final spliced symbol, as well as the value, by which the previous quotes have been shifted, while splicing with that symbol, should be be specified for each symbol.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Splicing may take some time. A large volume of the accumulated tick data on spliced symbols may greatly affect a splicing time. However, splicing is performed asynchronously — charts are completed step by step without interfering with the platform operation.</span></p></td></tr></tbody></table>

[Sessions](/en/docs/mt5/platform/administration/admin_symbols/admin_symbols_settings/symbol_settings_sessions)

[Import of Symbols](/en/docs/mt5/platform/administration/admin_symbols/symbols_import)