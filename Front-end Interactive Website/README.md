# Front-end Interactive Website

## Description
This is the website we developed to allow a user to interact with one of our best models for heart disease prediction.

The website is meant to be run locally and was developed using Flask, the Python-based web framework.

## Setup instructions
In order to get the website up and running on your local machine, you'll need to have a few things installed. Most importantly
among these is Python, since both the website and the model used for predictions were programmed in Python.

Once you have Python installed, you'll also need to have a few Python packages installed as well. Most importantly, you'll need
Flask, which is the framework on top of which the website runs. In addition, you'll need scikit-learn, which was the library used
to construct our final classification model. You'll also need pickle, which was the library used to save and load the model as a file.
To install these packages, you could run commands similar to the following:

    pip install flask
    pip install scikit-learn
    pip install pickle

To actually run the website locally, you must first navigate to this folder (i.e., the folder containing app.py) via command line.
From here, you can start up the website with the following command:

    flask run

If you did not install Flask as a globally recognized program, and instead only installed it as a Python module, you can run the
following command instead:

    python -m flask run

Once the local web server is up and running, it should print out a message like the one below:

    * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

Following the link in that message will take you to the locally-running website.

## Using the website
Once you are on the website, you can simply fill out the form located at the top of the website, under the "Interact" section.
Once you have done this, you can click the "Enter" button located just below the form, and the website will be reloaded. Below
the "Enter" button, a message will appear telling you whether or not our machine learning model predicts that you have heart disease,
based on the information that you entered in the form.

You can also feel free to scroll down below the "Interact" section and read some information regarding our project and the models
we developed for it. Note that this information is not as detailed as our group's project report.
