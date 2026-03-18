# Working with machine learning models

> Source: https://support.metaquotes.net/en/docs/mt4/metaeditor/machine_learning

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

[MetaTrader 4](/en/docs/mt4)[MetaEditor](/en/docs/mt4/metaeditor)Working with machine learning models

# Working with machine learning models

The MQL5 language supports operations with [ONNX](https://en.wikipedia.org/wiki/Open_Neural_Network_Exchange) (Open Neural Network Exchange) models. ONNX is an open-source format for machine learning models. This format is supported by many platforms, including [Chainer](https://chainer.org/), [Caffee2](https://caffe2.ai/) and [PyTorch](https://pytorch.org/). Create an ONNX model using specialized tools, integrate it into your MQL5 application and use it to make trading decisions. Descriptions of all supported functions are available in the [MQL5 Documentation](https://www.mql5.com/ru/docs/onnx).

## View models in MetaEditor [#](machine_learning#onnx)

You can view the contents of the ONNX model file (\*.onnx) directly in the editor. As an example, find the project ONNX.Price.Prediction under [Toolbox \\ Public Projects](/en/docs/mt5/metaeditor/projects#public) and select Join in the context menu. The project will be downloaded to your computer and will appear in the Navigator.

![Open ONNX models directly in MetaEditor](/en/docs/mt5/metaeditor/img/onnx_view.png "Open ONNX models directly in MetaEditor")

## View models in Netron [#](machine_learning#netron)

[Netron](https://github.com/lutzroeder/netron) is a specialized viewer for ML models which enables the convenient visualization of their content. It supports popular models, including ONNX, TensorFlow Lite, Caffe, Keras and ncnn, among others.

To view a model, select its file in the Navigator and click "Open in Netron". If this utility is not installed, its [GitHub page](https://github.com/lutzroeder/netron/releases) will open, from which you can download the relevant installer, according to your operating system. For example, use Netron-Setup-X.X.X.exe for Windows. If the program is installed, the model will immediately open for viewing from the Navigator.

![Visualize machine learning models with Netron](/en/docs/mt5/metaeditor/img/onnx_netron.png "Visualize machine learning models with Netron")

Supported formats:

-   armnn, caffemodel, circle, ckpt, cmf, dlc, dnn, h5, har, hd5, hdf5, hn, keras, kmodel,
-   lite, mar, meta, mge, mlmodel, mlnet, mlpackage, mnn, model, nb, ngf, nn, nnp,
-   om, onnx, ort, paddle, param, pb, pbtxt, pdiparams, pdmodel, pdopt, pdparams, prototxt, pt, pth, ptl,
-   rknn, t7, tfl, tflite, tmfile, tm, tnnproto, torchscript, uff, xmodel

[Working with SQL data bases](/en/docs/mt4/metaeditor/database)

[Example of developing a program](/en/docs/mt4/metaeditor/project_example)