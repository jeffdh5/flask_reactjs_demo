from flask import Flask, render_template
import json
from firebase import firebase
app = Flask(__name__)

db_url = "https://blinding-heat-2796.firebaseio.com/"
firebase = firebase.FirebaseApplication(db_url, authentication=None)

data = [{
	"id": 1,
	"name": "Item name 1",
	"price": 100
},{
	"id": 2,
	"name": "Item name 2",
	"price": 100
}]

result = firebase.put('/', 'test_data', data)

@app.route("/")
def index():
	data = firebase.get('/test_data', None)
	print(data)

	return render_template("index.html", data=json.dumps(data))

@app.route("/load_products/", methods=["GET"])
def load_products():
	data = [{
		"id": 1,
		"name": "Item name 1",
		"price": 100
	},{
		"id": 2,
		"name": "Item name 2",
		"price": 100
	}]
	print("at load products")
	return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)