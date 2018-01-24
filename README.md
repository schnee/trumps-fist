trumps-fist
==============================

Various attempts to classify Trump's tweets. In 2016, Candidate Trump used an Android to tweet and his staff used iPhones. This provides a labeled set of data that, in theory, can be used to build a model to determine who is tweeting under @realDonaldTrump.

To reproduce, install docker, and nvidia-docker (assuming a GPU). Then navigate to 'docker' and type 'make notebook'. This will build a docker container and execute Jupyter Notebook. It will also attempt to mount a filesystem from the host to the container, so data can be shared. See the Makefile, essentially
```PROJECT?="${PWD}/.."``` is defined (relative to the Makefile) and then ```-v $(PROJECT):/project``` mounts the root of 'trumps-fist' to the /project directory in the container.

Data:
Trump's tweets:
```cd data/external; wget \
https://github.com/bpb27/trump_tweet_data_archive/blob/master/condensed_2016.json.zip```

Fasttext-based wikipedia vectors (large...):
```cd data/external; wget \
https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.en.zip; unzip wiki.en.zip```


See
https://github.com/arm5077/trump-twitter-classify
https://factba.se/blog/2017/04/07/nerdwhen-occams-razor-cuts-younerd/

Tweet data from
http://www.trumptwitterarchive.com/

Project Organization
(may not be complete)
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
    |   docker             <- Based on Keras' Dockerfile and must use nvidia-docker
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
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
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience. Small changes made where appropriate (e.g. docker)</small></p>
