from flask import Flask, jsonify
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt

app = Flask(__name__)

ly_df = pd.read_csv("last_year.csv")
busy_df = pd.read_csv("busy.csv")

def last_year_to_obj():
    ly_obj = ly_df.set_index("date")["prcp"].to_dict()
    return ly_obj    

def df_from_start(start):
    session = Session(bind = engine)
    vals = session.query(Measurement).filter(Measurement.date >= start).all()
    
    print(vals[0])
    session.close()
    return pd.DataFrame.from_records([r.__dict__ for r in vals], columns=Measurement.__table__.columns.keys())

# -- SQL STUFF
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
base = automap_base()
base.prepare(autoload_with=engine)
Station = base.classes.station
Measurement = base.classes.measurement

#-- 

@app.route("/")
def home():
    print("YOLO CHOLO")
    # Start at the homepage.
    # List all the available routes.
    return (
        f"Welcome to the Hawaii API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station/<br/>"
        f"/api/v1.0/tobs/<br/>"
        f"Enter date as YYYY<br/>"
        f"/api/v1.0/<start>/<br/>"
        f"/api/v1.0/<start>/<end>/<br/>"
        )
        

@app.route("/api/v1.0/precipitation")
def nothome():
    # Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    last_year_prcp =last_year_to_obj()
    # Return the JSON representation of your dictionary.
    return last_year_prcp

@app.route("/api/v1.0/stations")
def somthing():
    # Return a JSON list of stations from the dataset.
    return jsonify(list(ly_df["station"].unique()))

@app.route("/api/v1.0/tobs")
def waitasecond():
    # Query the dates and temperature observations of the most-active station for the previous year of data.
    
    # Return a JSON list of temperature observations for the previous year.
    return busy_df.set_index("date")["tobs"].to_dict()

@app.route("/api/v1.0/<start>")
def noway(start):
    start_f = start.replace(" ", "").lower()
    from_start_df = df_from_start(start_f)
    start_stats = [from_start_df["tobs"].min(),from_start_df["tobs"].max(), from_start_df["tobs"].mean()]
    # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    return jsonify(start_stats)

@app.route("/api/v1.0/<start>/<end>")
def holup(start,end):
    start_f = start.replace(" ", "").lower()
    end_f = end.replace(" ", "").lower()
    from_start_df = df_from_start(start_f)
    to_end_df = from_start_df[from_start_df["date"] <= end_f]
    # create boolean mask for rows to be deleted
    mask = from_start_df['date'] < end_f
    # drop rows from DataFrame using the boolean mask
    to_end_df = from_start_df.drop(from_start_df[mask].index, inplace=False)
    end_stats = [to_end_df["tobs"].min(),to_end_df["tobs"].max(), to_end_df["tobs"].mean()]
    # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    return jsonify(end_stats)


if(__name__=="__main__"):
    app.run(debug=True)


# Join the station and measurement tables for some of the queries.

# Use the Flask jsonify function to convert your API data to a valid JSON response object.