# Import dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import numpy as np

# Create engine to connect with database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs <br>"
        f"/api/v1.0/start_date <br> "
        f"/api/v1.0/end_date <br> "
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(measurement.date >= "2016-08-23").\
        filter(measurement.date <= "2017-08-23").all()   

@app.route("/api/v1.0/stations")
def stations():
    results = session.query(station.station).all()
    station_list = list(np.ravel(results))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    results = session.query(measurement.tobs).\
        filter(Measurement.date >= "2016-08-23").\
        filter(Measurement.date <= "2017-08-23").all()
    tobs_list = list(np.ravel(results))
    return jsonify(tobs_list)
    
    
    precipitation_dict = []
        for row in results:
        date_dict = {}
        date_dict[row.date] = row.prcp
        precipitation_dict.append(date_dict)
    return jsonify(precipitation_dict)

if __name__ == '__main__':
    app.run(debug=True)