# Integrated Payment Processing System

> Source: https://support.metaquotes.net/en/docs/mt5/manager/payments

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
        -   [Managing Trade Server Settings](/en/docs/mt5/manager/trade_server_settings)
        -   [Server Reports](/en/docs/mt5/manager/reports)
        -   [Analytics](/en/docs/mt5/manager/analytics)
        -   [Payments](/en/docs/mt5/manager/payments)
            -   [Controlling Payments](/en/docs/mt5/manager/payments_operations)
            -   [Processing Payments](/en/docs/mt5/manager/payments_processing)
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

[MetaTrader 5](/en/docs/mt5)[Manager](/en/docs/mt5/manager)Payments

# Integrated Payment Processing System

MetaTrader 5 features a built-in payment receiving and sending system. Your clients do not have to leave the platform in order to deposit or withdraw funds. The relevant operations can be performed straight through the trading terminal. The platform is integrated with various payment providers and thus your traders can access all the necessary deposit/withdrawal methods, including bank cards, popular wallets, and bank transfers. All transactions are securely encrypted and are completely safe.

Payment system integration with the platform ensures that you always work with a single database. All transactions are linked to accounts and client records. For example, by opening client data, you can easily see all payments along with transaction amounts, dates, cards, etc. You won't need complex and expensive integrations with payment systems and third-party CRMs.

![Integrated Payment Processing System](/en/docs/mt5/manager/img/payments.png "Integrated Payment Processing System")

The benefits of built-in services for your company:

-   Streamlined onboarding. Since the need for additional registration on your website is eliminated, users can download the trading platform, open an account, make a deposit, and start trading. This accelerates the account opening process for potential customers and enables a seamless transition to real trading for demo users.
-   Cost reduction. You don't need to invest in the development, configuration, and maintenance of infrastructure for customer registration, payment processing and transaction management. This might be especially relevant for start-up companies which possess limited resources.
-   Increased deposit volumes. The natively integrated payment option simplifies the deposit process. Thus, users can faster respond to market situations by adding funds to their accounts. This contributes to overall growth in user deposits.
-   Higher deposit frequency. With all the required features available within the trading environment, your traders can maintain trading focus and engagement for longer periods. By eliminating distractions and the need for additional authentications in third-party resources, These factors will impact decision-making speed and increase the frequency of deposits accordingly.

Configure integrated payments for your traders to avoid extra expenses, to increase demo to real conversion rates, to implement seamless onboarding and to boost existing clients' deposits.

## How it works

-   You set up integration with the payment system on the server side.
-   A special section for deposits and withdrawals will become available in client terminal.
-   Your client makes a payment via the terminal and the transaction is forwarded to your payment provider for processing. Depending on the rules configured on the server, the transaction may be additionally [confirmed by the manager](/en/docs/mt5/manager/payments_processing).
-   If the transaction is successfully processed in the payment system, the corresponding balance operation is performed on the client's account in MetaTrader 5.
-   All deposit and withdrawal operations are stored in the platform database and are available in the [Active](/en/docs/mt5/manager/payments_operations) and [History](/en/docs/mt5/manager/payments_operations) sections. Transactions are linked to client records and trading accounts, so you can easily access all the necessary information whenever you need.

The manager terminal is used to control and manually process payments.

[Analytics](/en/docs/mt5/manager/analytics)

[Controlling Payments](/en/docs/mt5/manager/payments_operations)