from flask import Blueprint, request
from api import db
import bson

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

#Retreive one item based on _id
@itemBlueprint.route("/get",methods=["POST"])
def get_item():
    data = request.json
    id = data["_id"]
    print(id)
    try:
        item = db.Items.find_one({'_id':bson.ObjectId(oid=str(id))})
    except Exception:
        print (Exception)
    return item

    