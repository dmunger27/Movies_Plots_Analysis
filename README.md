Movies Reviews and Ratings Analysis
==============================

# Collaborators 

- [Jimmy Nguyen](https://github.com/jimmy-nguyen-data-science)
- [Dallin Munger](https://github.com/dmunger27)
- Tyler Wolff

# Final Project Objective

Build a machine learning based application that can classify the genre of any movie based on a summary/synopsis of a movie. The goal is to build a highly-accurate classification model that will be able to classify a plot summary into five distinct categories: animation, action, comedy, documentary, and drama. Lastly, build a topic model to fully understand the structure of a plot summary for more insights for each word.

# Data set Description

Data source comes from pulling the data from OMDB's API. The estimate size of the data set may be close to 5,000 movie descriptions or less. The total number of variables is 15 for now from the raw data set. This includes the movie title, genre, IMDB rating, and the movie plot summary. However, upon data preparation and cleaning, the number of dimensionality may increase exponentially due to TF-IDF transformations.

# Application 

Live demo of the application can be found here: https://movie-plot-classification.herokuapp.com/ 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    │
    │
    ├── flask_app          <- Folder for our deployment code with Flask and Heroku
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
