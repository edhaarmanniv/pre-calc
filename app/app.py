from flask import Flask, jsonify, redirect
from matplotlib import pyplot as plt
from random import choice
import numpy as np
import time
import pymongo

from .question import *

client = pymongo.MongoClient(os.getenv("CONN"))
db = client.mathQuestions
db.abc_questions.drop()
db.hk_questions.drop()

arbitrary_id = {"_id":0}

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/new_question")

@app.route("/new_question")
def new_question():
    q = Question()
    db.abc_questions.update_one(arbitrary_id, {"$set":q.create_question_abc()}, upsert=True)
    db.hk_questions.update_one(arbitrary_id, {"$set":q.create_question_hk()}, upsert=True)
    return redirect(choice(["/get_abc", "/get_hk"]))

@app.route("/get_abc")
def get_abc_question():
    return db.abc_questions.find_one(arbitrary_id)

@app.route("/get_hk")
def get_hk_question():
    return db.hk_questions.find_one(arbitrary_id)
    

if __name__ == "__main__":
    app.run(debug=True)
