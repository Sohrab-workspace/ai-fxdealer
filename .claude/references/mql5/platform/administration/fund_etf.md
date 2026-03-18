# Funds and ETFs

> Source: https://support.metaquotes.net/en/docs/mt5/platform/administration/fund_etf

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

[MetaTrader 5](/en/docs/mt5)[Platform](/en/docs/mt5/platform)[Platform Setup](/en/docs/mt5/platform/administration)Funds & ETF

# Funds and ETFs

An investment fund is a way of investing money, in which investors do not have to trade in the market themselves. They entrust their money to an organization, which then manages the funds, for example by investing them in certain securities. The profit obtained from the funds turnover is further distributed among investors, while the fund receives a certain fee for the investment and management activities.

MetaTrader 5 enables the automation of fund and ETF operation:

-   Manage investors and keep detailed records of investments. Fund management is performed according to a traditional scheme adopted in the platform: you create investor accounts, add relevant investment amounts to their balances and add these accounts to a special fund investors section.
-   Work with the fund managers. Similarly to investors, managers are added in the system in the form of regular trading accounts. Invested assets are credited to these accounts and are further used to perform trading operations.
-   Automatically build AUM (Assets Under Management) charts. The money invested is credited to regular trading accounts, in which it is used by the fund managers for trading (management). The platform automatically builds the AUM charts based on the account equity data and taking into account applicable management and success fees. Investors can view this chart in the desktop, mobile and web terminals by connecting using their trading accounts, similar to regular traders.
-   Automate the calculation of fees and payments to investors. You do not need to use third-party accounting systems. The platform provides flexible fund settings, which include the hurdle rate, fees, fee calculation frequency and payment mode among others.
-   Provide real-time fund performance information to investors. Investors can view the fund charts and the current value of the shares by simply connecting to the trading account via the MetaTrader 5 desktop, mobile or web terminal.
-   Receive [fund performance reports](/en/docs/mt5/platform/administration/admin_reports/fund_overview_report).

## Create symbols to display the fund yield [#](fund_etf#symbols)

