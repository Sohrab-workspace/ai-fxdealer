# Viewing project history

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/mql5storage_diff

-   [MetaTrader 5](/en/docs/mt5)
    -   [Platform](/en/docs/mt5/platform)
    -   [Administrator](/en/docs/mt5/platform/administrator)
    -   [Manager](/en/docs/mt5/manager)
    -   [Client terminal](/en/docs/mt5/client)
    -   [MetaEditor](/en/docs/mt5/metaeditor)
        -   [Launch](/en/docs/mt5/metaeditor/open)
        -   [Settings](/en/docs/mt5/metaeditor/settings)
        -   [Integration with other IDEs](/en/docs/mt5/metaeditor/integration_ide)
        -   [Main menu](/en/docs/mt5/metaeditor/main_menu)
        -   [Toolbars](/en/docs/mt5/metaeditor/toolbar)
        -   [Workspace](/en/docs/mt5/metaeditor/workspace)
        -   [Projects and MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage)
            -   [Enabling the Storage](/en/docs/mt5/metaeditor/mql5storage_connect)
            -   [Working with Projects](/en/docs/mt5/metaeditor/projects)
            -   [Working with Storage](/en/docs/mt5/metaeditor/mql5storage_working)
            -   [Viewing project history](/en/docs/mt5/metaeditor/mql5storage_diff)
            -   [Merging changes](/en/docs/mt5/metaeditor/mql5storage_merging)
            -   [External Subversion client](/en/docs/mt5/metaeditor/mql5storage_svn_client)
        -   [MQL4/MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard)
        -   [Developing programs](/en/docs/mt5/metaeditor/development)
        -   [Working with SQL data bases](/en/docs/mt5/metaeditor/database)
        -   [Working with machine learning models](/en/docs/mt5/metaeditor/machine_learning)
        -   [Example of developing a program](/en/docs/mt5/metaeditor/project_example)
        -   [MetaEditor environment folders](/en/docs/mt5/metaeditor/structure)
        -   [MQL5.community: Community of Traders](/en/docs/mt5/metaeditor/mql5community)
        -   [Built-in help](/en/docs/mt5/metaeditor/mql5_help)
        -   [Articles on the development of trading applications](/en/docs/mt5/metaeditor/articles)
        -   [Trading platform video guides](/en/docs/mt5/metaeditor/video_guides)
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

[MetaTrader 5](/en/docs/mt5)[MetaEditor](/en/docs/mt5/metaeditor)[Projects and MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage)Viewing project history

# Viewing project history

MQL5 Storage applies the version control system. This means that any modification of files in a shared or personal project in the storage can be checked and, if necessary, canceled.

## Comparing the working copy and the latest revision [#](mql5storage_diff#diff)

Before you submit changes made to the local copy of the file, you can view and check them. MetaEditor compares the current state of the file with the state at the time of the last synchronization of the file with the data storage (the local file revision).

To view changes to a file, select it in the "Navigator" window, or open it in the code editor, and then click ![Difference of Versions](/en/docs/mt5/metaeditor/img/mql5storage_diff_icon.png "Difference of Versions") Difference of Versions [in the context menu](/en/docs/mt5/metaeditor/mql5storage_working).

## Comparing the selected revision with the working copy [#](mql5storage_diff#compare_working)

The MetaEditor allows you to compare any version of a file with the current working copy. You can see all the accumulated changes to the file for the selected period.

