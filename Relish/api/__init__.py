"""
Flask imports
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask.json.provider import JSONProvider

"""
Utility Libraries
"""
import configparser
import json
from datetime import datetime
import time
from bson.json_util import ObjectId
from pymongo import MongoClient
from utilities import *


"""
Config Setup
"""
config = configparser.ConfigParser()
config.read("config.ini")
dbConfig = config["DB"]

client = MongoClient(
    generateMongoConnectionString(
        dbConfig["username"],
        dbConfig["password"],
        dbConfig["url"],
        dbConfig["db"],
    )
)
db = client[dbConfig["db"]]
print("CONNECTED DB: ", client.list_database_names())


class BSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(BSONEncoder, self).default(obj)


class BSONProvider(JSONProvider):
    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, cls=BSONEncoder)

    def loads(self, s, **kwargs):
        return json.loads(s, **kwargs)


def init_app():
    app = Flask(__name__)
    CORS(app)
    # app.json_provider_class = BSONProvider
    app.json = BSONProvider(app)

    @app.route("/serverrunningstatus", methods=["GET"])
    def checkWorkingStatus():
        startTime = time.time()
        return {
            "code": 200,
            "status": "online",
            "ping": time.time() - startTime,
        }

    with app.app_context():
        from .customer import customer
        from .items import items
        app.register_blueprint(customer.customerBlueprint, url_prefix="/customer")
        app.register_blueprint(items.itemBlueprint,url_prefix = "/item")
    return app
