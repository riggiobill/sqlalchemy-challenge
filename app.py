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







@app.route("/")
def home():
    return (
        f"Welcome to SQLAlchemy Challenge API!<br/>"
        f"Available Routes:<br/>"
        f" '/' :                home<br/>"
        f" '/precipitation' :   returns DICT of query results as Date:Prcp<br/>"
        f" '/stations' :        returns JSON list of stations<br/>"
        f" '/start' :           returns JSON list of temp observation after a certain date<br/>"
        f" '/start/end' :       returns JSON list of temp observation between two dates<br/>"
        f""
    )




##basically, the below are each the same calls as the other portion of the homework
##pull from that and it'll be done in no time.

@app.route("/precipitation")
def precipitation():
    """Return a dictionary including Date and Precipitation in a JSON DICT format"""
    session = Session(engine)
   
    # Query all date/precipitation info
    results = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_prcp
    all_prcp = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)

@app.route("/stations")
def stations():
    """Return a JSON list of all stations from the dataset"""
    session = Session(engine)
   
    # Query all date/precipitation info
    results = session.query(Station.name).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_prcp
    all_station = []
    for station in results:
        station_dict = {}
        station_dict["station"] = station
        all_station.append(station_dict)

    return jsonify(all_station)

@app.route("/<start>")
def start():
    
    return ""

@app.route("/<start>/<end>")
def startend():
    
    return ""



if __name__ == "__main__":
    app.run(debug=True)