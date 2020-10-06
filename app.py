## imported skeletal text from older code


from flask import Flask

app = Flask(__name__)





@app.route("/")
def home():
    print("")
    return ""

@app.route("/about")
def about():
    name = ""
    current_location = ""
    return f"{name} {current_location}"

@app.route("/contact")
def contact():
    email = ""
    return "" + email

if __name__ == "__main__":
    app.run(debug=True)