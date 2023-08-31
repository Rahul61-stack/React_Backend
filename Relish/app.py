from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import json_util

app = Flask(__name__)
app.config['MONGO_URI'] =  'mongodb+srv://rahulsrivastav400:y0ApyM5aRyYXANwE@clusterx7.kw8zg9h.mongodb.net/Relish'
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'
localhost = 'http://localhost:3000'
cors = CORS(app, resources={r'/add/customer': {"origins": localhost},r'/get/customers':{"origins": localhost}})
mongo = PyMongo(app)
@app.route('/add/customer', methods=['POST'])
def add_customer():
    data = request.json
    print(data)
    mongo.db.Customers.insert_one(data)
    return 'Data Added Successfully'
@app.route('/get/customers', methods=['GET'])
def read_records():
    records = list(mongo.db.Customers.find())
    print(records)
    return jsonify(json_util.dumps(records))
if __name__ == "__main__":
    app.run(debug = True)