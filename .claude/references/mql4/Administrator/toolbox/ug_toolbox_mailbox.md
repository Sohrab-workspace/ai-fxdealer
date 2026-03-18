# Mailbox

> Source: https://support.metaquotes.net/en/docs/mt4/administrator/toolbox/ug_toolbox_mailbox

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
        -   [Getting Started](/en/docs/mt4/administrator/getting_started)
        -   [Terminal Settings](/en/docs/mt4/administrator/settings)
        -   [Managed Servers](/en/docs/mt4/administrator/administered_servers)
        -   [Server Administration Commands](/en/docs/mt4/administrator/server_commands)
        -   [Administration](/en/docs/mt4/administrator/administration)
        -   [Toolbox](/en/docs/mt4/administrator/toolbox)
            -   [Monitor](/en/docs/mt4/administrator/toolbox/ug_toolbox_monitor)
            -   [Mailbox](/en/docs/mt4/administrator/toolbox/ug_toolbox_mailbox)
            -   [Journal](/en/docs/mt4/administrator/toolbox/ug_toolbox_journal)
            -   [Support](/en/docs/mt4/administrator/toolbox/ug_toolbox_support)
            -   [Articles](/en/docs/mt4/administrator/toolbox/toolbox_articles)
        -   [Articles](/en/docs/mt4/administrator/articles)
        -   [Additional Features](/en/docs/mt4/administrator/additional)
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

[MetaTrader 4](/en/docs/mt4)[Administrator](/en/docs/mt4/administrator)[Toolbox](/en/docs/mt4/administrator/toolbox)Mailbox

# Mailbox

Online trading system MetaTrader 4 includes internal mailbox allowing clients and managers to exchange messages. The "Mailbox" tab of the "Toolbox" window contains the list of income messages.

![Mailbox](/en/docs/mt4/administrator/img/tb_mail.png "Mailbox")

The received messages are saved in the subdirectory of /mailbox directory in which the administrator terminal is installed. When a new message incomes the event set for the mail receiving will sound, and a record about the income message will be done in the terminal journal.

The following commands are available in the context menu:

-   Create — write and send a new message in internal mailbox;
-   View — open a message to view it;
-   Delete — delete the message from the list and from HDD;
-   Auto Arrange — automatic arrangement of column sizes when the window size is changed;
-   Grid — show/hide the grid to separate columns.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The command of creating a mail is active only if the mailbox name is specified in the <a href="/en/docs/mt4/administrator/administration/ug_managers" class="topiclink">settings</a> of the manager's account. The right to use the internal mail should also be enabled for the manager's account.</span></p></td></tr></tbody></table>

## New Message (Mail window) [#](ug_toolbox_mailbox#mail)

The "Mail" window allows to write and send a new message in internal mailbox. It is necessary to input the account number(s) of the recipient(s), separated by commas, or the range of accounts, separated by hyphen, the subject of the message, and its text. Mail-templates are located in "templates\\mails" subfolder as plain text files or html files.

![New Mail](/en/docs/mt4/administrator/img/new_mail.png "New Mail")

When setting up the messages to be sent, it is possible to use a set of macros - key words that will be replaced with the user's record data when composing the message:

<table class="table" cellspacing="0" cellpadding="5" border="1"><thead><tr class="table"><th class="table" style="vertical-align:middle; width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; font-weight: bold; color: #565656;">Macro</span></p></th><th class="table" style="vertical-align:middle;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; font-weight: bold; color: #565656;">Description</span></p></th></tr></thead><tbody><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#LOGIN#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Account login</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#USERNAME#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">User name</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#BALANCE#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Account balance</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#CREDIT#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Account credit</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#EQUITY#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Account equity</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#MARGIN#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Margin requirements</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#MARGIN_LEVEL#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Margin level</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#MARGIN_SHORT#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Margin shortage</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#MARGIN_CALL_LEVEL#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Margin call level for the user group to which the recipient belongs (MT Administrator-&gt;Groups-&gt;Margins-&gt;Margin Call level)</span></p></td></tr><tr class="table"><td class="table" style="width:17%;"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">#SIGNATURE#</span></p></td><td class="table"><p><span style="font-size: 9pt; font-family: Tahoma,Geneva,Verdana,sans-serif; color: #565656;">Company signature from settings of the user group to which the recipient belongs (MT Administrator-&gt;Groups-&gt;Reports-&gt;Signature)</span></p></td></tr></tbody></table>

The "Send" command will send the message to receivers.

[Monitor](/en/docs/mt4/administrator/toolbox/ug_toolbox_monitor)

[Journal](/en/docs/mt4/administrator/toolbox/ug_toolbox_journal)