To compare a file, select it and open [the storage log](/en/docs/mt5/metaeditor/mql5storage_working#journal) by executing the context menu command ![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log. Next, select the revision for comparison.

![Comparing the files](/en/docs/mt5/metaeditor/img/mql5storage_compare.png "Comparing the files")

Select the required file at the bottom of the list of files that have changed in the specified revision, and click ![Compare with Working Copy](/en/docs/mt5/metaeditor/img/mql5storage_compare_working_icon.png "Compare with Working Copy") Compare with Working Copy.

## Comparing with the previous revision [#](mql5storage_diff#compare_previous)

When searching for the causes of errors, you often need to conduct a stepwise analysis of the changes. The MetaEditor allows you to compare files of any revisions with their previous state. So you can keep track of what changes were made in each of the revisions.

For such comparison, select a file and open [the storage log](/en/docs/mt5/metaeditor/mql5storage_working#journal) by executing the context menu command ![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log. Next, select the revision for comparison. Select the required file at the bottom of the list of files that have changed in the specified revision, and click ![Compare with Previous Revision](/en/docs/mt5/metaeditor/img/mql5storage_compare_previous_icon.png "Compare with Previous Revision") Compare with Previous Revision.

## Comparing two revisions [#](mql5storage_diff#compare_revisions)

MetaEditor allows comparing two arbitrary file revisions. So you can see the changes in the file accumulated over a period of time.

To do this, select the file and open [the storage log](/en/docs/mt5/metaeditor/mql5storage_working#journal) by using the ![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log context menu command. Next, click on two revisions, while holding Ctrl. The list of files that have changed in both revisions appears at the bottom of the window. Select the desired file and click ![Compare Revisions](/en/docs/mt5/metaeditor/img/mql5storage_compare_revisions_icon.png "Compare Revisions") Compare Revisions.

## Window for viewing changes [#](mql5storage_diff#diff_window)

The window opens when you run one of the commands for comparing files described above.

![Changes](/en/docs/mt5/metaeditor/img/mql5storage_diff.png "Changes")

The left part of the window displays an earlier revision of a file, while the right one — a recent revision. The color of the lines background shows the nature of changes:

-   Lines changed in a later version of the file are shown in green.
-   Lines added in the later file version are displayed in light blue.
-   Lines deleted from the later file version are displayed in red.

At the bottom of the window you can see a comparison of the selected line in the earlier and recent revisions.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If for any reason, file comparison failed, the <img class="help" alt="Unable to compare files" title="Unable to compare files" width="16" height="16" src="/en/docs/mt5/metaeditor/img/mql5storage_diff_failed_icon.png"> icon is displayed in the right upper corner. In case of successful comparison, the <img class="help" alt="Files successfully compared" title="Files successfully compared" width="16" height="16" src="/en/docs/mt5/metaeditor/img/mql5storage_diff_success_icon.png"> icon is displayed.</span></p></td></tr></tbody></table>

## Toolbar [#](mql5storage_diff#toolbar)

The following commands are available in the window toolbar:

-   ![Open files to diff](/en/docs/mt5/metaeditor/img/open_icon.png "Open files to diff") — select any two files for [comparison](/en/docs/mt5/metaeditor/mql5storage_diff#compare_files).
-   ![Update files](/en/docs/mt5/metaeditor/img/refresh_icon.png "Update files") — update files in the changes window. Run this command if you edit the file while comparing the changes.
-   ![Go to previous diff](/en/docs/mt5/metaeditor/img/arrowup_icon.png "Go to previous diff") — go to the previous change in the file.
-   ![Go to next diff](/en/docs/mt5/metaeditor/img/arrowdwon_icon.png "Go to next diff") — go to the next change in the file.

## Comparing two files [#](mql5storage_diff#compare_files)

In addition to viewing the changes in the working copy of a file, you can compare any two files. Click ![Open files to diff](/en/docs/mt5/metaeditor/img/open_icon.png "Open files to diff") on the toolbar.

![Choosing files to compare](/en/docs/mt5/metaeditor/img/mql5storage_diff_files.png "Choosing files to compare")

Use the "Browse" buttons to select two files for comparison in the "Base file" and "Their file" fields. Then click OK.

[Working with Storage](/en/docs/mt5/metaeditor/mql5storage_working)

[Merging changes](/en/docs/mt5/metaeditor/mql5storage_merging)