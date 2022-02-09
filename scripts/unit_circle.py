"""
Plots for the transforms 01 lecture

Useful links:
Arcs : https://stackoverflow.com/a/54850819/10188737
"""

# %%

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

from utils import *
set_style()

# %%


def angle_arrow(ax):
    style = "Simple, tail_width=0.5, head_width=4, head_length=8"
    kw = dict(arrowstyle=style, color="k")
    a = FancyArrowPatch((3, 0), (2, 2),
                        connectionstyle="arc3,rad=.2", **kw)
    ax.text(3.5, 1, r"$\theta$", ha="center", va="center", fontsize=10)
    ax.add_patch(a)


def hypot(ax, radius=10, theta=np.pi / 4,):
    x = [0, radius * np.cos(theta)]
    y = [0, radius * np.sin(theta)]
    green = (0.1, 0.5, 0)
    grey = (0.5, 0.5, 0.5)
    ax.plot(x, y, 'b-', lw=1, zorder=10, clip_on=False)
    ax.plot(x, [0, 0], 'r-', lw=1, zorder=10, clip_on=False)
    ax.plot([0, 0], y, '-', color=green, lw=1, zorder=10, clip_on=False)
    ax.plot([x[1], x[1]], y, '--', color=grey, lw=1,)
    ax.plot(x, [y[1], y[1]], '--', color=grey, lw=1,)
    ax.text(-1, y[1]/2, "y", fontsize=10, color=green)
    ax.text(x[1]/2, -1, "x", color='r', fontsize=10)
    ax.text(x[1]/2, y[1]/2 + 1, 'r', color='b', fontsize=10)


def circle(ax, radius=10):
    a = Ellipse((0, 0), 2*radius, 2*radius,
                0, facecolor=(1, 1, 1, 0), edgecolor='k', lw=1)
    ax.add_patch(a)


# %%

radius = 14

fig, ax = plt.subplots(1, 1)
circle(ax, radius=radius)
set_spines(ax, (-15, 15), (-15, 15))
angle_arrow(ax)
hypot(ax, radius=radius)
ax.grid(False)
fig.savefig("unit_circle.png")
