from flask import Blueprint, request
from api import db

customerBlueprint = Blueprint("customer", __name__)

"""
ADD ONE CUSTOMER API

"""


@customerBlueprint.route("/add", methods=["POST"])
def add():
    data = request.json
    db.Customers.insert_one(data)

    return {
        "status": "customer data added",
    }


"""
LIST ALL CUSTOMERS API

"""


@customerBlueprint.route("/list", methods=["GET"])
def _list():
    records = list(db.Customers.find())

    return records


"""
FILTER CUSTOMERS API

expected schema: 
{
    ...
}
"""


@customerBlueprint.route("/filter", methods=["POST"])
def filter():
    filters = request.json
    records = list(db.Customers.find(filters))

    return records


"""
FETCH ONE CUSTOMER API

expected schema: 
{
    "email": "..."
}
"""


@customerBlueprint.route("/get", methods=["POST"])
def get():
    data = request.json
    customer = db.Customers.find_one(data)
    if customer:
        return "Exists"
    else:
        return "0"


"""
UPDATE ONE CUSTOMER API

expected schema: 
{
    "email": "...",
    "updates": {
        ...
    }
}
"""


@customerBlueprint.route("/update", methods=["POST"])
def update():
    data = request.json

    identifier = {"email": data.get("email")}
    updates = data.get("updates")

    result = db.Customers.update_one(
        identifier,
        updates,
    )

    return {
        "status": "customer data updated",
        "returnedObject": result.acknowledged,
    }
