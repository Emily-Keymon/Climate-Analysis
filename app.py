##################################################
# Step 2 - Climate App
# Design a Flask API based on the queries developed
# Use Flask to create routes

##################################################
# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

##################################################
# Database Setup
# Create engine
engine = create_engine("sqlite:///hawaii.sqlite", connect_args={'check_same_thread': False})

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

##################################################
# Flask Setup
app = Flask(__name__)


##################################################
# Routes

##################################################
# Home page, list all routes available
@app.route("/")
def home_page():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"<br>"
        f"Available routes are as follows:<br/>"
        f"<br>"
        f"/api/v1.0/precipitation<br/>"
        f" The precipitation route returns precipitation from 8/23/16 to 8/23/17<br/>"
        f"<br>"
        f"/api/v1.0/stations<br/>"
        f" The stations route returns a list of station numbers that collected the measurements<br/>"
        f"<br>"
        f"/api/v1.0/tobs<br/>"
        f" The tobs route uses the station with the  highest number of observations to return the temperature "
        f"observations (tobs) for previous year<br/>"
        f"<br>"
        f"/api/v1.0/temp/start/end"
        f"<br>"
        f" The temp start date end date route returns the minimum temperature, the average temperature, and the max "
        f"temperature for a given start-end date range<br/>"
        f"Enter trip start and end dates in yyyy-mm-dd format for results")


##################################################
# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year from the last date in database (2017-08-23)
    previous_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation results
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= previous_year).all()

    # Convert query results to a dictionary using date as the key and prcp as the value
    # Return the JSON representation of the dictionary
    precip = {date: prcp for date, prcp in results}
    return jsonify(precip)


##################################################
# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Design a query to calculate the total number of stations
    locations = session.query(Station.station).all()

    # Return a JSON list of stations from the dataset
    stations = list(np.ravel(locations))
    return jsonify(stations=stations)


##################################################
# TOBS route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    # Calculate the date one year from the last date in database (2017-08-23)
    previous_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the dates and temperature observations (tobs) of the most active station for the least year of data
    # Most active station is USC00519281
    results = session.query(Measurement.tobs). \
        filter(Measurement.station == 'USC00519281'). \
        filter(Measurement.date >= previous_year).all()

    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))

    # Return a JSON list of temperature observations (tobs) for the previous year
    return jsonify(temps=temps)


##################################################
# Temp start/end date route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def temp_range(start, end):
    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # When given start date only, calculate TMIN, TAVG, TMAX for all dates greater than or equal to the start date
        results = session.query(*sel). \
            filter(Measurement.date >= start).all()

        # Unravel results into a 1D array and convert to a list
        temps = list(np.ravel(results))

        # Return a JSON list of minimum, average and max temperatures for the start date chosen
        return jsonify(temps)

    #  When given start and end dates, calculate TMIN, TAVG, TMAX for dates between the start and end date inclusive
    results = session.query(*sel). \
        filter(Measurement.date >= start). \
        filter(Measurement.date <= end).all()

    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))

    # Return a JSON list of minimum, average and max temperatures for the date range chosen
    return jsonify(temps=temps)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
