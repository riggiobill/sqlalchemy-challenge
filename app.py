## imported skeletal text from older code


from flask import Flask

app = Flask(__name__)


## see: app w/ querying notes
##

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

@app.route("/precipitation")
def about():
    name = ""
    current_location = ""
    return f"{name} {current_location}"

@app.route("/stations")
def contact():
    email = ""
    return "" + email

@app.route("/<start>")
def contact():
    
    return ""

@app.route("/<start>/<end>")
def contact():
    
    return ""



if __name__ == "__main__":
    app.run(debug=True)