# Merging changes

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/mql5storage_merging

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)Merging changes

# Merging changes

When working on a [shared project](/en/docs/mt5/metaeditor/projects#shared) in a team, it may happen that the same files are edited by several users simultaneously. To save such changes from being overwritten, MetaEditor features the function for merging data.

If you try to save a file that has already been changed by someone to the storage, MetaEditor prompts you to get the latest changes first. When the changes are received, an attempt is made to merge the data: changes from the storage are applied to the local data copy and an attempt is made to save the current local changes.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Merging is applied only to text files with the source code (mq4, mq5, mqh, cpp and h) in ANSI format. Bmp and wav files are always completely replaced by newer versions.</span></li><li class="p_tableatten"><span class="f_tableatten">Source code files are compared line by line. When conflicts arise (for example, the same line is changed in the local file and in the corresponding file in the repository), the merging algorithm aims to maximize the preservation of local changes.</span></li></ul></td></tr></tbody></table>

## Sample merging

Let's consider a typical case of merging two files. As mentioned above, during merging, source code files are compared line by line. If a file in the storage contains the lines that are not present in the local file, these lines are added. Consider the following example of merging two files:

![Example of merging two files](/en/docs/mt5/metaeditor/img/merge_example_1.png "Example of merging two files")

After you click ![Update from Storage](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update from Storage") Update from Storage, the local files remain unchanged, since local changes are of higher priority. If the storage file had contained the new line "x=0;", it would have been added, while "return(true);" line would have remained unchanged:

![Example of merging two files](/en/docs/mt5/metaeditor/img/merge_example_2.png "Example of merging two files")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The main principle of merging is the higher priority of local data. The algorithm seeks to maximize the preservation of local changes.</span></li><li class="p_tableatten"><span class="f_tableatten">There are many types of conflicts during merging. In this section, just one of the most common situations was considered. The merging algorithm is complex and provides a comprehensive approach in the analysis files. More information about the merger can be found in <a href="https://svnbook.red-bean.com/en/1.2/svn-book.html" target="_blank" class="weblink" title="The book about Subversion">a book on Subversion</a>.</span></li></ul></td></tr></tbody></table>

[Viewing project history](/en/docs/mt4/metaeditor/mql5storage_diff)

[External Subversion client](/en/docs/mt4/metaeditor/mql5storage_svn_client)