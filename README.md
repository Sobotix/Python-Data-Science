#Python Data Science

Multiple datasets are included as this code works with any dataset given. From left navigation panel switch to home panel, from there load as many datasets as you like using load button. From this menu you can mange user-defined variables as well, user-defined variables support many functionalities like holding different chunks or totatally different datasets. Other menues include Assign, Visualization, Data Munging and Prediction.

Suggested dataset: train_dataset.csv for normal usage and missing_dataset for data munging related tasks

-------------------------------------------------------
Dependencies are to be resolved manually, as __setup__.py file is not there.

Dependencies:
    pandas
    numpy
    sklearn
    wx
    matplotlib

On the bright side GUI is using tkinter
-----------------------------------------------------------
This project consits of different modules, for execcuting the program run the source.py file

Suggested method: from comandline execute following command:

python source.py
-------------------------------------------------------------
Project structure:

    core.py contains core logic of datascience functionality this app supports
    gui.py is all about user interface
    visualizer.py is for display dataframe etc
    pages package contain different pages
        assign_page.py
        home_page.py
        data_munging_page.py
        visualization_page.py
        prediction_page.py
        page.py
        __init__.py
    images
    LICENSE
    README.md
    Sample datasets

Execution starts from source.py and it is then delegated to gui.py which calls different methods of core.py