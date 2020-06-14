from flask import Flask, jsonify
from matplotlib import pyplot as plt
import numpy as np
import time

from plot import *
from question import *


app = Flask(__name__)

q = Question()

@app.route("/")
def index():
    # return("test")
    return {"time": time.time()}


if __name__ == "__main__":
    app.run(debug=True)
