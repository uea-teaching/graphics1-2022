"""
Plots for the transforms 03 lecture

Useful links:
Arcs : https://stackoverflow.com/a/54850819/10188737
"""

# %%

import numpy as np
import matplotlib.pyplot as plt

from utils import *
set_style()
plt.rcParams['figure.figsize'] = [6.0, 5.0]

FILL1 = (0.5, 0.0, 0.5, 0.5)
FILL2 = (0.0, 0.5, 0.5, 0.5)
FILL3 = (0.5, 0.5, 0.0, 0.5)
STROKE = (0.0, 0.0, 0.0, 1.0)


# %%

# square homogeneous coordinates
square = np.array([
    [-0.5, -0.5, 1], [0.5, -0.5, 1],
    [0.5, 0.5, 1], [-0.5, 0.5, 1]]).T
square.shape

# %%


def plot_rect(ax, rect, col=FILL1):
    """plot a rectangle"""
    ax.fill(rect[0], rect[1], facecolor=col, edgecolor=STROKE, linewidth=1)


# start
fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 6), y_range=(-1, 6))
plot_rect(ax, square)
ax.grid(False)
ax.text(-1.5, 0, '$s$', verticalalignment="center", fontsize=14, color='k')


# %%

def scale_xy(x=1, y=1):
    """scale the x and y axes"""
    return np.array([[x, 0, 0],
                     [0, y, 0],
                     [0, 0, 1]])


def trans_xy(x=0, y=0):
    """transform the x and y axes"""
    return np.array([[1, 0, x],
                     [0, 1, y],
                     [0, 0, 1]])


def R(a):
    """Rotation matrix"""
    rad = a / 180 * np.pi
    return np.array([[np.cos(rad), -np.sin(rad), 0],
                     [np.sin(rad), np.cos(rad), 0],
                     [0, 0, 1]])


# %%

a, b, c, alpha, beta = 2, 3, 2, 30, 45

# %%

# gantry
gantry = trans_xy(y=a/2) @ scale_xy(y=a) @ square.copy()

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 6), y_range=(-1, 6))
plot_rect(ax, gantry)
ax.grid(False)


# %%

# link1
link1 = (trans_xy(y=a)
         @ R(alpha)
         @ trans_xy(x=b / 2)
         @ scale_xy(x=b)
         @ square.copy())

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 6), y_range=(-1, 6))
plot_rect(ax, link1, col=FILL2)
ax.grid(False)

# %%

# link2
link2 = (trans_xy(y=a)
         @ R(alpha)
         @ trans_xy(x=b)
         @ R(beta)
         @ trans_xy(x=c / 2)
         @ scale_xy(x=c)
         @ square.copy())

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 6), y_range=(-1, 6))
plot_rect(ax, link2, col=FILL3)
ax.grid(False)

# %%

fig, ax = plt.subplots(1, 1)
set_spines(ax, x_range=(-1, 6), y_range=(-1, 6))
plot_rect(ax, gantry)
plot_rect(ax, link1, col=FILL2)
plot_rect(ax, link2, col=FILL3)
ax.grid(False)
# %%
