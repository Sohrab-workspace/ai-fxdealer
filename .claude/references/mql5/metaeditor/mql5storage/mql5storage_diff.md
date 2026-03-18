# Viewing Changes

> Source: https://support.metaquotes.net/en/docs/mt5/metaeditor/mql5storage/mql5storage_diff

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

# Viewing Changes

MetaEditor provides a wide range of tools for analyzing changes made to the files with which you work through the storage.

## Comparing the Working Copy and the Latest Revision

Before you submit changes made to the local copy of the file, you can view and check them. The MetaEditor compares the current state of the file with the state at the time of the last synchronization of the file with the data storage (the local file revision).

To view changes to a file, select it in the "Navigator" window, or open it in the code editor, and then select "![Changes](/en/docs/mt5/metaeditor/img/mql5storage_diff_icon.png "Changes") Difference of Versions" [in the context menu](/en/docs/mt5/metaeditor/mql5storage/mql5storage_working).

## Comparing the Selected Revision with the Working Copy

The MetaEditor allows you to compare any version of a file with the current working copy. You can see all the accumulated changes to the file for the selected period.

To compare a file, select it and open [the storage log](/en/docs/mt5/metaeditor/mql5storage/mql5storage_working#journal) by executing the context menu command "![Show log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show log") Show Storage Log". Next, select the revision for comparison.

![File comparison](/en/docs/mt5/metaeditor/img/mql5storage_compare.png "File comparison")

Select the required file at the bottom of the list of files that have changed in the specified revision, and click "![Compare with Working Copy](/en/docs/mt5/metaeditor/img/mql5storage_compare_working_icon.png "Compare with Working Copy") Compare with Working Copy".

## Comparing with the Previous Revision

When searching for the causes of errors, you often need to conduct a stepwise analysis of the changes. The MetaEditor allows you to compare files of any revisions with their previous state. So you can keep track of what changes were made in each of the revisions.

For such comparison, select a file and open [the storage log](/en/docs/mt5/metaeditor/mql5storage/mql5storage_working#journal) by executing the context menu command "![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log". Next, select the revision for comparison. Select the required file at the bottom of the list of files that have changed in the specified revision, and click "![Compare with Previous Revision](/en/docs/mt5/metaeditor/img/mql5storage_compare_previous_icon.png "Compare with Previous Revision") Compare with Previous Revision".

## Comparing Two Revisions

Another tool for viewing differences between files is the comparison of any two revisions of a file. So you can see the changes in the file accumulated over a period of time.

For such comparison, select a file and open [the storage log](/en/docs/mt5/metaeditor/mql5storage/mql5storage_working#journal) by executing the context menu command "![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log". Next, select the two revisions by holding down the Ctrl key and clicking on them with the left mouse button. The list of files that have changed in both revisions appears on at the bottom of the window. Select the desired file and click "![Compare Revisions](/en/docs/mt5/metaeditor/img/mql5storage_compare_revisions_icon.png "Compare Revisions") Compare Revisions".

## The Window of Changes

This window opens when you run one of the commands for comparing files described above.

![Changes](/en/docs/mt5/metaeditor/img/mql5storage_diff.png "Changes")

The left part of the window shows the earlier revision of the file, the right part shows the later version of the file. The character of changes is displayed using the background color of rows:

-   Lines changed in the later version of the file are shown in green.
-   Lines added in the later version of the file are shown in blue.
-   Lines deleted from the later version of the file are shown in red.

At the bottom of the window you can see a comparison of the selected row in the local revision and in the current working copy.

<table class="attentable" cellspacing="0" cellpadding="8" border="1" style="background-color:#fbfbec; border:solid thin #e2e2e2; border-spacing:0px;"><tbody><tr style="text-align:left;vertical-align:top;"><td style="vertical-align:top; padding:8px; border:none"><p class="p_tableatten"><span class="f_tableatten">If for any reason, file comparison failed, in the right upper corner the icon <img class="help" alt="Unable to compare files" title="Unable to compare files" width="16" height="16" src="/en/docs/mt5/metaeditor/img/mql5storage_diff_failed_icon.png"> appears. In case of successful comparison, icon <img class="help" alt="Files successfully compared" title="Files successfully compared" width="16" height="16" src="/en/docs/mt5/metaeditor/img/mql5storage_diff_success_icon.png"> is shown.</span></p></td></tr></tbody></table>

## Toolbar

The following commands are available in the window toolbar:

-   ![Open files to diff](/en/docs/mt5/metaeditor/img/open_icon.png "Open files to diff") — select any two files for [comparison](/en/docs/mt5/metaeditor/mql5storage/mql5storage_diff#compare_files).
-   ![Update files](/en/docs/mt5/metaeditor/img/refresh_icon.png "Update files") — update files in the changes window. Run this command if you edit the file while comparing the changes.
-   ![Go to previous diff](/en/docs/mt5/metaeditor/img/arrowup_icon.png "Go to previous diff") — go to the previous change in the file.
-   ![Go to next diff](/en/docs/mt5/metaeditor/img/arrowdwon_icon.png "Go to next diff") — go to the next change in the file.

## Comparing Two Files

In addition to viewing the changes in the working copy of a file, you can compare any two files. Click ![Open files to diff](/en/docs/mt5/metaeditor/img/open_icon.png "Open files to diff") on the toolbar.

![Choosing files to compare](/en/docs/mt5/metaeditor/img/mql5storage_diff_files.png "Choosing files to compare")

Use the "Browse" buttons to select two files for comparison in the fields "Base file" and "Their file". Then click "OK."