from flask import Flask, render_template
import json
from firebase import firebase
app = Flask(__name__)

# STEP 1: Replace db_url string with your own URL to firebase database
db_url = "https://blinding-heat-2796.firebaseio.com"
firebase = firebase.FirebaseApplication(db_url, authentication=None)

data = [{
	"id": 1,
	"name": "Eat Breakfast",
	"minutes": 30
},
{
	"id": 2,
	"name": "Workout",
	"minutes": 60
},
{
	"id": 3,
	"name": "Go to work",
	"minutes": 30
},{
	"id": 4,
	"name": "Be lazy at work",
	"minutes": 240
},
{
	"id": 5,
	"name": "Continue being lazy at work",
	"minutes": 240
},
{
	"id": 6,
	"name": "Drive home",
	"minutes": 30
},
{
	"id": 7,
	"name": "Work on interesting Sitepoint article",
	"minutes": 30
},
{
	"id": 8,
	"name": "Sleep",
	"minutes": 480
}]


result = firebase.put('/', 'test_data', data)

@app.route("/")
def index():
	data = firebase.get('/test_data', None)
	print(data)

	return render_template("index.html", data=json.dumps(data))

@app.route("/load_products/", methods=["GET"])
def load_products():
	# Use the global variable "data", defined above, in this example
	print("at load products")
	return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)