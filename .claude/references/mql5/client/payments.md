# Deposits and withdrawals

> Source: https://support.metaquotes.net/en/docs/mt5/client/payments

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
        -   [Getting Started](/en/docs/mt5/client/startworking)
            -   [User Interface](/en/docs/mt5/client/interface)
            -   [Open an Account](/en/docs/mt5/client/acc_open)
            -   [Connect to an Account](/en/docs/mt5/client/authorization)
            -   [Deposits and withdrawals](/en/docs/mt5/client/payments)
            -   [Platform Settings](/en/docs/mt5/client/settings)
            -   [For Advanced Users](/en/docs/mt5/client/start_advanced)
        -   [Trading Operations](/en/docs/mt5/client/trading)
        -   [Price Charts, Technical and Fundamental Analysis](/en/docs/mt5/client/charts_analysis)
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

[MetaTrader 5](/en/docs/mt5)[Client terminal](/en/docs/mt5/client)[Getting Started](/en/docs/mt5/client/startworking)Deposits and withdrawals

# Deposits and withdrawals

You can manage your account balance directly within the trading platform, without the need to navigate to external sites and undergo extra authorization steps. Here is why it's convenient:

-   Increased security: no need to store extra passwords and regularly enter payment details on third-party sites.
-   Enhanced convenience: no need to switch to external resources and waste time.
-   Expanded trading opportunities: deposit money to your account whenever you need.

Open the 'Navigator \\ Payments' section. It displays the available operations: deposits and/or withdrawals, as well as the payment history.

![Manage your account balance through the Payments section](/en/docs/mt5/client/img/payments.png "Manage your account balance through the Payments section")

The following information is provided for each operation in the history:

