from flask import Flask
from matplotlib import pyplot as plt
import numpy as np
import time

app = Flask(__name__)

@app.route('/time')
def index():
    # return("test")
    return {'time': time.time()}

@app.route('/question'):
def parabola():
    return {}

if __name__ == "__main__":
    index()