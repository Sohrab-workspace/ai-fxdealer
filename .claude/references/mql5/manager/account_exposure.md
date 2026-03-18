# Exposure

> Source: https://support.metaquotes.net/en/docs/mt5/manager/account_exposure

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
            -   [Clients](/en/docs/mt5/manager/clients)
            -   [Online Accounts](/en/docs/mt5/manager/online_accounts)
            -   [Creation of Accounts](/en/docs/mt5/manager/account_create)
            -   [Importing Accounts](/en/docs/mt5/manager/account_import)
            -   [Preliminary Accounts](/en/docs/mt5/manager/preliminary_accounts)
            -   [Push Notifications, SMS and Mail](/en/docs/mt5/manager/communication)
            -   [Account Overview](/en/docs/mt5/manager/account_overview)
            -   [Exposure](/en/docs/mt5/manager/account_exposure)
            -   [Personal Data](/en/docs/mt5/manager/account_personal)
            -   [Account Trading Settings](/en/docs/mt5/manager/account_tradeaccount)
            -   [Balance Operations](/en/docs/mt5/manager/account_balance)
            -   [Trading Operations](/en/docs/mt5/manager/account_trading)
            -   [Account History](/en/docs/mt5/manager/account_history)
            -   [Security and Certificates](/en/docs/mt5/manager/account_security)
        -   [Trading Operations](/en/docs/mt5/manager/trading)
        -   [Corporate Actions and Bulk Operations](/en/docs/mt5/manager/corporate_actions)
        -   [Dealing and Risk Management](/en/docs/mt5/manager/dealing_risk_management)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Exposure

# Exposure

The Exposure tab contains the current account assets grouped by currencies.

![Exposure](/en/docs/mt5/manager/img/account_view_exposure.png "Exposure")

The following information is available:

-   Assets — name of a currency or financial instrument.
-   Volume — client's position volume (in units) for the currency or financial instrument including leverage.
-   Rate — currency or instrument rate in relation to the deposit currency.
-   Deposit currency — amount of deposit currency (excluding leverage) actually expended to buy/sell the currency or trading instrument.
-   Graph — graphical representation of the client's position in the deposit currency (blue bars show long positions, red ones denote short ones).
-   Long/Short Positions — information on long and short positions in the form of a diagram. To switch between long and short position diagrams, click the diagram name or use the context menu.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The assets of an account by a deposit currency are displayed considering free margin.</span></p></td></tr></tbody></table>

## Account status

The trading account status bar is displayed under the exposure data:

-   Balance — money on an account, not accounting for the results of currently open positions.
-   Equity — money accounting for the results of the currently open positions.
-   Margin — money required to cover open positions.
-   Free Margin — free amount of money that can be used to maintain open positions.
-   Margin Level — percentage of an account equity to a margin volume.

## Context menu [#](account_exposure#context)

The following commands can be run from the context menu of this tab:

-   Diagram — open the diagram control submenu:

-   Long Positions — display the diagram on buy positions.
-   Short Positions — display the diagram on sell positions.
-   Hide — hide the diagram.
-   ![Save](/en/docs/mt5/manager/img/save_icon.png "Save") Save — save the information about assets as an HTML file.
-   Report — generate a report on assets in the XML or HTML format.
-   Grid — show/hide grid to separate the fields.
-   Auto Arrange — enable/disable auto arrange of column sizes when resizing the window.

[Account Overview](/en/docs/mt5/manager/account_overview)

[Personal Data](/en/docs/mt5/manager/account_personal)