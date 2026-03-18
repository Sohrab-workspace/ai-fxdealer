# Mailbox

> Source: https://support.metaquotes.net/en/docs/mt4/manager/news_mail/ug_mail

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
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
        -   [Getting Started](/en/docs/mt4/manager/getting_started)
        -   [Client Accounts](/en/docs/mt4/manager/client_accounts)
        -   [Mail, News and Support](/en/docs/mt4/manager/news_mail)
            -   [Mailbox](/en/docs/mt4/manager/news_mail/ug_mail)
            -   [News](/en/docs/mt4/manager/news_mail/ug_news)
            -   [Support](/en/docs/mt4/manager/news_mail/ug_toolbox_support)
        -   [Request Processing](/en/docs/mt4/manager/request_processing)
        -   [Reports and Journal](/en/docs/mt4/manager/reports_journal)
        -   [Risk Management](/en/docs/mt4/manager/risk_management)
        -   [User Interface](/en/docs/mt4/manager/user_interface)
        -   [Articles](/en/docs/mt4/manager/articles)
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

[MetaTrader 4](/en/docs/mt4)[Manager](/en/docs/mt4/manager)[Mail, News and Support](/en/docs/mt4/manager/news_mail)Mailbox

# Mailbox

Online trading system MetaTrader 4 includes internal mailbox allowing clients and managers to exchange messages. The "Mailbox" tab of the "Toolbox" window contains the list of income messages.

![Mailbox](/en/docs/mt4/manager/img/tb_mail.png "Mailbox")

The received messages are saved in the subdirectory of /mailbox directory in which the manager terminal is installed. When a new message incomes the event set for the mail receiving will sound, and a record about the income message will be done in the terminal journal.

The following commands are available in the context menu:

-   Create — write and send a new message in internal mailbox;
-   View — open a message to view it;
-   Delete — delete the message from the list and from HDD;
-   Auto Arrange — automatic arrangement of column sizes when the window size is changed;
-   Grid — show/hide the grid to separate columns.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Feature: click onto field From in the message window and you can quickly call the window of the sender account details.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">The command of email creation is active only if the mailbox name is specified in the manager account settings, and if the manager is permitted to send emails. Appropriate account settings can be made by the platform administrator.</span></li></ul></td></tr></tbody></table>

## New Message (Mail window) [#](ug_mail#mail)

The "Mail" window allows to write and send a new message in internal mailbox. Mail-templates are located in "templates\\mails" subfolder as plain text files or html files. If storage of personal details is allowed in the [server settings](/en/docs/mt4/manager/getting_started/ug_setup#server), the messages sent are stored in a subdirectory "mailbox\\sent" of the directory where the Manager temrinal is installed. To create other messages, one can use the previously messages as templates.

![New Mail](/en/docs/mt4/manager/img/new_mail.png "New Mail")

The message recipients can be a list of accounts separated by semicolons, accounts ranges separated by hyphens, lists of groups, countries, or cities. The minimal and/or the maximal build of the terminal can be specified as the message target, too. A message will be sent to users that connect to the server using the terminal of the specified build:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="vertical-align:middle; width:91px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Prefix</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable">&nbsp;</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">list or range of accounts, for example: "2;4;6;8;10-20;55"</span></p></td></tr><tr class="table"><td class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable">group:</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">list of groups, for example: "group: contest,demo*"</span></p></td></tr><tr class="table"><td class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable">country:</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">list of countries, for example: "country: Russia,USA"</span></p></td></tr><tr class="table"><td class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable">city:</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">list of cities, for example: "city: Moscow,Kiev"</span></p></td></tr><tr class="table"><td class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable">build_min:</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">the minimal terminal build, for example: "build_min: 200"</span></p></td></tr><tr class="table"><td class="table" style="width:91px;"><p class="p_fortable"><span class="f_fortable">build_max:</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">the maximal terminal build, for example: "build_max: 201"</span></p></td></tr></tbody></table>

For example, if the line of "2;4-6;country: USA;city: Moscow;build\_min: 200" is given as message recipients, the message will be sent to accounts '2', '4', '5', '6', to accounts from the USA, and to accounts from Moscow if they all connect to the server through the terminal, the build number of which is equal to or larger than 200.

When setting up the messages to be sent, it is possible to use a set of macros - key words that will be replaced with the user's record data at composing of the message:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="vertical-align:middle; width:152px;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Macro</span></p></th><th class="table" style="vertical-align:middle;"><p class="p_fortable"><span class="f_fortable" style="font-weight: bold;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#LOGIN#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Account login</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#USERNAME#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">User name</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#BALANCE#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Account balance</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#CREDIT#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Account credit</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#EQUITY#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Account equity</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#MARGIN#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Margin requirements</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#MARGIN_LEVEL#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Margin level</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#MARGIN_SHORT#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Margin shortage</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#MARGIN_CALL_LEVEL#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Margin call level for the user group to which the recipient belongs (MT Administrator-&gt;Groups-&gt;Margins-&gt;Margin Call level)</span></p></td></tr><tr class="table"><td class="table" style="width:152px;"><p class="p_fortable"><span class="f_fortable">#SIGNATURE#</span></p></td><td class="table"><p class="p_fortable"><span class="f_fortable">Company signature from settings of the user group to which the recipient belongs (MT Administrator-&gt;Groups-&gt;Reports-&gt;Signature)</span></p></td></tr></tbody></table>

The "Send" command will send the message to recipients.

[Mail, News and Support](/en/docs/mt4/manager/news_mail)

[News](/en/docs/mt4/manager/news_mail/ug_news)