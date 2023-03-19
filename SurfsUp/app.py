from flask import Flask, jsonify
import pandas as pd
app = Flask(__name__)

ly_df = pd.read_csv("last_year.csv")


def last_year_to_obj():
    ly_obj = ly_df.set_index("date")["prcp"].to_dict()
    return ly_obj    


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
        f"/api/v1.0/<start>/<br/>"
        f"/api/v1.0/<start>/<end>/<br/>"
        )
        

@app.route("/api/v1.0/precipitation")
def nothome():
    # Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    last_year_prcp =last_year_to_obj()
    # Return the JSON representation of your dictionary.
    return jsonify(last_year_prcp)

@app.route("/api/v1.0/stations")
def somthing():
    # Return a JSON list of stations from the dataset.
    return jsonify(list(ly_df["station"].unique()))
    pass

@app.route("/api/v1.0/tobs")
def waitasecond():
    # Query the dates and temperature observations of the most-active station for the previous year of data.
    # Return a JSON list of temperature observations for the previous year.
    pass

@app.route("/api/v1.0/<start>")
def noway(start):
    # Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.
    pass

@app.route("/api/v1.0/<start>/<end>")
def holup():
    pass


if(__name__=="__main__"):
    app.run(debug=True)




# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

# Hints
# Join the station and measurement tables for some of the queries.

# Use the Flask jsonify function to convert your API data to a valid JSON response object.