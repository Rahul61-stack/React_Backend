from flask import Blueprint, request
from api import db

customerBlueprint = Blueprint("customer", __name__)


@customerBlueprint.route("/add", methods=["POST"])
def add_customer():
    data = request.json
    print(data)
    db.Customers.insert_one(data)

    return "Data Added Successfully"


@customerBlueprint.route("/get", methods=["GET"])
def read_records():
    records = list(db.Customers.find())
    print(records)
    # return jsonify(json_util.dumps(records))

    return records
