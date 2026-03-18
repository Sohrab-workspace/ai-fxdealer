# Exposure

> Source: https://support.metaquotes.net/en/docs/mt5/manager/exposure

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
        -   [Terminal Start](/en/docs/mt5/manager/start)
        -   [Connecting to the Server](/en/docs/mt5/manager/connect)
        -   [Terminal Settings](/en/docs/mt5/manager/settings)
        -   [For Advanced Users](/en/docs/mt5/manager/beginning_advanced)
        -   [User Interface](/en/docs/mt5/manager/interface)
        -   [Clients and Trading Accounts](/en/docs/mt5/manager/accounts)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
            -   [Dealing](/en/docs/mt5/manager/dealing)
            -   [Accounts with Margin Call/Stop Out](/en/docs/mt5/manager/margin_calls)
            -   [Queue of Trade Requests](/en/docs/mt5/manager/trade_queue)
            -   [Quoting and Symbol Management](/en/docs/mt5/manager/quotes_symbols)
            -   [Summary Positions and Coverage](/en/docs/mt5/manager/summary_positions)
            -   [Exposure](/en/docs/mt5/manager/exposure)
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
        -   [Ultency](/en/docs/mt5/manager/ultency)
        -   [Subscriptions](/en/docs/mt5/manager/subscriptions)
        -   [App Store](/en/docs/mt5/manager/appstore)
        -   [Technical Support](/en/docs/mt5/manager/tech_support)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)Exposure

# Exposure

The Exposure tab contains the assets of clients and the covered assets of a company grouped by currencies. The information about the covered assets is displayed from a special coverage account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Coverage accounts are those created in groups whose names start with "coverage". For example, coverage\forex. This tab displays summary exposure for all coverage accounts of a trade server. A more detailed description about coverage is provided in the <a href="/en/docs/mt5/manager/summary_positions#coverage" class="topiclink">"Summary positions"</a>.</span></p></td></tr></tbody></table>

![Exposure](/en/docs/mt5/manager/img/toolbox_exposure.png "Exposure")

The following information is available about assets:

-   Asset — name of an asset.
-   Clients — volume of clients' positions by a selected asset (in units).
-   Coverage — volume of the positions on the coverage account by a selected asset (in units).
-   Net Total — difference between the clients' positions and the covered positions.
-   Rate — rate of converting the net total to a selected currency.
-   Net Total (Currency) — net total displayed in a selected currency. One can select a currency using the corresponding command of the context menu.
-   Positive (Currency) — positive net total displayed in a selected currency.
-   Graph — graphical ratio of clients' and covered assets as well as their net total are displayed here.

The lower part contains the Total line, which displays the summary rates by all assets. Client and covered assets are displayed on the right side as a diagram. Click on it to switch between short/long position data. The diagram can also be changed via the context menu.

## Context menu [#](exposure#context)

The following commands can be run from the context menu of this tab:

-   Currency — open the submenu of selecting a currency the net total and the positive net total will be displayed in. Any currency used as the deposit currency of a group of accounts at the server is available for selection.
-   Graph — open the submenu for managing the diagram by assets:

-   Long Positions — display the diagram by buy positions.
-   Short Positions — display the diagram by sell positions.
-   Clients — display the diagram by the clients' assets.
-   Coverage — display the diagram by the covered assets.
-   Net Total — display the diagram of the difference between clients' and covered positions.
-   Hide — hide the diagram.
-   ![Copy](/en/docs/mt5/manager/img/copy_icon.png "Copy") Copy — copy a selected line to the clipboard.
-   Report — generate a report on assets in the XML or HTML format.
-   ![Save](/en/docs/mt5/manager/img/save_icon.png "Save") Save — save the information about assets as an HTML file.
-   Reset Sort Order — restore the default sorting order.
-   Auto Arrange — if enabled, the size of columns is selected automatically.
-   Grid — show/hide the grid to separate the table fields.

[Summary Positions and Coverage](/en/docs/mt5/manager/summary_positions)

[Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)