For each fund, you should create three financial instruments: to display [NAV (Net Asset Value)](/en/docs/mt5/platform/administration/fund_etf#nav_formula) chart, [AUM (Assets Under Management)](/en/docs/mt5/platform/administration/fund_etf#aum_formula) chart and [fund performance](/en/docs/mt5/platform/administration/fund_etf#performance_formula). In the future, NAV displaying symbols will also be used for buying shares, i.e. it will be possible to invest by simply opening a regular trading position via the client terminal.

Add a separate funds section under the ["Symbols" section](/en/docs/mt5/platform/administration/admin_symbols) and create financial instruments. They do not require any specific settings.

![Creating financial instruments to display NAV](/en/docs/mt5/platform/img/funds_add_symbol.png "Creating financial instruments to display NAV")

## Create funds and configure general settings [#](fund_etf#common)

Create a configuration for each fund under the "Funds and ETF" section:

![Creating fund configuration](/en/docs/mt5/platform/img/funds_add.png "Creating fund configuration")

Set up the following parameters under the Common section:

-   Name — the fund name.
-   Symbol — the name of the trading symbol, in which the [NAV (Net Asset Value)](/en/docs/mt5/platform/administration/fund_etf#nav_formula) will be reflected.
-   Assets symbol — the name of the trading symbol, in which a change in the [AUM (Assets Under Managements)](/en/docs/mt5/platform/administration/fund_etf#aum_formula) will be shown.
-   Performance symbol — the name of the trading symbol, which will reflect the [fund performance](/en/docs/mt5/platform/administration/fund_etf#performance_formula) chart.
-   Trade server — the [trade server](/en/docs/mt5/platform/administration/admin_network/network_add_edit/network_trade_server), on which the fund will be managed. Only accounts opened on the selected server can be used to created [investors](/en/docs/mt5/platform/administration/fund_etf#investors) and fund [managers](/en/docs/mt5/platform/administration/fund_etf#trade_accounts). They cannot be created on different servers.
-   Manager — the account of the [manager](/en/docs/mt5/platform/administration/admin_managers), who will administer the fund. Currently the field is not used. In the future, the field will be used to grant separate permissions to access the fund reports, as well as to change the lists of investors and managers.
-   Recalculation — [fund charts calculation](/en/docs/mt5/platform/administration/fund_etf#fund_parameters) mode:

-   Every minute — the fund chart is recalculated every minute, after which appropriate quotes are added to the symbols' price stream.
-   Every hour — the fund chart is recalculated every hour, after which appropriate quotes are added to the symbols' price stream.
-   Daily — the fund chart is recalculated at the end of each trading session, after which appropriate quotes are added to the symbols' price stream.
-   Manually — the platform does not calculate fund performance variables and does not generate charts. This mode should be used when broadcasting fund data from external sources via [gateways](/en/docs/mt5/platform/administration/admin_gateways) or [data feeds](/en/docs/mt5/platform/administration/admin_feeds).
-   Type — fund type:

-   Open-end — the shares of such a fund can be purchased or sold at any day. The assets of the fund can be freely increased or decreased.

-   Closed-end — unlike the previous type, the capital of such a fund cannot be changed. The fund issues a limited number of shares, which will not change in the future.
-   Period — the fund lifetime. The platform performs any operations concerning the fund (such as calculations, charting, fee charging, etc.) only within the specified period.
-   Maximum capital — the maximum allowable amount of investments within the fund. Investors and their shares are managed [under a separate section of fund settings](/en/docs/mt5/platform/administration/fund_etf#investors). When the investment amount reaches the specified value, the platform will prevent from further adding of new investors or from increase of shares of existing investors.
-   Currency — the currency in which all the fund variables are calculated: prices, commissions, etc. For example, AUM (Assets under Management) is calculated based on the funds on [trading accounts](/en/docs/mt5/platform/administration/fund_etf#trade_accounts). If the trading account deposit currency is GBP, while the fund currency is USD, the funds will be converted at the current GBPUSD rate when calculating AUM.
-   Maximum investors — the maximum number of investors who can purchase the fund shares (specified [under a separate section of fund settings](/en/docs/mt5/platform/administration/fund_etf#investors)).

## Configure payments and fees [#](fund_etf#fees)

The MetaTrader 5 trading platform enables the automation of all calculations concerning the fund: management fees and payments of returns.

Before configuring payments, you should [create a separate trading account](/en/docs/mt5/platform/administration/admin_accounts/account_add) for each fund: all relevant payments will be performed in this account ("Fees account"). It is recommended to [create a separate group](/en/docs/mt5/platform/administration/admin_groups) for such accounts, while this enables more convenient work with accounts (including granting of appropriate access permissions to managers).

![Create a separate payment account for the fund](/en/docs/mt5/platform/img/fund_fees_account.png "Create a separate payment account for the fund")

### Management fees [#](fund_etf#management_fee)

The company which manages the fund, charges investors a certain fee for the services. This is usually equal to a percentage of the [Assets Under Management (AUM)](/en/docs/mt5/platform/administration/fund_etf#aum_formula). This is referred to as the "Management fees". All relevant calculation parameters are specified under the fund's "Fees" section:

-   Distribution — fee distribution mode. If "Automatic", the fee will be calculated by the platform. The "Report" mode enables manual calculation using external data.
-   Period — fee calculation and distribution frequency: daily, monthly, quarterly or yearly.
-   Fees account — a special trading account, to which fund management fees will be credited.
-   Management fee — the fund management fee as a percentage of [AUM](/en/docs/mt5/platform/administration/fund_etf#aum_formula). The calculation can also be based on assets values as of the beginning of the calculation period, end of period, or as an average value over a period. For example, if you select quarterly or period beginning calculation, the specified percentage will be calculated based on AUM as of the end of the previous quarter.

![Configuring the fund payments](/en/docs/mt5/platform/img/fund_fees.png "Configuring the fund payments")

Management Fee is calculated using the following formula:

Management Fee = (Fund Equity \* Days \* Management Fee Percent/100)/365

where:

-   'Fund Equity' is the fund value at the time of calculation
-   'Days' is the calculation period
-   'Management Fee Percent' is the management fee in percent

On a selected basis, the platform will calculate the management fees and will transfer the relevant amount to the special account, which is specified in the fund settings ("Fees account"). The accrual is performed as a balance operation of Commission type, with a comment "MF '\[Fund Name\]'". For example, "MF 'ENTHIGH'".

The fees account balance is taken into account when [calculating fund values](/en/docs/mt5/platform/administration/fund_etf#fund_parameters), including its AUM. Actually, each management fee transfer reduces the fund's AUM by an appropriate amount. Nothing is deducted from [investor accounts](/en/docs/mt5/platform/administration/fund_etf#investors).

### Success fee [#](fund_etf#success_fee)

In the case of successful fund management (i.e. profitable trading), the company may charge an additional fee, the so-called "Success fee". If during the selected period the AUM value increases by the amount, which is equal to or exceeds the threshold value (Hurdle rate), additional commission will be deducted from the fees account. All related calculation parameters are specified under the "Fees" section.

-   Distribution, Period, Fees accounts — these parameters are common for [management fee](/en/docs/mt5/platform/administration/fund_etf#management_fee) and access fee.
-   Success fee — fee as a percentage of the total returns for the current period or of the profit above the Hurdle Rate (defined in the "Calculation" field). The returns are determined separately for each share: actually it is performed by the [position on the investor account](/en/docs/mt5/platform/administration/fund_etf#investors). The success fee calculation mode is also specified here: before or after management fee calculation. The management fee affects the AUM value, which is taken into account during performance calculation. Therefore the success fee value is affected by its calculation time.
-   Calculation — determines the amount based on which success fee will be calculated: the total yield amount for the current period or the amount above the hurdle rate.
-   High water mark — the fund management success can be determined using different methods. Currently only the most popular method is supported in the platform: "High water mark". In accordance with this method, management in the calculation period is considered successful if the increase per share (positions on the investor account) exceeds the hurdle rate. You can select how the excess shall be determined: over the entire fund management period, the last year or the last quarter.
-   Hurdle rate — is the threshold rate of return. If exceeded during the selected period (specified in "High water mark"), the fund management is considered successful and a commission fee will be charged.

The calculated success fee is deducted from investor accounts as a balance operation of "Commission" type with a comment "SF '\[Fund Name\]'". For example, "SF 'ENTHIGH'". Further this amount is transferred to the "[Fees account](/en/docs/mt5/platform/administration/fund_etf#fees_account)" as a Commission operation. A comment for this operation is specified as "SF '\[Fund Name\]'-'\[Investor account from which the commission has been debited\]'". For example, "SF 'ENTHIGH'-'1235966'".

For each position on investor accounts, the platform performs the following actions:

-   Determines the Hurdle rate of the share (position): "Maximum share value (NAV) over the High water mark period" + "NAV Hurdle Rate". The platform calculates the maximum position value over the entire time, over the last year or over the last quarter, depending on the "High water mark" parameter. The position value is calculated as volume multiplied by [NAV](/en/docs/mt5/platform/administration/fund_etf#nav_formula), its maximum value is searched in the price history of the appropriate symbol. Then "Hurdle rate" percentage of this amount is calculated and added to the total value.
-   Then the platform checks if share profit exceeded the hurdle rate: "NAV at the end of the period" - "Hurdle rate". It means that the platform uses the position value as at the calculation time (before or after charging the management fee) and deducts the hurdle rate calculated at the previous stage, from the position value.
-   The share value (NAV) is determined: "NAV at the end of the period" - "Maximum NAV over the High water mark period". The values are calculated as shown in previous points.
-   If the share profit is negative (loss), zero, or it does not exceed the Hurdle Rate, the success fee is not charged.
-   If the share profit exceeds the Hurdle Rate, the success fee is calculated in accordance with the Calculation field value:
-   Soft: Profit per share \* Success fee. The fee is calculated as percentage of share profit calculated above.
-   Hard: Profit beyond the Hurdle Rate \* Success fee.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The "Fees account" balance is taken into account when calculating the <a href="/en/docs/mt5/platform/administration/fund_etf#aum_formula" class="topiclink">AUM</a>. Thus, charging of any management fees reduces the AUM value.</span></li><li class="p_tableatten"><span class="f_tableatten">Use a separate trading account for each fund's "Fees account". Do not perform any other operations on this account.</span></li></ul></td></tr></tbody></table>

## Set up trading accounts for fund managers [#](fund_etf#trade_accounts)

Common trading accounts are used for managing invested funds. You distribute funds between these accounts and then the managers connect to these accounts and perform trading operations.

[Create a separate trading account](/en/docs/mt5/platform/administration/admin_accounts/account_add) for each fund manager. It is recommended to [create a separate group](/en/docs/mt5/platform/administration/admin_groups) for such accounts, while this enables more convenient work with the accounts (for example, generation of relevant reports). Then transfer the investors' funds to these accounts, for example, by performing balance operations using the Manager terminal.

Once you have prepared the accounts, specify them in the fund settings, under the "Trading Accounts" section:

![Trading manager accounts](/en/docs/mt5/platform/img/funds_trading_accounts.png "Trading manager accounts")

The current balances and equity amounts will be instantly shown for each of the manager accounts.

The [current fund AUM value](/en/docs/mt5/platform/administration/fund_etf#fund_parameters) is calculated based on the equity amounts available on the trading manager accounts.

## Set the investors [#](fund_etf#investors)

The fund investors are also managed using trading accounts.

[Create a separate trading account](/en/docs/mt5/platform/administration/admin_accounts/account_add) for each investor. It is recommended to [create a separate group](/en/docs/mt5/platform/administration/admin_groups) for such accounts. Make sure to use [hedging position accounting](/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk) for an investor group. Once the share purchaser invests the required funds, distribute them between the trading accounts of the [trading managers](/en/docs/mt5/platform/administration/fund_etf#trade_accounts). Next, to allocate a share, open on the investorss account a long trading position for the [fund symbol](/en/docs/mt5/platform/administration/fund_etf#symbols), while the position size should be equal to the relevant share. For example, if the share size is 1000, then the position size on the investors account should be 1000 lots (provided that the symbol contract size is 1).

Thus, the investor will be able to monitor their investments by connecting to the trading account via the client terminal. The investor will have access to [three fund charts](/en/docs/mt5/platform/administration/fund_etf#fund_parameters), as well as to their share state, which is displayed as a trading position. The trading position state will be updated in accordance with the current total fund value (the update frequency depends on the "[Recalculation](/en/docs/mt5/platform/administration/fund_etf#recalculation)" parameter).

To open positions on investor accounts, use the Manager terminal:

![Open a position on the investor's account through the Manager terminal](/en/docs/mt5/platform/img/fund_add_position.png "Open a position on the investor's account through the Manager terminal")

If there are no prices for the fund yet, drop the first price into the stream, otherwise an attempt to open a position will cause the terminal ot display the "no prices" error. Once all the shares have been allocated and the relevant funds have been added to the fund managers' accounts, the prices will be calculated automatically.

![Add the first fund price to the stream](/en/docs/mt5/platform/img/fund_throw_price.png "Add the first fund price to the stream")

Once you have prepared the accounts, specify them in the fund settings, under the "Investors" section:

![Trading accounts of the fund investors](/en/docs/mt5/platform/img/fund_investors.png "Trading accounts of the fund investors")

By clicking on the investor name you can view the current state of the investor's share (position). Also, maximum share value (High water mark) over [the current calculation period](/en/docs/mt5/platform/administration/fund_etf#recalculation) is shown for each share.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The volume of shares is calculated only for positions which are opened for the symbol corresponding to the current fund. No other positions opened on these accounts are taken into account in this section.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">Investor accounts should be located in <a href="/en/docs/mt5/platform/administration/admin_groups/groups_settings#risk" class="topiclink">hedging position accounting</a> groups. Otherwise, calculations in the fund may be performed incorrectly.</span></li></ul></td></tr></tbody></table>

## Allocation of additional shares

If you need to allocate additional shares within an already running fund, please pay attention to the following:

-   After allocating shares for new investors (opening positions on their accounts) and adding investors to the list, do not forget to distribute their invested funds between relevant managers' accounts. Otherwise, the NAV chart will be incorrect as the number of units has increased, while the management funds have not. Funds are distributed between managers at your discretion.
-   To avoid incorrect NAV values before you distribute funds between manager accounts, you can temporarily disable the fund. This will pause the calculation of charts. After completing the setup, turn the fund back on.
-   If incorrect prices were still added to the fund charts, you can delete such prices via the "1 Minute History Chars" and "Bid/Ask/Last Ticks" sections.

## Assets Under Management and Net Asset Value; fund performance chart [#](fund_etf#fund_parameters)

The trading platform allows tracking the fund yield dynamics in real time, similarly to tracking of common symbol quotes.

As described above, [ordinary trading instruments](/en/docs/mt5/platform/administration/fund_etf#symbols) are created for the fund. The platform automatically records the changes in NAV (Net Asset Value), the AUM value (assets under management) value and profitability into the price history of these symbols.

These charts are calculated at intervals, specified in the "[Recalculation](/en/docs/mt5/platform/administration/fund_etf#recalculation)" field. After each calculation, a quote with the appropriate fund value is added to the symbols' price history.

### Assets Under Management (AUM) [#](fund_etf#aum_formula)

The current fund value is used for calculating the fund [management fee](/en/docs/mt5/platform/administration/fund_etf#management_fee) and the [success fee](/en/docs/mt5/platform/administration/fund_etf#success_fee), as well as for calculating all other charts. It is calculated according to the following formula:

(The total amount of equity on the fund's trading accounts - management fees)

The platform sums the equity of all [trading accounts of the fund](/en/docs/mt5/platform/administration/fund_etf#trade_accounts) and deducts the amount of charged management fees. The trading account deposit currency differing from the [fund currency](/en/docs/mt5/platform/administration/fund_etf#currency) is converted at the current rate.

### Net Asset Value (NAV) [#](fund_etf#nav_formula)

The value is calculated according to the following formula:

AUM / Number of fund shares

AUM value calculated by the previous formula is divided by the [current number of shares](/en/docs/mt5/platform/administration/fund_etf#investors) allocated by the fund to its investors.

### Fund Performance [#](fund_etf#performance_formula)

The value is calculated according to the following formula:

Previous-period Performance + log(Current-period AUM / Previous-period AUM)

Here:

-   Previous-period Performance — for the first value on the chart this formula element is ignored. For the first period, the previous period performance will be zero.
-   Current-period AUM is calculated according to the AUM formula specified above.
-   Previous-period AUM is also calculated according to the above AUM formula, but for the previous period. The amount of funds deposited during the calculation period is added to this value (i.e. the money [distributed](/en/docs/mt5/platform/administration/fund_etf#trade_accounts) at the beginning of the calculation period between managers).

Period refers to the chart calculation periodicity, specified in the [Recalculation](/en/docs/mt5/platform/administration/fund_etf#recalculation) field. If charts are recalculated once a minute, the previous period is equal to the previous minute.

## Reset the Fund State [#](fund_etf#reset)

The fund state can be reset using two commands in the settings dialog:

-   Recalculation — full recalculation of fund charts: NAV, AUM and performance. The platform reproduces the entire fund history based on manager and investor accounts: investment operations, share purchases and other operations. The graph history is calculated and recorded based on this data.
-   Reset — resetting accumulated statistics used for the calculation of fund parameters, including commissions. Use this option if you need to restart the fund and exclude previously accumulated values from further calculations. For example, this operation may be needed after testing.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Use these commands with caution. Deleted values cannot be recovered.</span></p></td></tr></tbody></table>

[Example of Rules](/en/docs/mt5/platform/administration/requests_routing/routing_example)

[Symbols](/en/docs/mt5/platform/administration/admin_symbols)