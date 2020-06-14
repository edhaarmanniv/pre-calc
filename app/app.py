from flask import Flask, jsonify, redirect
from matplotlib import pyplot as plt
import numpy as np
import time
import pymongo

# from plot import *
from question import *

CONN = "mongodb://localhost:27017"
client = pymongo.MongoClient(CONN)
db = client.mathQuestions

arbitrary_id = {"_id":0}

app = Flask(__name__)

@app.route("/time")
def index():
    # return("test")
    return {"time": time.time()}

@app.route("/new_question")
def new_question():
    q = Question()
    db.abc_questions.update_one(arbitrary_id, {"$set":q.create_all_options_abc()}, upsert=True)
    db.hk_questions.update_one(arbitrary_id, {"$set":q.create_all_options_hk()}, upsert=True)
    return jsonify("1")

@app.route("/get_abc")
def get_abc_question():
    return db.abc_questions.find_one(arbitrary_id)

@app.route("/get_hk")
def get_hk_question():
    return db.hk_questions.find_one(arbitrary_id)

if __name__ == "__main__":
    app.run(debug=True)

