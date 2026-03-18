# Creating and working with a project

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/projects

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)[Projects and MQL5 Storage](/en/docs/mt4/metaeditor/mql5storage)Working with Projects

# Creating and working with a project

MetaEditor provides convenient functionality for working with large projects, allowing users to combine files into a single structure, manage project settings and develop applications in teams via the online [MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage) repository with version control.

## What is a project?

A project is a separate file with the MQPROJ extension, which stores program settings, compilation parameters and information about all files used in the project. A separate tab in the Navigator is provided for work convenience within the project. All files, such as include, resource, header and other files are arranged into categories on this tab.

![Project structure and settings](/en/docs/mt5/metaeditor/img/project.png "Project structure and settings")

## Creating a project [#](projects#create)

Creation of a new project is as easy as the creation of a normal MQL5 program. Click New Project and select the type of the desired program in the [MQL5 Wizard](/en/docs/mt5/metaeditor/mql5_wizard):

![Creating a new project](/en/docs/mt5/metaeditor/img/project_new.png "Creating a new project")

Then complete standard MQL5 Wizard steps: set the type, name and properties of the desired program, as well as select appropriate event handlers.

Also the Wizard allows the creation of empty projects. This is a useful feature for non-standard development projects with specific file structures for which the default templates are not suitable. An empty settings file "mqproj" is created in this case. Source code files should be created manually.

## Creating a project based on an MQ5 file [#](projects#create_source)

If you already have developments in the form of MQ5 files, you can easily transform them to a project. Select a file and click ![New Project from Source](/en/docs/mt5/metaeditor/img/project_from_source_icon.png "New Project from Source") New Project from Source in the file context menu:

![Creating a new project based on the source file](/en/docs/mt5/metaeditor/img/project_from_source.png "Creating a new project based on the source file")

In the directory where the selected file is located, a new project file with the same name and the mqproj extension will be created. The main program properties specified in the source code via #property will be automatically added to the project, including the name, copyright, version, link to the developer's site and program description. All files included in the source code through the #include directive will be added to the Dependencies section of the project.

## Project properties [#](projects#properties)

Main project settings can be accessed from a separate dialog box instead of editing the source code as it is normally done in separate MQ5 files. To open project settings click ![Project properties](/en/docs/mt5/metaeditor/img/project_properties_icon.png "Project properties") Properties in the project context menu. The following project settings are available:

-   Platform means the platform version, for which the project is developed, i.e. MetaTrader 4 or MetaTrader 5.
-   Program type: Expert Advisor, Indicator, Script or Library.
-   Copyright shows copyright information similar to "#property copyright ..." in the source code.
-   Link shows the link to a developer's site similar to "#property link ..." in the source code.
-   Version: specifying the version of the program similar to "#property version ..." in the source code.
-   Icon: the icon of the program similar to "#property icon ..." in the source code.
-   Description: program description similar to "#property description ..." in the source code.
-   Enable additional optimization: applications with the optimization disabled are compiled faster, but execute more slowly.
-   Check floating point dividers: applications with the check disabled work a little faster, because the zero divide error is not checked during code execution.
-   Use optimization cache — during optimization, the strategy tester saves results of all performed passes in cache. Results are saved for each set of inputs. This allows the use of ready results during re-optimization with the same parameters, without spending time on recalculation.  
    But in some tasks (for example, in math calculations), it may be necessary to carry out calculations regardless of the availability of previous results. In this case you should disable the "Use optimization cache option" in the project. All test results will still be saved in the cache and thus you can view data on performed passes in the strategy tester report.
-   Calculate indicator on every tick in tester — this option is only available for indicator projects. It forcibly enables indicator calculation at each tick when running in the strategy tester. The option only applies to the operation in the Strategy Tester. In the platform, indicators are always calculated at each incoming tick.  
    When you test Expert Advisors using indicators, the Strategy Tester calculates indicator values only when their data are accessed, i.e. when indicator buffer values are requested. This provides significant acceleration during testing and optimization, if the Expert Advisor does not need indicator values at each tick. Enable this option, if the indicator needs to be calculated at each tick.  
    Also, indicators in the Strategy tester are calculated at each tick in the following cases:

-   when testing in the visual mode
-   if the indicator contains functions EventChartCustom, OnChartEvent, OnTimer
-   if the indicator was created using the compiler build below 1916

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">The set of program properties in the project file is given a higher priority, than properties specified in the program code. If properties are specified both in the project and in the source file, properties from the project will be used.</span></p></td></tr></tbody></table>

## Adding and removing files from a project [#](projects#add_delete_files)

All files used in the source code are added to the project navigator automatically. For example, if you include a new MQH file using the #include directive, it will automatically appear in the Dependencies section of the navigator. Used header files are added to the Headers section; images, sounds and other MQL programs used in the project as resources (via the #resource directive) are added to the Resources section.

