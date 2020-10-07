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
        f" '/tobs' :            returns JSON DICT of TOBS for most active station for previous year<br/>"
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

@app.route("/tobs")
def tobs():
    """Query the Date and Temperature Observation from the most active station for the last year"""
    session = Session(engine)
    query_date = dt.date(2017,8,23)-dt.timedelta(days=365)
    station_id_max = 'USC00519281'
    # Query all date/precipitation info
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date>=query_date).filter(Measurement.station==station_id_max).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_prcp
    all_tobs = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_tobs.append(tobs_dict)

    return jsonify(all_tobs)
    

@app.route("/<start>")
def start(start):
    """Query the Min, Avg, and Max Temperatures in a given range"""
    session = Session(engine)
    query_date = start
    
    # Query all date/precipitation info
    results = session.query(Measurement.tobs, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date>=query_date).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_prcp
    all_start = []
    for tobs, min, max, avg in results:
        start_dict = {}
        start_dict["Tobs"] = tobs
        start_dict["Min"] = min
        start_dict["Avg"] = avg
        start_dict["Max"] = max
        all_start.append(start_dict)

    return jsonify(all_start)


@app.route("/<start>/<end>")
def startend(start,end):
    """Query the Min, Avg, and Max Temperatures in a given range"""
    session = Session(engine)
    query_date1 = start
    query_date2 = end
    
    # Query all date/precipitation info
    results = session.query(Measurement.tobs, func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date>=query_date1).filter(Measurement.date<=query_date2).all()
    session.close()

    # Create a dictionary from the row data and append to a list of all_prcp
    all_start = []
    for tobs, min, max, avg in results:
        start_dict = {}
        start_dict["Tobs"] = tobs
        start_dict["Min"] = min
        start_dict["Avg"] = avg
        start_dict["Max"] = max
        all_start.append(start_dict)

    return jsonify(all_start)



if __name__ == "__main__":
    app.run(debug=True)