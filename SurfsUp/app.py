from flask import Flask, jsonify
import pandas as pd
app = Flask(__name__)

pageList = ["/api/v1.0/precipitation","/api/v1.0/stations","/api/v1.0/tobs","/api/v1.0/<start>","/api/v1.0/<start>/<end>"]
ly_df = pd.read_csv("last_year.csv")


def last_year_to_obj():
    ly_obj = ly_df.set_index("date")["prcp"].to_dict()
    return ly_obj    


@app.route("/")
def home():
    print("YOLO CHOLO")
    # Start at the homepage.
    # List all the available routes.
    return jsonify(pageList)

@app.route("/api/v1.0/precipitation")
def nothome():
    # Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value.
    # Return the JSON representation of your dictionary.
    return jsonify(last_year_to_obj())

@app.route("/api/v1.0/stations")
def somthing():
    stations = ly_df["station"].unique()
    return jsonify(stations)
    # Return a JSON list of stations from the dataset.
    pass

@app.route("/api/v1.0/tobs")
def waitasecond():
    # Query the dates and temperature observations of the most-active station for the previous year of data.
    # Return a JSON list of temperature observations for the previous year.
    pass

@app.route("/api/v1.0/")
def noway():
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