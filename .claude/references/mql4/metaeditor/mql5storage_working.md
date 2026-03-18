# Working with Storage

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/mql5storage_working

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)Working with Storage

# Working with Storage

The MQL5 Storage (or repository) only works with the MQL5 (or MQL4) folder of the trading platform, and with the special Shared Projects directory, which is used for [group projects](/en/docs/mt5/metaeditor/projects#shared).

All operations with the MQL5 Storage are performed via the context menu of the [Navigator](/en/docs/mt5/metaeditor/navigator) window and through the context menu of the [source code editor](/en/docs/mt5/metaeditor/source_code_windows):

![MQL5 Storage menu](/en/docs/mt5/metaeditor/img/mql5storage_menu.png "MQL5 Storage menu")

Using the menu commands, you can perform the following actions in the MQL5 Storage:

-   [Receive](/en/docs/mt5/metaeditor/mql5storage_working#update) data from Storage;
-   [Commit](/en/docs/mt5/metaeditor/mql5storage_working#commit) to Storage;
-   [Add](/en/docs/mt5/metaeditor/mql5storage_working#add) files/folders to Storage;
-   [Delete](/en/docs/mt5/metaeditor/mql5storage_working#delete) files/folders from Storage;
-   [Cancel](/en/docs/mt5/metaeditor/mql5storage_working#revert) current changes in the local copy of data;
-   View [logs](/en/docs/mt5/metaeditor/mql5storage_working#journal) of data changes in Storage;
-   [View changes](/en/docs/mt5/metaeditor/mql5storage_diff) in the working copy of the file.

## Getting started [#](mql5storage_working#start)

Storage contains the information as a tree of files. When connecting to Storage, a MetaEditor user reads and writes these files. The user always works with a local copy of data and, if necessary, sends changes to Storage.

To begin to work with data in the MQL5 Storage, you must associate a local data folder with the appropriate folder in the repository:

-   If you have just [created a repository](/en/docs/mt5/metaeditor/mql5storage_connect), it is empty. You need to [add](/en/docs/mt5/metaeditor/mql5storage_working#add) a directory to it. After that, an appropriate directory is created for the specified directory in the repository (at the same path relative to the /MQL5 folder). This is a root directory. All operations with files are performed in this directory.
-   If the storage already has some data, download them to a local directory. To do this, click ![Update from Storage](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update from Storage") "Update files from Storage" in the context menu of the root MQL5 (or MQL4) element in the Navigator.

## Versioned data storage

Version control is implemented for directories/files associated with the repository, therefore such directories/files have a version, i.e. a revision number. A revision number corresponds to each data update. Each time you update the directory/file in the repository, the revision number is incremented for this directory/file and for the entire root directory. A revision is a state of the directory/file at a point of time.

The root directories are the MQL5/MQL4 folder and folders of each shared project. Revisions are managed separately for each root directory, so they have individual revision numbers. When you commit changes made to the MQL5 directory, its revision number is increased, while the revision number of projects does not change (unless the projects use shared files from the MQL5 directory).

General operation scheme:

-   When you add a file to the MQL5 storage or extract it from the storage to a local PC, its versions (revision number) on the computer and in the storage will match.
-   The revision numbers of the local file (the working copy) and the appropriate file in the storage are initially equal. This happens if you just added a file or extracted it from the repository.
-   If you change the file and commit changes to the repository, the revision number will increase both locally and in the repository.
-   When you submit changes, it may turn out that the file has already been edited by someone and the revision number in the repository is greater than your local one. In this case, you should extract changes from the repository before sending your own changes. MQL5 Storage will try to [merge changes](/en/docs/mt5/metaeditor/mql5storage_merging) in the repository and your local file. In this case, the revision number of the local file will be set equal to the revision number of the file in the repository.

Each transaction of changes is recorded in the [Storage journal](/en/docs/mt5/metaeditor/mql5storage_working#journal), and later the user can view when, by whom and what files were changed. The user can also update the local data copy [to a selected revision](/en/docs/mt5/metaeditor/mql5storage_working#update_revision) and [revert changes](/en/docs/mt5/metaeditor/mql5storage_working#revert_revision) to a selected revision.

## Adding to Storage [#](mql5storage_working#add)

To add a folder or file to the repository, select it and execute the ![Add File or Folder](/en/docs/mt5/metaeditor/img/mql5storage_add_icon.png "Add File or Folder") Add File or Folder command. This brings up a dialog box showing the list of folders and files to be added.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Files are added locally. To send changes to the repository, execute <img class="help" alt="Commit to Storage" title="Commit to Storage" width="14" height="14" src="/en/docs/mt5/metaeditor/img/mql5storage_commit_icon.png"> Commit to Storage.</span></li></ul><ul><li class="p_tableatten"><span class="f_tableatten">MQL5 Storage only works with the following types of files: mq4, mq5, mqh, cpp, h, bmp, wav, ex4, ex5, tpl and set. Other types of files cannot be added to the repository.</span></li><li class="p_tableatten"><span class="f_tableatten">Files larger than 64 MB cannot be added to the storage.</span></li></ul></td></tr></tbody></table>

![Adding the folder to Storage](/en/docs/mt5/metaeditor/img/mql5storage_adding_folder.png "Adding the folder to Storage")

Tick ​​off the necessary files and folders and click OK.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">The principle of storage operation does not allow to add files without the folder in which they are located. You cannot add a file located in the folder, which is not added to the repository.</span></li><li class="p_tableatten"><span class="f_tableatten">You cannot add individual files to the root directory /MQL4 or /MQL5.</span></li><li class="p_tableatten"><span class="f_tableatten">In the folder associated with the repository, only its child directories can be added. Folders that are lower in the hierarchy cannot be added without their parent folders.</span></li></ul></td></tr></tbody></table>

Added files and folders are marked with ![Added to Storage](/en/docs/mt5/metaeditor/img/mql5storage_add_icon.png "Added to Storage"):

![Added files and folders](/en/docs/mt5/metaeditor/img/mql5storage_added.png "Added files and folders")

Next, these changes should be sent to the repository. Select the added folder/file and execute ![Commit to Storage](/en/docs/mt5/metaeditor/img/mql5storage_commit_icon.png "Commit to Storage")  Commit to Storage.

![Committing to Storage](/en/docs/mt5/metaeditor/img/mql5storage_committing.png "Committing to Storage")

In this dialog, you can also choose the changes that should be sent to the repository. You can add a comment when committing changes. Detailed comments facilitate the analysis of changes in the future.

After committing the current changes in the repository, the corresponding folders and files are marked with ![No changes](/en/docs/mt5/metaeditor/img/mql5storage_nochanges_icon.png "No changes"). This means that the local copy of data does not differ from the one that is in the storage at the time of the last commit/update operation.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">If a folder that corresponds to the one you add already exists in the storage, error "Folder already exists, update it from storage" will appear. For such a folder select <img class="help" alt="Update from Storage" title="Update from Storage" width="14" height="14" src="/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png"> Update from Storage. After that, it will be bound to Storage, and data from the repository will be added to it. Then you can send your changes to the repository using the <img class="help" alt="Commit to Storage" title="Commit to Storage" width="14" height="14" src="/en/docs/mt5/metaeditor/img/mql5storage_commit_icon.png">Commit to Storage command.</span></li><li class="p_tableatten"><span class="f_tableatten">If the file size exceeds 1 MB, selection is automatically removed from it in the commit dialog. Download large files with care to avoid overloading the storage system.</span></li></ul></td></tr></tbody></table>

## Checkout and update from the MQL5 Storage [#](mql5storage_working#checkout)

Primary data extraction is executed when the [storage is activated](/en/docs/mt5/metaeditor/mql5storage_connect) in MetaEditor. Once you execute the ![Activate MQL5 Storage](/en/docs/mt5/metaeditor/img/storage_enable_icon.png "Activate MQL5 Storage") Activate MQL5 Storage command, MetaEditor will check if Storage contains any data.

-   If Storage contains data from the MQL5 (MQL4) directory, these data will be instantly downloaded to the computer.
-   If Storage has available shared projects, these projects will appear in the Shared Projects section. To download project files to a local computer, click ![Update from Storage](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update from Storage") Update from Storage in the context menu of the project.

Further updates can be received from the Storage using the ![Update from Storage](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update from Storage") Update from Storage command in the context menu of files and folders in the Navigator.

If the storage contains folders that do not exist in your local working copy, execute Update from Storage at the MQL5 (or MQL4) root element in the Navigator window. All data from the Storage will be downloaded to the corresponding local folders. The revision number of data will match the revision of data in the storage.

![Updating data](/en/docs/mt5/metaeditor/img/mql5storage_updating.png "Updating data")

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">If a local folder contains data, then during checkout data obtained from the repository will be added to it. New files will be added. For files with matching names and paths it will try to <a href="/en/docs/mt5/metaeditor/mql5storage_merging" class="topiclink">merge data</a>.</span></p></td></tr></tbody></table>

## Updating to revision [#](mql5storage_working#update_revision)

MQL5 Storage stores the entire history of changes committed by users to the storage. Each commit of changes is a new [revision](/en/docs/mt5/metaeditor/mql5storage_working#start) (state of the storage at a particular time). During parallel work of multiple users with data through the storage, you need to periodically receive changes made by other users. ![Update to Revision](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update to Revision") Update to revision allows you to gradually update the local copy of data from the repository.

For example, since the last update of the local copy of data, three new revisions appeared in the storage. You can first upgrade to the first revision, then to the second and to the third one.

To update to a specific revision, select a file or folder and call [the storage log](/en/docs/mt5/metaeditor/mql5storage_working#journal) by clicking ![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log.

![Updating to revision](/en/docs/mt5/metaeditor/img/mql5storage_update_revision.png "Updating to revision")

In the window that opens, select the required revision and run the ![Update to Revision](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update to Revision") Update to Revision command.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">A local copy of data can only be updated to a higher (later) revision.</span></li><li class="p_tableatten"><span class="f_tableatten">Data obtained from the repository are added to the local copy. For files with matching names and paths, it will try to <a href="/en/docs/mt5/metaeditor/mql5storage_merging" class="topiclink">merge data</a>. If files have been added to a revision, they will be added to the local copy. If files have been deleted from a revision, they will be deleted from the local copy.</span></li></ul></td></tr></tbody></table>

## Reverting to revision [#](mql5storage_working#revert_revision)

MQL5 Storage stores the entire history of changes committed by users to the storage. Each commit of changes is a new [revision](/en/docs/mt5/metaeditor/mql5storage_working#start) (state of the storage at a particular time). At any time, you can return to one of the previous states of a file or folder.

To revert to a specific revision, select a file or folder and call [the storage log](/en/docs/mt5/metaeditor/mql5storage_working#journal) by clicking ![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log.

![Reverting to revision](/en/docs/mt5/metaeditor/img/mql5storage_revert_revision.png "Reverting to revision")

In the opened window, select the required revision and click ![Revert to This Revision](/en/docs/mt5/metaeditor/img/mql5storage_revert_revision_icon.png "Revert to This Revision") Revert to This Revision.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">After reverting to the revision, the selected file/folder will fully return to the specified state. You can revert both to earlier and to later revisions.</span></p></td></tr></tbody></table>

## Committing changes to Storage [#](mql5storage_working#commit)

As mentioned earlier, you can work with the data only in their local copies. To transfer local changes to the repository, use the ![Commit to Storage](/en/docs/mt5/metaeditor/img/mql5storage_commit_icon.png "Commit to Storage") Commit to Storage command. Local files and folders that have been changed are marked with an icon ![Changed](/en/docs/mt5/metaeditor/img/mql5storage_changed_icon.png "Changed").

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">Before committing changes, you can <a href="/en/docs/mt5/metaeditor/mql5storage_diff" class="topiclink">view</a> them by selecting a file and selecting <img class="help" alt="Difference of Versions" title="Difference of Versions" width="14" height="16" src="/en/docs/mt5/metaeditor/img/mql5storage_diff_icon.png"> Difference of Versions in the context menu.</span></p></td></tr></tbody></table>

![Committing to Storage](/en/docs/mt5/metaeditor/img/mql5storage_committing.png "Committing to Storage")

In the commit dialog, you can select changed files and folders that should be committed to the repository. You can add a comment when committing changes. Detailed comments facilitated the analysis of changes in the future.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Local changes are of higher priority, in any case they are added to Storage.</span></li><li class="p_tableatten"><span class="f_tableatten">If the revision number in the storage is above the local revision (modified from another source, and local data is not updated from the repository), then you will get an error like "Out of date" when trying to commit the changes. In this case, first execute the <img class="help" alt="Update from Storage" title="Update from Storage" width="14" height="14" src="/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png"> Update from Storage command to <a href="/en/docs/mt5/metaeditor/mql5storage_merging" class="topiclink">merge data</a>, and then select the </span><img class="help" alt="Commit to Storage" title="Commit to Storage" width="14" height="14" src="/en/docs/mt5/metaeditor/img/mql5storage_commit_icon.png"><span class="f_txt"> Commit to Storage.</span></li><li class="p_tableatten"><span class="f_txt">Be careful when updating bmp and wav files. When merged, these files are completely replaced by newer revisions. Thus, during update they may be replaced with files from the repository. To avoid such situations, save copies of these files separately, execute the </span><img class="help" alt="Update from Storage" title="Update from Storage" width="14" height="14" src="/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png"><span class="f_tableatten"> Update from Storage command to increase the number of the local revision, move the previously copied files back and commit changes to Storage.</span></li></ul></td></tr></tbody></table>

## Deleting [#](mql5storage_working#delete)

If you want to delete a file or a folder, use the command ![Delete File or Folder](/en/docs/mt5/metaeditor/img/mql5storage_delete_icon.png "Delete File or Folder") Delete File or Folder. The folder/file will be deleted from the local copy of data. To delete a file or a folder from the repository, commit these changes using the ![Commit to Storage](/en/docs/mt5/metaeditor/img/mql5storage_commit_icon.png "Commit to Storage") Commit to Storage.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><ul><li class="p_tableatten"><span class="f_tableatten">Deletion of a file or folder by the standard <img class="help" alt="Delete" title="Delete" width="13" height="14" src="/en/docs/mt5/metaeditor/img/delete_icon.png"> Delete command of the <a href="/en/docs/mt5/metaeditor/navigator" class="topiclink">Navigator</a> window does not influence the MQL5 Storage. With the next <a href="/en/docs/mt5/metaeditor/mql5storage_working#update" class="topiclink">update</a>, the deleted data will be restored from Storage.</span></li><li class="p_tableatten"><span class="f_tableatten"><a href="/en/docs/mt5/metaeditor/mql5storage_working#start" class="topiclink">The root directory</a> linked to Storage cannot be deleted.</span></li></ul></td></tr></tbody></table>

## Reverting changes [#](mql5storage_working#revert)

If you want to undo the changes made in the current local copy of data, execute the ![Revert Changes](/en/docs/mt5/metaeditor/img/mql5storage_revert_icon.png "Revert Changes") Revert Changes command for a necessary file or folder. The file/folder returns to a state that was saved locally during the previous synchronization with the repository.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you revert changes, the initial local revision is restored, not the current revision in the repository.</span></p></td></tr></tbody></table>

## Storage log [#](mql5storage_working#journal)

Each commit of changes to Storage using the ![Commit to Storage](/en/docs/mt5/metaeditor/img/mql5storage_commit_icon.png "Commit to Storage") Commit to Storage command is saved in the log. The logs help you to easily analyze the history of changes in your projects. To view the change log of a file/folder, select ![Show Storage Log](/en/docs/mt5/metaeditor/img/mql5storage_journal_icon.png "Show Storage Log") Show Storage Log.

![Viewing the log](/en/docs/mt5/metaeditor/img/mql5storage_journal.png "Viewing the log")

The upper part shows a list of changes:

-   Revision — the unique number of the commit;
-   Author — the name of the user (same as the login of the MQL5.community account), who made these changes;
-   Date — date when the changes were committed in the UTC format;
-   Comment — comment to changes.

Using the context menu command ![Update to Revision](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update to Revision") Update to Revision, you can update the local copy of data [to a selected revision](/en/docs/mt5/metaeditor/mql5storage_working#update_revision).

The bottom of the window displays a list of files modified in the selected revision. Icons show the types of changes:

-   ![Added](/en/docs/mt5/metaeditor/img/mql5storage_added_icon.png "Added") — file added;
-   ![Changed](/en/docs/mt5/metaeditor/img/mql5storage_modified_icon.png "Changed") — file changed;
-   ![Deleted](/en/docs/mt5/metaeditor/img/mql5storage_deleted_icon.png "Deleted") — file deleted.

Using the context menu of the list of modified files, you can analyze the changes:

-   ![Compare with Working Copy](/en/docs/mt5/metaeditor/img/mql5storage_compare_working_icon.png "Compare with Working Copy") Compare with Working Copy — compare the selected file with its [working copy](/en/docs/mt5/metaeditor/mql5storage_diff#compare_working).
-   ![Compare with Previous Revision](/en/docs/mt5/metaeditor/img/mql5storage_compare_previous_icon.png "Compare with Previous Revision") Compare with Previous Revision — compare the selected file with its [previous revision](/en/docs/mt5/metaeditor/mql5storage_diff#compare_previous).
-   ![Compare Revisions](/en/docs/mt5/metaeditor/img/mql5storage_compare_revisions_icon.png "Compare Revisions") Compare Revisions — compare [two revisions of a file](/en/docs/mt5/metaeditor/mql5storage_diff#compare_revisions) pre-selecting them at the top of the window.

[Working with Projects](/en/docs/mt4/metaeditor/projects)

[Viewing project history](/en/docs/mt4/metaeditor/mql5storage_diff)