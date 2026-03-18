# Personal Data

> Source: https://support.metaquotes.net/en/docs/mt5/manager/account_personal

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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)[Clients and Trading Accounts](/en/docs/mt5/manager/accounts)Personal Data

# Personal Data

Here you can view and edit account holder's personal data:

![Personal details of the account holder](/en/docs/mt5/manager/img/account_view_personal.png "Personal details of the account holder")

The following data is specified for an account:

-   Name — name of an account holder.
-   Last Name — second name of the account owner.
-   Middle Name — middle name of the account owner.
-   Company — name of an account holder's company.
-   Registered — account registration date. The date is added automatically during account creation. Please be careful when changing the registration date manually: the data should fit the account trading history, and thus there should not be any trading operations before the registration date. Otherwise, such operations can be ignored when generating [reports](/en/docs/mt5/manager/reports).
-   Language — user's language. If the account is created through the client terminal, the language is set automatically based on the terminal's interface language.
-   Status — status of an account holder, RE (resident) or NR (non-resident).
-   Lead Source, Lead Campaign — website, from which a client has come (lead source), and a name of a marketing campaign that attracted the client (lead campaign).  
    These fields are used to analyze marketing campaigns and track where clients come from. To receive the data, add the following labels to the client or mobile platform download link:

<table class="table" cellspacing="0" cellpadding="5" border="1"><tbody><tr class="table"><td class="table"><p class="p_CodeExample"><span class="f_CodeExample">https://download.terminal.free/cdn/web/metaquotes.ltd/mt5/mt5setup.exe</span><span class="f_CodeExample" style="background-color: #dce6f2;">?utm_source=YourWebsite&amp;utm_campaign=YourCampaign</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt5/ios</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_source=YourWebsite&amp;utm_campaign=YourCampaign</span><br><span class="f_CodeExample">https://download.terminal.free/cdn/mobile/mt5/android</span><span class="f_CodeExample" style="background-color: #dce6f2;">?server=ABC-Demo,ABC-Real&amp;utm_source=YourWebsite&amp;utm_campaign=YourCampaign</span></p></td></tr></tbody></table>

Here YourCampaign is the company name, and YourWebsite is the address of the website hosting the link. In the "server" parameter of the mobile platform links, enter the list of your servers to be shown to traders when they open an account.  
When opening a demo account and connecting to any trading account via the terminal downloaded using such a link, utm\_source and utm\_campaign values are set in a client record at the server side. If the fields are already filled, the label values are not overwritten when re-connecting to the account (even if the terminal used for connection was downloaded by a link containing other labels).

-   ID number — number of a passport, tax ID or any other unique identifiers of an account holder.
-   MetaQuotes ID — during installation of mobile MetaTrader 5 for [iPhone](https://download.terminal.free/cdn/mobile/mt5/ios?hl=en&utm_campaign=download&utm_source=metatrader5.help "iPhone") or [Android](https://download.terminal.free/cdn/mobile/mt5/android?hl=en&utm_campaign=download&utm_source=metatrader5.help "Android") a unique MetaQuotes ID is provided to every user. This identifier is used like a phone number. After specifying MetaQuotes ID in the desktop version of the client terminal, users can send notifications of different trade events to their mobile devices. MetaQuotes ID is also supported at [MQL5.community](https://www.mql5.com/en "MQL4.com"): after specifying an ID in the profile, a user is able to receive important notifications from the website and communicate with other community participants via personal messages. You can find more details in the article [MetaQuotes ID in MetaTrader Mobile terminal](https://www.mql5.com/en/articles/476 "The article MetaQuotes ID in MetaTrader Mobile Terminal").  
    MetaQuotes ID is added to the client record on the server side, once the client specifies it in the terminal settings. To [send a message](/en/docs/mt5/manager/communication) to the client, click Notification.
-   E-mail — e-mail address.
-   Phone — phone number.
-   Country — country of residence.
-   State — state (region) of residence.
-   City/Town — city/town of residence.
-   Zip code — zip or postal code.
-   Address — client's address.
-   Comment — text comment to an account.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">When opening a demo account from the client terminal, the client's country and city/town are filled in using GeoIP data. If defining a location by GeoIP is impossible, a language of the client's operating system is used.</span></li><li class="p_tableatten"><span class="f_tableatten">Lead Source and Lead Campaign data from terminal download links can be written to created accounts only if the broker has a <a href="https://support.metaquotes.net/en/docs/mt5/platform/administration/integration/integration_finteza" target="_blank" class="weblink">Finteza license</a>.</span></li></ul></td></tr></tbody></table>

## Automatic correction of personal data [#](account_personal#fix)

The manager terminal includes a function for automatic correction of personal data in the database of trading accounts:

-   Names are converted to the proper case: First Name Last Name.
-   Country names are converted to standard ones.
-   Phone numbers are formatted to a unified style: +countrycode number. If the phone number does not initially include a country code, it will be added according to the country specified in the account/client data.

To apply the function, select accounts and click "Bulk Operations\\Fix Personal Data" in the context menu:

![Automatic correction of personal data](/en/docs/mt5/manager/img/account_personal_fix.png "Automatic correction of personal data")

[Exposure](/en/docs/mt5/manager/account_exposure)

[Account Trading Settings](/en/docs/mt5/manager/account_tradeaccount)