# External Subversion client

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/mql5storage_svn_client

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
        -   [Launch](/en/docs/mt4/metaeditor/open)
        -   [Settings](/en/docs/mt4/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt4/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt4/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt4/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt4/metaeditor/workspace)
        -   [Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)
            -   [Enabling the Storage](/en/docs/mt4/metaeditor/mql5storage_connect)
            -   [Working with Projects](/en/docs/mt4/metaeditor/projects)
            -   [Working with Storage](/en/docs/mt4/metaeditor/mql5storage_working)
            -   [Viewing project history](/en/docs/mt4/metaeditor/mql5storage_diff)
            -   [Merging changes](/en/docs/mt4/metaeditor/mql5storage_merging)
            -   [External Subversion client](/en/docs/mt4/metaeditor/mql5storage_svn_client)
        -   [MQL4/MQL5 Wizard](/en/docs/mt4/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt4/metaeditor/development)
        -   [Working with SQL data bases](/en/docs/mt4/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt4/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt4/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt4/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt4/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt4/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt4/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt4/metaeditor/video_guides)
    -   [WebTerminal](/en/docs/mt4/administrator/web_terminal)
    -   [MultiTerminal](/en/docs/mt4/multiterminal)
    -   [API](/en/docs/mt4/api)
-   [Finteza](/en/docs/finteza)
    -   [CMS Plugins](/en/docs/finteza/plugins)
    -   [Finteza JavaScript Client](/en/docs/finteza/javascript-client)
    -   [Finteza SDK](/en/docs/finteza/sdk)
-   [MQL5.community](/en/docs/community)

window.fz('show', 'fotcgrjxafakglznxzxkinbtytrjklzamk');

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)External Subversion client

# External Subversion client

The MQL5 Storage is based on a free centralized version control system [Subversion 1.7](https://subversion.apache.org "Official site of Subversion 1.7"). You can work with the storage not only from MetaEditor, but also via any external client that supports [Subversion 1.7](https://subversion.apache.org "Official site of Subversion 1.7"). For example, [Tortoise SVN](https://tortoisesvn.net/ "Official site of Tortoise SVN").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">More info on Subversion is available in a <a href="https://svnbook.red-bean.com/en/1.2/svn-book.html" target="_blank" class="weblink" title="The book about Subversion">special book</a>.</span></p></td></tr></tbody></table>

## Example of connecting to the storage via Tortoise SVN

Install the latest version of Tortoise SVN. Create any folder to connect to [previously generated](/en/docs/mt5/metaeditor/mql5storage_connect) MQL5 Storage. This folder will be synchronized with the storage. Next, open the folder's context menu and click SVN Checkout.

![SVN Checkout](/en/docs/mt5/metaeditor/img/mql5storage_tortoise_menu.png "SVN Checkout")

Enter the storage address in the "URL of repository" field:

-   If you want to extract data from a personal folder: https://storage.mql5.io/repos/MQL5.\[login\], where \[login\] is a login of your account on [MQL5.community](https://www.mql5.com/en "MQL5.community")
-   If you want to extract a shared project: https://storage.mql5.io/repos/\[project name\], where \[project name\] is a [shared project](/en/docs/mt5/metaeditor/projects#shared) name.

Click OK. If you see an error validating the certificate, with which connection to the repository is encrypted, agree to accept the certificate permanently (Accept certificate permanently). This is a trusted certificate issued by Thawte Inc.

![Accept certificate permanently](/en/docs/mt5/metaeditor/img/mql5storage_accept_certificate.png "Accept certificate permanently")

Next, specify the login and password of your MQL5.community account:

![Authentication](/en/docs/mt5/metaeditor/img/mql5storage_authentication.png "Authentication")

After successful authentication, the data is downloaded from the repository to a local folder. Now you can work with the repository via Tortoise SVN.

[Merging changes](/en/docs/mt4/metaeditor/mql5storage_merging)

[MQL4/MQL5 Wizard](/en/docs/mt4/metaeditor/mql5_wizard)