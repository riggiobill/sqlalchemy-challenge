## imported skeletal text from older code
import numpy as np
import pandas as pd 
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

app = Flask(__name__)


## see: app w/ querying notes
##

##session engine sqlite file
##query engine in same way as other file
##save tables as classes

##create info variables for Measurement and Station to use below

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Station = Base.classes.station
Measurement = Base.classes.measurement

session = Session(bind=engine)






@app.route("/")
def home():
    return (
        f"Welcome to SQLAlchemy Challenge API!<br/>"
        f"Available Routes:<br/>"
        f" '/' : home<br/>"
        f" '/precipitation' : returns DICT of query results as Date:Prcp<br/>"
        f" '/stations' : returns JSON list of stations<br/>"
        f" '/<start>' : returns JSON list of temp observation after a certain date<br/>"
        f" '/<start>/<end>' : returns JSON list of temp observation between two dates<br/>"
        f""
    )




##basically, the below are each the same calls as the other portion of the homework
##pull from that and it'll be done in no time.

@app.route("/precipitation")
def about():

    ##query for precipitation for last 12 months
    ##as per other file
    ##instantiated as a DICT
    ##jsonify?



    name = ""
    current_location = ""
    return f"{name} {current_location}"

@app.route("/stations")
def contact():
    email = ""
    return "" + email

@app.route("/<start>")
def start():
    
    return ""

@app.route("/<start>/<end>")
def startend():
    
    return ""



if __name__ == "__main__":
    app.run(debug=True)