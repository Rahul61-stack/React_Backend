"""
Flask imports
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

"""
Utility Libraries
"""
import configparser
import json
from datetime import datetime
import time
from bson import json_util
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


def init_app():
    app = Flask(__name__)
    CORS(app)

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

        app.register_blueprint(customer.customerBlueprint, url_prefix="/users")

    return app