MQ5 files with the source code are displayed in the Sources section. Other files, such as set files for testing and chart templates, can be added to the "Settings and files" section.

Use context menu commands to add existing files to a project or to delete files from it. Be careful when deleting files, since you can remove a file from the project (remove the binding) or completely delete it from the hard disk:

![Adding and removing the files from the project](/en/docs/mt5/metaeditor/img/project_add_delete_files.png "Adding and removing the files from the project")

The "Add existing folder" command enables a batch addition of all supported files from the selected directory into the project.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">A file added to the project manually is not included to the program code and is not copied to the project directory. The file is only linked to the project to be displayed in its navigator.</span></p></td></tr></tbody></table>

## Compiling a project [#](projects#compile)

To compile an executable EX5 file, open the project or the main MQ5 file of the program, and then run the compiler command (F7). The resulting executable file will be created in the same directory, where the project file MQPROJ is located.

## Shared projects [#](projects#shared)

MetaEditor allows programmers to remotely develop MQL5 applications in teams. The [MQL5 Storage](/en/docs/mt5/metaeditor/mql5storage) online repository is integrated into the editor:

-   Version support allows you to see all changes made to the project and revert them if necessary.
-   Online access to the project ensures access for all project members from any computer, using the [MQL5.community](https://www.mql5.com/ "MQL5.community") account.
-   Project update notifications — stay updated of all changes in project files or settings. To receive notifications on your mobile phone, specify your [MetaQuote ID](https://www.mql5.com/en/articles/476) under the "Settings \\ Security" section of your MQL5.community profile. To communicate with the team, use [group chats](https://www.mql5.com/en/articles/8586).
-   You can grant separate rights to project participants allowing to view or to edit the project.
-   You can also create [public projects](/en/docs/mt5/metaeditor/projects#public), which are visible to all users. Public projects are displayed in a separate tab in MetaEditor, from which anyone can apply for participation.

Shared projects are managed from a separate Shared Projects section. If you have not activated Storage yet, execute the Activate MQL5 Storage command from the context menu of the desired folder. MetaEditor will check if your storage contains any saved data and if there are any shared projects available to you. All available data will be retrieved from Storage and uploaded to your computer. Available group projects appear in the Shared Projects section. To retrieve the projects, execute Checkout from Storage in the context menu.

To create a new group project, select the Shared Projects folder and click New Project:

![Creating a shared project](/en/docs/mt5/metaeditor/img/project_new.png "Creating a shared project")

Then complete standard MQL5 steps: set the type, name and properties of the desired program. For group projects, you should use clear and understandable names, so that other participants could easily find them. Only Latin letters and numbers without spaces can be used in project names.

A created project is immediately added to the MQL5 Storage. [Standard Library](https://www.mql5.com/en/docs/standardlibrary) files used in the project are not added to the storage, and you can add them manually.

To allow other participants to work with the project, open the project properties. You can grant permissions to selected users and set general parameters for the team work:

-   A private project is only available to the author
-   A free to join project allows anyone to join it
-   A join by request project can be accessed after sending a request to the author

![Configuring access to the shared project](/en/docs/mt5/metaeditor/img/project_settings.png "Configuring access to the shared project")

To grant permissions to a selected user, click on "add new user" and specify the MQL5.community login of this user. Then select permissions:

-   Read: the user can see the project data and will be able to download to his or her MetaEditor.
-   Read and Write: the user can see the project data, as well as upload his or her own changes to Storage, but cannot change the list of participants.

<table class="attentable" cellspacing="0" cellpadding="8" border="1"><tbody><tr class="attentable"><td class="attentable"><p class="p_tableatten"><span class="f_tableatten">When you compile a group project, the executable EX5 file is automatically copied to the local Experts, Indicators or Scripts directory depending on the program type. It allows you to instantly run the program in the platform without having to copy it manually to the proper directory.</span></p></td></tr></tbody></table>

## Public projects [#](projects#public)

Each [shared project](/en/docs/mt5/metaeditor/projects#shared) in MQL5 Storage has publicity settings: the project can be private or open to other users. All projects that you can join are displayed in the separate Public Projects tab.

![Public projects](/en/docs/mt5/metaeditor/img/project_public.png "Public projects")

Click Join in order to join a project. After that the project will appear in the Shared Projects section. Then click ![Update from Storage](/en/docs/mt5/metaeditor/img/mql5storage_update_icon.png "Update from Storage") Update from Storage in the context menu of the project in order to download it to your computer.

Each joined user gets read-only rights. Contact the project author to be able to submit your changes. To know his or her MQL5.community login, open the project properties via the context menu:

![Viewing the project properties](/en/docs/mt5/metaeditor/img/project_settings_view.png "Viewing the project properties")

[Enabling the Storage](/en/docs/mt4/metaeditor/mql5storage_connect)

[Working with Storage](/en/docs/mt4/metaeditor/mql5storage_working)