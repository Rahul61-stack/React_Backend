from flask import Blueprint, request
from api import db

itemBlueprint = Blueprint("item", __name__)

#Add one item
@itemBlueprint.route("/add",methods=["POST"])
def add_item():
    data = request.json
    db.Items.insert_one(data)
    return "Item added Successfully"

#List all items
@itemBlueprint.route("/list",methods=["GET"])
def list_items():
    items = list(db.Items.find())
    return items

    