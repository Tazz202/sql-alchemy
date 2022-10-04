import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

###########  The following code is nearly identical to Day 3 Activity 10 
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
Base.classes.keys()
# Save references to each table
######  There are 2 tables in the db
measurement=Base.classes.measurement
station=Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
###### Everything you need here can be found in Day 3 Activity 10
@app.route("/")
def welcome():
    return (

    )

###### the 'precipitation' route you will query and return the data Day 3 Activity 10
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    # Calculate the date 1 year ago from last date in database

    last_year_date=dt.date(2017, 8, 23) - dt.timedelta(days=366)
    print(last_year_date)

    # Query for the date and precipitation for the last year

    last_year_date_prcp_values=session.query(measurement.date, measurement.prcp, measurement.station).\
        filter(measurement.date >= last_year_date).\
        filter(measurement.prcp).all()

    # Dict with date as the key and prcp as the value
    lista = []
    for date, precip, stat in last_year_date_prcp_values:

        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = precip
        prcp_dict["station"]=stat
        lista.append(prcp_dict)
        jsonify(list)

###### the 'stations' route you will query and return the data Day 3 Activity 10
@app.route("/api/v1.0/stations")
def stations():
#     """Return a list of stations."""
    station_list=session.query(station.station).all()
    # Unravel results into a 1D array and convert to a list
    list2 = []
    for x in station_list:
        station_dict = {}
        station_dict["station"] = station
        list.append(station_list)
        return jsonify(list2)

###### the 'tobs' route you will query and return the data Day 3 Activity 10
@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations (tobs) for previous year."""
    # Calculate the date 1 year ago from last date in database


    # Query the primary station for all tobs from the last year

    # Unravel results into a 1D array and convert to a list


    # Return the results


###### the 'temp' route you will query the data with params in the url and return the data Day 3 Activity 10
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start=None, end=None):
    """Return TMIN, TAVG, TMAX."""

    # Select statement


    # calculate TMIN, TAVG, TMAX with start and stop


    # Unravel results into a 1D array and convert to a list



if __name__ == '__main__':
    app.run()
