from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from random import *
import math

from math_funcs import *


def format_plot_axes(ax):
    axes_map = {"left": "zero", "bottom": "zero", "right": "none", "top": "none"}

    ax.spines["left"].set_position(axes_map["left"])
    ax.spines["bottom"].set_position(axes_map["bottom"])
    ax.spines["right"].set_color(axes_map["right"])
    ax.spines["top"].set_color(axes_map["top"])
    ax.xaxis.set_ticks_position("bottom")
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_ticks_position("left")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    xmin, xmax = (-12, 12)
    ymin, ymax = (-12, 12)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)


def create_subplots(num_plots):
    sqrt = math.sqrt(num_plots)
    size = (10, 10)
    fig, axs = plt.subplots(int(sqrt), int(sqrt), figsize=size)
    for row in axs:
        for ax in row:
            format_plot_axes(ax)
    return fig, axs


def create_parabola(x, coeffs, ax):
    ax.plot(x, f(x, coeffs))


def create_full_grid(x, coeffs, axs):
    all_possible = [(0, 0), (0, 1), (1, 0), (1, 1)]
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
