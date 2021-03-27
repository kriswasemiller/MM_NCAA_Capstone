from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
from modelHelper import ModelHelper
import pickle
#init app and class
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

#endpoint
# Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')
                          
# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")


# Route to render index.html template
@app.route("/about")
def about():
    # Return template and data
    return render_template("about.html")

# Route to render index.html template
@app.route("/glossary")
def glossary():
    # Return template and data
    return render_template("glossary.html")

# Route to render index.html template
@app.route("/data")
def data():
    # Return template and data
    return render_template("madnessData.html")

# Route to render index.html template
@app.route("/prediction")
def machine():
    # Return template and data
    return render_template("mLearning.html")

# Route to render index.html template
@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tabDash.html")

@app.route("/makePredictions", methods=["POST"])
def makePredictions():
    
    yr1 = 2019
    yr2 = 2018
    if (yr1 == 2021):
        avg_df_year = pd.read_csv('static/data/full_avg_2021.csv')
        gb_year = pickle.load(open('static/models/finalized_model_2021.sav', 'rb'))
    elif (yr1 == 2020):
        avg_df_year = pd.read_csv('static/data/full_avg_2020.csv')
        gb_year = pickle.load(open('static/models/finalized_model_2020.sav', 'rb'))
    elif (yr1 == 2019):
        avg_df_year = pd.read_csv('static/data/full_avg_2019.csv')
        gb_year = pickle.load(open('static/models/finalized_model_2019.sav', 'rb'))
    elif (yr1 == 2018):
        avg_df_year = pd.read_csv('static/data/full_avg_2018.csv')
        gb_year = pickle.load(open('static/models/finalized_model_2018.sav', 'rb'))
    elif (yr1 ==2017):
        avg_df_year = pd.read_csv('static/data/full_avg_2017.csv')
        gb_year = pickle.load(open('static/models/finalized_model_2017.sav', 'rb'))
    else:
        avg_df_year = pd.read_csv('static/data/full_avg_2016.csv')
        gb_year = pickle.load(open('static/models/finalized_model_2016.sav', 'rb'))
    teamA = 'ohio st.'
    if (yr2 == 2021):
        avg_df_year2 = pd.read_csv('static/data/full_avg_2021.csv')
        gb_year2 = pickle.load(open('static/models/finalized_model_2021.sav', 'rb'))
    elif (yr2 == 2020):
        avg_df_year2 = pd.read_csv('static/data/full_avg_2020.csv')
        gb_year2 = pickle.load(open('static/models/finalized_model_2020.sav', 'rb'))
    elif (yr2 == 2019):
        avg_df_year2 = pd.read_csv('static/data/full_avg_2019.csv')
        gb_year2 = pickle.load(open('static/models/finalized_model_2019.sav', 'rb'))
    elif (yr2 == 2018):
        avg_df_year2 = pd.read_csv('static/data/full_avg_2018.csv')
        gb_year2 = pickle.load(open('static/models/finalized_model_2018.sav', 'rb'))
    elif (yr2 ==2017):
        avg_df_year2 = pd.read_csv('static/data/full_avg_2017.csv')
        gb_year2 = pickle.load(open('static/models/finalized_model_2017.sav', 'rb'))
    else:
        avg_df_year2 = pd.read_csv('static/data/full_avg_2016.csv')
        gb_year2 = pickle.load(open('static/models/finalized_model_2016.sav', 'rb'))
    teamB = 'oral roberts'
    prediction = modelHelper.get_matchup(yr1, yr2, avg_df_year, teamA, gb_year, avg_df_year2, teamB, gb_year2)
    print(prediction)
    return(jsonify({"ok": True, "prediction": prediction}))

####################################
# ADD MORE ENDPOINTS
####################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=False)
