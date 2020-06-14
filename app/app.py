from flask import Flask
from matplotlib import pyplot as plt
import numpy as np
import time

from plot import *
from math_funcs import *

x = np.linspace(-10, 10, 100)
coeffs = create_coeffs()

app = Flask(__name__)

@app.route('/time')
def index():
    # return("test")
    return {'time': time.time()}

@app.route('/correct')
def correct_ans():
    return 

@app.route("/grid")
def create_full_grid(x, coeffs, axs):
    all_possible = [(0,0), (0, 1), (1, 0), (1, 1)]
    correct = decide_correct()
    
    create_parabola(x, coeffs, axs[correct[0]][correct[1]])
    
    for coord in all_possible:
        if coord != correct:
            r, c = coord
            create_parabola(x, create_wrong(coeffs), axs[r][c])
    
    titles = ["A", "B", "C", "D"]
    for i, coord in enumerate(all_possible):
        r, c = coord
        axs[r][c].set_title(titles[i], fontsize=24)
    
    return correct

if __name__ == "__main__":
    index()