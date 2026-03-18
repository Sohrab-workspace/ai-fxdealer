# Connecting the Storage

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/mql5storage/mql5storage_connect

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

# Connecting the Storage

To start working with the MQL5 Storage, you should activate it in MetaEditor using your [MQL5.community](https://www.mql5.com/ "MQL5.community")account.

Open the context menu of the [Navigator](/en/docs/mt5/metaeditor/interface/navigator) window and execute the "![Activate MQL5 Storage](/en/docs/mt5/metaeditor/img/storage_enable_icon.png "Activate MQL5 Storage") Activate MQL5 Storage" command. If you have specified your MQL5.community login and password in the [MetaEditor settings](/en/docs/mt5/metaeditor/settings/settings_mql5community) earlier, the storage will be activated immediately. Otherwise, you will need to specify account details:

![MQL5.community account](/en/docs/mt5/metaeditor/img/mql5_account_specify.png "MQL5.community account")

If you have never used the storage before, a repository will be created for your MQL5 account at the time of activation. If you previously worked with the storage and it stores some data, MetaEditor will extract all data from the storage to your computer (to the current copy of MetaEditor) immediately upon activation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">If you do not have an MQL5.community account, please <a href="https://www.mql5.com/ru/auth_register" target="_blank" class="weblink" title="Register at MQL5.community">register</a> and get access to unique opportunities. You will also receive a bonus of 2 credits which you can use to test programs through <a href="https://cloud.mql5.com/" target="_blank" class="weblink" title="MQL5 Cloud Network">the MQL5 Cloud Network</a>.</span></p></td></tr></tbody></table>

## Activating Storage via MQL5.community

You can also activate the storage from the "Storage" section of your profile on [MQL5.community](https://www.mql5.com/ "MQL5.community"):

![Activating the MQL5 Storage from the MQL5.community user profile](/en/docs/mt5/metaeditor/img/mql5_storage_activate_profile.png "Activating the MQL5 Storage from the MQL5.community user profile")

Enable the "Use MQL5 Storage" option. After that a private repository will be created for you. It will be only available to your MQL5.community account. After activating the storage on the site, specify your MQL5.community account details in [MetaEditor settings](/en/docs/mt5/metaeditor/settings/settings_mql5community).

The contents of the repository can be viewed in the browser using the following link: [https://storage.mql5.io](https://storage.mql5.io). The browser will require from you to enter your MQL5.community account login and password.

![Viewing a storage in the browser](/en/docs/mt5/metaeditor/img/mql5_storage_browser.png "Viewing a storage in the browser")

Here you can view and download files stored currently in the Storage. The top level features your [shared projects](/en/docs/mt5/metaeditor/projects#shared) and an MQL5.\[login\] folder, in which data from your MQL5 working directory of MetaEditor are saved.