-   Date — the date the operation was created.
-   Ticket — unique transaction number. When contacting a broker with questions concerning a specific transaction, be sure to indicate its ticket.
-   Operation — description of the transaction. The description may include the transaction type and additional information.
-   Payment system — the name of the payment system through which the transaction was executed. The list of available payment methods depends on the broker.
-   Status — the current state of the transaction: completed successfully, failed, pending processing by the broker.
-   Amount — the transaction amount in the deposit currency of your trading account.
-   Commission — fee charged by the broker for the transaction. The fee is indicated in the deposit currency of your trading account.
-   PDF — download a PDF file with an invoice. This option is only used for transactions involving [bank transfers](/en/docs/mt5/client/payments#bank_transfer).

Please note that the history displays only balance transactions conducted through the trading platform. Operations performed via alternative methods, such as the broker's website, will not appear here.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_fortable"><span class="f_fortable">The availability of the payments section depends on the brokerage company with which you opened your trading account. If the section is not available, reach out to your broker for assistance.</span></li><li class="p_fortable"><span class="f_fortable">All payment transactions are managed directly by your brokerage company with which you opened your current account. If you encounter any payment-related issues, please contact your broker directly.</span></li></ul></td></tr></tbody></table>

## Depositing to account [#](payments#deposit)

To replenish your account, specify the desired amount and currency. If the payment currency differs from your account deposit currency, the amount will be automatically converted upon crediting.

Please note that the funds will be deposited to the trading account currently active in the platform. To replenish a different account, switch to it accordingly.

![To deposit funds, enter the desired amount and select a payment system](/en/docs/mt5/client/img/payments_deposit.png "To deposit funds, enter the desired amount and select a payment system")

Select your preferred payment method: card, e-wallet, bank transfer, or another option. Each payment method may be supported by multiple payment systems which are provided by companies authorized by your broker. Choose the relevant provider in the "Payment service provider" field. The availability of payment methods and providers is entirely dependent on your broker.

Next, enter your contact email. For certain systems like PayPal, this email serves as your wallet identifier. Otherwise, it is solely used for payment notifications.

Some systems supporting card payments offer the option to [add cards](/en/docs/mt5/client/payments#add_card) for future use. With this option, you first add your card to the system, specify its details, and then use it as a ready-made payment method. Adding an account is typically not required for deposit transactions. You can proceed directly to the transaction by clicking "Continue".

After clicking "Continue", you will be redirected to a secure payment page where you will input your payment method details. Follow the instructions provided on this page. Once the transaction is complete, you will be redirected back to the payments section. To ensure a smooth transaction process, refrain from closing the payment page until you receive confirmation of its successful completion.

![Enter payment method details](/en/docs/mt5/client/img/payments_card_details.png "Enter payment method details")

Some brokers may conduct additional payment checks before crediting the payment to your account. You can track the status of your transactions in the [transaction history](/en/docs/mt5/client/payments#transactions). If you have questions about your payments, please reach out directly to your broker.

Once the transaction is completed and is approved by the broker, the relevant amount will be credited to your account as a balance operation. This operation will be displayed in the [history section](/en/docs/mt5/client/performing_deals#trade_history):

![Depositing operation](/en/docs/mt5/client/img/payments_trade_history.png "Depositing operation")

## Withdrawing funds from your account [#](payments#withdraw)

To withdraw funds from your account, enter the desired amount, ensuring it does not exceed the available balance. Please note that credit funds cannot be withdrawn from the account. For further details regarding withdrawal terms and conditions, please contact your broker.

Please note that the funds will be withdrawn from the trading account currently active in the platform. To withdraw funds from a different account, switch to it accordingly.

Select your preferred payment method: card, e-wallet, bank transfer, or another option. Each payment method may be supported by multiple payment systems which are provided by companies authorized by your broker. Choose the relevant provider in the "Payment service provider" field. The availability of payment methods and providers is entirely dependent on your broker.

Some systems supporting card payments may require prior [card addition](/en/docs/mt5/client/payments#add_card) for future use: You first add your card to the system, specifying its details, and then use it as a ready-made payment method. This is typically required for fund withdrawals.

![Select a payment method to withdraw funds](/en/docs/mt5/client/img/payments_withdraw.png "Select a payment method to withdraw funds")

Once you've selected your payment method, click "Continue". If you have previously added a card, no further action is necessary. Otherwise, you will need to input additional transaction details either directly on the withdrawal page within the platform or on the selected payment system's page. Follow the instructions provided on this page.

![Specify wallet details to transfer funds](/en/docs/mt5/client/img/payments_withdraw_details.png "Specify wallet details to transfer funds")

Once the transaction is complete, you will be redirected back to the payments section. To ensure a smooth transaction process, refrain from closing the payment page until you receive confirmation of its successful completion.

Some brokers may conduct additional payment checks before withdrawing funds to the selected card/wallet. In such cases, the amount is debited from your trading account immediately. You will see it in the [history section](/en/docs/mt5/client/performing_deals#trade_history). If the transaction fails or is rejected by the broker, the funds will be returned to your account after some time.

![Withdrawal operation](/en/docs/mt5/client/img/payments_trade_history.png "Withdrawal operation")

Track the status of your transactions via the [transaction history](/en/docs/mt5/client/payments#transactions). If you have questions about your payments, please reach out directly to your broker.

## Adding cards [#](payments#add_card)

Due to operational specifics, some payment providers require the prior specification of the card that will be used for payments. If you haven't previously added cards and have never deposited funds (as cards are automatically added during deposits), you may need to add a card before withdrawing funds:

![Adding a card](/en/docs/mt5/client/img/payments_add_card.png "Adding a card")

Select "Add new card", enter your email and click "Add". You will be redirected to the payment system page to input card details. A special operation is performed in the system with a 1 USD authorization charge, which is then immediately released, so no funds are debited from your account. Upon completion, you will be redirected back to the payment section. The card will be displayed in the list as another payment instrument. Select it and proceed with the withdrawal.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When depositing funds, the used card is automatically added to the system. Adding it separately is not required. Simply specify the amount and click "Continue".</span></p></td></tr></tbody></table>

## Saved payment methods [#](payments#saved_methods)

Cards and e-wallets used for payments are stored within the system. This is convenient as you will not need to re-enter all your details for each transaction. Simply select the previously saved payment method and confirm the payment by entering your wallet password or card CVV code.

Saved payment methods are displayed alongside other systems. To delete a method, click the cross symbol next to it.

![Saved card in the list of payment methods](/en/docs/mt5/client/img/payments_saved_card.png "Saved card in the list of payment methods")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The broker does not store all payment details for cards and wallets. Only a limited set of data is saved, which does not allow for payments but solely identifies the payment method within the system.</span></p></td></tr></tbody></table>

## Deposits and withdrawals via bank transfers [#](payments#bank_transfer)

This payment method enables balance transactions on the account by transferring funds via bank details: from the user to the brokerage company for deposits or from the brokerage company to the user for withdrawals. Please note that bank transfers take significantly longer to process compared to payments through electronic systems:

-   Sending and processing incoming transfers is usually done manually by the broker.
-   The transfer then may take several business days depending on the bank.

### Deposit process

To deposit funds, select the corresponding option in the platform's payment section. Then, choose the bank to which you will transfer the funds from the "Payment service provider" field. The available banks depend on your broker.

![Select a bank to deposit funds to your account](/en/docs/mt5/client/img/payments_bank_deposit.png "Select a bank to deposit funds to your account")

Click "Continue," and the system will generate an invoice for you. Check the invoice, and if everything is correct, confirm it. You can then proceed to make the payment through any available method — either directly at your bank or by initiating a request through the banking application.

![Check your invoice ](/en/docs/mt5/client/img/payments_bank_invoice.png "Check your invoice ")

The payment will appear in the [transaction history](/en/docs/mt5/client/payments#transactions) as "Pending". Once the broker receives and processes your transfer, the funds will be credited to your account.

If you notice an error on your invoice, reject it. You can then repeat the process. Rejected transactions are not saved in the transaction history.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">For some payment systems, the transfer process may vary. The system may require inputting some details on the platform side or redirect you to a transfer page through the banking application.</span></p></td></tr></tbody></table>

### Withdrawal process

To withdraw funds, select the corresponding option in the payment section. In the "Payment service provider" field, choose the transfer method.

-   Wire Transfer — for a regular bank transfer using the provided details. Manually processed by the broker.
-   Another option — for transfers through one of the supported electronic systems.

The available methods depend on your broker.

You will see a form where you will need to input your bank details for transferring funds from your trading account.

![Provide your bank account details to transfer funds](/en/docs/mt5/client/img/payments_bank_withdrawal.png "Provide your bank account details to transfer funds")

After filling out the form, a pending payment will appear in the [transaction history](/en/docs/mt5/client/payments#transactions). The withdrawal amount will be debited from your trading account immediately. The broker will process your request and initiate the transfer. Track the transaction status in the transaction history. For any transaction-related queries, please contact your broker directly.

## Deposit and withdrawal links [#](payments#links)

Instead of an internal payment system, the broker may show links to deposit and withdrawal pages on their own website. In this case, the "Payments" section is not visible to you. Instead, you will have the relevant commands in the account menu under "Navigator" and on the trading tab in the Toolbox.

![Fast switch to deposit and withdrawal operations on the broker website](/en/docs/mt5/client/img/deposit_withdrawal.png "Fast switch to deposit and withdrawal operations on the broker website")

This method is less convenient than using the internal payment system but still provides easier access to balance transactions. You do not need to search for these features in the account area of your broker's website.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Deposit/withdrawal operations are only available if the relevant functions are enabled for the trading account on the brokerage side.</span></li><li class="p_tableatten"><span class="f_tableatten">The trading platform does not conduct any deposit/withdrawal operations. The integrated functions redirect the user to the respective web page of the brokerage company.</span></li></ul></td></tr></tbody></table>

[Connect to an Account](/en/docs/mt5/client/authorization)

[Platform Settings](/en/docs/mt5/client/settings)